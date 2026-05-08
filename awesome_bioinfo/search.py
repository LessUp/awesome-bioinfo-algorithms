"""
Search command for Awesome Bioinformatics Algorithms.

This module provides backward-compatible imports.
The implementation has been merged into __main__.py.
"""

# Re-export from __main__ for backward compatibility
from .__main__ import cmd_search, format_algorithm_short, search_algorithms

__all__ = ["cmd_search", "search_algorithms", "format_algorithm_short"]
