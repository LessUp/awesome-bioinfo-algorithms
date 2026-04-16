#!/usr/bin/env python3
"""
Generate MkDocs documentation from algorithm YAML data.

Usage:
    python scripts/generate_mkdocs.py
"""

import re
import shutil
from pathlib import Path
from typing import Optional

import yaml

from .schema import DIFFICULTY_LABELS


def get_base_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def load_data(base_dir: Path) -> tuple[list[dict], list[dict]]:
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


def trim_text(value: str, limit: int = 80) -> str:
    normalized = " ".join(value.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 1].rstrip() + "…"


# ---------------------------------------------------------------------------
# Index (landing page) — inline HTML in markdown
# ---------------------------------------------------------------------------


def generate_index(
    categories: list[dict],
    algorithms: list[dict],
    cat_map: dict,
    by_cat: dict,
    by_tag: dict,
) -> str:
    """Generate the landing page as inline HTML in index.md."""
    total = len(algorithms)
    all_tags = set()
    with_paper = 0
    with_impl = 0

    for algo in algorithms:
        all_tags.update(algo.get("tags", []))
        if algo.get("paper_url"):
            with_paper += 1
        if algo.get("implementation_url"):
            with_impl += 1

    cats_with_algo = [cat for cat in categories if by_cat.get(cat["id"])]

    # Build categories HTML
    cat_cards = []
    for cat in categories:
        count = len(by_cat.get(cat["id"], []))
        if count == 0:
            continue
        cat_cards.append(
            f'<a class="aba-cat-card" href="categories/{cat["id"]}/">'
            f'<div class="aba-cat-name">{cat["name"]}</div>'
            f'<div class="aba-cat-name-en">{cat.get("name_en", "")}</div>'
            f'<div class="aba-cat-desc">{trim_text(cat.get("description", ""), 60)}</div>'
            f'<div class="aba-cat-count">{count} 个算法 →</div>'
            f"</a>"
        )

    # Build latest algorithms HTML
    latest = sorted(
        [a for a in algorithms if a.get("year")],
        key=lambda e: (e.get("year", 0), e.get("name", "")),
        reverse=True,
    )[:8]
    algo_cards = []
    for algo in latest:
        cat_info = cat_map.get(algo.get("category", ""), {})
        cat_label = cat_info.get("name", algo.get("category", ""))
        summary = trim_text(algo.get("purpose") or algo.get("description", ""), 70)
        algo_cards.append(
            f'<a class="aba-algo-card" href="algorithms/{algo["id"]}/">'
            f'<div class="aba-algo-meta">{algo["year"]} · {cat_label}</div>'
            f'<div class="aba-algo-name">{algo["name"]}</div>'
            f'<div class="aba-algo-desc">{summary}</div>'
            f"</a>"
        )

    lines = [
        "---",
        "hide:",
        "  - navigation",
        "  - toc",
        "---",
        "",
        # Hero
        '<div class="aba-hero" markdown>',
        "",
        "# :dna: Awesome Bioinformatics Algorithms",
        "",
        f"生物信息学算法结构化知识库 — 收录 **{total}** 个算法，覆盖 **{len(cats_with_algo)}** 个研究方向",
        "",
        "[浏览全部算法](algorithms/){ .md-button .md-button--primary }",
        "[按分类浏览](categories/){ .md-button }",
        "[按标签筛选](tags/){ .md-button }",
        "",
        "</div>",
        "",
        # Stats bar
        '<div class="aba-stats">',
        f'<div class="aba-stats-item"><strong>{total}</strong><span>算法条目</span></div>',
        f'<div class="aba-stats-item"><strong>{len(cats_with_algo)}</strong><span>研究方向</span></div>',
        f'<div class="aba-stats-item"><strong>{len(all_tags)}</strong><span>标签索引</span></div>',
        f'<div class="aba-stats-item"><strong>{with_paper}</strong><span>论文链接</span></div>',
        f'<div class="aba-stats-item"><strong>{with_impl}</strong><span>代码实现</span></div>',
        "</div>",
        "",
        # Categories section
        '<div class="aba-section" markdown>',
        "",
        "## 研究方向",
        "",
        "按生物信息学问题域组织，快速定位感兴趣的算法类别",
        "{ .aba-subtitle }",
        "",
        '<div class="aba-cat-grid">',
        *cat_cards,
        "</div>",
        "",
        "</div>",
        "",
        '<hr class="aba-divider">',
        "",
        # Latest section
        '<div class="aba-section" markdown>',
        "",
        "## 最新收录",
        "",
        "近年发表的前沿算法与工具",
        "{ .aba-subtitle }",
        "",
        '<div class="aba-latest-grid">',
        *algo_cards,
        "</div>",
        "",
        "</div>",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Algorithm detail page
# ---------------------------------------------------------------------------


def generate_algo_page(algo: dict, cat_map: dict) -> str:
    """Generate a single algorithm detail page."""
    cat = cat_map.get(algo.get("category", ""), {})
    cat_name = cat.get("name", algo.get("category", ""))
    cat_id = algo.get("category", "")
    sub = cat_map.get(algo.get("subcategory", ""), {})
    sub_name = sub.get("name", "")

    lines = [f"# {algo['name']}", ""]

    # Metadata badges line
    badges = []
    if algo.get("year"):
        badges.append(f"**{algo['year']}**")
    if cat_name:
        badges.append(f"[{cat_name}](../categories/{cat_id}.md)")
    if sub_name:
        badges.append(sub_name)
    if algo.get("difficulty"):
        badges.append(DIFFICULTY_LABELS.get(algo["difficulty"], algo["difficulty"]))
    if algo.get("language"):
        badges.append(" / ".join(algo["language"]))
    if badges:
        lines.append(" · ".join(badges))
        lines.append("")

    # Description
    desc = algo.get("description", "").strip()
    if desc:
        lines.append(desc)
        lines.append("")

    # Core info table
    lines.append("| 属性 | 值 |")
    lines.append("|:-----|:---|")
    if algo.get("purpose"):
        lines.append(f"| **用途** | {algo['purpose']} |")
    if algo.get("time_complexity"):
        lines.append(f"| **时间复杂度** | `{algo['time_complexity']}` |")
    if algo.get("space_complexity"):
        lines.append(f"| **空间复杂度** | `{algo['space_complexity']}` |")
    if algo.get("paper_url"):
        url = algo["paper_url"]
        lines.append(f"| **论文** | [{url}]({url}) |")
    if algo.get("implementation_url"):
        url = algo["implementation_url"]
        lines.append(f"| **实现** | [{url}]({url}) |")
    lines.append("")

    # Related tools
    if algo.get("related_tools"):
        lines.append("**相关工具：** " + " · ".join(algo["related_tools"]))
        lines.append("")

    # Tags
    if algo.get("tags"):
        lines.append("**标签：** " + " ".join(f"`{t}`" for t in algo["tags"]))
        lines.append("")

    # References
    if algo.get("references"):
        lines.append("## 参考资料")
        lines.append("")
        for ref in algo["references"]:
            title = ref.get("title") or ref.get("url", "")
            ref_type = f" *{ref['type']}*" if ref.get("type") else ""
            lines.append(f"- [{title}]({ref['url']}){ref_type}")
        lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Category pages
# ---------------------------------------------------------------------------


def generate_category_page(cat: dict, algos: list[dict], cat_map: dict) -> str:
    """Generate a category page with subcategory sections."""
    lines = [
        f"# {cat['name']}",
        f"### {cat.get('name_en', '')}",
        "",
    ]
    if cat.get("description"):
        lines.append(f"> {cat['description']}")
        lines.append("")

    lines.append(f"共收录 **{len(algos)}** 个算法。")
    lines.append("")

    for sub in cat.get("subcategories", []):
        sub_algos = sorted(
            [a for a in algos if a.get("subcategory") == sub["id"]],
            key=lambda a: (a.get("year") or 0, a.get("name", "")),
            reverse=True,
        )
        if not sub_algos:
            continue
        lines.append(f"## {sub['name']} ({sub.get('name_en', '')})")
        lines.append("")
        if sub.get("description"):
            lines.append(f"*{sub['description']}*")
            lines.append("")

        # Table format for better readability
        lines.append("| 算法 | 年份 | 用途 | 难度 |")
        lines.append("|:-----|:----:|:-----|:----:|")
        for algo in sub_algos:
            name_link = f"[{algo['name']}](../algorithms/{algo['id']}.md)"
            year = str(algo.get("year", "-"))
            purpose = trim_text(algo.get("purpose", "-"), 50)
            diff_map = {"beginner": "入门", "intermediate": "进阶", "advanced": "高级"}
            diff = diff_map.get(algo.get("difficulty", ""), "-")
            lines.append(f"| {name_link} | {year} | {purpose} | {diff} |")
        lines.append("")

    # Algorithms without subcategory
    direct = sorted(
        [a for a in algos if not a.get("subcategory")],
        key=lambda a: (a.get("year") or 0, a.get("name", "")),
        reverse=True,
    )
    if direct:
        lines.append("## 其他")
        lines.append("")
        lines.append("| 算法 | 年份 | 用途 |")
        lines.append("|:-----|:----:|:-----|")
        for algo in direct:
            name_link = f"[{algo['name']}](../algorithms/{algo['id']}.md)"
            year = str(algo.get("year", "-"))
            purpose = trim_text(algo.get("purpose", "-"), 50)
            lines.append(f"| {name_link} | {year} | {purpose} |")
        lines.append("")

    return "\n".join(lines)


def generate_category_index(categories: list[dict], by_cat: dict) -> str:
    """Generate category overview page."""
    cats_with_algo = [
        (cat, len(by_cat.get(cat["id"], []))) for cat in categories if by_cat.get(cat["id"])
    ]

    lines = [
        "# 分类总览",
        "",
        f"共 **{len(cats_with_algo)}** 个研究方向，按算法数量排序。",
        "",
        "| 分类 | 英文名 | 算法数 | 简介 |",
        "|:-----|:-------|:------:|:-----|",
    ]
    for cat, count in sorted(cats_with_algo, key=lambda x: -x[1]):
        link = f"[{cat['name']}]({cat['id']}.md)"
        lines.append(
            f"| {link} | {cat.get('name_en', '')} | {count} | {trim_text(cat.get('description', ''), 40)} |"
        )
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Tags page
# ---------------------------------------------------------------------------


def generate_tags_page(by_tag: dict) -> str:
    """Generate tags index page with tag cloud feel."""
    sorted_tags = sorted(by_tag.items(), key=lambda x: (-len(x[1]), x[0]))

    lines = [
        "# 标签索引",
        "",
        f"共 **{len(by_tag)}** 个标签，按算法数量排序。点击标签查看关联算法。",
        "",
    ]
    for tag, algos in sorted_tags:
        lines.append(f"## `{tag}` ({len(algos)})")
        lines.append("")
        for algo in sorted(algos, key=lambda a: a.get("name", "")):
            year = f" ({algo['year']})" if algo.get("year") else ""
            lines.append(f"- [{algo['name']}{year}](algorithms/{algo['id']}.md)")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Algorithm index page
# ---------------------------------------------------------------------------


def generate_algo_index(algorithms: list[dict], cat_map: dict) -> str:
    """Generate the full algorithm listing as a searchable table."""
    lines = [
        "# 全部算法",
        "",
        f"共收录 **{len(algorithms)}** 个算法。使用顶部搜索框可快速定位。",
        "",
        "| 算法 | 年份 | 分类 | 用途 |",
        "|:-----|:----:|:-----|:-----|",
    ]
    for algo in sorted(algorithms, key=lambda a: a.get("name", "").lower()):
        name_link = f"[{algo['name']}]({algo['id']}.md)"
        year = str(algo.get("year", "-"))
        cat_info = cat_map.get(algo.get("category", ""), {})
        cat_name = cat_info.get("name", "-")
        purpose = trim_text(algo.get("purpose", "-"), 45)
        lines.append(f"| {name_link} | {year} | {cat_name} | {purpose} |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Nav generation (dynamic)
# ---------------------------------------------------------------------------


def generate_nav_yaml(categories: list[dict], by_cat: dict) -> str:
    """Generate the nav YAML block as text."""
    lines = [
        "nav:",
        "  - 首页: index.md",
        "  - 算法:",
        "    - 全部算法: algorithms/index.md",
        "  - 分类:",
        "    - 分类总览: categories/index.md",
    ]
    for cat in categories:
        if by_cat.get(cat["id"]):
            lines.append(f"    - {cat['name']}: categories/{cat['id']}.md")
    lines.append("  - 标签: tags.md")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def write_generated_pages(
    base_dir: Path,
    mkdocs_dir: Path,
    categories: list[dict],
    algorithms: list[dict],
    cat_map: dict[str, dict],
    by_cat: dict[str, list[dict]],
    by_tag: dict[str, list[dict]],
):
    # Clean previous generated docs (keep stylesheets and .gitkeep)
    if mkdocs_dir.exists():
        for item in mkdocs_dir.iterdir():
            if item.name in ("stylesheets", ".gitkeep"):
                continue
            if item.is_dir():
                shutil.rmtree(item)
            else:
                item.unlink()

    # Landing page
    write_file(
        mkdocs_dir / "index.md",
        generate_index(categories, algorithms, cat_map, by_cat, by_tag),
    )

    # Algorithm detail pages
    for algo in algorithms:
        write_file(
            mkdocs_dir / "algorithms" / f"{algo['id']}.md",
            generate_algo_page(algo, cat_map),
        )

    # Algorithm index
    write_file(
        mkdocs_dir / "algorithms" / "index.md",
        generate_algo_index(algorithms, cat_map),
    )

    # Category pages
    for cat in categories:
        algos = by_cat.get(cat["id"], [])
        if algos:
            write_file(
                mkdocs_dir / "categories" / f"{cat['id']}.md",
                generate_category_page(cat, algos, cat_map),
            )

    # Category index
    write_file(
        mkdocs_dir / "categories" / "index.md",
        generate_category_index(categories, by_cat),
    )

    # Tags
    write_file(mkdocs_dir / "tags.md", generate_tags_page(by_tag))

    # Update nav in mkdocs.yml (text-based to preserve !!python/name tags)

    mkdocs_yml = base_dir / "mkdocs" / "mkdocs.yml"
    with open(mkdocs_yml, encoding="utf-8") as f:
        text = f.read()

    # Remove existing nav block if present
    text = re.sub(r"(?m)^nav:.*?(?=^\S|\Z)", "", text, flags=re.DOTALL).rstrip() + "\n\n"

    # Append generated nav
    text += generate_nav_yaml(categories, by_cat)

    with open(mkdocs_yml, "w", encoding="utf-8") as f:
        f.write(text)


def main(base_dir: Optional[Path] = None) -> int:
    base_dir = base_dir or get_base_dir()
    mkdocs_dir = base_dir / "mkdocs" / "docs"

    print("Loading data...")
    categories, algorithms = load_data(base_dir)
    cat_map = build_category_map(categories)
    by_cat = build_algo_by_category(algorithms)
    by_tag = build_tag_index(algorithms)
    print(f"  {len(algorithms)} algorithms, {len(categories)} categories, {len(by_tag)} tags")

    print("Generating pages...")
    write_generated_pages(base_dir, mkdocs_dir, categories, algorithms, cat_map, by_cat, by_tag)

    print(f"  Generated {len(algorithms)} algorithm pages")
    print(f"  Generated {len([c for c in categories if by_cat.get(c['id'])])} category pages")
    print("  Generated algorithm index, category index, and tags page")
    print("\nDone! Run 'mkdocs serve -f mkdocs/mkdocs.yml' to preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
