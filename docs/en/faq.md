---
title: FAQ
layout: default
nav_order: 4
description: "Frequently asked questions and troubleshooting guide"
---

# Frequently Asked Questions
{: .no_toc }

Find answers to common questions about using and contributing to the Awesome Bioinformatics Algorithms project.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## General Questions

### What is this project?

Awesome Bioinformatics Algorithms is a curated, open-source collection of bioinformatics algorithms. It provides:

- 📊 Structured algorithm data in YAML format
- 🔍 Search and comparison capabilities
- 📖 Auto-generated documentation
- 🌐 Bilingual support (English and Chinese)

All algorithms include time/space complexity, related papers, implementation links, and tags.

### Who maintains this project?

The project is community-maintained under the LessUp organization. Contributions are welcome from anyone in the bioinformatics community.

### How often is the project updated?

Updates vary based on community contributions. We typically review and merge pull requests within a few days.

---

## Getting Started

### How do I set up the development environment?

```bash
# Clone the repository
git clone https://github.com/LessUp/awesome-bioinfo-algorithms.git
cd awesome-bioinfo-algorithms

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate    # Windows

# Install dependencies
pip install -e ".[dev]"

# Verify setup
python -m scripts validate
```

### What Python version is required?

Python 3.9 or higher is required. We test against Python 3.9, 3.10, 3.11, and 3.12.

### Do I need bioinformatics expertise to contribute?

No! While bioinformatics knowledge is helpful for adding algorithms, you can contribute in many ways:

- Improving documentation
- Fixing typos and formatting
- Adding test cases
- Improving the Python tooling

---

## Adding Algorithms

### What information is required for a new algorithm?

**Required fields:**

| Field | Description | Example |
|:------|:------------|:--------|
| `id` | Unique identifier (lowercase, hyphens) | `smith-waterman` |
| `name` | Algorithm name | `Smith-Waterman` |
| `description` | Description (50-500 characters) | Description of the algorithm |
| `purpose` | What the algorithm is used for | `Local sequence alignment` |
| `time_complexity` | Big-O notation | `O(mn)` |
| `category` | Must be a valid category ID | `sequence-alignment` |

**Optional but recommended fields:**
- `space_complexity` — Space complexity
- `year` — Publication year
- `paper_url` — Link to original paper
- `implementation_url` — Link to reference implementation
- `tags` — Relevant tags for categorization

### How do I choose the right category?

Check [`data/categories.yaml`](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/data/categories.yaml) for the complete list of categories and subcategories. If you're unsure, you can:

1. Search similar algorithms with `python -m scripts search "keyword"`
2. Check which category they belong to
3. Use the same category for your algorithm

### Why is my description being rejected?

Descriptions must be **50-500 characters** after trimming. This ensures:

- Enough detail to understand what the algorithm does
- Concise enough for readability in listings

**Example of a good description:**
```yaml
description: |
  The Smith-Waterman algorithm performs local sequence alignment, 
  identifying the most similar subsequences between two sequences. 
  It uses dynamic programming with guarantees of optimal local alignment.
```

### Can I add a new category?

Yes, but please open an issue first to discuss the addition. New categories should:

- Represent a distinct bioinformatics domain
- Have broad applicability
- Be able to contain multiple algorithms

### How do I choose difficulty level?

Use the `difficulty` field with one of:

- `beginner` — Basic algorithms, easy to understand and implement
- `intermediate` — Moderate complexity, requires some background
- `advanced` — Complex algorithms, research-level implementations

---

## Using the CLI

### How do I search for algorithms?

```bash
# Basic search
python -m scripts search "alignment"

# Search in specific category
python -m scripts search "fast" --category sequence-alignment

# Case-insensitive search
python -m scripts search "BLAST"
```

### How do I compare two algorithms?

```bash
python -m scripts compare smith-waterman needleman-wunsch
```

This will show a side-by-side comparison of:
- Time/space complexity
- Use cases
- Related tools

### How do I export data?

```bash
# Export as JSON
python -m scripts export --format json > algorithms.json

# Export as YAML
python -m scripts export --format yaml > algorithms.yaml
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'scripts'"

**Cause:** Package not installed in development mode.

**Solution:**
```bash
pip install -e ".[dev]"
```

### "ValidationError: description too short"

**Cause:** Description is fewer than 50 characters.

**Solution:** Expand your description to at least 50 characters.

### YAML syntax errors

**Symptoms:** Parser errors when running `validate`

**Solutions:**
1. Use spaces, not tabs, for indentation
2. Quote strings with special characters
3. Use a YAML validator: [yaml-validator.com](https://yaml-validator.com)

### Tests are failing with Hypothesis errors

**Cause:** Property-based tests might be too slow on your machine.

**Solution:** This is usually handled automatically, but you can run specific tests:

```bash
# Run only validation tests
python -m pytest tests/test_validate.py -v

# Run specific test
python -m pytest tests/test_validate.py::test_algorithm_valid -v
```

### "git diff --exit-code" fails in CI

**Cause:** Generated files are out of date.

**Solution:**
```bash
# Regenerate all outputs
python -m scripts generate
python -m scripts mkdocs

# Check differences
git diff

# Commit changes
git add README.md mkdocs/docs/
git commit -m "chore: regenerate documentation"
```

---

## Contributing

### How can I contribute?

We welcome contributions in these areas:

1. **Adding new algorithms** — Follow our algorithm template
2. **Improving descriptions** — Make existing content more accurate
3. **Adding references** — Link to papers and implementations
4. **Bug fixes** — Fix errors in data or code
5. **Documentation** — Improve guides and API docs

### What is the contribution workflow?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run validation: `python -m scripts validate`
5. Run tests: `python -m pytest tests/ -v`
6. Generate outputs: `python -m scripts generate`
7. Submit a pull request

### What are the commit message conventions?

We follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add new algorithm for sequence alignment
fix: correct time complexity of algorithm XYZ
docs: update API reference for search function
refactor: simplify validation logic
test: add test for edge cases
```

### How long until my PR is reviewed?

We aim to review PRs within 3-5 days. During busy periods, it may take up to a week.

---

## Data Questions

### How is the data organized?

Algorithm data is stored in YAML files under `data/algorithms/`, organized by category:

```
data/algorithms/
├── sequence-alignment.yaml
├── assembly.yaml
├── variant-calling.yaml
└── ...
```

Each file contains multiple algorithm entries under the `algorithms:` key.

### Can I use this data in my own project?

Yes! The data is licensed under CC0 1.0 (Public Domain). You can:

- Use the data freely
- Modify it
- Redistribute it
- Use it commercially

No attribution required, though it's appreciated.

### How do I report an error in algorithm data?

Open an issue on GitHub describing:
- The algorithm ID
- What's incorrect
- What the correct information should be

Or submit a pull request with the fix.

---

## Technical Questions

### Why Jekyll for documentation?

Jekyll integrates seamlessly with GitHub Pages, providing:
- Free hosting
- Version control integration
- Simple Markdown-based content
- Built-in theming

### Why YAML instead of JSON?

YAML was chosen for:
- Better readability with comments
- Support for multi-line strings
- Cleaner syntax for bioinformaticians
- Easier manual editing

### Can I use the Python API in my own code?

Yes! After installing the package:

```python
from scripts.algorithm_registry import AlgorithmRegistry

registry = AlgorithmRegistry()
registry.load_all()

# Use in your application
algorithms = registry.search("alignment")
```

---

## Still Have Questions?

- 📖 Read the [Contributing Guide](https://github.com/LessUp/awesome-bioinfo-algorithms/blob/master/CONTRIBUTING.md)
- 📚 Check the [API Documentation]({% link en/api.md %})
- 🔍 Search existing [GitHub Issues](https://github.com/LessUp/awesome-bioinfo-algorithms/issues)
- 💬 Open a new issue with your question
