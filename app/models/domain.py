"""Business rules for the password generator domain layer."""

from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from enum import Enum
from typing import Final

MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 128


class PasswordStrength(str, Enum):
    """Strength categories for generated passwords."""

    WEAK = "fraca"
    MEDIUM = "média"
    STRONG = "forte"


@dataclass(frozen=True)
class PasswordPolicy:
    """Contains the rules used to generate a secure password."""

    length: int = 16
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True

    def __post_init__(self) -> None:
        """Validates the policy values."""
        if not isinstance(self.length, int):
            raise TypeError("O tamanho da senha deve ser um inteiro.")

        if not MIN_PASSWORD_LENGTH <= self.length <= MAX_PASSWORD_LENGTH:
            raise ValueError(
                "O tamanho da senha deve estar entre "
                f"{MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}."
            )

        if not any(
            (
                self.use_uppercase,
                self.use_lowercase,
                self.use_numbers,
                self.use_symbols,
            )
        ):
            raise ValueError("Selecione pelo menos um tipo de caractere.")

    def validate(self) -> None:
        """Runs validation for policy consistency."""
        if not MIN_PASSWORD_LENGTH <= self.length <= MAX_PASSWORD_LENGTH:
            raise ValueError(
                "O tamanho da senha deve estar entre "
                f"{MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}."
            )

        if not any(
            (
                self.use_uppercase,
                self.use_lowercase,
                self.use_numbers,
                self.use_symbols,
            )
        ):
            raise ValueError("Selecione pelo menos um tipo de caractere.")


@dataclass(frozen=True)
class PasswordResult:
    """Represents the generated password and its evaluated strength."""

    value: str
    strength: PasswordStrength


def build_character_pool(policy: PasswordPolicy) -> str:
    """Builds the pool of allowed characters using policy flags."""
    policy.validate()

    pool_parts: list[str] = []

    if policy.use_uppercase:
        pool_parts.append(string.ascii_uppercase)
    if policy.use_lowercase:
        pool_parts.append(string.ascii_lowercase)
    if policy.use_numbers:
        pool_parts.append(string.digits)
    if policy.use_symbols:
        pool_parts.append(string.punctuation)

    return "".join(pool_parts)


def generate_password(policy: PasswordPolicy) -> str:
    """Generates a random password based on the configured policy."""
    policy.validate()

    character_pool = build_character_pool(policy)
    required_characters: list[str] = []

    if policy.use_uppercase:
        required_characters.append(secrets.choice(string.ascii_uppercase))
    if policy.use_lowercase:
        required_characters.append(secrets.choice(string.ascii_lowercase))
    if policy.use_numbers:
        required_characters.append(secrets.choice(string.digits))
    if policy.use_symbols:
        required_characters.append(secrets.choice(string.punctuation))

    for _ in range(policy.length - len(required_characters)):
        required_characters.append(secrets.choice(character_pool))

    secrets.SystemRandom().shuffle(required_characters)
    return "".join(required_characters)


def validate_password(password: str, policy: PasswordPolicy) -> bool:
    """Checks whether a password satisfies the current policy rules."""
    if not isinstance(password, str):
        raise TypeError("A senha deve ser uma string.")

    if len(password) != policy.length:
        return False

    if policy.use_uppercase and not any(char.isupper() for char in password):
        return False
    if policy.use_lowercase and not any(char.islower() for char in password):
        return False
    if policy.use_numbers and not any(char.isdigit() for char in password):
        return False
    if policy.use_symbols and not any(not char.isalnum() for char in password):
        return False

    allowed_characters = build_character_pool(policy)
    return all(char in allowed_characters for char in password)


def evaluate_password_strength(password: str) -> PasswordStrength:
    """Assigns a qualitative strength based on password characteristics."""
    if not isinstance(password, str):
        raise TypeError("A senha deve ser uma string.")

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    score = sum((has_upper, has_lower, has_digit, has_symbol))

    if len(password) >= 12 and score >= 3:
        return PasswordStrength.STRONG

    if len(password) >= 8 and score >= 2:
        return PasswordStrength.MEDIUM

    return PasswordStrength.WEAK


def generate_password_with_strength(policy: PasswordPolicy) -> PasswordResult:
    """Generates a password and evaluates its strength in one step."""
    generated = generate_password(policy)
    strength = evaluate_password_strength(generated)
    return PasswordResult(value=generated, strength=strength)
