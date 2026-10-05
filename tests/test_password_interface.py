from __future__ import annotations

import pytest

from app.models import interface


def test_render_password_form_collects_size_and_character_options(monkeypatch: pytest.MonkeyPatch) -> None:
    """The form should collect all relevant configuration values."""
    captured: dict[str, object] = {}

    def fake_slider(*args: object, **kwargs: object) -> int:
        captured["slider"] = kwargs
        return 24

    def fake_checkbox(label: str, value: bool = True) -> bool:
        captured[label] = value
        return value

    monkeypatch.setattr(interface.st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "slider", fake_slider)
    monkeypatch.setattr(interface.st, "checkbox", fake_checkbox)

    config = interface.render_password_form()

    assert config.length == 24
    assert config.use_uppercase is True
    assert config.use_lowercase is True
    assert config.use_numbers is True
    assert config.use_symbols is True
    assert captured["slider"]["min_value"] == interface.MIN_PASSWORD_LENGTH
    assert captured["slider"]["max_value"] == interface.MAX_PASSWORD_LENGTH


def test_render_password_result_displays_generated_password_for_copy(monkeypatch: pytest.MonkeyPatch) -> None:
    """The password should be shown in a copy-friendly text block."""
    recorded: dict[str, object] = {}

    monkeypatch.setattr(interface.st, "subheader", lambda title: recorded.setdefault("subheader", title))
    monkeypatch.setattr(interface.st, "code", lambda value, language="text": recorded.setdefault("code", (value, language)))

    interface.render_password_result("Aa1!bcDef2")

    assert recorded["subheader"] == "Senha gerada"
    assert recorded["code"] == ("Aa1!bcDef2", "text")


def test_render_password_result_rejects_empty_password() -> None:
    """Empty output should not be rendered in the interface."""
    with pytest.raises(ValueError):
        interface.render_password_result("")


def test_generate_password_uses_selected_configurations(monkeypatch: pytest.MonkeyPatch) -> None:
    """The main generator should respect user-defined rules."""
    config = interface.PasswordConfig(
        length=18,
        use_uppercase=True,
        use_lowercase=True,
        use_numbers=True,
        use_symbols=False,
    )

    generated = interface.generate_password(config)

    assert len(generated) == 18
    assert any(char.isupper() for char in generated)
    assert any(char.islower() for char in generated)
    assert any(char.isdigit() for char in generated)
    assert not any(not char.isalnum() for char in generated)


def test_validate_password_config_rejects_invalid_config() -> None:
    """Invalid password configs should be rejected immediately."""
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
    """The interface should show a friendly message when no character type is selected."""
    messages: list[str] = []

    monkeypatch.setattr(interface.st, "title", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "write", lambda *args, **kwargs: None)
    monkeypatch.setattr(interface.st, "subheader", lambda *args, **kwargs: None)
    monkeypatch.setattr(
        interface.st,
        "slider",
        lambda *args, **kwargs: 16,
    )
    monkeypatch.setattr(
        interface.st,
        "checkbox",
        lambda *args, **kwargs: False,
    )
    monkeypatch.setattr(interface.st, "error", lambda message: messages.append(message))

    interface.build_interface()

    assert messages == [
        "⚠️ Nenhum tipo de caractere foi selecionado. "
        "Escolha pelo menos uma opção para gerar a senha."
    ]
