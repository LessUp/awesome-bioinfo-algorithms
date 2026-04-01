"""
Search command for Awesome Bioinformatics Algorithms.
Provides keyword, tag, category, and difficulty filtering.
"""

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .schema import VALID_DIFFICULTIES, AlgorithmEntry


def search_algorithms(
    registry: AlgorithmRegistry,
    category_manager: CategoryManager,
    keyword: str = "",
    tag: str = "",
    category: str = "",
    difficulty: str = "",
) -> list[AlgorithmEntry]:
    """
    Search algorithms with optional filters.

    Args:
        registry: Loaded algorithm registry
        category_manager: Loaded category manager
        keyword: Keyword to search in name/description/tags
        tag: Filter by tag
        category: Filter by category ID
        difficulty: Filter by difficulty level

    Returns:
        List of matching AlgorithmEntry objects
    """
    results = registry.get_all_algorithms()

    if keyword:
        kw = keyword.lower()
        results = [
            a
            for a in results
            if kw in a.name.lower()
            or kw in a.description.lower()
            or kw in a.purpose.lower()
            or any(kw in t.lower() for t in a.tags)
        ]

    if tag:
        tag_lower = tag.lower()
        results = [a for a in results if any(tag_lower in t.lower() for t in a.tags)]

    if category:
        results = [a for a in results if a.category == category or a.subcategory == category]

    if difficulty:
        results = [a for a in results if a.difficulty == difficulty]

    return results


def format_algorithm_short(algo: AlgorithmEntry, category_manager: CategoryManager) -> str:
    """Format a single algorithm as a short listing line."""
    cat = category_manager.get_category(algo.category)
    cat_label = cat.name_en if cat else algo.category
    year_str = f" ({algo.year})" if algo.year else ""
    diff_str = f" [{algo.difficulty}]" if algo.difficulty else ""
    return f"  {algo.id}{year_str} - {algo.name}{diff_str} | {cat_label}"


def cmd_search(
    registry: AlgorithmRegistry,
    category_manager: CategoryManager,
    keyword: str = "",
    tag: str = "",
    category: str = "",
    difficulty: str = "",
) -> int:
    """Execute the search command."""
    if difficulty and difficulty not in VALID_DIFFICULTIES:
        print(f"Invalid difficulty: '{difficulty}'. Valid: {', '.join(VALID_DIFFICULTIES)}")
        return 1

    if not any([keyword, tag, category, difficulty]):
        print("Usage: python -m scripts search [options]")
        print("Options:")
        print("  --keyword <text>    Search in name, description, purpose, tags")
        print("  --tag <tag>         Filter by tag")
        print("  --category <id>     Filter by category ID")
        print("  --difficulty <d>    Filter by difficulty (beginner/intermediate/advanced)")
        return 1

    results = search_algorithms(registry, category_manager, keyword, tag, category, difficulty)

    if not results:
        print("No algorithms found matching your criteria.")
        return 0

    print(f"Found {len(results)} algorithm(s):\n")
    for algo in results:
        print(format_algorithm_short(algo, category_manager))

    return 0
