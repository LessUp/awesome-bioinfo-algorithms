---
title: Contributing Guide
layout: default
nav_order: 5
description: "How to add algorithms, branch conventions, and contribution workflow"
---

# Contributing Guide
{: .no_toc }

Thank you for your interest in contributing to Awesome Bioinformatics Algorithms! This guide will help you get started.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Ways to Contribute

We welcome contributions in the following areas:

| Type | Description |
|:-----|:------------|
| 🆕 **New Algorithms** | Add algorithms to existing categories |
| 📝 **Improvements** | Enhance existing descriptions |
| 🔗 **References** | Add paper links or implementations |
| 🐛 **Bug Fixes** | Fix errors in data or code |
| 📚 **Documentation** | Improve guides and API docs |
| 🧪 **Tests** | Add or improve test coverage |

---

## Quick Start

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms
```

### 2. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS

# Install dependencies
pip install -e ".[dev]"
```

### 3. Create Branch

```bash
git checkout -b feat/add-my-algorithm
```

**Branch naming conventions:**
- `feat/` — New features or algorithms
- `fix/` — Bug fixes
- `docs/` — Documentation updates
- `refactor/` — Code refactoring

### 4. Make Changes

Edit files as needed. For adding algorithms, see [Adding Algorithms](#adding-algorithms) below.

### 5. Validate

```bash
# Validate data
python -m awesome_bioinfo validate

# Run tests
python -m pytest tests/ -v

# Check code quality
ruff check scripts/ tests/
mypy scripts/
```

### 6. Generate Outputs

```bash
# Regenerate README
python -m awesome_bioinfo generate

# Regenerate docs
python -m awesome_bioinfo mkdocs
```

### 7. Commit and Push

```bash
git add .
git commit -m "feat: add algorithm for sequence alignment"
git push origin feat/add-my-algorithm
```

### 8. Create Pull Request

Open a pull request on GitHub with:
- Clear title and description
- Reference to related issues (if any)
- Summary of changes

---

## Adding Algorithms

### Algorithm Data Format

Add your algorithm to the appropriate YAML file in `data/algorithms/`:

```yaml
algorithms:
  - id: your-algorithm-id      # Unique, lowercase, hyphens
    name: Your Algorithm Name
    description: |
      A detailed description (50-500 characters) explaining what 
      the algorithm does, its main features, and typical use cases.
    purpose: What the algorithm is used for
    time_complexity: O(n)      # Big-O notation
    space_complexity: O(n)     # Optional
    category: category-id      # See categories below
    subcategory: sub-id        # Optional
    year: 2024                 # Publication year (optional)
    paper_url: https://...     # Paper DOI/URL (optional)
    implementation_url: https://...  # GitHub/code link (optional)
    related_tools:             # List of related tools (optional)
      - Tool1
      - Tool2
    tags:                      # Relevant tags (optional)
      - tag1
      - tag2
    difficulty: intermediate   # beginner/intermediate/advanced (optional)
    language: Python           # Implementation language (optional)
```

### Available Categories

| Category ID | Name |
|:------------|:-----|
| `sequence-alignment` | Sequence Alignment |
| `assembly` | Sequence Assembly |
| `variant-calling` | Variant Calling |
| `expression-analysis` | Gene Expression Analysis |
| `protein-structure` | Protein Structure Prediction |
| `phylogenetics` | Phylogenetics |
| `functional-annotation` | Functional Annotation |
| `data-compression` | Data Compression |
| `single-cell` | Single-Cell Genomics |
| `metagenomics` | Metagenomics |
| `epigenomics` | Epigenomics |
| `gene-prediction` | Gene Prediction |
| `population-genetics` | Population Genetics |
| `spatial-omics` | Spatial Omics |
| `graph-genomics` | Graph Genomics |
| `protein-language-model` | Protein Language Model |

See `data/categories.yaml` for subcategories.

### Quality Requirements

Before submitting, ensure your algorithm entry:

- ✅ Has a unique ID (lowercase, hyphens)
- ✅ Description is 50-500 characters
- ✅ All required fields are present
- ✅ Category ID is valid
- ✅ Subcategory belongs to the selected category
- ✅ YAML syntax is valid
- ✅ Links are accessible (if provided)
- ✅ Difficulty is one of: `beginner`, `intermediate`, `advanced`

### Example: Adding a New Algorithm

```bash
# 1. Edit the appropriate category file
vim data/algorithms/sequence-alignment.yaml

# 2. Add your algorithm entry following the format above

# 3. Validate
python -m awesome_bioinfo validate

# 4. Check it appears correctly
python -m awesome_bioinfo info your-algorithm-id

# 5. Generate updated README
python -m awesome_bioinfo generate
```

---

## Code Style

### Python Code

We use `ruff` for linting and formatting:

```bash
# Check formatting
ruff format --check scripts/ tests/

# Fix formatting
ruff format scripts/ tests/

# Check style
ruff check scripts/ tests/

# Auto-fix style issues
ruff check --fix scripts/ tests/
```

### YAML Data

- Use 2 spaces for indentation
- Use block scalars (`|`) for multi-line descriptions
- Quote strings with special characters
- Keep lines under 100 characters when possible

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat` — New feature or algorithm
- `fix` — Bug fix
- `docs` — Documentation changes
- `style` — Code style (formatting, missing semi colons, etc.)
- `refactor` — Code refactoring
- `test` — Adding or updating tests
- `chore` — Maintenance tasks

**Examples:**
```
feat: add Smith-Waterman algorithm entry

fix: correct time complexity for Dijkstra's algorithm

docs: update API documentation for search function

refactor: simplify validation logic in validate.py
```

---

## Testing

### Running Tests

```bash
# All tests
python -m pytest tests/ -v

# Specific test file
python -m pytest tests/test_validate.py -v

# Specific test
python -m pytest tests/test_validate.py::test_algorithm_valid -v

# With coverage
python -m pytest tests/ --cov=scripts --cov-report=html
```

### Writing Tests

When adding new features, please include tests:

```python
# tests/test_new_feature.py
def test_new_feature():
    """Test description."""
    result = new_feature_function()
    assert result is True
```

---

## Pull Request Process

### Before Submitting

1. ✅ All tests pass
2. ✅ Data validation passes
3. ✅ Code style checks pass
4. ✅ README has been regenerated (if data changed)
5. ✅ Documentation updated (if needed)

### PR Description Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New algorithm
- [ ] Documentation update
- [ ] Refactoring

## Checklist
- [ ] Tests pass
- [ ] Validation passes
- [ ] README regenerated (if data changed)
- [ ] Follows contributing guidelines

## Related Issues
Fixes #123
```

### Review Process

1. Automated tests run on your PR
2. Maintainers review within 3-5 days
3. Address any requested changes
4. Once approved, your PR will be merged

---

## Getting Help

- 💬 Open an issue for questions
- 📖 Read the [FAQ]({% link en/faq.md %})
- 🔍 Check existing issues

---

## License

By contributing, you agree that your contributions will be licensed under CC0 1.0 Universal (Public Domain).

Thank you for contributing! 🎉
