"""Tests for VitePress docs generator whitepaper outputs."""

from pathlib import Path

from awesome_bioinfo.generate_docs import (
    build_algo_by_category,
    build_category_map,
    build_tag_index,
    write_all_pages,
)
from awesome_bioinfo.schema import AlgorithmEntry, Category


def _sample_category() -> Category:
    return Category(
        id="sequence-alignment",
        name="序列比对",
        name_en="Sequence Alignment",
        description="用于比较和对齐生物序列的算法。",
        description_en="Algorithms for comparing and aligning biological sequences.",
        subcategories=[],
    )


def _sample_algorithm() -> AlgorithmEntry:
    return AlgorithmEntry(
        id="smith-waterman",
        name="Smith-Waterman",
        description=(
            "经典的局部序列比对算法，使用动态规划方法找出两条序列之间最相似的区域，"
            "常用于蛋白质和核酸序列分析场景。"
        ),
        description_en=(
            "A classic local alignment algorithm based on dynamic programming, widely used in "
            "protein and nucleotide sequence analysis."
        ),
        purpose="局部序列比对与高相似片段检测。",
        purpose_en="Local sequence alignment and high-similarity segment discovery.",
        time_complexity="O(mn)",
        space_complexity="O(mn)",
        category="sequence-alignment",
        tags=["local-alignment", "dynamic-programming"],
        year=1981,
        difficulty="intermediate",
        paper_url="https://doi.org/10.1016/0022-2836(81)90087-5",
        implementation_url="https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library",
        language=["C"],
    )


def _run_generation(tmp_path: Path) -> Path:
    docs_dir = tmp_path / "docs"
    categories = [_sample_category()]
    algorithms = [_sample_algorithm()]
    cat_map = build_category_map(categories)
    by_cat = build_algo_by_category(algorithms)
    by_tag = build_tag_index(algorithms)
    write_all_pages(docs_dir, categories, algorithms, cat_map, by_cat, by_tag)
    return docs_dir


def test_write_all_pages_generates_whitepaper_structure(tmp_path: Path) -> None:
    docs_dir = _run_generation(tmp_path)

    expected_pages = [
        docs_dir / "zh" / "guides" / "project-overview.md",
        docs_dir / "zh" / "academy" / "learning-path.md",
        docs_dir / "zh" / "architecture" / "system-architecture.md",
        docs_dir / "zh" / "architecture" / "data-pipeline.md",
        docs_dir / "zh" / "architecture" / "quality-assurance.md",
        docs_dir / "zh" / "research" / "references.md",
        docs_dir / "zh" / "research" / "evolution.md",
        docs_dir / "zh" / "reference" / "cli-workflow.md",
        docs_dir / "en" / "guides" / "project-overview.md",
        docs_dir / "en" / "academy" / "learning-path.md",
        docs_dir / "en" / "architecture" / "system-architecture.md",
        docs_dir / "en" / "architecture" / "data-pipeline.md",
        docs_dir / "en" / "architecture" / "quality-assurance.md",
        docs_dir / "en" / "research" / "references.md",
        docs_dir / "en" / "research" / "evolution.md",
        docs_dir / "en" / "reference" / "cli-workflow.md",
    ]
    for page in expected_pages:
        assert page.exists(), f"missing generated page: {page}"


def test_generated_architecture_pages_include_mermaid(tmp_path: Path) -> None:
    docs_dir = _run_generation(tmp_path)
    zh_arch = (docs_dir / "zh" / "architecture" / "system-architecture.md").read_text(
        encoding="utf-8"
    )
    en_arch = (docs_dir / "en" / "architecture" / "system-architecture.md").read_text(
        encoding="utf-8"
    )
    assert "```mermaid" in zh_arch
    assert "```mermaid" in en_arch


def test_generated_homepage_is_whitepaper_positioned(tmp_path: Path) -> None:
    docs_dir = _run_generation(tmp_path)
    zh_index = (docs_dir / "zh" / "index.md").read_text(encoding="utf-8")
    en_index = (docs_dir / "en" / "index.md").read_text(encoding="utf-8")

    assert "技术白皮书" in zh_index
    assert "Technical Whitepaper" in en_index
