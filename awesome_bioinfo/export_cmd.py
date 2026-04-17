"""
Export command for Awesome Bioinformatics Algorithms.
Export algorithms to JSON or CSV format.
"""

import csv
import json
import sys

from .algorithm_registry import AlgorithmRegistry
from .category_manager import CategoryManager


def cmd_export(
    registry: AlgorithmRegistry,
    category_manager: CategoryManager,
    fmt: str = "json",
    output: str = "",
) -> int:
    """Export all algorithms to JSON or CSV."""
    if fmt not in ("json", "csv"):
        print(f"Unsupported format: '{fmt}'. Use 'json' or 'csv'.")
        return 1

    algorithms = registry.get_all_algorithms()
    if not algorithms:
        print("No algorithms to export.")
        return 1

    if fmt == "json":
        data = {
            "algorithms": [a.to_dict() for a in algorithms],
            "total": len(algorithms),
        }
        content = json.dumps(data, ensure_ascii=False, indent=2)
    else:
        import io

        buf = io.StringIO()
        writer = csv.writer(buf)
        writer.writerow(
            [
                "id",
                "name",
                "year",
                "category",
                "subcategory",
                "difficulty",
                "time_complexity",
                "space_complexity",
                "language",
                "tags",
                "purpose",
            ]
        )
        for a in algorithms:
            writer.writerow(
                [
                    a.id,
                    a.name,
                    a.year or "",
                    a.category,
                    a.subcategory,
                    a.difficulty,
                    a.time_complexity,
                    a.space_complexity,
                    "|".join(a.language),
                    "|".join(a.tags),
                    a.purpose,
                ]
            )
        content = buf.getvalue()

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Exported {len(algorithms)} algorithms to {output}")
    else:
        sys.stdout.write(content)

    return 0
