"""Tests for the search command module."""

import pytest

from awesome_bioinfo.algorithm_registry import AlgorithmRegistry
from awesome_bioinfo.category_manager import CategoryManager
from awesome_bioinfo.schema import AlgorithmEntry, Category
from awesome_bioinfo.search import cmd_search, format_algorithm_short, search_algorithms


@pytest.fixture
def mock_category_manager():
    """Create a mock category manager."""
    manager = CategoryManager()
    manager.from_categories(
        [
            Category(
                id="test-cat",
                name="测试分类",
                name_en="Test Category",
                description="A test category",
            ),
        ]
    )
    return manager


@pytest.fixture
def mock_registry():
    """Create a mock registry with sample algorithms."""
    registry = AlgorithmRegistry()
    # Use from_algorithms to properly register algorithms
    registry.from_algorithms(
        [
            AlgorithmEntry(
                id="algo-1",
                name="Test Algorithm One",
                description="A test algorithm description that meets the minimum length requirement for validation purposes.",
                purpose="Testing purposes",
                time_complexity="O(n)",
                category="test-cat",
                tags=["test", "unit"],
                difficulty="beginner",
            ),
            AlgorithmEntry(
                id="algo-2",
                name="Test Algorithm Two",
                description="Another test algorithm description that meets the minimum length requirement for validation.",
                purpose="More testing",
                time_complexity="O(n log n)",
                category="test-cat",
                tags=["test", "integration"],
                difficulty="intermediate",
            ),
        ]
    )
    return registry


class TestSearchAlgorithms:
    """Tests for search_algorithms function."""

    def test_search_by_keyword(self, mock_registry, mock_category_manager):
        """Test keyword search returns matching algorithms."""
        results = search_algorithms(mock_registry, mock_category_manager, keyword="One")
        assert len(results) == 1
        assert results[0].id == "algo-1"

    def test_search_by_tag(self, mock_registry, mock_category_manager):
        """Test tag filter returns matching algorithms."""
        results = search_algorithms(mock_registry, mock_category_manager, tag="unit")
        assert len(results) == 1
        assert results[0].id == "algo-1"

    def test_search_by_category(self, mock_registry, mock_category_manager):
        """Test category filter returns matching algorithms."""
        results = search_algorithms(mock_registry, mock_category_manager, category="test-cat")
        assert len(results) == 2

    def test_search_by_difficulty(self, mock_registry, mock_category_manager):
        """Test difficulty filter returns matching algorithms."""
        results = search_algorithms(mock_registry, mock_category_manager, difficulty="beginner")
        assert len(results) == 1
        assert results[0].id == "algo-1"

    def test_search_combined_filters(self, mock_registry, mock_category_manager):
        """Test combined filters work correctly."""
        results = search_algorithms(
            mock_registry,
            mock_category_manager,
            tag="test",
            difficulty="intermediate",
        )
        assert len(results) == 1
        assert results[0].id == "algo-2"

    def test_search_no_results(self, mock_registry, mock_category_manager):
        """Test search with no matches returns empty list."""
        results = search_algorithms(mock_registry, mock_category_manager, keyword="nonexistent")
        assert len(results) == 0


class TestFormatAlgorithmShort:
    """Tests for format_algorithm_short function."""

    def test_format_basic(self, mock_registry, mock_category_manager):
        """Test basic formatting of algorithm."""
        algo = mock_registry.get_algorithm("algo-1")
        result = format_algorithm_short(algo, mock_category_manager)
        assert "algo-1" in result
        assert "Test Algorithm One" in result

    def test_format_with_year(self, mock_registry, mock_category_manager):
        """Test formatting includes year when present."""
        algo = AlgorithmEntry(
            id="algo-year",
            name="Test Algorithm",
            description="A test algorithm description that meets the minimum length requirement.",
            purpose="Testing",
            time_complexity="O(n)",
            category="test-cat",
            year=2020,
        )
        result = format_algorithm_short(algo, mock_category_manager)
        assert "(2020)" in result

    def test_format_with_difficulty(self, mock_registry, mock_category_manager):
        """Test formatting includes difficulty when present."""
        algo = mock_registry.get_algorithm("algo-1")
        result = format_algorithm_short(algo, mock_category_manager)
        assert "[beginner]" in result


class TestCmdSearch:
    """Tests for cmd_search function."""

    def test_cmd_search_no_filters(self, mock_registry, mock_category_manager, capsys):
        """Test search with no filters shows usage."""
        result = cmd_search(mock_registry, mock_category_manager)
        assert result == 1
        output = capsys.readouterr().out
        assert "Usage" in output

    def test_cmd_search_invalid_difficulty(self, mock_registry, mock_category_manager, capsys):
        """Test search with invalid difficulty returns error."""
        result = cmd_search(mock_registry, mock_category_manager, difficulty="invalid")
        assert result == 1
        output = capsys.readouterr().out
        assert "Invalid difficulty" in output

    def test_cmd_search_success(self, mock_registry, mock_category_manager, capsys):
        """Test successful search returns results."""
        result = cmd_search(mock_registry, mock_category_manager, keyword="Test")
        assert result == 0
        output = capsys.readouterr().out
        assert "Found" in output

    def test_cmd_search_no_results(self, mock_registry, mock_category_manager, capsys):
        """Test search with no results."""
        result = cmd_search(mock_registry, mock_category_manager, keyword="nonexistent")
        assert result == 0
        output = capsys.readouterr().out
        assert "No algorithms found" in output

    def test_cmd_search_usage_references_correct_module(self, mock_registry, mock_category_manager, capsys):
        """Usage text must reference python -m awesome_bioinfo, not python -m scripts."""
        cmd_search(mock_registry, mock_category_manager)
        output = capsys.readouterr().out
        assert "python -m awesome_bioinfo" in output
        assert "python -m scripts" not in output
