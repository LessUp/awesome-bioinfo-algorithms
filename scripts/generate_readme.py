#!/usr/bin/env python3
"""
Main script to generate README.md for Awesome Bioinformatics Algorithms.

Usage:
    python -m scripts.generate_readme
    python scripts/generate_readme.py
"""
import os
import sys
from pathlib import Path

# Support both `python -m scripts.generate_readme` and `python scripts/generate_readme.py`
try:
    from .algorithm_registry import AlgorithmRegistry
    from .category_manager import CategoryManager
    from .readme_generator import ReadmeGenerator
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from scripts.algorithm_registry import AlgorithmRegistry
    from scripts.category_manager import CategoryManager
    from scripts.readme_generator import ReadmeGenerator


def main():
    """Generate README.md from algorithm data."""
    # Paths
    base_dir = Path(__file__).resolve().parent.parent
    categories_path = base_dir / 'data' / 'categories.yaml'
    algorithms_dir = base_dir / 'data' / 'algorithms'
    template_path = base_dir / 'templates' / 'readme_template.md'
    output_path = base_dir / 'README.md'

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
