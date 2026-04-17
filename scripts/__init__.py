"""Compatibility shim - redirects to awesome_bioinfo.

This module is deprecated. Use awesome_bioinfo directly instead.
"""
import warnings
import sys

# Import all from awesome_bioinfo
from awesome_bioinfo import *  # noqa: F401,F403

# Check if this is a direct invocation
if __name__ == "scripts":
    warnings.warn(
        "The 'scripts' package is deprecated. Use 'python -m awesome_bioinfo' instead.",
        DeprecationWarning,
        stacklevel=2,
    )
