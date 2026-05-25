"""
Tests for compare command ambiguity/missing behavior and check-links contract.

Covers gaps identified in testing-strategy spec:
- Compare: ambiguous fuzzy match must be identified (not collapsed to "not found")
- Compare: missing argument must be identified
- Check-links: unit-level coverage for is_valid_url and cmd_check_links routing
"""

import pytest

from awesome_bioinfo.__main__ import cmd_compare
from awesome_bioinfo.algorithm_registry import AlgorithmRegistry
from awesome_bioinfo.category_manager import CategoryManager
from awesome_bioinfo.link_checker import (
    LinkCheckResult,
    LinkCheckSummary,
    cmd_check_links,
    is_valid_url,
)
from awesome_bioinfo.schema import AlgorithmEntry, Category

# ---------------------------------------------------------------------------
# Shared fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def simple_category_manager() -> CategoryManager:
    manager = CategoryManager()
    manager.from_categories(
        [
            Category(
                id="seq",
                name="序列比对",
                name_en="Sequence Alignment",
                description="Sequence alignment algorithms",
            )
        ]
    )
    return manager


@pytest.fixture()
def registry_with_ambiguous_pair() -> AlgorithmRegistry:
    """Registry containing two algorithms whose names both match 'align'."""
    registry = AlgorithmRegistry()
    registry.from_algorithms(
        [
            AlgorithmEntry(
                id="local-align",
                name="Local Alignment Algorithm",
                description="A local alignment algorithm that meets the minimum description length.",
                purpose="Local alignment of sequences",
                time_complexity="O(mn)",
                category="seq",
            ),
            AlgorithmEntry(
                id="global-align",
                name="Global Alignment Algorithm",
                description="A global alignment algorithm that meets the minimum description length.",
                purpose="Global alignment of sequences",
                time_complexity="O(mn)",
                category="seq",
            ),
            AlgorithmEntry(
                id="unique-algo",
                name="Unique Algorithm",
                description="A completely unique algorithm with a description long enough to pass validation.",
                purpose="Unique processing",
                time_complexity="O(n)",
                category="seq",
            ),
        ]
    )
    return registry


# ---------------------------------------------------------------------------
# Compare: exact-match happy path (sanity)
# ---------------------------------------------------------------------------


class TestCompareExactMatch:
    def test_exact_ids_produce_table(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "local-align",
            "global-align",
        )
        output = capsys.readouterr().out
        assert exit_code == 0
        assert "local-align" in output
        assert "global-align" in output


# ---------------------------------------------------------------------------
# Compare: ambiguous argument must be *identified*
# ---------------------------------------------------------------------------


class TestCompareAmbiguousArgument:
    def test_ambiguous_first_arg_identified_in_output(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        """Spec: ambiguous argument SHALL be identified in error output."""
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "align",  # matches both local-align and global-align
            "unique-algo",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        # Must name the ambiguous argument
        assert "align" in output
        # Must NOT say "not found" — it was found, just ambiguous
        assert "not found" not in output.lower()

    def test_ambiguous_second_arg_identified_in_output(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "unique-algo",
            "align",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "align" in output
        assert "not found" not in output.lower()

    def test_ambiguous_output_lists_candidate_ids(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        """Spec: matching algorithm IDs SHALL be listed for disambiguation."""
        cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "align",
            "unique-algo",
        )
        output = capsys.readouterr().out
        assert "local-align" in output
        assert "global-align" in output


# ---------------------------------------------------------------------------
# Compare: missing (zero-match) argument must be identified
# ---------------------------------------------------------------------------


class TestCompareMissingArgument:
    def test_missing_first_arg_identified(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "totally-unknown-xyz",
            "unique-algo",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "totally-unknown-xyz" in output

    def test_missing_and_ambiguous_arguments_are_both_identified(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "totally-unknown-xyz",
            "align",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "totally-unknown-xyz" in output
        assert "align" in output
        assert "local-align" in output
        assert "global-align" in output

    def test_ambiguous_and_missing_arguments_are_both_identified(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "align",
            "totally-unknown-xyz",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "align" in output
        assert "totally-unknown-xyz" in output
        assert "local-align" in output
        assert "global-align" in output

    def test_missing_second_arg_identified(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "unique-algo",
            "totally-unknown-xyz",
        )
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "totally-unknown-xyz" in output


# ---------------------------------------------------------------------------
# Compare: unambiguous fuzzy match works transparently
# ---------------------------------------------------------------------------


class TestCompareFuzzyUnambiguous:
    def test_unambiguous_fuzzy_resolves_transparently(
        self, registry_with_ambiguous_pair, simple_category_manager, capsys
    ):
        """Spec: unambiguous partial match SHALL be used transparently."""
        exit_code = cmd_compare(
            registry_with_ambiguous_pair,
            simple_category_manager,
            "unique",  # matches only unique-algo
            "local-align",
        )
        output = capsys.readouterr().out
        assert exit_code == 0
        assert "unique-algo" in output


# ---------------------------------------------------------------------------
# Check-links: is_valid_url unit tests
# ---------------------------------------------------------------------------


class TestIsValidUrl:
    def test_valid_https_url(self):
        assert is_valid_url("https://example.com/paper") is True

    def test_valid_http_url(self):
        assert is_valid_url("http://example.com") is True

    def test_invalid_no_scheme(self):
        assert is_valid_url("example.com/paper") is False

    def test_invalid_ftp_scheme(self):
        assert is_valid_url("ftp://example.com/file") is False

    def test_invalid_empty_string(self):
        assert is_valid_url("") is False

    def test_invalid_no_netloc(self):
        assert is_valid_url("https://") is False


# ---------------------------------------------------------------------------
# Check-links: cmd_check_links routing (mocked async core)
# ---------------------------------------------------------------------------


class TestCmdCheckLinks:
    def test_returns_zero_when_no_errors(self, capsys):
        """Spec: all links valid → exit code 0 with summary."""
        summary = LinkCheckSummary(total=3, ok=3, errors=0, warnings=0)

        async def fake_check_all_links(_data_dir):
            return summary

        with pytest.MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr(
                "awesome_bioinfo.link_checker.check_all_links", fake_check_all_links
            )
            exit_code = cmd_check_links()
        output = capsys.readouterr().out
        assert exit_code == 0
        assert "3" in output  # total checked

    def test_returns_one_when_errors_present(self, capsys):
        """Spec: broken links → exit code 1 with broken URLs reported."""
        bad = LinkCheckResult(
            url="https://broken.example.com",
            algorithm_id="algo-x",
            field_type="paper_url",
            status="error",
            error_message="Connection refused",
        )
        summary = LinkCheckSummary(total=2, ok=1, errors=1, warnings=0, results=[bad])

        async def fake_check_all_links(_data_dir):
            return summary

        with pytest.MonkeyPatch.context() as monkeypatch:
            monkeypatch.setattr(
                "awesome_bioinfo.link_checker.check_all_links", fake_check_all_links
            )
            exit_code = cmd_check_links()
        output = capsys.readouterr().out
        assert exit_code == 1
        assert "algo-x" in output
        assert "https://broken.example.com" in output

    def test_docstring_references_correct_module(self):
        """link_checker module docstring must say python -m awesome_bioinfo."""
        import awesome_bioinfo.link_checker as lc

        module_doc = lc.__doc__ or ""
        assert "python -m awesome_bioinfo" in module_doc
        assert "python -m scripts" not in module_doc
