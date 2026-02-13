#!/usr/bin/env python3
"""
Main script to generate README.md for Awesome Bioinformatics Algorithms.
"""
import os
import sys

from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager
from scripts.readme_generator import ReadmeGenerator


def main():
    """Generate README.md from algorithm data."""
    # Paths
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    categories_path = os.path.join(base_dir, 'data', 'categories.yaml')
    algorithms_dir = os.path.join(base_dir, 'data', 'algorithms')
    template_path = os.path.join(base_dir, 'templates', 'readme_template.md')
    output_path = os.path.join(base_dir, 'README.md')

    # Load categories
    print("Loading categories...")
    category_manager = CategoryManager()
    try:
        category_manager.load_categories(categories_path)
        print(f"  Loaded {len(category_manager.list_all_categories())} categories")
    except FileNotFoundError:
        print(f"  Warning: Categories file not found at {categories_path}")
        print("  Using empty category list")

    # Load algorithms
    print("Loading algorithms...")
    registry = AlgorithmRegistry(algorithms_dir)
    registry.load_all()
    stats = registry.get_statistics()
    print(f"  Loaded {stats.total_algorithms} algorithms")
    print(f"  Categories with algorithms: {stats.total_categories}")
    print(f"  Unique tags: {stats.total_tags}")

    # Generate README
    print("Generating README...")
    generator = ReadmeGenerator(registry, category_manager, template_path)
    generator.save(output_path)
    print(f"  README saved to {output_path}")

    print("\nDone!")
    return 0


if __name__ == '__main__':
    sys.exit(main())
