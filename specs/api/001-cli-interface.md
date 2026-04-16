# CLI Interface Specification

## Overview

**Spec ID**: API-SPEC-001  
**Version**: 1.0.0  
**Status**: Implemented  
**Created**: 2026-04-17

This document specifies the command-line interface (CLI) for the Awesome Bioinformatics Algorithms project.

## Entry Point

```bash
python -m scripts <command> [options]
```

## Global Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--help` | `-h` | Show help message | - |
| `--verbose` | `-v` | Enable verbose output | `False` |
| `--quiet` | `-q` | Suppress non-essential output | `False` |

## Commands

### 1. validate

Validate all YAML data against schema and constraints.

**Syntax**:
```bash
python -m scripts validate
```

**Options**: None

**Output**:
```
Validation Results:
✓ Passed: 201 algorithms
✗ Errors: 0
⚠ Warnings: 2

Warnings:
- algorithm-xyz: description is close to minimum length (52 chars)
- algorithm-abc: missing optional field 'year'
```

**Exit Codes**:
- `0` - Validation passed (warnings allowed)
- `1` - Validation failed (errors present)

**Error Format**:
```
Validation Errors:
✗ algorithm-123: description too short (32 chars, min 50)
✗ algorithm-456: invalid category 'unknown-category'
```

### 2. stats

Display statistics about the algorithm collection.

**Syntax**:
```bash
python -m scripts stats
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--format` | `-f` | Output format (`text`, `json`, `markdown`) | `text` |

**Output (text)**:
```
Algorithm Collection Statistics
================================
Total Algorithms: 201
Categories: 16
Subcategories: 45
Unique Tags: 399

Top Categories:
1. Sequence Alignment: 25 algorithms
2. Sequence Assembly: 18 algorithms
3. Variant Calling: 22 algorithms
...
```

**Exit Codes**:
- `0` - Success

### 3. search

Search algorithms by name, category, tags, or description.

**Syntax**:
```bash
python -m scripts search <query> [options]
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--category` | `-c` | Filter by category | - |
| `--subcategory` | `-s` | Filter by subcategory | - |
| `--tags` | `-t` | Filter by tags (comma-separated) | - |
| `--difficulty` | `-d` | Filter by difficulty (`beginner`, `intermediate`, `advanced`) | - |
| `--year` | `-y` | Filter by year | - |
| `--limit` | `-l` | Limit results | `50` |

**Examples**:
```bash
# Search by name
python -m scripts search smith

# Search by category
python -m scripts search --category sequence-alignment

# Search by tags
python -m scripts search --tags dynamic-programming,fast

# Combined search
python -m scripts search smith --category sequence-alignment --difficulty beginner
```

**Output**:
```
Search Results: "smith" (3 matches)
=====================================
1. smith-waterman (Smith-Waterman)
   Category: sequence-alignment/pairwise-alignment
   Year: 1981
   Tags: dynamic-programming, local-alignment, classic

2. complete-striped-smith-waterman (Complete Striped Smith-Waterman)
   Category: sequence-alignment/pairwise-alignment
   Year: 2000
   Tags: smith-waterman, optimized

3. smith-waterman-gotoh (Smith-Waterman-Gotoh)
   Category: sequence-alignment/pairwise-alignment
   Year: 1995
   Tags: dynamic-programming, affine-gap
```

**Exit Codes**:
- `0` - Success (matches found)
- `1` - No matches found

### 4. info

Display detailed information about a specific algorithm.

**Syntax**:
```bash
python -m scripts info <algorithm-id>
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--format` | `-f` | Output format (`text`, `json`, `yaml`) | `text` |

**Output (text)**:
```
Algorithm: smith-waterman
Name: Smith-Waterman
Year: 1981
Category: sequence-alignment
Subcategory: pairwise-alignment
Difficulty: intermediate

Description:
  Classic local sequence alignment algorithm using dynamic programming
  to find the highest-scoring local similarity region between two sequences.

Purpose: Local sequence alignment, finding similar regions
Time Complexity: O(mn)
Space Complexity: O(mn)

Paper: https://doi.org/10.1016/0022-2836(81)90087-5
Implementation: https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library

Related Tools: BLAST, FASTA, SSEARCH
Tags: dynamic-programming, local-alignment, classic
```

**Exit Codes**:
- `0` - Success
- `1` - Algorithm not found

**Error Output**:
```
Error: Algorithm 'unknown-algo' not found.
Use 'python -m scripts search' to find existing algorithms.
```

### 5. compare

Compare multiple algorithms side-by-side.

**Syntax**:
```bash
python -m scripts compare <id1> <id2> [id3 ...]
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--fields` | `-f` | Fields to compare (comma-separated) | All fields |
| `--format` | `-m` | Output format (`text`, `markdown`, `json`) | `text` |

**Example**:
```bash
python -m scripts compare smith-waterman needleman-wunsch
```

**Output**:
```
Algorithm Comparison
====================

Field              | smith-waterman          | needleman-wunsch
-------------------|------------------------|------------------------
Name               | Smith-Waterman         | Needleman-Wunsch
Year               | 1981                   | 1970
Category           | sequence-alignment     | sequence-alignment
Subcategory        | pairwise-alignment     | pairwise-alignment
Time Complexity    | O(mn)                  | O(mn)
Space Complexity   | O(mn)                  | O(mn)
Purpose            | Local sequence align.  | Global sequence align.

Key Differences:
- smith-waterman performs LOCAL alignment
- needleman-wunsch performs GLOBAL alignment
```

**Exit Codes**:
- `0` - Success
- `1` - One or more algorithms not found

### 6. export

Export algorithm data in various formats.

**Syntax**:
```bash
python -m scripts export --format <format> [options]
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--format` | `-f` | Export format (`json`, `yaml`, `csv`, `markdown`) | Required |
| `--category` | `-c` | Filter by category | All |
| `--output` | `-o` | Output file path (stdout if omitted) | stdout |
| `--pretty` | `-p` | Pretty-print JSON/YAML | `False` |

**Examples**:
```bash
# Export all as JSON
python -m scripts export --format json > /tmp/algorithms.json

# Export specific category as YAML
python -m scripts export --format yaml --category sequence-alignment

# Export as CSV
python -m scripts export --format csv -o algorithms.csv
```

**Exit Codes**:
- `0` - Success
- `1` - Invalid format or export failed

### 7. generate

Generate README.md from template and algorithm data.

**Syntax**:
```bash
python -m scripts generate
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output file path | `README.md` |
| `--template` | `-t` | Template file path | `templates/readme_template.md` |
| `--lang` | `-l` | Language (`en`, `zh`) | `en` |

**Examples**:
```bash
# Generate English README
python -m scripts generate

# Generate Chinese README
python -m scripts generate --lang zh --output README.zh-CN.md
```

**Exit Codes**:
- `0` - Success
- `1` - Generation failed (template error or invalid data)

**Validation**:
After generation, CI runs:
```bash
git diff --exit-code -- README.md
```
This ensures generated files are up-to-date with source data.

### 8. mkdocs

Generate MkDocs documentation site.

**Syntax**:
```bash
python -m scripts mkdocs
```

**Options**:
| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--output` | `-o` | Output directory | `mkdocs/docs/` |
| `--serve` | `-s` | Start development server | `False` |

**Examples**:
```bash
# Generate MkDocs site
python -m scripts mkdocs

# Preview locally
python -m scripts mkdocs --serve
```

**Exit Codes**:
- `0` - Success
- `1` - Generation failed

**Post-Generation**:
CI runs:
```bash
python scripts/generate_mkdocs.py
mkdocs build -f mkdocs/mkdocs.yml -d ./_site
git diff --exit-code -- mkdocs/docs/
```

## Error Handling

### General Error Format

```
Error: <error message>
Hint: <helpful suggestion>

Use 'python -m scripts --help' for usage information.
```

### Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `Algorithm not found` | Invalid algorithm ID | Use `search` to find valid IDs |
| `Invalid category` | Category doesn't exist | Check `data/categories.yaml` |
| `YAML parse error` | Malformed YAML | Validate file syntax |
| `Template not found` | Missing template file | Check templates directory |

## Output Standards

1. **Human-readable by default**: All text output should be readable without parsing
2. **Machine-readable options**: Support `--format json` for programmatic access
3. **Consistent encoding**: UTF-8 for all output
4. **Bilingual support**: Support Chinese characters in output
5. **Exit codes**: Always return appropriate exit codes

## Testing Requirements

Each command must have:
1. Unit tests for core logic
2. Integration tests with CLI isolation (`monkeypatch`)
3. Error case tests (invalid inputs, missing data)
4. Output format tests (text, JSON, etc.)

See `/specs/testing/001-cli-tests.md` for detailed test specifications.

## Change History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-04-17 | 1.0.0 | Initial specification | Community |
