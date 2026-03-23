#!/usr/bin/env python3
"""
CLI entry point for Awesome Bioinformatics Algorithms scripts.

Usage:
    python -m scripts generate    # Generate README.md
    python -m scripts validate    # Validate all data files
    python -m scripts stats       # Show statistics
"""
import sys
from pathlib import Path

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .readme_generator import ReadmeGenerator
from .validate import Validator


def get_base_dir() -> Path:
    """Return the project root directory for a repository checkout."""
    return Path(__file__).resolve().parent.parent


def validate_repo_layout(base_dir: Path) -> list[str]:
    """Return missing repository paths required by the maintenance CLI."""
    required_paths = [
        base_dir / 'data' / 'categories.yaml',
        base_dir / 'data' / 'algorithms',
        base_dir / 'templates' / 'readme_template.md',
    ]
    return [str(path) for path in required_paths if not path.exists()]


def ensure_repo_layout() -> tuple[Path, list[str]]:
    """Validate that commands are being run from a repository checkout."""
    base_dir = get_base_dir()
    return base_dir, validate_repo_layout(base_dir)


def cmd_generate() -> int:
    """Generate README.md from algorithm data."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: This command must be run from an intact repository checkout.")
        print("Missing required paths:")
        for path in missing_paths:
            print(f"  - {path}")
        return 1

    data_dir = base_dir / 'data'
    categories_path = base_dir / 'data' / 'categories.yaml'
    algorithms_dir = base_dir / 'data' / 'algorithms'
    template_path = base_dir / 'templates' / 'readme_template.md'
    output_path = base_dir / 'README.md'

    print("Validating data files...")
    validator = Validator()
    validation_result = validator.validate_all(str(data_dir))
    if validation_result.errors:
        print(f"  Error: Cannot generate README with {len(validation_result.errors)} validation error(s).")
        for error in validation_result.errors:
            print(f"    - {error}")
        return 1

    if validation_result.warnings:
        print(f"  Warning: {len(validation_result.warnings)} validation warning(s) detected.")
        for warning in validation_result.warnings:
            print(f"    - {warning}")

    print("Loading categories...")
    category_manager = CategoryManager()
    try:
        category_manager.load_categories(str(categories_path))
        print(f"  Loaded {len(category_manager.list_all_categories())} categories")
    except FileNotFoundError:
        print(f"  Warning: Categories file not found at {categories_path}")

    print("Loading algorithms...")
    registry = AlgorithmRegistry(str(algorithms_dir))
    try:
        registry.load_all()
    except ValueError as exc:
        print(f"  Error: {exc}")
        return 1
    stats = registry.get_statistics()
    print(f"  Loaded {stats.total_algorithms} algorithms")
    print(f"  Categories with algorithms: {stats.total_categories}")
    print(f"  Unique tags: {stats.total_tags}")

    print("Generating README...")
    generator = ReadmeGenerator(registry, category_manager, str(template_path))
    generator.save(str(output_path))
    print(f"  README saved to {output_path}")
    print("\nDone!")
    return 0


def cmd_validate() -> int:
    """Validate all data files."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: This command must be run from an intact repository checkout.")
        print("Missing required paths:")
        for path in missing_paths:
            print(f"  - {path}")
        return 1

    data_dir = base_dir / 'data'

    print("Validating data files...")
    validator = Validator()
    result = validator.validate_all(str(data_dir))

    if result.errors:
        print(f"\n❌ {len(result.errors)} error(s):")
        for error in result.errors:
            print(f"  - {error}")

    if result.warnings:
        print(f"\n⚠️  {len(result.warnings)} warning(s):")
        for warning in result.warnings:
            print(f"  - {warning}")

    if result.is_valid:
        print("\n✅ All data files are valid!")
        return 0
    else:
        print("\n❌ Validation failed.")
        return 1


def cmd_stats() -> int:
    """Show statistics about the algorithm registry."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: This command must be run from an intact repository checkout.")
        print("Missing required paths:")
        for path in missing_paths:
            print(f"  - {path}")
        return 1

    algorithms_dir = base_dir / 'data' / 'algorithms'
    categories_path = base_dir / 'data' / 'categories.yaml'

    category_manager = CategoryManager()
    category_manager.load_categories(str(categories_path))

    registry = AlgorithmRegistry(str(algorithms_dir))
    try:
        registry.load_all()
    except ValueError as exc:
        print(f"Error: {exc}")
        return 1
    stats = registry.get_statistics()

    print("📊 Awesome Bioinformatics Algorithms - Statistics")
    print("=" * 50)
    print(f"  算法总数 (Total Algorithms): {stats.total_algorithms}")
    print(f"  分类数量 (Categories):       {stats.total_categories}")
    print(f"  标签数量 (Tags):             {stats.total_tags}")
    print()
    print("📁 Algorithms per Category:")
    for cat_id, count in sorted(stats.algorithms_by_category.items()):
        cat = category_manager.get_category(cat_id)
        label = f"{cat.name} ({cat.name_en})" if cat else cat_id
        print(f"  {label}: {count}")

    return 0


COMMANDS = {
    'generate': cmd_generate,
    'validate': cmd_validate,
    'stats': cmd_stats,
}


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python -m scripts <command>")
        print(f"Commands: {', '.join(COMMANDS.keys())}")
        return 1

    command = sys.argv[1]
    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        print(f"Commands: {', '.join(COMMANDS.keys())}")
        return 1

    return COMMANDS[command]()


if __name__ == '__main__':
    sys.exit(main())
