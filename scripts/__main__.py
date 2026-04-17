"""Compatibility shim for CLI entry point.

This module is deprecated. Use 'python -m awesome_bioinfo' instead.
"""
import warnings

warnings.warn(
    "The 'scripts' CLI is deprecated. Use 'python -m awesome_bioinfo' instead.",
    DeprecationWarning,
    stacklevel=2,
)

# Delegate to awesome_bioinfo
from awesome_bioinfo.__main__ import main

if __name__ == "__main__":
    main()
