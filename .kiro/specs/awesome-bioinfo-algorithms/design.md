# Design Document: Awesome Bioinformatics Algorithms

## Overview

本项目是一个 GitHub 开源项目，采用 awesome-list 风格汇总生物信息学算法概要。项目使用 YAML 文件存储算法数据，通过 Python 脚本自动生成 README.md 文档。整体架构简洁，便于社区贡献和维护。

## Architecture

```
awesome-bioinfo-algorithms/
├── README.md                    # 自动生成的主文档
├── CONTRIBUTING.md              # 贡献指南
├── data/
│   ├── categories.yaml          # 分类定义
│   └── algorithms/
│       ├── sequence-alignment.yaml
│       ├── assembly.yaml
│       ├── variant-calling.yaml
│       └── ...                  # 按分类组织的算法文件
├── scripts/
│   ├── generate_readme.py       # README 生成脚本
│   ├── validate.py              # 数据验证脚本
│   └── schema.py                # 数据模式定义
├── templates/
│   ├── readme_template.md       # README 模板
│   └── algorithm_template.yaml  # 算法条目模板
└── .github/
    ├── ISSUE_TEMPLATE/
    │   └── new_algorithm.md     # 新算法提交模板
    └── workflows/
        └── validate.yml         # CI 验证工作流
```

## Components and Interfaces

### 1. Category Manager

负责管理算法分类体系。

```python
class Category:
    id: str              # 分类ID，如 "sequence-alignment"
    name: str            # 显示名称，如 "序列比对"
    name_en: str         # 英文名称
    description: str     # 分类描述
    subcategories: List[Category]  # 子分类
    
class CategoryManager:
    def load_categories(self, path: str) -> List[Category]
    def get_category(self, category_id: str) -> Category
    def list_all_categories(self) -> List[Category]
```

### 2. Algorithm Entry

算法条目的数据结构。

```python
@dataclass
class AlgorithmEntry:
    # 必填字段
    id: str                      # 唯一标识符
    name: str                    # 算法名称
    description: str             # 简要描述 (50-200字)
    purpose: str                 # 主要用途
    time_complexity: str         # 时间复杂度
    category: str                # 主分类ID
    
    # 可选字段
    space_complexity: str = ""   # 空间复杂度
    paper_url: str = ""          # 原始论文链接
    implementation_url: str = "" # 参考实现链接
    related_tools: List[str] = field(default_factory=list)  # 相关工具
    tags: List[str] = field(default_factory=list)           # 标签
    subcategory: str = ""        # 子分类ID
```

### 3. Algorithm Registry

算法注册表，管理所有算法条目。

```python
class AlgorithmRegistry:
    def __init__(self, data_dir: str)
    
    def load_all(self) -> List[AlgorithmEntry]
    def get_by_category(self, category_id: str) -> List[AlgorithmEntry]
    def get_by_tag(self, tag: str) -> List[AlgorithmEntry]
    def search(self, keyword: str) -> List[AlgorithmEntry]
    def validate_entry(self, entry: dict) -> ValidationResult
    def get_statistics(self) -> RegistryStats
```

### 4. README Generator

README 文档生成器。

```python
class ReadmeGenerator:
    def __init__(self, registry: AlgorithmRegistry, 
                 category_manager: CategoryManager,
                 template_path: str)
    
    def generate(self) -> str
    def generate_toc(self) -> str           # 生成目录
    def generate_category_section(self, category: Category) -> str
    def generate_algorithm_entry(self, algo: AlgorithmEntry) -> str
    def generate_statistics(self) -> str    # 生成统计信息
```

### 5. Validator

数据验证器。

```python
@dataclass
class ValidationResult:
    is_valid: bool
    errors: List[str]
    warnings: List[str]

class Validator:
    def validate_algorithm(self, data: dict) -> ValidationResult
    def validate_category(self, data: dict) -> ValidationResult
    def validate_all(self, data_dir: str) -> ValidationResult
```

## Data Models

### categories.yaml 格式

```yaml
categories:
  - id: sequence-alignment
    name: 序列比对
    name_en: Sequence Alignment
    description: 用于比较和对齐生物序列的算法
    subcategories:
      - id: pairwise
        name: 双序列比对
        name_en: Pairwise Alignment
      - id: multiple
        name: 多序列比对
        name_en: Multiple Sequence Alignment

  - id: assembly
    name: 序列组装
    name_en: Sequence Assembly
    description: 从短读段重建完整序列的算法
```

### 算法条目 YAML 格式

```yaml
# data/algorithms/sequence-alignment.yaml
algorithms:
  - id: smith-waterman
    name: Smith-Waterman
    description: |
      经典的局部序列比对算法，使用动态规划方法找出两条序列之间
      相似性最高的局部区域。适用于检测序列中的保守区域。
    purpose: 局部序列比对，寻找序列间的相似区域
    time_complexity: O(mn)
    space_complexity: O(mn)
    category: sequence-alignment
    subcategory: pairwise
    paper_url: https://doi.org/10.1016/0022-2836(81)90087-5
    implementation_url: https://github.com/mengyao/Complete-Striped-Smith-Waterman-Library
    related_tools:
      - BLAST
      - FASTA
    tags:
      - dynamic-programming
      - local-alignment
      - classic

  - id: needleman-wunsch
    name: Needleman-Wunsch
    description: |
      全局序列比对的经典算法，使用动态规划对两条完整序列进行
      端到端比对，找出最优的全局对齐方案。
    purpose: 全局序列比对
    time_complexity: O(mn)
    space_complexity: O(mn)
    category: sequence-alignment
    subcategory: pairwise
    paper_url: https://doi.org/10.1016/0022-2836(70)90057-4
    tags:
      - dynamic-programming
      - global-alignment
      - classic
```

### README 模板格式

```markdown
# Awesome Bioinformatics Algorithms

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> 生物信息学算法概要汇总

## 统计

- 📊 算法总数: {{ total_algorithms }}
- 📁 分类数量: {{ total_categories }}
- 🏷️ 标签数量: {{ total_tags }}

## 目录

{{ toc }}

---

{{ content }}

## 贡献

欢迎贡献！请阅读 [贡献指南](CONTRIBUTING.md)。

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system-essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Category Algorithm Count Accuracy

*For any* algorithm registry with algorithms distributed across categories, the count displayed for each category SHALL equal the actual number of algorithms in that category.

**Validates: Requirements 1.2, 3.4**

### Property 2: Subcategory Hierarchy Preservation

*For any* category with subcategories, retrieving the category SHALL return all its subcategories, and each subcategory SHALL correctly reference its parent category.

**Validates: Requirements 1.3**

### Property 3: Required Fields Validation

*For any* algorithm entry submission, if any required field (name, description, purpose, time_complexity, category) is missing or empty, the validator SHALL reject the entry and return an error.

**Validates: Requirements 1.4, 2.1, 4.2**

### Property 4: Optional Fields Storage

*For any* algorithm entry with optional fields (space_complexity, paper_url, implementation_url, related_tools, tags), storing and retrieving the entry SHALL preserve all optional field values exactly.

**Validates: Requirements 2.2, 2.4**

### Property 5: Markdown Output Consistency

*For any* algorithm entry, the generated Markdown output SHALL contain the algorithm name, description, purpose, and time complexity in a consistent format.

**Validates: Requirements 2.3**

### Property 6: Table of Contents Completeness

*For any* algorithm registry, the generated table of contents SHALL contain an entry for every category that has at least one algorithm.

**Validates: Requirements 3.1**

### Property 7: Validation Error Specificity

*For any* invalid algorithm entry or malformed data, the validator SHALL return an error message that identifies the specific field or format issue.

**Validates: Requirements 4.4, 6.3**

### Property 8: Search Result Correctness

*For any* search query (by name or tag), all returned algorithms SHALL match the search criteria, and no matching algorithm SHALL be omitted from the results.

**Validates: Requirements 5.1, 5.2, 5.3**

### Property 9: Anchor Link Format Validity

*For any* generated table of contents entry, the anchor link SHALL be a valid Markdown anchor that correctly links to the corresponding section.

**Validates: Requirements 5.4**

### Property 10: Data Format Validation

*For any* YAML data file, the validator SHALL correctly identify whether the file conforms to the expected schema and report all violations.

**Validates: Requirements 6.2**

### Property 11: Data Import/Export Round-Trip

*For any* valid algorithm registry, exporting the data and then importing it back SHALL produce an equivalent registry with identical algorithms and categories.

**Validates: Requirements 6.4**

## Error Handling

### Validation Errors

| Error Type | Condition | Response |
|------------|-----------|----------|
| MissingRequiredField | 必填字段缺失 | 返回缺失字段列表 |
| InvalidFieldLength | 描述长度不在 50-200 字范围 | 返回当前长度和要求范围 |
| InvalidCategory | 分类 ID 不存在 | 返回有效分类列表 |
| InvalidYAML | YAML 语法错误 | 返回行号和错误详情 |
| DuplicateID | 算法 ID 重复 | 返回冲突的算法信息 |
| InvalidURL | URL 格式不正确 | 返回无效的 URL 字段 |

### File System Errors

| Error Type | Condition | Response |
|------------|-----------|----------|
| FileNotFound | 数据文件不存在 | 创建默认文件或提示用户 |
| PermissionDenied | 无写入权限 | 提示检查文件权限 |
| EncodingError | 文件编码问题 | 提示使用 UTF-8 编码 |

## Testing Strategy

### Unit Tests

单元测试覆盖以下场景：

1. **Category Manager**
   - 加载分类配置
   - 获取单个分类
   - 获取子分类

2. **Algorithm Entry**
   - 创建有效条目
   - 必填字段验证
   - 可选字段处理

3. **Validator**
   - 各种验证规则
   - 错误消息格式

4. **README Generator**
   - 目录生成
   - 算法条目格式化
   - 统计信息计算

### Property-Based Tests

使用 Hypothesis (Python) 进行属性测试：

- 每个属性测试运行至少 100 次迭代
- 测试标注格式: **Feature: awesome-bioinfo-algorithms, Property {number}: {property_text}**

测试框架配置：
```python
from hypothesis import given, settings
from hypothesis import strategies as st

@settings(max_examples=100)
@given(...)
def test_property_name():
    # Feature: awesome-bioinfo-algorithms, Property N: property description
    pass
```

### Integration Tests

1. 完整的 README 生成流程
2. CI 验证工作流
3. 数据导入导出流程

