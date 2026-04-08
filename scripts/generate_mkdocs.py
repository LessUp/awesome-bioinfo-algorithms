#!/usr/bin/env python3
"""
Generate MkDocs documentation from algorithm YAML data.

Usage:
    python scripts/generate_mkdocs.py
"""

from collections import Counter
from pathlib import Path

import yaml

DOC_SOURCE_FILES = {
    "api.md": "API.md",
    "faq.md": "FAQ.md",
    "development.md": "DEVELOPMENT.md",
    "contributing.md": "contributing.md",
    "security.md": "security.md",
}

DOC_STATIC_FILES = {
    "changelog.md": "CHANGELOG.md",
    "code-of-conduct.md": "CODE_OF_CONDUCT.md",
    "security-policy.md": "SECURITY.md",
}


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


def read_text(path: Path) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def strip_front_matter(content: str) -> str:
    if not content.startswith("---\n"):
        return content

    closing = content.find("\n---\n", 4)
    if closing == -1:
        return content

    return content[closing + 5 :]


def prepare_docs_content(content: str) -> str:
    return strip_front_matter(content).replace("../CONTRIBUTING.md", "contributing.md")


def copy_docs_pages(base_dir: Path, mkdocs_dir: Path):
    docs_dir = base_dir / "docs"
    for target_name, source_name in DOC_SOURCE_FILES.items():
        content = prepare_docs_content(read_text(docs_dir / source_name))
        write_file(mkdocs_dir / target_name, content)

    for target_name, source_name in DOC_STATIC_FILES.items():
        content = read_text(base_dir / source_name)
        write_file(mkdocs_dir / target_name, content)


def generate_index(
    categories: list[dict], algorithms: list[dict], cat_map: dict, by_cat: dict
) -> str:
    """Generate home page."""
    total = len(algorithms)
    cats_with_algo = len(by_cat)
    all_tags = set()
    difficulty_counts: Counter[str] = Counter()
    language_counts: Counter[str] = Counter()
    with_paper = 0
    with_implementation = 0
    with_tools = 0

    def trim_text(value: str, limit: int = 84) -> str:
        normalized = " ".join(value.split())
        if len(normalized) <= limit:
            return normalized
        return normalized[: limit - 1].rstrip() + "…"

    for algorithm in algorithms:
        all_tags.update(algorithm.get("tags", []))
        difficulty_counts[algorithm.get("difficulty", "unspecified")] += 1
        language_counts.update(algorithm.get("language", []))
        if algorithm.get("paper_url"):
            with_paper += 1
        if algorithm.get("implementation_url"):
            with_implementation += 1
        if algorithm.get("related_tools"):
            with_tools += 1

    top_categories = sorted(
        (
            (len(by_cat.get(cat["id"], [])), cat)
            for cat in categories
            if len(by_cat.get(cat["id"], [])) > 0
        ),
        key=lambda item: (-item[0], item[1].get("name_en", "")),
    )[:8]
    latest_algorithms = sorted(
        [algorithm for algorithm in algorithms if algorithm.get("year")],
        key=lambda entry: (entry.get("year", 0), entry.get("name", "")),
        reverse=True,
    )[:6]
    top_languages = ", ".join(
        f"{language} {count}" for language, count in language_counts.most_common(4)
    )
    difficulty_summary = " / ".join(
        f"{label} {difficulty_counts[key]}"
        for key, label in [
            ("beginner", "入门"),
            ("intermediate", "进阶"),
            ("advanced", "高级"),
            ("unspecified", "未标注"),
        ]
        if difficulty_counts.get(key)
    )

    lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        "# Awesome Bioinformatics Algorithms",
        "",
        "> 把仓库中最有价值的部分——结构化算法条目、分类体系、标签索引、论文与实现链接——组织成适合网页浏览的知识入口。",
        "",
        "这个站点不再把 GitHub Pages 当作一张窄版 README 镜像，而是专门承担 **导航、检索、发现与快速浏览** 的角色；仓库本身仍然是权威数据源和贡献入口。",
        "",
        "[浏览全部算法](algorithms/){ .md-button .md-button--primary }",
        "[按分类浏览](categories/){ .md-button }",
        "[按标签筛选](tags/){ .md-button }",
        "[查看 GitHub 仓库](https://github.com/LessUp/awesome-bioinfo-algorithms){ .md-button }",
        "",
        '<div class="aba-stats-grid">',
        f'<div class="aba-stat-card"><span>算法条目</span><strong>{total}</strong><p>覆盖经典方法到 2024 年前沿模型。</p></div>',
        f'<div class="aba-stat-card"><span>有效分类</span><strong>{cats_with_algo}</strong><p>按研究任务组织，适合从问题域进入。</p></div>',
        f'<div class="aba-stat-card"><span>标签索引</span><strong>{len(all_tags)}</strong><p>可从技术关键词与方法特征快速聚合。</p></div>',
        f'<div class="aba-stat-card"><span>实现入口</span><strong>{with_implementation}</strong><p>大部分算法都提供了工具或代码链接。</p></div>',
        "</div>",
        "",
        "## 这个站点能提供什么价值",
        "",
        '<div class="aba-card-grid">',
        '<div class="aba-value-card"><h3>结构化数据而不是散乱链接</h3><p>每个算法条目都尽量统一整理了描述、用途、时间复杂度、空间复杂度、论文、实现与标签，适合横向比较。</p></div>',
        '<div class="aba-value-card"><h3>从研究任务快速进入</h3><p>分类页按生物信息学问题域组织内容，避免在长文档里盲目滚动查找。</p></div>',
        '<div class="aba-value-card"><h3>支持发现而不只是查找</h3><p>标签索引、全量算法页和最新方向快照让你更容易发现相近方法、替代工具和新趋势。</p></div>',
        '<div class="aba-value-card"><h3>仓库与页面各司其职</h3><p>GitHub 仓库负责维护、协作与数据源；Pages 负责展示、导航与检索，不再重复堆叠 README 内容。</p></div>',
        "</div>",
        "",
        "## 按研究方向快速进入",
        "",
        '<div class="aba-category-grid">',
    ]
    for count, cat in top_categories:
        lines.append(
            f'<a class="aba-category-card" href="categories/{cat["id"]}/">'
            f'<span>{cat["name"]}</span>'
            f'<strong>{cat["name_en"]}</strong>'
            f'<p>{trim_text(cat.get("description", ""))}</p>'
            f'<em>{count} 个算法</em></a>'
        )
    lines += [
        "</div>",
        "",
        "## 数据覆盖情况",
        "",
        f"- 论文链接：**{with_paper}/{total}**",
        f"- 实现入口：**{with_implementation}/{total}**",
        f"- 相关工具：**{with_tools}/{total}**",
        f"- 难度分布：**{difficulty_summary}**",
        f"- 常见实现语言：**{top_languages or '未标注'}**",
        "",
        "## 近期方向快照",
        "",
        '<div class="aba-latest-grid">',
    ]
    for algorithm in latest_algorithms:
        category = cat_map.get(algorithm.get("category", ""), {})
        summary = algorithm.get("purpose") or algorithm.get("description", "")
        lines.append(
            f'<a class="aba-latest-card" href="algorithms/{algorithm["id"]}/">'
            f'<span>{algorithm["year"]} · {category.get("name", algorithm.get("category", ""))}</span>'
            f'<strong>{algorithm["name"]}</strong>'
            f'<p>{trim_text(summary)}</p>'
            "<em>查看条目</em></a>"
        )
    lines += [
        "</div>",
        "",
        "## 建议的使用方式",
        "",
        "- 想先建立全局认知：从 [分类总览](categories/) 开始",
        "- 想做技术路线筛选：先看 [标签索引](tags/)",
        "- 想直接检索名称、用途或关键词：使用顶部搜索框，或参考 [检索页](search/)",
        "- 想贡献或修订条目：前往 [贡献指南](contributing/) 与 [开发文档](development/)",
        "",
    ]
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
        lines.append(" ".join(f"`{tag}`" for tag in algo["tags"]))
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
        sub_algos = [algo for algo in algos if algo.get("subcategory") == sub["id"]]
        if sub_algos:
            lines.append(f"## {sub['name']} ({sub.get('name_en', '')})")
            lines.append("")
            if sub.get("description"):
                lines.append(sub["description"])
                lines.append("")
            for algo in sub_algos:
                year = f" ({algo['year']})" if algo.get("year") else ""
                diff = f" [{algo['difficulty']}]" if algo.get("difficulty") else ""
                lines.append(f"- [{algo['name']}{year}](../algorithms/{algo['id']}.md){diff}")
                if algo.get("purpose"):
                    lines.append(f"  {algo['purpose']}")
            lines.append("")

    direct = [algo for algo in algos if not algo.get("subcategory")]
    if direct:
        lines.append("## Other")
        lines.append("")
        for algo in direct:
            year = f" ({algo['year']})" if algo.get("year") else ""
            lines.append(f"- [{algo['name']}{year}](../algorithms/{algo['id']}.md)")
        lines.append("")

    return "\n".join(lines)


def generate_tags_page(by_tag: dict) -> str:
    """Generate tags index page."""
    lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        "# 标签索引",
        "",
        f"当前共整理 **{len(by_tag)}** 个标签。若你知道方法特征但暂时想不起算法名，可以先从这里进入，再回到具体算法页。",
        "",
    ]
    for tag in sorted(by_tag.keys()):
        algos = by_tag[tag]
        lines.append(f"## `{tag}` ({len(algos)})")
        lines.append("")
        for algo in algos:
            year = f" ({algo['year']})" if algo.get("year") else ""
            lines.append(f"- [{algo['name']}{year}](algorithms/{algo['id']}.md)")
        lines.append("")
    return "\n".join(lines)


def generate_search_page() -> str:
    """Generate static search help page."""
    return """\
---
hide:
  - toc
---

# 检索与筛选

这个站点最适合承担“快速定位与发现”的角色。若你不想在 README 或仓库目录里长时间滚动，建议优先使用下面三种入口。

## 站内全文搜索

顶部搜索框可以直接匹配：

- 算法名称
- 条目描述与用途
- 标签关键词
- 分类页与项目文档

## 推荐浏览路径

- 想按研究任务浏览：从 [分类总览](categories/) 进入
- 想按技术特征筛选：从 [标签索引](tags/) 进入
- 想扫描全部条目：从 [全部算法](algorithms/) 进入
- 想回到权威数据源和贡献入口：访问 [GitHub 仓库](https://github.com/LessUp/awesome-bioinfo-algorithms)

## 命令行检索

你也可以在本地仓库中直接搜索：

```bash
python -m scripts search "dynamic programming"
python -m scripts search --tag fast
python -m scripts search --category sequence-alignment
python -m scripts search --difficulty beginner
```
"""


def generate_about_page() -> str:
    return """\
---
hide:
  - toc
---

# 关于项目

**Awesome Bioinformatics Algorithms** 是一个面向生物信息学算法的结构化知识仓库。GitHub 仓库负责维护、协作和数据更新，Pages 站点负责展示、导航与检索。

## 仓库里最有价值的资产

- `data/algorithms/*.yaml`：算法主数据，统一整理描述、用途、复杂度、论文、实现与标签
- `data/categories.yaml`：分类体系与子分类定义
- `scripts/`：用于校验、搜索、导出、README 生成与 MkDocs 生成的维护工具
- 自动生成的 README 与站点页面：减少内容漂移，保证仓库与网页的一致性

## 适合谁使用

- 想快速比较同类算法的研究者和工程师
- 想按问题域梳理方法谱系的学习者
- 想补充论文、实现链接或元数据的贡献者

## 工作方式

- 数据以 YAML 维护，便于审阅、批量处理和自动校验
- README 与网页文档自动生成，降低手工维护成本
- CLI 支持验证、搜索、统计和导出，方便本地维护与集成

## 相关链接

- [GitHub Repository](https://github.com/LessUp/awesome-bioinfo-algorithms)
- [Contributing Guide](contributing/)
- [Development Guide](development/)
- [Changelog](changelog/)
"""


def write_generated_pages(
    base_dir: Path,
    mkdocs_dir: Path,
    categories: list[dict],
    algorithms: list[dict],
    cat_map: dict[str, dict],
    by_cat: dict[str, list[dict]],
    by_tag: dict[str, list[dict]],
):
    write_file(mkdocs_dir / "index.md", generate_index(categories, algorithms, cat_map, by_cat))

    for algo in algorithms:
        write_file(
            mkdocs_dir / "algorithms" / f"{algo['id']}.md",
            generate_algo_page(algo, cat_map),
        )

    for cat in categories:
        algos = by_cat.get(cat["id"], [])
        if algos:
            write_file(
                mkdocs_dir / "categories" / f"{cat['id']}.md",
                generate_category_page(cat, algos, cat_map),
            )

    cat_index_lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        "# 分类总览",
        "",
        f"当前共有 **{len([cat for cat in categories if by_cat.get(cat['id'])])}** 个已收录分类，建议先从与你的问题域最接近的方向进入。",
        "",
    ]
    for cat in categories:
        count = len(by_cat.get(cat["id"], []))
        if count:
            cat_index_lines.append(
                f"- [{cat['name']} ({cat['name_en']})]({cat['id']}.md) — {count} 个算法"
            )
    write_file(mkdocs_dir / "categories" / "index.md", "\n".join(cat_index_lines) + "\n")

    algo_index_lines = [
        "---",
        "hide:",
        "  - toc",
        "---",
        "",
        "# 全部算法",
        "",
        f"当前共收录 **{len(algorithms)}** 个算法，下面按名称排序。若你想先缩小范围，建议先看分类页或标签页。",
        "",
    ]
    for algo in sorted(algorithms, key=lambda entry: entry.get("name", "")):
        year = f" ({algo['year']})" if algo.get("year") else ""
        algo_index_lines.append(f"- [{algo['name']}{year}]({algo['id']}.md)")
    write_file(mkdocs_dir / "algorithms" / "index.md", "\n".join(algo_index_lines) + "\n")

    write_file(mkdocs_dir / "tags.md", generate_tags_page(by_tag))
    write_file(mkdocs_dir / "search.md", generate_search_page())
    write_file(mkdocs_dir / "about.md", generate_about_page())
    copy_docs_pages(base_dir, mkdocs_dir)


def main(base_dir: Path | None = None) -> int:
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
    print(f"  Generated {len([cat for cat in categories if by_cat.get(cat['id'])])} category pages")
    print("  Generated tags, search, about, and documentation pages")
    print("\nDone! Run 'mkdocs serve -f mkdocs/mkdocs.yml' to preview.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
