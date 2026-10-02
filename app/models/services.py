"""Service layer for password generation and validation."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final

from app.models.domain import (
    PasswordPolicy,
    PasswordResult,
    PasswordStrength,
    evaluate_password_strength,
    generate_password_with_strength,
    validate_password,
)

MIN_POLICY_LENGTH: Final[int] = 8
MAX_POLICY_LENGTH: Final[int] = 128


@dataclass(frozen=True)
class PasswordServiceResult:
    """Represents the output of a password generation service request."""

    password: str
    strength: PasswordStrength
    is_valid: bool


class PasswordService:
    """Coordinates password generation, validation and strength evaluation."""

    def create_policy(
        self,
        length: int,
        *,
        use_uppercase: bool = True,
        use_lowercase: bool = True,
        use_numbers: bool = True,
        use_symbols: bool = True,
    ) -> PasswordPolicy:
        """Creates a validated password policy instance."""
        return PasswordPolicy(
            length=length,
            use_uppercase=use_uppercase,
            use_lowercase=use_lowercase,
            use_numbers=use_numbers,
            use_symbols=use_symbols,
        )

    def generate(self, policy: PasswordPolicy) -> PasswordServiceResult:
        """Generates and validates a password according to the policy."""
        result: PasswordResult = generate_password_with_strength(policy)
        is_valid = validate_password(result.value, policy)

        return PasswordServiceResult(
            password=result.value,
            strength=result.strength,
            is_valid=is_valid,
        )

    def validate(self, password: str, policy: PasswordPolicy) -> bool:
        """Checks whether a password matches the configured policy."""
        return validate_password(password, policy)

    def evaluate_strength(self, password: str) -> PasswordStrength:
        """Returns the evaluated security level of a password."""
        return evaluate_password_strength(password)

    def ensure_valid_policy(self, length: int, **kwargs: object) -> PasswordPolicy:
        """Creates a policy and raises a validation error if it is invalid."""
        if not isinstance(length, int):
            raise TypeError("O tamanho da senha deve ser um inteiro.")

        if not MIN_POLICY_LENGTH <= length <= MAX_POLICY_LENGTH:
            raise ValueError(
                "O tamanho da senha deve estar entre "
                f"{MIN_POLICY_LENGTH} e {MAX_POLICY_LENGTH}."
            )

        return self.create_policy(
            length,
            use_uppercase=bool(kwargs.get("use_uppercase", True)),
            use_lowercase=bool(kwargs.get("use_lowercase", True)),
            use_numbers=bool(kwargs.get("use_numbers", True)),
            use_symbols=bool(kwargs.get("use_symbols", True)),
        )
