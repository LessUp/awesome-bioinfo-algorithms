from pathlib import Path

import scripts.__main__ as cli
from scripts.compare import cmd_compare
from scripts.export_cmd import cmd_export
from scripts.generate_mkdocs import main as generate_mkdocs
from scripts.info_cmd import cmd_info
from scripts.search import cmd_search, search_algorithms


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


def test_generate_mkdocs_creates_expected_pages(project_root, tmp_path):
    source_root = Path(project_root)
    temp_root = tmp_path / "repo"
    temp_root.mkdir()

    for relative in ["data", "docs", "mkdocs", "CHANGELOG.md", "CODE_OF_CONDUCT.md", "SECURITY.md"]:
        source_path = source_root / relative
        target_path = temp_root / relative
        if source_path.is_dir():
            import shutil

            shutil.copytree(source_path, target_path)
        else:
            target_path.write_text(source_path.read_text(encoding="utf-8"), encoding="utf-8")

    exit_code = generate_mkdocs(temp_root)

    assert exit_code == 0
    assert (temp_root / "mkdocs" / "docs" / "index.md").exists()
    assert (temp_root / "mkdocs" / "docs" / "api.md").exists()
    assert (temp_root / "mkdocs" / "docs" / "development.md").exists()
    assert (temp_root / "mkdocs" / "docs" / "code-of-conduct.md").exists()

    index_content = (temp_root / "mkdocs" / "docs" / "index.md").read_text(encoding="utf-8")
    search_content = (temp_root / "mkdocs" / "docs" / "search.md").read_text(encoding="utf-8")
    about_content = (temp_root / "mkdocs" / "docs" / "about.md").read_text(encoding="utf-8")
    category_index_content = (temp_root / "mkdocs" / "docs" / "categories" / "index.md").read_text(encoding="utf-8")
    algorithm_index_content = (temp_root / "mkdocs" / "docs" / "algorithms" / "index.md").read_text(encoding="utf-8")

    assert "导航、检索、发现与快速浏览" in index_content
    assert "aba-stats-grid" in index_content
    assert "按研究方向快速进入" in index_content
    assert "这个站点最适合承担“快速定位与发现”的角色" in search_content
    assert "仓库里最有价值的资产" in about_content
    assert "# 分类总览" in category_index_content
    assert "# 全部算法" in algorithm_index_content


def test_main_dispatches_new_cli_commands(monkeypatch):
    called = []

    monkeypatch.setattr(
        cli, "cmd_search_cli", lambda **kwargs: called.append(("search", kwargs)) or 0
    )
    monkeypatch.setattr(
        cli, "cmd_export_cli", lambda **kwargs: called.append(("export", kwargs)) or 0
    )
    monkeypatch.setattr(cli, "cmd_mkdocs", lambda: called.append(("mkdocs", {})) or 0)

    assert cli.main(["search", "smith"]) == 0
    assert cli.main(["export", "--format", "csv", "--output", "out.csv"]) == 0
    assert cli.main(["mkdocs"]) == 0

    assert called[0] == (
        "search",
        {"keyword": "smith", "tag": "", "category": "", "difficulty": ""},
    )
    assert called[1] == ("export", {"fmt": "csv", "output": "out.csv"})
    assert called[2] == ("mkdocs", {})
