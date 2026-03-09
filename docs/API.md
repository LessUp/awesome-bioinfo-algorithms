---
title: API 文档
layout: default
nav_order: 2
description: "公共 API 接口说明"
---

# API Documentation / API 文档

This document describes the public API of the Awesome Bioinformatics Algorithms project.

本文档描述 Awesome Bioinformatics Algorithms 项目的公共 API。

## Table of Contents / 目录

- [AlgorithmRegistry](#algorithmregistry)
- [CategoryManager](#categorymanager)
- [Validator](#validator)
- [DataIO](#dataio)
- [ReadmeGenerator](#readmegenerator)
- [Data Models](#data-models)

---

## AlgorithmRegistry

Manages algorithm entries loaded from YAML files.

管理从 YAML 文件加载的算法条目。

### Constructor

```python
AlgorithmRegistry(data_dir: str = "data/algorithms")
```

**Parameters:**
- `data_dir`: Path to the directory containing algorithm YAML files

### Methods

#### `load_all() -> list[AlgorithmEntry]`

Load all algorithms from YAML files in the data directory.

```python
registry = AlgorithmRegistry()
algorithms = registry.load_all()
```

#### `get_by_category(category_id: str) -> list[AlgorithmEntry]`

Get all algorithms in a specific category.

```python
alignment_algos = registry.get_by_category('sequence-alignment')
```

#### `get_by_tag(tag: str) -> list[AlgorithmEntry]`

Get all algorithms with a specific tag.

```python
dynamic_algos = registry.get_by_tag('dynamic-programming')
```

#### `search(keyword: str) -> list[AlgorithmEntry]`

Search algorithms by keyword in name, description, or tags.

```python
results = registry.search('alignment')
```


#### `get_algorithm(algo_id: str) -> Optional[AlgorithmEntry]`

Get an algorithm by its ID.

```python
algo = registry.get_algorithm('smith-waterman')
```

#### `get_statistics() -> RegistryStats`

Get statistics about the registry.

```python
stats = registry.get_statistics()
print(f"Total algorithms: {stats.total_algorithms}")
print(f"Categories: {stats.total_categories}")
```

#### `from_algorithms(algorithms: list[AlgorithmEntry])`

Load algorithms from a list of AlgorithmEntry objects.

```python
registry.from_algorithms(my_algorithms)
```

---

## CategoryManager

Manages algorithm categories loaded from YAML files.

管理从 YAML 文件加载的算法分类。

### Constructor

```python
CategoryManager()
```

### Methods

#### `load_categories(path: str) -> list[Category]`

Load categories from a YAML file.

```python
cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')
```

#### `get_category(category_id: str) -> Optional[Category]`

Get a category by its ID.

```python
category = cm.get_category('sequence-alignment')
```

#### `list_all_categories() -> list[Category]`

List all top-level categories.

```python
categories = cm.list_all_categories()
```

#### `list_all_category_ids() -> list[str]`

List all category IDs including subcategories.

```python
ids = cm.list_all_category_ids()
```

#### `category_exists(category_id: str) -> bool`

Check if a category exists.

```python
if cm.category_exists('assembly'):
    print("Category exists")
```

---

## Validator

Validates algorithm entries and categories.

验证算法条目和分类。

### Constructor

```python
Validator(valid_categories: Optional[list[str]] = None)
```

**Parameters:**
- `valid_categories`: Optional list of valid category IDs for validation

### Methods

#### `validate_algorithm(data: dict) -> ValidationResult`

Validate an algorithm entry dictionary.

```python
validator = Validator()
result = validator.validate_algorithm(algo_dict)
if not result.is_valid:
    print(f"Errors: {result.errors}")
```

#### `validate_category(data: dict) -> ValidationResult`

Validate a category entry dictionary.

```python
result = validator.validate_category(category_dict)
```

#### `validate_yaml_file(file_path: str) -> ValidationResult`

Validate a YAML file for syntax errors.

```python
result = validator.validate_yaml_file('data/algorithms/assembly.yaml')
```

#### `validate_all(data_dir: str) -> ValidationResult`

Validate all data files in a directory.

```python
result = validator.validate_all('data')
```

---

## DataIO

Handles import/export of algorithm and category data.

处理算法和分类数据的导入/导出。

### Methods

#### `export_data(output_path: str, fmt: str = "yaml") -> None`

Export all data to a file (YAML or JSON).

```python
io = DataIO(registry, category_manager)
io.export_data('backup.yaml', fmt='yaml')
io.export_data('backup.json', fmt='json')
```

#### `import_data(input_path: str) -> tuple[list[Category], list[AlgorithmEntry]]`

Import data from a file.

```python
categories, algorithms = io.import_data('backup.yaml')
```

---

## ReadmeGenerator

Generates README.md from categories and algorithms.

从分类和算法生成 README.md。

### Constructor

```python
ReadmeGenerator(registry: AlgorithmRegistry, category_manager: CategoryManager, template_path: str = "templates/readme_template.md")
```

### Methods

#### `generate() -> str`

Generate the complete README content.

```python
generator = ReadmeGenerator(registry, cm)
readme_content = generator.generate()
```

#### `save(output_path: str = "README.md")`

Generate and save README to file.

```python
generator.save('README.md')
```

---

## Data Models

### AlgorithmEntry

Represents a single algorithm entry.

```python
@dataclass
class AlgorithmEntry:
    id: str                    # Unique identifier
    name: str                  # Algorithm name
    description: str           # Description (50-200 chars)
    purpose: str               # Purpose/use case
    time_complexity: str       # Time complexity (e.g., "O(n^2)")
    category: str              # Category ID
    space_complexity: str = "" # Optional space complexity
    paper_url: str = ""        # Optional paper URL
    implementation_url: str = "" # Optional implementation URL
    related_tools: list[str] = [] # Optional related tools
    tags: list[str] = []       # Optional tags
    subcategory: str = ""      # Optional subcategory
```

### Category

Represents an algorithm category.

```python
@dataclass
class Category:
    id: str                    # Unique identifier
    name: str                  # Category name (Chinese)
    name_en: str               # Category name (English)
    description: str = ""      # Optional description
    subcategories: list[Category] = [] # Optional subcategories
    parent_id: Optional[str] = None    # Parent category ID
```

### ValidationResult

Result of a validation operation.

```python
@dataclass
class ValidationResult:
    is_valid: bool             # Whether validation passed
    errors: list[str] = []     # List of error messages
    warnings: list[str] = []   # List of warning messages
```

### RegistryStats

Statistics about the algorithm registry.

```python
@dataclass
class RegistryStats:
    total_algorithms: int      # Total number of algorithms
    total_categories: int      # Number of categories with algorithms
    total_tags: int            # Number of unique tags
    algorithms_by_category: dict[str, int]  # Count per category
```
