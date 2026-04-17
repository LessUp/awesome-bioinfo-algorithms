<!-- AGENTS.md - AI Agent Configuration for Awesome Bioinformatics Algorithms -->

# AGENTS.md - AI Agent Configuration

This file provides essential context for AI coding agents working on the **Awesome Bioinformatics Algorithms** project.

**中文**: 本文件为在 **Awesome Bioinformatics Algorithms** 项目上工作的 AI 编程助手提供必要的项目背景信息。

---

## Project Overview | 项目概述

**Awesome Bioinformatics Algorithms** is a curated collection of **201+ bioinformatics algorithms** across **16 categories**, providing:

- Time and space complexity analysis
- Links to original papers and implementations
- Multi-language documentation (Chinese/English)
- CLI toolkit for data management and validation

**中文**: 本项目收集和整理了 **201+ 个生物信息学算法**，涵盖 **16 个分类**，提供时间/空间复杂度分析、相关论文和实现链接，以及双语文档支持。

### Project Purpose | 项目目标

Create the most comprehensive, well-organized, and accessible collection of bioinformatics algorithms for researchers, students, and practitioners worldwide.

### Key Stats | 关键数据

| Metric | Value | 指标 | 数值 |
|:-------|------:|:-----|-----:|
| Total Algorithms | **201** | 算法总数 | **201** |
| Categories | **16** | 分类数 | **16** |
| Unique Tags | **399** | 唯一标签数 | **399** |

---

## Technology Stack | 技术栈

| Component | Technology | Version/Notes |
|-----------|------------|---------------|
| Language | Python | >=3.9 (3.9, 3.10, 3.11, 3.12) |
| Data Format | YAML | Structured algorithm entries |
| Schema Validation | JSON Schema | Draft-07 |
| Documentation | MkDocs Material | GitHub Pages deployment |
| Testing | pytest + Hypothesis | Property-based testing |
| Linting | ruff | Line length 100 |
| Type Checking | mypy | Progressive enhancement |
| Pre-commit | pre-commit | Git hooks |

---

## Project Structure | 项目结构

```
.
├── awesome_bioinfo/          # Main Python package (核心代码)
│   ├── __main__.py          # CLI entry point
│   ├── algorithm_registry.py # Algorithm data management
│   ├── category_manager.py   # Category taxonomy
│   ├── validate.py           # YAML data validation
│   ├── readme_generator.py   # README.md generation
│   ├── generate_mkdocs.py    # MkDocs site generation
│   ├── search.py             # Search functionality
│   ├── compare.py            # Algorithm comparison
│   └── ...
├── data/                     # Data files (数据文件)
│   ├── categories.yaml       # Category taxonomy (16 categories)
│   └── algorithms/           # Algorithm entries (16 YAML files)
├── specs/                    # Spec-Driven Development docs
│   ├── product/              # Product requirements (PRDs)
│   ├── rfc/                  # Technical design (RFCs)
│   ├── api/                  # CLI interface specs
│   ├── db/                   # Data schema definitions
│   └── testing/              # Test specifications
├── tests/                    # Test suite
├── templates/                # Generation templates
│   ├── algorithm_template.yaml
│   └── readme_template.md
├── schemas/                  # JSON Schema definitions
│   └── algorithm-schema.json
├── mkdocs/                   # MkDocs configuration
├── docs/                     # Documentation source
└── scripts/                  # Deprecated (use awesome_bioinfo)
```

---

## Philosophy: Spec-Driven Development (SDD) | 规范驱动开发

**This project strictly follows Spec-Driven Development.** All implementations MUST use the `/specs` directory as the single source of truth.

**中文**: 本项目严格遵循**规范驱动开发**范式。所有代码实现必须以 `/specs` 目录为唯一事实来源。

### Spec Hierarchy | 规范层级

| Directory | Purpose | Priority |
|-----------|---------|----------|
| `/specs/product/` | Product requirements and feature definitions | High |
| `/specs/rfc/` | Technical design documents and architecture | High |
| `/specs/api/` | API specifications (CLI interface definitions) | High |
| `/specs/db/` | Data schema definitions (YAML data structures) | High |
| `/specs/testing/` | Test specifications and acceptance criteria | Medium |

### AI Agent Workflow (MANDATORY) | AI 工作流（必须遵守）

**When developing new features, modifying functionality, or fixing bugs:**

1. **Step 1: Review Specs First** | 审查规范
   - MUST read relevant documentation in `/specs` directory
   - Check product requirements, RFCs, API definitions
   - **STOP immediately** if user request conflicts with existing specs

2. **Step 2: Spec-First Update** | 规范优先更新
   - Propose spec changes BEFORE implementation
   - Wait for user confirmation on spec modifications
   - Maintain document-code synchronization

3. **Step 3: Implementation** | 代码实现
   - Write code that **100% complies** with spec definitions
   - **NO gold-plating**: do not add features not in specs
   - Follow existing code conventions

4. **Step 4: Test against Spec** | 测试验证
   - Write tests based on acceptance criteria in specs
   - Run validation: `python -m awesome_bioinfo validate`

---

## Build and Test Commands | 构建与测试命令

### Environment Setup | 环境设置

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

### Formatting and Linting | 格式化和代码检查

```bash
# Format check
ruff format --check awesome_bioinfo/ tests/

# Format fix
ruff format awesome_bioinfo/ tests/

# Lint check
ruff check awesome_bioinfo/ tests/

# Lint fix
ruff check --fix awesome_bioinfo/ tests/

# Type check
mypy awesome_bioinfo/ --ignore-missing-imports

# All-in-one (pre-commit)
pre-commit run --all-files
```

### Testing | 测试

```bash
# Run all tests
python -m pytest tests/ -v --tb=short

# Run specific test file
python -m pytest tests/test_validate.py -v

# Run with keyword filter
python -m pytest tests/test_validate.py -k missing_required -v

# Run with coverage
python -m pytest tests/ --cov=awesome_bioinfo --cov-branch --cov-report=term-missing
```

### CLI Commands | CLI 命令

```bash
python -m awesome_bioinfo validate                    # Validate all YAML data
python -m awesome_bioinfo stats                       # Show statistics
python -m awesome_bioinfo search <query>              # Search algorithms
python -m awesome_bioinfo info <algorithm-id>         # Show algorithm details
python -m awesome_bioinfo compare <id1> <id2>         # Compare algorithms
python -m awesome_bioinfo export --format json        # Export data
python -m awesome_bioinfo generate                    # Generate README.md
python -m awesome_bioinfo mkdocs                      # Generate MkDocs site
python -m awesome_bioinfo check-links                 # Check URL validity
```

### MkDocs | 文档构建

```bash
python -m awesome_bioinfo mkdocs
mkdocs build -f mkdocs/mkdocs.yml -d ./_site
```

### Verification | 验证

```bash
# Ensure generated outputs are up-to-date
git diff --exit-code -- README.md mkdocs/docs/
```

---

## Code Style Guidelines | 代码风格规范

### Python Style | Python 风格

| Rule | Value/Description |
|------|-------------------|
| Target runtime | Python `>=3.9` |
| Line length | 100 characters |
| Lint rules | `E`, `F`, `W`, `I`, `N`, `UP`, `B`, `C4` |
| Ignored rules | `E501` (line length handled by formatter) |
| Formatter | `ruff format` |
| Import sorting | ruff managed |

### Naming Conventions | 命名规范

| Type | Convention | Example |
|------|------------|---------|
| Functions/Methods/Variables | `snake_case` | `load_algorithms()` |
| Classes/Dataclasses | `PascalCase` | `AlgorithmEntry` |
| Constants | `UPPER_SNAKE_CASE` | `MAX_DESCRIPTION_LENGTH` |
| Algorithm IDs | lowercase, hyphenated | `smith-waterman` |
| Tags | lowercase, hyphenated | `dynamic-programming` |

### Type Hints | 类型提示

- Use built-in generics: `list[str]`, `dict[str, int]` (not `typing.List`, `typing.Dict`)
- Prefer dataclasses for simple records
- Add type hints to public functions

### Error Handling | 错误处理

| Scenario | Approach |
|----------|----------|
| CLI errors | Print actionable messages, return non-zero status |
| Invalid user data | Use `ValidationResult.errors` and `warnings` |
| Invariant failures | Raise specific exceptions (`FileNotFoundError`, `ValueError`) |
| Bare `except` | **Never use** |

---

## Testing Strategy | 测试策略

### Testing Framework | 测试框架

- **pytest**: Main testing framework
- **Hypothesis**: Property-based testing
- **pytest-cov**: Coverage reporting (85% minimum)
- **pytest-benchmark**: Performance benchmarks

### Test Organization | 测试组织

| Test File | Coverage |
|-----------|----------|
| `test_validate.py` | YAML validation logic |
| `test_algorithm_registry.py` | Algorithm loading and registry |
| `test_category_manager.py` | Category management |
| `test_cli.py` | CLI entry points |
| `test_data_io.py` | Data import/export |
| `test_export_cmd.py` | Export command |
| `test_search.py` | Search functionality |
| `test_schema.py` | Data schema validation |

### Property-Based Testing | 基于属性的测试

Use Hypothesis for testing invariants:

```python
from hypothesis import given, strategies as st

@given(st.text(min_size=50, max_size=500))
def test_description_length(description):
    # Description must be 50-500 characters
    assert 50 <= len(description.strip()) <= 500
```

---

## Data and YAML Conventions | 数据和 YAML 规范

### Algorithm Entry Structure | 算法条目结构

**Required Fields** | 必填字段:
- `id` - Unique identifier (lowercase, hyphenated)
- `name` - Human-readable name
- `description` - 50-500 characters after trimming
- `purpose` - Main use case
- `time_complexity` - Big-O notation (e.g., `O(n)`, `O(mn)`)
- `category` - Must be valid category ID

**Optional Fields** | 可选字段:
- `space_complexity` - Big-O notation
- `year` - Publication year (1950-2100)
- `paper_url` - DOI or paper URL
- `implementation_url` - GitHub/repository URL
- `related_tools` - List of related tools
- `tags` - List of tags (lowercase, hyphenated)
- `subcategory` - Must belong to specified category
- `difficulty` - `beginner`, `intermediate`, or `advanced`
- `language` - Implementation language (e.g., `C++`, `Python`)
- `references` - Extended reference materials

### Category Taxonomy | 分类体系

16 Main Categories | 主分类:
1. `sequence-alignment` - 序列比对
2. `assembly` - 序列组装
3. `variant-calling` - 变异检测
4. `expression-analysis` - 基因表达分析
5. `protein-structure` - 蛋白质结构预测
6. `phylogenetics` - 系统发育分析
7. `functional-annotation` - 功能注释
8. `data-compression` - 数据压缩
9. `single-cell` - 单细胞基因组学
10. `metagenomics` - 宏基因组学
11. `epigenomics` - 表观基因组学
12. `gene-prediction` - 基因预测
13. `population-genetics` - 群体遗传学
14. `spatial-omics` - 空间组学
15. `graph-genomics` - 图基因组学
16. `protein-language-model` - 蛋白质语言模型

See `data/categories.yaml` for complete subcategory list.

### Validation Rules | 验证规则

| Field | Rule |
|-------|------|
| `id` | Lowercase, hyphenated, 3-50 chars, globally unique |
| `description` | 50-500 characters (trimmed) |
| `tags` | Lowercase, hyphenated, `^[a-z0-9]+(-[a-z0-9]+)*$` |
| `category` | Must exist in `data/categories.yaml` |
| `subcategory` | Must belong to specified `category` |
| `difficulty` | One of: `beginner`, `intermediate`, `advanced` |
| `references[*].type` | One of: `tutorial`, `blog`, `video`, `book`, `documentation`, `slides` |

---

## CI/CD and Deployment | 持续集成与部署

### GitHub Actions Workflow | 工作流

| Job | Description |
|-----|-------------|
| `lint` | ruff format check, ruff lint, mypy type check |
| `test` | Python 3.9-3.12 matrix, coverage on 3.11 |
| `verify-repository-tools` | CLI smoke checks, diff verification |

### What CI Actually Runs | CI 实际运行

1. **Lint**: `ruff format --check`, `ruff check`, `mypy`
2. **Test**: Python matrix with coverage collection on 3.11
3. **CLI Smoke Tests**: All CLI commands execution
4. **Diff Check**: `git diff --exit-code -- README.md mkdocs/docs/`
5. **MkDocs Build**: `mkdocs build` for GitHub Pages

### Change-Based Command Checklist | 基于变更的命令检查清单

| Change Type | Commands to Run |
|-------------|-----------------|
| Python in `awesome_bioinfo/` or `tests/` | `ruff`, `mypy`, relevant pytest |
| Validation logic | Focused test, then full suite |
| CLI behavior | Relevant `python -m awesome_bioinfo ...` command |
| `data/` YAML | `python -m awesome_bioinfo validate` |
| `templates/readme_template.md` | `python -m awesome_bioinfo generate` |
| MkDocs generation | `python -m awesome_bioinfo mkdocs`, `mkdocs build` |

---

## Generated Outputs | 生成输出

These files are **auto-generated**. Do not hand-edit.

| Output | Source | Generation Command |
|--------|--------|-------------------|
| `README.md` | Template + algorithm data | `python -m awesome_bioinfo generate` |
| `mkdocs/docs/` | Algorithm data | `python -m awesome_bioinfo mkdocs` |

When generator inputs change, regenerate outputs before considering work complete.

---

## Pre-commit Hooks | 预提交钩子

Configured in `.pre-commit-config.yaml`:

1. **ruff** - Linting and formatting
2. **mypy** - Type checking
3. **check-yaml** - YAML syntax validation
4. **check-jsonschema** - Validate algorithm YAML against schema
5. **trailing-whitespace** - Whitespace cleanup
6. **end-of-file-fixer** - EOF newline
7. **check-added-large-files** - File size limit (1MB)

---

## Security Considerations | 安全考虑

- Never commit sensitive files (`.env`, credentials)
- URLs in algorithm entries should be to reputable sources
- External links are validated periodically with `check-links` command
- No execution of user-provided code

---

## Common Tasks | 常见任务

### Adding a New Algorithm | 添加新算法

1. Edit the appropriate file in `data/algorithms/` (e.g., `sequence-alignment.yaml`)
2. Copy template from `templates/algorithm_template.yaml`
3. Fill in all required fields
4. Run `python -m awesome_bioinfo validate` to verify
5. Run `python -m awesome_bioinfo generate` to update README
6. Run `python -m awesome_bioinfo mkdocs` to update docs

### Adding a New Category | 添加新分类

1. Update `data/categories.yaml`
2. Update `schemas/algorithm-schema.json` category enum
3. Create RFC in `specs/rfc/` for community review
4. Update `templates/algorithm_template.yaml`

### Adding a New CLI Command | 添加新 CLI 命令

1. Update `specs/api/001-cli-interface.md`
2. Add command handler in `awesome_bioinfo/__main__.py`
3. Implement logic in new module (e.g., `awesome_bioinfo/new_cmd.py`)
4. Add tests in `tests/test_<command>.py`
5. Update CLI documentation

---

## Useful Resources | 有用资源

| Resource | Location |
|----------|----------|
| Contributing Guide | `CONTRIBUTING.md` |
| Spec Documentation | `specs/README.md` |
| Algorithm Template | `templates/algorithm_template.yaml` |
| JSON Schema | `schemas/algorithm-schema.json` |
| Category Taxonomy | `data/categories.yaml` |
| CLI Spec | `specs/api/001-cli-interface.md` |
| Data Schema Spec | `specs/db/001-algorithm-entry.md` |

---

## Rule Sources | 规则来源优先级

| Source | Priority | Description |
|--------|----------|-------------|
| `/specs/` | **Highest** | Specifications - single source of truth |
| `pyproject.toml` | High | Project configuration and dependencies |
| `.pre-commit-config.yaml` | Medium | Pre-commit hooks |
| `.github/workflows/ci.yml` | Medium | CI behavior |
| `CONTRIBUTING.md` | Medium | Contributor guidance |

---

## Language and Communication | 语言和沟通

This project supports **bilingual documentation** (English and Chinese).

- Code and comments: English preferred
- Documentation: Both languages
- CLI output: Bilingual where appropriate
- Commit messages: English preferred

---

*Last updated: 2026-04-17*
*Version: 1.0.0*
