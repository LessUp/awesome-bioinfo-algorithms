# RFC-0001: Core Architecture Design

## Status
- **Status**: Accepted
- **Created**: 2026-01-15
- **Last Updated**: 2026-04-17
- **Author**: Community
- **Reviewers**: Community Contributors

## Context

This document describes the core architecture of the Awesome Bioinformatics Algorithms project, including the Python CLI toolkit, YAML data structure, and documentation generation pipeline.

## Problem Statement

How do we maintain a large collection of bioinformatics algorithms (200+) with:
- Structured, machine-readable data
- Bilingual documentation (English + Chinese)
- Automated validation and generation
- Easy community contributions

## Proposed Architecture

### Layer 1: Data Layer

**YAML Database** (`data/`)
- `categories.yaml` - Hierarchical category taxonomy
- `algorithms/*.yaml` - Individual algorithm entries (organized by category)

**Design Decisions**:
- YAML chosen over JSON for human readability
- Split files by category for maintainability
- Single source of truth for all algorithm data

### Layer 2: Processing Layer

**Python Scripts** (`scripts/`)

```
scripts/
├── __init__.py
├── __main__.py           # CLI entry point
├── schema.py             # Data models (dataclasses)
├── data_io.py            # YAML loading/saving utilities
├── validate.py           # Data validation logic
├── registry.py           # Algorithm registry and indexing
├── stats.py              # Statistics generation
├── search.py             # Search and filtering
├── compare.py            # Algorithm comparison
├── export.py             # Data format export
├── readme_generator.py   # README generation
└── mkdocs_generator.py   # MkDocs generation
```

**Key Design Patterns**:
- Dataclasses for structured records (`AlgorithmEntry`, `Category`, `ValidationResult`)
- Registry pattern for algorithm lookup (`_by_id`, `_by_category`)
- Builder pattern for document generation

### Layer 3: CLI Layer

**Command Interface**: `python -m scripts <command> [options]`

Supported commands:
```bash
validate              # Validate all YAML data
stats                 # Show collection statistics
search <query>        # Search algorithms
info <algorithm-id>   # Show algorithm details
compare <id1> <id2>   # Compare algorithms
export --format <fmt> # Export data
generate              # Generate README.md
mkdocs                # Generate MkDocs site
```

**Exit Codes**:
- `0` - Success
- `1` - Validation errors or command failure
- `2` - Invalid arguments

### Layer 4: Documentation Layer

**Generated Outputs**:
- `README.md` - Main repository landing page (generated from template)
- `README.zh-CN.md` - Chinese version
- `mkdocs/docs/` - MkDocs documentation site

**Template System**:
- `templates/readme_template.md` - README template with placeholders
- `templates/algorithm_template.yaml` - Template for new algorithm entries

## Data Flow

```
┌─────────────────┐
│  YAML Data      │
│  (data/)        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Data Loader    │
│  (data_io.py)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Validation     │
│  (validate.py)  │
└────────┬────────┘
         │
    ┌────┴────┐
    ▼         ▼
┌────────┐ ┌──────────┐
│ Errors │ │ Registry │
│/Warns  │ │ (in-memory)│
└────────┘ └────┬─────┘
                │
         ┌──────┴──────┐
         ▼             ▼
   ┌──────────┐  ┌──────────┐
   │ CLI Cmd  │  │ Generator│
   └──────────┘  └──────────┘
```

## Technology Choices

| Component | Technology | Rationale |
|-----------|-----------|-----------|
| Language | Python 3.9+ | Wide compatibility, bioinformatics standard |
| CLI | argparse (stdlib) | No external dependencies for core |
| Data Format | YAML (PyYAML) | Human-readable, widely adopted |
| Validation | Custom + Hypothesis | Property-based testing for invariants |
| Linting | Ruff | Fast, modern Python linter |
| Type Checking | mypy | Industry standard for Python types |
| Testing | pytest | De facto Python testing framework |
| Doc Generation | MkDocs + Material | Beautiful, searchable docs |
| CI/CD | GitHub Actions | Native GitHub integration |

## Constraints

1. **No External Dependencies for Core CLI**: Core commands (`validate`, `search`, `info`) must work with only stdlib + PyYAML
2. **Python 3.9+ Compatibility**: Must support Python 3.9, 3.10, 3.11, 3.12
3. **Deterministic Generation**: Generated files must be deterministic for CI diff checks
4. **Bilingual Parity**: English and Chinese documentation must have feature parity

## Migration Strategy

Not applicable - this is the initial architecture design.

## Testing Strategy

1. **Unit Tests**: Test each module in isolation
2. **Integration Tests**: Test CLI commands end-to-end
3. **Property Tests**: Use Hypothesis to validate invariants
4. **Smoke Tests**: CI runs basic CLI commands

## Alternatives Considered

### Alternative 1: JSON instead of YAML
**Rejected**: YAML is more human-readable for large collections and supports comments

### Alternative 2: Web-based interface
**Rejected**: Out of scope - focus on CLI and static documentation

### Alternative 3: Database (SQLite/PostgreSQL)
**Rejected**: Overkill for static data; YAML files are easier to contribute to via PRs

## Risks and Mitigations

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| YAML parse errors | High | Low | Automated validation in CI |
| Generated files out of sync | Medium | Medium | CI checks with `git diff --exit-code` |
| Python version incompatibility | High | Low | CI tests on 3.9-3.12 |
| Large file performance | Medium | Low | Split YAML by category |

## Implementation Plan

- [x] Phase 1: Core data models and YAML I/O
- [x] Phase 2: Validation logic and testing
- [x] Phase 3: CLI commands (search, info, compare, stats)
- [x] Phase 4: Documentation generators (README, MkDocs)
- [x] Phase 5: CI pipeline and pre-commit hooks
- [x] Phase 6: Contributing guidelines and templates

## Related Documents

- Product Vision: `/specs/product/000-product-vision.md`
- API Spec: `/specs/api/001-cli-interface.md`
- Data Schema: `/specs/db/001-algorithm-entry.md`

## References

- Python argparse: https://docs.python.org/3/library/argparse.html
- MkDocs Material: https://squidfunk.github.io/mkdocs-material/
- Hypothesis testing: https://hypothesis.readthedocs.io/
