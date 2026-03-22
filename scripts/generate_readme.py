#!/usr/bin/env python3
"""Backward-compatible wrapper around `python -m scripts generate`."""
import sys
from pathlib import Path

try:
    from .__main__ import cmd_generate
except ImportError:
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
    from scripts.__main__ import cmd_generate


def main() -> int:
    """Generate README.md from algorithm data."""
    return cmd_generate()


if __name__ == '__main__':
    sys.exit(main())
