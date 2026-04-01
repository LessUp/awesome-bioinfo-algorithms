"""
Property-based tests for AlgorithmRegistry.
Feature: awesome-bioinfo-algorithms
"""
import pytest
from hypothesis import HealthCheck, given, settings
from hypothesis import strategies as st

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.schema import AlgorithmEntry

# Optimized strategies for generating test data
# Using simpler strategies to avoid slow generation

valid_id = st.from_regex(r'[a-z][a-z0-9]{0,19}', fullmatch=True)

valid_name = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '),
    min_size=3, max_size=30
)

# Pre-generate description with exact length to avoid filtering
valid_description = st.text(
    alphabet=st.sampled_from('abcdefghijklmnopqrstuvwxyz '),
    min_size=60, max_size=100
)

valid_complexity = st.sampled_from(['O(1)', 'O(n)', 'O(n^2)', 'O(mn)', 'O(log n)', 'O(n log n)'])

valid_tag = st.from_regex(r'[a-z][a-z\-]{0,9}', fullmatch=True)

valid_category = st.sampled_from([
    'sequence-alignment', 'assembly', 'variant-calling',
    'expression-analysis', 'protein-structure', 'phylogenetics'
])


@st.composite
def algorithm_entry_strategy(draw, category=None, algo_id=None):
    """Generate a valid AlgorithmEntry."""
    return AlgorithmEntry(
        id=algo_id if algo_id else draw(valid_id),
        name=draw(valid_name),
        description=draw(valid_description),
        purpose=draw(valid_name),
        time_complexity=draw(valid_complexity),
        category=category if category else draw(valid_category),
        space_complexity=draw(st.one_of(st.just(''), valid_complexity)),
        tags=draw(st.lists(valid_tag, min_size=0, max_size=3, unique=True)),
    )


@st.composite
def algorithms_list_strategy(draw):
    """Generate a list of algorithms with unique IDs."""
    num_algorithms = draw(st.integers(min_value=1, max_value=5))
    algorithms = []

    for i in range(num_algorithms):
        # Generate unique ID directly to avoid regeneration loops
        algo_id = f"algo{i}{draw(st.from_regex(r'[a-z]{3}', fullmatch=True))}"
        algo = draw(algorithm_entry_strategy(algo_id=algo_id))
        algorithms.append(algo)

    return algorithms


@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
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


@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
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


@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
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
        assert retrieved.id == algo.id, "Retrieved algorithm should have correct ID"


@settings(max_examples=100, suppress_health_check=[HealthCheck.too_slow])
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


def test_subcategory_lookup_returns_matching_algorithms():
    """Test that subcategory indexes are populated correctly."""
    pairwise = AlgorithmEntry(
        id='smith-waterman',
        name='Smith-Waterman',
        description='A' * 60,
        purpose='Local alignment',
        time_complexity='O(mn)',
        category='sequence-alignment',
        subcategory='pairwise',
        tags=['alignment'],
    )
    multiple = AlgorithmEntry(
        id='mafft',
        name='MAFFT',
        description='B' * 60,
        purpose='Multiple sequence alignment',
        time_complexity='O(n log n)',
        category='sequence-alignment',
        subcategory='multiple',
        tags=['alignment'],
    )

    registry = AlgorithmRegistry()
    registry.from_algorithms([pairwise, multiple])

    assert [algo.id for algo in registry.get_by_subcategory('pairwise')] == ['smith-waterman']
    assert [algo.id for algo in registry.get_by_subcategory('multiple')] == ['mafft']
    assert registry.get_direct_by_category('sequence-alignment') == []



def test_load_all_returns_empty_for_missing_directory(tmp_path):
    """Loading from a missing data directory should return an empty registry."""
    registry = AlgorithmRegistry(str(tmp_path / 'missing'))

    assert registry.load_all() == []
    assert registry.get_all_algorithms() == []



def test_load_all_ignores_yaml_without_algorithms_key(tmp_path):
    """Files without an algorithms key should be ignored cleanly."""
    data_dir = tmp_path / 'algorithms'
    data_dir.mkdir()
    (data_dir / 'metadata.yaml').write_text('metadata: {}\n', encoding='utf-8')

    registry = AlgorithmRegistry(str(data_dir))

    assert registry.load_all() == []
    assert registry.to_dict() == {'algorithms': []}



def test_load_all_loads_yaml_and_yml_files(tmp_path):
    """Both .yaml and .yml files should be loaded into indexes."""
    data_dir = tmp_path / 'algorithms'
    data_dir.mkdir()
    (data_dir / 'first.yaml').write_text(
        """algorithms:
  - id: smith-waterman
    name: Smith-Waterman
    description: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    purpose: Local alignment
    time_complexity: O(mn)
    category: sequence-alignment
    subcategory: pairwise
    tags:
      - alignment
""",
        encoding='utf-8',
    )
    (data_dir / 'second.yml').write_text(
        """algorithms:
  - id: blast
    name: BLAST
    description: BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
    purpose: Database search
    time_complexity: O(mn)
    category: sequence-alignment
    tags:
      - search
""",
        encoding='utf-8',
    )

    registry = AlgorithmRegistry(str(data_dir))
    loaded = registry.load_all()

    assert [algo.id for algo in loaded] == ['smith-waterman', 'blast']
    assert [algo.id for algo in registry.get_by_subcategory('pairwise')] == ['smith-waterman']
    assert [algo.id for algo in registry.get_direct_by_category('sequence-alignment')] == ['blast']



def test_load_all_rejects_duplicate_ids_across_files(tmp_path):
    """Duplicate IDs across files should raise ValueError."""
    data_dir = tmp_path / 'algorithms'
    data_dir.mkdir()
    content = """algorithms:
  - id: shared-id
    name: Example
    description: AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    purpose: Example purpose
    time_complexity: O(n)
    category: sequence-alignment
"""
    (data_dir / 'first.yaml').write_text(content, encoding='utf-8')
    (data_dir / 'second.yaml').write_text(content, encoding='utf-8')

    registry = AlgorithmRegistry(str(data_dir))

    with pytest.raises(ValueError, match="Duplicate algorithm ID"):
        registry.load_all()



def test_getters_return_defensive_copies():
    """Lookup helpers should return copies so callers cannot mutate registry state."""
    direct = AlgorithmEntry(
        id='blast',
        name='BLAST',
        description='A' * 60,
        purpose='Search',
        time_complexity='O(mn)',
        category='sequence-alignment',
        tags=['search'],
    )
    tagged = AlgorithmEntry(
        id='smith-waterman',
        name='Smith-Waterman',
        description='B' * 60,
        purpose='Align',
        time_complexity='O(mn)',
        category='sequence-alignment',
        subcategory='pairwise',
        tags=['search', 'alignment'],
    )
    registry = AlgorithmRegistry()
    registry.from_algorithms([direct, tagged])

    by_category = registry.get_by_category('sequence-alignment')
    by_tag = registry.get_by_tag('search')
    all_algorithms = registry.get_all_algorithms()

    by_category.clear()
    by_tag.clear()
    all_algorithms.clear()

    assert len(registry.get_by_category('sequence-alignment')) == 2
    assert len(registry.get_by_tag('search')) == 2
    assert len(registry.get_all_algorithms()) == 2



def test_get_all_tags_and_categories_reflect_loaded_indexes():
    """Tag and category listings should reflect current registry indexes."""
    direct = AlgorithmEntry(
        id='blast',
        name='BLAST',
        description='A' * 60,
        purpose='Search',
        time_complexity='O(mn)',
        category='sequence-alignment',
        tags=['search'],
    )
    tagged = AlgorithmEntry(
        id='spades',
        name='SPAdes',
        description='B' * 60,
        purpose='Assemble',
        time_complexity='O(n)',
        category='assembly',
        tags=['graph', 'search'],
    )
    registry = AlgorithmRegistry()
    registry.from_algorithms([direct, tagged])

    assert set(registry.get_all_categories()) == {'sequence-alignment', 'assembly'}
    assert set(registry.get_all_tags()) == {'search', 'graph'}



def test_validate_entry_delegates_to_validator_result():
    """Entry validation should preserve validator output semantics."""
    registry = AlgorithmRegistry()

    result = registry.validate_entry({
        'id': 'bad-entry',
        'name': 'Bad Entry',
        'description': 'too short',
        'purpose': 'Testing',
        'time_complexity': 'O(n)',
        'category': 'sequence-alignment',
    })

    assert not result.is_valid
    assert any('Description too short' in error for error in result.errors)



def test_get_algorithm_returns_none_for_missing_id():
    """Missing IDs should return None."""
    registry = AlgorithmRegistry()

    assert registry.get_algorithm('missing-id') is None



def test_search_is_case_insensitive_for_name_description_and_tags():
    """Search should match case-insensitively across name, description, and tags."""
    blast = AlgorithmEntry(
        id='blast',
        name='BLAST',
        description='Fast database search for protein sequences.' + 'A' * 30,
        purpose='Search',
        time_complexity='O(mn)',
        category='sequence-alignment',
        tags=['heuristic'],
    )
    smith = AlgorithmEntry(
        id='smith-waterman',
        name='Smith-Waterman',
        description='Local alignment with dynamic programming.' + 'B' * 30,
        purpose='Align',
        time_complexity='O(mn)',
        category='sequence-alignment',
        tags=['Dynamic-Programming'],
    )
    registry = AlgorithmRegistry()
    registry.from_algorithms([blast, smith])

    assert [algo.id for algo in registry.search('blast')] == ['blast']
    assert [algo.id for algo in registry.search('DATABASE')] == ['blast']
    assert [algo.id for algo in registry.search('dynamic')] == ['smith-waterman']



def test_from_algorithms_replaces_previous_state():
    """Reloading from a new list should replace previous indexes."""
    first = AlgorithmEntry(
        id='blast',
        name='BLAST',
        description='A' * 60,
        purpose='Search',
        time_complexity='O(mn)',
        category='sequence-alignment',
        tags=['search'],
    )
    second = AlgorithmEntry(
        id='spades',
        name='SPAdes',
        description='B' * 60,
        purpose='Assemble',
        time_complexity='O(n)',
        category='assembly',
        tags=['graph'],
    )
    registry = AlgorithmRegistry()
    registry.from_algorithms([first])
    registry.from_algorithms([second])

    assert registry.get_algorithm('blast') is None
    assert registry.get_algorithm('spades') is not None
    assert registry.get_all_categories() == ['assembly']



def test_statistics_and_to_dict_for_empty_registry():
    """Empty registries should report zeroed statistics and an empty export payload."""
    registry = AlgorithmRegistry()
    stats = registry.get_statistics()

    assert stats.total_algorithms == 0
    assert stats.total_categories == 0
    assert stats.total_tags == 0
    assert stats.algorithms_by_category == {}
    assert registry.to_dict() == {'algorithms': []}
