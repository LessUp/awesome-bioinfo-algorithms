# 贡献指南 | Contributing Guide

[English](#english) | [中文](#中文)

---

## 中文

感谢您对 Awesome Bioinformatics Algorithms 项目的关注！我们欢迎各种形式的贡献。

### 贡献方式

#### 1. 添加新算法

**步骤：**

1. Fork 本仓库
2. 在 `data/algorithms/` 目录下找到对应分类的 YAML 文件
3. 按照模板格式添加新算法条目
4. 提交 Pull Request

**算法条目格式：**

```yaml
algorithms:
  - id: algorithm-id          # 唯一标识符（小写字母、数字、连字符）
    name: Algorithm Name      # 算法名称
    description: |            # 算法描述（50-500字）
      算法的详细描述，包括基本原理、特点和适用场景。
    purpose: 主要用途          # 算法的主要用途
    time_complexity: O(n)     # 时间复杂度
    space_complexity: O(n)    # 空间复杂度（可选）
    category: category-id     # 分类ID
    subcategory: sub-id       # 子分类ID（可选）
    paper_url: https://...    # 原始论文链接（可选）
    implementation_url: https://...  # 参考实现链接（可选）
    related_tools:            # 相关工具（可选）
      - Tool1
      - Tool2
    tags:                     # 标签（可选）
      - tag1
      - tag2
```

#### 2. 可用分类

| 分类 ID | 中文名称 | English Name |
|---------|----------|--------------|
| sequence-alignment | 序列比对 | Sequence Alignment |
| assembly | 序列组装 | Sequence Assembly |
| variant-calling | 变异检测 | Variant Calling |
| expression-analysis | 基因表达分析 | Gene Expression Analysis |
| protein-structure | 蛋白质结构预测 | Protein Structure Prediction |
| phylogenetics | 系统发育分析 | Phylogenetics |
| functional-annotation | 功能注释 | Functional Annotation |
| data-compression | 数据压缩 | Data Compression |
| single-cell | 单细胞基因组学 | Single-Cell Genomics |
| metagenomics | 宏基因组学 | Metagenomics |
| epigenomics | 表观基因组学 | Epigenomics |
| gene-prediction | 基因预测 | Gene Prediction |
| population-genetics | 群体遗传学 | Population Genetics |
| spatial-omics | 空间组学 | Spatial Omics |
| graph-genomics | 图基因组学 | Graph Genomics |
| protein-language-model | 蛋白质语言模型 | Protein Language Model |

完整子分类列表请参考 `data/categories.yaml` 或 `templates/algorithm_template.yaml`。

如果要快速确认分类、子分类和已有条目，也可以运行：

```bash
python -m scripts stats
python -m scripts search --category sequence-alignment
```

#### 3. 参与规范文档编写

本项目采用**规范驱动开发（Spec-Driven Development）**，所有实现都以 `/specs` 目录下的文档为准。

**如何贡献：**

1. 阅读现有规范（`specs/README.md`）
2. 发现需要补充或修改的规范
3. 创建 RFC（Request for Comments）文档
4. 提交 PR 讨论，获得社区认可后合并

**规范类型：**
- `specs/product/` - 产品需求和功能定义
- `specs/rfc/` - 技术设计和架构方案
- `specs/api/` - CLI 接口规范
- `specs/db/` - 数据结构定义
- `specs/testing/` - 测试规范和验收标准

详见：[Spec 贡献指南](#spec-contributing-english)

#### 4. 质量要求

- ✅ 描述长度在 50-500 字之间
- ✅ 必须包含所有必填字段
- ✅ 分类 ID 和子分类 ID 必须有效
- ✅ `subcategory` 必须属于对应的 `category`
- ✅ 算法 ID 在整个仓库范围内必须唯一
- ✅ YAML 格式正确
- ✅ 链接有效且可访问
- ✅ `difficulty` 如填写，必须为 `beginner` / `intermediate` / `advanced`
- ✅ `references[*].type` 如填写，必须为 `tutorial` / `blog` / `video` / `book` / `documentation` / `slides`

#### 4. 本地验证

在提交前，请在本地运行验证：

```bash
# 安装依赖（开发模式）
pip install -e ".[dev]"
# 或：pip install -r requirements.txt

# 运行测试
python -m pytest tests/ -v

# 校验数据
python -m scripts validate

# 生成 MkDocs 预览页面
python -m scripts mkdocs

# 生成 README 预览
python -m scripts generate
```

### 其他贡献方式

- 📝 改进现有算法描述
- 🔗 添加或更新参考链接
- 🐛 报告错误或问题
- 💡 提出新功能建议

### 行为准则

- 尊重所有贡献者
- 保持专业和友好的交流
- 接受建设性的批评

---

## English

Thank you for your interest in Awesome Bioinformatics Algorithms! We welcome all kinds of contributions.

### How to Contribute

#### 1. Adding New Algorithms

**Steps:**

1. Fork this repository
2. Find the corresponding category YAML file in `data/algorithms/`
3. Add a new algorithm entry following the template format
4. Submit a Pull Request

**Algorithm Entry Format:**

```yaml
algorithms:
  - id: algorithm-id          # Unique identifier (lowercase, numbers, hyphens)
    name: Algorithm Name      # Algorithm name
    description: |            # Description (50-500 characters)
      Detailed description including principles, features, and use cases.
    purpose: Main purpose     # Main purpose of the algorithm
    time_complexity: O(n)     # Time complexity
    space_complexity: O(n)    # Space complexity (optional)
    category: category-id     # Category ID
    subcategory: sub-id       # Subcategory ID (optional)
    paper_url: https://...    # Original paper URL (optional)
    implementation_url: https://...  # Reference implementation URL (optional)
    related_tools:            # Related tools (optional)
      - Tool1
      - Tool2
    tags:                     # Tags (optional)
      - tag1
      - tag2
```

#### 2. Available Categories

| Category ID | Chinese Name | English Name |
|-------------|--------------|--------------|
| sequence-alignment | 序列比对 | Sequence Alignment |
| assembly | 序列组装 | Sequence Assembly |
| variant-calling | 变异检测 | Variant Calling |
| expression-analysis | 基因表达分析 | Gene Expression Analysis |
| protein-structure | 蛋白质结构预测 | Protein Structure Prediction |
| phylogenetics | 系统发育分析 | Phylogenetics |
| functional-annotation | 功能注释 | Functional Annotation |
| data-compression | 数据压缩 | Data Compression |
| single-cell | 单细胞基因组学 | Single-Cell Genomics |
| metagenomics | 宏基因组学 | Metagenomics |
| epigenomics | 表观基因组学 | Epigenomics |
| gene-prediction | 基因预测 | Gene Prediction |
| population-genetics | 群体遗传学 | Population Genetics |
| spatial-omics | 空间组学 | Spatial Omics |
| graph-genomics | 图基因组学 | Graph Genomics |
| protein-language-model | 蛋白质语言模型 | Protein Language Model |

See `data/categories.yaml` or `templates/algorithm_template.yaml` for the full subcategory list.

To quickly inspect available categories, subcategories, and existing entries, you can also run:

```bash
python -m scripts stats
python -m scripts search --category sequence-alignment
```

#### 3. Contributing to Specifications

This project follows **Spec-Driven Development (SDD)**, where all implementations are guided by documentation in the `/specs` directory.

**How to Contribute:**

1. Read existing specs (`specs/README.md`)
2. Identify specs that need updates or additions
3. Create an RFC (Request for Comments) document
4. Submit a PR for discussion, merge after community approval

**Spec Types:**
- `specs/product/` - Product requirements and feature definitions
- `specs/rfc/` - Technical design and architecture proposals
- `specs/api/` - CLI interface specifications
- `specs/db/` - Data schema definitions
- `specs/testing/` - Test specifications and acceptance criteria

See: [Spec Contributing Guide](#spec-contributing-english)

#### 4. Quality Requirements

- ✅ Description length between 50-500 characters
- ✅ All required fields must be included
- ✅ Category and subcategory IDs must be valid
- ✅ `subcategory` must belong to the selected `category`
- ✅ Algorithm IDs must be unique across the entire repository
- ✅ Correct YAML format
- ✅ Links must be valid and accessible
- ✅ `difficulty`, if provided, must be one of `beginner` / `intermediate` / `advanced`
- ✅ `references[*].type`, if provided, must be one of `tutorial` / `blog` / `video` / `book` / `documentation` / `slides`

#### 4. Local Validation

Before submitting, please run validation locally:

```bash
# Install dependencies (dev mode)
pip install -e ".[dev]"
# Or: pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Validate data
python -m scripts validate

# Generate MkDocs preview pages
python -m scripts mkdocs

# Generate README preview
python -m scripts generate
```

### Other Ways to Contribute

- 📝 Improve existing algorithm descriptions
- 🔗 Add or update reference links
- 🐛 Report bugs or issues
- 💡 Suggest new features

### Code of Conduct

- Respect all contributors
- Maintain professional and friendly communication
- Accept constructive criticism

---

<a id="spec-contributing-english"></a>

## Specification Contributing Guide

This project follows **Spec-Driven Development (SDD)**. All implementations must be guided by specifications in the `/specs` directory.

### When to Update Specs

1. **New Feature**: Create product spec → RFC → implementation
2. **Architecture Change**: Create RFC documenting the change
3. **API Changes**: Update API spec before implementation
4. **Data Schema Changes**: Update DB spec and migrate existing data

### Spec Workflow

1. **Review**: Read existing specs before proposing changes
2. **Propose**: Create RFC or update product spec
3. **Discuss**: Get community feedback via PR comments
4. **Implement**: Only after spec is approved and merged
5. **Verify**: Ensure implementation matches spec exactly

### RFC Template

```markdown
# RFC-XXXX: Title

## Status
- **Status**: Proposed | Accepted | Implemented
- **Created**: YYYY-MM-DD
- **Author**: Your Name

## Context
What problem are we solving?

## Proposal
Detailed technical proposal.

## Alternatives
What other approaches did you consider?

## Implementation Plan
How will this be implemented?

## Related Documents
Links to related specs or RFCs.
```

### Spec Quality Standards

- ✅ Clear and unambiguous language
- ✅ Examples for all patterns
- ✅ Validation rules defined explicitly
- ✅ Change history maintained
- ✅ Cross-references to related specs
- ✅ Bilingual where appropriate (English + Chinese summaries)

### AI Agent Instructions

AI assistants (Qwen Code, Cursor, etc.) must follow the spec-first workflow:
1. Read relevant specs before coding
2. Propose spec changes before implementation
3. Wait for approval before writing code
4. Implement exactly as specified in specs

See `AGENTS.md` for detailed AI workflow instructions.

---
