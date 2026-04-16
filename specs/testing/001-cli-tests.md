# Test Specifications: CLI and Validation

## Overview

**Spec ID**: TEST-SPEC-001  
**Version**: 1.0.0  
**Status**: Implemented  
**Created**: 2026-04-17

This document specifies the testing strategy and requirements for the Awesome Bioinformatics Algorithms project.

## Testing Philosophy

### Principles
1. **Test behavior, not implementation**: Tests should validate CLI outputs and data integrity
2. **Property-based testing for invariants**: Use Hypothesis for data validation properties
3. **Fast feedback**: Tests should complete in <30 seconds
4. **Clear failure messages**: Test failures should clearly indicate what went wrong

### Test Categories
1. **Unit Tests**: Test individual functions and classes
2. **Integration Tests**: Test CLI commands end-to-end
3. **Property Tests**: Test invariants and properties
4. **Smoke Tests**: CI runs basic functionality checks

## Test Structure

```
tests/
├── conftest.py              # Shared fixtures
├── test_validate.py         # Validation tests
├── test_schema.py           # Data model tests
├── test_data_io.py          # YAML I/O tests
├── test_registry.py         # Registry and indexing tests
├── test_cli.py              # CLI command tests
├── test_search.py           # Search functionality tests
├── test_export.py           # Export functionality tests
├── test_readme_generator.py # README generation tests
└── test_mkdocs_generator.py # MkDocs generation tests
```

## Test Requirements by Module

### 1. Validation Tests (`test_validate.py`)

**Coverage Target**: 95%

**Required Tests**:
- [x] Valid data passes validation
- [x] Missing required field detected
- [x] Invalid ID format detected
- [x] Description length validation (too short, too long)
- [x] Invalid category rejected
- [x] Invalid subcategory rejected
- [x] Duplicate IDs detected
- [x] Warnings for missing optional fields
- [x] Valid optional fields accepted
- [x] Cross-file validation works

**Property-Based Tests** (Hypothesis):
- [x] Any valid algorithm entry passes validation
- [x] Invalid entries always fail with appropriate errors
- [x] Generated test data respects schema constraints

**Example Test**:
```python
def test_category_missing_required_field(tmp_path, valid_entry_dict):
    """Validation should fail when a required field is missing."""
    entry = valid_entry_dict.copy()
    del entry["name"]  # Remove required field
    
    yaml_content = yaml.dump({"algorithms": [entry]})
    test_file = tmp_path / "test.yaml"
    test_file.write_text(yaml_content, encoding="utf-8")
    
    result = validate_file(test_file)
    assert not result.is_valid
    assert any("name" in err.lower() for err in result.errors)
```

### 2. CLI Command Tests (`test_cli.py`)

**Coverage Target**: 90%

**Required Tests for Each Command**:

#### validate command
- [x] Returns 0 on valid data
- [x] Returns 1 on invalid data
- [x] Prints error details on failure
- [x] Prints warning details without failing

#### stats command
- [x] Returns correct algorithm count
- [x] Returns correct category count
- [x] Returns correct tag count
- [x] JSON output format works
- [x] Markdown output format works

#### search command
- [x] Search by name returns matches
- [x] Search by category returns matches
- [x] Search by tags returns matches
- [x] No results returns exit code 1
- [x] Limit option works
- [x] Case-insensitive search

#### info command
- [x] Shows all fields for valid algorithm
- [x] Returns 1 for non-existent algorithm
- [x] JSON output format works
- [x] YAML output format works

#### compare command
- [x] Compares two algorithms successfully
- [x] Shows differences clearly
- [x] Returns 1 if any algorithm not found
- [x] Compares multiple algorithms (3+)

#### export command
- [x] JSON export works
- [x] YAML export works
- [x] CSV export works
- [x] Filter by category works
- [x] Output to file works

#### generate command
- [x] Generates README.md
- [x] Uses template correctly
- [x] Includes all algorithms
- [x] Bilingual generation works

#### mkdocs command
- [x] Generates MkDocs site
- [x] Creates all expected pages
- [x] Serve option starts server

**Example Test** (CLI isolation with monkeypatch):
```python
def test_validate_command_valid_data(monkeypatch, tmp_path):
    """Validate command should return 0 for valid data."""
    # Create valid test data
    valid_yaml = """
    algorithms:
      - id: test-algo
        name: Test Algorithm
        description: This is a test description for validation.
        purpose: Testing
        time_complexity: O(n)
        category: sequence-alignment
    """
    test_file = tmp_path / "test.yaml"
    test_file.write_text(valid_yaml, encoding="utf-8")
    
    # Monkeypatch data directory
    monkeypatch.setattr("scripts.validate.DATA_DIR", tmp_path)
    
    # Run command
    exit_code = run_validate_command()
    
    assert exit_code == 0
```

### 3. Data I/O Tests (`test_data_io.py`)

**Coverage Target**: 90%

**Required Tests**:
- [x] Load valid YAML file
- [x] Load multiple YAML files
- [x] Handle malformed YAML gracefully
- [x] Save YAML with correct encoding (UTF-8)
- [x] Preserve field order in output
- [x] Handle Unicode content correctly
- [x] Handle Chinese text correctly
- [x] `sort_keys=False` preserves order

**Example Test**:
```python
def test_yaml_preserves_unicode(tmp_path):
    """YAML I/O should preserve Unicode content."""
    original_data = {
        "algorithms": [
            {
                "id": "test-algo",
                "name": "测试算法",
                "description": "这是一个测试描述",
            }
        ]
    }
    
    test_file = tmp_path / "test.yaml"
    save_yaml(original_data, test_file)
    
    loaded_data = load_yaml(test_file)
    assert loaded_data["algorithms"][0]["name"] == "测试算法"
    assert loaded_data["algorithms"][0]["description"] == "这是一个测试描述"
```

### 4. Registry Tests (`test_registry.py`)

**Coverage Target**: 90%

**Required Tests**:
- [x] Load all algorithms from data directory
- [x] Get algorithm by ID
- [x] Get algorithms by category
- [x] Get algorithms by tag
- [x] Search by name (case-insensitive)
- [x] Statistics calculation correct
- [x] Duplicate IDs raise ValueError

**Property-Based Tests**:
- [x] Registry size matches file count
- [x] All categories have at least one algorithm
- [x] All tags are lowercase with hyphens

### 5. Schema Tests (`test_schema.py`)

**Coverage Target**: 85%

**Required Tests**:
- [x] AlgorithmEntry dataclass creation
- [x] from_dict() method works
- [x] to_dict() method works
- [x] Round-trip conversion preserves data
- [x] Validation method works
- [x] Missing fields detected

**Example Test**:
```python
def test_algorithm_entry_roundtrip(valid_entry_dict):
    """Converting to dict and back should preserve data."""
    entry = AlgorithmEntry.from_dict(valid_entry_dict)
    result_dict = entry.to_dict()
    
    assert result_dict["id"] == valid_entry_dict["id"]
    assert result_dict["name"] == valid_entry_dict["name"]
    assert result_dict["description"] == valid_entry_dict["description"]
    # ... check all fields
```

### 6. Search Tests (`test_search.py`)

**Coverage Target**: 90%

**Required Tests**:
- [x] Search by partial name match
- [x] Search by exact ID match
- [x] Filter by category
- [x] Filter by tags (single and multiple)
- [x] Filter by difficulty
- [x] Filter by year range
- [x] Combined filters work together
- [x] Results limited correctly
- [x] Empty results handled gracefully

### 7. Export Tests (`test_export.py`)

**Coverage Target**: 90%

**Required Tests**:
- [x] Export to JSON (valid JSON)
- [x] Export to YAML (valid YAML)
- [x] Export to CSV (correct columns)
- [x] Export to Markdown (formatted table)
- [x] Filter by category during export
- [x] Pretty-print option works
- [x] Export to file works
- [x] Export to stdout works

### 8. README Generator Tests (`test_readme_generator.py`)

**Coverage Target**: 85%

**Required Tests**:
- [x] Generate from template
- [x] Include all algorithms
- [x] Group by category
- [x] Generate statistics table
- [x] Generate table of contents
- [x] Bilingual generation (EN and ZH)
- [x] Deterministic output
- [x] Template errors reported

### 9. MkDocs Generator Tests (`test_mkdocs_generator.py`)

**Coverage Target**: 85%

**Required Tests**:
- [x] Generate all category pages
- [x] Generate all algorithm pages
- [x] Generate navigation structure
- [x] Cross-references work
- [x] Bilingual pages generated
- [x] Assets copied correctly

## Test Fixtures (conftest.py)

### Required Fixtures

```python
@pytest.fixture
def valid_entry_dict():
    """Return a valid algorithm entry dictionary."""
    return {
        "id": "smith-waterman",
        "name": "Smith-Waterman",
        "description": "Classic local sequence alignment algorithm...",
        "purpose": "Local sequence alignment",
        "time_complexity": "O(mn)",
        "space_complexity": "O(mn)",
        "category": "sequence-alignment",
        "subcategory": "pairwise-alignment",
        "year": 1981,
        "paper_url": "https://doi.org/10.1016/0022-2836(81)90087-5",
        "implementation_url": "https://github.com/example/sw",
        "related_tools": ["BLAST", "FASTA"],
        "tags": ["dynamic-programming", "local-alignment", "classic"],
        "difficulty": "intermediate",
        "language": "C",
    }

@pytest.fixture
def sample_categories_yaml():
    """Return sample categories YAML content."""
    return """
    categories:
      sequence-alignment:
        name: Sequence Alignment
        subcategories:
          - pairwise-alignment
          - multiple-alignment
      assembly:
        name: Sequence Assembly
        subcategories:
          - de-novo-assembly
    """

@pytest.fixture
def tmp_data_dir(tmp_path):
    """Create a temporary data directory with test files."""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    (data_dir / "algorithms").mkdir()
    return data_dir
```

## Hypothesis Strategies

### Algorithm Entry Strategy

```python
from hypothesis import strategies as st

@st.composite
def algorithm_entry_strategy(draw):
    """Generate valid algorithm entry dictionaries."""
    return {
        "id": draw(st.from_regex(r"^[a-z0-9]+(-[a-z0-9]+)*$").map(lambda s: s[:40])),
        "name": draw(st.text(min_size=3, max_size=100).filter(lambda s: len(s.strip()) >= 3)),
        "description": draw(st.text(min_size=50, max_size=500)),
        "purpose": draw(st.text(min_size=10, max_size=200)),
        "time_complexity": draw(st.sampled_from(["O(n)", "O(n^2)", "O(mn)", "O(n log n)"])),
        "category": draw(st.sampled_from(["sequence-alignment", "assembly", "variant-calling"])),
        # ... optional fields
    }
```

### Property Tests

```python
@given(algorithm_entry_strategy())
def test_any_valid_entry_passes_validation(entry):
    """Any entry generated by our strategy should pass validation."""
    result = validate_entry(entry)
    assert result.is_valid

@given(algorithm_entry_strategy())
def test_entry_roundtrip_preserves_data(entry):
    """Converting entry to/from dataclass should preserve data."""
    algo = AlgorithmEntry.from_dict(entry)
    result = algo.to_dict()
    
    for key in entry:
        assert result[key] == entry[key]
```

## CI Test Configuration

### Test Matrix

```yaml
python-version: ['3.9', '3.10', '3.11', '3.12']
commands:
  - python -m pytest tests/ -v --tb=short
  - python -m pytest tests/ --cov=scripts --cov-branch --cov-report=term-missing  # 3.11 only
```

### Performance Requirements

| Test Suite | Max Time | Current |
|------------|----------|---------|
| Unit Tests | 10s | TBD |
| Integration Tests | 15s | TBD |
| Property Tests | 20s | TBD |
| **Total** | **30s** | **TBD** |

### Coverage Requirements

| Module | Target | Current |
|--------|--------|---------|
| scripts/validate.py | 95% | TBD |
| scripts/schema.py | 85% | TBD |
| scripts/data_io.py | 90% | TBD |
| scripts/registry.py | 90% | TBD |
| scripts/search.py | 90% | TBD |
| scripts/export.py | 90% | TBD |
| scripts/readme_generator.py | 85% | TBD |
| scripts/mkdocs_generator.py | 85% | TBD |
| **Overall** | **>90%** | **TBD** |

## Test Execution

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific Test File
```bash
python -m pytest tests/test_validate.py -v
```

### Run Single Test
```bash
python -m pytest tests/test_validate.py::test_category_missing_required_field -v
```

### Run with Coverage
```bash
python -m pytest tests/ --cov=scripts --cov-branch --cov-report=term-missing
```

### Run Property Tests Only
```bash
python -m pytest tests/ -k hypothesis -v
```

### Run with Verbose Output
```bash
python -m pytest tests/ -vv --tb=long
```

## Test Maintenance

### When to Add Tests
- New feature: Add corresponding tests
- Bug fix: Add regression test
- Refactoring: Ensure existing tests pass, add if gaps found

### When to Update Tests
- Schema changes: Update validation tests
- CLI changes: Update command tests
- New edge cases: Add tests for discovered cases

### Test Quality Checklist
- [ ] Test has clear name (describes what it tests)
- [ ] Test has docstring explaining purpose
- [ ] Test failure message is actionable
- [ ] Test is independent (no ordering dependencies)
- [ ] Test uses appropriate fixtures
- [ ] Test coverage is meaningful (not just line coverage)

## Related Documents

- Product Vision: `/specs/product/000-product-vision.md`
- Core Architecture: `/specs/rfc/0001-core-architecture.md`
- CLI Interface: `/specs/api/001-cli-interface.md`
- Algorithm Entry Schema: `/specs/db/001-algorithm-entry.md`

## Change History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-04-17 | 1.0.0 | Initial test specification | Community |
