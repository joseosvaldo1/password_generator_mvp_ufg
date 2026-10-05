from __future__ import annotations

import pytest

from app.models.domain import PasswordStrength
from app.models.services import PasswordService


def test_password_service_creates_policy_with_custom_configuration() -> None:
    """The service should build a policy that respects user options."""
    service = PasswordService()

    policy = service.create_policy(
        12,
        use_uppercase=True,
        use_lowercase=False,
        use_numbers=True,
        use_symbols=False,
    )

    assert policy.length == 12
    assert policy.use_uppercase is True
    assert policy.use_lowercase is False
    assert policy.use_numbers is True
    assert policy.use_symbols is False


def test_password_service_generate_returns_valid_result() -> None:
    """The service must produce a valid password and strength classification."""
    service = PasswordService()
    policy = service.create_policy(
        14,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    result = service.generate(policy)

    assert result.is_valid is True
    assert len(result.password) == 14
    assert isinstance(result.strength, PasswordStrength)
    assert result.strength in PasswordStrength


def test_password_service_validate_matches_policy() -> None:
    """Validation should reflect the configured rules."""
    service = PasswordService()
    policy = service.create_policy(
        20,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    password = service.generate(policy).password

    assert service.validate(password, policy) is True
    assert service.validate("abc", policy) is False


def test_password_service_rejects_invalid_length() -> None:
    """An invalid length must produce a validation error."""
    service = PasswordService()

    with pytest.raises(ValueError):
        service.create_policy(7)

    with pytest.raises(ValueError):
        service.create_policy(200)


def test_password_service_ensure_valid_policy_raises_on_invalid_input() -> None:
    """The policy guard should reject invalid inputs early."""
    service = PasswordService()

    with pytest.raises(TypeError):
        service.ensure_valid_policy("12")

    with pytest.raises(ValueError):
        service.ensure_valid_policy(5)

    with pytest.raises(ValueError):
        service.ensure_valid_policy(12, use_uppercase=False, use_lowercase=False, use_numbers=False, use_symbols=False)
