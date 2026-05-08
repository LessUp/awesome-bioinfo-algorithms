"""
DataStore facade for Awesome Bioinformatics Algorithms.
Provides a unified interface for loading and accessing algorithm data.
"""

from pathlib import Path
from typing import Optional

from .algorithm_registry import AlgorithmRegistry, RegistryStats
from .category_manager import CategoryManager
from .schema import AlgorithmEntry, Category
from .validate import FieldValidator, ValidationResult


class DataStore:
    """
    Unified facade for algorithm data access.
    Manages AlgorithmRegistry and CategoryManager with automatic coordination.
    """

    def __init__(self, base_dir: Optional[Path] = None):
        """
        Initialize DataStore with optional base directory.

        Args:
            base_dir: Project root directory. If None, uses current working directory.
        """
        self._base_dir = base_dir or Path.cwd()
        self._registry: Optional[AlgorithmRegistry] = None
        self._category_manager: Optional[CategoryManager] = None
        self._field_validator: Optional[FieldValidator] = None

    @property
    def base_dir(self) -> Path:
        """Get the base directory."""
        return self._base_dir

    @property
    def algorithms_dir(self) -> Path:
        """Get the algorithms data directory."""
        return self._base_dir / "data" / "algorithms"

    @property
    def categories_path(self) -> Path:
        """Get the categories YAML file path."""
        return self._base_dir / "data" / "categories.yaml"

    @property
    def registry(self) -> AlgorithmRegistry:
        """Get the algorithm registry (lazy-loaded)."""
        if self._registry is None:
            self._registry = AlgorithmRegistry(str(self.algorithms_dir))
            self._registry.load_all()
        return self._registry

    @property
    def category_manager(self) -> CategoryManager:
        """Get the category manager (lazy-loaded)."""
        if self._category_manager is None:
            self._category_manager = CategoryManager()
            if self.categories_path.exists():
                self._category_manager.load_categories(str(self.categories_path))
        return self._category_manager

    @property
    def field_validator(self) -> FieldValidator:
        """Get the field validator (singleton)."""
        if self._field_validator is None:
            self._field_validator = FieldValidator()
        return self._field_validator

    def load_all(self) -> "DataStore":
        """
        Load both algorithms and categories.
        Returns self for method chaining.

        Raises:
            FileNotFoundError: If required data files are missing
            ValueError: If data loading fails
        """
        self._registry = AlgorithmRegistry(str(self.algorithms_dir))
        self._registry.load_all()

        self._category_manager = CategoryManager()
        if self.categories_path.exists():
            self._category_manager.load_categories(str(self.categories_path))

        return self

    def is_loaded(self) -> bool:
        """Check if data has been loaded."""
        return self._registry is not None and self._category_manager is not None

    def validate_layout(self) -> list[str]:
        """
        Validate that required repository paths exist.

        Returns:
            List of missing paths (empty if all valid)
        """
        missing = []
        if not self.categories_path.exists():
            missing.append(str(self.categories_path))
        if not self.algorithms_dir.exists():
            missing.append(str(self.algorithms_dir))
        return missing

    # =========================================================================
    # Algorithm accessors (delegate to registry)
    # =========================================================================

    def get_algorithm(self, algo_id: str) -> Optional[AlgorithmEntry]:
        """Get an algorithm by ID."""
        return self.registry.get_algorithm(algo_id)

    def get_all_algorithms(self) -> list[AlgorithmEntry]:
        """Get all algorithms."""
        return self.registry.get_all_algorithms()

    def search_algorithms(self, keyword: str) -> list[AlgorithmEntry]:
        """Search algorithms by keyword."""
        return self.registry.search(keyword)

    def get_algorithms_by_category(self, category_id: str) -> list[AlgorithmEntry]:
        """Get algorithms in a category."""
        return self.registry.get_by_category(category_id)

    def get_algorithms_by_tag(self, tag: str) -> list[AlgorithmEntry]:
        """Get algorithms with a specific tag."""
        return self.registry.get_by_tag(tag)

    def get_statistics(self) -> RegistryStats:
        """Get registry statistics."""
        return self.registry.get_statistics()

    # =========================================================================
    # Category accessors (delegate to category_manager)
    # =========================================================================

    def get_category(self, category_id: str) -> Optional[Category]:
        """Get a category by ID."""
        return self.category_manager.get_category(category_id)

    def get_all_categories(self) -> list[Category]:
        """Get all categories."""
        return self.category_manager.list_all_categories()

    def category_exists(self, category_id: str) -> bool:
        """Check if a category exists."""
        return self.category_manager.category_exists(category_id)

    # =========================================================================
    # Validation (coordinate between field_validator and category_manager)
    # =========================================================================

    def validate_algorithm_fields(self, data: dict) -> ValidationResult:
        """Validate algorithm field formats."""
        return self.field_validator.validate_algorithm_fields(data)

    def validate_category_reference(
        self, category: str, subcategory: str = ""
    ) -> ValidationResult:
        """Validate a category/subcategory reference."""
        return self.category_manager.validate_category_reference(category, subcategory)

    def validate_algorithm_full(self, data: dict) -> ValidationResult:
        """
        Validate algorithm fields and category reference together.
        Combines field validation with category relationship validation.
        """
        result = self.field_validator.validate_algorithm_fields(data)

        category = data.get("category", "")
        subcategory = data.get("subcategory", "")

        if category:
            cat_result = self.category_manager.validate_category_reference(
                category, subcategory
            )
            result.merge(cat_result)

        return result

    # =========================================================================
    # Factory methods for CLI commands
    # =========================================================================

    @classmethod
    def from_path(cls, path: Path) -> "DataStore":
        """
        Create a DataStore from a specific path.

        Args:
            path: Base directory path

        Returns:
            Loaded DataStore instance
        """
        return cls(path).load_all()

    @classmethod
    def from_cwd(cls) -> "DataStore":
        """
        Create a DataStore from current working directory.

        Returns:
            Loaded DataStore instance
        """
        return cls().load_all()
