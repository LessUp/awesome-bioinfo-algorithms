# Algorithm Schema Specification

## Purpose

Define the YAML schema for algorithm entries, including required and optional fields, validation rules, and constraints to ensure data integrity and consistency across the collection.

## Requirements

### Requirement: Algorithm ID Format

The algorithm ID SHALL follow kebab-case format and be globally unique.

#### Scenario: Valid algorithm ID
- **GIVEN** a new algorithm entry
- **WHEN** the `id` field is set
- **THEN** the ID MUST match pattern `^[a-z0-9]+(-[a-z0-9]+)*$`
- **AND** the ID MUST be globally unique across all files
- **AND** the ID length MUST be between 3 and 50 characters

#### Scenario: Invalid algorithm ID format
- **GIVEN** an algorithm entry with ID "My_Algorithm"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error "ID must be lowercase with hyphens"

#### Scenario: Duplicate algorithm ID
- **GIVEN** an algorithm entry with ID "smith-waterman"
- **WHEN** another entry with the same ID exists
- **THEN** validation SHALL fail with error "Duplicate ID: smith-waterman"

### Requirement: Algorithm Name

The algorithm name SHALL be a human-readable identifier.

#### Scenario: Valid name
- **GIVEN** an algorithm entry
- **WHEN** the `name` field is set
- **THEN** the length MUST be between 3 and 100 characters
- **AND** the name MAY contain spaces, hyphens, and parentheses

### Requirement: Algorithm Description

The algorithm description SHALL be informative and within bounds.

#### Scenario: Valid description length
- **GIVEN** a description text
- **WHEN** the text is trimmed
- **THEN** the length MUST be between 50 and 500 characters

#### Scenario: Description too short
- **GIVEN** a description of 30 characters
- **WHEN** validation is run
- **THEN** validation SHALL fail with error indicating minimum length

#### Scenario: Description too long
- **GIVEN** a description of 600 characters
- **WHEN** validation is run
- **THEN** validation SHALL fail with error indicating maximum length

### Requirement: Algorithm Purpose

The algorithm purpose SHALL describe the primary use case.

#### Scenario: Valid purpose
- **GIVEN** a purpose text
- **WHEN** the text is validated
- **THEN** the length MUST be between 10 and 200 characters

### Requirement: Time Complexity

The time complexity SHALL follow Big-O notation.

#### Scenario: Valid time complexity
- **GIVEN** a time complexity value
- **WHEN** validation is run
- **THEN** the value MUST match Big-O notation format (e.g., `O(n)`, `O(n^2)`, `O(mn)`, `O(n log n)`)

#### Scenario: Invalid time complexity
- **GIVEN** a time complexity value "fast"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error "Invalid Big-O notation"

### Requirement: Category Assignment

The category SHALL reference a valid category from the taxonomy.

#### Scenario: Valid category
- **GIVEN** a category value
- **WHEN** validation is run
- **THEN** the category MUST exist in `data/categories.yaml`

#### Scenario: Invalid category
- **GIVEN** a category "unknown-category"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error "Invalid category: unknown-category"

### Requirement: Subcategory Assignment

The subcategory SHALL belong to the specified category if provided.

#### Scenario: Valid subcategory
- **GIVEN** a category and subcategory pair
- **WHEN** validation is run
- **THEN** the subcategory MUST be listed under the category in `data/categories.yaml`

#### Scenario: Invalid subcategory
- **GIVEN** category "sequence-alignment" and subcategory "invalid-sub"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error indicating the subcategory is not valid for the category

### Requirement: Tag Format

All tags SHALL be lowercase with hyphens.

#### Scenario: Valid tag format
- **GIVEN** a tag value
- **WHEN** validation is run
- **THEN** the tag MUST match pattern `^[a-z0-9]+(-[a-z0-9]+)*$`
- **AND** 3-10 tags per algorithm are RECOMMENDED

#### Scenario: Invalid tag format
- **GIVEN** a tag "Dynamic_Programming"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error "Tag must be lowercase with hyphens"

### Requirement: Difficulty Level

The difficulty SHALL be one of the allowed values if provided.

#### Scenario: Valid difficulty
- **GIVEN** a difficulty value
- **WHEN** validation is run
- **THEN** the value MUST be one of: `beginner`, `intermediate`, `advanced`

#### Scenario: Invalid difficulty
- **GIVEN** a difficulty value "expert"
- **WHEN** validation is run
- **THEN** validation SHALL fail with error listing allowed values

### Requirement: Year Range

The year SHALL be within valid range if provided.

#### Scenario: Valid year
- **GIVEN** a year value
- **WHEN** validation is run
- **THEN** the year MUST be between 1970 and 2030

### Requirement: URL Format

All URLs SHALL be valid URL format if provided.

#### Scenario: Valid URL
- **GIVEN** a URL value for `paper_url` or `implementation_url`
- **WHEN** validation is run
- **THEN** the URL MUST be a valid URL format

### Requirement: References Structure

References SHALL follow the defined object schema.

#### Scenario: Valid reference
- **GIVEN** a reference object
- **WHEN** validation is run
- **THEN** `title` (string, required) SHALL be present
- **AND** `url` (string, required) SHALL be present and valid
- **AND** `type` (string, required) SHALL be one of: `tutorial`, `blog`, `video`, `book`, `documentation`, `slides`
- **AND** `author` (string, optional) MAY be present
- **AND** `year` (integer, optional) MAY be present

## Schema Summary

### Required Fields

| Field | Type | Constraints |
|-------|------|-------------|
| `id` | string | kebab-case, 3-50 chars, unique |
| `name` | string | 3-100 chars |
| `description` | string | 50-500 chars (trimmed) |
| `purpose` | string | 10-200 chars |
| `time_complexity` | string | Big-O notation |
| `category` | string | must exist in categories.yaml |

### Optional Fields

| Field | Type | Constraints |
|-------|------|-------------|
| `space_complexity` | string | Big-O notation |
| `year` | integer | 1970-2030 |
| `paper_url` | string | valid URL |
| `implementation_url` | string | valid URL |
| `related_tools` | array[string] | each 2-50 chars |
| `tags` | array[string] | kebab-case each |
| `subcategory` | string | must belong to category |
| `difficulty` | string | beginner/intermediate/advanced |
| `language` | string | implementation language |
| `references` | array[object] | see reference schema |

## Example Valid Entry

```yaml
algorithms:
  - id: smith-waterman
    name: Smith-Waterman
    description: |
      Classic local sequence alignment algorithm using dynamic programming
      to find the highest-scoring local similarity region between two sequences.
      This algorithm guarantees finding the optimal local alignment.
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
