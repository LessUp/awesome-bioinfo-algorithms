"""
Property-based tests for ReadmeGenerator.
Feature: awesome-bioinfo-algorithms
"""

from pathlib import Path

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from awesome_bioinfo.algorithm_registry import AlgorithmRegistry
from awesome_bioinfo.category_manager import CategoryManager
from awesome_bioinfo.readme_generator import ReadmeGenerator
from awesome_bioinfo.schema import AlgorithmEntry, Category

# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyz0123456789"), min_size=1, max_size=20
).filter(lambda x: x and x[0].isalpha())

valid_name = st.text(min_size=1, max_size=30).filter(lambda x: x.strip())

valid_description = st.text(min_size=50, max_size=200).filter(lambda x: len(x.strip()) >= 50)

valid_complexity = st.sampled_from(["O(1)", "O(n)", "O(n^2)", "O(mn)", "O(log n)"])


@st.composite
def category_with_id_strategy(draw, cat_id: str):
    """Generate a category with a specific ID."""
    return Category(
        id=cat_id,
        name=draw(valid_name),
        name_en=draw(valid_name),
        description=draw(st.text(min_size=0, max_size=100)),
        subcategories=[],
        parent_id=None,
    )


@st.composite
def algorithm_for_category_strategy(draw, category_id: str, algo_id: str):
    """Generate an algorithm for a specific category."""
    return AlgorithmEntry(
        id=algo_id,
        name=draw(valid_name),
        description=draw(valid_description),
        purpose=draw(valid_name),
        time_complexity=draw(valid_complexity),
        category=category_id,
        tags=draw(st.lists(valid_id, min_size=0, max_size=3, unique=True)),
    )


@st.composite
def registry_with_categories_strategy(draw):
    """Generate a registry with categories and algorithms."""
    num_categories = draw(st.integers(min_value=1, max_value=5))
    categories = []
    algorithms = []
    used_ids = set()
    counter = [0]

    def get_unique_id(prefix=""):
        base = draw(valid_id)
        while f"{prefix}{base}" in used_ids:
            counter[0] += 1
            base = f"{base}{counter[0]}"
        unique_id = f"{prefix}{base}" if prefix else base
        used_ids.add(unique_id)
        return unique_id

    for _ in range(num_categories):
        cat_id = get_unique_id("cat")
        cat = Category(
            id=cat_id,
            name=draw(valid_name),
            name_en=draw(valid_name),
            description=draw(st.text(min_size=0, max_size=100)),
            subcategories=[],
            parent_id=None,
        )
        categories.append(cat)

        # Add algorithms to this category
        num_algos = draw(st.integers(min_value=0, max_value=3))
        for _ in range(num_algos):
            algo_id = get_unique_id("algo")
            algo = AlgorithmEntry(
                id=algo_id,
                name=draw(valid_name),
                description=draw(valid_description),
                purpose=draw(valid_name),
                time_complexity=draw(valid_complexity),
                category=cat_id,
                tags=draw(st.lists(valid_id, min_size=0, max_size=3, unique=True)),
            )
            algorithms.append(algo)

    return categories, algorithms


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(data=registry_with_categories_strategy())
def test_property_6_toc_completeness(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 6: Table of Contents Completeness

    For any algorithm registry, the generated table of contents SHALL contain
    an entry for every category that has at least one algorithm.

    Validates: Requirements 3.1
    """
    categories, algorithms = data

    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    generator = ReadmeGenerator(registry, category_manager)
    toc = generator.generate_toc()

    # Check that every category with algorithms is in the TOC
    for category in categories:
        algos_in_cat = registry.get_by_category(category.id)
        if algos_in_cat:
            # Category should be in TOC (using Chinese name)
            assert category.name in toc, (
                f"Category '{category.name}' with {len(algos_in_cat)} algorithms should be in TOC"
            )


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(data=registry_with_categories_strategy())
def test_property_5_markdown_output_consistency(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 5: Markdown Output Consistency

    For any algorithm entry, the generated Markdown output SHALL contain
    the algorithm name, description, purpose, and time complexity in a consistent format.

    Validates: Requirements 2.3
    """
    categories, algorithms = data

    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    generator = ReadmeGenerator(registry, category_manager)

    for algo in algorithms:
        output = generator.generate_algorithm_entry(algo)

        # Verify required fields are present
        assert algo.name in output, f"Algorithm name '{algo.name}' should be in output"
        assert algo.description.strip() in output, "Algorithm description should be in output"
        assert algo.purpose in output, f"Algorithm purpose '{algo.purpose}' should be in output"
        assert algo.time_complexity in output, (
            f"Time complexity '{algo.time_complexity}' should be in output"
        )

        # Verify consistent format markers (Chinese labels)
        assert "**用途**:" in output, "Purpose should have consistent label"
        assert "**时间**:" in output, "Time complexity should have consistent label"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(data=registry_with_categories_strategy())
def test_property_9_anchor_link_validity(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 9: Anchor Link Format Validity

    For any generated table of contents entry, the anchor link SHALL be a valid
    Markdown anchor that correctly links to the corresponding section.

    Validates: Requirements 5.4
    """
    categories, algorithms = data

    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    generator = ReadmeGenerator(registry, category_manager)

    for category in categories:
        algos_in_cat = registry.get_by_category(category.id)
        if algos_in_cat:
            # Use Chinese name for anchor
            anchor = generator._generate_anchor(category.name)

            # Anchor should be lowercase
            assert anchor == anchor.lower(), f"Anchor '{anchor}' should be lowercase"

            # Anchor should not have spaces
            assert " " not in anchor, f"Anchor '{anchor}' should not contain spaces"

            # Anchor should not start or end with hyphen
            assert not anchor.startswith("-") and not anchor.endswith("-"), (
                f"Anchor '{anchor}' should not start or end with hyphen"
            )

            # Anchor should not have consecutive hyphens
            assert "--" not in anchor, f"Anchor '{anchor}' should not have consecutive hyphens"


@settings(
    max_examples=100, suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow]
)
@given(data=registry_with_categories_strategy())
def test_full_readme_generation(data):
    """Test that full README generation works without errors."""
    categories, algorithms = data

    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    generator = ReadmeGenerator(registry, category_manager)
    readme = generator.generate()

    # Verify basic structure (title can be markdown or HTML)
    assert "Awesome Bioinformatics Algorithms" in readme
    assert "统计摘要" in readme  # Statistics section (Chinese)
    assert "目录" in readme  # Table of Contents section (Chinese)

    # Verify statistics are filled in
    stats = registry.get_statistics()
    assert str(stats.total_algorithms) in readme


def test_subcategory_sections_and_toc_are_rendered():
    """Test that subcategories appear in the featured algorithms section."""
    pairwise = Category(
        id="pairwise",
        name="双序列比对",
        name_en="Pairwise Alignment",
        description="两条序列之间的比对算法",
        subcategories=[],
        parent_id="sequence-alignment",
    )
    category = Category(
        id="sequence-alignment",
        name="序列比对",
        name_en="Sequence Alignment",
        description="用于比较和对齐生物序列的算法",
        subcategories=[pairwise],
        parent_id=None,
    )
    algorithm = AlgorithmEntry(
        id="smith-waterman",
        name="Smith-Waterman",
        description="A" * 60,
        purpose="局部序列比对",
        time_complexity="O(mn)",
        category="sequence-alignment",
        subcategory="pairwise",
    )

    registry = AlgorithmRegistry()
    registry.from_algorithms([algorithm])

    category_manager = CategoryManager()
    category_manager.from_categories([category])

    generator = ReadmeGenerator(registry, category_manager)
    toc = generator.generate_toc()
    section = generator._generate_category_section(category)

    # TOC uses Chinese names
    assert "序列比对" in toc
    # Section shows featured algorithms in table format
    assert "Smith-Waterman" in section
    assert "双序列比对" in section  # Subcategory name shown


def test_generated_readme_matches_repository_readme(
    project_root, loaded_registry, loaded_category_manager
):
    """Real repository data and template should reproduce the committed README exactly."""
    template_path = Path(project_root) / "templates" / "readme_template.md"
    expected_readme = (Path(project_root) / "README.md").read_text(encoding="utf-8")

    generator = ReadmeGenerator(loaded_registry, loaded_category_manager, str(template_path))
    generated = generator.generate()

    assert generated == expected_readme
    assert "{{ total_algorithms }}" not in generated
    assert "{{ total_categories }}" not in generated
    assert "{{ total_tags }}" not in generated
    assert "{{ toc }}" not in generated
    assert "{{ category_overview }}" not in generated
    assert "{{ featured_content }}" not in generated


def test_real_repository_toc_entries_match_rendered_sections(
    project_root, loaded_registry, loaded_category_manager
):
    """Real generated TOC entries should line up with rendered category headings."""
    template_path = Path(project_root) / "templates" / "readme_template.md"
    generator = ReadmeGenerator(loaded_registry, loaded_category_manager, str(template_path))
    readme = generator.generate()

    for category in loaded_category_manager.list_all_categories():
        category_algorithms = loaded_registry.get_by_category(category.id)
        if not category_algorithms:
            continue

        # TOC uses Chinese name
        category_anchor = generator._generate_anchor(category.name)
        assert f"- [{category.name}](#{category_anchor})" in readme
        # Section headers use Chinese name
        assert f"### {category.name}" in readme


def test_save_writes_same_content_as_tracked_readme(
    tmp_path, project_root, loaded_registry, loaded_category_manager
):
    """save() should write the same content as the tracked repository README."""
    template_path = Path(project_root) / "templates" / "readme_template.md"
    expected_readme = (Path(project_root) / "README.md").read_text(encoding="utf-8")
    output_path = tmp_path / "README.md"

    generator = ReadmeGenerator(loaded_registry, loaded_category_manager, str(template_path))
    generator.save(str(output_path))

    assert output_path.read_text(encoding="utf-8") == expected_readme
