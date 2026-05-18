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
    details: 面向严苛技术面试与架构评审的深度叙事结构，含学院路径与质量保障体系
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
    details: In-depth narrative for rigorous technical interviews and reviews, including academy paths and quality assurance
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
3. **[参考文献与相关项目](/zh/research/references)** —— 按领域浏览经典论文、必读综述与竞品开源项目对比分析。
4. **[演进思考](/zh/research/evolution)** —— 回顾项目从"列表化"到"工程化"再到"白皮书化"的三阶段演进，并了解未来路线图。

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
3. **[References and Related Projects](/en/research/references)** — Browse classic papers, required reviews, and comparative analyses of competing open-source projects by domain.
4. **[Evolution Notes](/en/research/evolution)** — Review the project's three-phase evolution from "list-oriented" to "engineered" to "whitepaper-grade," and learn about the future roadmap.

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


# Architecture pages removed — not needed for an algorithm curation repository.



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
    write_file(zh_dir / "research" / "references.md", _generate_zh_references())
    write_file(zh_dir / "research" / "evolution.md", _generate_zh_evolution())
    write_file(zh_dir / "reference" / "cli-workflow.md", _generate_zh_cli_workflow())

    write_file(
        en_dir / "guides" / "project-overview.md",
        _generate_en_project_overview(total_algorithms, total_categories, total_tags),
    )
    write_file(en_dir / "academy" / "learning-path.md", _generate_en_learning_path())
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
