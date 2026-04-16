"""Tests for the info command module."""

import pytest

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager
from scripts.info_cmd import cmd_info
from scripts.schema import AlgorithmEntry, Category


@pytest.fixture
def mock_category_manager():
    """Create a mock category manager."""
    manager = CategoryManager()
    # Use from_categories to properly register categories
    manager.from_categories([
        Category(
            id="test-cat",
            name="测试分类",
            name_en="Test Category",
            description="A test category",
            subcategories=[
                Category(
                    id="test-sub",
                    name="测试子分类",
                    name_en="Test Subcategory",
                    description="A test subcategory",
                    parent_id="test-cat",
                )
            ],
        ),
    ])
    return manager


@pytest.fixture
def mock_registry():
    """Create a mock registry with sample algorithms."""
    registry = AlgorithmRegistry()
    registry.from_algorithms([
        AlgorithmEntry(
            id="test-algo",
            name="Test Algorithm",
            description="A test algorithm description that meets the minimum length requirement for validation purposes in our testing framework.",
            purpose="Testing purposes",
            time_complexity="O(n)",
            space_complexity="O(1)",
            category="test-cat",
            subcategory="test-sub",
            year=2020,
            difficulty="beginner",
            paper_url="https://example.com/paper",
            implementation_url="https://github.com/example/repo",
            related_tools=["Tool1", "Tool2"],
            tags=["test", "unit"],
            language=["Python"],
        ),
        AlgorithmEntry(
            id="simple-algo",
            name="Simple Algorithm",
            description="A simple algorithm for testing basic functionality without extra fields.",
            purpose="Simplicity testing",
            time_complexity="O(1)",
            category="test-cat",
        ),
    ])
    return registry


class TestCmdInfo:
    """Tests for cmd_info function."""

    def test_info_by_exact_id(self, mock_registry, mock_category_manager, capsys):
        """Test info command with exact ID match."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "Test Algorithm" in output
        assert "test-algo" in output

    def test_info_shows_year(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows year when present."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "(2020)" in output

    def test_info_shows_category(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows category with names."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "测试分类" in output
        assert "Test Category" in output

    def test_info_shows_subcategory(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows subcategory when present."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "测试子分类" in output

    def test_info_shows_difficulty(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows difficulty when present."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "入门" in output or "Beginner" in output

    def test_info_shows_complexity(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows time and space complexity."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "O(n)" in output
        assert "O(1)" in output

    def test_info_shows_urls(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows paper and implementation URLs."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "https://example.com/paper" in output
        assert "https://github.com/example/repo" in output

    def test_info_shows_related_tools(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows related tools."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "Tool1" in output
        assert "Tool2" in output

    def test_info_shows_tags(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows tags."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "test" in output

    def test_info_shows_language(self, mock_registry, mock_category_manager, capsys):
        """Test info command shows programming language."""
        result = cmd_info(mock_registry, mock_category_manager, "test-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "Python" in output

    def test_info_not_found(self, mock_registry, mock_category_manager, capsys):
        """Test info command with non-existent ID."""
        result = cmd_info(mock_registry, mock_category_manager, "nonexistent")
        assert result == 1
        output = capsys.readouterr().out
        assert "not found" in output

    def test_info_fuzzy_match_single(self, mock_registry, mock_category_manager, capsys):
        """Test info command with fuzzy match returning single result."""
        result = cmd_info(mock_registry, mock_category_manager, "simple")
        assert result == 0
        output = capsys.readouterr().out
        assert "Simple Algorithm" in output

    def test_info_fuzzy_match_multiple(self, mock_registry, mock_category_manager, capsys):
        """Test info command with fuzzy match returning multiple results."""
        result = cmd_info(mock_registry, mock_category_manager, "test")
        assert result == 1
        output = capsys.readouterr().out
        assert "Multiple matches" in output

    def test_info_simple_algorithm(self, mock_registry, mock_category_manager, capsys):
        """Test info command with algorithm having minimal fields."""
        result = cmd_info(mock_registry, mock_category_manager, "simple-algo")
        assert result == 0
        output = capsys.readouterr().out
        assert "Simple Algorithm" in output
        assert "O(1)" in output
