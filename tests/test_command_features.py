import awesome_bioinfo.__main__ as cli
from awesome_bioinfo.__main__ import (
    cmd_compare,
    cmd_export,
    cmd_info,
    cmd_search,
    search_algorithms,
)


def test_search_algorithms_filters_loaded_registry(loaded_registry, loaded_category_manager):
    results = search_algorithms(
        loaded_registry,
        loaded_category_manager,
        keyword="dynamic",
        tag="classic",
        category="pairwise",
    )

    ids = {algo.id for algo in results}
    assert "smith-waterman" in ids


def test_cmd_search_rejects_invalid_difficulty(loaded_registry, loaded_category_manager, capsys):
    exit_code = cmd_search(
        loaded_registry,
        loaded_category_manager,
        difficulty="expert",
    )

    output = capsys.readouterr().out
    assert exit_code == 1
    assert "Invalid difficulty" in output


def test_cmd_info_shows_algorithm_details(loaded_registry, loaded_category_manager, capsys):
    exit_code = cmd_info(loaded_registry, loaded_category_manager, "smith-waterman")

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Smith-Waterman" in output
    assert "ID:" in output
    assert "时间复杂度" in output


def test_cmd_compare_prints_side_by_side_table(loaded_registry, loaded_category_manager, capsys):
    exit_code = cmd_compare(
        loaded_registry,
        loaded_category_manager,
        "smith-waterman",
        "needleman-wunsch",
    )

    output = capsys.readouterr().out
    assert exit_code == 0
    assert "Algorithm 1" in output
    assert "Algorithm 2" in output
    assert "smith-waterman" in output
    assert "needleman-wunsch" in output


def test_cmd_export_json_to_stdout(loaded_registry, loaded_category_manager, capsys):
    exit_code = cmd_export(loaded_registry, loaded_category_manager, fmt="json")

    output = capsys.readouterr().out
    assert exit_code == 0
    assert '"algorithms"' in output
    assert '"total"' in output


def test_cmd_export_csv_to_file(loaded_registry, loaded_category_manager, tmp_path, capsys):
    output_path = tmp_path / "algorithms.csv"

    exit_code = cmd_export(
        loaded_registry,
        loaded_category_manager,
        fmt="csv",
        output=str(output_path),
    )

    output = capsys.readouterr().out
    assert exit_code == 0
    assert output_path.exists()
    assert "Exported" in output
    assert "id,name,year,category" in output_path.read_text(encoding="utf-8")


def test_main_dispatches_new_cli_commands(monkeypatch):
    called = []

    monkeypatch.setattr(
        cli, "cmd_search_cli", lambda **kwargs: called.append(("search", kwargs)) or 0
    )
    monkeypatch.setattr(
        cli, "cmd_export_cli", lambda **kwargs: called.append(("export", kwargs)) or 0
    )
    assert cli.main(["search", "smith"]) == 0
    assert cli.main(["export", "--format", "csv", "--output", "out.csv"]) == 0
    assert called[0] == (
        "search",
        {"keyword": "smith", "tag": "", "category": "", "difficulty": ""},
    )
    assert called[1] == ("export", {"fmt": "csv", "output": "out.csv"})
