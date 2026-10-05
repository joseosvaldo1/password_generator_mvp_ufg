from __future__ import annotations

import pytest

from app.models import interface
from app.models.domain import PasswordStrength


def test_render_password_form_uses_expected_length_range_and_default(monkeypatch: pytest.MonkeyPatch) -> None:
    """The form must start at 6 characters and allow the configured range."""
    captured: dict[str, object] = {}

    def fake_slider(*args: object, **kwargs: object) -> int:
        captured["slider"] = kwargs
        return 6

    def fake_checkbox(label: str, value: bool = True) -> bool:
        captured[label] = value
        return value

    monkeypatch.setattr(interface.st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "slider", fake_slider)
    monkeypatch.setattr(interface.st, "checkbox", fake_checkbox)

    config = interface.render_password_form()

    assert config.length == 6
    assert config.use_uppercase is True
    assert config.use_lowercase is True
    assert config.use_numbers is True
    assert config.use_symbols is True
    assert captured["slider"]["min_value"] == interface.MIN_PASSWORD_LENGTH
    assert captured["slider"]["max_value"] == interface.MAX_PASSWORD_LENGTH
    assert captured["slider"]["value"] == 6


def test_generate_password_uses_selected_configuration() -> None:
    """The generator must respect the selected character choices."""
    config = interface.PasswordConfig(
        length=18,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=False,
    )

    password = interface.generate_password(config)

    assert len(password) == 18
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)
    assert not any(not char.isalnum() for char in password)


def test_estimate_password_strength_matches_market_style_thresholds() -> None:
    """The interactive score should reflect entropy-based thresholds."""
    weak_config = interface.PasswordConfig(
        length=6,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=False,
        use_symbols=False,
    )
    medium_config = interface.PasswordConfig(
        length=8,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=False,
    )
    strong_config = interface.PasswordConfig(
        length=9,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=True,
    )

    weak_strength, _, _ = interface.estimate_password_strength(weak_config)
    medium_strength, _, _ = interface.estimate_password_strength(medium_config)
    strong_strength, _, _ = interface.estimate_password_strength(strong_config)

    assert weak_strength == PasswordStrength.WEAK
    assert medium_strength == PasswordStrength.MEDIUM
    assert strong_strength == PasswordStrength.STRONG


def test_render_password_result_displays_generated_password(monkeypatch: pytest.MonkeyPatch) -> None:
    """The result must be rendered in a copy-friendly text block."""
    recorded: dict[str, object] = {}

    monkeypatch.setattr(interface.st, "subheader", lambda title: recorded.setdefault("subheader", title))
    monkeypatch.setattr(interface.st, "code", lambda value, language="text": recorded.setdefault("code", (value, language)))
    monkeypatch.setattr(interface.st, "success", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "warning", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "error", lambda *args, **kwargs: None)

    interface.render_password_result("Aa1!bcDef2")

    assert recorded["subheader"] == "Senha gerada"
    assert recorded["code"] == ("Aa1!bcDef2", "text")


def test_render_password_result_rejects_empty_password() -> None:
    """Empty output should not be rendered in the interface."""
    with pytest.raises(ValueError):
        interface.render_password_result("")


def test_validate_password_config_rejects_invalid_inputs() -> None:
    """Invalid configuration values must be rejected."""
    with pytest.raises(TypeError):
        interface.validate_password_config("invalid")

    with pytest.raises(ValueError):
        interface.validate_password_config(
            interface.PasswordConfig(
                length=10,
                use_uppercase=False,
                use_lowercase=False,
                use_numbers=False,
                use_symbols=False,
            )
        )


def test_build_interface_handles_empty_character_selection(monkeypatch: pytest.MonkeyPatch) -> None:
    """A clear message should be shown when no character type is selected."""
    messages: list[str] = []

    monkeypatch.setattr(interface.st, "title", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "slider", lambda *args, **kwargs: 6)
    monkeypatch.setattr(interface.st, "checkbox", lambda *args, **kwargs: False)
    monkeypatch.setattr(interface.st, "error", lambda message: messages.append(message))

    interface.build_interface()

    assert messages == [
        "⚠️ Nenhum tipo de caractere foi selecionado. "
        "Escolha pelo menos uma opção para gerar a senha."
    ]
