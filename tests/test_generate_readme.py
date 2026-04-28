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


def test_wrapper_docstring_references_current_cli_module():
    """Compatibility wrapper docstring should reference awesome_bioinfo, not scripts."""
    module_doc = generate_readme.__doc__ or ""

    assert "python -m awesome_bioinfo generate" in module_doc
    assert "python -m scripts generate" not in module_doc
