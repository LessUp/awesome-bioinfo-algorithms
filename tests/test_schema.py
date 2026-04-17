"""
Property-based tests for data models.
Feature: awesome-bioinfo-algorithms, Property 4: Optional Fields Storage
"""

from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from awesome_bioinfo.schema import AlgorithmEntry, Category, Reference

# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyz-_0123456789"), min_size=1, max_size=50
).filter(lambda x: x and not x.startswith("-"))

valid_name = st.text(min_size=1, max_size=100).filter(lambda x: x.strip())

valid_description = st.text(min_size=50, max_size=200).filter(lambda x: len(x.strip()) >= 50)

valid_url = st.one_of(
    st.just(""), st.text(min_size=10, max_size=200).map(lambda x: f"https://example.com/{x}")
)

valid_tags = st.lists(
    st.text(alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyz-"), min_size=1, max_size=30),
    min_size=0,
    max_size=10,
)

valid_tools = st.lists(
    st.text(min_size=1, max_size=50).filter(lambda x: x.strip()), min_size=0, max_size=10
)

valid_difficulty = st.one_of(st.just(""), st.sampled_from(["beginner", "intermediate", "advanced"]))

valid_language = st.lists(
    st.text(alphabet=st.sampled_from("abcdefghijklmnopqrstuvwxyz+#"), min_size=1, max_size=20),
    min_size=0,
    max_size=5,
)

valid_references = st.lists(
    st.fixed_dictionaries(
        {
            "url": st.text(min_size=10, max_size=200).map(lambda x: f"https://example.com/{x}"),
            "title": st.one_of(
                st.just(""), st.text(min_size=1, max_size=100).filter(lambda x: x.strip())
            ),
            "type": st.one_of(st.just(""), st.sampled_from(["tutorial", "blog", "video", "book"])),
        }
    ),
    min_size=0,
    max_size=3,
)


@st.composite
def algorithm_entry_strategy(draw):
    """Generate valid AlgorithmEntry instances with optional fields."""
    ref_dicts = draw(valid_references)
    return AlgorithmEntry(
        id=draw(valid_id),
        name=draw(valid_name),
        description=draw(valid_description),
        purpose=draw(st.text(min_size=5, max_size=100).filter(lambda x: x.strip())),
        time_complexity=draw(st.sampled_from(["O(n)", "O(n^2)", "O(mn)", "O(n log n)", "O(1)"])),
        category=draw(valid_id),
        space_complexity=draw(st.sampled_from(["", "O(n)", "O(n^2)", "O(mn)", "O(1)"])),
        year=draw(st.one_of(st.just(0), st.integers(min_value=1970, max_value=2025))),
        paper_url=draw(valid_url),
        implementation_url=draw(valid_url),
        related_tools=draw(valid_tools),
        tags=draw(valid_tags),
        subcategory=draw(st.one_of(st.just(""), valid_id)),
        difficulty=draw(valid_difficulty),
        language=draw(valid_language),
        references=[Reference.from_dict(r) for r in ref_dicts],
    )


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
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
    assert restored_entry.year == entry.year
    assert restored_entry.paper_url == entry.paper_url
    assert restored_entry.implementation_url == entry.implementation_url
    assert restored_entry.related_tools == entry.related_tools
    assert restored_entry.tags == entry.tags
    assert restored_entry.subcategory == entry.subcategory
    assert restored_entry.difficulty == entry.difficulty
    assert restored_entry.language == entry.language
    assert len(restored_entry.references) == len(entry.references)
    for orig, rest in zip(entry.references, restored_entry.references):
        assert rest.url == orig.url
        assert rest.title == orig.title
        assert rest.type == orig.type

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
        parent_id=None,
    )


@settings(max_examples=100, suppress_health_check=[HealthCheck.filter_too_much])
@given(category=category_strategy())
def test_category_round_trip(category: Category):
    """Test Category serialization round-trip."""
    category_dict = category.to_dict()
    restored = Category.from_dict(category_dict)

    assert restored.id == category.id
    assert restored.name == category.name
    assert restored.name_en == category.name_en
    assert restored.description == category.description


def test_reference_round_trip():
    """Test Reference serialization round-trip."""
    ref = Reference(url="https://example.com/tutorial", title="Tutorial", type="tutorial")
    ref_dict = ref.to_dict()
    restored = Reference.from_dict(ref_dict)
    assert restored.url == ref.url
    assert restored.title == ref.title
    assert restored.type == ref.type


def test_reference_to_dict_omits_empty_fields():
    """Test Reference.to_dict omits empty optional fields."""
    ref = Reference(url="https://example.com")
    d = ref.to_dict()
    assert "url" in d
    assert "title" not in d
    assert "type" not in d


def test_algorithm_entry_with_new_fields():
    """Test AlgorithmEntry with difficulty, language, references."""
    algo = AlgorithmEntry(
        id="test-algo",
        name="Test",
        description="A" * 60,
        purpose="testing",
        time_complexity="O(n)",
        category="test-cat",
        difficulty="beginner",
        language=["Python", "C++"],
        references=[Reference(url="https://example.com", title="Ref", type="tutorial")],
    )
    d = algo.to_dict()
    assert d["difficulty"] == "beginner"
    assert d["language"] == ["Python", "C++"]
    assert len(d["references"]) == 1
    assert d["references"][0]["url"] == "https://example.com"

    restored = AlgorithmEntry.from_dict(d)
    assert restored.difficulty == "beginner"
    assert restored.language == ["Python", "C++"]
    assert len(restored.references) == 1
    assert restored.references[0].title == "Ref"
