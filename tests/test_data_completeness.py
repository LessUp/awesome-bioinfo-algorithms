"""
Property-based tests for data completeness.
Feature: project-enhancement
"""

from pathlib import Path

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager
from scripts.validate import Validator

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
ALGORITHMS_DIR = DATA_DIR / "algorithms"
CATEGORIES_PATH = DATA_DIR / "categories.yaml"


# Load actual data for testing
def load_registry():
    """Load the actual algorithm registry."""
    registry = AlgorithmRegistry(str(ALGORITHMS_DIR))
    registry.load_all()
    return registry


def load_categories():
    """Load the actual category manager."""
    cm = CategoryManager()
    cm.load_categories(str(CATEGORIES_PATH))
    return cm


@settings(max_examples=1, suppress_health_check=[HealthCheck.too_slow], deadline=None)
@given(st.just(None))
def test_property_1_algorithm_data_completeness(_):
    """
    Feature: project-enhancement, Property 1: Algorithm Data Completeness

    For any algorithm entry in the registry, the entry SHALL pass all validation
    rules including required fields, description length (50-500 characters),
    and valid category reference.

    Validates: Requirements 7.2, 7.3
    """
    registry = load_registry()
    cm = load_categories()
    validator = Validator()
    categories_result = validator.validate_categories_file(str(CATEGORIES_PATH))
    assert categories_result.is_valid, categories_result.errors
    valid_categories = cm.list_all_category_ids()

    algorithms = registry.get_all_algorithms()
    assert len(algorithms) > 0, "Registry should contain at least one algorithm"

    for algo in algorithms:
        algo_dict = algo.to_dict()
        result = validator.validate_algorithm(algo_dict)

        assert result.is_valid, f"Algorithm '{algo.id}' failed validation: {result.errors}"

        # Verify description length
        desc_len = len(algo.description.strip())
        assert 50 <= desc_len <= 500, (
            f"Algorithm '{algo.id}' description length {desc_len} not in range [50, 500]"
        )

        # Verify category exists
        assert algo.category in valid_categories, (
            f"Algorithm '{algo.id}' has invalid category '{algo.category}'"
        )


@settings(max_examples=1, suppress_health_check=[HealthCheck.too_slow], deadline=None)
@given(st.just(None))
def test_property_2_category_coverage(_):
    """
    Feature: project-enhancement, Property 2: Category Coverage

    For any main category defined in categories.yaml, the category SHALL
    contain at least 2 algorithms in the registry.

    Validates: Requirements 7.1
    """
    registry = load_registry()
    cm = load_categories()

    # Get main categories (top-level only)
    main_categories = cm.list_all_categories()

    for category in main_categories:
        algorithms = registry.get_by_category(category.id)
        assert len(algorithms) >= 2, (
            f"Category '{category.id}' ({category.name_en}) has only "
            f"{len(algorithms)} algorithm(s), expected at least 2"
        )


def test_all_algorithms_have_required_fields():
    """Test that all algorithms have all required fields populated."""
    registry = load_registry()

    required_fields = ["id", "name", "description", "purpose", "time_complexity", "category"]

    for algo in registry.get_all_algorithms():
        algo_dict = algo.to_dict()
        for field in required_fields:
            assert field in algo_dict, f"Algorithm '{algo.id}' missing required field '{field}'"
            assert algo_dict[field], f"Algorithm '{algo.id}' has empty required field '{field}'"


def test_no_duplicate_algorithm_ids():
    """Test that there are no duplicate algorithm IDs."""
    registry = load_registry()

    seen_ids = set()
    for algo in registry.get_all_algorithms():
        assert algo.id not in seen_ids, f"Duplicate algorithm ID found: '{algo.id}'"
        seen_ids.add(algo.id)
