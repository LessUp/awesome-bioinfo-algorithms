"""
Info command for Awesome Bioinformatics Algorithms.
Shows detailed information about a single algorithm.
"""

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager


def cmd_info(
    registry: AlgorithmRegistry,
    category_manager: CategoryManager,
    algo_id: str,
) -> int:
    """Show detailed info about an algorithm."""
    algo = registry.get_algorithm(algo_id)
    if not algo:
        # Try fuzzy match
        matches = registry.search(algo_id)
        if not matches:
            print(f"Algorithm not found: '{algo_id}'")
            return 1
        if len(matches) > 1:
            print(f"Multiple matches for '{algo_id}':")
            for m in matches:
                print(f"  - {m.id}: {m.name}")
            return 1
        algo = matches[0]

    cat = category_manager.get_category(algo.category)
    sub = category_manager.get_category(algo.subcategory) if algo.subcategory else None

    difficulty_labels = {
        "beginner": "入门 (Beginner)",
        "intermediate": "进阶 (Intermediate)",
        "advanced": "高级 (Advanced)",
    }

    print(f"{'=' * 60}")
    print(f"  {algo.name}" + (f" ({algo.year})" if algo.year else ""))
    print(f"{'=' * 60}")
    print(f"  ID:               {algo.id}")
    print(
        f"  分类:             {cat.name} ({cat.name_en})"
        if cat
        else f"  分类:             {algo.category}"
    )
    if sub:
        print(f"  子分类:           {sub.name} ({sub.name_en})")
    if algo.difficulty:
        print(f"  难度:             {difficulty_labels.get(algo.difficulty, algo.difficulty)}")
    print()
    print("  描述:")
    for line in algo.description.strip().split("\n"):
        print(f"    {line.strip()}")
    print()
    print(f"  用途:             {algo.purpose}")
    print(f"  时间复杂度:       {algo.time_complexity}")
    if algo.space_complexity:
        print(f"  空间复杂度:       {algo.space_complexity}")
    if algo.language:
        print(f"  实现语言:         {', '.join(algo.language)}")
    if algo.paper_url:
        print(f"  论文:             {algo.paper_url}")
    if algo.implementation_url:
        print(f"  实现:             {algo.implementation_url}")
    if algo.related_tools:
        print(f"  相关工具:         {', '.join(algo.related_tools)}")
    if algo.tags:
        print(f"  标签:             {', '.join(algo.tags)}")
    if algo.references:
        print("  扩展资料:")
        for ref in algo.references:
            title = ref.title or ref.url
            ref_type = f" [{ref.type}]" if ref.type else ""
            print(f"    - {title}{ref_type}: {ref.url}")

    print()
    return 0
