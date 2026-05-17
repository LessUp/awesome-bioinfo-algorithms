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


def _generate_zh_project_overview(total: int, categories: int, tags: int) -> str:
    return f"""---
title: 项目导读
---

# 项目导读

本项目定位为**生物信息学算法技术白皮书与架构展示站**，同时承担算法知识库与工程实践指南角色。

## 核心定位

- 面向严苛技术面试与高级开发者评审场景
- 强调“算法知识组织 + 工程化生成链路 + 可验证质量体系”
- 提供可追溯的数据源、生成流程与发布流程

## 当前规模

| 指标 | 数值 |
|---|---|
| 算法条目 | {total} |
| 顶级分类 | {categories} |
| 标签总数 | {tags} |

## 建议阅读路径

1. [学院路径](/zh/academy/learning-path)
2. [系统架构](/zh/architecture/system-architecture)
3. [数据与生成链路](/zh/architecture/data-pipeline)
4. [质量保障](/zh/architecture/quality-assurance)
5. [参考文献与竞品研究](/zh/research/references)
"""


def _generate_en_project_overview(total: int, categories: int, tags: int) -> str:
    return f"""---
title: Project Overview
---

# Project Overview

This project is positioned as a **technical whitepaper and architecture showcase** for bioinformatics
algorithms, with a parallel role as a practical knowledge academy.

## Core Positioning

- Designed for rigorous interview and senior engineering review contexts
- Combines algorithm curation, generation pipelines, and verifiable quality controls
- Keeps source data, generation flow, and publishing flow transparent

## Current Scale

| Metric | Value |
|---|---|
| Algorithms | {total} |
| Top-level Categories | {categories} |
| Tags | {tags} |

## Recommended Reading Path

1. [Learning Path](/en/academy/learning-path)
2. [System Architecture](/en/architecture/system-architecture)
3. [Data and Generation Pipeline](/en/architecture/data-pipeline)
4. [Quality Assurance](/en/architecture/quality-assurance)
5. [References and Ecosystem Study](/en/research/references)
"""


def _generate_zh_learning_path() -> str:
    return """---
title: 学院路径
---

# 学院路径

## Level 1: 导航理解

- 理解分类体系与标签体系
- 通过算法总览快速建立领域地图

## Level 2: 算法评估能力

- 从用途、复杂度、难度、实现语言评估选型
- 结合标签交叉检索同类方案

## Level 3: 架构与工程能力

- 理解数据源、生成器、VitePress 发布链路
- 通过 CLI 工作流维护数据一致性与文档质量
"""


def _generate_en_learning_path() -> str:
    return """---
title: Learning Path
---

# Learning Path

## Level 1: Navigation Literacy

- Understand category and tag taxonomies
- Build a domain map from algorithm index pages

## Level 2: Algorithm Evaluation

- Evaluate choices through purpose, complexity, difficulty, and implementation language
- Cross-check alternatives via tag intersections

## Level 3: Architecture and Engineering

- Understand source data, generator internals, and VitePress publishing flow
- Maintain consistency and quality through the CLI workflow
"""


def _generate_zh_system_architecture() -> str:
    return """---
title: 系统架构
---

# 系统架构

```mermaid
flowchart LR
    A[data/categories.yaml + data/algorithms/*.yaml] --> B[DataStore]
    B --> C[Validation]
    C --> D[generate_docs.py]
    D --> E[docs/zh + docs/en]
    E --> F[VitePress Build]
    F --> G[GitHub Pages]
```

本架构采用“数据源单一真相 + 生成驱动文档”的模式，降低手工维护成本并提升一致性。
"""


def _generate_en_system_architecture() -> str:
    return """---
title: System Architecture
---

# System Architecture

```mermaid
flowchart LR
    A[data/categories.yaml + data/algorithms/*.yaml] --> B[DataStore]
    B --> C[Validation]
    C --> D[generate_docs.py]
    D --> E[docs/zh + docs/en]
    E --> F[VitePress Build]
    F --> G[GitHub Pages]
```

The architecture follows a single-source-of-truth data model with generation-driven docs publishing.
"""


def _generate_zh_data_pipeline() -> str:
    return """---
title: 数据与生成链路
---

# 数据与生成链路

## 输入层

- `data/categories.yaml` 维护分类与层级
- `data/algorithms/*.yaml` 维护算法条目

## 处理层

- `DataStore` 加载并索引数据
- `validate` 负责规则校验
- `generate_docs.py` 生成 VitePress 页面

## 输出层

- `docs/zh/**`, `docs/en/**` 作为站点源码
- GitHub Actions 构建并发布到 Pages
"""


def _generate_en_data_pipeline() -> str:
    return """---
title: Data and Generation Pipeline
---

# Data and Generation Pipeline

## Input Layer

- `data/categories.yaml` defines category hierarchy
- `data/algorithms/*.yaml` stores algorithm entries

## Processing Layer

- `DataStore` loads and indexes data
- `validate` enforces schema and quality rules
- `generate_docs.py` produces VitePress content

## Output Layer

- `docs/zh/**`, `docs/en/**` become site sources
- GitHub Actions builds and deploys to Pages
"""


def _generate_zh_quality_assurance() -> str:
    return """---
title: 质量保障
---

# 质量保障

质量体系覆盖三层：

1. 数据层校验：`python -m awesome_bioinfo validate`
2. 代码层质量：`ruff` + `mypy` + `pytest`
3. 文档层验证：VitePress 构建与页面导航一致性检查
"""


def _generate_en_quality_assurance() -> str:
    return """---
title: Quality Assurance
---

# Quality Assurance

The quality strategy is enforced across three layers:

1. Data validation: `python -m awesome_bioinfo validate`
2. Code quality: `ruff` + `mypy` + `pytest`
3. Documentation verification: VitePress build and navigation consistency checks
"""


def _generate_zh_references() -> str:
    return """---
title: 参考文献与相关项目
---

# 参考文献与相关项目

## 经典论文

- Smith T.F., Waterman M.S. (1981). Identification of common molecular subsequences.
- Needleman S.B., Wunsch C.D. (1970). A general method applicable to the search for similarities.

## 相关开源项目探究

- [bioinformatics-workflows](https://github.com/topics/bioinformatics)
- [awesome-bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics)

## 技术启发

- 数据单一真相有助于维持大型知识库一致性
- 生成驱动文档可降低维护成本与链接漂移
"""


def _generate_en_references() -> str:
    return """---
title: References and Related Projects
---

# References and Related Projects

## Foundational Papers

- Smith T.F., Waterman M.S. (1981). Identification of common molecular subsequences.
- Needleman S.B., Wunsch C.D. (1970). A general method applicable to the search for similarities.

## Related Open Source Ecosystem

- [bioinformatics-workflows](https://github.com/topics/bioinformatics)
- [awesome-bioinformatics](https://github.com/danielecook/Awesome-Bioinformatics)

## Engineering Insights

- Single-source data models keep large knowledge systems coherent
- Generation-driven docs reduce maintenance burden and link drift
"""


def _generate_zh_evolution() -> str:
    return """---
title: 演进思考
---

# 演进思考

## 阶段一：列表化收录

重点解决“收录广度”问题，建立多分类算法目录。

## 阶段二：工程化治理

引入校验、生成、测试和 CI，解决一致性与可维护性问题。

## 阶段三：白皮书化表达

以架构叙事、研究引用、学院路径提升项目专业说服力。
"""


def _generate_en_evolution() -> str:
    return """---
title: Evolution Notes
---

# Evolution Notes

## Phase 1: List-Oriented Curation

Focused on breadth, creating a multi-category algorithm index.

## Phase 2: Engineering Governance

Added validation, generation, testing, and CI to improve consistency and maintainability.

## Phase 3: Whitepaper Positioning

Introduced architecture narratives, research references, and academy-style guidance for expert readers.
"""


def _generate_zh_cli_workflow() -> str:
    return """---
title: CLI 工作流参考
---

# CLI 工作流参考

```bash
python -m awesome_bioinfo validate
python -m awesome_bioinfo stats
python -m awesome_bioinfo search smith
python -m awesome_bioinfo info smith-waterman
python -m awesome_bioinfo compare smith-waterman needleman-wunsch
python -m awesome_bioinfo vitepress
```
"""


def _generate_en_cli_workflow() -> str:
    return """---
title: CLI Workflow Reference
---

# CLI Workflow Reference

```bash
python -m awesome_bioinfo validate
python -m awesome_bioinfo stats
python -m awesome_bioinfo search smith
python -m awesome_bioinfo info smith-waterman
python -m awesome_bioinfo compare smith-waterman needleman-wunsch
python -m awesome_bioinfo vitepress
```
"""


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

    for algo in algorithms:
        all_tags.update(algo.tags)

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
  tagline: 技术白皮书 / 架构展示站 / 项目学院
  actions:
    - theme: brand
      text: 阅读导读
      link: /zh/guides/project-overview
    - theme: alt
      text: 算法总览
      link: /zh/algorithms/
features:
  - icon: 🧬
    title: {total}+ 算法
    details: 可追溯的数据驱动算法图谱
  - icon: 🏛️
    title: 技术白皮书
    details: 面向严苛面试与架构评审的叙事结构
  - icon: 🧪
    title: 可验证工程链路
    details: 从校验、生成到发布的完整流程
---

## 技术白皮书入口

- [项目导读](/zh/guides/project-overview)
- [学院路径](/zh/academy/learning-path)
- [系统架构](/zh/architecture/system-architecture)
- [数据与生成链路](/zh/architecture/data-pipeline)
- [质量保障](/zh/architecture/quality-assurance)
- [参考文献与相关项目](/zh/research/references)
- [演进思考](/zh/research/evolution)

## 研究方向

{chr(10).join(cat_cards)}

## 最新收录

{chr(10).join(algo_list)}

[查看全部算法 →](/zh/algorithms/)
"""


def generate_zh_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    """Generate Chinese algorithm detail page."""
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

    links = []
    if algo.paper_url:
        links.append(f"- [📄 论文链接]({algo.paper_url})")
    if algo.implementation_url:
        links.append(f"- [💻 代码实现]({algo.implementation_url})")
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


def generate_zh_algo_index(algorithms: list[AlgorithmEntry], cat_map: dict[str, Category]) -> str:
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

        lines.append("| 算法 | 年份 | 用途 |")
        lines.append("|------|------|------|")
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
        lines.append(f"- **[{cat.name}]({cat.id}/)** — {trim_text(cat.description, 60)} ({count} 个算法)")

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


def generate_en_index(
    categories: list[Category],
    algorithms: list[AlgorithmEntry],
    cat_map: dict[str, Category],
    by_cat: dict[str, list[AlgorithmEntry]],
    by_tag: dict[str, list[AlgorithmEntry]],
) -> str:
    """Generate English landing page."""
    _ = cat_map
    total = len(algorithms)
    all_tags: set[str] = set()

    for algo in algorithms:
        all_tags.update(algo.tags)

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
  tagline: Technical Whitepaper / Architecture Showcase / Project Academy
  actions:
    - theme: brand
      text: Start with Overview
      link: /en/guides/project-overview
    - theme: alt
      text: Browse Algorithms
      link: /en/algorithms/
features:
  - icon: 🧬
    title: {total}+ Algorithms
    details: Data-driven algorithm atlas with traceable metadata
  - icon: 🏛️
    title: Technical Whitepaper
    details: Architecture-oriented narrative for expert reviewers
  - icon: 🧪
    title: Verifiable Engineering
    details: Validation, generation, and deployment as one chain
---

## Technical Whitepaper Entry

- [Project Overview](/en/guides/project-overview)
- [Learning Path](/en/academy/learning-path)
- [System Architecture](/en/architecture/system-architecture)
- [Data and Generation Pipeline](/en/architecture/data-pipeline)
- [Quality Assurance](/en/architecture/quality-assurance)
- [References and Related Projects](/en/research/references)
- [Evolution Notes](/en/research/evolution)

## Categories

{chr(10).join(cat_cards)}

## Latest Additions

{chr(10).join(algo_list)}

[View All Algorithms →](/en/algorithms/)
"""


def generate_en_algo_page(algo: AlgorithmEntry, cat_map: dict[str, Category]) -> str:
    """Generate English algorithm detail page."""
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


def generate_en_algo_index(algorithms: list[AlgorithmEntry], cat_map: dict[str, Category]) -> str:
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
