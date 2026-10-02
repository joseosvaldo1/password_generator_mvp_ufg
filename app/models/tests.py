"""Tests for password generation rules and service behavior."""

from __future__ import annotations

import pytest

from app.models.domain import (
    PasswordPolicy,
    PasswordStrength,
    evaluate_password_strength,
    generate_password,
    validate_password,
)
from app.models.services import PasswordService


def test_password_policy_accepts_valid_configuration() -> None:
    """Valid configuration should be accepted without errors."""
    policy = PasswordPolicy(
        length=16,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    assert policy.length == 16
    assert policy.use_uppercase is True


def test_password_policy_rejects_invalid_length() -> None:
    """Lengths outside the valid range should raise ValueError."""
    with pytest.raises(ValueError):
        PasswordPolicy(length=7)

    with pytest.raises(ValueError):
        PasswordPolicy(length=200)


def test_password_policy_requires_at_least_one_character_type() -> None:
    """At least one character group must be enabled."""
    with pytest.raises(ValueError):
        PasswordPolicy(
            length=12,
            use_uppercase=False,
            use_lowercase=False,
            use_numbers=False,
            use_symbols=False,
        )


def test_generate_password_respects_policy() -> None:
    """Generated passwords must match the selected policy."""
    policy = PasswordPolicy(
        length=20,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    password = generate_password(policy)

    assert len(password) == 20
    assert validate_password(password, policy) is True


def test_generate_password_contains_required_character_groups() -> None:
    """Each enabled group should appear in the generated password."""
    policy = PasswordPolicy(
        length=18,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    password = generate_password(policy)

    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)
    assert any(not char.isalnum() for char in password)


def test_evaluate_password_strength() -> None:
    """Password strength should be classified accurately."""
    assert evaluate_password_strength("Abc123!@#Def") == PasswordStrength.STRONG
    assert evaluate_password_strength("Abc12345") == PasswordStrength.MEDIUM
    assert evaluate_password_strength("abc") == PasswordStrength.WEAK


def test_password_service_generates_valid_result() -> None:
    """Service layer should produce a valid password and strength label."""
    service = PasswordService()
    policy = service.create_policy(
        length=14,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    result = service.generate(policy)

    assert result.is_valid is True
    assert len(result.password) == 14
    assert isinstance(result.strength, PasswordStrength)


def test_password_service_rejects_invalid_policy() -> None:
    """Invalid length values should raise errors when creating a policy."""
    service = PasswordService()

    with pytest.raises(ValueError):
        service.create_policy(4)
