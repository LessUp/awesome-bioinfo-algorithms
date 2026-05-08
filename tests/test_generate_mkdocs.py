"""Tests for generate_mkdocs module."""

import tempfile
from pathlib import Path

import pytest

from awesome_bioinfo.generate_mkdocs import (
    get_base_dir,
    get_difficulty_badge_class,
    load_data,
    trim_text,
    write_file,
)
from awesome_bioinfo.schema import AlgorithmEntry, Category


class TestUtilityFunctions:
    """Test utility functions in generate_mkdocs."""

    def test_trim_text_short(self) -> None:
        """trim_text should return short text unchanged."""
        assert trim_text("hello", 10) == "hello"

    def test_trim_text_exact(self) -> None:
        """trim_text should return text at exact limit unchanged."""
        assert trim_text("hello", 5) == "hello"

    def test_trim_text_long(self) -> None:
        """trim_text should truncate long text with ellipsis."""
        result = trim_text("hello world this is a test", 10)
        assert result == "hello wor…"
        assert len(result) == 10

    def test_trim_text_default_limit(self) -> None:
        """trim_text should use default limit of 80."""
        long_text = "x" * 100
        result = trim_text(long_text)
        assert len(result) == 80
        assert result.endswith("…")

    def test_get_difficulty_badge_class_beginner(self) -> None:
        """Beginner difficulty should return green badge class."""
        assert get_difficulty_badge_class("beginner") == "aba-badge-difficulty-beginner"

    def test_get_difficulty_badge_class_intermediate(self) -> None:
        """Intermediate difficulty should return yellow badge class."""
        assert get_difficulty_badge_class("intermediate") == "aba-badge-difficulty-intermediate"

    def test_get_difficulty_badge_class_advanced(self) -> None:
        """Advanced difficulty should return red badge class."""
        assert get_difficulty_badge_class("advanced") == "aba-badge-difficulty-advanced"

    def test_get_difficulty_badge_class_unknown(self) -> None:
        """Unknown difficulty should return empty class."""
        assert get_difficulty_badge_class("unknown") == ""

    def test_get_difficulty_badge_class_empty(self) -> None:
        """Empty difficulty should return empty class."""
        assert get_difficulty_badge_class("") == ""


class TestWriteFile:
    """Test write_file function."""

    def test_write_file_creates_directory(self, tmp_path: Path) -> None:
        """write_file should create parent directories."""
        file_path = tmp_path / "subdir" / "test.md"
        write_file(file_path, "test content")
        assert file_path.exists()
        assert file_path.read_text() == "test content"

    def test_write_file_overwrites(self, tmp_path: Path) -> None:
        """write_file should overwrite existing files."""
        file_path = tmp_path / "test.md"
        write_file(file_path, "original")
        write_file(file_path, "new content")
        assert file_path.read_text() == "new content"

    def test_write_file_utf8(self, tmp_path: Path) -> None:
        """write_file should handle UTF-8 content."""
        file_path = tmp_path / "test.md"
        write_file(file_path, "中文内容 test émojis 🧬")
        assert file_path.read_text() == "中文内容 test émojis 🧬"


class TestLoadData:
    """Test load_data function."""

    def test_load_data_returns_tuple(self) -> None:
        """load_data should return tuple of categories and algorithms."""
        base_dir = get_base_dir()
        categories, algorithms = load_data(base_dir)
        assert isinstance(categories, list)
        assert isinstance(algorithms, list)

    def test_load_data_categories_structure(self) -> None:
        """load_data should return Category objects."""
        base_dir = get_base_dir()
        categories, _ = load_data(base_dir)
        assert len(categories) > 0
        for cat in categories:
            assert isinstance(cat, Category)
            assert cat.id
            assert cat.name

    def test_load_data_algorithms_structure(self) -> None:
        """load_data should return AlgorithmEntry objects."""
        base_dir = get_base_dir()
        _, algorithms = load_data(base_dir)
        assert len(algorithms) > 0
        for algo in algorithms:
            assert isinstance(algo, AlgorithmEntry)
            assert algo.id
            assert algo.name
            assert algo.category

    def test_load_data_file_not_found(self) -> None:
        """load_data should raise FileNotFoundError for missing data dir."""
        with tempfile.TemporaryDirectory() as tmpdir:
            empty_dir = Path(tmpdir)
            with pytest.raises(FileNotFoundError):
                load_data(empty_dir)


class TestGetBaseDir:
    """Test get_base_dir function."""

    def test_get_base_dir_returns_path(self) -> None:
        """get_base_dir should return a Path object."""
        result = get_base_dir()
        assert isinstance(result, Path)

    def test_get_base_dir_contains_data(self) -> None:
        """get_base_dir should point to project root with data directory."""
        result = get_base_dir()
        assert (result / "data").exists()
        assert (result / "awesome_bioinfo").exists()
