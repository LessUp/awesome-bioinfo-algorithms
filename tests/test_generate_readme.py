"""Tests for the generate_readme compatibility wrapper."""

import awesome_bioinfo.generate_readme as generate_readme


def test_main_delegates_to_cmd_generate(monkeypatch):
    """Wrapper main() should delegate directly to cmd_generate."""
    called = []

    def fake_cmd_generate() -> int:
        called.append("generate")
        return 5

    monkeypatch.setattr(generate_readme, "cmd_generate", fake_cmd_generate)

    assert generate_readme.main() == 5
    assert called == ["generate"]
