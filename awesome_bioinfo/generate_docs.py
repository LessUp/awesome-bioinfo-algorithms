#!/usr/bin/env python3
"""
Generate VitePress documentation from algorithm YAML data.

Usage:
    python -m awesome_bioinfo vitepress
"""

from datetime import datetime
from pathlib import Path
from typing import Optional

from awesome_bioinfo.schema import (
    DIFFICULTY_LABELS,
    DIFFICULTY_LABELS_BILINGUAL,
    AlgorithmEntry,
    Category,
)


def get_base_dir() -> Path:
    return Path(__file__).resolve().parent.parent


def load_data(base_dir: Path) -> tuple[list["Category"], list["AlgorithmEntry"]]:
    """Load categories and algorithms using DataStore."""
    from awesome_bioinfo.data_store import DataStore

    store = DataStore(base_dir)
    missing = store.validate_layout()
    if missing:
        raise FileNotFoundError(f"Missing required paths: {', '.join(missing)}")

    store.load_all()
    return store.get_all_categories(), store.get_all_algorithms()


def build_category_map(categories: list[Category]) -> dict[str, Category]:
    """Build flat map of category id -> category object (incl subcategories)."""
    cat_map: dict[str, Category] = {}
    for cat in categories:
        cat_map[cat.id] = cat
        for sub in cat.subcategories:
            sub.parent_id = cat.id
            cat_map[sub.id] = sub
    return cat_map


def build_algo_by_category(algorithms: list[AlgorithmEntry]) -> dict[str, list[AlgorithmEntry]]:
    """Group algorithms by category."""
    by_cat: dict[str, list[AlgorithmEntry]] = {}
    for algo in algorithms:
        by_cat.setdefault(algo.category, []).append(algo)
    return by_cat


def build_tag_index(algorithms: list[AlgorithmEntry]) -> dict[str, list[AlgorithmEntry]]:
    """Build tag -> algorithms index."""
    by_tag: dict[str, list[AlgorithmEntry]] = {}
    for algo in algorithms:
        for tag in algo.tags:
            by_tag.setdefault(tag, []).append(algo)
    return by_tag


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def trim_text(value: str, limit: int = 80) -> str:
    normalized = " ".join(value.split())
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 1].rstrip() + "…"


def get_difficulty_badge(difficulty: str, lang: str = "zh") -> str:
    """Get difficulty badge text."""
    if lang == "zh":
        return DIFFICULTY_LABELS_BILINGUAL.get(difficulty, difficulty)
    return DIFFICULTY_LABELS.get(difficulty, difficulty)


# -----------------------------------------------------------------------------
# Chinese Pages (zh/)
# -----------------------------------------------------------------------------


def generate_zh_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate Chinese landing page."""
    total = len(algorithms)
    all_tags: set[str] = set()
    cats_with_algo = [cat for cat in categories if by_cat.get(cat.id)]

    for algo in algorithms:
        all_tags.update(algo.tags)

    # Build category cards
    cat_cards = []
    for cat in categories:
        count = len(by_cat.get(cat.id, []))
        if count == 0:
            continue
        cat_cards.append(f"""
- **[{cat.name}](categories/{cat.id}/)** — {trim_text(cat.description, 60)} ({count} 个算法)
""")

    # Build latest algorithms
    latest = sorted(
        [a for a in algorithms if a.year],
        key=lambda e: (e.year, e.name),
        reverse=True,
    )[:8]

    algo_list = []
    for algo in latest:
        cat_info = cat_map.get(algo.category)
        year_str = f"({algo.year})" if algo.year else ""
        algo_list.append(
            f"- [{algo.name}](algorithms/{algo.id}.md) {year_str} — {trim_text(algo.purpose, 50)}"
        )

    current_year = datetime.now().year

    return f"""---
layout: home
title: 首页
hero:
  name: Awesome Bioinformatics
  text: Algorithms
  tagline: 生物信息学算法知识库 — 收录 {total} 个算法
  actions:
    - theme: brand
      text: 浏览算法
      link: /zh/algorithms/
    - theme: alt
      text: 分类导航
      link: /zh/categories/
features:
  - icon: 🧬
    title: {total}+ 算法
    details: 涵盖序列比对、基因组组装、变异检测等核心领域
  - icon: 📊
    title: {len(cats_with_algo)} 个分类
    details: 系统化分类体系，快速定位所需算法
  - icon: 🔍
    title: {len(all_tags)} 个标签
    details: 多维度索引，精准检索
---

## 研究方向

{"".join(cat_cards)}

## 最新收录

{chr(10).join(algo_list)}

[查看全部算法 →](/zh/algorithms/)
"""


def generate_zh_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    """Generate Chinese algorithm detail page."""
    cat = cat_map.get(algo.category)
    cat_name = cat.name if cat else algo.category
    sub = cat_map.get(algo.subcategory) if algo.subcategory else None
    sub_name = sub.name if sub else ""

    # Build frontmatter
    frontmatter = f"""---
title: {algo.name}
description: {trim_text(algo.description, 150)}
---"""

    # Build info section
    info_lines = [f"# {algo.name}\n"]

    if algo.description:
        info_lines.append(f"{algo.description}\n")

    # Meta info table
    info_lines.append("| 属性 | 值 |")
    info_lines.append("|------|-----|")

    if algo.purpose:
        info_lines.append(f"| **用途** | {algo.purpose} |")
    if algo.time_complexity:
        info_lines.append(f"| **时间复杂度** | `{algo.time_complexity}` |")
    if algo.space_complexity:
        info_lines.append(f"| **空间复杂度** | `{algo.space_complexity}` |")
    if algo.year:
        info_lines.append(f"| **年份** | {algo.year} |")
    if algo.difficulty:
        info_lines.append(f"| **难度** | {get_difficulty_badge(algo.difficulty, 'zh')} |")
    if algo.language:
        info_lines.append(f"| **实现语言** | {'、'.join(algo.language)} |")
    if cat_name:
        info_lines.append(f"| **分类** | [{cat_name}](../categories/{algo.category}/) |")

    info_lines.append("")

    # Links
    links = []
    if algo.paper_url:
        links.append(f"- [📄 论文链接]({algo.paper_url})")
    if algo.implementation_url:
        links.append(f"- [💻 代码实现]({algo.implementation_url})")

    if links:
        info_lines.append("## 链接\n")
        info_lines.extend(links)
        info_lines.append("")

    # Related tools
    if algo.related_tools:
        info_lines.append("## 相关工具\n")
        info_lines.append(" · ".join(f"`{tool}`" for tool in algo.related_tools))
        info_lines.append("")

    # Tags
    if algo.tags:
        info_lines.append("## 标签\n")
        tag_links = " ".join(f"[{tag}](../tags#{tag})" for tag in algo.tags)
        info_lines.append(tag_links)
        info_lines.append("")

    # References
    if algo.references:
        info_lines.append("## 参考资料\n")
        for ref in algo.references:
            ref_type = f" *({ref.type})*" if ref.type else ""
            info_lines.append(f"- [{ref.title or ref.url}]({ref.url}){ref_type}")
        info_lines.append("")

    return frontmatter + "\n" + "\n".join(info_lines)


def generate_zh_algo_index(
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate Chinese algorithm listing page."""
    rows = []
    for algo in sorted(algorithms, key=lambda a: a.name.lower()):
        cat_info = cat_map.get(algo.category)
        cat_name = cat_info.name if cat_info else "-"
        year = str(algo.year) if algo.year else "-"
        diff = get_difficulty_badge(algo.difficulty, "zh") if algo.difficulty else "-"

        rows.append(
            f"| [{algo.name}]({algo.id}.md) | {year} | {cat_name} | {trim_text(algo.purpose or '-', 40)} | {diff} |"
        )

    return f"""---
title: 全部算法
---

# 全部算法

共收录 **{len(algorithms)}** 个算法。

| 算法 | 年份 | 分类 | 用途 | 难度 |
|------|------|------|------|------|
{chr(10).join(rows)}
"""


def generate_zh_category_page(
    cat: Category,
    algos: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate Chinese category page."""
    lines = [f"# {cat.name}\n"]

    if cat.description:
        lines.append(f"> {cat.description}\n")

    lines.append(f"**{len(algos)}** 个算法收录于该分类。\n")

    # Subcategories
    for sub in cat.subcategories:
        sub_algos = sorted(
            [a for a in algos if a.subcategory == sub.id],
            key=lambda a: (a.year or 0, a.name),
            reverse=True,
        )
        if not sub_algos:
            continue

        lines.append(f"## {sub.name}\n")
        if sub.description:
            lines.append(f"*{sub.description}*\n")

        lines.append("| 算法 | 年份 | 用途 |")
        lines.append("|------|------|------|")
        for algo in sub_algos:
            year = str(algo.year) if algo.year else "-"
            lines.append(
                f"| [{algo.name}](../../algorithms/{algo.id}.md) | {year} | {trim_text(algo.purpose or '-', 40)} |"
            )
        lines.append("")

    # Algorithms without subcategory
    direct = sorted(
        [a for a in algos if not a.subcategory],
        key=lambda a: (a.year or 0, a.name),
        reverse=True,
    )
    if direct:
        lines.append("## 其他\n")
        lines.append("| 算法 | 年份 | 用途 |")
        lines.append("|------|------|------|")
        for algo in direct:
            year = str(algo.year) if algo.year else "-"
            lines.append(
                f"| [{algo.name}](../../algorithms/{algo.id}.md) | {year} | {trim_text(algo.purpose or '-', 40)} |"
            )

    return "\n".join(lines)


def generate_zh_category_index(
    categories: list[Category],
    by_cat: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate Chinese category overview page."""
    cats_with_algo = [
        (cat, len(by_cat.get(cat.id, []))) for cat in categories if by_cat.get(cat.id)
    ]

    lines = [
        """---
title: 分类总览
---

# 分类总览

"""
    ]

    for cat, count in sorted(cats_with_algo, key=lambda x: -x[1]):
        lines.append(
            f"- **[{cat.name}]({cat.id}/)** — {trim_text(cat.description, 60)} ({count} 个算法)"
        )

    return "\n".join(lines)


def generate_zh_tags_page(by_tag: dict[str, list[AlgorithmEntry]]) -> str:
    """Generate Chinese tags page."""
    sorted_tags = sorted(by_tag.items(), key=lambda x: (-len(x[1]), x[0]))

    lines = [
        """---
title: 标签索引
---

# 标签索引

"""
    ]

    for tag, algos in sorted_tags:
        lines.append(f"## {tag}\n")
        lines.append(f"{len(algos)} 个算法\n")
        for algo in sorted(algos, key=lambda a: a.name):
            year = f" ({algo.year})" if algo.year else ""
            lines.append(f"- [{algo.name}](/zh/algorithms/{algo.id}.md){year}")
        lines.append("")

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# English Pages (en/)
# -----------------------------------------------------------------------------


def generate_en_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate English landing page."""
    total = len(algorithms)
    all_tags: set[str] = set()
    cats_with_algo = [cat for cat in categories if by_cat.get(cat.id)]

    for algo in algorithms:
        all_tags.update(algo.tags)

    cat_cards = []
    for cat in categories:
        count = len(by_cat.get(cat.id, []))
        if count == 0:
            continue
        desc = cat.description_en if cat.description_en else cat.description
        cat_cards.append(f"""
- **[{cat.name_en}](categories/{cat.id}/)** — {trim_text(desc, 60)} ({count} algorithms)
""")

    latest = sorted(
        [a for a in algorithms if a.year],
        key=lambda e: (e.year, e.name),
        reverse=True,
    )[:8]

    algo_list = []
    for algo in latest:
        cat_info = cat_map.get(algo.category)
        year_str = f"({algo.year})" if algo.year else ""
        purpose = algo.purpose_en if algo.purpose_en else algo.purpose
        algo_list.append(
            f"- [{algo.name}](algorithms/{algo.id}.md) {year_str} — {trim_text(purpose, 50)}"
        )

    return f"""---
layout: home
title: Home
hero:
  name: Awesome Bioinformatics
  text: Algorithms
  tagline: Bioinformatics Algorithm Knowledge Base — {total} algorithms
  actions:
    - theme: brand
      text: Browse Algorithms
      link: /en/algorithms/
    - theme: alt
      text: Categories
      link: /en/categories/
features:
  - icon: 🧬
    title: {total}+ Algorithms
    details: Covering sequence alignment, genome assembly, variant calling and more
  - icon: 📊
    title: {len(cats_with_algo)} Categories
    details: Systematic classification for quick navigation
  - icon: 🔍
    title: {len(all_tags)} Tags
    details: Multi-dimensional indexing for precise search
---

## Categories

{"".join(cat_cards)}

## Latest Additions

{chr(10).join(algo_list)}

[View All Algorithms →](/en/algorithms/)
"""


def generate_en_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    """Generate English algorithm detail page."""
    cat = cat_map.get(algo.category)
    cat_name = cat.name_en if cat and cat.name_en else (cat.name if cat else algo.category)
    sub = cat_map.get(algo.subcategory) if algo.subcategory else None
    sub_name = sub.name_en if sub and sub.name_en else (sub.name if sub else "")

    description = algo.description_en if algo.description_en else algo.description
    purpose = algo.purpose_en if algo.purpose_en else algo.purpose

    frontmatter = f"""---
title: {algo.name}
description: {trim_text(description, 150)}
---"""

    info_lines = [f"# {algo.name}\n"]

    if description:
        info_lines.append(f"{description}\n")

    info_lines.append("| Property | Value |")
    info_lines.append("|----------|-------|")

    if purpose:
        info_lines.append(f"| **Purpose** | {purpose} |")
    if algo.time_complexity:
        info_lines.append(f"| **Time Complexity** | `{algo.time_complexity}` |")
    if algo.space_complexity:
        info_lines.append(f"| **Space Complexity** | `{algo.space_complexity}` |")
    if algo.year:
        info_lines.append(f"| **Year** | {algo.year} |")
    if algo.difficulty:
        info_lines.append(f"| **Difficulty** | {get_difficulty_badge(algo.difficulty, 'en')} |")
    if algo.language:
        info_lines.append(f"| **Languages** | {', '.join(algo.language)} |")
    if cat_name:
        info_lines.append(f"| **Category** | [{cat_name}](../categories/{algo.category}/) |")

    info_lines.append("")

    links = []
    if algo.paper_url:
        links.append(f"- [📄 Paper]({algo.paper_url})")
    if algo.implementation_url:
        links.append(f"- [💻 Implementation]({algo.implementation_url})")

    if links:
        info_lines.append("## Links\n")
        info_lines.extend(links)
        info_lines.append("")

    if algo.related_tools:
        info_lines.append("## Related Tools\n")
        info_lines.append(" · ".join(f"`{tool}`" for tool in algo.related_tools))
        info_lines.append("")

    if algo.tags:
        info_lines.append("## Tags\n")
        tag_links = " ".join(f"[{tag}](../tags#{tag})" for tag in algo.tags)
        info_lines.append(tag_links)
        info_lines.append("")

    if algo.references:
        info_lines.append("## References\n")
        for ref in algo.references:
            ref_type = f" *({ref.type})*" if ref.type else ""
            info_lines.append(f"- [{ref.title or ref.url}]({ref.url}){ref_type}")
        info_lines.append("")

    return frontmatter + "\n" + "\n".join(info_lines)


def generate_en_algo_index(
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate English algorithm listing page."""
    rows = []
    for algo in sorted(algorithms, key=lambda a: a.name.lower()):
        cat_info = cat_map.get(algo.category)
        cat_name = (
            cat_info.name_en
            if cat_info and cat_info.name_en
            else (cat_info.name if cat_info else "-")
        )
        year = str(algo.year) if algo.year else "-"
        diff = get_difficulty_badge(algo.difficulty, "en") if algo.difficulty else "-"
        purpose = algo.purpose_en if algo.purpose_en else algo.purpose

        rows.append(
            f"| [{algo.name}]({algo.id}.md) | {year} | {cat_name} | {trim_text(purpose or '-', 40)} | {diff} |"
        )

    return f"""---
title: All Algorithms
---

# All Algorithms

**{len(algorithms)}** algorithms indexed.

| Algorithm | Year | Category | Purpose | Difficulty |
|-----------|------|----------|---------|------------|
{chr(10).join(rows)}
"""


def generate_en_category_page(
    cat: Category,
    algos: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate English category page."""
    cat_name = cat.name_en if cat.name_en else cat.name
    cat_desc = cat.description_en if cat.description_en else cat.description

    lines = [f"# {cat_name}\n"]

    if cat_desc:
        lines.append(f"> {cat_desc}\n")

    lines.append(f"**{len(algos)}** algorithms in this category.\n")

    for sub in cat.subcategories:
        sub_algos = sorted(
            [a for a in algos if a.subcategory == sub.id],
            key=lambda a: (a.year or 0, a.name),
            reverse=True,
        )
        if not sub_algos:
            continue

        sub_name = sub.name_en if sub.name_en else sub.name
        lines.append(f"## {sub_name}\n")

        if sub.description_en:
            lines.append(f"*{sub.description_en}*\n")
        elif sub.description:
            lines.append(f"*{sub.description}*\n")

        lines.append("| Algorithm | Year | Purpose |")
        lines.append("|-----------|------|---------|")
        for algo in sub_algos:
            year = str(algo.year) if algo.year else "-"
            purpose = algo.purpose_en if algo.purpose_en else algo.purpose
            lines.append(
                f"| [{algo.name}](../../algorithms/{algo.id}.md) | {year} | {trim_text(purpose or '-', 40)} |"
            )
        lines.append("")

    direct = sorted(
        [a for a in algos if not a.subcategory],
        key=lambda a: (a.year or 0, a.name),
        reverse=True,
    )
    if direct:
        lines.append("## Other\n")
        lines.append("| Algorithm | Year | Purpose |")
        lines.append("|-----------|------|---------|")
        for algo in direct:
            year = str(algo.year) if algo.year else "-"
            purpose = algo.purpose_en if algo.purpose_en else algo.purpose
            lines.append(
                f"| [{algo.name}](../../algorithms/{algo.id}.md) | {year} | {trim_text(purpose or '-', 40)} |"
            )

    return "\n".join(lines)


def generate_en_category_index(
    categories: list[Category],
    by_cat: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate English category overview page."""
    cats_with_algo = [
        (cat, len(by_cat.get(cat.id, []))) for cat in categories if by_cat.get(cat.id)
    ]

    lines = [
        """---
title: Categories
---

# Categories

"""
    ]

    for cat, count in sorted(cats_with_algo, key=lambda x: -x[1]):
        name = cat.name_en if cat.name_en else cat.name
        desc = cat.description_en if cat.description_en else cat.description
        lines.append(f"- **[{name}]({cat.id}/)** — {trim_text(desc, 60)} ({count} algorithms)")

    return "\n".join(lines)


def generate_en_tags_page(by_tag: dict[str, list[AlgorithmEntry]]) -> str:
    """Generate English tags page."""
    sorted_tags = sorted(by_tag.items(), key=lambda x: (-len(x[1]), x[0]))

    lines = [
        """---
title: Tags
---

# Tags Index

"""
    ]

    for tag, algos in sorted_tags:
        lines.append(f"## {tag}\n")
        lines.append(f"{len(algos)} algorithms\n")
        for algo in sorted(algos, key=lambda a: a.name):
            year = f" ({algo.year})" if algo.year else ""
            lines.append(f"- [{algo.name}](/en/algorithms/{algo.id}.md){year}")
        lines.append("")

    return "\n".join(lines)


# -----------------------------------------------------------------------------
# Main Generation
# -----------------------------------------------------------------------------


def write_all_pages(
    docs_dir: Path,
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> None:
    """Write all pages to docs/zh/ and docs/en/ directories."""

    # Chinese pages
    zh_dir = docs_dir / "zh"

    write_file(
        zh_dir / "index.md", generate_zh_index(categories, algorithms, cat_map, by_cat, by_tag)
    )
    write_file(zh_dir / "algorithms" / "index.md", generate_zh_algo_index(algorithms, cat_map))
    write_file(zh_dir / "categories" / "index.md", generate_zh_category_index(categories, by_cat))
    write_file(zh_dir / "tags.md", generate_zh_tags_page(by_tag))

    for algo in algorithms:
        write_file(zh_dir / "algorithms" / f"{algo.id}.md", generate_zh_algo_page(algo, cat_map))

    for cat in categories:
        algos = by_cat.get(cat.id, [])
        if algos:
            # Use directory form: {cat_id}/index.md
            write_file(
                zh_dir / "categories" / cat.id / "index.md",
                generate_zh_category_page(cat, algos, cat_map),
            )

    # English pages
    en_dir = docs_dir / "en"

    write_file(
        en_dir / "index.md", generate_en_index(categories, algorithms, cat_map, by_cat, by_tag)
    )
    write_file(en_dir / "algorithms" / "index.md", generate_en_algo_index(algorithms, cat_map))
    write_file(en_dir / "categories" / "index.md", generate_en_category_index(categories, by_cat))
    write_file(en_dir / "tags.md", generate_en_tags_page(by_tag))

    for algo in algorithms:
        write_file(en_dir / "algorithms" / f"{algo.id}.md", generate_en_algo_page(algo, cat_map))

    for cat in categories:
        algos = by_cat.get(cat.id, [])
        if algos:
            # Use directory form: {cat_id}/index.md
            write_file(
                en_dir / "categories" / cat.id / "index.md",
                generate_en_category_page(cat, algos, cat_map),
            )


def main(base_dir: Optional[Path] = None) -> int:
    base_dir = base_dir or get_base_dir()
    docs_dir = base_dir / "docs"

    print("Loading data...")
    categories, algorithms = load_data(base_dir)
    cat_map = build_category_map(categories)
    by_cat = build_algo_by_category(algorithms)
    by_tag = build_tag_index(algorithms)
    print(f"  {len(algorithms)} algorithms, {len(categories)} categories, {len(by_tag)} tags")

    print("Generating VitePress pages...")
    write_all_pages(docs_dir, categories, algorithms, cat_map, by_cat, by_tag)

    print(f"  Generated {len(algorithms)} algorithm pages (x2 languages)")
    print(
        f"  Generated {len([c for c in categories if by_cat.get(c.id)])} category pages (x2 languages)"
    )
    print("  Generated index pages and tags pages (x2 languages)")
    print("\nDone! Run 'cd docs && npm run dev' to preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
