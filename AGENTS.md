# AGENTS.md - AI Agent Configuration

## Project Philosophy: Spec-Driven Development (SDD)

This repository strictly follows **Spec-Driven Development (SDD)** paradigm. All code implementations must use the `/specs` directory documentation as the single source of truth.

**中文**: 本项目严格遵循**规范驱动开发（Spec-Driven Development）**范式。所有的代码实现必须以 `/specs` 目录下的规范文档为唯一事实来源（Single Source of Truth）。

---

## Directory Context (目录说明)

### Core Specifications (`/specs/`)

| Directory | Purpose | 中文说明 |
|-----------|---------|----------|
| `/specs/product/` | Product requirements and feature definitions (PRDs) | 产品需求文档 |
| `/specs/rfc/` | Technical design documents and architecture proposals | 技术设计与架构方案 |
| `/specs/api/` | API specifications (CLI interface definitions) | CLI 接口规范 |
| `/specs/db/` | Data schema definitions (YAML data structures) | 数据 Schema 定义 |
| `/specs/testing/` | Test specifications and acceptance criteria | 测试规范与验收标准 |

### Documentation (`/docs/`)

| Directory | Purpose |
|-----------|---------|
| `/docs/en/` | English documentation |
| `/docs/zh/` | Chinese documentation (简体中文) |
| `/docs/blog/` | Project blog posts and announcements |

### Data and Templates (`/data/`, `/templates/`)

| Path | Description |
|------|-------------|
| `/data/categories.yaml` | Category taxonomy (16 categories) |
| `/data/algorithms/*.yaml` | Algorithm entry files (201 algorithms) |
| `/templates/readme_template.md` | README generation template |
| `/templates/algorithm_template.yaml` | Algorithm entry template |

### Source Code (`/scripts/`, `/tests/`)

| Directory | Description |
|-----------|-------------|
| `/scripts/` | Python CLI tools and utilities |
| `/tests/` | Pytest test suite with Hypothesis property-based tests |

---

## AI Agent Workflow Instructions (AI 工作流指令)

When you (AI) are asked to develop a new feature, modify existing functionality, or fix a bug, **you MUST strictly follow this workflow without skipping any steps**:

### Step 1: 审查与分析 (Review Specs)

- **MUST** first read relevant documentation in `/specs` directory
- Check product requirements, RFCs, and API definitions
- If user request conflicts with existing specs, **STOP immediately** and point out the conflict, asking user whether to update specs first

### Step 2: 规范优先 (Spec-First Update)

- For new features or changes to interfaces/data structures, **MUST propose spec changes first**
- Wait for user confirmation on spec modifications before proceeding to code
- Ensure document-code synchronization at all times

### Step 3: 代码实现 (Implementation)

- Write code that **100% complies** with spec definitions
- **No gold-plating**: do not add features not defined in specs
- Follow existing code conventions from `/scripts/`

### Step 4: 测试验证 (Test against Spec)

- Write tests based on acceptance criteria in specs
- Ensure test coverage matches spec boundary conditions
- Run validation: `python -m scripts validate`

---

## Rule Sources

| Source | Priority | Description |
|--------|----------|-------------|
| `/specs/` | **Highest** | Specifications - single source of truth for implementation |
| `pyproject.toml` | High | Project configuration and dependencies |
| `.pre-commit-config.yaml` | Medium | Pre-commit hooks |
| `.github/workflows/ci.yml` | Medium | CI behavior |
| `CONTRIBUTING.md` | Medium | Contributor guidance |

---

## Environment Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

---

## Build, Lint, Test, and Validation Commands

### Formatting and Linting

```bash
# Format check
ruff format --check scripts/ tests/

# Format fix
ruff format scripts/ tests/

# Lint check
ruff check scripts/ tests/

# Lint fix
ruff check --fix scripts/ tests/

# Type check
mypy scripts/ --ignore-missing-imports

# All-in-one (pre-commit)
pre-commit run --all-files
```

### Testing

```bash
# Run all tests
python -m pytest tests/ -v --tb=short

# Run specific test file
python -m pytest tests/test_validate.py -v

# Run with keyword filter
python -m pytest tests/test_validate.py -k missing_required -v

# Run with coverage
python -m pytest tests/ --cov=scripts --cov-branch --cov-report=term-missing
```

### CLI Commands

```bash
python -m scripts validate                    # Validate all YAML data
python -m scripts stats                       # Show statistics
python -m scripts search <query>              # Search algorithms
python -m scripts info <algorithm-id>         # Show algorithm details
python -m scripts compare <id1> <id2>         # Compare algorithms
python -m scripts export --format json        # Export data
python -m scripts generate                    # Generate README.md
python -m scripts mkdocs                      # Generate MkDocs site
```

### MkDocs

```bash
python scripts/generate_mkdocs.py
mkdocs build -f mkdocs/mkdocs.yml -d ./_site
```

### Verification

```bash
git diff --exit-code -- README.md mkdocs/docs/
```

---

## What CI Actually Runs

1. **Lint job**: `ruff format --check`, `ruff check`, `mypy`
2. **Test job**: Python 3.9, 3.10, 3.11, 3.12 matrix
3. **Coverage**: Collected on Python 3.11 with `--cov=scripts --cov-branch`
4. **Verification**: CLI smoke checks for all commands
5. **Diff check**: `git diff --exit-code -- README.md mkdocs/docs/`
6. **Pages**: `mkdocs build` for GitHub Pages deployment

---

## Change-Based Command Checklist

| Change Type | Commands to Run |
|-------------|-----------------|
| Python in `scripts/` or `tests/` | `ruff`, `mypy`, relevant pytest target |
| Validation logic | Focused test file, then full suite |
| CLI behavior | Relevant `python -m scripts ...` command, update tests |
| `data/` YAML | `python -m scripts validate` |
| `templates/readme_template.md` | `python -m scripts generate` |
| MkDocs generation | `python -m scripts mkdocs`, `mkdocs build` |

---

## Python Style and Formatting

| Rule | Value/Description |
|------|-------------------|
| Target runtime | Python `>=3.9` |
| Line length | 100 characters |
| Lint rules | `E`, `F`, `W`, `I`, `N`, `UP`, `B`, `C4` |
| Ignored rules | `E501` |
| Formatter | `ruff format` |
| Import sorting | Ruff managed |
| Naming: functions/methods/variables | `snake_case` |
| Naming: classes/dataclasses | `PascalCase` |
| Naming: constants | `UPPER_SNAKE_CASE` |
| Generics | Prefer built-in `list[str]`, `dict[str, int]` |
| Data structures | Prefer dataclasses for simple records |

---

## Data and YAML Conventions

| Field | Rule |
|-------|------|
| Top-level category key | `categories:` |
| Top-level algorithm key | `algorithms:` |
| Algorithm IDs | lowercase, hyphenated, unique |
| Required algorithm fields | `id`, `name`, `description`, `purpose`, `time_complexity`, `category` |
| Optional algorithm fields | `space_complexity`, `year`, `paper_url`, `implementation_url`, `related_tools`, `tags`, `subcategory`, `difficulty`, `language`, `references` |
| Description length | 50-500 characters after trimming |
| `difficulty` values | `beginner`, `intermediate`, `advanced` |
| `references[*].type` values | `tutorial`, `blog`, `video`, `book`, `documentation`, `slides` |

---

## Error Handling Conventions

| Scenario | Approach |
|----------|----------|
| CLI errors | Print actionable messages, return non-zero status |
| Invalid user data | Collect in `ValidationResult.errors` and `ValidationResult.warnings` |
| Invariant failures | Raise specific exceptions (`FileNotFoundError`, `ValueError`) |
| Bare `except` | **Never use** |

---

## Generated Outputs

| Output | Source | Note |
|--------|--------|------|
| `README.md` | Generated from template | Do not hand-edit |
| `mkdocs/docs/` | Generated by mkdocs command | Do not hand-edit |

When generator inputs change, regenerate outputs before considering work complete.

---

## Code Generation Rules

1. Any externally exposed API changes **MUST** update `/specs/api/` specifications
2. When uncertain about technical details, consult `/specs/rfc/` architecture documents
3. **No gold-plating**: implement only what is specified in specs
4. Maintain document-code synchronization at all times

---

## Why These Rules Exist (为什么这些规则存在)

| Rule | Purpose |
|------|---------|
| **Prevent AI hallucinations** | Forcing spec-first approach anchors AI thinking to documented requirements |
| **Ensure document-code synchronization** | Specs are updated before code, keeping documentation current |
| **Improve PR quality** | Implementation aligned with business logic through spec-defined acceptance criteria |
| **Reduce rework** | Clear specs prevent misunderstandings and unnecessary refactoring |

---

## Quick Reference: Specs Structure

```
specs/
├── product/                    # 产品与功能需求 (PRD)
│   └── 000-product-vision.md
├── rfc/                        # 技术设计与架构方案 (RFCs)
│   ├── 0001-core-architecture.md
│   └── 0002-project-history-archive.md
├── api/                        # 接口规范
│   └── 001-cli-interface.md
├── db/                         # 数据库 Schema 设计规范
│   └── 001-algorithm-entry.md
└── testing/                    # 测试规范
    └── 001-cli-tests.md
```

For detailed spec workflow, see `/specs/README.md`.
