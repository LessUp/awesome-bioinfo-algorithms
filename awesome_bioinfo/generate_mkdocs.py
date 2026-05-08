#!/usr/bin/env python3
"""
Generate MkDocs documentation from algorithm YAML data - Next Generation
Modern, interactive, and visually stunning documentation generator.

Usage:
    python awesome_bioinfo/generate_mkdocs.py
"""

import re
import shutil
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
    """Load categories and algorithms using DataStore.

    Raises:
        FileNotFoundError: If categories.yaml or algorithms directory not found
    """
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


def get_difficulty_badge_class(difficulty: str) -> str:
    """Get CSS class for difficulty badge."""
    return {
        "beginner": "aba-badge-difficulty-beginner",
        "intermediate": "aba-badge-difficulty-intermediate",
        "advanced": "aba-badge-difficulty-advanced",
    }.get(difficulty, "")


def get_category_icon(category_id: str) -> str:
    """Get Material icon for category."""
    icons = {
        "sequence-alignment": "material-align-horizontal-left",
        "assembly": "material-assemble",
        "variant-calling": "material-waveform",
        "expression-analysis": "material-chart-line",
        "protein-structure": "material-cube-outline",
        "phylogenetics": "material-family-tree",
        "functional-annotation": "material-label",
        "data-compression": "material-zip-box",
        "single-cell": "material-cell",
        "metagenomics": "material-bacteria",
        "epigenomics": "material-dna",
        "gene-prediction": "material-eye",
        "population-genetics": "material-account-group",
        "spatial-omics": "material-map-marker",
        "graph-genomics": "material-graph",
        "protein-language-model": "material-brain",
    }
    return icons.get(category_id, "material-flask")


# -----------------------------------------------------------------------------
# Index (landing page) - Modern Hero Design
# -----------------------------------------------------------------------------


def generate_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate the landing page with modern hero design."""
    total = len(algorithms)
    all_tags: set[str] = set()
    with_paper = 0
    with_impl = 0
    cats_with_algo = [cat for cat in categories if by_cat.get(cat.id)]

    for algo in algorithms:
        all_tags.update(algo.tags)
        if algo.paper_url:
            with_paper += 1
        if algo.implementation_url:
            with_impl += 1

    # Build hero stats
    stats_data = [
        (total, "算法条目"),
        (len(cats_with_algo), "研究方向"),
        (len(all_tags), "标签索引"),
        (with_paper, "论文链接"),
        (with_impl, "代码实现"),
    ]
    stats_cards = []
    for i, (value, label) in enumerate(stats_data):
        stats_cards.append(f'<div class="aba-stat-card aba-animate aba-animate-delay-{i}">')
        stats_cards.append(f'  <div class="aba-stat-value">{value}</div>')
        stats_cards.append(f'  <div class="aba-stat-label">{label}</div>')
        stats_cards.append("</div>")
    stats_html = "\n".join(stats_cards)

    # Build bento grid for categories
    cat_cards = []
    for i, cat in enumerate(categories):
        count = len(by_cat.get(cat.id, []))
        if count == 0:
            continue
        icon = get_category_icon(cat.id)
        featured = " aba-bento-featured" if i < 2 else ""
        delay = min(i, 4)
        cat_cards.append(
            f'<a class="aba-bento-card{featured} aba-animate aba-animate-delay-{delay}" '
            f'href="categories/{cat.id}/" data-category="{cat.id}">'
            f'  <div class="aba-bento-icon">:{icon}:</div>'
            f'  <div class="aba-bento-content">'
            f'    <div class="aba-bento-title">{cat.name}</div>'
            f'    <div class="aba-bento-desc">{trim_text(cat.description, 80)}</div>'
            f'    <div class="aba-bento-meta">'
            f'      <span class="aba-bento-count">{count} 个算法</span>'
            f'      <span class="aba-bento-arrow">→</span>'
            f"    </div>"
            f"  </div>"
            f"</a>"
        )

    # Build latest algorithms
    latest = sorted(
        [a for a in algorithms if a.year],
        key=lambda e: (e.year, e.name),
        reverse=True,
    )[:6]

    algo_cards = []
    for i, algo in enumerate(latest):
        cat_info = cat_map.get(algo.category)
        diff_badge = ""
        if algo.difficulty:
            diff_class = get_difficulty_badge_class(algo.difficulty)
            diff_text = DIFFICULTY_LABELS.get(algo.difficulty, algo.difficulty)
            diff_badge = f'<span class="aba-badge {diff_class}">{diff_text}</span>'

        year_badge = (
            f'<span class="aba-badge aba-badge-year">{algo.year}</span>'
            if algo.year
            else ""
        )
        complexity = algo.time_complexity or "-"

        delay = min(i, 4)
        algo_cards.append(
            f'<a class="aba-algo-card aba-animate aba-animate-delay-{delay}" '
            f'href="algorithms/{algo.id}/" data-category="{cat_info.name if cat_info else ""}" '
            f'data-year="{algo.year}" data-difficulty="{algo.difficulty}">'
            f'  <div class="aba-algo-header">'
            f'    <div class="aba-algo-badges">{year_badge}{diff_badge}</div>'
            f'    <div class="aba-algo-name">{algo.name}</div>'
            f"  </div>"
            f'  <div class="aba-algo-body">'
            f'    <div class="aba-algo-purpose">{trim_text(algo.purpose, 100)}</div>'
            f"  </div>"
            f'  <div class="aba-algo-footer">'
            f'    <span class="aba-algo-complexity">{complexity}</span>'
            f'    <svg class="aba-algo-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
            f'      <path d="M5 12h14M12 5l7 7-7 7"/>'
            f"    </svg>"
            f"  </div>"
            f"</a>"
        )

    # Year distribution data for chart
    year_counts: dict[int, int] = {}
    for algo in algorithms:
        if algo.year:
            year_counts[algo.year] = year_counts.get(algo.year, 0) + 1

    timeline_items = []
    for year in sorted(year_counts.keys(), reverse=True)[:8]:
        count = year_counts[year]
        timeline_items.append(
            f'<div class="aba-timeline-item">'
            f'  <div class="aba-timeline-year">{year}</div>'
            f'  <div class="aba-timeline-content">'
            f"    <strong>{count}</strong> 个算法发表"
            f"  </div>"
            f"</div>"
        )

    current_year = datetime.now().year

    return f"""---
hide:
  - navigation
  - toc
title: 首页
---

<!-- Hero Section -->
<div class="aba-hero">
  <div class="aba-hero-content">
    <div class="aba-hero-badge">
      <span>🧬</span>
      <span>当前收录 {total} 个算法</span>
    </div>
    <h1 class="aba-hero-title">
      <span class="aba-gradient-text">Awesome Bioinformatics</span><br>
      Algorithms
    </h1>
    <p class="aba-hero-subtitle">
      生物信息学算法结构化知识库 — 涵盖序列分析、蛋白质结构、基因组组装等 {len(cats_with_algo)} 个核心领域
    </p>
    <div class="aba-hero-actions">
      <a href="algorithms/" class="aba-btn aba-btn-primary">
        浏览全部算法 →
      </a>
      <a href="categories/" class="aba-btn aba-btn-secondary">
        分类浏览
      </a>
      <a href="tags/" class="aba-btn aba-btn-secondary">
        标签索引
      </a>
    </div>
    <div class="aba-stats-bar">
      {stats_html}
    </div>
  </div>
</div>

<!-- Categories Section -->
<div class="aba-section">

## :material-folder-multiple: 研究方向

<div class="aba-bento-grid">
{chr(10).join(cat_cards)}
</div>

</div>

<hr class="aba-divider">

<!-- Latest Section -->
<div class="aba-section">

## :material-clock-star: 最新收录

<div class="aba-algo-grid">
{chr(10).join(algo_cards)}
</div>

</div>

<hr class="aba-divider">

<!-- Timeline Section -->
<div class="aba-section">

## :material-history: 算法演进时间线

<div class="aba-timeline">
{chr(10).join(timeline_items)}
</div>

<a href="algorithms/" class="aba-btn aba-btn-secondary" style="margin-top: 2rem;">
  查看完整时间线 →
</a>

</div>

<hr class="aba-divider">

<!-- Stats Visualization Section -->
<div class="aba-section">

## :material-chart-box: 数据统计

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem;">

<div id="year-distribution"></div>

<div id="difficulty-chart"></div>

<div id="category-chart"></div>

</div>

</div>

<hr class="aba-divider">

<!-- Quick Links & CTA -->
<div class="aba-section" style="text-align: center; padding: 3rem 0;">

## :material-rocket-launch: 开始探索

<p style="font-size: 1.125rem; color: var(--md-default-fg-color--light); max-width: 600px; margin: 1rem auto 2rem;">
  无论您是生物信息学初学者还是领域专家，这里都有适合您的算法和工具。
</p>

<div style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;">

[:material-magnify: 搜索算法](algorithms/){{ .aba-btn .aba-btn-secondary }}

[:material-tag-multiple: 按标签筛选](tags/){{ .aba-btn .aba-btn-secondary }}

[:material-github: GitHub 仓库](https://github.com/LessUp/awesome-bioinfo-algorithms){{ .aba-btn .aba-btn-secondary target="_blank" }}

</div>

</div>

---

<div style="text-align: center; padding: 2rem 0; font-size: 0.875rem; color: var(--md-default-fg-color--light);">

Built with :material-heart: by the LessUp Community | © 2025-{current_year} | CC0 1.0 Universal

</div>
"""


# -----------------------------------------------------------------------------
# Algorithm detail page - Rich content layout
# -----------------------------------------------------------------------------


def generate_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    """Generate a single algorithm detail page with modern layout."""
    cat = cat_map.get(algo.category)
    cat_name = cat.name if cat else algo.category
    cat_id = algo.category
    sub = cat_map.get(algo.subcategory) if algo.subcategory else None
    sub_name = sub.name if sub else ""

    # Build badges
    badges = []
    if algo.year:
        badges.append(f'<span class="aba-badge aba-badge-year">{algo.year}年</span>')
    if cat_name:
        badges.append(f'<span class="aba-badge">{cat_name}</span>')
    if sub_name:
        badges.append(f'<span class="aba-badge">{sub_name}</span>')
    if algo.difficulty:
        diff_class = get_difficulty_badge_class(algo.difficulty)
        diff_text = DIFFICULTY_LABELS.get(algo.difficulty, algo.difficulty)
        badges.append(f'<span class="aba-badge {diff_class}">{diff_text}</span>')

    # Build info grid
    info_items = []
    if algo.purpose:
        info_items.append(f"""
<div class="aba-info-item">
  <div class="aba-info-label">:material-target: 用途</div>
  <div class="aba-info-value">{algo.purpose}</div>
</div>
""")
    if algo.time_complexity:
        info_items.append(f"""
<div class="aba-info-item">
  <div class="aba-info-label">:material-clock-fast: 时间复杂度</div>
  <div class="aba-info-value"><code>{algo.time_complexity}</code></div>
</div>
""")
    if algo.space_complexity:
        info_items.append(f"""
<div class="aba-info-item">
  <div class="aba-info-label">:material-memory: 空间复杂度</div>
  <div class="aba-info-value"><code>{algo.space_complexity}</code></div>
</div>
""")
    if algo.language:
        langs = "、".join(algo.language)
        info_items.append(f"""
<div class="aba-info-item">
  <div class="aba-info-label">:material-code: 实现语言</div>
  <div class="aba-info-value">{langs}</div>
</div>
""")

    # Links section
    links_section = []
    if algo.paper_url:
        links_section.append(f'''
<a href="{algo.paper_url}" class="aba-btn aba-btn-secondary" target="_blank">
  :material-file-document: 论文链接
</a>
''')
    if algo.implementation_url:
        links_section.append(f'''
<a href="{algo.implementation_url}" class="aba-btn aba-btn-secondary" target="_blank">
  :material-github: 代码实现
</a>
''')

    # Related tools
    tools_section = ""
    if algo.related_tools:
        tool_links = " · ".join(f"`{tool}`" for tool in algo.related_tools)
        tools_section = f"""
### :material-tools: 相关工具

{tool_links}
"""

    # Tags
    tags_section = ""
    if algo.tags:
        tag_links = " ".join(
            f'[<span class="aba-badge">{tag}</span>](tags.md#{tag})' for tag in algo.tags
        )
        tags_section = f"""
### :material-tag: 标签

<div class="aba-tag-cloud">
{tag_links}
</div>
"""

    # References
    refs_section = ""
    if algo.references:
        refs = "\n".join(
            f"- [{ref.title or ref.url}]({ref.url})"
            + (f" *({ref.type})*" if ref.type else "")
            for ref in algo.references
        )
        refs_section = f"""
### :material-book-open: 参考资料

{refs}
"""

    return f"""# {algo.name}

<!-- Detail Hero -->
<div class="aba-detail-hero">
  <div class="aba-detail-header">
    <div class="aba-detail-badges">
      {chr(10).join(badges)}
    </div>
    <h1 class="aba-detail-title">{algo.name}</h1>
    <div class="aba-detail-description">
      {algo.description.strip().replace(chr(10), " ")}
    </div>
  </div>
</div>

<!-- Info Grid -->
<div class="aba-info-grid">
  {chr(10).join(info_items)}
</div>

<!-- Quick Actions -->
<div style="display: flex; flex-wrap: wrap; gap: 0.75rem; margin: 1.5rem 0;">
  {chr(10).join(links_section)}
  <a href="../categories/{cat_id}" class="aba-btn aba-btn-secondary">
    :material-folder: 查看分类
  </a>
</div>

<hr class="aba-divider">

<!-- Additional Info -->
{tools_section}

{tags_section}

{refs_section}

---

<div style="font-size: 0.875rem; color: var(--md-default-fg-color--light);">

:material-folder: 分类：<a href="../categories/{cat_id}">{cat_name}</a> {f' / <a href="../categories/{cat_id}#{sub.id}">{sub_name}</a>' if sub and sub_name else ""} |
:material-identifier: ID：<code>{algo.id}</code>

</div>
"""


# -----------------------------------------------------------------------------
# Category pages - Modern data table layout
# -----------------------------------------------------------------------------


def generate_category_page(
    cat: Category,
    algos: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate a category page with subcategory sections."""
    lines = [
        f"# {cat.name}",
        "",
    ]
    if cat.description:
        lines.append(f"> {cat.description}")
        lines.append("")

    lines.append(f"**{len(algos)}** 个算法收录于该分类。")
    lines.append("")

    # Add data attributes for JS filtering
    for sub in cat.subcategories:
        sub_algos = sorted(
            [a for a in algos if a.subcategory == sub.id],
            key=lambda a: (a.year or 0, a.name),
            reverse=True,
        )
        if not sub_algos:
            continue

        lines.append(f"## {sub.name} ({sub.name_en})")
        lines.append("")
        if sub.description:
            lines.append(f"*{sub.description}*")
            lines.append("")

        # Modern table
        lines.append('<div class="aba-table-container">')
        lines.append('<table class="aba-table">')
        lines.append("<thead><tr><th>算法</th><th>年份</th><th>用途</th><th>难度</th></tr></thead>")
        lines.append("<tbody>")

        for algo in sub_algos:
            diff_class = get_difficulty_badge_class(algo.difficulty)
            diff = DIFFICULTY_LABELS_BILINGUAL.get(algo.difficulty, "-")

            lines.append(
                f'<tr data-category="{cat.name}" data-difficulty="{algo.difficulty}" data-year="{algo.year}">'
                f'<td><a href="../algorithms/{algo.id}/">{algo.name}</a></td>'
                f"<td>{algo.year or '-'}</td>"
                f"<td>{trim_text(algo.purpose or '-', 50)}</td>"
                f'<td><span class="aba-badge {diff_class}">{diff}</span></td>'
                f"</tr>"
            )

        lines.append("</tbody>")
        lines.append("</table>")
        lines.append("</div>")
        lines.append("")

    # Algorithms without subcategory
    direct = sorted(
        [a for a in algos if not a.subcategory],
        key=lambda a: (a.year or 0, a.name),
        reverse=True,
    )
    if direct:
        lines.append("## 其他")
        lines.append("")
        lines.append('<div class="aba-table-container">')
        lines.append('<table class="aba-table">')
        lines.append("<thead><tr><th>算法</th><th>年份</th><th>用途</th></tr></thead>")
        lines.append("<tbody>")

        for algo in direct:
            lines.append(
                f'<tr data-category="{cat.name}" data-year="{algo.year}">'
                f'<td><a href="../algorithms/{algo.id}/">{algo.name}</a></td>'
                f"<td>{algo.year or '-'}</td>"
                f"<td>{trim_text(algo.purpose or '-', 50)}</td>"
                f"</tr>"
            )

        lines.append("</tbody>")
        lines.append("</table>")
        lines.append("</div>")

    return "\n".join(lines)


def generate_category_index(
    categories: list[Category],
    by_cat: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate category overview page."""
    cats_with_algo = [
        (cat, len(by_cat.get(cat.id, []))) for cat in categories if by_cat.get(cat.id)
    ]

    # Build bento grid
    cat_cards = []
    for i, (cat, count) in enumerate(sorted(cats_with_algo, key=lambda x: -x[1])):
        icon = get_category_icon(cat.id)
        delay = min(i, 4)
        cat_cards.append(
            f'<a class="aba-bento-card aba-animate aba-animate-delay-{delay}" href="{cat.id}/">'
            f'  <div class="aba-bento-icon">:{icon}:</div>'
            f'  <div class="aba-bento-title">{cat.name}</div>'
            f'  <div class="aba-bento-desc">{trim_text(cat.description, 80)}</div>'
            f'  <div class="aba-bento-meta">'
            f'    <span class="aba-bento-count">{count} 个算法</span>'
            f'    <span class="aba-bento-arrow">→</span>'
            f"  </div>"
            f"</a>"
        )

    return f"""# 分类总览

共 **{len(cats_with_algo)}** 个研究方向，按算法数量排序。

<div class="aba-bento-grid">
{chr(10).join(cat_cards)}
</div>

## 数据概览

<div id="category-chart"></div>
"""


def generate_tags_page(by_tag: dict[str, list[AlgorithmEntry]]) -> str:
    """Generate tags index page with interactive tag cloud."""
    sorted_tags = sorted(by_tag.items(), key=lambda x: (-len(x[1]), x[0]))
    max_count = max(len(algos) for algos in by_tag.values()) if by_tag else 1

    # Size calculation for cloud effect
    def get_size_class(count: int) -> int:
        ratio = count / max_count
        if ratio > 0.8:
            return 5
        if ratio > 0.6:
            return 4
        if ratio > 0.4:
            return 3
        if ratio > 0.2:
            return 2
        return 1

    # Build tag cloud
    tag_links = []
    for tag, algos in sorted_tags[:50]:  # Top 50 tags
        size = get_size_class(len(algos))
        tag_links.append(
            f'<a href="#{tag}" class="aba-tag aba-tag-size-{size}" data-tag="{tag}">'
            f'{tag}<span class="aba-tag-count">{len(algos)}</span></a>'
        )

    # Build tag details
    tag_sections = []
    for tag, algos in sorted_tags:
        algo_list = "\n".join(
            f"- [{algo.name} ({algo.year})](algorithms/{algo.id}.md)"
            if algo.year
            else f"- [{algo.name}](algorithms/{algo.id}.md)"
            for algo in sorted(algos, key=lambda a: a.name)
        )
        tag_sections.append(
            f'## <span id="{tag}">{tag}</span> {{ #{tag} }}\n\n{len(algos)} 个算法\n\n{algo_list}\n'
        )

    return f"""# 标签索引

共 **{len(by_tag)}** 个标签。点击标签快速跳转。

<div class="aba-tag-cloud">
{chr(10).join(tag_links)}
</div>

<hr class="aba-divider">

{chr(10).join(tag_sections[:30])}
"""


# -----------------------------------------------------------------------------
# Algorithm index page - Searchable table
# -----------------------------------------------------------------------------


def generate_algo_index(
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    """Generate the full algorithm listing as a searchable table."""
    rows = []
    for algo in sorted(algorithms, key=lambda a: a.name.lower()):
        cat_info = cat_map.get(algo.category)
        cat_name = cat_info.name if cat_info else "-"
        year = str(algo.year) if algo.year else "-"
        diff_class = get_difficulty_badge_class(algo.difficulty)
        diff = DIFFICULTY_LABELS_BILINGUAL.get(algo.difficulty, "-")

        rows.append(
            f'<tr data-category="{cat_name}" data-difficulty="{algo.difficulty}" '
            f'data-year="{algo.year}">'
            f'<td><a href="{algo.id}/">{algo.name}</a></td>'
            f"<td>{year}</td>"
            f"<td>{cat_name}</td>"
            f"<td>{trim_text(algo.purpose or '-', 45)}</td>"
            f'<td><span class="aba-badge {diff_class}">{diff}</span></td>'
            f"</tr>"
        )

    # Grid view cards (for JS toggle)
    grid_cards = []
    for i, algo in enumerate(sorted(algorithms, key=lambda a: a.name.lower())[:20]):
        cat_info = cat_map.get(algo.category)
        delay = min(i, 4)
        diff_badge = ""
        if algo.difficulty:
            diff_class = get_difficulty_badge_class(algo.difficulty)
            diff_text = DIFFICULTY_LABELS.get(algo.difficulty, algo.difficulty)
            diff_badge = f'<span class="aba-badge {diff_class}">{diff_text}</span>'

        year_badge = (
            f'<span class="aba-badge aba-badge-year">{algo.year}</span>'
            if algo.year
            else ""
        )

        grid_cards.append(
            f'<a class="aba-algo-card aba-animate aba-animate-delay-{delay}" '
            f'href="{algo.id}/" data-category="{cat_info.name if cat_info else ""}" '
            f'data-year="{algo.year}" data-difficulty="{algo.difficulty}">'
            f'  <div class="aba-algo-header">'
            f'    <div class="aba-algo-badges">{year_badge}{diff_badge}</div>'
            f'    <div class="aba-algo-name">{algo.name}</div>'
            f"  </div>"
            f'  <div class="aba-algo-body">'
            f'    <div class="aba-algo-purpose">{trim_text(algo.purpose or "", 80)}</div>'
            f"  </div>"
            f'  <div class="aba-algo-footer">'
            f'    <span class="aba-algo-complexity">{cat_info.name if cat_info else ""}</span>'
            f'    <svg class="aba-algo-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">'
            f'      <path d="M5 12h14M12 5l7 7-7 7"/>'
            f"    </svg>"
            f"  </div>"
            f"</a>"
        )

    return f"""# 全部算法

共收录 **{len(algorithms)}** 个算法。使用顶部搜索框或下方筛选器快速定位。

<div class="aba-algo-grid">
{chr(10).join(grid_cards)}
</div>

## 完整列表

<div class="aba-table-container">
<table class="aba-table">
<thead>
<tr>
<th>算法</th>
<th>年份</th>
<th>分类</th>
<th>用途</th>
<th>难度</th>
</tr>
</thead>
<tbody>
{chr(10).join(rows)}
</tbody>
</table>
</div>
"""


# -----------------------------------------------------------------------------
# Nav generation
# -----------------------------------------------------------------------------


def generate_nav_yaml(
    categories: list[Category],
    by_cat: dict[str, list[AlgorithmEntry]],
) -> str:
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
        if by_cat.get(cat.id):
            lines.append(f"    - {cat.name}: categories/{cat.id}.md")
    lines.append("  - 标签: tags.md")
    return "\n".join(lines) + "\n"


def update_mkdocs_yml(
    base_dir: Path,
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> None:
    """Update mkdocs.yml with dynamic stats and nav."""
    mkdocs_yml = base_dir / "mkdocs" / "mkdocs.yml"
    with open(mkdocs_yml, encoding="utf-8") as f:
        text = f.read()

    # Calculate stats
    cats_with_algo = len([c for c in categories if by_cat.get(c.id)])

    # Update stats in extra section (inject after "generator: false")
    stats_block = f"""
  # Dynamic stats (updated by generate_mkdocs.py)
  stats:
    algorithms: {len(algorithms)}
    categories: {cats_with_algo}
    tags: {len(by_tag)}"""

    # Find "generator: false" and insert stats after it
    if "stats:" not in text:
        text = text.replace("generator: false", "generator: false" + stats_block)

    # Remove existing nav block if present
    text = re.sub(r"(?m)^nav:.*?(?=^\S|\Z)", "", text, flags=re.DOTALL).rstrip() + "\n\n"

    # Append generated nav
    text += generate_nav_yaml(categories, by_cat)

    with open(mkdocs_yml, "w", encoding="utf-8") as f:
        f.write(text)


def write_generated_pages(
    base_dir: Path,
    mkdocs_dir: Path,
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> None:
    # Clean previous generated docs (keep stylesheets and javascripts)
    if mkdocs_dir.exists():
        for item in mkdocs_dir.iterdir():
            if item.name in ("stylesheets", "javascripts", ".gitkeep"):
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
            mkdocs_dir / "algorithms" / f"{algo.id}.md",
            generate_algo_page(algo, cat_map),
        )

    # Algorithm index
    write_file(
        mkdocs_dir / "algorithms" / "index.md",
        generate_algo_index(algorithms, cat_map),
    )

    # Category pages
    for cat in categories:
        algos = by_cat.get(cat.id, [])
        if algos:
            write_file(
                mkdocs_dir / "categories" / f"{cat.id}.md",
                generate_category_page(cat, algos, cat_map),
            )

    # Category index
    write_file(
        mkdocs_dir / "categories" / "index.md",
        generate_category_index(categories, by_cat),
    )

    # Tags
    write_file(mkdocs_dir / "tags.md", generate_tags_page(by_tag))

    # Update mkdocs.yml with stats and nav
    update_mkdocs_yml(base_dir, categories, algorithms, by_cat, by_tag)


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
    print(f"  Generated {len([c for c in categories if by_cat.get(c.id)])} category pages")
    print("  Generated algorithm index, category index, and tags page")
    print("\nDone! Run 'mkdocs serve -f mkdocs/mkdocs.yml' to preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
