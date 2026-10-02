"""Typed interface helpers for the password generator app."""

from __future__ import annotations

import secrets
import string
from dataclasses import dataclass
from typing import Final

import streamlit as st

MIN_PASSWORD_LENGTH: Final[int] = 8
MAX_PASSWORD_LENGTH: Final[int] = 128


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
        value=16,
        step=1,
        help="Escolha o tamanho mínimo e máximo recomendado para segurança.",
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


def render_password_result(password: str) -> None:
    """Displays the generated password in the interface."""
    if not password:
        raise ValueError("A senha gerada não pode estar vazia.")

    st.subheader("Senha gerada")
    st.code(password, language="text")


def build_interface() -> None:
    """Creates the main password generator interface in Streamlit."""
    st.title("Gerador de Senhas Seguras")
    st.write("Configure os critérios e gere uma senha forte e confiável.")

    config = render_password_form()

    if st.button("Gerar senha"):
        try:
            new_password = generate_password(config)
            render_password_result(new_password)
        except ValueError as error:
            st.error(str(error))
