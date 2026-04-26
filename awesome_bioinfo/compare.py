"""
Compare command for Awesome Bioinformatics Algorithms.
Side-by-side comparison of two algorithms.
"""

from typing import Optional

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager
from .schema import AlgorithmEntry


def _resolve(
    registry: AlgorithmRegistry, algo_id: str
) -> tuple[Optional[AlgorithmEntry], list[AlgorithmEntry]]:
    """Resolve an algorithm by exact ID or unambiguous fuzzy search.

    Returns:
        A tuple of:
        - the resolved AlgorithmEntry when there is an exact or unambiguous fuzzy match
        - the list of ambiguous fuzzy candidates, empty when resolution is unambiguous
    """
    algo = registry.get_algorithm(algo_id)
    if algo:
        return algo, []
    matches = registry.search(algo_id)
    if len(matches) == 1:
        return matches[0], []
    if len(matches) > 1:
        return None, matches
    return None, []


def cmd_compare(
    registry: AlgorithmRegistry,
    category_manager: CategoryManager,
    id1: str,
    id2: str,
) -> int:
    """Compare two algorithms side by side."""
    r1, r1_candidates = _resolve(registry, id1)
    r2, r2_candidates = _resolve(registry, id2)

    problems: list[tuple[str, str, Optional[list[AlgorithmEntry]]]] = []
    if r1_candidates:
        problems.append(("ambiguous", id1, r1_candidates))
    elif not r1:
        problems.append(("missing", id1, None))

    if r2_candidates:
        problems.append(("ambiguous", id2, r2_candidates))
    elif not r2:
        problems.append(("missing", id2, None))

    if problems:
        for problem_type, query, candidates in problems:
            if problem_type == "ambiguous":
                assert candidates is not None
                print(f"Ambiguous argument '{query}': matches multiple algorithms:")
                for candidate in candidates:
                    print(f"  - {candidate.id}: {candidate.name}")
            else:
                print(f"Algorithm not found: '{query}'")
        return 1

    assert r1 is not None
    assert r2 is not None
    a1 = r1
    a2 = r2

    fields = [
        ("Name", lambda a: a.name),
        ("Year", lambda a: str(a.year) if a.year else "-"),
        ("Category", lambda a: a.category),
        ("Difficulty", lambda a: a.difficulty or "-"),
        ("Time Complexity", lambda a: a.time_complexity),
        ("Space Complexity", lambda a: a.space_complexity or "-"),
        ("Language", lambda a: ", ".join(a.language) if a.language else "-"),
        ("Purpose", lambda a: a.purpose),
        ("Related Tools", lambda a: ", ".join(a.related_tools) if a.related_tools else "-"),
        ("Tags", lambda a: ", ".join(a.tags) if a.tags else "-"),
    ]

    w1, w2 = 40, 40
    print(f"{'Field':<20} | {'Algorithm 1':^{w1}} | {'Algorithm 2':^{w2}}")
    print(f"{'-' * 20}-+-{'-' * w1}-+-{'-' * w2}")
    print(f"{'ID':<20} | {a1.id:^{w1}} | {a2.id:^{w2}}")
    for label, getter in fields:
        v1 = getter(a1)
        v2 = getter(a2)
        print(f"{label:<20} | {v1:<{w1}} | {v2:<{w2}}")

    # Description comparison
    print()
    print(f"  Description ({a1.name}):")
    for line in a1.description.strip().split("\n")[:3]:
        print(f"    {line.strip()}")
    print()
    print(f"  Description ({a2.name}):")
    for line in a2.description.strip().split("\n")[:3]:
        print(f"    {line.strip()}")
    print()

    return 0
