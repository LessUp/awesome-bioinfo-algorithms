"""
Property-based tests for data models.
Feature: awesome-bioinfo-algorithms, Property 4: Optional Fields Storage
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypothesis import given, settings, strategies as st
from scripts.schema import AlgorithmEntry, Category


# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz-_0123456789'),
    min_size=1, max_size=50
).filter(lambda x: x and not x.startswith('-'))

valid_name = st.text(min_size=1, max_size=100).filter(lambda x: x.strip())

valid_description = st.text(min_size=50, max_size=200).filter(lambda x: len(x.strip()) >= 50)

valid_url = st.one_of(
    st.just(""),
    st.text(min_size=10, max_size=200).map(lambda x: f"https://example.com/{x}")
)

valid_tags = st.lists(
    st.text(alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz-'), min_size=1, max_size=30),
    min_size=0, max_size=10
)

valid_tools = st.lists(
    st.text(min_size=1, max_size=50).filter(lambda x: x.strip()),
    min_size=0, max_size=10
)


@st.composite
def algorithm_entry_strategy(draw):
    """Generate valid AlgorithmEntry instances with optional fields."""
    return AlgorithmEntry(
        id=draw(valid_id),
        name=draw(valid_name),
        description=draw(valid_description),
        purpose=draw(st.text(min_size=5, max_size=100).filter(lambda x: x.strip())),
        time_complexity=draw(st.sampled_from(['O(n)', 'O(n^2)', 'O(mn)', 'O(n log n)', 'O(1)'])),
        category=draw(valid_id),
        space_complexity=draw(st.sampled_from(['', 'O(n)', 'O(n^2)', 'O(mn)', 'O(1)'])),
        paper_url=draw(valid_url),
        implementation_url=draw(valid_url),
        related_tools=draw(valid_tools),
        tags=draw(valid_tags),
        subcategory=draw(st.one_of(st.just(""), valid_id)),
    )


@settings(max_examples=100)
@given(entry=algorithm_entry_strategy())
def test_property_4_optional_fields_storage(entry: AlgorithmEntry):
    """
    Feature: awesome-bioinfo-algorithms, Property 4: Optional Fields Storage
    
    For any algorithm entry with optional fields (space_complexity, paper_url,
    implementation_url, related_tools, tags), storing and retrieving the entry
    SHALL preserve all optional field values exactly.
    
    Validates: Requirements 2.2, 2.4
    """
    # Convert to dict and back
    entry_dict = entry.to_dict()
    restored_entry = AlgorithmEntry.from_dict(entry_dict)
    
    # Verify all optional fields are preserved
    assert restored_entry.space_complexity == entry.space_complexity
    assert restored_entry.paper_url == entry.paper_url
    assert restored_entry.implementation_url == entry.implementation_url
    assert restored_entry.related_tools == entry.related_tools
    assert restored_entry.tags == entry.tags
    assert restored_entry.subcategory == entry.subcategory
    
    # Verify complete equality
    assert restored_entry == entry


@st.composite
def category_strategy(draw):
    """Generate valid Category instances."""
    return Category(
        id=draw(valid_id),
        name=draw(valid_name),
        name_en=draw(valid_name),
        description=draw(st.text(min_size=0, max_size=200)),
        subcategories=[],
        parent_id=None
    )


@settings(max_examples=100)
@given(category=category_strategy())
def test_category_round_trip(category: Category):
    """Test Category serialization round-trip."""
    category_dict = category.to_dict()
    restored = Category.from_dict(category_dict)
    
    assert restored.id == category.id
    assert restored.name == category.name
    assert restored.name_en == category.name_en
    assert restored.description == category.description
