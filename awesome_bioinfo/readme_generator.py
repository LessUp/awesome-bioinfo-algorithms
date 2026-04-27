"""
README Generator for Awesome Bioinformatics Algorithms.
Generates formatted README.md from algorithm data.
"""

import os
import re

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .schema import DIFFICULTY_LABELS_BILINGUAL, AlgorithmEntry, Category


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
        category_overview = self._generate_category_overview()
        featured_content = self._generate_featured_content()

        readme = template.replace("{{ total_algorithms }}", str(stats.total_algorithms))
        readme = readme.replace("{{ total_categories }}", str(stats.total_categories))
        readme = readme.replace("{{ total_tags }}", str(stats.total_tags))
        readme = readme.replace("{{ toc }}", toc)
        readme = readme.replace("{{ category_overview }}", category_overview)
        readme = readme.replace("{{ featured_content }}", featured_content)

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

> A curated collection of bioinformatics algorithms with complexity analysis

## Statistics

- 📊 Total Algorithms: {{ total_algorithms }}
- 📁 Categories: {{ total_categories }}
- 🏷️ Tags: {{ total_tags }}

## Table of Contents

{{ toc }}

---

{{ category_overview }}

---

{{ featured_content }}

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
"""

    def generate_toc(self) -> str:
        """
        Generate table of contents with anchor links.

        Returns:
            Markdown formatted table of contents
        """
        toc_lines = ["<details>", "<summary>Click to expand</summary>", ""]
        categories = self._category_manager.list_all_categories()

        for category in categories:
            algos = self._registry.get_by_category(category.id)
            if algos:  # Only include categories with algorithms
                anchor = self._generate_anchor(category.name_en)
                toc_lines.append(f"- [{category.name_en}](#{anchor})")

        toc_lines.extend(["", "</details>"])
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

    def _generate_category_overview(self) -> str:
        """Generate category overview table with statistics."""
        lines = ["## Category Overview", ""]
        lines.append("| Category | Algorithms | Description |")
        lines.append("|----------|------------|-------------|")

        categories = self._category_manager.list_all_categories()
        for category in categories:
            algos = self._registry.get_by_category(category.id)
            if algos:
                count = len(algos)
                desc = category.description_en or category.description
                lines.append(f"| {category.name_en} | {count} | {desc} |")

        lines.append("")
        return "\n".join(lines)

    def _generate_featured_content(self) -> str:
        """Generate featured algorithms content (limited per category)."""
        sections = ["## Featured Algorithms", ""]
        categories = self._category_manager.list_all_categories()

        for category in categories:
            section = self._generate_category_featured_section(category)
            if section.strip():
                sections.append(section)
                sections.append("")

        return "\n".join(sections)

    def _generate_category_featured_section(
        self, category: Category, max_algorithms: int = 5
    ) -> str:
        """
        Generate markdown section for a category with featured algorithms.

        Args:
            category: The category to generate section for
            max_algorithms: Maximum number of algorithms to show per subcategory

        Returns:
            Markdown formatted category section
        """
        lines = []
        all_algos = self._registry.get_by_category(category.id)

        if not all_algos:
            return ""

        # Category header with anchor and back-to-top link
        anchor = self._generate_anchor(category.name_en)
        lines.append(f'### {category.name_en} <a id="{anchor}"></a>')
        lines.append('<a href="#table-of-contents">↑ Back to Top</a>')
        lines.append("")

        # Get all algorithms with their subcategory info
        algo_data = []
        for algo in all_algos:
            subcategory_name = ""
            if algo.subcategory:
                for sub in category.subcategories:
                    if sub.id == algo.subcategory:
                        subcategory_name = sub.name_en
                        break
            algo_data.append((algo, subcategory_name))

        # Sort by importance: classic first, then by year (newer first)
        algo_data.sort(
            key=lambda x: (
                0 if x[0].is_classic() else (1 if x[0].is_new() else 2),
                -x[0].year if x[0].year else 0,
            )
        )

        # Group by subcategory
        subcategory_groups: dict[str, list[tuple[AlgorithmEntry, str]]] = {}
        for algo, sub_name in algo_data:
            key = sub_name or "General"
            if key not in subcategory_groups:
                subcategory_groups[key] = []
            subcategory_groups[key].append((algo, sub_name))

        # Generate tables for each subcategory
        for sub_name, algos in subcategory_groups.items():
            if sub_name != "General":
                lines.append(f"**{sub_name}**")
                lines.append("")

            # Table header
            lines.append("| Algorithm | Year | Time | Space | Tags |")
            lines.append("|-----------|------|------|-------|------|")

            # Featured algorithms
            featured = algos[:max_algorithms]
            for algo, _ in featured:
                badge = algo.get_year_badge()
                name = f"{badge} {algo.name}" if badge else algo.name
                year = str(algo.year) if algo.year else "-"
                time = algo.time_complexity
                space = algo.space_complexity or "-"
                tags = " ".join([f"`{t}`" for t in algo.tags[:3]]) if algo.tags else "-"

                lines.append(f"| {name} | {year} | {time} | {space} | {tags} |")

            lines.append("")

            # Link to view all
            total_in_sub = len(algos)
            if total_in_sub > max_algorithms:
                lines.append(
                    f"*[View all {total_in_sub} algorithms in this category →](https://lessup.github.io/awesome-bioinfo-algorithms/)*"
                )
                lines.append("")

        return "\n".join(lines)

    def generate_algorithm_entry(self, algo: AlgorithmEntry) -> str:
        """
        Generate markdown for a single algorithm entry (full detail format).

        Args:
            algo: The algorithm entry to format

        Returns:
            Markdown formatted algorithm entry
        """
        lines = []

        # Algorithm name as header (with year if available)
        badge = algo.get_year_badge()
        name_display = f"{badge} {algo.name}" if badge else algo.name
        if algo.year:
            lines.append(f"\n#### {name_display} ({algo.year})")
        else:
            lines.append(f"\n#### {name_display}")
        lines.append("")

        # Description (prefer English if available)
        desc = algo.description_en.strip() if algo.description_en else algo.description.strip()
        lines.append(desc)
        lines.append("")

        # Purpose
        purpose = algo.purpose_en if algo.purpose_en else algo.purpose
        lines.append(f"**Purpose**: {purpose}")

        # Complexity
        lines.append(f"**Time**: {algo.time_complexity}")
        if algo.space_complexity:
            lines.append(f"**Space**: {algo.space_complexity}")

        # Links
        if algo.paper_url:
            lines.append(f"**Paper**: [{algo.paper_url}]({algo.paper_url})")
        if algo.implementation_url:
            lines.append(
                f"**Implementation**: [{algo.implementation_url}]({algo.implementation_url})"
            )

        # Related tools
        if algo.related_tools:
            tools = ", ".join(algo.related_tools)
            lines.append(f"**Related Tools**: {tools}")

        # Tags
        if algo.tags:
            tags = " ".join([f"`{tag}`" for tag in algo.tags])
            lines.append(f"**Tags**: {tags}")

        # Difficulty
        if algo.difficulty:
            label = DIFFICULTY_LABELS_BILINGUAL.get(algo.difficulty, algo.difficulty)
            lines.append(f"**Difficulty**: {label}")

        # Implementation languages
        if algo.language:
            langs = ", ".join(algo.language)
            lines.append(f"**Language**: {langs}")

        # Extended references
        if algo.references:
            lines.append("**References**:")
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
            f"- 📊 Total Algorithms: {stats.total_algorithms}",
            f"- 📁 Categories: {stats.total_categories}",
            f"- 🏷️ Tags: {stats.total_tags}",
        ]
        return "\n".join(lines)

    def save(self, output_path: str = "README.md") -> None:
        """
        Generate and save README to file.

        Args:
            output_path: Path to save the README file
        """
        content = self.generate()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
