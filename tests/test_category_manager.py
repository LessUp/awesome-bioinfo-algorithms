"""
Property-based tests for CategoryManager.
Feature: awesome-bioinfo-algorithms, Property 2: Subcategory Hierarchy Preservation
"""
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from scripts.category_manager import CategoryManager
from scripts.schema import Category

# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz0123456789'),
    min_size=1, max_size=20
).filter(lambda x: x and x[0].isalpha())

valid_name = st.text(min_size=1, max_size=50).filter(lambda x: x.strip())


@st.composite
def subcategory_strategy(draw, parent_id: str):
    """Generate a subcategory with reference to parent."""
    return Category(
        id=draw(valid_id),
        name=draw(valid_name),
        name_en=draw(valid_name),
        description=draw(st.text(min_size=0, max_size=100)),
        subcategories=[],
        parent_id=parent_id
    )


@st.composite
def categories_list_strategy(draw):
    """Generate a list of categories with subcategories, ensuring unique IDs."""
    num_categories = draw(st.integers(min_value=1, max_value=5))
    categories = []
    used_ids = set()
    counter = [0]  # Use list to allow mutation in nested function

    def get_unique_id():
        """Generate a unique ID."""
        base = draw(valid_id)
        while base in used_ids:
            counter[0] += 1
            base = f"{base}{counter[0]}"
        used_ids.add(base)
        return base

    for _ in range(num_categories):
        cat_id = get_unique_id()
        num_subcategories = draw(st.integers(min_value=0, max_value=3))

        subcategories = []
        for _ in range(num_subcategories):
            sub_id = get_unique_id()
            sub = Category(
                id=sub_id,
                name=draw(valid_name),
                name_en=draw(valid_name),
                description=draw(st.text(min_size=0, max_size=100)),
                subcategories=[],
                parent_id=cat_id  # Correctly set parent_id to current category
            )
            subcategories.append(sub)

        cat = Category(
            id=cat_id,
            name=draw(valid_name),
            name_en=draw(valid_name),
            description=draw(st.text(min_size=0, max_size=100)),
            subcategories=subcategories,
            parent_id=None
        )
        categories.append(cat)

    return categories


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(categories=categories_list_strategy())
def test_property_2_subcategory_hierarchy_preservation(categories):
    """
    Feature: awesome-bioinfo-algorithms, Property 2: Subcategory Hierarchy Preservation

    For any category with subcategories, retrieving the category SHALL return
    all its subcategories, and each subcategory SHALL correctly reference its parent category.

    Validates: Requirements 1.3
    """
    manager = CategoryManager()
    manager.from_categories(categories)

    for category in categories:
        # Retrieve the category
        retrieved = manager.get_category(category.id)
        assert retrieved is not None, f"Category '{category.id}' should be retrievable"

        # Verify all subcategories are present
        assert len(retrieved.subcategories) == len(category.subcategories), \
            f"Category '{category.id}' should have {len(category.subcategories)} subcategories"

        # Verify each subcategory references the parent
        for sub in retrieved.subcategories:
            assert sub.parent_id == category.id, \
                f"Subcategory '{sub.id}' should reference parent '{category.id}'"

            # Verify subcategory is retrievable
            retrieved_sub = manager.get_category(sub.id)
            assert retrieved_sub is not None, \
                f"Subcategory '{sub.id}' should be retrievable"

            # Verify parent lookup works
            parent = manager.get_parent_category(sub.id)
            assert parent is not None, \
                f"Parent of subcategory '{sub.id}' should be retrievable"
            assert parent.id == category.id, \
                f"Parent of '{sub.id}' should be '{category.id}'"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(categories=categories_list_strategy())
def test_all_category_ids_listed(categories):
    """Test that all category IDs (including subcategories) are listed."""
    manager = CategoryManager()
    manager.from_categories(categories)

    all_ids = manager.list_all_category_ids()

    for category in categories:
        assert category.id in all_ids, f"Category '{category.id}' should be in ID list"
        for sub in category.subcategories:
            assert sub.id in all_ids, f"Subcategory '{sub.id}' should be in ID list"


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(categories=categories_list_strategy())
def test_category_exists_check(categories):
    """Test that category_exists correctly identifies existing categories."""
    manager = CategoryManager()
    manager.from_categories(categories)

    for category in categories:
        assert manager.category_exists(category.id), \
            f"Category '{category.id}' should exist"
        for sub in category.subcategories:
            assert manager.category_exists(sub.id), \
                f"Subcategory '{sub.id}' should exist"

    # Non-existent category
    assert not manager.category_exists('nonexistent-category-xyz')
