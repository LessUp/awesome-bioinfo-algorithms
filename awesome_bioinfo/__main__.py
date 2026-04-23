#!/usr/bin/env python3
"""
CLI entry point for Awesome Bioinformatics Algorithms scripts.

Usage:
    python -m awesome_bioinfo generate                     # Generate README.md
    python -m awesome_bioinfo validate                     # Validate all data files
    python -m awesome_bioinfo stats                        # Show statistics
    python -m awesome_bioinfo search [options]             # Search algorithms
    python -m awesome_bioinfo info <id>                    # Show algorithm details
    python -m awesome_bioinfo compare <id1> <id2>          # Compare two algorithms
    python -m awesome_bioinfo export [options]             # Export data to JSON/CSV
    python -m awesome_bioinfo mkdocs                       # Generate MkDocs pages
"""

import argparse
import sys
from pathlib import Path
from typing import Optional

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


def _print_repo_layout_error(missing_paths: list[str]) -> int:
    print("Error: This command must be run from an intact repository checkout.")
    print("Missing required paths:")
    for path in missing_paths:
        print(f"  - {path}")
    return 1


def _load_registry_and_categories(base_dir: Path) -> tuple[AlgorithmRegistry, CategoryManager]:
    """Load and return an initialized registry and category manager."""
    algorithms_dir = base_dir / "data" / "algorithms"
    categories_path = base_dir / "data" / "categories.yaml"

    category_manager = CategoryManager()
    category_manager.load_categories(str(categories_path))

    registry = AlgorithmRegistry(str(algorithms_dir))
    registry.load_all()

    return registry, category_manager


def cmd_generate(output_path: Optional[Path] = None) -> int:
    """Generate README.md from algorithm data."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

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
        return _print_repo_layout_error(missing_paths)

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

    print("\n❌ Validation failed.")
    return 1


def cmd_stats() -> int:
    """Show statistics about the algorithm registry."""
    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

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


def cmd_search_cli(
    *,
    keyword: str = "",
    tag: str = "",
    category: str = "",
    difficulty: str = "",
) -> int:
    """CLI wrapper for the search command."""
    from .search import cmd_search

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_search(registry, category_manager, keyword, tag, category, difficulty)


def cmd_info_cli(algo_id: str) -> int:
    """CLI wrapper for the info command."""
    from .info_cmd import cmd_info

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_info(registry, category_manager, algo_id)


def cmd_compare_cli(id1: str, id2: str) -> int:
    """CLI wrapper for the compare command."""
    from .compare import cmd_compare

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_compare(registry, category_manager, id1, id2)


def cmd_export_cli(*, fmt: str = "json", output: str = "") -> int:
    """CLI wrapper for the export command."""
    from .export_cmd import cmd_export

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    registry, category_manager = _load_registry_and_categories(base_dir)
    return cmd_export(registry, category_manager, fmt, output)


def cmd_mkdocs() -> int:
    """Generate MkDocs pages."""
    from .generate_mkdocs import main as generate_mkdocs_main

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    return generate_mkdocs_main(base_dir)


def cmd_check_links() -> int:
    """Check validity of algorithm URLs."""
    from .link_checker import cmd_check_links as _cmd_check_links

    base_dir, missing_paths = ensure_repo_layout()
    if missing_paths:
        return _print_repo_layout_error(missing_paths)

    return _cmd_check_links()


def build_parser() -> argparse.ArgumentParser:
    """Build the top-level CLI parser."""
    parser = argparse.ArgumentParser(prog="python -m awesome_bioinfo")
    subparsers = parser.add_subparsers(dest="command")

    generate_parser = subparsers.add_parser(
        "generate", help="Generate README.md from algorithm data"
    )
    generate_parser.add_argument("--output", type=Path, help="Write README output to a custom path")

    subparsers.add_parser("validate", help="Validate all YAML data files")
    subparsers.add_parser("stats", help="Show algorithm statistics")

    search_parser = subparsers.add_parser(
        "search", help="Search algorithms (keyword, tag, category, difficulty)"
    )
    search_parser.add_argument("keyword", nargs="?", default="", help="Keyword to search for")
    search_parser.add_argument(
        "--keyword", dest="keyword_flag", default="", help="Keyword to search for"
    )
    search_parser.add_argument("--tag", default="", help="Filter by tag")
    search_parser.add_argument(
        "--category", default="", help="Filter by category or subcategory ID"
    )
    search_parser.add_argument(
        "--difficulty",
        default="",
        help="Filter by difficulty (beginner/intermediate/advanced)",
    )

    info_parser = subparsers.add_parser("info", help="Show detailed info about an algorithm")
    info_parser.add_argument("algo_id", help="Algorithm ID or fuzzy keyword")

    compare_parser = subparsers.add_parser("compare", help="Compare two algorithms side by side")
    compare_parser.add_argument("id1", help="First algorithm ID or fuzzy keyword")
    compare_parser.add_argument("id2", help="Second algorithm ID or fuzzy keyword")

    export_parser = subparsers.add_parser("export", help="Export algorithms to JSON or CSV")
    export_parser.add_argument(
        "--format", dest="fmt", default="json", help="Export format: json or csv"
    )
    export_parser.add_argument("--output", default="", help="Write export output to a file")

    subparsers.add_parser("mkdocs", help="Generate MkDocs pages")

    subparsers.add_parser("check-links", help="Check validity of algorithm URLs")

    return parser


def main(argv: Optional[list[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "generate":
        return cmd_generate(output_path=args.output)
    if args.command == "validate":
        return cmd_validate()
    if args.command == "stats":
        return cmd_stats()
    if args.command == "search":
        keyword = args.keyword_flag or args.keyword
        return cmd_search_cli(
            keyword=keyword,
            tag=args.tag,
            category=args.category,
            difficulty=args.difficulty,
        )
    if args.command == "info":
        return cmd_info_cli(args.algo_id)
    if args.command == "compare":
        return cmd_compare_cli(args.id1, args.id2)
    if args.command == "export":
        return cmd_export_cli(fmt=args.fmt, output=args.output)
    if args.command == "mkdocs":
        return cmd_mkdocs()
    if args.command == "check-links":
        return cmd_check_links()

    parser.print_help()
    return 1


if __name__ == "__main__":
    sys.exit(main())
