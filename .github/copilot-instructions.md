# Copilot Instructions

## Project Overview

**Awesome Bioinformatics Algorithms** - A curated collection of 195 bioinformatics algorithms with complexity analysis, implementation links, and bilingual documentation.

## Authority Hierarchy

1. **OpenSpec Specs** (`openspec/specs/`) - Single source of truth for requirements
2. **AGENTS.md** - Project-specific development workflow
3. **CLAUDE.md** - Architecture and module documentation
4. **This file** - Quick reference for Copilot

## Key Commands

```bash
# Validation
python -m awesome_bioinfo validate
python -m awesome_bioinfo stats

# Generation (run after data changes)
python -m awesome_bioinfo generate    # README.md
python -m awesome_bioinfo mkdocs      # mkdocs/docs/

# Testing
pytest tests/ -v
ruff check awesome_bioinfo tests
mypy awesome_bioinfo --ignore-missing-imports
```

## Data Structure

- `data/categories.yaml` - 16 top-level categories
- `data/algorithms/*.yaml` - Algorithm entries (one file per category)
- `templates/` - README and algorithm templates

## Required Algorithm Fields

- `id` (lowercase, hyphenated, unique)
- `name`, `description` (50-500 chars), `purpose`
- `time_complexity`, `category`

## Generated Files (Do Not Edit)

- `README.md`
- `mkdocs/docs/`

## Correct URLs

- Site: `https://lessup.github.io/awesome-bioinfo-algorithms/`
- Repo: `https://github.com/LessUp/awesome-bioinfo-algorithms`
