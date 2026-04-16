# Algorithm Entry Schema Specification

## Overview

**Spec ID**: DB-SCHEMA-001  
**Version**: 1.0.0  
**Status**: Implemented  
**Created**: 2026-04-17

This document specifies the schema for algorithm entries in the YAML database.

## File Structure

### Location
```
data/algorithms/
├── sequence-alignment.yaml
├── assembly.yaml
├── variant-calling.yaml
└── ... (one file per category)
```

### File Format
Each file contains a list of algorithm entries under the `algorithms:` key.

```yaml
algorithms:
  - id: algorithm-id
    name: Algorithm Name
    # ... other fields
```

## Schema Definition

### Required Fields

#### `id` (string)
**Type**: String  
**Required**: Yes  
**Format**: `^[a-z0-9]+(-[a-z0-9]+)*$` (lowercase, hyphens)  
**Unique**: Globally unique across all files  
**Example**: `smith-waterman`

**Validation Rules**:
- Must be lowercase
- Must use hyphens as separators (not underscores)
- Must be unique across entire repository
- Length: 3-50 characters

#### `name` (string)
**Type**: String  
**Required**: Yes  
**Example**: `Smith-Waterman`

**Validation Rules**:
- Length: 3-100 characters
- Can contain spaces, hyphens, parentheses

#### `description` (string)
**Type**: String (multiline YAML)  
**Required**: Yes  
**Example**:
```yaml
description: |
  Classic local sequence alignment algorithm using dynamic programming
  to find the highest-scoring local similarity region.
```

**Validation Rules**:
- Length: 50-500 characters (after trimming)
- Must be informative and concise
- Should include: what it does, how it works, when to use it

#### `purpose` (string)
**Type**: String  
**Required**: Yes  
**Example**: `Local sequence alignment, finding similar regions`

**Validation Rules**:
- Length: 10-200 characters
- Should describe the primary use case

#### `time_complexity` (string)
**Type**: String  
**Required**: Yes  
**Example**: `O(mn)`, `O(n log n)`, `O(n^2)`

**Validation Rules**:
- Must follow Big-O notation format
- Should use standard complexity notation

#### `category` (string)
**Type**: String  
**Required**: Yes  
**Example**: `sequence-alignment`

**Validation Rules**:
- Must match a valid category ID from `data/categories.yaml`
- Cannot be changed without updating category taxonomy

### Optional Fields

#### `space_complexity` (string)
**Type**: String  
**Required**: No  
**Example**: `O(mn)`, `O(n)`

**Validation Rules**:
- Same format as `time_complexity`

#### `year` (integer)
**Type**: Integer  
**Required**: No  
**Example**: `1981`

**Validation Rules**:
- Range: 1970-2030
- Should be the year of original publication

#### `paper_url` (string, URL)
**Type**: String  
**Required**: No  
**Example**: `https://doi.org/10.1016/0022-2836(81)90087-5`

**Validation Rules**:
- Must be valid URL format
- Should point to original paper or DOI

#### `implementation_url` (string, URL)
**Type**: String  
**Required**: No  
**Example**: `https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library`

**Validation Rules**:
- Must be valid URL format
- Should point to reference implementation

#### `related_tools` (array of strings)
**Type**: Array[String]  
**Required**: No  
**Example**: `['BLAST', 'FASTA', 'SSEARCH']`

**Validation Rules**:
- Each item: 2-50 characters
- Should list related software tools

#### `tags` (array of strings)
**Type**: Array[String]  
**Required**: No  
**Example**: `['dynamic-programming', 'local-alignment', 'classic']`

**Validation Rules**:
- Each tag: lowercase, hyphens allowed
- Format: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Recommended: 3-10 tags per algorithm

#### `subcategory` (string)
**Type**: String  
**Required**: No  
**Example**: `pairwise-alignment`

**Validation Rules**:
- Must be valid subcategory under the specified `category`
- Defined in `data/categories.yaml`

#### `difficulty` (string, enum)
**Type**: String  
**Required**: No  
**Allowed Values**: `beginner`, `intermediate`, `advanced`  
**Example**: `intermediate`

**Validation Rules**:
- Must be one of the three allowed values
- Used for filtering and learning paths

#### `language` (string)
**Type**: String  
**Required**: No  
**Example**: `C++`, `Python`, `R`

**Validation Rules**:
- Should be the primary implementation language
- Can be comma-separated for multiple languages

#### `references` (array of objects)
**Type**: Array[Object]  
**Required**: No  

**Object Schema**:
```yaml
references:
  - title: "Tutorial: Smith-Waterman Implementation"
    url: "https://example.com/tutorial"
    type: tutorial
    author: "John Doe"
    year: 2023
```

**Fields**:
- `title` (string, required): Reference title
- `url` (string, required): Valid URL
- `type` (string, required): One of:
  - `tutorial`
  - `blog`
  - `video`
  - `book`
  - `documentation`
  - `slides`
- `author` (string, optional): Author name
- `year` (integer, optional): Publication year

## Complete Example

```yaml
algorithms:
  - id: smith-waterman
    name: Smith-Waterman
    description: |
      Classic local sequence alignment algorithm using dynamic programming
      to find the highest-scoring local similarity region between two sequences.
      This algorithm guarantees finding the optimal local alignment and is
      suitable for detecting conserved regions and functional domains.
    purpose: Local sequence alignment, finding similar regions
    time_complexity: O(mn)
    space_complexity: O(mn)
    category: sequence-alignment
    subcategory: pairwise-alignment
    year: 1981
    paper_url: https://doi.org/10.1016/0022-2836(81)90087-5
    implementation_url: https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library
    related_tools:
      - BLAST
      - FASTA
      - SSEARCH
    tags:
      - dynamic-programming
      - local-alignment
      - classic
    difficulty: intermediate
    language: C
    references:
      - title: "Complete Striped Smith-Waterman Library"
        url: "https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library"
        type: documentation
        author: "Mengyao Zhao"
        year: 2020
```

## Validation Constraints

### Cross-File Constraints
1. **Unique IDs**: No duplicate `id` across all YAML files
2. **Valid Category**: `category` must exist in `data/categories.yaml`
3. **Valid Subcategory**: If `subcategory` present, must belong to `category`

### Intra-Entry Constraints
1. **Description Length**: 50-500 characters (trimmed)
2. **Tag Format**: All tags must be lowercase with hyphens
3. **URL Format**: All URLs must be valid format

### Category Taxonomy
Categories and subcategories are defined in `data/categories.yaml`:

```yaml
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
      - reference-guided-assembly
  # ... more categories
```

## Schema Evolution

### Adding New Fields
1. Update this specification
2. Update `AlgorithmEntry` dataclass in `scripts/schema.py`
3. Update validation logic in `scripts/validate.py`
4. Update templates if field should appear in output
5. Run `python -m scripts validate` to check existing data

### Deprecating Fields
1. Mark field as deprecated in this spec
2. Add deprecation warning to validator
3. Remove field from new entries
4. Migrate existing entries or remove

### Breaking Changes
Breaking changes require:
- RFC approval
- Migration plan
- Community notification
- Grace period for existing entries

## Templates

### Algorithm Entry Template
See `templates/algorithm_template.yaml` for a starter template:

```yaml
algorithms:
  - id: your-algorithm-id
    name: Your Algorithm Name
    description: |
      Brief description of the algorithm (50-500 characters).
      Include principles, features, and use cases.
    purpose: Main purpose of the algorithm
    time_complexity: O(n)
    space_complexity: O(n)
    category: category-id
    subcategory: sub-id
    year: 2024
    paper_url: https://doi.org/...
    implementation_url: https://github.com/...
    related_tools:
      - Related Tool 1
      - Related Tool 2
    tags:
      - tag1
      - tag2
    difficulty: beginner
    language: Python
```

## Common Mistakes to Avoid

1. ❌ **Duplicate IDs**: Each algorithm must have unique ID
2. ❌ **Invalid category**: Check `data/categories.yaml` for valid IDs
3. ❌ **Description too short/long**: Keep between 50-500 chars
4. ❌ **Wrong tag format**: Tags must be lowercase with hyphens
5. ❌ **Invalid URLs**: Test all links before committing
6. ❌ **Missing required fields**: Check schema for required vs optional

## Validation Examples

### Valid Entry
```yaml
- id: needleman-wunsch
  name: Needleman-Wunsch
  description: |
    Global sequence alignment algorithm using dynamic programming for
    end-to-end alignment of two complete sequences.
  purpose: Global sequence alignment
  time_complexity: O(mn)
  space_complexity: O(mn)
  category: sequence-alignment
  subcategory: pairwise-alignment
  year: 1970
  tags:
    - dynamic-programming
    - global-alignment
    - classic
```

### Invalid Entry (errors highlighted)
```yaml
- id: Needleman_Wunsch  # ❌ Must be lowercase, use hyphens
  name: NW              # ❌ Too short (min 3 chars)
  description: Short    # ❌ Too short (min 50 chars)
  purpose: x            # ❌ Too short (min 10 chars)
  time_complexity: fast # ❌ Not valid Big-O notation
  category: unknown     # ❌ Invalid category
  tags:
    - Dynamic_Programming  # ❌ Must be lowercase
```

## Related Documents

- Product Vision: `/specs/product/000-product-vision.md`
- Core Architecture: `/specs/rfc/0001-core-architecture.md`
- CLI Interface: `/specs/api/001-cli-interface.md`
- Category Taxonomy: `data/categories.yaml`

## Change History

| Date | Version | Change | Author |
|------|---------|--------|--------|
| 2026-04-17 | 1.0.0 | Initial schema specification | Community |
