from __future__ import annotations

import pytest

from app.models.domain import PasswordStrength
from app.models.services import PasswordService


def test_password_service_creates_policy_with_custom_configuration() -> None:
    """The service must create a policy from the requested options."""
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
    """Generation must include validation and strength assessment."""
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
    assert isinstance(result.password, str)
    assert isinstance(result.strength, PasswordStrength)
    assert result.strength in PasswordStrength


def test_password_service_validate_matches_policy() -> None:
    """Validation should reject passwords that do not meet the current policy."""
    service = PasswordService()
    policy = service.create_policy(
        16,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    valid_password = service.generate(policy).password
    assert service.validate(valid_password, policy) is True
    assert service.validate("abc", policy) is False


def test_password_service_rejects_invalid_policy_length() -> None:
    """Invalid lengths must raise a validation error."""
    service = PasswordService()

    with pytest.raises(ValueError):
        service.create_policy(3)

    with pytest.raises(ValueError):
        service.create_policy(200)


def test_password_service_ensure_valid_policy_raises_on_invalid_input() -> None:
    """The guard method must reject invalid type and content early."""
    service = PasswordService()

    with pytest.raises(TypeError):
        service.ensure_valid_policy("12")

    with pytest.raises(ValueError):
        service.ensure_valid_policy(5)

    with pytest.raises(ValueError):
        service.ensure_valid_policy(
            10,
            use_uppercase=False,
            use_lowercase=False,
            use_numbers=False,
            use_symbols=False,
        )


def test_password_service_evaluate_strength_uses_domain_logic() -> None:
    """The service should expose the same strength classification as the domain layer."""
    service = PasswordService()

    assert service.evaluate_strength("abc") == PasswordStrength.WEAK
    assert service.evaluate_strength("Abc12345") == PasswordStrength.MEDIUM
    assert service.evaluate_strength("A1b2C3d4!") == PasswordStrength.STRONG
