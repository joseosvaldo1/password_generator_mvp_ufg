from __future__ import annotations

import pytest

from app.models.domain import (
    MAX_PASSWORD_LENGTH,
    MIN_PASSWORD_LENGTH,
    PasswordPolicy,
    PasswordStrength,
    evaluate_password_strength,
    generate_password,
    validate_password,
)


def test_password_policy_accepts_valid_configuration() -> None:
    """A valid password configuration should be accepted."""
    policy = PasswordPolicy(
        length=12,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    assert policy.length == 12
    assert policy.use_uppercase is True
    assert policy.use_lowercase is True
    assert policy.use_numbers is True
    assert policy.use_symbols is True


@pytest.mark.parametrize("length", [MIN_PASSWORD_LENGTH - 1, MAX_PASSWORD_LENGTH + 1])
def test_password_policy_rejects_invalid_length(length: int) -> None:
    """Out-of-range lengths must be rejected."""
    with pytest.raises(ValueError):
        PasswordPolicy(length=length)


def test_password_policy_requires_at_least_one_character_group() -> None:
    """At least one character type must remain enabled."""
    with pytest.raises(ValueError):
        PasswordPolicy(
            length=10,
            use_uppercase=False,
            use_lowercase=False,
            use_numbers=False,
            use_symbols=False,
        )


def test_password_policy_rejects_non_integer_lengths() -> None:
    """Length must be an integer value."""
    with pytest.raises(TypeError):
        PasswordPolicy(length="12")


def test_generate_password_respects_policy_rules() -> None:
    """Generated passwords must satisfy the selected policy."""
    policy = PasswordPolicy(
        length=18,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    password = generate_password(policy)

    assert len(password) == 18
    assert validate_password(password, policy) is True
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(not char.isalnum() for char in password)


def test_generate_password_excludes_unselected_character_groups() -> None:
    """Disabled groups must not appear in the generated password."""
    policy = PasswordPolicy(
        length=12,
        use_uppercase=True,
        use_lowercase=False,
        use_numbers=False,
        use_symbols=False,
    )

    password = generate_password(policy)

    assert len(password) == 12
    assert validate_password(password, policy) is True
    assert any(char.isupper() for char in password)
    assert not any(char.islower() for char in password)
    assert not any(char.isdigit() for char in password)
    assert not any(not char.isalnum() for char in password)


@pytest.mark.parametrize(
    ("password", "expected"),
    [
        ("abc", PasswordStrength.WEAK),
        ("Abc12345", PasswordStrength.MEDIUM),
        ("A1b2C3d4!", PasswordStrength.STRONG),
        ("Abc123!@#Def", PasswordStrength.STRONG),
    ],
)
def test_evaluate_password_strength(password: str, expected: PasswordStrength) -> None:
    """Strength should be based on length and entropy, not just format blocks."""
    assert evaluate_password_strength(password) == expected


def test_validate_password_rejects_invalid_passwords() -> None:
    """Passwords that violate policy rules must be rejected."""
    policy = PasswordPolicy(
        length=10,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    assert validate_password("abcd", policy) is False
    assert validate_password("abcdefghi!", policy) is False
    assert validate_password("Abcdefghi!", policy) is False


def test_generate_password_handles_minimum_and_maximum_lengths() -> None:
    """Boundary lengths should generate valid passwords."""
    minimum_policy = PasswordPolicy(
        length=MIN_PASSWORD_LENGTH,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )
    maximum_policy = PasswordPolicy(
        length=MAX_PASSWORD_LENGTH,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    assert len(generate_password(minimum_policy)) == MIN_PASSWORD_LENGTH
    assert len(generate_password(maximum_policy)) == MAX_PASSWORD_LENGTH


def test_validate_password_requires_string_input() -> None:
    """The password must be a string to be validated."""
    policy = PasswordPolicy(length=12)

    with pytest.raises(TypeError):
        validate_password(123, policy)
