---
title: Development Guide
layout: default
nav_order: 3
description: "Project structure, environment setup, and core architecture"
---

# Development Guide
{: .no_toc }

This guide covers everything you need to know about the Awesome Bioinformatics Algorithms project architecture, development workflow, and contribution process.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Project Overview

### Mission

To create the most comprehensive, well-organized, and accessible collection of bioinformatics algorithms for researchers, students, and practitioners worldwide.

### Design Principles

1. **Data-Driven**: All content is stored as structured YAML data
2. **Auto-Generated**: README and documentation are auto-generated from data
3. **Bilingual First**: Full support for both English and Chinese
4. **Community-Driven**: Open contribution process with quality gates

---

## Project Structure

```
awesome-bioinfo-algorithms/
├── README.md                    # Auto-generated from template + data
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md           # Community code of conduct
├── SECURITY.md                  # Security policy
├── CHANGELOG.md                 # Version changelog
├── LICENSE                      # CC0 1.0 Universal
├── pyproject.toml               # Python project configuration
├── .pre-commit-config.yaml      # Pre-commit hooks
├── requirements.txt             # Dependencies shortcut
│
├── data/                        # Source of truth — all algorithm data
│   ├── categories.yaml          # Category taxonomy
│   └── algorithms/              # Algorithm entries by category
│       ├── sequence-alignment.yaml
│       ├── assembly.yaml
│       └── ...
│
├── docs/                        # Documentation (Jekyll/GitHub Pages)
│   ├── index.md                 # Portal page
│   ├── 404.md                   # 404 error page
│   ├── _config.yml              # Jekyll configuration
│   ├── en/                      # English documentation
│   └── zh/                      # Chinese documentation
│
├── scripts/                     # Core Python modules
│   ├── __main__.py              # CLI entry point
│   ├── schema.py                # Data models (Category, AlgorithmEntry)
│   ├── validate.py              # Data validation
│   ├── category_manager.py      # Category management
│   ├── algorithm_registry.py    # Algorithm registry
│   ├── readme_generator.py      # README generation
│   ├── data_io.py               # Import/export functionality
│   ├── search.py                # Search command
│   ├── info_cmd.py              # Info command
│   ├── stats.py                 # Statistics command
│   ├── compare.py               # Algorithm comparison
│   ├── export_cmd.py            # Export command
│   └── generate_mkdocs.py       # MkDocs generation
│
├── templates/                   # Jinja2 templates
│   ├── readme_template.md       # README generation template
│   └── algorithm_template.yaml  # Algorithm entry template
│
├── tests/                       # Test suite (pytest)
│   ├── conftest.py              # Shared fixtures
│   ├── test_schema.py
│   ├── test_validate.py
│   ├── test_category_manager.py
│   ├── test_algorithm_registry.py
│   └── ...
│
├── changelog/                   # Detailed changelogs
│   ├── archive/                 # Archived entries
│   ├── en/                      # English changelogs
│   └── zh/                      # Chinese changelogs
│
└── mkdocs/                      # MkDocs configuration
    ├── mkdocs.yml
    └── docs/
```

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     Data Layer (YAML)                       │
│  ┌─────────────┐  ┌─────────────────────────────────────┐  │
│  │ categories  │  │           algorithms/               │  │
│  │   .yaml     │  │  (sequence-alignment.yaml, ...)     │  │
│  └──────┬──────┘  └─────────────────┬───────────────────┘  │
└─────────┼──────────────────────────┼────────────────────────┘
          │                          │
          ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Core Python Modules                      │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │   schema    │  │   validate   │  │ category_manager │   │
│  │  (models)   │  │  (validate)  │  │ (category mgmt)  │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  algorithm_ │  │   readme_    │  │     data_io      │   │
│  │  registry   │  │   generator  │  │  (import/export) │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
          │                          │
          ▼                          ▼
┌─────────────────────────────────────────────────────────────┐
│                    Output Generation                        │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │  README.md  │  │  docs/ (web) │  │  MkDocs site     │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Environment Setup

### Prerequisites

- Python 3.9 or higher
- Git
- (Optional) virtualenv or conda for isolated environments

### Installation

```bash
# Clone repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# Install in development mode
pip install -e ".[dev]"
# Or use: pip install -r requirements.txt

# Verify installation
python -m scripts --help
```

---

## Core Components

### 1. Data Models (`schema.py`)

```python
@dataclass
class AlgorithmEntry:
    id: str                    # Unique identifier
    name: str                  # Algorithm name
    description: str           # Description (50-500 chars)
    purpose: str               # Use case
    time_complexity: str       # Big-O notation
    category: str              # Category ID
    space_complexity: str = "" # Optional
    year: int = 0              # Publication year
    paper_url: str = ""        # Paper URL
    implementation_url: str = ""  # Implementation
    related_tools: list[str] = []
    tags: list[str] = []
    subcategory: str = ""
    difficulty: str = ""       # beginner/intermediate/advanced
    language: str = ""         # Implementation language
```

### 2. Category Manager (`category_manager.py`)

Manages hierarchical categories with support for subcategories:

```python
from scripts.category_manager import CategoryManager

cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')

# Get category by ID
category = cm.get_category('sequence-alignment')

# List all subcategories
subcats = cm.get_subcategories('sequence-alignment')

# Validate category existence
exists = cm.category_exists('variant-calling')
```

### 3. Algorithm Registry (`algorithm_registry.py`)

Central registry for all algorithms with search capabilities:

```python
from scripts.algorithm_registry import AlgorithmRegistry

registry = AlgorithmRegistry('data/algorithms')
registry.load_all()

# Search algorithms
results = registry.search('dynamic programming')

# Get by category
alignment_algos = registry.get_by_category('sequence-alignment')

# Get by tag
gpu_algos = registry.get_by_tag(' gpu-accelerated')

# Get statistics
stats = registry.get_statistics()
```

### 4. Validator (`validate.py`)

Comprehensive validation for data integrity:

```python
from scripts.validate import Validator

validator = Validator()

# Validate single algorithm
result = validator.validate_algorithm(algo_dict)

# Validate all data
result = validator.validate_all('data')

# Check validation result
if not result.is_valid:
    print("Errors:", result.errors)
    print("Warnings:", result.warnings)
```

---

## CLI Commands

### Core Commands

```bash
# Validate all data files
python -m scripts validate

# Generate README.md
python -m scripts generate

# Generate MkDocs pages
python -m scripts mkdocs

# Show statistics
python -m scripts stats

# Search algorithms
python -m scripts search "smith"
python -m scripts search --category sequence-alignment

# Get algorithm details
python -m scripts info smith-waterman

# Compare two algorithms
python -m scripts compare smith-waterman needleman-wunsch

# Export data
python -m scripts export --format json > algorithms.json
python -m scripts export --format yaml > algorithms.yaml
```

---

## Testing

### Running Tests

```bash
# Run all tests
python -m pytest tests/ -v

# Run specific test file
python -m pytest tests/test_validate.py -v

# Run with coverage
python -m pytest tests/ --cov=scripts --cov-report=html

# Run specific test
python -m pytest tests/test_validate.py::test_algorithm_missing_required_field -v
```

### Test Structure

- `test_schema.py` — Data model tests
- `test_validate.py` — Validation logic tests (including Hypothesis property tests)
- `test_category_manager.py` — Category management tests
- `test_algorithm_registry.py` — Registry functionality tests
- `test_data_io.py` — Import/export tests
- `test_cli.py` — CLI integration tests
- `conftest.py` — Shared fixtures

---

## Code Quality

### Linting and Formatting

```bash
# Check formatting
ruff format --check scripts/ tests/

# Apply formatting
ruff format scripts/ tests/

# Check linting
ruff check scripts/ tests/

# Fix linting issues
ruff check --fix scripts/ tests/

# Type checking
mypy scripts/ --ignore-missing-imports
```

### Pre-commit Hooks

```bash
# Install hooks
pre-commit install

# Run all hooks
pre-commit run --all-files
```

---

## Contributing Workflow

### 1. Setup Development Environment

See [Environment Setup](#environment-setup) above.

### 2. Make Changes

- Edit data files in `data/`
- Or edit Python code in `scripts/`
- Or edit documentation in `docs/`

### 3. Validate Changes

```bash
# Validate data
python -m scripts validate

# Run tests
python -m pytest tests/ -v

# Check code quality
ruff check scripts/ tests/
mypy scripts/
```

### 4. Generate Outputs

```bash
# If you edited data or templates
python -m scripts generate      # Update README
python -m scripts mkdocs        # Update docs

# Verify generated outputs are correct
git diff --exit-code -- README.md mkdocs/docs/
```

### 5. Submit Pull Request

- Follow [Conventional Commits](https://www.conventionalcommits.org/)
- Ensure all checks pass
- Include clear PR description

---

## Release Process

### Version Numbering

We follow [Semantic Versioning](https://semver.org/):

- `MAJOR.MINOR.PATCH`
- Breaking changes → MAJOR
- New features → MINOR
- Bug fixes → PATCH

### Release Steps

```bash
# 1. Update changelog
# 2. Create release tag
git tag -a v1.2.0 -m "Release v1.2.0"

# 3. Push tag
git push origin v1.2.0

# 4. Create GitHub Release (via gh CLI or web interface)
gh release create v1.2.0 --generate-notes
```

---

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -e ".[dev]"` |
| YAML syntax errors | Use online YAML validator |
| Test timeouts | Run with `-k` to specify specific tests |
| Generated README differs | Ensure you run `python -m scripts generate` |

### Getting Help

- Check [FAQ]({% link en/faq.md %})
- Open an issue on GitHub
- Join discussions

---

## Resources

- [Python Documentation](https://docs.python.org/3/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [MkDocs Documentation](https://www.mkdocs.org/)
