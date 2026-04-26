"""
Tests for correct owner/repository/Pages URL metadata.

Ensures no stale 'shane' owner references survive in generators,
config, or link-checker metadata.
"""

import inspect
import os
import re

import pytest


WRONG_OWNER_RE = re.compile(r"(shane\.github\.io|github\.com/shane\b|shane/awesome-bioinfo)", re.IGNORECASE)
CORRECT_AUTHOR = "LessUp"
CORRECT_REPO_URL = "https://github.com/LessUp/awesome-bioinfo-algorithms"
CORRECT_PAGES_URL = "https://lessup.github.io/awesome-bioinfo-algorithms/"


# ---------------------------------------------------------------------------
# readme_generator.py
# ---------------------------------------------------------------------------

def test_readme_generator_no_wrong_owner():
    """ReadmeGenerator source must not contain stale shane owner references."""
    from awesome_bioinfo import readme_generator
    source = inspect.getsource(readme_generator)
    assert not WRONG_OWNER_RE.search(source), (
        "awesome_bioinfo/readme_generator.py still contains wrong owner/URL: "
        + str(WRONG_OWNER_RE.findall(source))
    )


def test_readme_generator_pages_url_correct():
    """ReadmeGenerator should reference the correct GitHub Pages URL."""
    from awesome_bioinfo import readme_generator
    source = inspect.getsource(readme_generator)
    assert "lessup.github.io/awesome-bioinfo-algorithms" in source.lower()


# ---------------------------------------------------------------------------
# generate_mkdocs.py
# ---------------------------------------------------------------------------

def test_generate_mkdocs_no_wrong_owner():
    """generate_mkdocs source must not contain stale shane owner references."""
    from awesome_bioinfo import generate_mkdocs
    source = inspect.getsource(generate_mkdocs)
    assert not WRONG_OWNER_RE.search(source), (
        "awesome_bioinfo/generate_mkdocs.py still contains wrong owner/URL: "
        + str(WRONG_OWNER_RE.findall(source))
    )


def test_generate_mkdocs_repo_url_correct():
    """generate_mkdocs should reference the correct GitHub repo URL."""
    from awesome_bioinfo import generate_mkdocs
    source = inspect.getsource(generate_mkdocs)
    assert CORRECT_REPO_URL in source


# ---------------------------------------------------------------------------
# link_checker.py
# ---------------------------------------------------------------------------

def test_link_checker_user_agent_no_wrong_owner(project_root):
    """link_checker User-Agent must not contain stale shane owner URL."""
    path = os.path.join(project_root, "awesome_bioinfo", "link_checker.py")
    content = open(path, encoding="utf-8").read()
    assert not WRONG_OWNER_RE.search(content), (
        "awesome_bioinfo/link_checker.py still contains wrong owner/URL: "
        + str(WRONG_OWNER_RE.findall(content))
    )


def test_link_checker_repo_url_exact(project_root):
    """link_checker must reference the exact canonical repo URL."""
    path = os.path.join(project_root, "awesome_bioinfo", "link_checker.py")
    content = open(path, encoding="utf-8").read()
    assert CORRECT_REPO_URL in content, (
        f"awesome_bioinfo/link_checker.py must contain '{CORRECT_REPO_URL}'"
    )


# ---------------------------------------------------------------------------
# mkdocs/mkdocs.yml
# ---------------------------------------------------------------------------

def test_mkdocs_yml_no_wrong_owner(project_root):
    """mkdocs/mkdocs.yml must not contain stale shane owner references."""
    path = os.path.join(project_root, "mkdocs", "mkdocs.yml")
    content = open(path, encoding="utf-8").read()
    assert not WRONG_OWNER_RE.search(content), (
        "mkdocs/mkdocs.yml still contains wrong owner/URL: "
        + str(WRONG_OWNER_RE.findall(content))
    )


def test_mkdocs_yml_correct_urls(project_root):
    """mkdocs/mkdocs.yml should have correct repo and site URLs."""
    path = os.path.join(project_root, "mkdocs", "mkdocs.yml")
    content = open(path, encoding="utf-8").read()
    assert "lessup.github.io" in content
    assert "LessUp/awesome-bioinfo-algorithms" in content


# ---------------------------------------------------------------------------
# mkdocs/overrides/main.html
# ---------------------------------------------------------------------------

def test_overrides_main_html_no_wrong_owner(project_root):
    """mkdocs/overrides/main.html must not contain stale shane owner references."""
    path = os.path.join(project_root, "mkdocs", "overrides", "main.html")
    content = open(path, encoding="utf-8").read()
    assert not WRONG_OWNER_RE.search(content), (
        "mkdocs/overrides/main.html still contains wrong owner/URL: "
        + str(WRONG_OWNER_RE.findall(content))
    )


def test_overrides_main_html_exact_urls(project_root):
    """mkdocs/overrides/main.html must contain the exact canonical repo and Pages URLs."""
    path = os.path.join(project_root, "mkdocs", "overrides", "main.html")
    content = open(path, encoding="utf-8").read()
    assert CORRECT_REPO_URL in content, (
        f"mkdocs/overrides/main.html must contain '{CORRECT_REPO_URL}'"
    )
    assert CORRECT_PAGES_URL in content, (
        f"mkdocs/overrides/main.html must contain '{CORRECT_PAGES_URL}'"
    )


# ---------------------------------------------------------------------------
# package metadata
# ---------------------------------------------------------------------------


def test_package_author_uses_canonical_owner():
    """Package metadata should use the canonical LessUp owner name."""
    from awesome_bioinfo import __author__

    assert __author__ == CORRECT_AUTHOR
