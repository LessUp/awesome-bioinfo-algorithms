#!/usr/bin/env python3
"""
Generate MkDocs documentation from algorithm YAML data.

Usage:
    python scripts/generate_mkdocs.py
"""

from pathlib import Path

import yaml


def get_base_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def load_data(base_dir: Path) -> tuple[dict, list[dict]]:
    """Load categories and algorithms from YAML files."""
    categories_path = base_dir / "data" / "categories.yaml"
    with open(categories_path, encoding="utf-8") as f:
        cat_data = yaml.safe_load(f)

    algorithms = []
    alg_dir = base_dir / "data" / "algorithms"
    for fname in sorted(alg_dir.glob("*.yaml")):
        with open(fname, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if data and "algorithms" in data:
            algorithms.extend(data["algorithms"])

    return cat_data.get("categories", []), algorithms


def build_category_map(categories: list[dict]) -> dict[str, dict]:
    """Build flat map of category id -> category data (incl subcategories)."""
    cat_map = {}
    for cat in categories:
        cat_map[cat["id"]] = cat
        for sub in cat.get("subcategories", []):
            cat_map[sub["id"]] = {**sub, "parent": cat}
    return cat_map


def build_algo_by_category(algorithms: list[dict]) -> dict[str, list[dict]]:
    """Group algorithms by category."""
    by_cat: dict[str, list[dict]] = {}
    for algo in algorithms:
        cat = algo.get("category", "unknown")
        by_cat.setdefault(cat, []).append(algo)
    return by_cat


def build_tag_index(algorithms: list[dict]) -> dict[str, list[dict]]:
    """Build tag -> algorithms index."""
    by_tag: dict[str, list[dict]] = {}
    for algo in algorithms:
        for tag in algo.get("tags", []):
            by_tag.setdefault(tag, []).append(algo)
    return by_tag


def write_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def generate_index(
    categories: list[dict], algorithms: list[dict], cat_map: dict, by_cat: dict
) -> str:
    """Generate home page."""
    total = len(algorithms)
    cats_with_algo = len(by_cat)
    all_tags = set()
    for a in algorithms:
        all_tags.update(a.get("tags", []))

    lines = [
        "# Awesome Bioinformatics Algorithms",
        "",
        "> 🧬 生物信息学算法概要汇总 | A curated list of bioinformatics algorithms",
        "",
        "## 📊 统计 | Statistics",
        "",
        f"- 算法总数: **{total}**",
        f"- 分类数: **{cats_with_algo}**",
        f"- 标签数: **{len(all_tags)}**",
        "",
        "## 📑 分类 | Categories",
        "",
        "| 分类 | 中文名 | English | 算法数 |",
        "|------|--------|---------|--------|",
    ]
    for cat in categories:
        count = len(by_cat.get(cat["id"], []))
        if count > 0:
            lines.append(
                f"| [{cat['name_en']}](categories/{cat['id']}.md) "
                f"| {cat['name']} | {cat['name_en']} | {count} |"
            )
    lines += ["", "---", ""]
    return "\n".join(lines)


def generate_algo_page(algo: dict, cat_map: dict) -> str:
    """Generate a single algorithm page."""
    cat = cat_map.get(algo.get("category", ""), {})
    cat_name = cat.get("name_en", algo.get("category", ""))
    sub_name = ""
    sub = cat_map.get(algo.get("subcategory", ""), {})
    if sub:
        sub_name = sub.get("name_en", "")

    difficulty_labels = {
        "beginner": "Beginner",
        "intermediate": "Intermediate",
        "advanced": "Advanced",
    }

    lines = [
        f"# {algo['name']}",
        "",
    ]
    if algo.get("year"):
        lines.append(f"**Year:** {algo['year']}")
    lines.append(f"**Category:** {cat_name}")
    if sub_name:
        lines.append(f"**Subcategory:** {sub_name}")
    if algo.get("difficulty"):
        lines.append(
            f"**Difficulty:** {difficulty_labels.get(algo['difficulty'], algo['difficulty'])}"
        )
    if algo.get("language"):
        lines.append(f"**Language:** {', '.join(algo['language'])}")
    lines.append("")

    lines.append("## Description")
    lines.append("")
    lines.append(algo.get("description", "").strip())
    lines.append("")

    lines.append("## Details")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append(f"| Purpose | {algo.get('purpose', '-')} |")
    lines.append(f"| Time Complexity | {algo.get('time_complexity', '-')} |")
    lines.append(f"| Space Complexity | {algo.get('space_complexity', '-')} |")
    if algo.get("paper_url"):
        lines.append(f"| Paper | [{algo['paper_url']}]({algo['paper_url']}) |")
    if algo.get("implementation_url"):
        lines.append(
            f"| Implementation | [{algo['implementation_url']}]({algo['implementation_url']}) |"
        )
    lines.append("")

    if algo.get("related_tools"):
        lines.append("## Related Tools")
        lines.append("")
        for tool in algo["related_tools"]:
            lines.append(f"- {tool}")
        lines.append("")

    if algo.get("tags"):
        lines.append("## Tags")
        lines.append("")
        lines.append(" ".join(f"`{t}`" for t in algo["tags"]))
        lines.append("")

    if algo.get("references"):
        lines.append("## References")
        lines.append("")
        for ref in algo["references"]:
            title = ref.get("title") or ref.get("url", "")
            ref_type = f" [{ref['type']}]" if ref.get("type") else ""
            lines.append(f"- [{title}]({ref['url']}){ref_type}")
        lines.append("")

    return "\n".join(lines)


def generate_category_page(cat: dict, algos: list[dict], cat_map: dict) -> str:
    """Generate a category page listing all algorithms."""
    lines = [
        f"# {cat['name']} ({cat.get('name_en', '')})",
        "",
    ]
    if cat.get("description"):
        lines.append(cat["description"])
        lines.append("")

    for sub in cat.get("subcategories", []):
        sub_algos = [a for a in algos if a.get("subcategory") == sub["id"]]
        if sub_algos:
            lines.append(f"## {sub['name']} ({sub.get('name_en', '')})")
            lines.append("")
            if sub.get("description"):
                lines.append(sub["description"])
                lines.append("")
            for a in sub_algos:
                year = f" ({a['year']})" if a.get("year") else ""
                diff = f" [{a['difficulty']}]" if a.get("difficulty") else ""
                lines.append(f"- [{a['name']}{year}](../algorithms/{a['id']}.md){diff}")
                if a.get("purpose"):
                    lines.append(f"  {a['purpose']}")
            lines.append("")

    # Algorithms without subcategory
    direct = [a for a in algos if not a.get("subcategory")]
    if direct:
        lines.append("## Other")
        lines.append("")
        for a in direct:
            year = f" ({a['year']})" if a.get("year") else ""
            lines.append(f"- [{a['name']}{year}](../algorithms/{a['id']}.md)")
        lines.append("")

    return "\n".join(lines)


def generate_tags_page(by_tag: dict) -> str:
    """Generate tags index page."""
    lines = [
        "# Tags",
        "",
        f"共 {len(by_tag)} 个标签。",
        "",
    ]
    for tag in sorted(by_tag.keys()):
        algos = by_tag[tag]
        lines.append(f"## `{tag}` ({len(algos)})")
        lines.append("")
        for a in algos:
            year = f" ({a['year']})" if a.get("year") else ""
            lines.append(f"- [{a['name']}{year}](algorithms/{a['id']}.md)")
        lines.append("")
    return "\n".join(lines)


def generate_search_page() -> str:
    """Generate static search help page."""
    return """\
# Search

Use the built-in search (top bar) to find algorithms by name, description, or tags.

## CLI Search

You can also search from the command line:

```bash
python -m scripts search "dynamic programming"
python -m scripts search --tag fast
python -m scripts search --category sequence-alignment
python -m scripts search --difficulty beginner
```

## Filter by Tag

Browse the [Tags](tags.md) page to see all available tags.
"""


def generate_about_page() -> str:
    return """\
# About

**Awesome Bioinformatics Algorithms** 是一个收集和整理生物信息学领域常用算法的开源项目。

This project collects and organizes commonly used algorithms in bioinformatics.

## Features

- 📊 200+ algorithms across 16 categories
- 🔍 Searchable web interface
- 📋 YAML-based data storage
- 🔧 CLI tools for validation, search, and export
- 🤖 Auto-generated README and web docs

## Links

- [GitHub Repository](https://github.com/LessUp/awesome-bioinfo-algorithms)
- [Contributing Guide](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/main/CONTRIBUTING.md)
- [Changelog](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/main/CHANGELOG.md)
"""


def main():
    base_dir = get_base_dir()
    mkdocs_dir = base_dir / "mkdocs" / "docs"

    print("Loading data...")
    categories, algorithms = load_data(base_dir)
    cat_map = build_category_map(categories)
    by_cat = build_algo_by_category(algorithms)
    by_tag = build_tag_index(algorithms)
    print(f"  {len(algorithms)} algorithms, {len(categories)} categories, {len(by_tag)} tags")

    print("Generating pages...")

    # Index
    write_file(mkdocs_dir / "index.md", generate_index(categories, algorithms, cat_map, by_cat))

    # Algorithm pages
    for algo in algorithms:
        write_file(
            mkdocs_dir / "algorithms" / f"{algo['id']}.md", generate_algo_page(algo, cat_map)
        )

    # Category pages
    for cat in categories:
        algos = by_cat.get(cat["id"], [])
        if algos:
            write_file(
                mkdocs_dir / "categories" / f"{cat['id']}.md",
                generate_category_page(cat, algos, cat_map),
            )

    # Categories index
    cat_index_lines = ["# All Categories", ""]
    for cat in categories:
        count = len(by_cat.get(cat["id"], []))
        if count:
            cat_index_lines.append(
                f"- [{cat['name']} ({cat['name_en']})]({cat['id']}.md) — {count} algorithms"
            )
    write_file(mkdocs_dir / "categories" / "index.md", "\n".join(cat_index_lines) + "\n")

    # Algorithms index
    algo_index_lines = ["# All Algorithms", "", f"共 {len(algorithms)} 个算法。", ""]
    for algo in sorted(algorithms, key=lambda a: a.get("name", "")):
        year = f" ({algo['year']})" if algo.get("year") else ""
        algo_index_lines.append(f"- [{algo['name']}{year}]({algo['id']}.md)")
    write_file(mkdocs_dir / "algorithms" / "index.md", "\n".join(algo_index_lines) + "\n")

    # Tags, Search, About
    write_file(mkdocs_dir / "tags.md", generate_tags_page(by_tag))
    write_file(mkdocs_dir / "search.md", generate_search_page())
    write_file(mkdocs_dir / "about.md", generate_about_page())

    print(f"  Generated {len(algorithms)} algorithm pages")
    print(f"  Generated {len([c for c in categories if by_cat.get(c['id'])])} category pages")
    print("  Generated tags, search, about, index pages")
    print("\nDone! Run 'mkdocs serve' from mkdocs/ to preview.")


if __name__ == "__main__":
    main()
