"""
Property-based tests for AlgorithmRegistry.
Feature: awesome-bioinfo-algorithms
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hypothesis import given, settings, strategies as st
from scripts.schema import AlgorithmEntry
from scripts.algorithm_registry import AlgorithmRegistry


# Strategies for generating test data
valid_id = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz0123456789-'),
    min_size=1, max_size=30
).filter(lambda x: x and x[0].isalpha() and not x.endswith('-'))

valid_name = st.text(min_size=1, max_size=50).filter(lambda x: x.strip())

valid_description = st.text(min_size=50, max_size=200).filter(lambda x: len(x.strip()) >= 50)

valid_complexity = st.sampled_from(['O(1)', 'O(n)', 'O(n^2)', 'O(mn)', 'O(log n)', 'O(n log n)'])

valid_tag = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz-'),
    min_size=1, max_size=20
).filter(lambda x: x and x[0].isalpha())

valid_category = st.sampled_from([
    'sequence-alignment', 'assembly', 'variant-calling',
    'expression-analysis', 'protein-structure', 'phylogenetics'
])


@st.composite
def algorithm_entry_strategy(draw, category=None):
    """Generate a valid AlgorithmEntry."""
    return AlgorithmEntry(
        id=draw(valid_id),
        name=draw(valid_name),
        description=draw(valid_description),
        purpose=draw(valid_name),
        time_complexity=draw(valid_complexity),
        category=category if category else draw(valid_category),
        space_complexity=draw(st.one_of(st.just(''), valid_complexity)),
        tags=draw(st.lists(valid_tag, min_size=0, max_size=5, unique=True)),
    )


@st.composite
def algorithms_list_strategy(draw):
    """Generate a list of algorithms with unique IDs."""
    num_algorithms = draw(st.integers(min_value=1, max_value=10))
    algorithms = []
    used_ids = set()
    
    for i in range(num_algorithms):
        algo = draw(algorithm_entry_strategy())
        # Ensure unique ID
        while algo.id in used_ids:
            algo = AlgorithmEntry(
                id=f"{algo.id}{i}",
                name=algo.name,
                description=algo.description,
                purpose=algo.purpose,
                time_complexity=algo.time_complexity,
                category=algo.category,
                space_complexity=algo.space_complexity,
                tags=algo.tags,
            )
        used_ids.add(algo.id)
        algorithms.append(algo)
    
    return algorithms


@settings(max_examples=100)
@given(algorithms=algorithms_list_strategy())
def test_property_1_category_algorithm_count_accuracy(algorithms):
    """
    Feature: awesome-bioinfo-algorithms, Property 1: Category Algorithm Count Accuracy
    
    For any algorithm registry with algorithms distributed across categories,
    the count displayed for each category SHALL equal the actual number of
    algorithms in that category.
    
    Validates: Requirements 1.2, 3.4
    """
    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)
    
    stats = registry.get_statistics()
    
    # Count algorithms by category manually
    expected_counts = {}
    for algo in algorithms:
        expected_counts[algo.category] = expected_counts.get(algo.category, 0) + 1
    
    # Verify counts match
    assert stats.algorithms_by_category == expected_counts, \
        f"Category counts should match: {stats.algorithms_by_category} vs {expected_counts}"
    
    # Verify total count
    assert stats.total_algorithms == len(algorithms), \
        f"Total algorithms should be {len(algorithms)}, got {stats.total_algorithms}"
    
    # Verify get_by_category returns correct count
    for category, expected_count in expected_counts.items():
        actual = registry.get_by_category(category)
        assert len(actual) == expected_count, \
            f"Category '{category}' should have {expected_count} algorithms, got {len(actual)}"


@settings(max_examples=100)
@given(algorithms=algorithms_list_strategy())
def test_property_8_search_result_correctness(algorithms):
    """
    Feature: awesome-bioinfo-algorithms, Property 8: Search Result Correctness
    
    For any search query (by name or tag), all returned algorithms SHALL match
    the search criteria, and no matching algorithm SHALL be omitted from the results.
    
    Validates: Requirements 5.1, 5.2, 5.3
    """
    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)
    
    # Test search by name
    for algo in algorithms:
        # Search by partial name
        search_term = algo.name[:3] if len(algo.name) >= 3 else algo.name
        results = registry.search(search_term)
        
        # Verify the algorithm is in results
        matching_ids = [r.id for r in results]
        assert algo.id in matching_ids, \
            f"Algorithm '{algo.id}' should be found when searching for '{search_term}'"
        
        # Verify all results actually match
        for result in results:
            assert (search_term.lower() in result.name.lower() or
                    search_term.lower() in result.description.lower() or
                    any(search_term.lower() in tag.lower() for tag in result.tags)), \
                f"Result '{result.id}' should match search term '{search_term}'"
    
    # Test search by tag
    for algo in algorithms:
        for tag in algo.tags:
            results = registry.get_by_tag(tag)
            matching_ids = [r.id for r in results]
            assert algo.id in matching_ids, \
                f"Algorithm '{algo.id}' should be found when filtering by tag '{tag}'"


@settings(max_examples=100)
@given(algorithms=algorithms_list_strategy())
def test_all_algorithms_retrievable(algorithms):
    """Test that all loaded algorithms can be retrieved."""
    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)
    
    all_algos = registry.get_all_algorithms()
    assert len(all_algos) == len(algorithms), \
        f"Should have {len(algorithms)} algorithms, got {len(all_algos)}"
    
    for algo in algorithms:
        retrieved = registry.get_algorithm(algo.id)
        assert retrieved is not None, f"Algorithm '{algo.id}' should be retrievable"
        assert retrieved.id == algo.id, f"Retrieved algorithm should have correct ID"


@settings(max_examples=100)
@given(algorithms=algorithms_list_strategy())
def test_tag_statistics(algorithms):
    """Test that tag statistics are accurate."""
    registry = AlgorithmRegistry()
    registry.from_algorithms(algorithms)
    
    stats = registry.get_statistics()
    
    # Count unique tags manually
    all_tags = set()
    for algo in algorithms:
        all_tags.update(algo.tags)
    
    assert stats.total_tags == len(all_tags), \
        f"Should have {len(all_tags)} unique tags, got {stats.total_tags}"
