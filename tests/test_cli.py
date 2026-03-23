"""Smoke tests for the repository-maintenance CLI."""
import scripts.__main__ as cli

REPO_LAYOUT_PATHS = [
    'data/categories.yaml',
    'data/algorithms',
    'templates/readme_template.md',
]


def test_validate_repo_layout_passes_in_repository_checkout(project_root):
    """The maintenance CLI should detect a valid repository checkout."""
    missing = cli.validate_repo_layout(cli.get_base_dir())

    assert missing == []

    for relative_path in REPO_LAYOUT_PATHS:
        assert (cli.get_base_dir() / relative_path).exists(), f"Missing expected path: {relative_path}"


def test_cli_commands_succeed_against_repository_data():
    """Repository CLI commands should succeed against the checked-out project data."""
    assert cli.cmd_validate() == 0
    assert cli.cmd_stats() == 0
    assert cli.cmd_generate() == 0
