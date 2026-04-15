"""
README Generator for Awesome Bioinformatics Algorithms.
Generates formatted README.md from algorithm data.
"""

import os
import re

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .schema import DIFFICULTY_LABELS, AlgorithmEntry, Category


class ReadmeGenerator:
    """Generates README.md from algorithm registry and categories."""

    def __init__(
        self,
        registry: AlgorithmRegistry,
        category_manager: CategoryManager,
        template_path: str = "templates/readme_template.md",
    ):
        self._registry = registry
        self._category_manager = category_manager
        self._template_path = template_path

    def generate(self) -> str:
        """
        Generate the complete README content.

        Returns:
            Complete README markdown string
        """
        template = self._load_template()

        stats = self._registry.get_statistics()
        toc = self.generate_toc()
        content = self._generate_content()

        readme = template.replace("{{ total_algorithms }}", str(stats.total_algorithms))
        readme = readme.replace("{{ total_categories }}", str(stats.total_categories))
        readme = readme.replace("{{ total_tags }}", str(stats.total_tags))
        readme = readme.replace("{{ toc }}", toc)
        readme = readme.replace("{{ content }}", content)

        return readme

    def _load_template(self) -> str:
        """Load the README template file."""
        if os.path.exists(self._template_path):
            with open(self._template_path, encoding="utf-8") as f:
                return f.read()
        return self._default_template()

    def _default_template(self) -> str:
        """Return default template if file not found."""
        return """# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 生物信息学算法概要汇总

## 统计

- 📊 算法总数: {{ total_algorithms }}
- 📁 有算法的分类数: {{ total_categories }}
- 🏷️ 标签数量: {{ total_tags }}

## 目录

{{ toc }}

---

{{ content }}

## 贡献

欢迎贡献！请阅读 [贡献指南](CONTRIBUTING.md)。

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
"""

    def generate_toc(self) -> str:
        """
        Generate table of contents with anchor links.

        Returns:
            Markdown formatted table of contents
        """
        toc_lines = []
        categories = self._category_manager.list_all_categories()

        for category in categories:
            algos = self._registry.get_by_category(category.id)
            if algos:  # Only include categories with algorithms
                title = f"{category.name} ({category.name_en})"
                anchor = self._generate_anchor(title)
                toc_lines.append(f"- [{title}](#{anchor})")

                # Add subcategories
                for sub in category.subcategories:
                    sub_algos = self._get_subcategory_algorithms(category.id, sub.id)
                    if sub_algos:
                        sub_title = f"{sub.name} ({sub.name_en})"
                        sub_anchor = self._generate_anchor(sub_title)
                        toc_lines.append(f"  - [{sub_title}](#{sub_anchor})")

        return "\n".join(toc_lines)

    @staticmethod
    def _generate_anchor(text: str) -> str:
        """Generate a valid Markdown anchor from text."""
        anchor = text.lower()
        anchor = anchor.replace(" ", "-")
        anchor = re.sub(r"[^\w\u4e00-\u9fff-]", "", anchor)
        anchor = re.sub(r"-+", "-", anchor)
        anchor = anchor.strip("-")
        return anchor

    def generate_category_section(self, category: Category) -> str:
        """
        Generate markdown section for a category.

        Args:
            category: The category to generate section for

        Returns:
            Markdown formatted category section
        """
        lines = []
        direct_algos = self._registry.get_direct_by_category(category.id)
        has_subcategory_content = any(
            self._get_subcategory_algorithms(category.id, sub.id) for sub in category.subcategories
        )

        if direct_algos or has_subcategory_content:
            lines.append(f"## {category.name} ({category.name_en})")
            if category.description:
                lines.append(f"\n{category.description}\n")

            for algo in direct_algos:
                lines.append(self.generate_algorithm_entry(algo))

        # Generate subcategory sections
        for sub in category.subcategories:
            sub_algos = self._get_subcategory_algorithms(category.id, sub.id)
            if sub_algos:
                lines.append(f"\n### {sub.name} ({sub.name_en})")
                if sub.description:
                    lines.append(f"\n{sub.description}\n")

                for algo in sub_algos:
                    lines.append(self.generate_algorithm_entry(algo))

        return "\n".join(lines)

    def generate_algorithm_entry(self, algo: AlgorithmEntry) -> str:
        """
        Generate markdown for a single algorithm entry.

        Args:
            algo: The algorithm entry to format

        Returns:
            Markdown formatted algorithm entry
        """
        lines = []

        # Algorithm name as header (with year if available)
        if algo.year:
            lines.append(f"\n#### {algo.name} ({algo.year})")
        else:
            lines.append(f"\n#### {algo.name}")
        lines.append("")

        # Description
        lines.append(algo.description.strip())
        lines.append("")

        # Purpose
        lines.append(f"**用途**: {algo.purpose}")

        # Complexity
        lines.append(f"**时间复杂度**: {algo.time_complexity}")
        if algo.space_complexity:
            lines.append(f"**空间复杂度**: {algo.space_complexity}")

        # Links
        if algo.paper_url:
            lines.append(f"**论文**: [{algo.paper_url}]({algo.paper_url})")
        if algo.implementation_url:
            lines.append(f"**实现**: [{algo.implementation_url}]({algo.implementation_url})")

        # Related tools
        if algo.related_tools:
            tools = ", ".join(algo.related_tools)
            lines.append(f"**相关工具**: {tools}")

        # Tags
        if algo.tags:
            tags = " ".join([f"`{tag}`" for tag in algo.tags])
            lines.append(f"**标签**: {tags}")

        # Difficulty
        if algo.difficulty:
            label = DIFFICULTY_LABELS.get(algo.difficulty, algo.difficulty)
            lines.append(f"**难度**: {label}")

        # Implementation languages
        if algo.language:
            langs = ", ".join(algo.language)
            lines.append(f"**实现语言**: {langs}")

        # Extended references
        if algo.references:
            lines.append("**扩展资料**:")
            for ref in algo.references:
                title = ref.title or ref.url
                ref_type = f" [{ref.type}]" if ref.type else ""
                lines.append(f"  - [{title}]({ref.url}){ref_type}")

        lines.append("")
        return "\n".join(lines)

    def _get_subcategory_algorithms(
        self, category_id: str, subcategory_id: str
    ) -> list[AlgorithmEntry]:
        """Return algorithms that match both the parent category and subcategory."""
        return [
            algo
            for algo in self._registry.get_by_subcategory(subcategory_id)
            if algo.category == category_id
        ]

    def generate_statistics(self) -> str:
        """
        Generate statistics section.

        Returns:
            Markdown formatted statistics
        """
        stats = self._registry.get_statistics()
        lines = [
            f"- 📊 算法总数: {stats.total_algorithms}",
            f"- 📁 有算法的分类数: {stats.total_categories}",
            f"- 🏷️ 标签数量: {stats.total_tags}",
        ]
        return "\n".join(lines)

    def _generate_content(self) -> str:
        """Generate all category sections."""
        sections = []
        categories = self._category_manager.list_all_categories()

        for category in categories:
            section = self.generate_category_section(category)
            if section.strip():
                sections.append(section)

        return "\n\n".join(sections)

    def save(self, output_path: str = "README.md"):
        """
        Generate and save README to file.

        Args:
            output_path: Path to save the README file
        """
        content = self.generate()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
