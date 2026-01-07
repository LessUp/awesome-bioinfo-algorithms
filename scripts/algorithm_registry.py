"""
Algorithm Registry for Awesome Bioinformatics Algorithms.
Manages loading, searching, and organizing algorithm entries.
"""
import glob
import os
from dataclasses import dataclass
from typing import Optional

import yaml

from .schema import AlgorithmEntry
from .validate import ValidationResult, Validator


@dataclass
class RegistryStats:
    """Statistics about the algorithm registry."""
    total_algorithms: int
    total_categories: int
    total_tags: int
    algorithms_by_category: dict[str, int]


class AlgorithmRegistry:
    """Manages all algorithm entries loaded from YAML files."""

    def __init__(self, data_dir: str = "data/algorithms"):
        self._data_dir = data_dir
        self._algorithms: list[AlgorithmEntry] = []
        self._by_category: dict[str, list[AlgorithmEntry]] = {}
        self._by_tag: dict[str, list[AlgorithmEntry]] = {}
        self._by_id: dict[str, AlgorithmEntry] = {}
        self._validator = Validator()

    def load_all(self) -> list[AlgorithmEntry]:
        """
        Load all algorithms from YAML files in the data directory.

        Returns:
            List of AlgorithmEntry objects
        """
        self._algorithms = []
        self._by_category = {}
        self._by_tag = {}
        self._by_id = {}

        if not os.path.exists(self._data_dir):
            return []

        yaml_files = glob.glob(os.path.join(self._data_dir, "*.yaml"))
        yaml_files.extend(glob.glob(os.path.join(self._data_dir, "*.yml")))

        for yaml_file in yaml_files:
            self._load_file(yaml_file)

        return self._algorithms

    def _load_file(self, path: str):
        """Load algorithms from a single YAML file."""
        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data or 'algorithms' not in data:
            return

        for algo_data in data['algorithms']:
            algo = AlgorithmEntry.from_dict(algo_data)
            self._register_algorithm(algo)

    def _register_algorithm(self, algo: AlgorithmEntry):
        """Register an algorithm in all lookup structures."""
        self._algorithms.append(algo)
        self._by_id[algo.id] = algo

        # Register by category
        if algo.category not in self._by_category:
            self._by_category[algo.category] = []
        self._by_category[algo.category].append(algo)

        # Register by tags
        for tag in algo.tags:
            if tag not in self._by_tag:
                self._by_tag[tag] = []
            self._by_tag[tag].append(algo)

    def get_by_category(self, category_id: str) -> list[AlgorithmEntry]:
        """
        Get all algorithms in a category.

        Args:
            category_id: The category ID to filter by

        Returns:
            List of algorithms in the category
        """
        return self._by_category.get(category_id, []).copy()

    def get_by_tag(self, tag: str) -> list[AlgorithmEntry]:
        """
        Get all algorithms with a specific tag.

        Args:
            tag: The tag to filter by

        Returns:
            List of algorithms with the tag
        """
        return self._by_tag.get(tag, []).copy()

    def search(self, keyword: str) -> list[AlgorithmEntry]:
        """
        Search algorithms by keyword in name, description, or tags.

        Args:
            keyword: Search keyword (case-insensitive)

        Returns:
            List of matching algorithms
        """
        keyword_lower = keyword.lower()
        results = []

        for algo in self._algorithms:
            if (keyword_lower in algo.name.lower() or
                keyword_lower in algo.description.lower() or
                any(keyword_lower in tag.lower() for tag in algo.tags)):
                results.append(algo)

        return results

    def get_algorithm(self, algo_id: str) -> Optional[AlgorithmEntry]:
        """Get an algorithm by its ID."""
        return self._by_id.get(algo_id)

    def validate_entry(self, entry: dict) -> ValidationResult:
        """Validate an algorithm entry dictionary."""
        return self._validator.validate_algorithm(entry)

    def get_statistics(self) -> RegistryStats:
        """
        Get statistics about the registry.

        Returns:
            RegistryStats object with counts
        """
        all_tags = set()
        for algo in self._algorithms:
            all_tags.update(algo.tags)

        return RegistryStats(
            total_algorithms=len(self._algorithms),
            total_categories=len(self._by_category),
            total_tags=len(all_tags),
            algorithms_by_category={
                cat: len(algos) for cat, algos in self._by_category.items()
            }
        )

    def get_all_algorithms(self) -> list[AlgorithmEntry]:
        """Get all loaded algorithms."""
        return self._algorithms.copy()

    def get_all_tags(self) -> list[str]:
        """Get all unique tags."""
        return list(self._by_tag.keys())

    def get_all_categories(self) -> list[str]:
        """Get all category IDs that have algorithms."""
        return list(self._by_category.keys())

    def from_algorithms(self, algorithms: list[AlgorithmEntry]):
        """Load algorithms from a list of AlgorithmEntry objects."""
        self._algorithms = []
        self._by_category = {}
        self._by_tag = {}
        self._by_id = {}

        for algo in algorithms:
            self._register_algorithm(algo)

    def to_dict(self) -> dict:
        """Convert all algorithms to dictionary for serialization."""
        return {
            'algorithms': [algo.to_dict() for algo in self._algorithms]
        }
