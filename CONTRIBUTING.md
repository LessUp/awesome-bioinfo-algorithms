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
python -m awesome_bioinfo stats
python -m awesome_bioinfo search --category sequence-alignment
```

#### 3. 参与规范文档编写

本项目采用 **OpenSpec 规范驱动开发**，`openspec/specs/` 目录是所有需求的唯一来源。规范文件直接在此目录中维护，不再使用 RFC 流程。

**何时需要提案（propose）：**
- 新增 CLI 命令、修改校验规则、重构涉及多个模块 → 使用 `/opsx:propose` 创建变更提案
- 修正已合并代码对应的规范文字、修改单个算法条目 → 直接编辑对应文件即可

**OpenSpec 标准工作流：**

1. **`/opsx:propose <想法>`** — 生成变更提案（含设计、规范更新和任务列表）
2. **`/opsx:apply`** — 逐步执行提案中的任务
3. **`/opsx:archive`** — 任务完成后归档提案、更新 Living Spec

**规范文件位置：**
- `openspec/specs/product-vision/spec.md` — 产品需求
- `openspec/specs/core-architecture/spec.md` — 技术架构
- `openspec/specs/cli-interface/spec.md` — CLI 接口
- `openspec/specs/algorithm-schema/spec.md` — 数据模式
- `openspec/specs/testing-strategy/spec.md` — 测试策略

详见：[规范贡献指南（英文）](#spec-contributing-english)

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
# 安装依赖（开发 + MkDocs）
pip install -e ".[dev,docs]"
# 或：pip install -r requirements.txt

# 运行测试
python -m pytest tests/ -v

# 校验数据
python -m awesome_bioinfo validate

# 生成 MkDocs 预览页面
python -m awesome_bioinfo mkdocs

# 生成 README 预览
python -m awesome_bioinfo generate
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
python -m awesome_bioinfo stats
python -m awesome_bioinfo search --category sequence-alignment
```

#### 3. Contributing to Specifications

This project follows **OpenSpec-driven development**. `openspec/specs/` is the single source of truth — all specs are living documents maintained directly in that directory. There is no RFC process.

**When to create a change proposal:**
- Adding a new CLI command, changing validation rules, or refactoring across multiple modules → use `/opsx:propose`
- Correcting spec wording to match already-merged code, or adding a single algorithm entry → edit directly, no proposal needed

**OpenSpec workflow:**

1. **`/opsx:propose <idea>`** — generate a change proposal (includes design, spec updates, and task list)
2. **`/opsx:apply`** — execute tasks from the proposal step by step
3. **`/opsx:archive`** — archive the proposal and update the living specs when done

**Spec locations:**
- `openspec/specs/product-vision/spec.md` — product requirements
- `openspec/specs/core-architecture/spec.md` — technical architecture
- `openspec/specs/cli-interface/spec.md` — CLI interface contracts
- `openspec/specs/algorithm-schema/spec.md` — YAML data schema
- `openspec/specs/testing-strategy/spec.md` — testing strategy

See: [Specification Contributing Guide](#spec-contributing-english)

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
# Install dependencies (dev + MkDocs)
pip install -e ".[dev,docs]"
# Or: pip install -r requirements.txt

# Run tests
python -m pytest tests/ -v

# Validate data
python -m awesome_bioinfo validate

# Generate MkDocs preview pages
python -m awesome_bioinfo mkdocs

# Generate README preview
python -m awesome_bioinfo generate
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

This project uses **OpenSpec**. Living specs in `openspec/specs/` are the single source of truth. There are no RFCs and no separate spec approval step — propose, apply, and archive via the commands below.

### Decision: Propose vs. Edit Directly

| Situation | Action |
|-----------|--------|
| Adding or correcting one algorithm entry | Edit `data/algorithms/*.yaml` directly |
| Fixing spec wording to match merged code | Edit the spec directly |
| New CLI feature, validation rule change, multi-module refactor | `/opsx:propose` → `/opsx:apply` → `/opsx:archive` |
| Updating multiple specs or introducing new spec capabilities | `/opsx:propose` → `/opsx:apply` → `/opsx:archive` |

### OpenSpec Workflow

```
/opsx:propose <idea>   # Creates proposal with design, spec diffs, and task list
/opsx:apply            # Implements tasks from the current proposal
/opsx:archive          # Updates living specs and archives the proposal
```

### Branch Strategy

- **Trivial / single-file changes**: commit directly to the default branch (currently `master`).
- **Non-trivial changes**: short-lived branch `<type>/<description>`, merged via PR, branch deleted after merge.
- Keep branches short-lived. Aim to merge within one or two days to avoid divergence.

### When to Request a Review (`/review`)

Use `/review` before merging when the change:
- modifies Python logic in `awesome_bioinfo/`
- updates a living spec in `openspec/specs/`
- adds or removes a category
- spans multiple files or modules

Pure data additions (algorithm YAML entries that pass `validate`) and documentation typo fixes do not require a review step.

### Spec Quality Standards

- ✅ Clear and unambiguous language
- ✅ Validation rules stated explicitly
- ✅ Examples for non-obvious patterns
- ✅ Cross-references to related specs
- ✅ Bilingual where appropriate (Chinese primary, English secondary)

### AI Agent Instructions

AI assistants must follow the spec-first workflow defined in `AGENTS.md`. Key points:

1. Read `openspec/specs/` before making changes.
2. Use `/opsx:propose` for non-trivial changes; edit directly for small fixes.
3. Run local verification commands before committing (see `AGENTS.md` → **Change-Based Verification**).
4. Use `/review` for changes touching Python logic or living specs.

---
