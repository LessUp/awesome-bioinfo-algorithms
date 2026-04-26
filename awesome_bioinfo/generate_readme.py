#!/usr/bin/env python3
"""Backward-compatible wrapper around `python -m awesome_bioinfo generate`."""

import sys

from .__main__ import cmd_generate


def main() -> int:
    """Generate README.md from algorithm data."""
    return cmd_generate()


if __name__ == "__main__":
    sys.exit(main())
