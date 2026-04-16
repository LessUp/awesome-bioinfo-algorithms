---
title: API 文档
layout: default
nav_order: 2
description: "公共 API 参考，包含代码示例和最佳实践"
---

# API 文档
{: .no_toc }

Awesome Bioinformatics Algorithms Python API 的完整参考。
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>目录</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## 快速开始

```python
from scripts.algorithm_registry import AlgorithmRegistry
from scripts.category_manager import CategoryManager

# 加载所有数据
registry = AlgorithmRegistry('data/algorithms')
registry.load_all()

cm = CategoryManager()
cm.load_categories('data/categories.yaml')

# 示例：获取所有序列比对算法
algorithms = registry.get_by_category('sequence-alignment')
print(f"找到 {len(algorithms)} 个算法")

# 示例：搜索动态规划算法
results = registry.search('dynamic programming')
```

---

## AlgorithmRegistry

管理从 YAML 文件加载的算法条目。

### 构造函数

```python
AlgorithmRegistry(data_dir: str = "data/algorithms")
```

**参数：**

| 参数 | 类型 | 默认值 | 说明 |
|:----------|:-----|:--------|:------------|
| `data_dir` | `str` | `"data/algorithms"` | 算法目录路径 |

**示例：**

```python
# 默认使用
registry = AlgorithmRegistry()

# 自定义路径
registry = AlgorithmRegistry('/path/to/algorithms')
```

---

### 方法

#### load_all()

```python
load_all() -> list[AlgorithmEntry]
```

从数据目录的 YAML 文件加载所有算法。

**返回：** `AlgorithmEntry` 对象列表

**示例：**

```python
registry = AlgorithmRegistry()
algorithms = registry.load_all()
print(f"加载了 {len(algorithms)} 个算法")
```

---

#### get_by_category()

```python
get_by_category(category_id: str) -> list[AlgorithmEntry]
```

获取特定分类中的所有算法（包括子分类）。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `category_id` | `str` | 分类标识符（如 'sequence-alignment'） |

**返回：** `AlgorithmEntry` 对象列表

**示例：**

```python
# 获取所有序列比对算法
alignment_algos = registry.get_by_category('sequence-alignment')

# 获取所有变异检测算法
variant_algos = registry.get_by_category('variant-calling')
```

---

#### get_by_subcategory()

```python
get_by_subcategory(subcategory_id: str) -> list[AlgorithmEntry]
```

获取特定子分类中的所有算法。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `subcategory_id` | `str` | 子分类标识符（如 'pairwise'） |

**返回：** `AlgorithmEntry` 对象列表

**示例：**

```python
# 获取双序列比对算法
pairwise_algos = registry.get_by_subcategory('pairwise')

# 获取从头组装算法
de_novo_algos = registry.get_by_subcategory('de-novo')
```

---

#### get_by_tag()

```python
get_by_tag(tag: str) -> list[AlgorithmEntry]
```

获取具有特定标签的所有算法。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `tag` | `str` | 标签名（如 'dynamic-programming'） |

**返回：** `AlgorithmEntry` 对象列表

**示例：**

```python
# 获取所有动态规划算法
dp_algos = registry.get_by_tag('dynamic-programming')

# 获取所有 GPU 加速算法
gpu_algos = registry.get_by_tag('gpu-accelerated')
```

---

#### search()

```python
search(keyword: str) -> list[AlgorithmEntry]
```

在名称、描述、用途或标签中搜索算法。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `keyword` | `str` | 搜索关键词 |

**返回：** 按相关性排序的 `AlgorithmEntry` 对象列表

**示例：**

```python
# 搜索比对算法
results = registry.search('alignment')

# 搜索特定算法
results = registry.search('smith waterman')

# 搜索 GPU 相关算法
results = registry.search('gpu')
```

**注意：** 搜索不区分大小写，支持部分匹配。

---

#### get_algorithm()

```python
get_algorithm(algo_id: str) -> Optional[AlgorithmEntry]
```

通过 ID 获取单个算法。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `algo_id` | `str` | 算法标识符（如 'smith-waterman'） |

**返回：** `AlgorithmEntry` 对象，未找到时返回 `None`

**示例：**

```python
# 获取特定算法
algo = registry.get_algorithm('smith-waterman')
if algo:
    print(f"名称: {algo.name}")
    print(f"复杂度: {algo.time_complexity}")
else:
    print("算法未找到")
```

---

#### get_statistics()

```python
get_statistics() -> RegistryStats
```

获取注册表的详细统计信息。

**返回：** `RegistryStats` 对象

**示例：**

```python
stats = registry.get_statistics()
print(f"算法总数: {stats.total_algorithms}")
print(f"分类数: {stats.total_categories}")
print(f"唯一标签数: {stats.total_tags}")

# 获取每个分类的计数
for cat, count in stats.algorithms_by_category.items():
    print(f"  {cat}: {count}")
```

---

## CategoryManager

管理从 YAML 文件加载的算法分类。

### 构造函数

```python
CategoryManager()
```

**示例：**

```python
cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')
```

---

### 方法

#### load_categories()

```python
load_categories(path: str) -> list[Category]
```

从 YAML 文件加载分类。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `path` | `str` | 分类 YAML 文件路径 |

**返回：** `Category` 对象列表

**示例：**

```python
cm = CategoryManager()
categories = cm.load_categories('data/categories.yaml')
```

---

#### get_category()

```python
get_category(category_id: str) -> Optional[Category]
```

通过 ID 获取分类。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `category_id` | `str` | 分类标识符 |

**返回：** `Category` 对象或 `None`

**示例：**

```python
category = cm.get_category('sequence-alignment')
if category:
    print(f"名称: {category.name}")
    print(f"英文: {category.name_en}")
```

---

#### get_subcategories()

```python
get_subcategories(category_id: str) -> list[Category]
```

获取顶层分类的所有子分类。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `category_id` | `str` | 父分类标识符 |

**返回：** `Category` 对象列表

**示例：**

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

检查分类是否存在。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `category_id` | `str` | 分类标识符 |

**返回：** 分类存在时返回 `True`

**示例：**

```python
if cm.category_exists('variant-calling'):
    print("分类存在")
else:
    print("分类未找到")
```

---

## Validator

验证算法条目和分类。

### 构造函数

```python
Validator(valid_categories: Optional[list[str]] = None)
```

**参数：**

| 参数 | 类型 | 默认值 | 说明 |
|:----------|:-----|:--------|:------------|
| `valid_categories` | `list[str]` | `None` | 可选的有效分类 ID 列表 |

**示例：**

```python
# 创建验证器
validator = Validator()

# 使用特定分类创建验证器
validator = Validator(['sequence-alignment', 'variant-calling'])
```

---

### 方法

#### validate_algorithm()

```python
validate_algorithm(data: dict) -> ValidationResult
```

验证算法条目字典。

**验证项：**

- 必填字段：`id`、`name`、`description`、`purpose`、`time_complexity`、`category`
- 描述长度：50-500 字符
- 仓库范围内 ID 唯一
- 有效的分类和子分类 ID
- 有效的难度级别（如提供）
- 有效的引用类型（如提供）

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `data` | `dict` | 算法数据字典 |

**返回：** `ValidationResult` 对象

**示例：**

```python
validator = Validator()

# 验证算法数据
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
    print("错误:", result.errors)
if result.warnings:
    print("警告:", result.warnings)
```

---

#### validate_all()

```python
validate_all(data_dir: str) -> ValidationResult
```

验证目录中的所有数据文件。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `data_dir` | `str` | 数据目录路径 |

**返回：** 包含聚合错误的 `ValidationResult`

**示例：**

```python
result = validator.validate_all('data')

if not result.is_valid:
    for error in result.errors:
        print(f"错误: {error}")
else:
    print("所有验证通过！")
```

---

## DataIO

处理算法和分类数据的导入/导出。

### 构造函数

```python
DataIO(
    algorithm_registry: AlgorithmRegistry,
    category_manager: CategoryManager
)
```

---

### 方法

#### export_data()

```python
export_data(output_path: str, fmt: str = "yaml") -> None
```

将所有数据导出到文件（YAML 或 JSON）。

**参数：**

| 参数 | 类型 | 默认值 | 说明 |
|:----------|:-----|:--------|:------------|
| `output_path` | `str` | — | 输出文件路径 |
| `fmt` | `str` | `"yaml"` | 格式：'yaml' 或 'json' |

**示例：**

```python
from scripts.data_io import DataIO

io = DataIO(registry, cm)

# 导出为 YAML
io.export_data('backup.yaml', fmt='yaml')

# 导出为 JSON
io.export_data('backup.json', fmt='json')
```

---

#### import_data()

```python
import_data(input_path: str) -> tuple[list[Category], list[AlgorithmEntry]]
```

从文件导入数据。

**参数：**

| 参数 | 类型 | 说明 |
|:----------|:-----|:------------|
| `input_path` | `str` | 输入文件路径 |

**返回：** (分类列表, 算法列表) 元组

**示例：**

```python
# 从备份导入
categories, algorithms = io.import_data('backup.yaml')

print(f"导入了 {len(categories)} 个分类")
print(f"导入了 {len(algorithms)} 个算法")
```

---

## 数据模型

### AlgorithmEntry

表示单个算法条目。

```python
@dataclass
class AlgorithmEntry:
    # 必填字段
    id: str                    # 唯一标识符（小写、连字符）
    name: str                  # 算法名称
    description: str           # 描述（50-500 字符）
    purpose: str               # 用途
    time_complexity: str       # 时间复杂度（如 "O(n^2)"）
    category: str              # 分类 ID
    
    # 可选字段
    space_complexity: str = "" # 空间复杂度
    year: int = 0              # 发表年份
    paper_url: str = ""        # 论文 URL
    implementation_url: str = ""  # 实现链接
    related_tools: list[str] = [] # 相关工具
    tags: list[str] = []       # 标签
    subcategory: str = ""      # 子分类 ID
    difficulty: str = ""       # 难度级别
    language: str = ""         # 实现语言
    references: list[dict] = []   # 额外引用
```

**示例：**

```python
from scripts.schema import AlgorithmEntry

algo = AlgorithmEntry(
    id='smith-waterman',
    name='Smith-Waterman',
    description='局部序列比对算法...',
    purpose='局部序列比对',
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

表示算法分类。

```python
@dataclass
class Category:
    id: str                    # 唯一标识符
    name: str                  # 分类名（中文）
    name_en: str               # 分类名（英文）
    description: str = ""      # 可选描述
    subcategories: list[Category] = []  # 子分类
    parent_id: Optional[str] = None     # 父分类 ID
```

---

### ValidationResult

验证操作的结果。

```python
@dataclass
class ValidationResult:
    is_valid: bool             # 验证是否通过
    errors: list[str] = []     # 错误信息
    warnings: list[str] = []   # 警告信息
```

**示例：**

```python
result = ValidationResult(
    is_valid=False,
    errors=['缺少必填字段：purpose'],
    warnings=['描述较短']
)

if not result.is_valid:
    print("验证失败！")
```

---

## 最佳实践

### 1. 错误处理

加载数据时始终检查错误：

```python
from scripts.validate import Validator

validator = Validator()
result = validator.validate_all('data')

if not result.is_valid:
    for error in result.errors:
        print(f"错误: {error}")
    exit(1)
```

### 2. 使用分类

使用分类管理器确保操作有效：

```python
cm = CategoryManager()
cm.load_categories('data/categories.yaml')

# 使用前始终检查分类存在性
if not cm.category_exists(category_id):
    raise ValueError(f"无效分类: {category_id}")
```

### 3. 搜索算法

结合搜索和过滤获得最佳结果：

```python
# 搜索算法
results = registry.search('alignment')

# 按标签过滤
dp_results = [r for r in results if 'dynamic-programming' in r.tags]

# 按年份排序
sorted_results = sorted(results, key=lambda x: x.year, reverse=True)
```

### 4. 导出数据

导出前始终验证：

```python
# 先验证
result = validator.validate_all('data')
if not result.is_valid:
    raise ValueError("无法导出不合法的数据")

# 然后导出
io.export_data('backup.yaml')
```

---

## 版本兼容性

| API 版本 | Python 版本 | 状态 |
|:------------|:---------------|:-------|
| 1.0.x | 3.9+ | 稳定 |
| 2.0.x (计划中) | 3.10+ | 开发中 |

---

## 相关链接

- [开发指南]({% link zh/development.md %}) — 项目架构和设置
- [贡献指南]({% link zh/contributing.md %}) — 如何添加新算法
- [常见问题]({% link zh/faq.md %}) — 常见问题解答
