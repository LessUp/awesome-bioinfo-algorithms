"""
Data Import/Export for Awesome Bioinformatics Algorithms.
Handles importing and exporting algorithm data in YAML and JSON formats.
"""

import json
import os
from typing import Optional

import yaml

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .schema import AlgorithmEntry, Category

YAML_DUMP_KWARGS = {
    "allow_unicode": True,
    "default_flow_style": False,
    "sort_keys": False,
}


class DataIO:
    """Handles data import and export operations."""

    def __init__(
        self,
        registry: Optional[AlgorithmRegistry] = None,
        category_manager: Optional[CategoryManager] = None,
    ):
        self._registry = registry or AlgorithmRegistry()
        self._category_manager = category_manager or CategoryManager()

    def export_data(self, output_path: str, fmt: str = "yaml") -> None:
        """
        Export all data to a file.

        Args:
            output_path: Path to save the exported data
            fmt: Export format ('yaml' or 'json')
        """
        data = {
            "categories": [cat.to_dict() for cat in self._category_manager.list_all_categories()],
            "algorithms": [algo.to_dict() for algo in self._registry.get_all_algorithms()],
        }

        with open(output_path, "w", encoding="utf-8") as f:
            if fmt.lower() == "json":
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                yaml.safe_dump(data, f, **YAML_DUMP_KWARGS)

    def import_data(self, input_path: str) -> tuple[list[Category], list[AlgorithmEntry]]:
        """
        Import data from a file.

        Args:
            input_path: Path to the data file

        Returns:
            Tuple of (categories, algorithms)
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Data file not found: {input_path}")

        with open(input_path, encoding="utf-8") as f:
            if input_path.endswith(".json"):
                data = json.load(f)
            else:
                data = yaml.safe_load(f)

        categories = []
        algorithms = []

        if data:
            if "categories" in data:
                categories = [Category.from_dict(cat) for cat in data["categories"]]
            if "algorithms" in data:
                algorithms = [AlgorithmEntry.from_dict(algo) for algo in data["algorithms"]]

        return categories, algorithms

    def import_and_load(self, input_path: str) -> tuple[CategoryManager, AlgorithmRegistry]:
        """
        Import data and load into managers.

        Args:
            input_path: Path to the data file

        Returns:
            Tuple of (CategoryManager, AlgorithmRegistry)
        """
        categories, algorithms = self.import_data(input_path)

        self._category_manager.from_categories(categories)
        self._registry.from_algorithms(algorithms)

        return self._category_manager, self._registry

    def export_categories(self, output_path: str, fmt: str = "yaml") -> None:
        """Export only categories to a file."""
        data = {
            "categories": [cat.to_dict() for cat in self._category_manager.list_all_categories()]
        }

        with open(output_path, "w", encoding="utf-8") as f:
            if fmt.lower() == "json":
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                yaml.safe_dump(data, f, **YAML_DUMP_KWARGS)

    def export_algorithms(self, output_path: str, fmt: str = "yaml") -> None:
        """Export only algorithms to a file."""
        data = {"algorithms": [algo.to_dict() for algo in self._registry.get_all_algorithms()]}

        with open(output_path, "w", encoding="utf-8") as f:
            if fmt.lower() == "json":
                json.dump(data, f, ensure_ascii=False, indent=2)
            else:
                yaml.safe_dump(data, f, **YAML_DUMP_KWARGS)

    @staticmethod
    def export_to_dict(categories: list[Category], algorithms: list[AlgorithmEntry]) -> dict:
        """
        Convert categories and algorithms to a dictionary.

        Args:
            categories: List of Category objects
            algorithms: List of AlgorithmEntry objects

        Returns:
            Dictionary representation
        """
        return {
            "categories": [cat.to_dict() for cat in categories],
            "algorithms": [algo.to_dict() for algo in algorithms],
        }

    @staticmethod
    def import_from_dict(data: dict) -> tuple[list[Category], list[AlgorithmEntry]]:
        """
        Import categories and algorithms from a dictionary.

        Args:
            data: Dictionary with 'categories' and 'algorithms' keys

        Returns:
            Tuple of (categories, algorithms)
        """
        categories = []
        algorithms = []

        if data:
            if "categories" in data:
                categories = [Category.from_dict(cat) for cat in data["categories"]]
            if "algorithms" in data:
                algorithms = [AlgorithmEntry.from_dict(algo) for algo in data["algorithms"]]

        return categories, algorithms
