"""Smoke tests for the repository-maintenance CLI."""

from pathlib import Path
from types import SimpleNamespace

import pytest

import awesome_bioinfo.__main__ as cli
from awesome_bioinfo.validate import ValidationResult

REPO_LAYOUT_PATHS = [
    "data/categories.yaml",
    "data/algorithms",
    "templates/readme_template.md",
]


class StubValidator:
    """Return a predetermined validation result."""

    result = ValidationResult(is_valid=True)

    def validate_all(self, _data_dir: str) -> ValidationResult:
        return self.result


class StubCategoryManager:
    """Minimal category manager stub for CLI tests."""

    def load_categories(self, _categories_path: str):
        return None

    def list_all_categories(self) -> list[object]:
        return []

    def get_category(self, _category_id: str):
        return None


class StubRegistry:
    """Minimal algorithm registry stub for CLI tests."""

    def __init__(self, _algorithms_dir: str):
        self._stats = SimpleNamespace(total_algorithms=1, total_categories=1, total_tags=1)

    def load_all(self):
        return None

    def get_statistics(self):
        return self._stats


class StubGenerator:
    """Minimal README generator stub for CLI tests."""

    def __init__(self, _registry, _category_manager, _template_path: str):
        return None

    def save(self, output_path: str):
        Path(output_path).write_text("# generated\n", encoding="utf-8")


def test_validate_repo_layout_passes_in_repository_checkout(project_root):
    """The maintenance CLI should detect a valid repository checkout."""
    missing = cli.validate_repo_layout(cli.get_base_dir())

    assert missing == []

    for relative_path in REPO_LAYOUT_PATHS:
        assert (cli.get_base_dir() / relative_path).exists(), (
            f"Missing expected path: {relative_path}"
        )


def test_cli_commands_succeed_against_repository_data(tmp_path):
    """Repository CLI commands should succeed against the checked-out project data."""
    output_path = tmp_path / "README.md"

    assert cli.cmd_validate() == 0
    assert cli.cmd_stats() == 0
    assert cli.cmd_generate(output_path=output_path) == 0
    assert output_path.exists()


def test_cmd_validate_returns_non_zero_on_validation_errors(monkeypatch, capsys):
    """Validate command should fail and surface validation errors."""
    StubValidator.result = ValidationResult(is_valid=False, errors=["bad field"])
    monkeypatch.setattr(cli, "ensure_repo_layout", lambda: (Path("/tmp/repo"), []))
    monkeypatch.setattr(cli, "Validator", StubValidator)

    exit_code = cli.cmd_validate()
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "bad field" in output
    assert "Validation failed" in output


def test_cmd_validate_allows_warnings(monkeypatch, capsys):
    """Validate command should succeed when only warnings are present."""
    StubValidator.result = ValidationResult(is_valid=True, warnings=["check year"])
    monkeypatch.setattr(cli, "ensure_repo_layout", lambda: (Path("/tmp/repo"), []))
    monkeypatch.setattr(cli, "Validator", StubValidator)

    exit_code = cli.cmd_validate()
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "check year" in output
    assert "All data files are valid" in output


def test_cmd_generate_stops_on_validation_errors(monkeypatch, tmp_path, capsys):
    """Generate command should not write output when validation fails."""
    output_path = tmp_path / "README.md"
    StubValidator.result = ValidationResult(is_valid=False, errors=["broken data"])
    monkeypatch.setattr(cli, "ensure_repo_layout", lambda: (Path("/tmp/repo"), []))
    monkeypatch.setattr(cli, "Validator", StubValidator)

    exit_code = cli.cmd_generate(output_path=output_path)
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "broken data" in output
    assert not output_path.exists()


def test_cmd_generate_surfaces_warnings_and_continues(monkeypatch, tmp_path, capsys):
    """Generate command should continue when validation only emits warnings."""
    output_path = tmp_path / "README.md"
    StubValidator.result = ValidationResult(is_valid=True, warnings=["suspicious year"])
    monkeypatch.setattr(cli, "ensure_repo_layout", lambda: (Path("/tmp/repo"), []))
    monkeypatch.setattr(cli, "Validator", StubValidator)
    monkeypatch.setattr(cli, "CategoryManager", StubCategoryManager)
    monkeypatch.setattr(cli, "AlgorithmRegistry", StubRegistry)
    monkeypatch.setattr(cli, "ReadmeGenerator", StubGenerator)

    exit_code = cli.cmd_generate(output_path=output_path)
    output = capsys.readouterr().out

    assert exit_code == 0
    assert "suspicious year" in output
    assert output_path.exists()


@pytest.mark.parametrize(
    ("command", "kwargs"),
    [
        (cli.cmd_validate, {}),
        (cli.cmd_stats, {}),
        (cli.cmd_generate, {"output_path": Path("/tmp/README.md")}),
    ],
)
def test_commands_fail_when_repo_layout_is_incomplete(command, kwargs, monkeypatch, capsys):
    """CLI commands should fail fast outside an intact repository checkout."""
    missing_path = "/tmp/repo/data/categories.yaml"
    monkeypatch.setattr(cli, "ensure_repo_layout", lambda: (Path("/tmp/repo"), [missing_path]))

    exit_code = command(**kwargs)
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "must be run from an intact repository checkout" in output
    assert missing_path in output


def test_validate_repo_layout_reports_missing_paths(tmp_path):
    """Repository layout checker should list any missing required paths."""
    missing = cli.validate_repo_layout(tmp_path)

    assert len(missing) == len(REPO_LAYOUT_PATHS)
    assert str(tmp_path / "data" / "categories.yaml") in missing
    assert str(tmp_path / "data" / "algorithms") in missing
    assert str(tmp_path / "templates" / "readme_template.md") in missing


def test_main_returns_help_when_no_command_is_provided(capsys):
    """main() should print argparse help and fail when no command is given."""
    exit_code = cli.main([])
    output = capsys.readouterr().out

    assert exit_code == 1
    assert "usage: python -m awesome_bioinfo" in output
    assert "search" in output
    assert "mkdocs" in output


def test_main_rejects_unknown_command(capsys):
    """main() should let argparse reject unknown commands."""
    with pytest.raises(SystemExit) as excinfo:
        cli.main(["unknown"])

    output = capsys.readouterr().err

    assert excinfo.value.code == 2
    assert "invalid choice" in output
    assert "unknown" in output


def test_main_dispatches_to_selected_command(monkeypatch):
    """main() should call the selected command and return its exit code."""
    called = []

    def fake_validate() -> int:
        called.append("validate")
        return 7

    monkeypatch.setattr(cli, "cmd_validate", fake_validate)

    assert cli.main(["validate"]) == 7
    assert called == ["validate"]


def test_build_parser_accepts_new_command_options():
    """Parser should expose the new subcommands and flags."""
    parser = cli.build_parser()

    args = parser.parse_args(["search", "--keyword", "smith", "--tag", "classic"])
    assert args.command == "search"
    assert args.keyword_flag == "smith"
    assert args.tag == "classic"

    args = parser.parse_args(["export", "--format", "csv", "--output", "out.csv"])
    assert args.command == "export"
    assert args.fmt == "csv"
    assert args.output == "out.csv"

    args = parser.parse_args(["mkdocs"])
    assert args.command == "mkdocs"

    args = parser.parse_args(["check-links"])
    assert args.command == "check-links"


def test_main_prefers_keyword_flag_over_positional(monkeypatch):
    """main() should prefer --keyword over the positional search term."""
    called = []

    monkeypatch.setattr(
        cli,
        "cmd_search_cli",
        lambda **kwargs: called.append(kwargs) or 0,
    )

    assert cli.main(["search", "ignored", "--keyword", "smith"]) == 0
    assert called == [{"keyword": "smith", "tag": "", "category": "", "difficulty": ""}]


def test_main_dispatches_generate_with_output_argument(monkeypatch, tmp_path):
    """main() should pass generate --output through as a Path."""
    called = []
    output_path = tmp_path / "README.md"

    monkeypatch.setattr(
        cli, "cmd_generate", lambda output_path=None: called.append(output_path) or 0
    )

    assert cli.main(["generate", "--output", str(output_path)]) == 0
    assert called == [output_path]


def test_main_dispatches_info_and_compare_commands(monkeypatch):
    """main() should pass positional identifiers to info and compare wrappers."""
    info_called = []
    compare_called = []

    monkeypatch.setattr(cli, "cmd_info_cli", lambda algo_id: info_called.append(algo_id) or 0)
    monkeypatch.setattr(
        cli, "cmd_compare_cli", lambda id1, id2: compare_called.append((id1, id2)) or 0
    )

    assert cli.main(["info", "smith-waterman"]) == 0
    assert cli.main(["compare", "smith-waterman", "needleman-wunsch"]) == 0
    assert info_called == ["smith-waterman"]
    assert compare_called == [("smith-waterman", "needleman-wunsch")]


def test_main_dispatches_mkdocs_command(monkeypatch):
    """main() should dispatch the mkdocs subcommand."""
    called = []
    monkeypatch.setattr(cli, "cmd_mkdocs", lambda: called.append("mkdocs") or 0)

    assert cli.main(["mkdocs"]) == 0
    assert called == ["mkdocs"]


def test_main_dispatches_check_links_command(monkeypatch):
    """main() should dispatch the check-links subcommand."""
    called = []
    monkeypatch.setattr(cli, "cmd_check_links", lambda: called.append("check-links") or 0)

    assert cli.main(["check-links"]) == 0
    assert called == ["check-links"]
