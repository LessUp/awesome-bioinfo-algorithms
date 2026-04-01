#!/usr/bin/env python3
"""
CLI entry point for Awesome Bioinformatics Algorithms scripts.

Usage:
    python -m scripts generate              # Generate README.md
    python -m scripts validate              # Validate all data files
    python -m scripts stats                 # Show statistics
    python -m scripts search [options]      # Search algorithms
    python -m scripts info <id>             # Show algorithm details
    python -m scripts compare <id1> <id2>   # Compare two algorithms
    python -m scripts export [options]      # Export data to JSON/CSV
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
        base_dir / "data" / "categories.yaml",
        base_dir / "data" / "algorithms",
        base_dir / "templates" / "readme_template.md",
    ]
    return [str(path) for path in required_paths if not path.exists()]


def ensure_repo_layout() -> tuple[Path, list[str]]:
    """Validate that commands are being run from a repository checkout."""
    base_dir = get_base_dir()
    return base_dir, validate_repo_layout(base_dir)


def _load_registry_and_categories(base_dir: Path) -> tuple[AlgorithmRegistry, CategoryManager]:
    """Load and return an initialized registry and category manager."""
    algorithms_dir = base_dir / "data" / "algorithms"
    categories_path = base_dir / "data" / "categories.yaml"

    category_manager = CategoryManager()
    category_manager.load_categories(str(categories_path))

    registry = AlgorithmRegistry(str(algorithms_dir))
    registry.load_all()

    return registry, category_manager


def cmd_generate(output_path: Path | None = None) -> int:
    """Generate README.md from algorithm data."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: This command must be run from an intact repository checkout.")
        print("Missing required paths:")
        for path in missing_paths:
            print(f"  - {path}")
        return 1

    data_dir = base_dir / "data"
    categories_path = base_dir / "data" / "categories.yaml"
    algorithms_dir = base_dir / "data" / "algorithms"
    template_path = base_dir / "templates" / "readme_template.md"
    output_path = output_path or (base_dir / "README.md")

    print("Validating data files...")
    validator = Validator()
    validation_result = validator.validate_all(str(data_dir))
    if validation_result.errors:
        print(
            f"  Error: Cannot generate README with {len(validation_result.errors)} validation error(s)."
        )
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

    data_dir = base_dir / "data"

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

    registry, category_manager = _load_registry_and_categories(base_dir)
    stats = registry.get_statistics()

    print("📊 Awesome Bioinformatics Algorithms - Statistics")
    print("=" * 50)
    print(f"  算法总数 (Total Algorithms): {stats.total_algorithms}")
    print(f"  有算法的分类数 (Categories with algorithms): {stats.total_categories}")
    print(f"  标签数量 (Tags):             {stats.total_tags}")
    print()
    print("📁 Algorithms per Category:")
    for cat_id, count in sorted(stats.algorithms_by_category.items()):
        cat = category_manager.get_category(cat_id)
        label = f"{cat.name} ({cat.name_en})" if cat else cat_id
        print(f"  {label}: {count}")

    return 0


def cmd_search_cli() -> int:
    """CLI wrapper for the search command."""
    from .search import cmd_search

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: must run from repository checkout.")
        return 1

    registry, category_manager = _load_registry_and_categories(base_dir)

    args = sys.argv[2:]
    keyword = tag = category = difficulty = ""
    i = 0
    while i < len(args):
        if args[i] == "--keyword" and i + 1 < len(args):
            keyword = args[i + 1]
            i += 2
        elif args[i] == "--tag" and i + 1 < len(args):
            tag = args[i + 1]
            i += 2
        elif args[i] == "--category" and i + 1 < len(args):
            category = args[i + 1]
            i += 2
        elif args[i] == "--difficulty" and i + 1 < len(args):
            difficulty = args[i + 1]
            i += 2
        else:
            if not args[i].startswith("--") and not keyword:
                keyword = args[i]
            i += 1

    return cmd_search(registry, category_manager, keyword, tag, category, difficulty)


def cmd_info_cli() -> int:
    """CLI wrapper for the info command."""
    from .info_cmd import cmd_info

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: must run from repository checkout.")
        return 1

    if len(sys.argv) < 3:
        print("Usage: python -m scripts info <algorithm-id>")
        return 1

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_info(registry, category_manager, sys.argv[2])


def cmd_compare_cli() -> int:
    """CLI wrapper for the compare command."""
    from .compare import cmd_compare

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: must run from repository checkout.")
        return 1

    if len(sys.argv) < 4:
        print("Usage: python -m scripts compare <id1> <id2>")
        return 1

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_compare(registry, category_manager, sys.argv[2], sys.argv[3])


def cmd_export_cli() -> int:
    """CLI wrapper for the export command."""
    from .export_cmd import cmd_export

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        print("Error: must run from repository checkout.")
        return 1

    registry, category_manager = _load_registry_and_categories(base_dir)

    fmt = "json"
    output = ""
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--format" and i + 1 < len(args):
            fmt = args[i + 1]
            i += 2
        elif args[i] == "--output" and i + 1 < len(args):
            output = args[i + 1]
            i += 2
        else:
            i += 1

    return cmd_export(registry, category_manager, fmt, output)


COMMANDS = {
    "generate": cmd_generate,
    "validate": cmd_validate,
    "stats": cmd_stats,
    "search": cmd_search_cli,
    "info": cmd_info_cli,
    "compare": cmd_compare_cli,
    "export": cmd_export_cli,
}

COMMAND_HELP = {
    "generate": "Generate README.md from algorithm data",
    "validate": "Validate all YAML data files",
    "stats": "Show algorithm statistics",
    "search": "Search algorithms (keyword, tag, category, difficulty)",
    "info": "Show detailed info about an algorithm",
    "compare": "Compare two algorithms side by side",
    "export": "Export algorithms to JSON or CSV",
}


def main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        if len(sys.argv) >= 2:
            print(f"Unknown command: {sys.argv[1]}")
        print("Usage: python -m scripts <command> [options]")
        print()
        print("Commands:")
        for cmd, desc in COMMAND_HELP.items():
            print(f"  {cmd:<12} {desc}")
        return 1

    return COMMANDS[sys.argv[1]]()


if __name__ == "__main__":
    sys.exit(main())
