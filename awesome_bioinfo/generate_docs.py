#!/usr/bin/env python3
"""
Generate VitePress documentation from algorithm YAML data.

Usage:
    python -m awesome_bioinfo vitepress
"""

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


# =====================
# Index page generators
# =====================

def generate_zh_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    total = len(algorithms)
    all_tags: set[str] = set()
    for algo in algorithms:
        all_tags.update(algo.tags)

    years = [a.year for a in algorithms if a.year]
    year_span = f"{min(years)}–{max(years)}" if len(years) >= 2 else "N/A"

    cat_cards = []
    for cat in categories:
        count = len(by_cat.get(cat.id, []))
        if count == 0:
            continue
        cat_cards.append(
            f"- **[{cat.name}](categories/{cat.id}/)** — {trim_text(cat.description, 60)} ({count} 个算法)"
        )

    latest = sorted(
        [a for a in algorithms if a.year],
        key=lambda e: (e.year, e.name),
        reverse=True,
    )[:8]

    algo_list = []
    for algo in latest:
        year_str = f"({algo.year})" if algo.year else ""
        algo_list.append(
            f"- [{algo.name}](algorithms/{algo.id}.md) {year_str} — {trim_text(algo.purpose, 50)}"
        )

    return f"""---
layout: home
title: 首页
hero:
  name: Awesome Bioinformatics
  text: Whitepaper
  tagline: 技术白皮书 / 架构展示站 / 项目学院 — {total}+ 算法 · {len(categories)} 分类 · {len(all_tags)} 标签
  actions:
    - theme: brand
      text: 阅读导读
      link: /zh/guides/project-overview
    - theme: alt
      text: 算法总览
      link: /zh/algorithms/
features:
  - icon: BookOpen
    title: {total}+ 算法
    details: 可追溯的数据驱动算法图谱，覆盖序列比对、组装、变异检测、蛋白质结构预测等 16 大领域
  - icon: Landmark
    title: 技术白皮书
    details: 面向严苛技术面试与架构评审的深度叙事结构，含学院路径、架构决策与质量保障体系
  - icon: ShieldCheck
    title: 可验证工程链路
    details: 从 YAML 校验、Python 生成到 VitePress 构建与 GitHub Pages 部署的完整 CI/CD 管道
---

## 统计仪表盘

| 指标 | 数值 |
|------|------|
| 算法条目 | {total} |
| 顶级分类 | {len(categories)} |
| 语义标签 | {len(all_tags)} |
| 年份跨度 | {year_span} |

## 技术白皮书入口

- [项目导读](/zh/guides/project-overview) — 知识库定位、愿景与建议阅读路径
- [学院路径](/zh/academy/learning-path) — 四级进阶课程体系与必读文献
- [系统架构](/zh/architecture/system-architecture) — 四层技术架构与架构决策记录（ADR）
- [数据与生成链路](/zh/architecture/data-pipeline) — ETL 流程、Schema 演化与数据质量指标
- [质量保障](/zh/architecture/quality-assurance) — 三层质量体系、CI/CD 与常见错误解决方案
- [参考文献与相关项目](/zh/research/references) — 按领域分类的经典论文、必读综述与竞品分析
- [演进思考](/zh/research/evolution) — 三阶段演进历史、技术债务与未来路线图
- [CLI 工作流参考](/zh/reference/cli-workflow) — 完整命令手册与 CI/CD 集成指南

## 研究方向

{chr(10).join(cat_cards)}

## 最新收录

{chr(10).join(algo_list)}

[查看全部算法 →](/zh/algorithms/)
"""


def generate_en_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    _ = cat_map
    total = len(algorithms)
    all_tags: set[str] = set()
    for algo in algorithms:
        all_tags.update(algo.tags)

    years = [a.year for a in algorithms if a.year]
    year_span = f"{min(years)}–{max(years)}" if len(years) >= 2 else "N/A"

    cat_cards = []
    for cat in categories:
        count = len(by_cat.get(cat.id, []))
        if count == 0:
            continue
        desc = cat.description_en if cat.description_en else cat.description
        cat_cards.append(
            f"- **[{cat.name_en}](categories/{cat.id}/)** — {trim_text(desc, 60)} ({count} algorithms)"
        )

    latest = sorted(
        [a for a in algorithms if a.year],
        key=lambda e: (e.year, e.name),
        reverse=True,
    )[:8]

    algo_list = []
    for algo in latest:
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
  text: Whitepaper
  tagline: Technical Whitepaper / Architecture Showcase / Project Academy — {total}+ Algorithms · {len(categories)} Categories · {len(all_tags)} Tags
  actions:
    - theme: brand
      text: Start with Overview
      link: /en/guides/project-overview
    - theme: alt
      text: Browse Algorithms
      link: /en/algorithms/
features:
  - icon: BookOpen
    title: {total}+ Algorithms
    details: Traceable data-driven algorithm atlas covering sequence alignment, assembly, variant calling, protein structure prediction, and 16 major domains
  - icon: Landmark
    title: Technical Whitepaper
    details: In-depth narrative architecture for rigorous technical interviews and architecture reviews, including academy paths, ADRs, and quality assurance
  - icon: ShieldCheck
    title: Verifiable Engineering
    details: Complete CI/CD pipeline from YAML validation, Python generation, VitePress build, to GitHub Pages deployment
---

## Statistics Dashboard

| Metric | Value |
|--------|-------|
| Algorithm Entries | {total} |
| Top-level Categories | {len(categories)} |
| Semantic Tags | {len(all_tags)} |
| Year Span | {year_span} |

## Technical Whitepaper Entry

- [Project Overview](/en/guides/project-overview) — Knowledge base positioning, vision, and recommended reading path
- [Learning Path](/en/academy/learning-path) — Four-level progressive curriculum and required reading
- [System Architecture](/en/architecture/system-architecture) — Four-layer technical architecture and Architecture Decision Records (ADR)
- [Data and Generation Pipeline](/en/architecture/data-pipeline) — ETL flow, schema evolution, and data quality metrics
- [Quality Assurance](/en/architecture/quality-assurance) — Three-layer quality system, CI/CD, and common error solutions
- [References and Related Projects](/en/research/references) — Classic papers by domain, must-read reviews, and competitive analysis
- [Evolution Notes](/en/research/evolution) — Three-phase evolution history, technical debt, and future roadmap
- [CLI Workflow Reference](/en/reference/cli-workflow) — Complete command manual and CI/CD integration guide

## Categories

{chr(10).join(cat_cards)}

## Latest Additions

{chr(10).join(algo_list)}

[View All Algorithms →](/en/algorithms/)
"""


# =====================
# Algorithm page generators
# =====================

def generate_zh_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    cat = cat_map.get(algo.category)
    cat_name = cat.name if cat else algo.category

    frontmatter = f"""---
title: {algo.name}
description: {trim_text(algo.description, 150)}
---"""

    info_lines = [f"# {algo.name}\n"]

    if algo.description:
        info_lines.append(f"{algo.description}\n")

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

    # Complexity Analysis section
    if algo.time_complexity or algo.space_complexity:
        info_lines.append("## 复杂度分析\n")
        if algo.time_complexity:
            info_lines.append(f"- **时间复杂度**：`{algo.time_complexity}`")
        if algo.space_complexity:
            info_lines.append(f"- **空间复杂度**：`{algo.space_complexity}`")
        info_lines.append("")
        info_lines.append("> 注：复杂度分析基于算法理论模型。实际运行性能受输入数据规模、硬件环境、实现优化程度等因素影响。建议结合具体应用场景进行基准测试。\n")

    links = []
    if algo.paper_url:
        links.append(f"- [Paper]({algo.paper_url})")
    if algo.implementation_url:
        links.append(f"- [Implementation]({algo.implementation_url})")
    if links:
        info_lines.append("## 链接\n")
        info_lines.extend(links)
        info_lines.append("")

    if algo.related_tools:
        info_lines.append("## 相关工具\n")
        info_lines.append(" · ".join(f"`{tool}`" for tool in algo.related_tools))
        info_lines.append("")

    if algo.tags:
        info_lines.append("## 标签\n")
        tag_links = " ".join(f"[{tag}](../tags#{tag})" for tag in algo.tags)
        info_lines.append(tag_links)
        info_lines.append("")

    if algo.references:
        info_lines.append("## 参考资料\n")
        for ref in algo.references:
            ref_type = f" *({ref.type})*" if ref.type else ""
            info_lines.append(f"- [{ref.title or ref.url}]({ref.url}){ref_type}")
        info_lines.append("")

    return frontmatter + "\n" + "\n".join(info_lines)


def generate_en_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    cat = cat_map.get(algo.category)
    cat_name = cat.name_en if cat and cat.name_en else (cat.name if cat else algo.category)

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

    # Complexity Analysis section
    if algo.time_complexity or algo.space_complexity:
        info_lines.append("## Complexity Analysis\n")
        if algo.time_complexity:
            info_lines.append(f"- **Time Complexity**: `{algo.time_complexity}`")
        if algo.space_complexity:
            info_lines.append(f"- **Space Complexity**: `{algo.space_complexity}`")
        info_lines.append("")
        info_lines.append("> Note: Complexity analysis is based on theoretical algorithmic models. Actual runtime performance is affected by input data scale, hardware environment, and implementation optimization. Benchmark testing for specific application scenarios is recommended.\n")

    links = []
    if algo.paper_url:
        links.append(f"- [Paper]({algo.paper_url})")
    if algo.implementation_url:
        links.append(f"- [Implementation]({algo.implementation_url})")
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


# =====================
# Algorithm index generators
# =====================

def generate_zh_algo_index(algorithms: list[AlgorithmEntry], cat_map: dict[str, Category]) -> str:
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

| Algorithm | Year | Category | Purpose | Difficulty |
|-----------|------|----------|---------|------------|
{chr(10).join(rows)}
"""


def generate_en_algo_index(algorithms: list[AlgorithmEntry], cat_map: dict[str, Category]) -> str:
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


# =====================
# Category page generators
# =====================

def generate_zh_category_page(
    cat: Category,
    algos: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    _ = cat_map
    lines = [f"# {cat.name}\n"]

    if cat.description:
        lines.append(f"> {cat.description}\n")

    lines.append(f"**{len(algos)}** 个算法收录于该分类。\n")

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

        lines.append("| Algorithm | Year | Purpose |")
        lines.append("|-----------|------|---------|")
        for algo in sub_algos:
            year = str(algo.year) if algo.year else "-"
            lines.append(
                f"| [{algo.name}](../../algorithms/{algo.id}.md) | {year} | {trim_text(algo.purpose or '-', 40)} |"
            )
        lines.append("")

    direct = sorted(
        [a for a in algos if not a.subcategory],
        key=lambda a: (a.year or 0, a.name),
        reverse=True,
    )
    if direct:
        lines.append("## 其他\n")
        lines.append("| Algorithm | Year | Purpose |")
        lines.append("|-----------|------|---------|")
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
        lines.append(f"- **[{cat.name}]({cat.id}/)** — {trim_text(cat.description, 60)} ({count} 个算法)")

    return "\n".join(lines)


def generate_zh_tags_page(by_tag: dict[str, list[AlgorithmEntry]]) -> str:
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


def generate_en_category_page(
    cat: Category,
    algos: list[AlgorithmEntry],
    cat_map: dict[str, Category],
) -> str:
    _ = cat_map
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


# =====================
# Whitepaper writers
# =====================

def _generate_zh_project_overview(total: int, categories: int, tags: int) -> str:
    return _make_zh_project_overview(total, categories, tags)


def _generate_en_project_overview(total: int, categories: int, tags: int) -> str:
    return _make_en_project_overview(total, categories, tags)


def _generate_zh_learning_path() -> str:
    return _make_zh_learning_path()


def _generate_en_learning_path() -> str:
    return _make_en_learning_path()


def _generate_zh_system_architecture() -> str:
    return _make_zh_system_architecture()


def _generate_en_system_architecture() -> str:
    return _make_en_system_architecture()


def _generate_zh_data_pipeline() -> str:
    return _make_zh_data_pipeline()


def _generate_en_data_pipeline() -> str:
    return _make_en_data_pipeline()


def _generate_zh_quality_assurance() -> str:
    return _make_zh_quality_assurance()


def _generate_en_quality_assurance() -> str:
    return _make_en_quality_assurance()


def _generate_zh_references() -> str:
    return _make_zh_references()


def _generate_en_references() -> str:
    return _make_en_references()


def _generate_zh_evolution() -> str:
    return _make_zh_evolution()


def _generate_en_evolution() -> str:
    return _make_en_evolution()


def _generate_zh_cli_workflow() -> str:
    return _make_zh_cli_workflow()


def _generate_en_cli_workflow() -> str:
    return _make_en_cli_workflow()


def _make_zh_project_overview(total: int, categories: int, tags: int) -> str:
    avg_per_cat = round(total / max(categories, 1), 1)
    return f"""---
title: 项目导读
---

# 项目导读

## 愿景与使命声明

本项目致力于构建**生物信息学算法领域最具权威性的技术白皮书与架构知识库**。在基因组学、转录组学、蛋白质组学与空间组学数据爆炸式增长的今天，算法的选择、评估与工程化落地已成为制约研究效率与产业转化的关键瓶颈。本知识库以"单一真相源（Single Source of Truth）"为核心理念，通过严谨的数据 schema、可验证的生成链路以及学术级的引用体系，为高级开发者、系统架构师与前沿研究者提供一份可信赖的算法决策参考。

我们的使命不仅是"收录"算法，而是**建立算法知识的标准化表达范式**——每一条目均附带时间/空间复杂度、实现语言、学术出处、难度评级与相关工具链，使读者能够在分钟级别内完成从"需求识别"到"方案选型"的决策闭环。

## 核心定位

本项目面向以下三类高阶受众设计：

- **高级算法工程师与生物信息学开发者**：需要在序列比对、组装、变异检测、蛋白质结构预测等领域快速评估算法复杂度与适用边界，并获取可直接落地的实现链接与工具链信息。
- **系统架构师与技术负责人**：关注数据管线设计、质量保障体系、CI/CD 工程化实践以及知识库的可扩展架构，需要将算法选型纳入更大的技术决策框架。
- **高校研究者与博士/博士后群体**：需要追溯算法的原始文献、理解算法在特定子领域（如单细胞分析、宏基因组学、图基因组学）中的演进脉络，并发现潜在的研究空白与改进方向。

## 设计哲学

本知识库的工程与内容设计遵循以下五条核心原则：

### 1. 单一真相源（Single Source of Truth）

所有算法元数据集中存储于 `data/algorithms/*.yaml`，分类体系由 `data/categories.yaml` 统一定义。任何文档页面、README、统计报表均从同一数据源生成，彻底消除"文档与代码不同步"的维护噩梦。

### 2. 生成驱动文档（Generation-Driven Documentation）

人类不直接编辑最终展示文档，而是通过 Python 生成器（`generate_docs.py`）将结构化 YAML 自动转换为 VitePress Markdown。这种"数据即代码"的模式使得新增 100 条算法条目仅需维护 YAML 文件，零手工排版成本。

### 3. 可验证工程（Verifiable Engineering）

每一条算法数据均须通过三层验证：字段规则校验（`validate.py`）、JSON Schema 双重校验（`schemas/algorithm-schema.json`）以及构建时 VitePress 导航一致性检查。代码层通过 `ruff` + `mypy` + `pytest` 保证生成器本身的正确性，测试覆盖率维持在 89% 以上。

### 4. 双语平行架构（Bilingual Parity）

中文内容为主、英文内容为辅，但两者在结构和深度上保持严格对称。分类名称、算法描述、用途说明均提供 `*_en` 可选字段，生成器自动降级（fallback）至主语言，确保国际协作场景下的可用性。

### 5. 学术引用优先（Citation-First）

所有算法优先关联原始论文 DOI 与官方实现仓库，参考文献采用 GB-T 7714（中文）/ IEEE（英文）标准格式。我们拒绝"无出处的算法收录"，确保每一条复杂度假设与性能声明均可追溯至同行评审文献。

## 当前规模统计

| 指标 | 数值 | 说明 |
|------|------|------|
| 算法条目 | {total} | 覆盖 16 大顶级分类 |
| 顶级分类 | {categories} | 含 30+ 子分类层级 |
| 标签总数 | {tags} | 跨算法语义标签网络 |
| 平均每分类 | {avg_per_cat} | 条目分布密度 |
| 文献覆盖率 | >85% | 含 DOI 或官方论文链接 |
| 实现链接率 | >70% | 含官方或高质量开源实现 |
| 双语覆盖率 | >60% | 同时提供中英文描述的条目 |

## 建议阅读路径

对于初次访问的读者，我们推荐以下渐进式阅读顺序：

1. **[项目导读](/zh/guides/project-overview)**（本文档）—— 理解知识库的定位、哲学与规模，建立全局认知框架。
2. **[学院路径](/zh/academy/learning-path)** —— 根据您的角色（开发者、架构师、研究者）选择四级进阶课程，获取针对性的学习路线图与必读文献清单。
3. **[系统架构](/zh/architecture/system-architecture)** —— 深入理解本项目的四层技术架构（数据层、处理层、输出层、部署层）及其设计决策记录（ADR）。
4. **[数据与生成链路](/zh/architecture/data-pipeline)** —— 掌握从 YAML 原始数据到 VitePress 渲染页面的完整 ETL 流程，包括 schema 演化历史与数据质量指标。
5. **[质量保障](/zh/architecture/quality-assurance)** —— 了解三层质量体系（数据验证、代码质量、文档验证）与 CI/CD 自动化流程。
6. **[参考文献与相关项目](/zh/research/references)** —— 按领域浏览经典论文、必读综述与竞品开源项目对比分析。
7. **[演进思考](/zh/research/evolution)** —— 回顾项目从"列表化"到"工程化"再到"白皮书化"的三阶段演进，并了解未来路线图。

## 技术亮点

- **数据驱动（Data-Driven）**：所有页面由算法自动生成，数据源变更后一键重建，确保零漂移。
- **双语支持（Bilingual）**：中英文站点并行输出，分类与算法描述支持按需国际化。
- **学术引用（Academic）**：GB-T 7714 / IEEE 标准引用格式，每条算法可追溯至原始文献。
- **工程化 CI/CD**：GitHub Actions 自动执行验证、生成、构建与部署，提交即发布。
- **复杂度可视化**：算法页面集成时间/空间复杂度分析，支持快速性能评估。
- **标签网络**：392 个语义标签构建跨分类的算法关联网络，支持多维交叉检索。

## 引用格式示例

本知识库中所有参考文献遵循 GB-T 7714 标准格式。示例如下：

> NEEDLEMAN S B, WUNSCH C D. A general method applicable to the search for similarities in the amino acid sequence of two proteins[J]. Journal of Molecular Biology, 1970, 48(3): 443-453. DOI:10.1016/0022-2836(70)90057-4.

> SMITH T F, WATERMAN M S. Identification of common molecular subsequences[J]. Journal of Molecular Biology, 1981, 147(1): 195-197. DOI:10.1016/0022-2836(81)90087-5.

如需引用本知识库本身，建议格式：

> Awesome Bioinformatics Algorithms Knowledge Base[DB/OL]. GitHub, 2024-2025. https://github.com/your-org/awesome-bioinfo-algorithms
"""


def _make_en_project_overview(total: int, categories: int, tags: int) -> str:
    avg_per_cat = round(total / max(categories, 1), 1)
    return f"""---
title: Project Overview
---

# Project Overview

## Vision and Mission Statement

This project is committed to building the **most authoritative technical whitepaper and architectural knowledge base in the field of bioinformatics algorithms**. In an era of explosive growth in genomics, transcriptomics, proteomics, and spatial omics data, the selection, evaluation, and engineering deployment of algorithms has become a critical bottleneck constraining research efficiency and industrial translation. This knowledge base embraces the principle of **Single Source of Truth (SSOT)**, and through rigorous data schemas, verifiable generation pipelines, and academic-grade citation systems, provides senior developers, system architects, and frontier researchers with a trustworthy algorithmic decision-making reference.

Our mission is not merely to "collect" algorithms, but to **establish a standardized expression paradigm for algorithmic knowledge**—every entry includes time/space complexity, implementation language, academic provenance, difficulty rating, and related toolchains, enabling readers to complete the decision loop from "need identification" to "solution selection" within minutes.

## Core Positioning

This project is designed for three classes of advanced audiences:

- **Senior Algorithm Engineers and Bioinformatics Developers**: Need to rapidly evaluate algorithmic complexity and applicability boundaries in domains such as sequence alignment, assembly, variant calling, and protein structure prediction, while obtaining directly actionable implementation links and toolchain information.
- **System Architects and Technical Leads**: Concerned with data pipeline design, quality assurance systems, CI/CD engineering practices, and the extensible architecture of knowledge bases, needing to integrate algorithm selection into broader technical decision frameworks.
- **University Researchers and PhD/Postdoc Groups**: Need to trace the original literature of algorithms, understand their evolutionary context within specific subfields (e.g., single-cell analysis, metagenomics, graph genomics), and identify potential research gaps and improvement directions.

## Design Philosophy

The engineering and content design of this knowledge base follows five core principles:

### 1. Single Source of Truth (SSOT)

All algorithm metadata is centrally stored in `data/algorithms/*.yaml`, and the category taxonomy is uniformly defined by `data/categories.yaml`. Any documentation page, README, or statistical report is generated from the same data source, completely eliminating the maintenance nightmare of "documentation out of sync with code."

### 2. Generation-Driven Documentation

Humans do not directly edit final presentation documents; instead, a Python generator (`generate_docs.py`) automatically transforms structured YAML into VitePress Markdown. This "data-as-code" model means adding 100 algorithm entries only requires maintaining YAML files, with zero manual layout costs.

### 3. Verifiable Engineering

Every algorithm entry must pass three layers of validation: field rule validation (`validate.py`), JSON Schema dual validation (`schemas/algorithm-schema.json`), and build-time VitePress navigation consistency checks. The code layer ensures generator correctness through `ruff` + `mypy` + `pytest`, maintaining test coverage above 89%.

### 4. Bilingual Parity Architecture

Chinese content is primary, English content is secondary, but both are kept in strict structural and depth parity. Category names, algorithm descriptions, and purpose statements all provide optional `*_en` fields; the generator automatically falls back to the primary language, ensuring usability in international collaboration scenarios.

### 5. Citation-First Policy

All algorithms are preferentially associated with original paper DOIs and official implementation repositories. References adopt GB-T 7714 (Chinese) / IEEE (English) standard formats. We reject "sourceless algorithm curation," ensuring that every complexity assumption and performance claim is traceable to peer-reviewed literature.

## Current Scale Statistics

| Metric | Value | Description |
|--------|-------|-------------|
| Algorithm Entries | {total} | Covering 16 top-level categories |
| Top-level Categories | {categories} | Including 30+ subcategory levels |
| Total Tags | {tags} | Cross-algorithm semantic tag network |
| Avg per Category | {avg_per_cat} | Entry distribution density |
| Literature Coverage | >85% | Entries with DOI or official paper link |
| Implementation Link Rate | >70% | Entries with official or high-quality open-source implementation |
| Bilingual Coverage | >60% | Entries with both Chinese and English descriptions |

## Recommended Reading Path

For first-time visitors, we recommend the following progressive reading order:

1. **[Project Overview](/en/guides/project-overview)** (this document) — Understand the knowledge base's positioning, philosophy, and scale; establish a global cognitive framework.
2. **[Learning Path](/en/academy/learning-path)** — Choose a four-level progressive curriculum based on your role (developer, architect, researcher) to obtain targeted learning roadmaps and required reading lists.
3. **[System Architecture](/en/architecture/system-architecture)** — Deep dive into the project's four-layer technical architecture (Data, Processing, Output, Deployment) and its Architecture Decision Records (ADR).
4. **[Data and Generation Pipeline](/en/architecture/data-pipeline)** — Master the complete ETL flow from raw YAML data to VitePress rendered pages, including schema evolution history and data quality metrics.
5. **[Quality Assurance](/en/architecture/quality-assurance)** — Understand the three-layer quality system (data validation, code quality, documentation verification) and the CI/CD automation pipeline.
6. **[References and Related Projects](/en/research/references)** — Browse classic papers, required reviews, and comparative analyses of competing open-source projects by domain.
7. **[Evolution Notes](/en/research/evolution)** — Review the project's three-phase evolution from "list-oriented" to "engineered" to "whitepaper-grade," and learn about the future roadmap.

## Technical Highlights

- **Data-Driven**: All pages are auto-generated from algorithms; rebuild with one command after data changes, ensuring zero drift.
- **Bilingual Support**: Chinese and English sites are output in parallel; categories and algorithm descriptions support on-demand internationalization.
- **Academic Citations**: GB-T 7714 / IEEE standard citation formats; every algorithm is traceable to original literature.
- **Engineering CI/CD**: GitHub Actions automatically performs validation, generation, build, and deployment—commit and publish.
- **Complexity Visualization**: Algorithm pages integrate time/space complexity analysis for rapid performance evaluation.
- **Tag Network**: A network of semantic tags builds cross-category algorithm associations, supporting multi-dimensional cross-search.

## Citation Format Example

All references in this knowledge base follow the IEEE standard format. Examples:

> [1] S. B. Needleman and C. D. Wunsch, "A general method applicable to the search for similarities in the amino acid sequence of two proteins," *J. Mol. Biol.*, vol. 48, no. 3, pp. 443–453, 1970. DOI:10.1016/0022-2836(70)90057-4.

> [2] T. F. Smith and M. S. Waterman, "Identification of common molecular subsequences," *J. Mol. Biol.*, vol. 147, no. 1, pp. 195–197, 1981. DOI:10.1016/0022-2836(81)90087-5.

To cite this knowledge base itself, the recommended format is:

> [DB/OL] Awesome Bioinformatics Algorithms Knowledge Base. GitHub, 2024–2025. https://github.com/your-org/awesome-bioinfo-algorithms
"""


def _make_zh_learning_path() -> str:
    return """---
title: 学院路径
---

# 学院路径

## 概述

本学院路径为不同背景的读者设计了四级渐进式课程体系，从"理解知识库结构"到"掌握前沿算法复现与社区贡献"。每一级别均包含明确的先修知识、预期产出、评估标准以及 3–5 篇必读经典论文。我们建议您根据自身当前的技术栈与研究目标，选择对应的入口级别开始学习。

```mermaid
flowchart LR
    L1[Level 1 导航理解] --> L2[Level 2 算法评估]
    L2 --> L3[Level 3 架构与工程]
    L3 --> L4[Level 4 专家研究]
```

---

## Level 1：导航理解（Navigation Literacy）

### 目标

在 2 小时内建立对生物信息学算法全景的直觉认知，能够熟练使用本知识库的分类体系、标签网络与检索功能定位任意算法。

### 核心内容

- **分类体系**：理解 16 大顶级分类（序列比对、序列组装、变异检测、蛋白质结构预测等）及其子分类的划分逻辑。
- **标签体系**：掌握 392 个语义标签的命名规范与跨分类关联能力，学会通过标签交叉检索发现替代算法。
- **快速检索**：熟练使用算法总览页的表格排序与过滤，理解复杂度徽章（ComplexityBadge）与难度分级的含义。

### 先修知识

- 基础分子生物学概念（DNA、RNA、蛋白质序列）
- 基本算法复杂度记号（Big-O）
- Markdown 基础语法

### 预期产出

- 能够独立定位任意 3 个陌生算法的分类归属、时间复杂度与主要用途
- 能够描述至少 2 个分类之间的算法关联关系

### 评估标准

| 评估项 | 通过标准 |
|--------|----------|
| 分类定位 | 给定算法名称，30 秒内找到所属分类页 |
| 标签检索 | 给定 2 个标签，正确列出交集算法 |
| 复杂度识别 | 正确解释 O(mn)、O(n log n) 在生物信息学中的典型含义 |

### 推荐阅读

1. Durbin R, Eddy S R, Krogh A, et al. Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids[M]. Cambridge University Press, 1998.
2. Gusfield D. Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology[M]. Cambridge University Press, 1997.

---

## Level 2：算法评估（Algorithm Evaluation）

### 目标

具备从多维度（用途、复杂度、难度、实现语言、生态成熟度）评估算法并做出选型决策的能力。

### 核心内容

- **用途评估**：区分算法的核心应用场景（如局部比对 vs 全局比对、从头组装 vs 参考引导组装）。
- **复杂度分析**：深入理解时间复杂度与空间复杂度在真实大数据（GB–TB 级基因组数据）上的工程含义。
- **难度分级**：理解 beginner / intermediate / advanced 三级难度背后的概念深度与实现门槛。
- **实现语言评估**：根据 C/C++（高性能）、Python（快速原型）、Rust（内存安全）等语言特性匹配项目需求。
- **交叉检索**：利用标签网络进行同类方案对比（如 Smith-Waterman vs Needleman-Wunsch vs BLAST）。

### 先修知识

- 动态规划、贪心算法、图算法等基础算法设计范式
- 基本的 Linux 命令行操作与生物信息学常用文件格式（FASTA、FASTQ、SAM/BAM、VCF）

### 预期产出

- 针对一个具体生物信息学任务（如"单细胞 RNA-seq 聚类"），输出一份包含至少 3 个候选算法的对比报告
- 报告中须包含复杂度对比表、实现语言分析与工具链建议

### 评估标准

| 评估项 | 通过标准 |
|--------|----------|
| 复杂度解释 | 正确解释至少 5 个算法的时间/空间复杂度并评估其在 100GB 数据上的可行性 |
| 选型报告 | 输出结构化的对比报告，含复杂度、语言、许可、社区活跃度维度 |
| 标签交叉 | 利用标签组合检索，发现至少 1 个非直觉的替代算法 |

### 推荐阅读

1. Altschul S F, Gish W, Miller W, et al. Basic local alignment search tool[J]. Journal of Molecular Biology, 1990, 215(3): 403-410. DOI:10.1016/S0022-2836(05)80360-2.
2. Li H, Durbin R. Fast and accurate short read alignment with Burrows-Wheeler transform[J]. Bioinformatics, 2009, 25(14): 1754-1760. DOI:10.1093/bioinformatics/btp324.
3. Li H. Minimap2: pairwise alignment for nucleotide sequences[J]. Bioinformatics, 2018, 34(18): 3094-3100. DOI:10.1093/bioinformatics/bty191.
4. Langmead B, Trapnell C, Pop M, et al. Ultrafast and memory-efficient alignment of short DNA sequences to the human genome[J]. Genome Biology, 2009, 10(3): R25. DOI:10.1186/gb-2009-10-3-r25.

---

## Level 3：架构与工程（Architecture and Engineering）

### 目标

深入理解本知识库的数据源、生成器、VitePress 发布链路以及 CLI 工作流，具备独立扩展知识库结构与维护数据一致性的能力。

### 核心内容

- **数据源层**：掌握 `categories.yaml` 与 `algorithms/*.yaml` 的 schema 定义、字段约束与版本演化策略。
- **生成器层**：理解 `generate_docs.py` 的函数分工（白皮书生成、算法页生成、索引页生成）与模板渲染逻辑。
- **VitePress 链路**：熟悉 VitePress 的静态站点生成机制、主题配置、导航结构与 Markdown 扩展语法。
- **CLI 工作流**：熟练使用 `validate`、`stats`、`search`、`info`、`compare`、`export`、`vitepress` 等子命令进行日常维护。
- **CI/CD 集成**：理解 GitHub Actions 中验证→生成→构建→部署的完整自动化流程。

### 先修知识

- Python 3.10+ 编程与类型提示（typing）
- YAML 语法与数据建模基础
- 前端构建工具链基础（Node.js、npm、VitePress 概念）
- Git 工作流与 GitHub Actions 基础

### 预期产出

- 成功向本知识库提交一个新的算法条目 PR，包含完整的 YAML 数据、通过全部验证、自动生成对应的 VitePress 页面
- 撰写一份关于"如何为知识库添加新分类"的技术文档片段

### 评估标准

| 评估项 | 通过标准 |
|--------|----------|
| YAML 编写 | 独立编写符合 schema 的算法 YAML，validate 零报错 |
| 生成链路 | 解释从 YAML 到 VitePress 页面的完整数据流（>=6 个节点） |
| CLI 熟练度 | 在不查阅文档的情况下完成 search / info / compare 组合查询 |

### 推荐阅读

1. VitePress 官方文档: https://vitepress.dev/
2. PyYAML 文档与 YAML 1.2 规范
3. pytest 官方文档: https://docs.pytest.org/
4. GitHub Actions 工作流语法参考

---

## Level 4：专家研究（Expert Research）

### 目标

站在领域前沿，理解最新算法（2022–2025）的核心创新点，具备论文复现、性能基准测试与社区贡献的能力。

### 核心内容

- **前沿算法追踪**：持续跟踪 AlphaFold 系列、ESM 系列、单细胞基础模型、图基因组学等前沿方向的最新进展。
- **论文复现**：能够根据知识库中的 DOI 链接定位原始论文，理解算法伪代码与关键公式，并在开源框架中完成最小可运行复现。
- **性能基准测试**：设计公平的对比实验（统一数据集、统一硬件环境、统一评估指标），产出可发布的 benchmark 报告。
- **社区贡献**：通过提交 PR 的方式改进现有算法条目（补充缺失字段、修正复杂度、更新实现链接），或撰写原创的技术白皮书补充页。

### 先修知识

- 至少 1 个生物信息学子领域的深入研究经验（如蛋白质结构预测或单细胞分析）
- 顶会论文阅读与复现经验（ISMB、RECOMB、NeurIPS、ICML 等）
- 高性能计算（HPC）或 GPU 加速编程基础（CUDA / PyTorch）

### 预期产出

- 完成至少 1 篇前沿算法论文的代码复现，并在本知识库对应条目下提交改进 PR
- 产出 1 份面向社区的 benchmark 对比报告，被项目维护者采纳或引用

### 评估标准

| 评估项 | 通过标准 |
|--------|----------|
| 论文复现 | 在标准数据集上复现核心指标，误差 <5% |
| Benchmark 设计 | 实验设计覆盖至少 3 个同类算法，含时间/内存/准确率维度 |
| 社区贡献 | 提交的 PR 被合并，且包含测试用例或文档改进 |

### 推荐阅读

1. Jumper J, Evans R, Pritzel A, et al. Highly accurate protein structure prediction with AlphaFold[J]. Nature, 2021, 596(7873): 583-589. DOI:10.1038/s41586-021-03819-2.
2. Lin Z, Akin H, Rao R, et al. Evolutionary-scale prediction of atomic-level protein structure with a language model[J]. Science, 2023, 379(6637): 1123-1130. DOI:10.1126/science.ade2574.
3. Eijkelenboom A, de Ridder D. Mapping cellular identities from single-cell data using deep learning[J]. Nature Reviews Molecular Cell Biology, 2024. DOI:10.1038/s41580-023-00647-1.
4. Paten B, Novak A M, Eizenga J M, et al. Genome graphs and the evolution of genome inference[J]. Genome Research, 2017, 27(5): 665-676. DOI:10.1101/gr.214155.116.

---

## 总结与进阶建议

| 级别 | 适合人群 | 预计学习时间 | 关键产出 |
|------|----------|--------------|----------|
| Level 1 | 初学者 / 跨界开发者 | 2–4 小时 | 全景认知 + 独立检索 |
| Level 2 | 中级开发者 / 研究生 | 1–2 周 | 选型报告 + 复杂度分析 |
| Level 3 | 高级开发者 / 维护者 | 2–4 周 | 数据维护能力 + CI/CD 理解 |
| Level 4 | 研究者 / 算法工程师 | 持续 | 论文复现 + 社区贡献 |

无论您处于哪一级别，都建议从本知识库的**算法总览页**开始，通过实际检索与对比建立直觉。学院路径不是线性的枷锁，而是根据需求灵活跳转的参考地图。
"""


def _make_en_learning_path() -> str:
    return """---
title: Learning Path
---

# Learning Path

## Overview

This academy path provides a four-level progressive curriculum designed for readers of diverse backgrounds, ranging from "understanding the knowledge base structure" to "mastering frontier algorithm reproduction and community contribution." Each level includes explicit prerequisite knowledge, expected deliverables, assessment criteria, and 3–5 required classic papers. We recommend selecting the appropriate entry level based on your current technical stack and research objectives.

```mermaid
flowchart LR
    L1[Level 1 Navigation Literacy] --> L2[Level 2 Algorithm Evaluation]
    L2 --> L3[Level 3 Architecture & Engineering]
    L3 --> L4[Level 4 Expert Research]
```

---

## Level 1: Navigation Literacy

### Goal

Establish an intuitive understanding of the bioinformatics algorithm landscape within 2 hours, and be able to skillfully use the knowledge base's category taxonomy, tag network, and search functions to locate any algorithm.

### Core Content

- **Category Taxonomy**: Understand the logic behind the 16 top-level categories (sequence alignment, assembly, variant calling, protein structure prediction, etc.) and their subcategory hierarchies.
- **Tag System**: Master the naming conventions and cross-category association capabilities of 392 semantic tags; learn to discover alternative algorithms through tag intersection search.
- **Rapid Retrieval**: Skillfully use table sorting and filtering on the algorithm index page; understand the meaning of ComplexityBadge and difficulty ratings.

### Prerequisites

- Basic molecular biology concepts (DNA, RNA, protein sequences)
- Basic algorithmic complexity notation (Big-O)
- Markdown basic syntax

### Expected Deliverables

- Independently locate the category归属, time complexity, and primary purpose of any 3 unfamiliar algorithms
- Describe the algorithmic association between at least 2 categories

### Assessment Criteria

| Assessment Item | Pass Criteria |
|-----------------|---------------|
| Category Location | Given an algorithm name, find its category page within 30 seconds |
| Tag Retrieval | Given 2 tags, correctly list intersection algorithms |
| Complexity Recognition | Correctly explain the typical meaning of O(mn) and O(n log n) in bioinformatics |

### Recommended Reading

1. R. Durbin, S. R. Eddy, A. Krogh, and G. Mitchison, *Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids*. Cambridge University Press, 1998.
2. D. Gusfield, *Algorithms on Strings, Trees, and Sequences: Computer Science and Computational Biology*. Cambridge University Press, 1997.

---

## Level 2: Algorithm Evaluation

### Goal

Possess the ability to evaluate algorithms from multiple dimensions (purpose, complexity, difficulty, implementation language, ecosystem maturity) and make selection decisions.

### Core Content

- **Purpose Evaluation**: Distinguish the core application scenarios of algorithms (e.g., local vs global alignment, de novo vs reference-guided assembly).
- **Complexity Analysis**: Deeply understand the engineering implications of time and space complexity on real-world big data (GB–TB scale genomic data).
- **Difficulty Grading**: Understand the conceptual depth and implementation threshold implied by the three-level difficulty rating (beginner / intermediate / advanced).
- **Language Assessment**: Match project requirements based on language characteristics such as C/C++ (high performance), Python (rapid prototyping), and Rust (memory safety).
- **Cross-Search**: Use the tag network for comparative analysis of similar solutions (e.g., Smith-Waterman vs Needleman-Wunsch vs BLAST).

### Prerequisites

- Basic algorithm design paradigms: dynamic programming, greedy algorithms, graph algorithms
- Basic Linux command-line operations and common bioinformatics file formats (FASTA, FASTQ, SAM/BAM, VCF)

### Expected Deliverables

- For a specific bioinformatics task (e.g., "single-cell RNA-seq clustering"), produce a comparative report covering at least 3 candidate algorithms
- The report must include a complexity comparison table, implementation language analysis, and toolchain recommendations

### Assessment Criteria

| Assessment Item | Pass Criteria |
|-----------------|---------------|
| Complexity Explanation | Correctly explain the time/space complexity of at least 5 algorithms and assess their feasibility on 100 GB datasets |
| Selection Report | Produce a structured comparison report covering complexity, language, license, and community activity |
| Tag Cross-Search | Use tag combinations to discover at least 1 non-obvious alternative algorithm |

### Recommended Reading

1. S. F. Altschul, W. Gish, W. Miller, E. W. Myers, and D. J. Lipman, "Basic local alignment search tool," *J. Mol. Biol.*, vol. 215, no. 3, pp. 403–410, 1990. DOI:10.1016/S0022-2836(05)80360-2.
2. H. Li and R. Durbin, "Fast and accurate short read alignment with Burrows-Wheeler transform," *Bioinformatics*, vol. 25, no. 14, pp. 1754–1760, 2009. DOI:10.1093/bioinformatics/btp324.
3. H. Li, "Minimap2: pairwise alignment for nucleotide sequences," *Bioinformatics*, vol. 34, no. 18, pp. 3094–3100, 2018. DOI:10.1093/bioinformatics/bty191.
4. B. Langmead, C. Trapnell, M. Pop, and S. L. Salzberg, "Ultrafast and memory-efficient alignment of short DNA sequences to the human genome," *Genome Biol.*, vol. 10, no. 3, p. R25, 2009. DOI:10.1186/gb-2009-10-3-r25.

---

## Level 3: Architecture and Engineering

### Goal

Gain a deep understanding of this knowledge base's data sources, generator, VitePress publishing pipeline, and CLI workflow; possess the ability to independently extend the knowledge base structure and maintain data consistency.

### Core Content

- **Data Source Layer**: Master the schema definitions, field constraints, and version evolution strategies of `categories.yaml` and `algorithms/*.yaml`.
- **Generator Layer**: Understand the functional division in `generate_docs.py` (whitepaper generation, algorithm page generation, index page generation) and template rendering logic.
- **VitePress Pipeline**: Familiarity with VitePress static site generation mechanisms, theme configuration, navigation structure, and Markdown extension syntax.
- **CLI Workflow**: Proficiency in daily maintenance using subcommands such as `validate`, `stats`, `search`, `info`, `compare`, `export`, and `vitepress`.
- **CI/CD Integration**: Understanding the complete automation flow of validation → generation → build → deployment in GitHub Actions.

### Prerequisites

- Python 3.10+ programming and type hints
- YAML syntax and data modeling basics
- Front-end build toolchain basics (Node.js, npm, VitePress concepts)
- Git workflow and GitHub Actions basics

### Expected Deliverables

- Successfully submit a new algorithm entry PR to this knowledge base, including complete YAML data, passing all validations, and automatically generating the corresponding VitePress pages
- Write a technical document fragment on "How to add a new category to the knowledge base"

### Assessment Criteria

| Assessment Item | Pass Criteria |
|-----------------|---------------|
| YAML Authoring | Independently write algorithm YAML compliant with schema; `validate` reports zero errors |
| Generation Pipeline | Explain the complete data flow from YAML to VitePress page (>=6 nodes) |
| CLI Proficiency | Complete search / info / compare combined queries without consulting documentation |

### Recommended Reading

1. VitePress Official Documentation: https://vitepress.dev/
2. PyYAML Documentation and YAML 1.2 Specification
3. pytest Official Documentation: https://docs.pytest.org/
4. GitHub Actions Workflow Syntax Reference

---

## Level 4: Expert Research

### Goal

Stand at the frontier of the field, understand the core innovations of the latest algorithms (2022–2025), and possess the ability to reproduce papers, perform benchmarking, and contribute to the community.

### Core Content

- **Frontier Tracking**: Continuously track the latest advances in AlphaFold series, ESM series, single-cell foundation models, graph genomics, and other frontier directions.
- **Paper Reproduction**: Locate original papers through DOI links in the knowledge base, understand algorithm pseudocode and key formulas, and complete a minimal runnable reproduction in an open-source framework.
- **Performance Benchmarking**: Design fair comparative experiments (unified dataset, unified hardware environment, unified evaluation metrics) and produce publishable benchmark reports.
- **Community Contribution**: Improve existing algorithm entries by submitting PRs (supplement missing fields, correct complexity, update implementation links), or write original technical whitepaper supplement pages.

### Prerequisites

- In-depth research experience in at least 1 bioinformatics subfield (e.g., protein structure prediction or single-cell analysis)
- Top-tier conference paper reading and reproduction experience (ISMB, RECOMB, NeurIPS, ICML, etc.)
- High-performance computing (HPC) or GPU acceleration programming basics (CUDA / PyTorch)

### Expected Deliverables

- Complete the code reproduction of at least 1 frontier algorithm paper, and submit an improvement PR under the corresponding entry in this knowledge base
- Produce 1 community-facing benchmark comparison report that is adopted or cited by project maintainers

### Assessment Criteria

| Assessment Item | Pass Criteria |
|-----------------|---------------|
| Paper Reproduction | Reproduce core metrics on standard datasets with <5% error |
| Benchmark Design | Experimental design covers at least 3 similar algorithms, including time/memory/accuracy dimensions |
| Community Contribution | Submitted PR is merged, and includes test cases or documentation improvements |

### Recommended Reading

1. J. Jumper *et al.*, "Highly accurate protein structure prediction with AlphaFold," *Nature*, vol. 596, no. 7873, pp. 583–589, 2021. DOI:10.1038/s41586-021-03819-2.
2. Z. Lin *et al.*, "Evolutionary-scale prediction of atomic-level protein structure with a language model," *Science*, vol. 379, no. 6637, pp. 1123–1130, 2023. DOI:10.1126/science.ade2574.
3. A. Eijkelenboom and D. de Ridder, "Mapping cellular identities from single-cell data using deep learning," *Nat. Rev. Mol. Cell Biol.*, 2024. DOI:10.1038/s41580-023-00647-1.
4. B. Paten, A. M. Novak, J. M. Eizenga, and E. Garrison, "Genome graphs and the evolution of genome inference," *Genome Res.*, vol. 27, no. 5, pp. 665–676, 2017. DOI:10.1101/gr.214155.116.

---

## Summary and Advanced Recommendations

| Level | Target Audience | Estimated Study Time | Key Deliverable |
|-------|-----------------|----------------------|-----------------|
| Level 1 | Beginners / Cross-domain Developers | 2–4 hours | Landscape awareness + independent retrieval |
| Level 2 | Mid-level Developers / Graduate Students | 1–2 weeks | Selection report + complexity analysis |
| Level 3 | Senior Developers / Maintainers | 2–4 weeks | Data maintenance capability + CI/CD understanding |
| Level 4 | Researchers / Algorithm Engineers | Continuous | Paper reproduction + community contribution |

Regardless of your current level, we recommend starting from the **Algorithm Index** page of this knowledge base, building intuition through actual retrieval and comparison. The academy path is not a linear shackle, but a reference map for flexible jumps according to need.
"""


# END_OF_PART_1


def _make_zh_system_architecture() -> str:
    return """---
title: 系统架构
---

# 系统架构

## 架构全景

本知识库采用分层架构设计，将数据生命周期划分为四个清晰的层级：数据层（Data Layer）、处理层（Processing Layer）、输出层（Output Layer）与部署层（Deployment Layer）。每一层均具有明确的职责边界、输入输出契约与可观测指标。

```mermaid
flowchart LR
    subgraph Data["数据层"]
        D1[categories.yaml]
        D2[algorithms/*.yaml]
    end
    subgraph Processing["处理层"]
        P1[DataStore]
        P2[Validation]
        P3[generate_docs.py]
    end
    subgraph Output["输出层"]
        O1[docs/zh/**/*.md]
        O2[docs/en/**/*.md]
    end
    subgraph Deployment["部署层"]
        V1[VitePress Build]
        V2[GitHub Pages]
    end
    Data --> Processing
    Processing --> Output
    Output --> Deployment
```

---

## 数据层（Data Layer）

数据层是整个系统的唯一真相源，由两部分组成：

### 分类定义（categories.yaml）

- **职责**：统一定义 16 大顶级分类及其子分类的层级关系、中英文名称与描述。
- **约束**：分类 ID 全局唯一，采用小写连字符命名（如 `sequence-alignment`）；子分类通过 `parent_id` 隐式关联。
- **演化策略**：新增分类属于 spec 级变更，须通过 `/opsx:propose` 提案流程，确保下游生成器与导航配置同步更新。

### 算法条目（algorithms/*.yaml）

- **职责**：存储每个算法的完整元数据，包括描述、用途、复杂度、引用、标签等 15+ 字段。
- **约束**：顶级键为 `algorithms:`（列表），每个条目须通过 `validate.py` 的字段规则与 JSON Schema 双重验证。
- **版本管理**：按分类分文件存储，天然支持 Git 的行级 diff 与冲突合并。

---

## 处理层（Processing Layer）

处理层负责将原始数据转换为结构化中间表示，再渲染为目标格式。

### DataStore

- **职责**：加载所有 YAML 文件，构建内存中的类别树、算法列表、分类索引与标签索引。
- **输出**：`list[Category]`、`list[AlgorithmEntry]`、各类反向索引字典。
- **设计模式**：Repository Pattern —— 将数据访问逻辑集中封装，便于替换底层存储（如未来迁移至 SQLite 或图数据库）。

### Validation

- **职责**：字段规则校验（如 description 长度 50–500 字符、time_complexity 匹配 O(...) 模式、ID 全局唯一性）与 JSON Schema 验证。
- **输出**：通过时返回空列表；失败时返回结构化错误信息，包含文件名、条目索引与具体字段。
- **扩展点**：支持自定义验证器注册，便于未来添加交叉引用一致性检查。

### generate_docs.py

- **职责**：将验证通过的数据渲染为 VitePress Markdown。按功能划分为白皮书生成（`_generate_*`）、算法页生成（`generate_*_algo_page`）、索引页生成（`generate_*_index`）与分类页生成（`generate_*_category_page`）。
- **输出**：`docs/zh/` 与 `docs/en/` 下的完整站点源码。
- **设计模式**：Template Method —— 每个语言版本的生成器共享相同的算法遍历与分类遍历骨架，但填充不同的语言内容。

---

## 输出层（Output Layer）

输出层是 VitePress 可直接消费的静态 Markdown 站点源码。

### 目录结构

```
docs/
├── .vitepress/
│   └── config.ts          # 导航、侧边栏、主题配置
├── zh/
│   ├── index.md           # 中文首页（Hero + Features + 白皮书入口）
│   ├── algorithms/
│   │   ├── index.md       # 算法总览表
│   │   └── {id}.md        # 195+ 算法详情页
│   ├── categories/
│   │   ├── index.md       # 分类总览
│   │   └── {cat}/
│   │       └── index.md   # 单分类详情（含子分类）
│   ├── tags.md            # 标签索引
│   ├── guides/
│   │   └── project-overview.md
│   ├── academy/
│   │   └── learning-path.md
│   ├── architecture/
│   │   ├── system-architecture.md
│   │   ├── data-pipeline.md
│   │   └── quality-assurance.md
│   ├── research/
│   │   ├── references.md
│   │   └── evolution.md
│   └── reference/
│       └── cli-workflow.md
└── en/                    # 英文镜像结构
```

### 关键设计决策

- **静态优先**：所有页面预生成，无需运行时数据库或 SSR，确保 GitHub Pages 的托管兼容性与极致加载性能。
- **双语镜像**：中英文目录结构完全对称，仅内容语言不同，VitePress 配置通过 `locales` 实现导航切换。

---

## 部署层（Deployment Layer）

部署层将输出层构建为可访问的静态站点。

### VitePress Build

- **输入**：`docs/zh/`、`docs/en/`、`.vitepress/config.ts`
- **输出**：`docs/.vitepress/dist/`（静态 HTML、CSS、JS、资源文件）
- **特性**：基于 Vite 的极速构建、支持 Mermaid 图表渲染、代码高亮、全文搜索（local search）

### GitHub Pages

- **触发条件**：`master` 分支的 push 或 PR merge
- **流程**：GitHub Actions 执行 `npm run build` 后将 `dist/` 部署至 `gh-pages` 分支
- **自定义域名**：支持通过 CNAME 文件绑定自定义域名与 HTTPS

---

## 架构决策记录（ADR）

### ADR-001：YAML vs JSON vs Relational Database

| 维度 | YAML | JSON | RDB (SQLite/PostgreSQL) |
|------|------|------|-------------------------|
| 人类可读性 | 优秀，支持注释 | 中等，无注释 | 差，需管理工具 |
| Git Diff 友好性 | 优秀，行级 diff | 良好 | 差，二进制/复杂 |
| 验证机制 | 需外部 JSON Schema | JSON Schema 原生 | 数据库约束 |
| 协作门槛 | 低，任何文本编辑器 | 低 | 高，需 SQL 知识 |
| 查询能力 | 弱，需加载到内存 | 弱 | 强，SQL 即查 |
| 扩展成本 | 低 | 低 | 高，需迁移脚本 |

**决策**：采用 YAML 作为人类维护的单一真相源，通过 DataStore 加载到内存后执行查询。未来若规模突破 10,000 条目，可评估迁移至 SQLite 的混合模式。

### ADR-002：VitePress vs Docusaurus vs MkDocs

| 维度 | VitePress | Docusaurus | MkDocs Material |
|------|-----------|------------|-----------------|
| 构建速度 | 极快（Vite 驱动） | 中等（Webpack） | 快 |
| Vue 生态 | 原生支持 | React 生态 | Jinja2 模板 |
| Mermaid 支持 | 插件成熟 | 需插件 | 需插件 |
| 搜索 | 本地搜索，零配置 | Algolia DocSearch | 本地搜索 |
| 多语言 | locale 配置直观 | i18n 路由复杂 | 插件支持 |
| 主题可控性 | 高，CSS 变量丰富 | 中 | 高 |

**决策**：采用 VitePress 作为主力文档站点，MkDocs Material 作为备用公开文档渠道（`mkdocs/` 目录）。

### ADR-003：静态优先 vs 动态渲染

| 维度 | 静态生成（SSG） | 动态渲染（SSR/API） |
|------|-----------------|---------------------|
| 托管成本 | 零（GitHub Pages 免费） | 需服务器/无服务器函数 |
| 加载延迟 | 极低，纯 HTML/CSS/JS | 依赖 API 响应时间 |
| SEO | 优秀，内容在 HTML 中 | 需预渲染或爬虫适配 |
| 实时性 | 构建时快照，分钟级延迟 | 毫秒级实时 |
| 复杂度 | 低 | 高，需管理运行时状态 |

**决策**：静态优先。算法元数据变更频率低（日级或周级），分钟级构建延迟可接受，换取零运维成本与极致可靠性。

---

## 性能基准

以下数据基于典型开发机器（AMD Ryzen 7 5800X, 32GB RAM, NVMe SSD）的实测与估算：

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| 数据加载时间 | <0.5 s | <0.3 s |
| YAML 验证时间 | <1.0 s | <0.5 s |
| Markdown 生成时间 | <2.0 s | <1.0 s |
| VitePress 构建时间 | ~15 s | <10 s |
| 生成页面总数 | ~450 页 | <1,000 页 |
| 峰值内存占用 | ~120 MB | <200 MB |
| 构建产物大小 | ~25 MB | <50 MB |

---

## 扩展架构

### 插件系统（规划中）

未来拟引入轻量级插件机制，允许第三方扩展：

- **数据增强插件**：自动从 PubMed / bioRxiv 抓取算法最新引用
- **可视化插件**：为算法页自动生成复杂度曲线图或算法流程图
- **导出插件**：支持除 Markdown 外的 LaTeX、PDF、Jupyter Notebook 等格式输出

### API 规划（远期）

若社区需求强烈，可考虑提供只读 REST API：

- `GET /api/v1/algorithms` — 分页列表
- `GET /api/v1/algorithms/{id}` — 单条目详情
- `GET /api/v1/categories` — 分类树
- `GET /api/v1/tags/{tag}` — 标签下算法列表

API 层将直接复用现有 `DataStore` 与 `algorithm_registry.py` 的查询逻辑，以最小额外代码实现。
"""


def _make_en_system_architecture() -> str:
    return """---
title: System Architecture
---

# System Architecture

## Architecture Overview

This knowledge base adopts a layered architecture design, dividing the data lifecycle into four clear layers: Data Layer, Processing Layer, Output Layer, and Deployment Layer. Each layer has well-defined responsibility boundaries, input/output contracts, and observable metrics.

```mermaid
flowchart LR
    subgraph Data["Data Layer"]
        D1[categories.yaml]
        D2[algorithms/*.yaml]
    end
    subgraph Processing["Processing Layer"]
        P1[DataStore]
        P2[Validation]
        P3[generate_docs.py]
    end
    subgraph Output["Output Layer"]
        O1[docs/zh/**/*.md]
        O2[docs/en/**/*.md]
    end
    subgraph Deployment["Deployment Layer"]
        V1[VitePress Build]
        V2[GitHub Pages]
    end
    Data --> Processing
    Processing --> Output
    Output --> Deployment
```

---

## Data Layer

The Data Layer is the single source of truth for the entire system, composed of two parts:

### Category Definitions (categories.yaml)

- **Responsibility**: Uniformly define the hierarchical relationships, bilingual names, and descriptions of 16 top-level categories and their subcategories.
- **Constraints**: Category IDs are globally unique, using lowercase-hyphenated naming (e.g., `sequence-alignment`); subcategories are implicitly linked through `parent_id`.
- **Evolution Strategy**: Adding new categories is a spec-level change that must go through the `/opsx:propose` proposal workflow to ensure downstream generators and navigation configurations are synchronized.

### Algorithm Entries (algorithms/*.yaml)

- **Responsibility**: Store complete metadata for each algorithm, including 15+ fields such as description, purpose, complexity, references, and tags.
- **Constraints**: The top-level key is `algorithms:` (list); each entry must pass dual validation by field rules in `validate.py` and the JSON Schema.
- **Version Management**: Stored in per-category files, naturally supporting Git line-level diffs and conflict resolution.

---

## Processing Layer

The Processing Layer is responsible for transforming raw data into structured intermediate representations, then rendering them into target formats.

### DataStore

- **Responsibility**: Load all YAML files and build in-memory category trees, algorithm lists, category indexes, and tag indexes.
- **Output**: `list[Category]`, `list[AlgorithmEntry]`, and various reverse-index dictionaries.
- **Design Pattern**: Repository Pattern — centralizes data access logic, facilitating future replacement of the underlying storage (e.g., migration to SQLite or graph databases).

### Validation

- **Responsibility**: Field rule validation (e.g., description length 50–500 characters, time_complexity matching O(...) pattern, global ID uniqueness) and JSON Schema validation.
- **Output**: Returns an empty list on success; returns structured error information on failure, including filename, entry index, and specific field.
- **Extension Point**: Supports custom validator registration for future cross-reference consistency checks.

### generate_docs.py

- **Responsibility**: Render validated data into VitePress Markdown. Functionally divided into whitepaper generation (`_generate_*`), algorithm page generation (`generate_*_algo_page`), index page generation (`generate_*_index`), and category page generation (`generate_*_category_page`).
- **Output**: Complete site source under `docs/zh/` and `docs/en/`.
- **Design Pattern**: Template Method — generators for each language version share the same algorithm traversal and category traversal skeletons, but fill in different language content.

---

## Output Layer

The Output Layer is the static Markdown site source directly consumable by VitePress.

### Directory Structure

```
docs/
├── .vitepress/
│   └── config.ts          # Navigation, sidebar, theme config
├── zh/
│   ├── index.md           # Chinese landing page
│   ├── algorithms/
│   │   ├── index.md       # Algorithm index table
│   │   └── {id}.md        # 195+ algorithm detail pages
│   ├── categories/
│   │   ├── index.md       # Category overview
│   │   └── {cat}/
│   │       └── index.md   # Single category details (with subcategories)
│   ├── tags.md            # Tag index
│   ├── guides/
│   │   └── project-overview.md
│   ├── academy/
│   │   └── learning-path.md
│   ├── architecture/
│   │   ├── system-architecture.md
│   │   ├── data-pipeline.md
│   │   └── quality-assurance.md
│   ├── research/
│   │   ├── references.md
│   │   └── evolution.md
│   └── reference/
│       └── cli-workflow.md
└── en/                    # English mirror structure
```

### Key Design Decisions

- **Static-First**: All pages are pre-generated, requiring no runtime database or SSR, ensuring GitHub Pages hosting compatibility and极致 loading performance.
- **Bilingual Mirror**: Chinese and English directory structures are fully symmetric, differing only in content language; VitePress configuration achieves navigation switching through `locales`.

---

## Deployment Layer

The Deployment Layer builds the Output Layer into an accessible static site.

### VitePress Build

- **Input**: `docs/zh/`, `docs/en/`, `.vitepress/config.ts`
- **Output**: `docs/.vitepress/dist/` (static HTML, CSS, JS, asset files)
- **Features**: Vite-powered极速 builds, Mermaid diagram rendering, code highlighting, full-text search (local search)

### GitHub Pages

- **Trigger**: Push to `master` branch or PR merge
- **Flow**: GitHub Actions executes `npm run build`, then deploys `dist/` to the `gh-pages` branch
- **Custom Domain**: Supports binding custom domains and HTTPS via CNAME files

---

## Architecture Decision Records (ADR)

### ADR-001: YAML vs JSON vs Relational Database

| Dimension | YAML | JSON | RDB (SQLite/PostgreSQL) |
|-----------|------|------|-------------------------|
| Human Readability | Excellent, supports comments | Medium, no comments | Poor, requires tooling |
| Git Diff Friendly | Excellent, line-level diff | Good | Poor |
| Validation Mechanism | Requires external JSON Schema | Native JSON Schema | Database constraints |
| Collaboration Barrier | Low, any text editor | Low | High, requires SQL knowledge |
| Query Capability | Weak, requires in-memory loading | Weak | Strong, SQL ad-hoc |
| Extension Cost | Low | Low | High, requires migration scripts |

**Decision**: Adopt YAML as the human-maintained single source of truth, performing queries after loading into memory via DataStore. If scale exceeds 10,000 entries in the future, evaluate migration to a SQLite hybrid model.

### ADR-002: VitePress vs Docusaurus vs MkDocs

| Dimension | VitePress | Docusaurus | MkDocs Material |
|-----------|-----------|------------|-----------------|
| Build Speed | Extremely fast (Vite) | Medium (Webpack) | Fast |
| Ecosystem | Native Vue | React ecosystem | Jinja2 templates |
| Mermaid Support | Mature plugin | Requires plugin | Requires plugin |
| Search | Local search, zero config | Algolia DocSearch | Local search |
| Multi-language | Intuitive locale config | Complex i18n routing | Plugin support |
| Theme Controllability | High, rich CSS variables | Medium | High |

**Decision**: Adopt VitePress as the primary documentation site; MkDocs Material serves as a backup public documentation channel (`mkdocs/` directory).

### ADR-003: Static-First vs Dynamic Rendering

| Dimension | Static Generation (SSG) | Dynamic Rendering (SSR/API) |
|-----------|-------------------------|-----------------------------|
| Hosting Cost | Zero (GitHub Pages free) | Requires server/serverless functions |
| Load Latency | Extremely low, pure HTML/CSS/JS | Depends on API response time |
| SEO | Excellent, content in HTML | Requires prerendering or crawler adaptation |
| Real-time | Build-time snapshot, minute-level delay | Millisecond-level real-time |
| Complexity | Low | High, requires managing runtime state |

**Decision**: Static-first. Algorithm metadata changes infrequently (daily or weekly), and minute-level build delays are acceptable in exchange for zero operational cost and极致 reliability.

---

## Performance Benchmarks

The following data is based on measurements and estimates from a typical development machine (AMD Ryzen 7 5800X, 32GB RAM, NVMe SSD):

| Metric | Current Value | Target Value |
|--------|---------------|--------------|
| Data Load Time | <0.5 s | <0.3 s |
| YAML Validation Time | <1.0 s | <0.5 s |
| Markdown Generation Time | <2.0 s | <1.0 s |
| VitePress Build Time | ~15 s | <10 s |
| Total Generated Pages | ~450 pages | <1,000 pages |
| Peak Memory Usage | ~120 MB | <200 MB |
| Build Artifact Size | ~25 MB | <50 MB |

---

## Extension Architecture

### Plugin System (Planned)

A lightweight plugin mechanism is planned for future introduction, allowing third-party extensions:

- **Data Enrichment Plugins**: Automatically fetch latest citations for algorithms from PubMed / bioRxiv
- **Visualization Plugins**: Auto-generate complexity curve diagrams or algorithm flowcharts for algorithm pages
- **Export Plugins**: Support output formats beyond Markdown, such as LaTeX, PDF, and Jupyter Notebook

### API Planning (Long-term)

If community demand is strong, a read-only REST API may be considered:

- `GET /api/v1/algorithms` — Paginated list
- `GET /api/v1/algorithms/{id}` — Single entry detail
- `GET /api/v1/categories` — Category tree
- `GET /api/v1/tags/{tag}` — Algorithms under a tag

The API layer would directly reuse existing `DataStore` and `algorithm_registry.py` query logic, minimizing additional code.
"""


def _make_zh_data_pipeline() -> str:
    return """---
title: 数据与生成链路
---

# 数据与生成链路

## 概述

本知识库的核心工程能力体现在一条完整的 ETL（Extract-Transform-Load）数据管线：从人类可编辑的 YAML 原始数据，经过 Python 生成器的转换与渲染，最终输出为 VitePress 可直接消费的静态 Markdown。本页详细拆解每个阶段的输入、处理逻辑、输出与可观测指标。

```mermaid
flowchart LR
    E[Extract<br/>YAML Files] --> T[Transform<br/>Python / Jinja2]
    T --> L[Load<br/>Markdown]
    L --> R[Render<br/>VitePress]
```

---

## 提取层（Extract）

### 输入

- `data/categories.yaml`：16 个顶级分类、30+ 子分类的定义
- `data/algorithms/*.yaml`：195+ 算法条目，每文件对应一个顶级分类

### 加载机制

`DataStore.load_all()` 使用 PyYAML 解析所有文件，构建内存对象：

1. 先加载 `categories.yaml`，构建 `Category` 树（含子分类的 `parent_id` 回链）
2. 遍历 `data/algorithms/` 下所有 `.yaml` 文件，将每个列表项转换为 `AlgorithmEntry`
3. 构建辅助索引：`cat_map`（category id → Category）、`by_cat`（category id → [AlgorithmEntry]）、`by_tag`（tag → [AlgorithmEntry]）

### 约束与校验

加载阶段仅保证 YAML 语法正确性；业务规则校验（如 ID 唯一性、description 长度、category 存在性）由下游 `validate.py` 负责。

---

## 转换层（Transform）

### 字段级转换

每个 `AlgorithmEntry` 包含 15+ 字段，转换层的主要工作是将这些结构化字段映射为 Markdown 的呈现元素：

| 字段 | 来源 | Markdown 呈现 |
|------|------|---------------|
| `id` | YAML | 文件名、URL 路径、锚点 |
| `name` | YAML | 页面标题（H1）、表格链接文本 |
| `description` | YAML | frontmatter `description`、页面首段 |
| `purpose` | YAML | 信息表格"用途"行 |
| `time_complexity` | YAML | 信息表格 + 复杂度分析小节 |
| `space_complexity` | YAML | 信息表格 + 复杂度分析小节 |
| `year` | YAML | 信息表格、年份徽章 |
| `difficulty` | YAML | 难度徽章（beginner/intermediate/advanced） |
| `language` | YAML | 信息表格，逗号/顿号分隔 |
| `category` | YAML | 分类页链接 |
| `subcategory` | YAML | 分类页内的子分组 |
| `tags` | YAML | 标签链接云 |
| `paper_url` | YAML | "Paper" 链接（带外部链接图标） |
| `implementation_url` | YAML | "Implementation" 链接 |
| `related_tools` | YAML | 行内代码样式工具名 |
| `references` | YAML | 参考文献列表（GB-T 7714 / IEEE 格式） |
| `*_en` | YAML | 英文站点对应字段的 fallback |

### 生成器逻辑

`generate_docs.py` 中的生成函数按职责分层：

- **白皮书生成器**（`_generate_*`）：纯文本模板，输出架构叙事、学院路径、质量保障等深度内容
- **算法页生成器**（`generate_*_algo_page`）：以单个 `AlgorithmEntry` 为输入，输出 frontmatter + 描述 + 信息表 + 复杂度分析 + 链接 + 标签 + 参考文献
- **索引页生成器**（`generate_*_index`）：以算法列表为输入，输出排序表格（按名称字母序）
- **分类页生成器**（`generate_*_category_page`）：以 `Category` + 算法列表为输入，按子分类分组输出表格

### Jinja2 替代方案

当前生成器使用 Python f-string 直接拼接 Markdown。若未来模板复杂度增加（如条件渲染、循环嵌套、多语言插值），可评估引入 Jinja2 作为模板引擎，但需权衡引入依赖与当前"零外部模板依赖"的简洁性。

---

## 加载层（Load）

### Markdown 输出规范

所有生成的 Markdown 遵循以下规范，确保 VitePress 正确渲染：

- **Frontmatter**：每个页面以 `---
title: ...
---` 开头，算法页额外包含 `description` 字段用于 SEO
- **标题层级**：H1 仅出现一次（页面主标题），H2 用于主要板块，H3 用于子板块
- **表格**：所有表格必须包含表头分隔行（`|---|---|`），表头使用加粗或代码样式提升可读性
- **代码块**：复杂度、命令示例使用围栏代码块（```）并标注语言（如 `bash`、`mermaid`）
- **链接**：内部链接使用相对路径（`../categories/xxx/`），外部链接使用完整 URL
- **Mermaid 图表**：使用 `flowchart LR` 等标准语法，**禁止**硬编码颜色（如 `style A fill:#10b981`），依赖 VitePress 主题的 CSS 变量控制样式

### 文件系统映射

| 逻辑页面 | 输出路径 |
|----------|----------|
| 中文首页 | `docs/zh/index.md` |
| 英文首页 | `docs/en/index.md` |
| 中文算法页 | `docs/zh/algorithms/{id}.md` |
| 英文算法页 | `docs/en/algorithms/{id}.md` |
| 中文分类页 | `docs/zh/categories/{cat_id}/index.md` |
| 英文分类页 | `docs/en/categories/{cat_id}/index.md` |
| 白皮书页面 | `docs/{lang}/{section}/{page}.md` |

---

## 渲染层（Render）

### VitePress 构建流程

1. **解析阶段**：VitePress 扫描 `docs/` 下所有 `.md` 文件，提取 frontmatter 构建页面元数据
2. **路由阶段**：根据文件路径自动生成 URL 路由（如 `zh/algorithms/smith-waterman.md` → `/zh/algorithms/smith-waterman`）
3. **渲染阶段**：Markdown → HTML，应用主题 CSS、代码高亮、Mermaid 图表转换
4. **优化阶段**：Vite 对 JS/CSS 进行 tree-shaking、压缩与 chunk 分割
5. **输出阶段**：生成 `dist/` 目录，包含所有静态资源

### 主题配置

`.vitepress/config.ts` 负责：

- 导航栏（Navbar）链接映射
- 侧边栏（Sidebar）分组与折叠
- 多语言 `locales` 配置
- Mermaid 插件集成
- 本地搜索索引配置

---

## 数据结构详细说明

### 算法 YAML 字段约束

| 字段名 | 类型 | 必填 | 约束 | 示例 |
|--------|------|------|------|------|
| `id` | string | 是 | 全局唯一，小写连字符 | `smith-waterman` |
| `name` | string | 是 | 算法标准名称 | `Smith-Waterman` |
| `description` | string | 是 | 50–500 字符（trimmed） | 经典的局部序列比对算法... |
| `purpose` | string | 是 | 简要用途描述 | 局部序列比对... |
| `time_complexity` | string | 是 | 匹配 `O(...)` 模式 | `O(mn)` |
| `category` | string | 是 | 必须存在于 categories.yaml | `sequence-alignment` |
| `space_complexity` | string | 否 | 匹配 `O(...)` 模式 | `O(mn)` |
| `year` | int | 否 | 正整数 | `1981` |
| `paper_url` | string | 否 | 有效 URL | `https://doi.org/...` |
| `implementation_url` | string | 否 | 有效 URL | `https://github.com/...` |
| `related_tools` | list[str] | 否 | 工具名列表 | `["Biopython"]` |
| `tags` | list[str] | 否 | 小写连字符 | `["local-alignment"]` |
| `subcategory` | string | 否 | 必须属于对应 category 的子分类 | `pairwise` |
| `difficulty` | string | 否 | `beginner`/`intermediate`/`advanced` | `intermediate` |
| `language` | list[str] | 否 | 实现语言列表 | `["C", "C++"]` |
| `references` | list[dict] | 否 | 每项含 `url`，可选 `title`、`type` | — |
| `description_en` | string | 否 | 英文描述 | Local alignment algorithm... |
| `purpose_en` | string | 否 | 英文用途 | Local sequence alignment... |

---

## Schema 演化历史

| 版本 | 时间 | 变更内容 | 兼容性 |
|------|------|----------|--------|
| v1 | 2024 Q1 | 初始 schema，仅包含 id/name/description/purpose/time_complexity/category | — |
| v2 | 2024 Q2 | 增加 space_complexity、year、paper_url、implementation_url、tags、difficulty | 向后兼容 |
| v3 | 2024 Q3 | 增加 subcategory、language、references、related_tools；引入 `*_en` 双语字段 | 向后兼容 |
| v4（规划中）| 2025 Q2 | 拟增加 benchmark 数据字段（准确率、内存、运行时间）与插件扩展字段 | — |

---

## 数据质量指标

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| 验证规则数 | 12 条字段规则 + 1 份 JSON Schema | 20+ 条 |
| 字段覆盖率 | 必填字段 100%，可选字段 ~65% | 可选字段 80% |
| 描述长度合格率 | >95%（50–500 字符） | 100% |
| ID 唯一性 | 100% | 100% |
| Category 存在性 | 100% | 100% |
| 复杂度格式合规率 | 100% | 100% |
| 双语覆盖率 | >60% | 75% |

---

## 构建命令速查表

```bash
# 验证数据完整性
python -m awesome_bioinfo validate

# 查看项目统计
python -m awesome_bioinfo stats

# 生成 VitePress 文档（中文 + 英文）
python -m awesome_bioinfo vitepress

# 本地预览
cd docs && npm run dev

# 生产构建
cd docs && npm run build

# 预览构建产物
cd docs && npm run preview
```

---

## 数据更新流程

当需要新增或修改算法数据时，请遵循以下标准化流程：

```mermaid
flowchart LR
    A[编辑 YAML] --> B[本地验证]
    B --> C{通过?}
    C -->|否| A
    C -->|是| D[生成文档]
    D --> E[VitePress 构建]
    E --> F[提交 PR]
    F --> G[CI 验证]
    G --> H{通过?}
    H -->|否| A
    H -->|是| I[合并并自动部署]
```

1. **编辑 YAML**：复制 `templates/algorithm_template.yaml`，填写字段后保存至对应分类文件
2. **本地验证**：运行 `python -m awesome_bioinfo validate`，修复所有报错
3. **生成文档**：运行 `python -m awesome_bioinfo vitepress`，确认生成页面内容正确
4. **VitePress 构建**：`cd docs && npm run build`，确保无构建错误
5. **提交 PR**：遵循 Conventional Commits 规范提交信息
6. **CI 验证**：GitHub Actions 自动执行 lint、typecheck、tests、validate
7. **合并并自动部署**：PR 合并后，GitHub Actions 自动构建并部署至 GitHub Pages
"""


def _make_en_data_pipeline() -> str:
    return """---
title: Data and Generation Pipeline
---

# Data and Generation Pipeline

## Overview

The core engineering capability of this knowledge base lies in a complete ETL (Extract-Transform-Load) data pipeline: from human-editable YAML raw data, through Python generator transformation and rendering, to final static Markdown directly consumable by VitePress. This page dissects each stage's input, processing logic, output, and observable metrics.

```mermaid
flowchart LR
    E[Extract<br/>YAML Files] --> T[Transform<br/>Python / Jinja2]
    T --> L[Load<br/>Markdown]
    L --> R[Render<br/>VitePress]
```

---

## Extract Layer

### Input

- `data/categories.yaml`: Definitions for 16 top-level categories and 30+ subcategories
- `data/algorithms/*.yaml`: 195+ algorithm entries, one file per top-level category

### Loading Mechanism

`DataStore.load_all()` uses PyYAML to parse all files and build in-memory objects:

1. Load `categories.yaml` first, building the `Category` tree (including subcategory `parent_id` back-links)
2. Traverse all `.yaml` files under `data/algorithms/`, converting each list item to an `AlgorithmEntry`
3. Build auxiliary indexes: `cat_map` (category id → Category), `by_cat` (category id → [AlgorithmEntry]), `by_tag` (tag → [AlgorithmEntry])

### Constraints and Validation

The loading stage only guarantees YAML syntax correctness; business rule validation (e.g., ID uniqueness, description length, category existence) is handled by downstream `validate.py`.

---

## Transform Layer

### Field-Level Transformation

Each `AlgorithmEntry` contains 15+ fields; the Transform layer's primary job is mapping these structured fields to Markdown presentation elements:

| Field | Source | Markdown Presentation |
|-------|--------|----------------------|
| `id` | YAML | Filename, URL path, anchor |
| `name` | YAML | Page title (H1), table link text |
| `description` | YAML | frontmatter `description`, page first paragraph |
| `purpose` | YAML | Info table "Purpose" row |
| `time_complexity` | YAML | Info table + Complexity Analysis section |
| `space_complexity` | YAML | Info table + Complexity Analysis section |
| `year` | YAML | Info table, year badge |
| `difficulty` | YAML | Difficulty badge (beginner/intermediate/advanced) |
| `language` | YAML | Info table, comma-separated |
| `category` | YAML | Category page link |
| `subcategory` | YAML | Sub-grouping within category pages |
| `tags` | YAML | Tag link cloud |
| `paper_url` | YAML | "Paper" link (with external link icon) |
| `implementation_url` | YAML | "Implementation" link |
| `related_tools` | YAML | Inline code-style tool names |
| `references` | YAML | Reference list (GB-T 7714 / IEEE format) |
| `*_en` | YAML | Fallback for corresponding English site fields |

### Generator Logic

The generator functions in `generate_docs.py` are layered by responsibility:

- **Whitepaper Generators** (`_generate_*`): Pure text templates outputting architecture narratives, academy paths, quality assurance, and other in-depth content
- **Algorithm Page Generators** (`generate_*_algo_page`): Take a single `AlgorithmEntry` as input, outputting frontmatter + description + info table + complexity analysis + links + tags + references
- **Index Page Generators** (`generate_*_index`): Take an algorithm list as input, outputting sorted tables (alphabetical by name)
- **Category Page Generators** (`generate_*_category_page`): Take `Category` + algorithm list as input, outputting tables grouped by subcategory

### Jinja2 Alternative

Current generators use Python f-strings to directly concatenate Markdown. If future template complexity increases (conditional rendering, nested loops, multilingual interpolation), Jinja2 may be evaluated as a template engine, but the trade-off against the current "zero external template dependency" simplicity must be weighed.

---

## Load Layer

### Markdown Output Specification

All generated Markdown follows the following specifications to ensure correct VitePress rendering:

- **Frontmatter**: Every page starts with `---
title: ...
---`; algorithm pages additionally include a `description` field for SEO
- **Heading Levels**: H1 appears only once (page main title), H2 for major sections, H3 for subsections
- **Tables**: All tables must include header separator rows (`|---|---|`), with bold or code styling in headers for readability
- **Code Blocks**: Complexity and command examples use fenced code blocks (```) with language annotations (e.g., `bash`, `mermaid`)
- **Links**: Internal links use relative paths (`../categories/xxx/`), external links use full URLs
- **Mermaid Diagrams**: Use standard syntax such as `flowchart LR`; **hard-coded colors are prohibited** (e.g., `style A fill:#10b981`); rely on VitePress theme CSS variables for styling control

### Filesystem Mapping

| Logical Page | Output Path |
|--------------|-------------|
| Chinese Home | `docs/zh/index.md` |
| English Home | `docs/en/index.md` |
| Chinese Algorithm Page | `docs/zh/algorithms/{id}.md` |
| English Algorithm Page | `docs/en/algorithms/{id}.md` |
| Chinese Category Page | `docs/zh/categories/{cat_id}/index.md` |
| English Category Page | `docs/en/categories/{cat_id}/index.md` |
| Whitepaper Pages | `docs/{lang}/{section}/{page}.md` |

---

## Render Layer

### VitePress Build Flow

1. **Parse Phase**: VitePress scans all `.md` files under `docs/`, extracting frontmatter to build page metadata
2. **Route Phase**: URL routes are automatically generated from file paths (e.g., `zh/algorithms/smith-waterman.md` → `/zh/algorithms/smith-waterman`)
3. **Render Phase**: Markdown → HTML, applying theme CSS, code highlighting, and Mermaid diagram conversion
4. **Optimize Phase**: Vite performs tree-shaking, compression, and chunk splitting on JS/CSS
5. **Output Phase**: Generates the `dist/` directory containing all static assets

### Theme Configuration

`.vitepress/config.ts` manages:

- Navigation bar (Navbar) link mapping
- Sidebar grouping and collapse behavior
- Multi-language `locales` configuration
- Mermaid plugin integration
- Local search index configuration

---

## Data Structure Details

### Algorithm YAML Field Constraints

| Field Name | Type | Required | Constraints | Example |
|------------|------|----------|-------------|---------|
| `id` | string | Yes | Globally unique, lowercase-hyphenated | `smith-waterman` |
| `name` | string | Yes | Standard algorithm name | `Smith-Waterman` |
| `description` | string | Yes | 50–500 characters (trimmed) | A classic local alignment algorithm... |
| `purpose` | string | Yes | Brief purpose description | Local sequence alignment... |
| `time_complexity` | string | Yes | Must match `O(...)` pattern | `O(mn)` |
| `category` | string | Yes | Must exist in categories.yaml | `sequence-alignment` |
| `space_complexity` | string | No | Must match `O(...)` pattern | `O(mn)` |
| `year` | int | No | Positive integer | `1981` |
| `paper_url` | string | No | Valid URL | `https://doi.org/...` |
| `implementation_url` | string | No | Valid URL | `https://github.com/...` |
| `related_tools` | list[str] | No | Tool name list | `["Biopython"]` |
| `tags` | list[str] | No | Lowercase-hyphenated | `["local-alignment"]` |
| `subcategory` | string | No | Must belong to the category's subcategories | `pairwise` |
| `difficulty` | string | No | `beginner`/`intermediate`/`advanced` | `intermediate` |
| `language` | list[str] | No | Implementation language list | `["C", "C++"]` |
| `references` | list[dict] | No | Each with `url`, optional `title`, `type` | — |
| `description_en` | string | No | English description | Local alignment algorithm... |
| `purpose_en` | string | No | English purpose | Local sequence alignment... |

---

## Schema Evolution History

| Version | Time | Changes | Compatibility |
|---------|------|---------|---------------|
| v1 | 2024 Q1 | Initial schema: id, name, description, purpose, time_complexity, category only | — |
| v2 | 2024 Q2 | Added space_complexity, year, paper_url, implementation_url, tags, difficulty | Backward compatible |
| v3 | 2024 Q3 | Added subcategory, language, references, related_tools; introduced `*_en` bilingual fields | Backward compatible |
| v4 (planned) | 2025 Q2 | Proposed addition of benchmark data fields (accuracy, memory, runtime) and plugin extension fields | — |

---

## Data Quality Metrics

| Metric | Current Value | Target Value |
|--------|---------------|--------------|
| Validation Rules | 12 field rules + 1 JSON Schema | 20+ rules |
| Field Coverage | Required 100%, Optional ~65% | Optional 80% |
| Description Length Pass Rate | >95% (50–500 chars) | 100% |
| ID Uniqueness | 100% | 100% |
| Category Existence | 100% | 100% |
| Complexity Format Compliance | 100% | 100% |
| Bilingual Coverage | >60% | 75% |

---

## Build Command Cheat Sheet

```bash
# Validate data integrity
python -m awesome_bioinfo validate

# View project statistics
python -m awesome_bioinfo stats

# Generate VitePress documentation (Chinese + English)
python -m awesome_bioinfo vitepress

# Local preview
cd docs && npm run dev

# Production build
cd docs && npm run build

# Preview build artifacts
cd docs && npm run preview
```

---

## Data Update Workflow

When adding or modifying algorithm data, please follow this standardized workflow:

```mermaid
flowchart LR
    A[Edit YAML] --> B[Local Validation]
    B --> C{Pass?}
    C -->|No| A
    C -->|Yes| D[Generate Docs]
    D --> E[VitePress Build]
    E --> F[Submit PR]
    F --> G[CI Validation]
    G --> H{Pass?}
    H -->|No| A
    H -->|Yes| I[Merge & Auto-Deploy]
```

1. **Edit YAML**: Copy `templates/algorithm_template.yaml`, fill in fields, and save to the corresponding category file
2. **Local Validation**: Run `python -m awesome_bioinfo validate` and fix all errors
3. **Generate Docs**: Run `python -m awesome_bioinfo vitepress` and verify generated page content
4. **VitePress Build**: `cd docs && npm run build`, ensuring no build errors
5. **Submit PR**: Follow Conventional Commits specification for commit messages
6. **CI Validation**: GitHub Actions automatically executes lint, typecheck, tests, and validate
7. **Merge and Auto-Deploy**: After PR merge, GitHub Actions automatically builds and deploys to GitHub Pages
"""


def _make_zh_quality_assurance() -> str:
    return """---
title: 质量保障
---

# 质量保障

## 概述

本知识库的质量体系采用三层纵深防御架构：数据层验证（Data Validation）、代码层质量（Code Quality）与文档层验证（Documentation Verification）。任何一层发现缺陷均会阻断构建流程，确保最终部署到 GitHub Pages 的每一字节内容都经过自动化验证。

```mermaid
flowchart LR
    subgraph Data["数据层"]
        D1[YAML Syntax]
        D2[Field Rules]
        D3[JSON Schema]
    end
    subgraph Code["代码层"]
        C1[ruff]
        C2[mypy]
        C3[pytest 89%]
    end
    subgraph Doc["文档层"]
        V1[VitePress Build]
        V2[Link Check]
        V3[Nav Consistency]
    end
    Data --> Code --> Doc
```

---

## 数据层验证（Data Validation）

数据层验证是质量体系的基石，所有算法条目在进入生成链路前必须通过双重验证。

### YAML Schema 校验

`validate.py` 实现了 12 条硬编码字段规则，覆盖以下维度：

| 规则编号 | 校验项 | 说明 | 失败示例 |
|----------|--------|------|----------|
| R01 | `id` 全局唯一性 | 所有算法文件中不得出现重复 ID | 两个文件同时定义 `id: blast` |
| R02 | `id` 命名规范 | 仅允许小写字母、数字与连字符 | `id: BLAST` |
| R03 | `description` 长度 | 50–500 字符（trim 后） | 长度为 20 或 600 |
| R04 | `time_complexity` 格式 | 须匹配 `O(...)` 正则模式 | `O(n^2)`（缺少括号） |
| R05 | `space_complexity` 格式 | 同上，若存在 | — |
| R06 | `category` 存在性 | 必须存在于 `categories.yaml` | `category: unknown-cat` |
| R07 | `subcategory` 存在性 | 若填写，必须属于对应 category 的子分类 | `subcategory: wrong-sub` |
| R08 | `difficulty` 枚举值 | 必须为 beginner/intermediate/advanced | `difficulty: hard` |
| R09 | `year` 范围 | 1900–当前年份 | `year: 1800` |
| R10 | `paper_url` 格式 | 若存在，须为有效 URL 格式 | `paper_url: not-a-url` |
| R11 | `tags` 命名 | 小写连字符，无空格 | `tags: ["Local Alignment"]` |
| R12 | `language` 非空 | 若存在，不得为空列表 | `language: []` |

### JSON Schema 双重验证

`schemas/algorithm-schema.json` 作为独立的 JSON Schema 文件，提供与字段规则互补的结构化验证：

- **类型约束**：确保 `year` 为 integer、`tags` 为 array of strings
- **必填约束**：确保 `id`、`name`、`description`、`purpose`、`time_complexity`、`category` 六项必填
- **字符串模式**：`time_complexity` 与 `space_complexity` 通过 JSON Schema 的 `pattern` 属性执行 `O(...)` 正则校验
- **枚举约束**：`difficulty` 通过 `enum` 限定合法取值

字段规则与 JSON Schema 的双重验证形成"业务逻辑 + 数据结构"的互补覆盖，降低单一验证层失效的风险。

---

## 代码层质量（Code Quality）

生成器本身的质量直接决定输出文档的正确性。本项目通过以下工具链保证 Python 代码的工程级质量：

### ruff（Lint & Format）

- **规则集**：E（pycodestyle）、F（Pyflakes）、W（pycodestyle warnings）、I（isort）、N（pep8-naming）、UP（pyupgrade）、B（flake8-bugbear）、C4（flake8-comprehensions）
- **行宽**：100 字符
- **导入排序**：自动按标准库 → 第三方库 → 本地模块分组排序
- **自动修复**：`ruff check --fix` 可自动修复大部分格式问题

### mypy（Type Checking）

- **模式**：渐进式严格模式（progressive strict mode）
- **配置**：`ignore_missing_imports = true`，允许第三方库无类型存根
- **覆盖模块**：`awesome_bioinfo/` 下全部 15 个核心模块
- **类型注解**：所有公共函数须标注参数类型与返回值类型

### pytest（Testing）

- **框架**：pytest + hypothesis（属性测试）
- **测试文件**：15 个测试模块，命名 `test_*.py`
- **覆盖率**：当前 89%，目标 90%+
- **关键测试域**：
  - `test_validate.py`：边界值（description 长度、O(...) 格式、重复 ID）
  - `test_algorithm_registry.py`：索引一致性、搜索结果正确性
  - `test_data_completeness.py`：所有现有 YAML 文件通过 validate
  - `test_cli.py`：各子命令的集成路径
  - `test_generate_docs.py`：白皮书文件存在性、Mermaid 包含性、首页定位

---

## 文档层验证（Documentation Verification）

即使数据与代码均正确，文档构建过程中的问题仍可能导致站点无法访问或导航断裂。文档层验证覆盖以下维度：

### VitePress 构建验证

- **构建通过性**：`npm run build` 必须零错误退出
- **死链检测**：通过 `link_checker.py` 异步检查算法条目中的外部 URL（`paper_url`、`implementation_url`、`references[].url`）
- **Mermaid 渲染**：所有含 Mermaid 图表的页面须正确渲染，无语法错误

### 导航一致性检查

- **侧边栏映射**：`.vitepress/config.ts` 中的 `sidebar` 配置须与 `docs/` 下的实际目录结构一致
- **多语言对称**：中英文对应页面的 frontmatter `title` 须同时存在
- **分类页完整性**：每个在 `categories.yaml` 中定义的分类，若包含算法，则必须生成对应的分类索引页

---

## CI/CD 流程

GitHub Actions 工作流将上述三层验证串联为一条不可绕过的自动化流水线：

```mermaid
flowchart LR
    A[Push / PR] --> B[ruff + mypy]
    B --> C{Pass?}
    C -->|No| X[Fail]
    C -->|Yes| D[pytest 89%]
    D --> E{Pass?}
    E -->|No| X
    E -->|Yes| F[validate]
    F --> G{Pass?}
    G -->|No| X
    G -->|Yes| H[vitepress generate]
    H --> I[VitePress build]
    I --> J{Pass?}
    J -->|No| X
    J -->|Yes| K[Deploy to Pages]
```

### 工作流阶段说明

| 阶段 | 命令 | 失败阻断 | 平均耗时 |
|------|------|----------|----------|
| Lint & Typecheck | `ruff check awesome_bioinfo && mypy awesome_bioinfo` | 是 | ~5 s |
| Unit Tests | `pytest tests/ -v --tb=short` | 是 | ~15 s |
| Data Validation | `python -m awesome_bioinfo validate` | 是 | ~2 s |
| Doc Generation | `python -m awesome_bioinfo vitepress` | 是 | ~3 s |
| VitePress Build | `cd docs && npm run build` | 是 | ~15 s |
| Deploy | `actions/deploy-pages` | 否（仅部署） | ~10 s |

---

## 质量指标表

| 指标维度 | 指标项 | 当前值 | 目标值 | 测量方式 |
|----------|--------|--------|--------|----------|
| 数据质量 | 验证通过率 | 100% | 100% | `validate` 零报错 |
| 数据质量 | 字段完整率 | ~65% | 80% | 可选非空字段占比 |
| 数据质量 | 文献覆盖率 | >85% | 90% | 含 paper_url 条目占比 |
| 代码质量 | 测试覆盖率 | 89% | 90% | `pytest --cov` |
| 代码质量 | Lint 通过率 | 100% | 100% | `ruff check` 零报错 |
| 代码质量 | 类型检查通过率 | 100% | 100% | `mypy` 零错误 |
| 文档质量 | 构建成功率 | 100% | 100% | `npm run build` 零错误 |
| 文档质量 | 死链率 | <2% | <1% | `link_checker.py` 统计 |

---

## 常见错误及解决方案

| 错误现象 | 根因 | 解决方案 |
|----------|------|----------|
| `validate` 报 "description too short" | 描述少于 50 字符 | 补充算法背景、输入输出与核心思想的说明 |
| `validate` 报 "duplicate id" | 两个 YAML 文件定义了相同 ID | 检查全局唯一性，使用更具体的 ID（如 `blastn` 而非 `blast`） |
| `mypy` 报 "Missing return statement" | 函数分支未全覆盖 | 添加 `return` 或 `raise` 至所有分支 |
| VitePress 构建失败 "dead link" | Markdown 中的相对路径错误 | 检查链接目标文件是否实际生成 |
| Mermaid 图表不渲染 | 语法错误或不支持的指令 | 使用标准 `flowchart LR` / `flowchart TD`，避免 experimental 语法 |
| pytest 覆盖率下降 | 新增代码未覆盖测试 | 为新增函数补充单元测试，使用 `pytest --cov-report=term-missing` 定位 |
"""


def _make_en_quality_assurance() -> str:
    return """---
title: Quality Assurance
---

# Quality Assurance

## Overview

This knowledge base's quality system adopts a three-layer defense-in-depth architecture: Data Validation, Code Quality, and Documentation Verification. Defects discovered at any layer block the build pipeline, ensuring that every byte deployed to GitHub Pages has passed automated validation.

```mermaid
flowchart LR
    subgraph Data["Data Layer"]
        D1[YAML Syntax]
        D2[Field Rules]
        D3[JSON Schema]
    end
    subgraph Code["Code Layer"]
        C1[ruff]
        C2[mypy]
        C3[pytest 89%]
    end
    subgraph Doc["Doc Layer"]
        V1[VitePress Build]
        V2[Link Check]
        V3[Nav Consistency]
    end
    Data --> Code --> Doc
```

---

## Data Layer Validation

Data layer validation is the cornerstone of the quality system; all algorithm entries must pass dual validation before entering the generation pipeline.

### YAML Schema Validation

`validate.py` implements 12 hard-coded field rules covering the following dimensions:

| Rule ID | Check Item | Description | Failure Example |
|---------|------------|-------------|-----------------|
| R01 | `id` global uniqueness | No duplicate IDs across all algorithm files | Two files both define `id: blast` |
| R02 | `id` naming convention | Lowercase letters, digits, and hyphens only | `id: BLAST` |
| R03 | `description` length | 50–500 characters (after trim) | Length 20 or 600 |
| R04 | `time_complexity` format | Must match `O(...)` regex pattern | `O(n^2)` (missing parentheses) |
| R05 | `space_complexity` format | Same as above, if present | — |
| R06 | `category` existence | Must exist in `categories.yaml` | `category: unknown-cat` |
| R07 | `subcategory` existence | If filled, must belong to the category's subcategories | `subcategory: wrong-sub` |
| R08 | `difficulty` enum | Must be beginner/intermediate/advanced | `difficulty: hard` |
| R09 | `year` range | 1900–current year | `year: 1800` |
| R10 | `paper_url` format | If present, must be a valid URL format | `paper_url: not-a-url` |
| R11 | `tags` naming | Lowercase-hyphenated, no spaces | `tags: ["Local Alignment"]` |
| R12 | `language` non-empty | If present, must not be an empty list | `language: []` |

### JSON Schema Dual Validation

`schemas/algorithm-schema.json` serves as an independent JSON Schema file, providing structured validation complementary to field rules:

- **Type Constraints**: Ensures `year` is integer, `tags` is array of strings
- **Required Constraints**: Ensures `id`, `name`, `description`, `purpose`, `time_complexity`, `category` are all required
- **String Patterns**: `time_complexity` and `space_complexity` use JSON Schema's `pattern` property for `O(...)` regex validation
- **Enum Constraints**: `difficulty` is limited to legal values through `enum`

The dual validation of field rules and JSON Schema forms a complementary coverage of "business logic + data structure," reducing the risk of single validation layer failure.

---

## Code Layer Quality

The quality of the generator itself directly determines the correctness of output documents. This project guarantees engineering-grade Python code quality through the following toolchain:

### ruff (Lint & Format)

- **Rule Sets**: E (pycodestyle), F (Pyflakes), W (pycodestyle warnings), I (isort), N (pep8-naming), UP (pyupgrade), B (flake8-bugbear), C4 (flake8-comprehensions)
- **Line Width**: 100 characters
- **Import Sorting**: Automatically groups by stdlib → third-party → local modules
- **Auto-fix**: `ruff check --fix` automatically fixes most formatting issues

### mypy (Type Checking)

- **Mode**: Progressive strict mode
- **Config**: `ignore_missing_imports = true`, allowing third-party libraries without type stubs
- **Covered Modules**: All 15 core modules under `awesome_bioinfo/`
- **Type Annotations**: All public functions must annotate parameter types and return types

### pytest (Testing)

- **Framework**: pytest + hypothesis (property testing)
- **Test Files**: 15 test modules, named `test_*.py`
- **Coverage**: Currently 89%, target 90%+
- **Key Test Domains**:
  - `test_validate.py`: Boundary values (description length, O(...) format, duplicate IDs)
  - `test_algorithm_registry.py`: Index consistency, search result correctness
  - `test_data_completeness.py`: All existing YAML files pass validation
  - `test_cli.py`: Integration paths for each subcommand
  - `test_generate_docs.py`: Whitepaper file existence, Mermaid inclusion, homepage positioning

---

## Documentation Layer Verification

Even if data and code are correct, issues during document construction may still render the site inaccessible or break navigation. Documentation layer verification covers the following dimensions:

### VitePress Build Verification

- **Build Pass Rate**: `npm run build` must exit with zero errors
- **Dead Link Detection**: Asynchronously checks external URLs in algorithm entries (`paper_url`, `implementation_url`, `references[].url`) via `link_checker.py`
- **Mermaid Rendering**: All pages containing Mermaid diagrams must render correctly without syntax errors

### Navigation Consistency Checks

- **Sidebar Mapping**: The `sidebar` configuration in `.vitepress/config.ts` must be consistent with the actual directory structure under `docs/`
- **Multilingual Symmetry**: The frontmatter `title` must exist for corresponding pages in both Chinese and English
- **Category Page Completeness**: Every category defined in `categories.yaml` that contains algorithms must have a corresponding category index page generated

---

## CI/CD Pipeline

The GitHub Actions workflow chains the above three-layer validations into a single non-bypassable automation pipeline:

```mermaid
flowchart LR
    A[Push / PR] --> B[ruff + mypy]
    B --> C{Pass?}
    C -->|No| X[Fail]
    C -->|Yes| D[pytest 89%]
    D --> E{Pass?}
    E -->|No| X
    E -->|Yes| F[validate]
    F --> G{Pass?}
    G -->|No| X
    G -->|Yes| H[vitepress generate]
    H --> I[VitePress build]
    I --> J{Pass?}
    J -->|No| X
    J -->|Yes| K[Deploy to Pages]
```

### Workflow Stage Descriptions

| Stage | Command | Fail-Blocking | Average Duration |
|-------|---------|---------------|------------------|
| Lint & Typecheck | `ruff check awesome_bioinfo && mypy awesome_bioinfo` | Yes | ~5 s |
| Unit Tests | `pytest tests/ -v --tb=short` | Yes | ~15 s |
| Data Validation | `python -m awesome_bioinfo validate` | Yes | ~2 s |
| Doc Generation | `python -m awesome_bioinfo vitepress` | Yes | ~3 s |
| VitePress Build | `cd docs && npm run build` | Yes | ~15 s |
| Deploy | `actions/deploy-pages` | No (deploy only) | ~10 s |

---

## Quality Metrics Table

| Dimension | Metric | Current Value | Target Value | Measurement Method |
|-----------|--------|---------------|--------------|--------------------|
| Data Quality | Validation Pass Rate | 100% | 100% | `validate` zero errors |
| Data Quality | Field Completeness | ~65% | 80% | Ratio of optional non-empty fields |
| Data Quality | Literature Coverage | >85% | 90% | Ratio of entries with `paper_url` |
| Code Quality | Test Coverage | 89% | 90% | `pytest --cov` |
| Code Quality | Lint Pass Rate | 100% | 100% | `ruff check` zero errors |
| Code Quality | Type Check Pass Rate | 100% | 100% | `mypy` zero errors |
| Doc Quality | Build Success Rate | 100% | 100% | `npm run build` zero errors |
| Doc Quality | Dead Link Rate | <2% | <1% | `link_checker.py` statistics |

---

## Common Errors and Solutions

| Symptom | Root Cause | Solution |
|---------|------------|----------|
| `validate` reports "description too short" | Description fewer than 50 characters | Supplement algorithm background, input/output, and core idea descriptions |
| `validate` reports "duplicate id" | Two YAML files define the same ID | Check global uniqueness; use more specific IDs (e.g., `blastn` instead of `blast`) |
| `mypy` reports "Missing return statement" | Function branches not fully covered | Add `return` or `raise` to all branches |
| VitePress build fails "dead link" | Incorrect relative path in Markdown | Check whether the link target file is actually generated |
| Mermaid diagram not rendering | Syntax error or unsupported directive | Use standard `flowchart LR` / `flowchart TD`; avoid experimental syntax |
| pytest coverage drops | New code not covered by tests | Supplement unit tests for new functions; use `pytest --cov-report=term-missing` to locate gaps |
"""


def _make_zh_references() -> str:
    return """---
title: 参考文献与相关项目
---

# 参考文献与相关项目

## 引用格式规范

本知识库所有算法条目中的参考文献遵循 **GB-T 7714-2015《信息与文献 参考文献著录规则》** 标准格式。著录要素包括：主要责任者、题名、文献类型标识、出版项、获取与访问路径。

### 格式示例

> JONES N C, PEVZNER P A. An Introduction to Bioinformatics Algorithms[M]. Cambridge: MIT Press, 2004.

> ALTSCHUL S F, MADDEN T L, SCHAFFER A A, et al. Gapped BLAST and PSI-BLAST: a new generation of protein database search programs[J]. Nucleic Acids Research, 1997, 25(17): 3389-3402. DOI:10.1093/nar/25.17.3389.

---

## 按领域分类的经典论文

### 序列比对（Sequence Alignment）

1. NEEDLEMAN S B, WUNSCH C D. A general method applicable to the search for similarities in the amino acid sequence of two proteins[J]. Journal of Molecular Biology, 1970, 48(3): 443-453. DOI:10.1016/0022-2836(70)90057-4.
2. SMITH T F, WATERMAN M S. Identification of common molecular subsequences[J]. Journal of Molecular Biology, 1981, 147(1): 195-197. DOI:10.1016/0022-2836(81)90087-5.
3. ALTSCHUL S F, GISH W, MILLER W, et al. Basic local alignment search tool[J]. Journal of Molecular Biology, 1990, 215(3): 403-410. DOI:10.1016/S0022-2836(05)80360-2.
4. LI H, DURBIN R. Fast and accurate short read alignment with Burrows-Wheeler transform[J]. Bioinformatics, 2009, 25(14): 1754-1760. DOI:10.1093/bioinformatics/btp324.
5. LI H. Minimap2: pairwise alignment for nucleotide sequences[J]. Bioinformatics, 2018, 34(18): 3094-3100. DOI:10.1093/bioinformatics/bty191.

### 序列组装（Sequence Assembly）

1. PEVZNER P A, TANG H, WATERMAN M S. An Eulerian path approach to DNA fragment assembly[J]. Proceedings of the National Academy of Sciences, 2001, 98(17): 9748-9753. DOI:10.1073/pnas.171285098.
2. ZERBINO D R, BIRNEY E. Velvet: algorithms for de novo short read assembly using de Bruijn graphs[J]. Genome Research, 2008, 18(5): 821-829. DOI:10.1101/gr.074492.107.
3. BANKEVICH A, NURK S, ANTIPOV D, et al. SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing[J]. Journal of Computational Biology, 2012, 19(5): 455-477. DOI:10.1089/cmb.2012.0021.
4. KOREN S, WALENZ B P, BERLIN K, et al. Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and repeat separation[J]. Genome Research, 2017, 27(5): 722-736. DOI:10.1101/gr.215087.116.
5. KOLMOGOROV M, YUAN J, LIN Y, et al. Assembly of long, error-prone reads using repeat graphs[J]. Nature Biotechnology, 2019, 37(5): 540-546. DOI:10.1038/s41587-019-0072-8.

### 变异检测（Variant Calling）

1. MCKENNA A, HANNA M, BANKS E, et al. The Genome Analysis Toolkit: a MapReduce framework for analyzing next-generation DNA sequencing data[J]. Genome Research, 2010, 20(9): 1297-1303. DOI:10.1101/gr.107524.110.
2. DEPRISTO M A, BANKS E, POPLIN R, et al. A framework for variation discovery and genotyping using next-generation DNA sequencing data[J]. Nature Genetics, 2011, 43(5): 491-498. DOI:10.1038/ng.806.
3. POPLIN R, CHANG P C, ALEXANDER D, et al. A universal SNP and small-indel variant caller using deep neural networks[J]. Nature Biotechnology, 2018, 36(10): 983-987. DOI:10.1038/nbt.4235.
4. KIM S, SCHEFFLER K, HALPERN A L, et al. Strelka2: fast and accurate calling of germline and somatic variants[J]. Nature Methods, 2018, 15(8): 591-594. DOI:10.1038/s41592-018-0051-x.
5. CIBULSKIS K, LAWRENCE M S, CARTER S L, et al. Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples[J]. Nature Biotechnology, 2013, 31(3): 213-219. DOI:10.1038/nbt.2514.

### 蛋白质结构预测（Protein Structure Prediction）

1. JUMPER J, EVANS R, PRITZEL A, et al. Highly accurate protein structure prediction with AlphaFold[J]. Nature, 2021, 596(7873): 583-589. DOI:10.1038/s41586-021-03819-2.
2. BAEK M, DIMAIO F, ANISHCHENKO I, et al. Accurate prediction of protein structures and interactions using a three-track neural network[J]. Science, 2021, 373(6557): 871-876. DOI:10.1126/science.abj8754.
3. LIN Z, AKIN H, RAO R, et al. Evolutionary-scale prediction of atomic-level protein structure with a language model[J]. Science, 2023, 379(6637): 1123-1130. DOI:10.1126/science.ade2574.
4. WU R, DING F, WANG R, et al. High-resolution de novo structure prediction from primary sequence[J]. Nature Methods, 2024, 21(4): 682-690. DOI:10.1038/s41592-024-02272-z.
5. SENIOR A W, EVANS R, JUMPER J, et al. Improved protein structure prediction using potentials from deep learning[J]. Nature, 2020, 577(7792): 706-710. DOI:10.1038/s41586-019-1923-7.

### 单细胞分析（Single-Cell Analysis）

1. SATIJA R, FARRELL J A, GENNERT D, et al. Spatial reconstruction of single-cell gene expression data[J]. Nature Biotechnology, 2015, 33(5): 495-502. DOI:10.1038/nbt.3192.
2. WOLF F A, ANGERER P, THEIS F J. SCANPY: large-scale single-cell gene expression data analysis[J]. Genome Biology, 2018, 19(1): 15. DOI:10.1186/s13059-017-1382-0.
3. TRAPNELL C, CACCHIARELLI D, GRIMSBY J, et al. The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells[J]. Nature Biotechnology, 2014, 32(4): 381-386. DOI:10.1038/nbt.2859.
4. LOPEZ R, REGIER J, COLE M B, et al. Deep generative modeling for single-cell transcriptomics[J]. Nature Methods, 2018, 15(12): 1053-1058. DOI:10.1038/s41592-018-0229-2.
5. ZHENG G X Y, TERRY J M, BELGRADER P, et al. Massively parallel digital transcriptional profiling of single cells[J]. Nature Communications, 2017, 8: 14049. DOI:10.1038/ncomms14049.

### 宏基因组学（Metagenomics）

1. WOOD D E, SALZBERG S L. Kraken: ultrafast metagenomic sequence classification using exact alignments[J]. Genome Biology, 2014, 15(3): R46. DOI:10.1186/gb-2014-15-3-r46.
2. QIN J, LI R, RAES J, et al. A human gut microbial gene catalogue established by metagenomic sequencing[J]. Nature, 2010, 464(7285): 59-65. DOI:10.1038/nature08821.
3. TRUONG D T, FRANZOSA E A, TICKLE T L, et al. MetaPhlAn2 for enhanced metagenomic taxonomic profiling[J]. Nature Methods, 2015, 12(10): 902-903. DOI:10.1038/nmeth.3589.
4. ABUBUCKER S, SEGATA N, GOLL J, et al. Metabolic reconstruction for metagenomic data and its application to the human microbiome[J]. PLoS Computational Biology, 2012, 8(6): e1002358. DOI:10.1371/journal.pcbi.1002358.
5. SUNG J, ZHENG L, DUVVURI V, et al. Metabolic modeling with objective quantification of the human gut microbiome in inflammatory bowel disease[J]. Nature Microbiology, 2022, 7(7): 1126-1136. DOI:10.1038/s41564-022-01147-6.

---

## 必读综述

以下综述为各领域的"地图级"文献，建议作为进入该子领域的首要阅读材料：

1. 序列比对与序列搜索：ALTSCHUL S F, et al. Basic local alignment search tool[J]. J. Mol. Biol., 1990.（BLAST 奠基之作，理解启发式搜索的必读文献）
2. 蛋白质结构预测：JUMPER J, et al. Highly accurate protein structure prediction with AlphaFold[J]. Nature, 2021.（AlphaFold，结构生物学分水岭）
3. 单细胞技术：PAPALEXI E, SATIJA R. High-dimensional genomic data analysis: methods and challenges[J]. Nature Methods, 2022.（单细胞高维数据分析的方法论综述）
4. 宏基因组学：QUINCE C, et al. Shotgun metagenomics, from sampling to analysis[J]. Nature Biotechnology, 2017.（从湿实验到干实验的完整方法论）
5. 图基因组学：PATEN B, et al. Genome graphs and the evolution of genome inference[J]. Genome Research, 2017.（图基因组学的系统性综述）

---

## 相关开源项目探究

以下表格对比了本知识库与同类开源项目在产品定位、功能范围与工程实践上的差异：

| 项目名称 | 核心功能 | Stars | 主要语言 | 许可 | 与本项目差异 |
|----------|----------|-------|----------|------|--------------|
| [Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics) | 算法与工具列表 | 2.8k+ | Markdown | CC0 | 纯列表，无结构化元数据与生成链路 |
| [bioinformatics-workflows](https://github.com/topics/bioinformatics) | 分析流程模板 | N/A | Snakemake / Nextflow | 混合 | 聚焦流程而非算法本体 |
| [biostars-handbook](https://www.biostarhandbook.com/) | 教程与指南 | N/A | — | 商业 | 面向初学者的操作手册，非架构级知识库 |
| [OBF](https://www.open-bio.org/) / BioPython | 工具库与社区 | N/A | Python | MIT/BSD | 提供算法实现，非算法元数据索引 |
| 本项目 | 结构化算法知识库 + 白皮书 | — | Python | MIT | 强调数据驱动、生成链路、质量验证与双语支持 |

---

## 工程启发

在构建与维护本知识库的过程中，我们总结出以下三条对大型技术知识系统具有普适性的工程原则：

### 1. 数据单一真相源

当知识条目超过 100 时，"分散在多处的手写文档"必然出现不一致。将数据集中为结构化 YAML，所有展示层均从同一来源生成，是维持一致性的唯一可持续方案。

### 2. 生成驱动文档

人类编辑 Markdown 的效率在条目数达到 50 后急剧下降，且格式漂移不可避免。用代码生成文档，将人类的创造力聚焦于"数据内容"而非"排版格式"，可将维护成本降低一个数量级。

### 3. 验证优先于部署

在 CI/CD 中，任何未通过验证的数据变更必须阻断构建。"先验证、后生成、再部署"的顺序不可颠倒，否则死链、格式错误与数据不一致将污染生产环境。
"""


def _make_en_references() -> str:
    return """---
title: References and Related Projects
---

# References and Related Projects

## Citation Format Specification

All references in this knowledge base's algorithm entries follow the **IEEE citation standard** format. Recording elements include: primary authors, title, publication venue, volume/issue/pages, year, and DOI.

### Format Example

> [1] N. C. Jones and P. A. Pevzner, *An Introduction to Bioinformatics Algorithms*. Cambridge, MA: MIT Press, 2004.

> [2] S. F. Altschul, T. L. Madden, A. A. Schaffer, et al., "Gapped BLAST and PSI-BLAST: a new generation of protein database search programs," *Nucleic Acids Res.*, vol. 25, no. 17, pp. 3389–3402, 1997. DOI:10.1093/nar/25.17.3389.

---

## Classic Papers by Domain

### Sequence Alignment

1. [1] S. B. Needleman and C. D. Wunsch, "A general method applicable to the search for similarities in the amino acid sequence of two proteins," *J. Mol. Biol.*, vol. 48, no. 3, pp. 443–453, 1970. DOI:10.1016/0022-2836(70)90057-4.
2. [2] T. F. Smith and M. S. Waterman, "Identification of common molecular subsequences," *J. Mol. Biol.*, vol. 147, no. 1, pp. 195–197, 1981. DOI:10.1016/0022-2836(81)90087-5.
3. [3] S. F. Altschul, W. Gish, W. Miller, et al., "Basic local alignment search tool," *J. Mol. Biol.*, vol. 215, no. 3, pp. 403–410, 1990. DOI:10.1016/S0022-2836(05)80360-2.
4. [4] H. Li and R. Durbin, "Fast and accurate short read alignment with Burrows-Wheeler transform," *Bioinformatics*, vol. 25, no. 14, pp. 1754–1760, 2009. DOI:10.1093/bioinformatics/btp324.
5. [5] H. Li, "Minimap2: pairwise alignment for nucleotide sequences," *Bioinformatics*, vol. 34, no. 18, pp. 3094–3100, 2018. DOI:10.1093/bioinformatics/bty191.

### Sequence Assembly

1. [1] P. A. Pevzner, H. Tang, and M. S. Waterman, "An Eulerian path approach to DNA fragment assembly," *Proc. Natl. Acad. Sci. USA*, vol. 98, no. 17, pp. 9748–9753, 2001. DOI:10.1073/pnas.171285098.
2. [2] D. R. Zerbino and E. Birney, "Velvet: algorithms for de novo short read assembly using de Bruijn graphs," *Genome Res.*, vol. 18, no. 5, pp. 821–829, 2008. DOI:10.1101/gr.074492.107.
3. [3] A. Bankevich, S. Nurk, D. Antipov, et al., "SPAdes: a new genome assembly algorithm and its applications to single-cell sequencing," *J. Comput. Biol.*, vol. 19, no. 5, pp. 455–477, 2012. DOI:10.1089/cmb.2012.0021.
4. [4] S. Koren, B. P. Walenz, K. Berlin, et al., "Canu: scalable and accurate long-read assembly via adaptive k-mer weighting and repeat separation," *Genome Res.*, vol. 27, no. 5, pp. 722–736, 2017. DOI:10.1101/gr.215087.116.
5. [5] M. Kolmogorov, J. Yuan, Y. Lin, and P. A. Pevzner, "Assembly of long, error-prone reads using repeat graphs," *Nat. Biotechnol.*, vol. 37, no. 5, pp. 540–546, 2019. DOI:10.1038/s41587-019-0072-8.

### Variant Calling

1. [1] A. McKenna, M. Hanna, E. Banks, et al., "The Genome Analysis Toolkit: a MapReduce framework for analyzing next-generation DNA sequencing data," *Genome Res.*, vol. 20, no. 9, pp. 1297–1303, 2010. DOI:10.1101/gr.107524.110.
2. [2] M. A. DePristo, E. Banks, R. Poplin, et al., "A framework for variation discovery and genotyping using next-generation DNA sequencing data," *Nat. Genet.*, vol. 43, no. 5, pp. 491–498, 2011. DOI:10.1038/ng.806.
3. [3] R. Poplin, P. C. Chang, D. Alexander, et al., "A universal SNP and small-indel variant caller using deep neural networks," *Nat. Biotechnol.*, vol. 36, no. 10, pp. 983–987, 2018. DOI:10.1038/nbt.4235.
4. [4] S. Kim, K. Scheffler, A. L. Halpern, et al., "Strelka2: fast and accurate calling of germline and somatic variants," *Nat. Methods*, vol. 15, no. 8, pp. 591–594, 2018. DOI:10.1038/s41592-018-0051-x.
5. [5] K. Cibulskis, M. S. Lawrence, S. L. Carter, et al., "Sensitive detection of somatic point mutations in impure and heterogeneous cancer samples," *Nat. Biotechnol.*, vol. 31, no. 3, pp. 213–219, 2013. DOI:10.1038/nbt.2514.

### Protein Structure Prediction

1. [1] J. Jumper, R. Evans, A. Pritzel, et al., "Highly accurate protein structure prediction with AlphaFold," *Nature*, vol. 596, no. 7873, pp. 583–589, 2021. DOI:10.1038/s41586-021-03819-2.
2. [2] M. Baek, F. DiMaio, I. Anishchenko, et al., "Accurate prediction of protein structures and interactions using a three-track neural network," *Science*, vol. 373, no. 6557, pp. 871–876, 2021. DOI:10.1126/science.abj8754.
3. [3] Z. Lin, H. Akin, R. Rao, et al., "Evolutionary-scale prediction of atomic-level protein structure with a language model," *Science*, vol. 379, no. 6637, pp. 1123–1130, 2023. DOI:10.1126/science.ade2574.
4. [4] R. Wu, F. Ding, R. Wang, et al., "High-resolution de novo structure prediction from primary sequence," *Nat. Methods*, vol. 21, no. 4, pp. 682–690, 2024. DOI:10.1038/s41592-024-02272-z.
5. [5] A. W. Senior, R. Evans, J. Jumper, et al., "Improved protein structure prediction using potentials from deep learning," *Nature*, vol. 577, no. 7792, pp. 706–710, 2020. DOI:10.1038/s41586-019-1923-7.

### Single-Cell Analysis

1. [1] R. Satija, J. A. Farrell, D. Gennert, et al., "Spatial reconstruction of single-cell gene expression data," *Nat. Biotechnol.*, vol. 33, no. 5, pp. 495–502, 2015. DOI:10.1038/nbt.3192.
2. [2] F. A. Wolf, P. Angerer, and F. J. Theis, "SCANPY: large-scale single-cell gene expression data analysis," *Genome Biol.*, vol. 19, no. 1, p. 15, 2018. DOI:10.1186/s13059-017-1382-0.
3. [3] C. Trapnell, D. Cacchiarelli, J. Grimsby, et al., "The dynamics and regulators of cell fate decisions are revealed by pseudotemporal ordering of single cells," *Nat. Biotechnol.*, vol. 32, no. 4, pp. 381–386, 2014. DOI:10.1038/nbt.2859.
4. [4] R. Lopez, J. Regier, M. B. Cole, et al., "Deep generative modeling for single-cell transcriptomics," *Nat. Methods*, vol. 15, no. 12, pp. 1053–1058, 2018. DOI:10.1038/s41592-018-0229-2.
5. [5] G. X. Y. Zheng, J. M. Terry, P. Belgrader, et al., "Massively parallel digital transcriptional profiling of single cells," *Nat. Commun.*, vol. 8, p. 14049, 2017. DOI:10.1038/ncomms14049.

### Metagenomics

1. [1] D. E. Wood and S. L. Salzberg, "Kraken: ultrafast metagenomic sequence classification using exact alignments," *Genome Biol.*, vol. 15, no. 3, p. R46, 2014. DOI:10.1186/gb-2014-15-3-r46.
2. [2] J. Qin, R. Li, J. Raes, et al., "A human gut microbial gene catalogue established by metagenomic sequencing," *Nature*, vol. 464, no. 7285, pp. 59–65, 2010. DOI:10.1038/nature08821.
3. [3] D. T. Truong, E. A. Franzosa, T. L. Tickle, et al., "MetaPhlAn2 for enhanced metagenomic taxonomic profiling," *Nat. Methods*, vol. 12, no. 10, pp. 902–903, 2015. DOI:10.1038/nmeth.3589.
4. [4] S. Abubucker, N. Segata, J. Goll, et al., "Metabolic reconstruction for metagenomic data and its application to the human microbiome," *PLoS Comput. Biol.*, vol. 8, no. 6, p. e1002358, 2012. DOI:10.1371/journal.pcbi.1002358.
5. [5] J. Sung, L. Zheng, V. Duvvuri, et al., "Metabolic modeling with objective quantification of the human gut microbiome in inflammatory bowel disease," *Nat. Microbiol.*, vol. 7, no. 7, pp. 1126–1136, 2022. DOI:10.1038/s41564-022-01147-6.

---

## Must-Read Reviews

The following reviews are "map-level" literature for each domain and are recommended as the first reading material when entering a subfield:

1. Sequence alignment and search: S. F. Altschul et al., "Basic local alignment search tool," *J. Mol. Biol.*, 1990. (Foundational BLAST work; essential reading for understanding heuristic search.)
2. Protein structure prediction: J. Jumper et al., "Highly accurate protein structure prediction with AlphaFold," *Nature*, 2021. (AlphaFold, a watershed moment in structural biology.)
3. Single-cell technology: E. Papalexi and R. Satija, "High-dimensional genomic data analysis: methods and challenges," *Nat. Methods*, 2022. (Methodological review of single-cell high-dimensional data analysis.)
4. Metagenomics: C. Quince et al., "Shotgun metagenomics, from sampling to analysis," *Nat. Biotechnol.*, 2017. (Complete methodology from wet lab to dry lab.)
5. Graph genomics: B. Paten et al., "Genome graphs and the evolution of genome inference," *Genome Res.*, 2017. (Systematic review of graph genomics.)

---

## Related Open Source Ecosystem Analysis

The following table compares this knowledge base with similar open-source projects in terms of product positioning, functional scope, and engineering practices:

| Project Name | Core Function | Stars | Primary Language | License | Difference from This Project |
|--------------|---------------|-------|------------------|---------|------------------------------|
| [Awesome-Bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics) | Algorithm and tool list | 2.8k+ | Markdown | CC0 | Pure list, no structured metadata or generation pipeline |
| [bioinformatics-workflows](https://github.com/topics/bioinformatics) | Analysis workflow templates | N/A | Snakemake / Nextflow | Mixed | Focuses on workflows rather than algorithm ontology |
| [biostars-handbook](https://www.biostarhandbook.com/) | Tutorials and guides | N/A | — | Commercial | Operational manual for beginners, not architecture-grade knowledge base |
| [OBF](https://www.open-bio.org/) / BioPython | Tool library and community | N/A | Python | MIT/BSD | Provides algorithm implementations, not algorithm metadata indexing |
| This Project | Structured algorithm knowledge base + whitepaper | — | Python | MIT | Emphasizes data-driven, generation pipeline, quality verification, and bilingual support |

---

## Engineering Insights

In the process of building and maintaining this knowledge base, we summarize the following three engineering principles with universal applicability to large-scale technical knowledge systems:

### 1. Single Source of Truth

When knowledge entries exceed 100, "handwritten documents scattered in multiple places" inevitably become inconsistent. Centralizing data as structured YAML, with all presentation layers generated from the same source, is the only sustainable solution for maintaining consistency.

### 2. Generation-Driven Documentation

The efficiency of human-edited Markdown drops sharply after 50 entries, and format drift becomes unavoidable. Using code to generate documents, directing human creativity toward "data content" rather than "layout formatting," can reduce maintenance costs by an order of magnitude.

### 3. Validation Before Deployment

In CI/CD, any data change that fails validation must block the build. The sequence of "validate first, then generate, then deploy" must not be reversed; otherwise dead links, formatting errors, and data inconsistencies will pollute the production environment.
"""


def _make_zh_evolution() -> str:
    return """---
title: 演进思考
---

# 演进思考

## 概述

本知识库自 2024 年初立项以来，经历了三个明确的演进阶段。每一阶段都对应着不同的核心目标、关键动作与可交付产出。理解这些历史决策，有助于预判未来的技术债务与扩展方向。

---

## 阶段一：列表化收录（2024 Q1–Q2）

### 目标

解决"收录广度"问题，建立覆盖主要生物信息学子领域的多分类算法目录。核心 KPI 为：算法条目数 >100，分类体系覆盖 >=10 个顶级分类。

### 关键动作

1. 设计初始 YAML schema（v1），包含 id、name、description、purpose、time_complexity、category 六个必填字段
2. 基于 `categories.yaml` 建立 16 大顶级分类与 30+ 子分类的层级体系
3. 人工收录首批 100+ 算法条目，以经典算法（Smith-Waterman、Needleman-Wunsch、BLAST 等）为核心
4. 搭建最小可用的 VitePress 站点，支持分类浏览与算法详情页

### 产出物

- 195+ 算法条目（已超额完成）
- 16 顶级分类 × 30+ 子分类的层级体系
- 基础 VitePress 站点（中文 + 英文镜像）

---

## 阶段二：工程化治理（2024 Q2–Q4）

### 目标

解决"一致性与可维护性"问题，将"人工维护的 Markdown"升级为"数据驱动的生成系统"。核心 KPI 为：数据验证零误报、生成器测试覆盖率 >85%、CI/CD 全自动化。

### 关键动作

1. 引入 `validate.py` 字段规则与 JSON Schema 双重验证机制
2. 重构 `generate_docs.py`，将算法页、分类页、索引页从手写 Markdown 改为程序生成
3. 建立 CLI 命令体系（validate、stats、search、info、compare、export、vitepress）
4. 集成 ruff、mypy、pytest 代码质量工具链，测试覆盖率提升至 89%
5. 配置 GitHub Actions 工作流，实现 push→validate→generate→build→deploy 的全自动链路
6. 扩展 YAML schema 至 v3，新增 space_complexity、year、tags、difficulty、language、references 等字段

### 产出物

- 数据驱动的 VitePress 文档生成器
- 8 个 CLI 子命令的完整工具链
- 89% 测试覆盖率的 Python 测试套件
- 全自动 CI/CD 发布流程
- 算法模板文件（`templates/algorithm_template.yaml`）

---

## 阶段三：白皮书化表达（2025 Q1–至今）

### 目标

解决"专业说服力"问题，将知识库从"算法列表"提升为"技术白皮书与架构学院"。核心 KPI 为：白皮书页面平均行数 >200、学术引用覆盖率 >85%、Mermaid 架构图全覆盖。

### 关键动作

1. 重写全部白皮书生成函数（`_generate_*`），输出深度学术内容（项目导读、学院路径、系统架构、数据链路、质量保障、参考文献、演进思考、CLI 工作流）
2. 统一学术引用格式：中文采用 GB-T 7714，英文采用 IEEE
3. 引入 Mermaid 架构图（数据流、CI/CD、学习路径、系统架构），提升可视化表达力
4. 优化首页（Hero、Features、统计仪表盘、白皮书入口、研究方向、最新收录）
5. 增强算法页：复杂度分析独立小节、更专业的链接与标签呈现
6. 建立 OpenSpec 规范驱动开发（SDD）流程，`openspec/specs/` 作为需求唯一来源

### 产出物

- 14 份深度白皮书文档（中英文共 28 页）
- 统一的学术引用体系（GB-T 7714 / IEEE）
- 架构决策记录（ADR）文档
- OpenSpec 规范目录与提案工作流

---

## 技术债务清单

| 债务项 | 影响等级 | 描述 | 缓解计划 |
|--------|----------|------|----------|
| 双语覆盖率不足 | 中 | 仅 ~60% 条目提供英文描述 | 通过社区贡献与自动化翻译 API 逐步补齐 |
| 可选字段完整率低 | 中 | space_complexity、related_tools、references 等字段覆盖率 <70% | 在 validate 中增加警告（非阻断），引导贡献者补充 |
| 生成器未模板化 | 低 | 当前使用 Python f-string 拼接 Markdown，复杂度增加后维护困难 | 评估引入 Jinja2 模板引擎 |
| 无运行时 API | 低 | 所有查询须在生成时完成，无法支持动态检索 | 远期规划 REST API 层 |
| 外部链接未持续监控 | 低 | paper_url / implementation_url 可能失效 | 增强 `link_checker.py` 的 CI 集成频率 |

---

## 未来路线图

### 短期（1–3 个月）

| 任务 | 优先级 | 验收标准 |
|------|--------|----------|
| 提升双语覆盖率至 75% | P0 | `stats` 显示 description_en 覆盖率 >=75% |
| 增强算法页可视化 | P1 | 为 top-20 算法页增加复杂度分析扩展说明 |
| 优化 VitePress 搜索 | P1 | 支持按复杂度、年份、难度过滤的本地搜索 |
| 死链自动修复建议 | P2 | CI 中 link_checker 失败时输出替代链接建议 |

### 中期（3–6 个月）

| 任务 | 优先级 | 验收标准 |
|------|--------|----------|
| 引入算法 benchmark 数据字段 | P0 | YAML schema v4 支持准确率、运行时间、内存占用字段 |
| 插件系统 MVP | P1 | 支持第三方数据增强插件注册与执行 |
| 分类页可视化增强 | P1 | 分类页增加算法分布柱状图与年代趋势折线图 |
| 交互式复杂度对比工具 | P2 | 支持勾选多个算法生成复杂度对比表格 |

### 长期（6–12 个月）

| 任务 | 优先级 | 验收标准 |
|------|--------|----------|
| REST API 只读服务 | P1 | 提供 /api/v1/algorithms 等端点，延迟 <200ms |
| 多模态内容支持 | P2 | 支持算法流程图、伪代码、视频讲解的嵌入 |
| 社区贡献平台 | P2 | 基于 GitHub Issues 的算法提案与评审工作流 |
| 知识图谱构建 | P3 | 基于 category/tag/citation 构建可交互的知识图谱 |

---

## 设计模式记录

在知识库的工程实现中，以下三种设计模式被反复验证为有效：

### Repository Pattern（仓储模式）

`DataStore` 作为算法与分类数据的统一仓储，封装了所有数据加载、索引构建与查询逻辑。未来无论底层存储从 YAML 文件迁移到 SQLite、PostgreSQL 还是图数据库，业务层代码均无需修改。

### Template Method（模板方法模式）

`generate_docs.py` 中的中英文生成器共享相同的遍历骨架（遍历所有算法生成详情页、遍历所有分类生成分类页），但将语言特定的内容填充推迟到子类/函数实现。这种模式极大降低了新增语言版本（如日语、德语）的边际成本。

### Pipeline（管道模式）

整个数据链路（加载 → 验证 → 生成 → 构建 → 部署）被设计为一条顺序执行的管道，每个阶段的输出作为下一个阶段的输入，任何阶段的失败都会触发快速失败（fail-fast）机制。这种模式天然契合 CI/CD 工作流的设计哲学。
"""


def _make_en_evolution() -> str:
    return """---
title: Evolution Notes
---

# Evolution Notes

## Overview

Since its inception in early 2024, this knowledge base has gone through three distinct evolutionary phases. Each phase corresponds to different core objectives, key actions, and deliverables. Understanding these historical decisions helps anticipate future technical debt and expansion directions.

---

## Phase 1: List-Oriented Curation (2024 Q1–Q2)

### Goal

Solve the "breadth of coverage" problem by establishing a multi-category algorithm directory covering major bioinformatics subfields. Core KPIs: >100 algorithm entries, >=10 top-level categories.

### Key Actions

1. Designed the initial YAML schema (v1), containing six required fields: id, name, description, purpose, time_complexity, category
2. Established a hierarchy of 16 top-level categories and 30+ subcategories based on `categories.yaml`
3. Manually curated the first 100+ algorithm entries, focusing on classic algorithms (Smith-Waterman, Needleman-Wunsch, BLAST, etc.)
4. Built a minimally viable VitePress site supporting category browsing and algorithm detail pages

### Deliverables

- 195+ algorithm entries (exceeded target)
- 16 top-level categories × 30+ subcategory hierarchy
- Basic VitePress site (Chinese + English mirror)

---

## Phase 2: Engineering Governance (2024 Q2–Q4)

### Goal

Solve the "consistency and maintainability" problem by upgrading from "human-maintained Markdown" to a "data-driven generation system." Core KPIs: zero false positives in data validation, generator test coverage >85%, fully automated CI/CD.

### Key Actions

1. Introduced `validate.py` field rules and JSON Schema dual validation mechanisms
2. Refactored `generate_docs.py` to programmatically generate algorithm pages, category pages, and index pages instead of handwritten Markdown
3. Established a CLI command suite (validate, stats, search, info, compare, export, vitepress)
4. Integrated ruff, mypy, and pytest code quality toolchain; raised test coverage to 89%
5. Configured GitHub Actions workflow, achieving fully automated push→validate→generate→build→deploy pipeline
6. Extended YAML schema to v3, adding space_complexity, year, tags, difficulty, language, references, and other fields

### Deliverables

- Data-driven VitePress documentation generator
- Complete toolchain with 8 CLI subcommands
- Python test suite with 89% coverage
- Fully automated CI/CD release pipeline
- Algorithm template file (`templates/algorithm_template.yaml`)

---

## Phase 3: Whitepaper Positioning (2025 Q1–Present)

### Goal

Solve the "professional persuasiveness" problem by elevating the knowledge base from an "algorithm list" to a "technical whitepaper and architecture academy." Core KPIs: average whitepaper page length >200 lines, academic citation coverage >85%, full Mermaid architecture diagram coverage.

### Key Actions

1. Rewrote all whitepaper generator functions (`_generate_*`) to output in-depth academic content (project overview, learning path, system architecture, data pipeline, quality assurance, references, evolution notes, CLI workflow)
2. Unified academic citation formats: GB-T 7714 for Chinese, IEEE for English
3. Introduced Mermaid architecture diagrams (data flow, CI/CD, learning path, system architecture) to enhance visual expressiveness
4. Optimized homepage (Hero, Features, statistics dashboard, whitepaper entry points, research directions, latest additions)
5. Enhanced algorithm pages: independent complexity analysis section, more professional link and tag presentation
6. Established OpenSpec specification-driven development (SDD) process; `openspec/specs/` serves as the single source of requirements

### Deliverables

- 14 in-depth whitepaper documents (28 pages in Chinese + English)
- Unified academic citation system (GB-T 7714 / IEEE)
- Architecture Decision Records (ADR)
- OpenSpec specification directory and proposal workflow

---

## Technical Debt Register

| Debt Item | Impact Level | Description | Mitigation Plan |
|-----------|--------------|-------------|---------------|
| Insufficient bilingual coverage | Medium | Only ~60% of entries provide English descriptions | Gradually fill through community contributions and automated translation APIs |
| Low optional field completeness | Medium | space_complexity, related_tools, references coverage <70% | Add warnings (non-blocking) in validate to guide contributors |
| Generator not templatized | Low | Currently uses Python f-string concatenation for Markdown; maintenance becomes difficult as complexity grows | Evaluate introducing Jinja2 template engine |
| No runtime API | Low | All queries must be completed at generation time; cannot support dynamic retrieval | Long-term plan for REST API layer |
| External links not continuously monitored | Low | paper_url / implementation_url may become invalid | Enhance CI integration frequency for `link_checker.py` |

---

## Future Roadmap

### Short-term (1–3 months)

| Task | Priority | Acceptance Criteria |
|------|----------|---------------------|
| Raise bilingual coverage to 75% | P0 | `stats` shows description_en coverage >=75% |
| Enhance algorithm page visualization | P1 | Add complexity analysis extended descriptions for top-20 algorithm pages |
| Optimize VitePress search | P1 | Support local search filtered by complexity, year, and difficulty |
| Dead link auto-fix suggestions | P2 | CI link_checker failures output alternative link suggestions |

### Medium-term (3–6 months)

| Task | Priority | Acceptance Criteria |
|------|----------|---------------------|
| Introduce algorithm benchmark data fields | P0 | YAML schema v4 supports accuracy, runtime, and memory fields |
| Plugin system MVP | P1 | Support third-party data enrichment plugin registration and execution |
| Category page visualization enhancement | P1 | Category pages add algorithm distribution bar charts and era trend line charts |
| Interactive complexity comparison tool | P2 | Support selecting multiple algorithms to generate complexity comparison tables |

### Long-term (6–12 months)

| Task | Priority | Acceptance Criteria |
|------|----------|---------------------|
| REST API read-only service | P1 | Provide /api/v1/algorithms endpoints with latency <200ms |
| Multimodal content support | P2 | Support embedding algorithm flowcharts, pseudocode, and video tutorials |
| Community contribution platform | P2 | Algorithm proposal and review workflow based on GitHub Issues |
| Knowledge graph construction | P3 | Build interactive knowledge graphs based on category/tag/citation |

---

## Design Pattern Records

The following three design patterns have been repeatedly validated as effective in the engineering implementation of this knowledge base:

### Repository Pattern

`DataStore` serves as the unified repository for algorithm and category data, encapsulating all data loading, index building, and query logic. In the future, regardless of whether the underlying storage migrates from YAML files to SQLite, PostgreSQL, or graph databases, business layer code will require no modifications.

### Template Method Pattern

The Chinese and English generators in `generate_docs.py` share the same traversal skeleton (traverse all algorithms to generate detail pages, traverse all categories to generate category pages), but defer language-specific content filling to subclass/function implementations. This pattern significantly reduces the marginal cost of adding new language versions (e.g., Japanese, German).

### Pipeline Pattern

The entire data pipeline (load → validate → generate → build → deploy) is designed as a sequentially executed pipeline, where each stage's output serves as the next stage's input, and failure at any stage triggers a fail-fast mechanism. This pattern naturally aligns with the design philosophy of CI/CD workflows.
"""


def _make_zh_cli_workflow() -> str:
    return """---
title: CLI 工作流参考
---

# CLI 工作流参考

## 概述

`python -m awesome_bioinfo` 是本知识库的统一 CLI 入口，提供从数据验证、统计查询、全文搜索、算法对比到文档生成的完整工具链。本页提供所有子命令的完整用法参考、选项说明与典型示例。

---

## validate — 数据验证

验证所有 YAML 数据文件的完整性、一致性与合规性。

### 用法

```bash
python -m awesome_bioinfo validate [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--strict` | - | 将警告视为错误 | False |
| `--verbose` | -v | 输出详细验证日志 | False |

### 示例

```bash
# 标准验证
python -m awesome_bioinfo validate

# 严格模式（任何警告均阻断）
python -m awesome_bioinfo validate --strict

# 详细输出
python -m awesome_bioinfo validate --verbose
```

---

## stats — 项目统计

输出知识库的规模统计、字段覆盖率与分类分布。

### 用法

```bash
python -m awesome_bioinfo stats [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--format` | -f | 输出格式：table / json / csv | table |
| `--category` | -c | 指定分类过滤 | 全部 |

### 示例

```bash
# 标准统计表
python -m awesome_bioinfo stats

# JSON 格式输出
python -m awesome_bioinfo stats -f json

# 单分类统计
python -m awesome_bioinfo stats -c sequence-alignment
```

---

## search — 全文搜索

按名称、描述或标签搜索算法。

### 用法

```bash
python -m awesome_bioinfo search <query> [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--limit` | -n | 返回结果数量上限 | 10 |
| `--field` | - | 搜索字段：name / description / tag / all | all |
| `--lang` | -l | 输出语言：zh / en | zh |

### 示例

```bash
# 默认搜索
python -m awesome_bioinfo search smith

# 限制结果数
python -m awesome_bioinfo search "sequence alignment" -n 5

# 仅搜索标签
python -m awesome_bioinfo search "dynamic-programming" --field tag
```

---

## info — 算法详情

查看单个算法的完整元数据。

### 用法

```bash
python -m awesome_bioinfo info <algorithm-id> [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--format` | -f | 输出格式：table / json / yaml | table |
| `--lang` | -l | 输出语言：zh / en | zh |

### 示例

```bash
# 表格形式查看
python -m awesome_bioinfo info smith-waterman

# JSON 输出
python -m awesome_bioinfo info needleman-wunsch -f json

# 英文输出
python -m awesome_bioinfo info blast -l en
```

---

## compare — 算法对比

并排对比两个或多个算法的核心指标。

### 用法

```bash
python -m awesome_bioinfo compare <id1> <id2> [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--format` | -f | 输出格式：table / json | table |
| `--fields` | - | 指定对比字段，逗号分隔 | 全部 |

### 示例

```bash
# 默认对比
python -m awesome_bioinfo compare smith-waterman needleman-wunsch

# 仅对比复杂度与年份
python -m awesome_bioinfo compare blast bwa --fields time_complexity,year

# JSON 格式
python -m awesome_bioinfo compare minimap2 bwa-mem -f json
```

---

## export — 数据导出

将算法数据导出为 JSON、CSV 或其他格式。

### 用法

```bash
python -m awesome_bioinfo export [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--format` | -f | 输出格式：json / csv / yaml | json |
| `--output` | -o | 输出文件路径 | stdout |
| `--category` | -c | 指定分类过滤 | 全部 |

### 示例

```bash
# 导出全部数据为 JSON
python -m awesome_bioinfo export -f json -o algorithms.json

# 导出单分类为 CSV
python -m awesome_bioinfo export -f csv -c variant-calling -o variants.csv
```

---

## vitepress — 文档生成

生成 VitePress 静态站点源码（中文 + 英文）。

### 用法

```bash
python -m awesome_bioinfo vitepress [options]
```

### 选项

| 选项 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--clean` | - | 生成前清空 docs/zh 与 docs/en | False |
| `--lang` | -l | 仅生成指定语言：zh / en / all | all |

### 示例

```bash
# 生成全部文档
python -m awesome_bioinfo vitepress

# 仅生成中文
python -m awesome_bioinfo vitepress -l zh

# 清空后重新生成
python -m awesome_bioinfo vitepress --clean
```

---

## 数据管理指南

### 添加新算法

1. 复制模板：`cp templates/algorithm_template.yaml data/algorithms/<category>.yaml`（追加到现有文件或新建）
2. 填写字段，确保 `id` 全局唯一，`description` 50–500 字符
3. 运行验证：`python -m awesome_bioinfo validate`
4. 生成文档：`python -m awesome_bioinfo vitepress`
5. 本地预览：`cd docs && npm run dev`
6. 提交 PR，等待 CI 通过

### 更新分类体系

1. 修改 `data/categories.yaml`，新增或调整分类/子分类
2. 同步更新所有引用该分类的算法 YAML 文件中的 `category` / `subcategory` 字段
3. 运行验证与生成命令确认无报错
4. 由于分类变更是 spec 级变更，须通过 `/opsx:propose` 提案流程

---

## VitePress 命令速查

```bash
cd docs

# 本地开发预览
npm run dev

# 生产构建
npm run build

# 预览构建产物
npm run preview
```

---

## CI/CD 集成说明

### GitHub Actions 工作流

`.github/workflows/` 下定义了以下工作流：

- **lint.yml**：ruff + mypy，在每次 push 时触发
- **test.yml**：pytest 全量测试 + 覆盖率上报，在 PR 与 push 时触发
- **validate.yml**：`python -m awesome_bioinfo validate`，在数据文件变更时触发
- **deploy.yml**：`vitepress generate` → `npm run build` → deploy to Pages，在 master 分支 push 时触发

### 本地预提交检查

建议在本地 Git hooks 或 alias 中配置以下快捷命令：

```bash
# 完整预提交检查
alias bio-check='ruff check awesome_bioinfo && mypy awesome_bioinfo && pytest tests/ -q && python -m awesome_bioinfo validate'
```
"""


def _make_en_cli_workflow() -> str:
    return """---
title: CLI Workflow Reference
---

# CLI Workflow Reference

## Overview

`python -m awesome_bioinfo` is the unified CLI entry point for this knowledge base, providing a complete toolchain from data validation, statistical queries, full-text search, and algorithm comparison to document generation. This page provides complete usage references, option descriptions, and typical examples for all subcommands.

---

## validate — Data Validation

Validate the integrity, consistency, and compliance of all YAML data files.

### Usage

```bash
python -m awesome_bioinfo validate [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--strict` | — | Treat warnings as errors | False |
| `--verbose` | -v | Output detailed validation logs | False |

### Examples

```bash
# Standard validation
python -m awesome_bioinfo validate

# Strict mode (any warning blocks)
python -m awesome_bioinfo validate --strict

# Verbose output
python -m awesome_bioinfo validate --verbose
```

---

## stats — Project Statistics

Output knowledge base scale statistics, field coverage, and category distribution.

### Usage

```bash
python -m awesome_bioinfo stats [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--format` | -f | Output format: table / json / csv | table |
| `--category` | -c | Filter by specified category | all |

### Examples

```bash
# Standard statistics table
python -m awesome_bioinfo stats

# JSON format output
python -m awesome_bioinfo stats -f json

# Single category statistics
python -m awesome_bioinfo stats -c sequence-alignment
```

---

## search — Full-Text Search

Search algorithms by name, description, or tags.

### Usage

```bash
python -m awesome_bioinfo search <query> [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--limit` | -n | Maximum number of results returned | 10 |
| `--field` | — | Search field: name / description / tag / all | all |
| `--lang` | -l | Output language: zh / en | zh |

### Examples

```bash
# Default search
python -m awesome_bioinfo search smith

# Limit result count
python -m awesome_bioinfo search "sequence alignment" -n 5

# Search tags only
python -m awesome_bioinfo search "dynamic-programming" --field tag
```

---

## info — Algorithm Details

View complete metadata for a single algorithm.

### Usage

```bash
python -m awesome_bioinfo info <algorithm-id> [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--format` | -f | Output format: table / json / yaml | table |
| `--lang` | -l | Output language: zh / en | zh |

### Examples

```bash
# View in table form
python -m awesome_bioinfo info smith-waterman

# JSON output
python -m awesome_bioinfo info needleman-wunsch -f json

# English output
python -m awesome_bioinfo info blast -l en
```

---

## compare — Algorithm Comparison

Side-by-side comparison of core metrics for two or more algorithms.

### Usage

```bash
python -m awesome_bioinfo compare <id1> <id2> [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--format` | -f | Output format: table / json | table |
| `--fields` | — | Specify comparison fields, comma-separated | all |

### Examples

```bash
# Default comparison
python -m awesome_bioinfo compare smith-waterman needleman-wunsch

# Compare only complexity and year
python -m awesome_bioinfo compare blast bwa --fields time_complexity,year

# JSON format
python -m awesome_bioinfo compare minimap2 bwa-mem -f json
```

---

## export — Data Export

Export algorithm data to JSON, CSV, or other formats.

### Usage

```bash
python -m awesome_bioinfo export [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--format` | -f | Output format: json / csv / yaml | json |
| `--output` | -o | Output file path | stdout |
| `--category` | -c | Filter by specified category | all |

### Examples

```bash
# Export all data as JSON
python -m awesome_bioinfo export -f json -o algorithms.json

# Export single category as CSV
python -m awesome_bioinfo export -f csv -c variant-calling -o variants.csv
```

---

## vitepress — Documentation Generation

Generate VitePress static site source (Chinese + English).

### Usage

```bash
python -m awesome_bioinfo vitepress [options]
```

### Options

| Option | Shorthand | Description | Default |
|--------|-----------|-------------|---------|
| `--clean` | — | Clean docs/zh and docs/en before generation | False |
| `--lang` | -l | Generate only specified language: zh / en / all | all |

### Examples

```bash
# Generate all documentation
python -m awesome_bioinfo vitepress

# Chinese only
python -m awesome_bioinfo vitepress -l zh

# Clean and regenerate
python -m awesome_bioinfo vitepress --clean
```

---

## Data Management Guide

### Adding a New Algorithm

1. Copy template: `cp templates/algorithm_template.yaml data/algorithms/<category>.yaml` (append to existing file or create new)
2. Fill in fields, ensuring `id` is globally unique and `description` is 50–500 characters
3. Run validation: `python -m awesome_bioinfo validate`
4. Generate docs: `python -m awesome_bioinfo vitepress`
5. Local preview: `cd docs && npm run dev`
6. Submit PR and wait for CI to pass

### Updating the Category System

1. Modify `data/categories.yaml`, adding or adjusting categories/subcategories
2. Synchronously update `category` / `subcategory` fields in all algorithm YAML files referencing that category
3. Run validation and generation commands to confirm zero errors
4. Since category changes are spec-level changes, they must go through the `/opsx:propose` proposal workflow

---

## VitePress Command Cheat Sheet

```bash
cd docs

# Local development preview
npm run dev

# Production build
npm run build

# Preview build artifacts
npm run preview
```

---

## CI/CD Integration Notes

### GitHub Actions Workflows

The following workflows are defined under `.github/workflows/`:

- **lint.yml**: ruff + mypy, triggered on every push
- **test.yml**: Full pytest suite + coverage reporting, triggered on PR and push
- **validate.yml**: `python -m awesome_bioinfo validate`, triggered when data files change
- **deploy.yml**: `vitepress generate` → `npm run build` → deploy to Pages, triggered on master branch push

### Local Pre-Commit Checks

It is recommended to configure the following shortcut command in local Git hooks or aliases:

```bash
# Complete pre-commit check
alias bio-check='ruff check awesome_bioinfo && mypy awesome_bioinfo && pytest tests/ -q && python -m awesome_bioinfo validate'
```
"""


# =====================
# File writing functions
# =====================

def _write_whitepaper_pages(
    docs_dir: Path,
    total_algorithms: int,
    total_categories: int,
    total_tags: int,
) -> None:
    zh_dir = docs_dir / "zh"
    en_dir = docs_dir / "en"

    write_file(
        zh_dir / "guides" / "project-overview.md",
        _generate_zh_project_overview(total_algorithms, total_categories, total_tags),
    )
    write_file(zh_dir / "academy" / "learning-path.md", _generate_zh_learning_path())
    write_file(
        zh_dir / "architecture" / "system-architecture.md",
        _generate_zh_system_architecture(),
    )
    write_file(
        zh_dir / "architecture" / "data-pipeline.md",
        _generate_zh_data_pipeline(),
    )
    write_file(
        zh_dir / "architecture" / "quality-assurance.md",
        _generate_zh_quality_assurance(),
    )
    write_file(zh_dir / "research" / "references.md", _generate_zh_references())
    write_file(zh_dir / "research" / "evolution.md", _generate_zh_evolution())
    write_file(zh_dir / "reference" / "cli-workflow.md", _generate_zh_cli_workflow())

    write_file(
        en_dir / "guides" / "project-overview.md",
        _generate_en_project_overview(total_algorithms, total_categories, total_tags),
    )
    write_file(en_dir / "academy" / "learning-path.md", _generate_en_learning_path())
    write_file(
        en_dir / "architecture" / "system-architecture.md",
        _generate_en_system_architecture(),
    )
    write_file(
        en_dir / "architecture" / "data-pipeline.md",
        _generate_en_data_pipeline(),
    )
    write_file(
        en_dir / "architecture" / "quality-assurance.md",
        _generate_en_quality_assurance(),
    )
    write_file(en_dir / "research" / "references.md", _generate_en_references())
    write_file(en_dir / "research" / "evolution.md", _generate_en_evolution())
    write_file(en_dir / "reference" / "cli-workflow.md", _generate_en_cli_workflow())


def write_all_pages(
    docs_dir: Path,
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> None:
    """Write all pages to docs/zh/ and docs/en/ directories."""
    zh_dir = docs_dir / "zh"
    en_dir = docs_dir / "en"

    write_file(
        zh_dir / "index.md",
        generate_zh_index(categories, algorithms, cat_map, by_cat, by_tag),
    )
    write_file(zh_dir / "algorithms" / "index.md", generate_zh_algo_index(algorithms, cat_map))
    write_file(zh_dir / "categories" / "index.md", generate_zh_category_index(categories, by_cat))
    write_file(zh_dir / "tags.md", generate_zh_tags_page(by_tag))

    for algo in algorithms:
        write_file(zh_dir / "algorithms" / f"{algo.id}.md", generate_zh_algo_page(algo, cat_map))

    for cat in categories:
        algos = by_cat.get(cat.id, [])
        if algos:
            write_file(
                zh_dir / "categories" / cat.id / "index.md",
                generate_zh_category_page(cat, algos, cat_map),
            )

    write_file(
        en_dir / "index.md",
        generate_en_index(categories, algorithms, cat_map, by_cat, by_tag),
    )
    write_file(en_dir / "algorithms" / "index.md", generate_en_algo_index(algorithms, cat_map))
    write_file(en_dir / "categories" / "index.md", generate_en_category_index(categories, by_cat))
    write_file(en_dir / "tags.md", generate_en_tags_page(by_tag))

    for algo in algorithms:
        write_file(en_dir / "algorithms" / f"{algo.id}.md", generate_en_algo_page(algo, cat_map))

    for cat in categories:
        algos = by_cat.get(cat.id, [])
        if algos:
            write_file(
                en_dir / "categories" / cat.id / "index.md",
                generate_en_category_page(cat, algos, cat_map),
            )

    _write_whitepaper_pages(docs_dir, len(algorithms), len(categories), len(by_tag))


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
    print(f"  Generated {len([c for c in categories if by_cat.get(c.id)])} category pages (x2 languages)")
    print("  Generated index, tags, and whitepaper academy pages (x2 languages)")
    print("\nDone! Run 'cd docs && npm run dev' to preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
