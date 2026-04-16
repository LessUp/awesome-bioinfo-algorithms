---
title: API Documentation
layout: default
nav_order: 2
description: "Public API reference with code examples and best practices"
---

# API Documentation
{: .no_toc }

Complete reference for the Awesome Bioinformatics Algorithms Python API.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Quick Start

```python
from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager

# Load all data
registry = AlgorithmRegistry('data/algorithms')
registry.load_all()

cm = CategoryManager()
cm.load_categories('data/categories.yaml')

# Example: Get all sequence alignment algorithms
algorithms = registry.get_by_category('sequence-alignment')
print(f"Found {len(algorithms)} algorithms")

# Example: Search for dynamic programming algorithms
results = registry.search('dynamic programming')
```

---

## AlgorithmRegistry

Manages algorithm entries loaded from YAML files.

### Constructor

```python
AlgorithmRegistry(data_dir: str = "data/algorithms")
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `data_dir` | `str` | `"data/algorithms"` | Path to algorithms directory |

**Example:**

```python
# Default usage
registry = AlgorithmRegistry()

# Custom path
registry = AlgorithmRegistry('/path/to/algorithms')
```

---

### Methods

#### load_all()

```python
load_all() -> list[AlgorithmEntry]
```

Load all algorithms from YAML files in the data directory.

**Returns:** List of `AlgorithmEntry` objects

**Example:**

```python
registry = AlgorithmRegistry()
algorithms = registry.load_all()
print(f"Loaded {len(algorithms)} algorithms")
```

---

#### get_by_category()

```python
get_by_category(category_id: str) -> list[AlgorithmEntry]
```

Get all algorithms in a specific category, including subcategories.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `category_id` | `str` | Category identifier (e.g., 'sequence-alignment') |

**Returns:** List of `AlgorithmEntry` objects

**Example:**

```python
# Get all sequence alignment algorithms
alignment_algos = registry.get_by_category('sequence-alignment')

# Get all variant calling algorithms
variant_algos = registry.get_by_category('variant-calling')
```

---

#### get_by_subcategory()

```python
get_by_subcategory(subcategory_id: str) -> list[AlgorithmEntry]
```

Get all algorithms in a specific subcategory.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `subcategory_id` | `str` | Subcategory identifier (e.g., 'pairwise') |

**Returns:** List of `AlgorithmEntry` objects

**Example:**

```python
# Get pairwise alignment algorithms
pairwise_algos = registry.get_by_subcategory('pairwise')

# Get de novo assembly algorithms
de_novo_algos = registry.get_by_subcategory('de-novo')
```

---

#### get_by_tag()

```python
get_by_tag(tag: str) -> list[AlgorithmEntry]
```

Get all algorithms with a specific tag.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `tag` | `str` | Tag name (e.g., 'dynamic-programming') |

**Returns:** List of `AlgorithmEntry` objects

**Example:**

```python
# Get all dynamic programming algorithms
dp_algos = registry.get_by_tag('dynamic-programming')

# Get all GPU-accelerated algorithms
gpu_algos = registry.get_by_tag('gpu-accelerated')
```

---

#### search()

```python
search(keyword: str) -> list[AlgorithmEntry]
```

Search algorithms by keyword in name, description, purpose, or tags.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `keyword` | `str` | Search keyword |

**Returns:** List of `AlgorithmEntry` objects sorted by relevance

**Example:**

```python
# Search for alignment algorithms
results = registry.search('alignment')

# Search for specific algorithm
results = registry.search('smith waterman')

# Search for GPU-related algorithms
results = registry.search('gpu')
```

**Note:** Search is case-insensitive and matches partial strings.

---

#### get_algorithm()

```python
get_algorithm(algo_id: str) -> Optional[AlgorithmEntry]
```

Get a single algorithm by its ID.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `algo_id` | `str` | Algorithm identifier (e.g., 'smith-waterman') |

**Returns:** `AlgorithmEntry` or `None` if not found

**Example:**

```python
# Get specific algorithm
algo = registry.get_algorithm('smith-waterman')
if algo:
    print(f"Name: {algo.name}")
    print(f"Complexity: {algo.time_complexity}")
else:
    print("Algorithm not found")
```

---

#### get_statistics()

```python
get_statistics() -> RegistryStats
```

Get comprehensive statistics about the registry.

**Returns:** `RegistryStats` object

**Example:**

```python
stats = registry.get_statistics()
print(f"Total algorithms: {stats.total_algorithms}")
print(f"Categories: {stats.total_categories}")
print(f"Unique tags: {stats.total_tags}")

# Get count per category
for cat, count in stats.algorithms_by_category.items():
    print(f"  {cat}: {count}")
```

---

## CategoryManager

Manages algorithm categories loaded from YAML files.

### Constructor

```python
CategoryManager()
```

**Example:**

```python
cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')
```

---

### Methods

#### load_categories()

```python
load_categories(path: str) -> list[Category]
```

Load categories from a YAML file.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `path` | `str` | Path to categories YAML file |

**Returns:** List of `Category` objects

**Example:**

```python
cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')
```

---

#### get_category()

```python
get_category(category_id: str) -> Optional[Category]
```

Get a category by its ID.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `category_id` | `str` | Category identifier |

**Returns:** `Category` object or `None`

**Example:**

```python
category = cm.get_category('sequence-alignment')
if category:
    print(f"Name: {category.name}")
    print(f"English: {category.name_en}")
```

---

#### get_subcategories()

```python
get_subcategories(category_id: str) -> list[Category]
```

Get all subcategories of a top-level category.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `category_id` | `str` | Parent category identifier |

**Returns:** List of `Category` objects

**Example:**

```python
subcats = cm.get_subcategories('sequence-alignment')
for subcat in subcats:
    print(f"  - {subcat.name}")
```

---

#### category_exists()

```python
category_exists(category_id: str) -> bool
```

Check if a category exists.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `category_id` | `str` | Category identifier |

**Returns:** `True` if category exists

**Example:**

```python
if cm.category_exists('variant-calling'):
    print("Category exists")
else:
    print("Category not found")
```

---

## Validator

Validates algorithm entries and categories.

### Constructor

```python
Validator(valid_categories: Optional[list[str]] = None)
```

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `valid_categories` | `list[str]` | `None` | Optional list of valid category IDs |

**Example:**

```python
# Create validator
validator = Validator()

# Create validator with specific categories
validator = Validator(['sequence-alignment', 'variant-calling'])
```

---

### Methods

#### validate_algorithm()

```python
validate_algorithm(data: dict) -> ValidationResult
```

Validate an algorithm entry dictionary.

**Validations:**

- Required fields: `id`, `name`, `description`, `purpose`, `time_complexity`, `category`
- Description length: 50-500 characters
- Unique ID across repository
- Valid category and subcategory IDs
- Valid difficulty level (if provided)
- Valid reference types (if provided)

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `data` | `dict` | Algorithm data dictionary |

**Returns:** `ValidationResult` object

**Example:**

```python
validator = Validator()

# Validate algorithm data
algo_data = {
    'id': 'my-algorithm',
    'name': 'My Algorithm',
    'description': 'A useful algorithm...',
    'purpose': 'Solving specific problems',
    'time_complexity': 'O(n)',
    'category': 'sequence-alignment'
}

result = validator.validate_algorithm(algo_data)

if not result.is_valid:
    print("Errors:", result.errors)
if result.warnings:
    print("Warnings:", result.warnings)
```

---

#### validate_all()

```python
validate_all(data_dir: str) -> ValidationResult
```

Validate all data files in a directory.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `data_dir` | `str` | Path to data directory |

**Returns:** `ValidationResult` with aggregated errors

**Example:**

```python
result = validator.validate_all('data')

if not result.is_valid:
    for error in result.errors:
        print(f"ERROR: {error}")
else:
    print("All validations passed!")
```

---

## DataIO

Handles import/export of algorithm and category data.

### Constructor

```python
DataIO(
    algorithm_registry: AlgorithmRegistry,
    category_manager: CategoryManager
)
```

---

### Methods

#### export_data()

```python
export_data(output_path: str, fmt: str = "yaml") -> None
```

Export all data to a file (YAML or JSON).

**Parameters:**

| Parameter | Type | Default | Description |
|:----------|:-----|:--------|:------------|
| `output_path` | `str` | — | Output file path |
| `fmt` | `str` | `"yaml"` | Format: 'yaml' or 'json' |

**Example:**

```python
from scripts.data_io import DataIO

io = DataIO(registry, cm)

# Export as YAML
io.export_data('backup.yaml', fmt='yaml')

# Export as JSON
io.export_data('backup.json', fmt='json')
```

---

#### import_data()

```python
import_data(input_path: str) -> tuple[list[Category], list[AlgorithmEntry]]
```

Import data from a file.

**Parameters:**

| Parameter | Type | Description |
|:----------|:-----|:------------|
| `input_path` | `str` | Input file path |

**Returns:** Tuple of (categories, algorithms)

**Example:**

```python
# Import from backup
categories, algorithms = io.import_data('backup.yaml')

print(f"Imported {len(categories)} categories")
print(f"Imported {len(algorithms)} algorithms")
```

---

## Data Models

### AlgorithmEntry

Represents a single algorithm entry.

```python
@dataclass
class AlgorithmEntry:
    # Required fields
    id: str                    # Unique identifier (lowercase, hyphens)
    name: str                  # Algorithm name
    description: str           # Description (50-500 chars)
    purpose: str               # Purpose/use case
    time_complexity: str       # Time complexity (e.g., "O(n^2)")
    category: str              # Category ID
    
    # Optional fields
    space_complexity: str = "" # Space complexity
    year: int = 0              # Publication year
    paper_url: str = ""        # Paper URL
    implementation_url: str = ""  # Implementation URL
    related_tools: list[str] = [] # Related tools
    tags: list[str] = []       # Tags
    subcategory: str = ""      # Subcategory ID
    difficulty: str = ""       # Difficulty level
    language: str = ""         # Implementation language
    references: list[dict] = []   # Additional references
```

**Example:**

```python
from scripts.schema import AlgorithmEntry

algo = AlgorithmEntry(
    id='smith-waterman',
    name='Smith-Waterman',
    description='Local sequence alignment algorithm...',
    purpose='Local sequence alignment',
    time_complexity='O(mn)',
    space_complexity='O(mn)',
    category='sequence-alignment',
    subcategory='pairwise',
    year=1981,
    tags=['dynamic-programming', 'local-alignment']
)
```

---

### Category

Represents an algorithm category.

```python
@dataclass
class Category:
    id: str                    # Unique identifier
    name: str                  # Category name (Chinese)
    name_en: str               # Category name (English)
    description: str = ""      # Optional description
    subcategories: list[Category] = []  # Subcategories
    parent_id: Optional[str] = None     # Parent category ID
```

---

### ValidationResult

Result of a validation operation.

```python
@dataclass
class ValidationResult:
    is_valid: bool             # Whether validation passed
    errors: list[str] = []     # Error messages
    warnings: list[str] = []   # Warning messages
```

**Example:**

```python
result = ValidationResult(
    is_valid=False,
    errors=['Missing required field: purpose'],
    warnings=['Description is very short']
)

if not result.is_valid:
    print("Validation failed!")
```

---

## Best Practices

### 1. Error Handling

Always check for errors when loading data:

```python
from scripts.validate import Validator

validator = Validator()
result = validator.validate_all('data')

if not result.is_valid:
    for error in result.errors:
        print(f"ERROR: {error}")
    exit(1)
```

### 2. Working with Categories

Use the category manager to ensure valid operations:

```python
cm = CategoryManager()
cm.load_categories('data/categories.yaml')

# Always check category exists before using
if not cm.category_exists(category_id):
    raise ValueError(f"Invalid category: {category_id}")
```

### 3. Searching Algorithms

Combine search and filtering for best results:

```python
# Search for algorithms
results = registry.search('alignment')

# Filter by tag
dp_results = [r for r in results if 'dynamic-programming' in r.tags]

# Sort by year
sorted_results = sorted(results, key=lambda x: x.year, reverse=True)
```

### 4. Exporting Data

Always validate before exporting:

```python
# Validate first
result = validator.validate_all('data')
if not result.is_valid:
    raise ValueError("Cannot export invalid data")

# Then export
io.export_data('backup.yaml')
```

---

## Version Compatibility

| API Version | Python Version | Status |
|:------------|:---------------|:-------|
| 1.0.x | 3.9+ | Stable |
| 2.0.x (planned) | 3.10+ | In development |

---

## See Also

- [Development Guide]({% link en/development.md %}) — Project architecture and setup
- [Contributing Guide]({% link en/contributing.md %}) — How to add new algorithms
- [FAQ]({% link en/faq.md %}) — Frequently asked questions
