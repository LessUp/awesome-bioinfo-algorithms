"""
Category Manager for Awesome Bioinformatics Algorithms.
Manages algorithm categories and subcategories.
"""
import os
from typing import Optional

import yaml

from .schema import Category


class CategoryManager:
    """Manages algorithm categories loaded from YAML files."""

    def __init__(self):
        self._categories: list[Category] = []
        self._category_map: dict[str, Category] = {}

    def load_categories(self, path: str) -> list[Category]:
        """
        Load categories from a YAML file.

        Args:
            path: Path to the categories YAML file

        Returns:
            List of Category objects
        """
        if not os.path.exists(path):
            raise FileNotFoundError(f"Categories file not found: {path}")

        with open(path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data or 'categories' not in data:
            return []

        self._categories = []
        self._category_map = {}

        for cat_data in data['categories']:
            category = Category.from_dict(cat_data)
            self._categories.append(category)
            self._register_category(category)

        return self._categories

    def _register_category(self, category: Category):
        """Register a category and its subcategories in the lookup map."""
        self._category_map[category.id] = category
        for sub in category.subcategories:
            self._register_category(sub)

    def get_category(self, category_id: str) -> Optional[Category]:
        """
        Get a category by its ID.

        Args:
            category_id: The category ID to look up

        Returns:
            Category object or None if not found
        """
        return self._category_map.get(category_id)

    def list_all_categories(self) -> list[Category]:
        """
        List all top-level categories.

        Returns:
            List of top-level Category objects
        """
        return self._categories.copy()

    def list_all_category_ids(self) -> list[str]:
        """
        List all category IDs including subcategories.

        Returns:
            List of all category IDs
        """
        return list(self._category_map.keys())

    def get_subcategories(self, category_id: str) -> list[Category]:
        """
        Get subcategories of a category.

        Args:
            category_id: The parent category ID

        Returns:
            List of subcategory objects
        """
        category = self.get_category(category_id)
        if category:
            return category.subcategories.copy()
        return []

    def get_parent_category(self, category_id: str) -> Optional[Category]:
        """
        Get the parent category of a subcategory.

        Args:
            category_id: The subcategory ID

        Returns:
            Parent Category object or None
        """
        category = self.get_category(category_id)
        if category and category.parent_id:
            return self.get_category(category.parent_id)
        return None

    def category_exists(self, category_id: str) -> bool:
        """Check if a category ID exists."""
        return category_id in self._category_map

    def to_dict(self) -> dict:
        """Convert all categories to dictionary for serialization."""
        return {
            'categories': [cat.to_dict() for cat in self._categories]
        }

    def from_categories(self, categories: list[Category]):
        """Load categories from a list of Category objects."""
        self._categories = categories
        self._category_map = {}
        for cat in categories:
            self._register_category(cat)
