"""
Data validation for Awesome Bioinformatics Algorithms.
Implements Validator class for algorithm and category validation.
"""
import os
import re
from dataclasses import dataclass, field
from typing import Any, Optional

import yaml


@dataclass
class ValidationResult:
    """Result of a validation operation."""
    is_valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def add_error(self, error: str):
        """Add an error message."""
        self.errors.append(error)
        self.is_valid = False

    def add_warning(self, warning: str):
        """Add a warning message."""
        self.warnings.append(warning)

    def merge(self, other: 'ValidationResult'):
        """Merge another validation result into this one."""
        if not other.is_valid:
            self.is_valid = False
        self.errors.extend(other.errors)
        self.warnings.extend(other.warnings)


class Validator:
    """Validates algorithm entries and categories."""

    REQUIRED_ALGORITHM_FIELDS = ['id', 'name', 'description', 'purpose', 'time_complexity', 'category']
    OPTIONAL_ALGORITHM_FIELDS = ['space_complexity', 'paper_url', 'implementation_url',
                                  'related_tools', 'tags', 'subcategory']
    REQUIRED_CATEGORY_FIELDS = ['id', 'name', 'name_en']

    MIN_DESCRIPTION_LENGTH = 50
    MAX_DESCRIPTION_LENGTH = 200

    URL_PATTERN = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE
    )

    def __init__(self, valid_categories: Optional[list[str]] = None):
        """Initialize validator with optional list of valid category IDs."""
        self.valid_categories = valid_categories or []

    def validate_algorithm(self, data: dict[str, Any]) -> ValidationResult:
        """
        Validate an algorithm entry.

        Args:
            data: Dictionary containing algorithm data

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = ValidationResult(is_valid=True)

        # Check required fields
        for field_name in self.REQUIRED_ALGORITHM_FIELDS:
            if field_name not in data:
                result.add_error(f"Missing required field: '{field_name}'")
            elif not data[field_name]:
                result.add_error(f"Required field '{field_name}' is empty")

        if not result.is_valid:
            return result

        # Validate description length
        description = data.get('description', '')
        desc_length = len(description.strip())
        if desc_length < self.MIN_DESCRIPTION_LENGTH:
            result.add_error(
                f"Description too short: {desc_length} characters "
                f"(minimum: {self.MIN_DESCRIPTION_LENGTH})"
            )
        elif desc_length > self.MAX_DESCRIPTION_LENGTH:
            result.add_error(
                f"Description too long: {desc_length} characters "
                f"(maximum: {self.MAX_DESCRIPTION_LENGTH})"
            )

        # Validate category exists (if we have a list of valid categories)
        if self.valid_categories and data.get('category') not in self.valid_categories:
            result.add_error(
                f"Invalid category: '{data.get('category')}'. "
                f"Valid categories: {', '.join(self.valid_categories)}"
            )

        # Validate URLs if provided
        for url_field in ['paper_url', 'implementation_url']:
            url = data.get(url_field, '')
            if url and not self.URL_PATTERN.match(url):
                result.add_warning(f"Invalid URL format in '{url_field}': {url}")

        # Validate tags and related_tools are lists
        if 'tags' in data and not isinstance(data['tags'], list):
            result.add_error("Field 'tags' must be a list")

        if 'related_tools' in data and not isinstance(data['related_tools'], list):
            result.add_error("Field 'related_tools' must be a list")

        return result

    def validate_category(self, data: dict[str, Any]) -> ValidationResult:
        """
        Validate a category entry.

        Args:
            data: Dictionary containing category data

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = ValidationResult(is_valid=True)

        # Check required fields
        for field_name in self.REQUIRED_CATEGORY_FIELDS:
            if field_name not in data:
                result.add_error(f"Missing required field: '{field_name}'")
            elif not data[field_name]:
                result.add_error(f"Required field '{field_name}' is empty")

        # Validate subcategories if present
        if 'subcategories' in data:
            if not isinstance(data['subcategories'], list):
                result.add_error("Field 'subcategories' must be a list")
            else:
                for i, sub in enumerate(data['subcategories']):
                    sub_result = self.validate_category(sub)
                    for error in sub_result.errors:
                        result.add_error(f"Subcategory {i}: {error}")
                    for warning in sub_result.warnings:
                        result.add_warning(f"Subcategory {i}: {warning}")

        return result

    def validate_yaml_file(self, file_path: str) -> ValidationResult:
        """
        Validate a YAML file.

        Args:
            file_path: Path to the YAML file

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = ValidationResult(is_valid=True)

        if not os.path.exists(file_path):
            result.add_error(f"File not found: {file_path}")
            return result

        try:
            with open(file_path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            result.add_error(f"YAML parsing error: {str(e)}")
            return result
        except UnicodeDecodeError as e:
            result.add_error(f"Encoding error (use UTF-8): {str(e)}")
            return result

        if data is None:
            result.add_error("Empty YAML file")
            return result

        return result

    def validate_algorithms_file(self, file_path: str) -> ValidationResult:
        """
        Validate an algorithms YAML file.

        Args:
            file_path: Path to the algorithms YAML file

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = self.validate_yaml_file(file_path)
        if not result.is_valid:
            return result

        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if 'algorithms' not in data:
            result.add_error("Missing 'algorithms' key in file")
            return result

        if not isinstance(data['algorithms'], list):
            result.add_error("'algorithms' must be a list")
            return result

        seen_ids = set()
        for i, algo in enumerate(data['algorithms']):
            algo_result = self.validate_algorithm(algo)
            for error in algo_result.errors:
                result.add_error(f"Algorithm {i} ({algo.get('id', 'unknown')}): {error}")
            for warning in algo_result.warnings:
                result.add_warning(f"Algorithm {i} ({algo.get('id', 'unknown')}): {warning}")

            # Check for duplicate IDs
            algo_id = algo.get('id')
            if algo_id:
                if algo_id in seen_ids:
                    result.add_error(f"Duplicate algorithm ID: '{algo_id}'")
                seen_ids.add(algo_id)

        return result

    def validate_categories_file(self, file_path: str) -> ValidationResult:
        """
        Validate a categories YAML file.

        Args:
            file_path: Path to the categories YAML file

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = self.validate_yaml_file(file_path)
        if not result.is_valid:
            return result

        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if 'categories' not in data:
            result.add_error("Missing 'categories' key in file")
            return result

        if not isinstance(data['categories'], list):
            result.add_error("'categories' must be a list")
            return result

        for i, cat in enumerate(data['categories']):
            cat_result = self.validate_category(cat)
            for error in cat_result.errors:
                result.add_error(f"Category {i} ({cat.get('id', 'unknown')}): {error}")
            for warning in cat_result.warnings:
                result.add_warning(f"Category {i} ({cat.get('id', 'unknown')}): {warning}")

        return result

    def validate_all(self, data_dir: str) -> ValidationResult:
        """
        Validate all data files in a directory.

        Args:
            data_dir: Path to the data directory

        Returns:
            ValidationResult with validation status and any errors/warnings
        """
        result = ValidationResult(is_valid=True)

        # Validate categories file
        categories_path = os.path.join(data_dir, 'categories.yaml')
        if os.path.exists(categories_path):
            cat_result = self.validate_categories_file(categories_path)
            result.merge(cat_result)

            # Load valid categories for algorithm validation
            with open(categories_path, encoding='utf-8') as f:
                cat_data = yaml.safe_load(f)
                if cat_data and 'categories' in cat_data:
                    self.valid_categories = self._extract_category_ids(cat_data['categories'])

        # Validate algorithm files
        algorithms_dir = os.path.join(data_dir, 'algorithms')
        if os.path.exists(algorithms_dir):
            for filename in os.listdir(algorithms_dir):
                if filename.endswith('.yaml') or filename.endswith('.yml'):
                    file_path = os.path.join(algorithms_dir, filename)
                    algo_result = self.validate_algorithms_file(file_path)
                    for error in algo_result.errors:
                        result.add_error(f"{filename}: {error}")
                    for warning in algo_result.warnings:
                        result.add_warning(f"{filename}: {warning}")

        return result

    def _extract_category_ids(self, categories: list[dict]) -> list[str]:
        """Extract all category IDs including subcategories."""
        ids = []
        for cat in categories:
            if 'id' in cat:
                ids.append(cat['id'])
            if 'subcategories' in cat:
                ids.extend(self._extract_category_ids(cat['subcategories']))
        return ids
