"""Interface helpers for the password generator app."""

from __future__ import annotations

import math
import secrets
import string
from dataclasses import dataclass
from typing import Final

import streamlit as st

from app.models.domain import PasswordStrength, evaluate_password_strength

MIN_PASSWORD_LENGTH: Final[int] = 4
MAX_PASSWORD_LENGTH: Final[int] = 50


@dataclass(frozen=True)
class PasswordConfig:
    """Stores the validation rules for a generated password."""

    length: int = 16
    use_uppercase: bool = True
    use_lowercase: bool = True
    use_numbers: bool = True
    use_symbols: bool = True

    def __post_init__(self) -> None:
        """Validates the password configuration values."""
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


def validate_password_config(config: PasswordConfig) -> None:
    """Ensures the password configuration is valid."""
    if not isinstance(config, PasswordConfig):
        raise TypeError("A configuração da senha deve ser um PasswordConfig.")

    if not MIN_PASSWORD_LENGTH <= config.length <= MAX_PASSWORD_LENGTH:
        raise ValueError(
            "O tamanho da senha deve estar entre "
            f"{MIN_PASSWORD_LENGTH} e {MAX_PASSWORD_LENGTH}."
        )

    if not any(
        (
            config.use_uppercase,
            config.use_lowercase,
            config.use_numbers,
            config.use_symbols,
        )
    ):
        raise ValueError("Selecione pelo menos um tipo de caractere.")


def get_character_pool(config: PasswordConfig) -> str:
    """Builds the allowed character pool for password generation."""
    validate_password_config(config)

    pool: list[str] = []

    if config.use_uppercase:
        pool.append(string.ascii_uppercase)
    if config.use_lowercase:
        pool.append(string.ascii_lowercase)
    if config.use_numbers:
        pool.append(string.digits)
    if config.use_symbols:
        pool.append(string.punctuation)

    return "".join(pool)


def get_enabled_character_groups(config: PasswordConfig) -> int:
    """Counts how many character groups are enabled."""
    validate_password_config(config)

    return sum(
        (
            config.use_uppercase,
            config.use_lowercase,
            config.use_numbers,
            config.use_symbols,
        )
    )


def estimate_password_strength(config: PasswordConfig) -> tuple[PasswordStrength, int, str]:
    """Estimates the password strength using entropy and character diversity."""
    validate_password_config(config)

    enabled_groups = get_enabled_character_groups(config)
    character_pool = 0

    if config.use_uppercase:
        character_pool += 26
    if config.use_lowercase:
        character_pool += 26
    if config.use_numbers:
        character_pool += 10
    if config.use_symbols:
        character_pool += 32

    entropy_bits = config.length * math.log2(character_pool)

    if config.length >= 9 and enabled_groups >= 3 and entropy_bits >= 55:
        return (
            PasswordStrength.STRONG,
            100,
            "Senha forte: combina tamanho adequado com muita variedade de caracteres.",
        )

    if config.length >= 8 and enabled_groups >= 2 and entropy_bits >= 40:
        return (
            PasswordStrength.MEDIUM,
            65,
            "Senha moderada: aumente o tamanho ou a variedade para reforçar a segurança.",
        )

    return (
        PasswordStrength.WEAK,
        30,
        "Senha fraca: prefira mais caracteres e mais tipos de opções ativadas.",
    )


def generate_password(config: PasswordConfig) -> str:
    """Generates a secure random password according to the selected rules."""
    validate_password_config(config)

    pools: list[str] = []
    if config.use_uppercase:
        pools.append(string.ascii_uppercase)
    if config.use_lowercase:
        pools.append(string.ascii_lowercase)
    if config.use_numbers:
        pools.append(string.digits)
    if config.use_symbols:
        pools.append(string.punctuation)

    password_chars: list[str] = []
    for pool in pools:
        password_chars.append(secrets.choice(pool))

    available_chars = "".join(pools)
    remaining_length = config.length - len(password_chars)

    for _ in range(remaining_length):
        password_chars.append(secrets.choice(available_chars))

    secrets.SystemRandom().shuffle(password_chars)
    return "".join(password_chars)


def render_password_form() -> PasswordConfig:
    """Renders the input controls for password generation in Streamlit."""
    st.subheader("Configuração da senha")

    password_length = st.slider(
        "Tamanho da senha",
        min_value=MIN_PASSWORD_LENGTH,
        max_value=MAX_PASSWORD_LENGTH,
        value=6,
        step=1,
        help="Escolha o tamanho da senha para equilibrar segurança e usabilidade.",
    )

    use_uppercase = st.checkbox("Incluir letras maiúsculas", value=True)
    use_lowercase = st.checkbox("Incluir letras minúsculas", value=True)
    use_numbers = st.checkbox("Incluir números", value=True)
    use_symbols = st.checkbox("Incluir caracteres especiais", value=True)

    config = PasswordConfig(
        length=password_length,
        use_uppercase=use_uppercase,
        use_lowercase=use_lowercase,
        use_numbers=use_numbers,
        use_symbols=use_symbols,
    )

    return config


def render_password_strength(config: PasswordConfig) -> None:
    """Shows the estimated password strength according to the selected configuration."""
    strength, percentage, message = estimate_password_strength(config)

    st.subheader("Força estimada")
    st.progress(percentage / 100)

    if strength == PasswordStrength.STRONG:
        st.success(f"{strength.value.title()} — {message}")
    elif strength == PasswordStrength.MEDIUM:
        st.warning(f"{strength.value.title()} — {message}")
    else:
        st.error(f"{strength.value.title()} — {message}")

    st.caption(
        "A força é calculada com base no tamanho e na variedade dos caracteres "
        "selecionados."
    )


def render_password_result(password: str) -> None:
    """Displays the generated password in the interface."""
    if not password:
        raise ValueError("A senha gerada não pode estar vazia.")

    st.subheader("Senha gerada")
    st.code(password, language="text")

    strength = evaluate_password_strength(password)
    if strength == PasswordStrength.STRONG:
        st.success(f"Força da senha gerada: {strength.value.title()}")
    elif strength == PasswordStrength.MEDIUM:
        st.warning(f"Força da senha gerada: {strength.value.title()}")
    else:
        st.error(f"Força da senha gerada: {strength.value.title()}")


def build_interface() -> None:
    """Creates the main password generator interface in Streamlit."""
    st.title("Gerador de Senhas Seguras")
    st.write("Configure os critérios e gere uma senha forte e confiável.")

    try:
        config = render_password_form()
    except ValueError:
        st.error(
            "⚠️ Nenhum tipo de caractere foi selecionado. "
            "Escolha pelo menos uma opção para gerar a senha."
        )
        return

    render_password_strength(config)

    if st.button("Gerar senha"):
        try:
            new_password = generate_password(config)
            render_password_result(new_password)
        except ValueError as error:
            st.error(str(error))
