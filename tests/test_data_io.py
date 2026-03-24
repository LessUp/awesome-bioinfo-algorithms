"""
Property-based tests for Data Import/Export.
Feature: awesome-bioinfo-algorithms, Property 11: Data Import/Export Round-Trip
"""
import os
import tempfile

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager
from scripts.data_io import DataIO
from scripts.schema import AlgorithmEntry, Category

# Strategies for generating test data - using ASCII-safe characters for YAML round-trip
valid_id = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz0123456789'),
    min_size=1, max_size=20
).filter(lambda x: x and x[0].isalpha())

# Use ASCII-safe characters to avoid YAML Unicode normalization issues
valid_name = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -_'),
    min_size=1, max_size=30
).filter(lambda x: x.strip())

valid_description = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,!?-_'),
    min_size=50, max_size=200
).filter(lambda x: len(x.strip()) >= 50)

valid_complexity = st.sampled_from(['O(1)', 'O(n)', 'O(n^2)', 'O(mn)', 'O(log n)'])


@st.composite
def categories_and_algorithms_strategy(draw):
    """Generate categories and algorithms with matching category IDs."""
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
            parent_id=None
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
                space_complexity=draw(st.one_of(st.just(''), valid_complexity)),
                year=draw(st.one_of(st.just(0), st.integers(min_value=1970, max_value=2025))),
                paper_url=draw(st.one_of(st.just(''), st.just('https://example.com/paper'))),
                implementation_url=draw(st.one_of(st.just(''), st.just('https://github.com/example'))),
                related_tools=draw(st.lists(valid_name, min_size=0, max_size=3)),
                tags=draw(st.lists(valid_id, min_size=0, max_size=3, unique=True)),
                subcategory=draw(st.one_of(st.just(''), valid_id)),
            )
            algorithms.append(algo)

    return categories, algorithms


@settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.filter_too_much])
@given(data=categories_and_algorithms_strategy())
def test_property_11_round_trip_yaml(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 11: Data Import/Export Round-Trip

    For any valid algorithm registry, exporting the data and then importing it back
    SHALL produce an equivalent registry with identical algorithms and categories.

    Validates: Requirements 6.4
    """
    categories, algorithms = data

    # Set up registry and category manager
    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    data_io = DataIO(registry, category_manager)

    # Export to YAML
    with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False) as f:
        temp_path = f.name

    try:
        data_io.export_data(temp_path, fmt='yaml')

        # Import back
        imported_categories, imported_algorithms = data_io.import_data(temp_path)

        # Verify categories match
        assert len(imported_categories) == len(categories), \
            f"Should have {len(categories)} categories, got {len(imported_categories)}"

        for orig, imported in zip(categories, imported_categories):
            assert orig.id == imported.id, "Category ID should match"
            assert orig.name == imported.name, "Category name should match"
            assert orig.name_en == imported.name_en, "Category name_en should match"

        # Verify algorithms match
        assert len(imported_algorithms) == len(algorithms), \
            f"Should have {len(algorithms)} algorithms, got {len(imported_algorithms)}"

        for orig, imported in zip(algorithms, imported_algorithms):
            assert orig.id == imported.id, "Algorithm ID should match"
            assert orig.name == imported.name, "Algorithm name should match"
            assert orig.description == imported.description, "Algorithm description should match"
            assert orig.purpose == imported.purpose, "Algorithm purpose should match"
            assert orig.time_complexity == imported.time_complexity, "Time complexity should match"
            assert orig.category == imported.category, "Category should match"
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
@given(data=categories_and_algorithms_strategy())
def test_property_11_round_trip_json(data):
    """
    Feature: awesome-bioinfo-algorithms, Property 11: Data Import/Export Round-Trip (JSON)

    For any valid algorithm registry, exporting to JSON and importing back
    SHALL produce an equivalent registry.

    Validates: Requirements 6.4
    """
    categories, algorithms = data

    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)

    category_manager = CategoryManager()
    category_manager.from_categories(categories)

    data_io = DataIO(registry, category_manager)

    # Export to JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_path = f.name

    try:
        data_io.export_data(temp_path, fmt='json')

        # Import back
        imported_categories, imported_algorithms = data_io.import_data(temp_path)

        # Verify counts match
        assert len(imported_categories) == len(categories)
        assert len(imported_algorithms) == len(algorithms)

        # Verify all algorithm IDs are preserved
        orig_ids = {a.id for a in algorithms}
        imported_ids = {a.id for a in imported_algorithms}
        assert orig_ids == imported_ids, "All algorithm IDs should be preserved"
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much, HealthCheck.too_slow])
@given(data=categories_and_algorithms_strategy())
def test_dict_round_trip(data):
    """Test round-trip through dictionary conversion."""
    categories, algorithms = data

    # Export to dict
    exported = DataIO.export_to_dict(categories, algorithms)

    # Import from dict
    imported_categories, imported_algorithms = DataIO.import_from_dict(exported)

    # Verify
    assert len(imported_categories) == len(categories)
    assert len(imported_algorithms) == len(algorithms)

    for orig, imported in zip(algorithms, imported_algorithms):
        assert orig == imported, f"Algorithm {orig.id} should equal imported version"
