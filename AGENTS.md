# AGENTS.md - AI Agent Configuration

## Project Philosophy: Spec-Driven Development (SDD)

This repository strictly follows **Spec-Driven Development (SDD)** paradigm. All code implementations must use the `/specs` directory documentation as the single source of truth.

**中文**: 本项目严格遵循**规范驱动开发（Spec-Driven Development）**范式。所有的代码实现必须以 `/specs` 目录下的规范文档为唯一事实来源。

---

## Directory Context (目录说明)

### Core Specifications (`/specs/`)
- `/specs/product/` - Product requirements and feature definitions (PRDs)
- `/specs/rfc/` - Technical design documents and architecture proposals
- `/specs/api/` - API specifications (CLI interface definitions)
- `/specs/db/` - Data schema definitions (YAML data structures)
- `/specs/testing/` - Test specifications and acceptance criteria

### Documentation (`/docs/`)
- `/docs/en/` - English documentation
- `/docs/zh/` - Chinese documentation (简体中文)
- `/docs/blog/` - Project blog posts and announcements
- `/docs/DEVELOPMENT.md` - Development setup and workflow guide

### Data and Templates (`/data/`, `/templates/`)
- `/data/categories.yaml` - Category taxonomy
- `/data/algorithms/*.yaml` - Algorithm entry files
- `/templates/readme_template.md` - README generation template
- `/templates/algorithm_template.yaml` - Algorithm entry template

### Source Code (`/scripts/`, `/tests/`)
- `/scripts/` - Python CLI tools and utilities
- `/tests/` - Pytest test suite with Hypothesis property-based tests

---

## AI Agent Workflow Instructions (AI 工作流指令)

When you (AI) are asked to develop a new feature, modify existing functionality, or fix a bug, **you MUST strictly follow this workflow without skipping any steps**:

### Step 1: 审查与分析 (Review Specs)
- First, read relevant documentation in `/specs` directory
- Check product requirements, RFCs, and API definitions
- If user request conflicts with existing specs, **STOP immediately** and point out the conflict, asking user whether to update specs first

### Step 2: 规范优先 (Spec-First Update)
- For new features or changes to interfaces/data structures, **MUST propose spec changes first**
- Wait for user confirmation on spec modifications before proceeding to code
- Ensure document-code synchronization at all times

### Step 3: 代码实现 (Implementation)
- Write code that **100% complies** with spec definitions
- No gold-plating: do not add features not defined in specs
- Follow existing code conventions from `/scripts/`

### Step 4: 测试验证 (Test against Spec)
- Write tests based on acceptance criteria in specs
- Ensure test coverage matches spec boundary conditions
- Run validation: `python -m scripts validate`

---

## Rule Sources

- **Primary source of truth**: `pyproject.toml`
- **Specifications**: `/specs/` directory (NEW - highest priority for implementation)
- **Pre-commit automation**: `.pre-commit-config.yaml`
- **CI behavior**: `.github/workflows/ci.yml` and `.github/workflows/pages.yml`
- **Contributor guidance**: `CONTRIBUTING.md` and `docs/DEVELOPMENT.md`
- **PR expectations**: `.github/PULL_REQUEST_TEMPLATE.md`

---

## Repository Map

### Specifications (NEW)
- `/specs/product/` - Product requirement documents
- `/specs/rfc/` - Request for Comments (technical designs)
- `/specs/api/` - CLI API specifications
- `/specs/db/` - Data schema definitions
- `/specs/testing/` - Test specifications

### Source Code
- `scripts/` - Python source for validation, registry loading, README generation, MkDocs generation, and CLI commands
- `tests/` - Pytest suite, including property-based tests with Hypothesis

### Data
- `data/categories.yaml` - Category taxonomy
- `data/algorithms/*.yaml` - Algorithm entries
- `templates/readme_template.md` - Source template for generated `README.md`
- `templates/algorithm_template.yaml` - Algorithm entry template

### Documentation
- `README.md` - Generated repository landing document (English)
- `README.zh-CN.md` - Chinese version (简体中文)
- `docs/` - MkDocs documentation source
- `mkdocs/` - MkDocs configuration

### Configuration
- `pyproject.toml` - Project configuration and dependencies
- `requirements.txt` - Convenience wrapper around `-e .[dev]`
- `.pre-commit-config.yaml` - Pre-commit hooks

---

## Environment Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
# or: pip install -r requirements.txt
```

---

## Build, Lint, Test, and Validation Commands

Use these commands from the repository root.

```bash
# Formatting
ruff format --check scripts/ tests/
ruff format scripts/ tests/

# Linting
ruff check scripts/ tests/
ruff check --fix scripts/ tests/
mypy scripts/ --ignore-missing-imports

# Pre-commit
pre-commit run --all-files

# Testing
python -m pytest tests/ -v --tb=short
python -m pytest tests/test_validate.py -v
python -m pytest tests/test_validate.py::test_category_missing_required_field -v
python -m pytest tests/test_validate.py -k missing_required -v
python -m pytest tests/ --cov=scripts --cov-branch --cov-report=term-missing

# CLI Commands
python -m scripts validate
python -m scripts stats
python -m scripts search smith
python -m scripts info smith-waterman
python -m scripts compare smith-waterman needleman-wunsch
python -m scripts export --format json > /tmp/algorithms.json
python -m scripts generate
python -m scripts mkdocs

# MkDocs
python scripts/generate_mkdocs.py
mkdocs build -f mkdocs/mkdocs.yml -d ./_site

# Verification
git diff --exit-code -- README.md mkdocs/docs/
```

---

## What CI Actually Runs

- Lint job runs `ruff format --check scripts/ tests/`
- Lint job runs `ruff check scripts/ tests/`
- Lint job runs `mypy scripts/ --ignore-missing-imports`
- Test job runs on Python `3.9`, `3.10`, `3.11`, and `3.12`
- Coverage is collected on Python `3.11` with `--cov=scripts --cov-branch --cov-report=term-missing`
- Repository verification also runs CLI smoke checks for `validate`, `stats`, `search`, `info`, `compare`, `export`, `mkdocs`, and `generate`
- CI then checks that generated outputs are up to date with `git diff --exit-code -- README.md mkdocs/docs/`
- Pages deployment separately runs `python scripts/generate_mkdocs.py` and `mkdocs build -f mkdocs/mkdocs.yml -d ./_site`

---

## Change-Based Command Checklist

- If you edit only Python under `scripts/` or tests, run Ruff, mypy, and the smallest relevant pytest target
- If you edit validation logic, prefer a focused test file first, then the full suite
- If you edit CLI behavior, run the relevant `python -m scripts ...` command directly and update smoke-style tests
- If you edit `data/` YAML, run `python -m scripts validate`
- If you edit `data/`, `templates/readme_template.md`, or `scripts/readme_generator.py`, run `python -m scripts generate`
- If you edit MkDocs generation or pages content, run `python -m scripts mkdocs` and `mkdocs build -f mkdocs/mkdocs.yml -d ./_site`
- `pre-commit run --all-files` is the closest local approximation to the repo hooks

---

## Python Style and Formatting

- Target runtime declared in `pyproject.toml`: Python `>=3.9`
- Ruff line length is `100`
- Ruff lint rules selected: `E`, `F`, `W`, `I`, `N`, `UP`, `B`, `C4`
- `E501` is ignored, but keep lines near the 100-column limit unless surrounding code clearly differs
- Use `ruff format` for formatting
- Let Ruff manage import sorting
- Keep imports grouped as standard library, third-party, then local package imports
- Inside `scripts/`, prefer relative imports such as `from .schema import AlgorithmEntry`
- Preserve module-level docstrings; this codebase uses them consistently
- Preserve docstrings on public classes and functions
- Use `snake_case` for functions, methods, variables, modules, and CLI option names
- Use `PascalCase` for classes and dataclasses
- Use `UPPER_SNAKE_CASE` for module-level constants
- Prefer explicit return annotations on public functions
- Built-in generics like `list[str]` and `dict[str, int]` are common and acceptable
- Some modules use `Optional[T]` while newer ones use `Path | None`; match the local file instead of restyling unrelated annotations
- Favor straightforward loops, comprehensions, and small helpers over extra abstraction
- Prefer dataclasses for simple structured records
- Avoid introducing new dependencies unless the task truly requires them

---

## Naming and Structure Conventions

- Public CLI wrappers generally return `int` exit codes
- Internal state on classes commonly uses leading underscores, for example `_registry` or `_by_id`
- Validation/statistics/result containers are represented as dataclasses
- File names under `tests/` follow `test_*.py`
- Test names are descriptive sentences in `snake_case`
- Match the path API already used in the file: older modules often use `os.path`, newer ones often use `pathlib.Path`

---

## Error Handling Conventions

- For CLI code, print actionable messages and return a non-zero status rather than raising uncaught exceptions
- For invalid user data, prefer collecting issues in `ValidationResult.errors` and `ValidationResult.warnings`
- Warnings are allowed without failing when that matches existing validator behavior
- Raise specific exceptions for true invariant failures or missing resources
- Existing examples include `FileNotFoundError` for missing inputs and `ValueError` for duplicate IDs
- Avoid bare `except` blocks
- Keep error text specific enough for tests to assert on substrings

---

## File I/O and Serialization

- Open text files with `encoding="utf-8"`
- Preserve Unicode content; the repository intentionally contains Chinese and English text
- YAML writes in `scripts/data_io.py` use `yaml.safe_dump(..., allow_unicode=True, default_flow_style=False, sort_keys=False)`
- Preserve stable field ordering when editing serialized structures
- Do not rewrite files just to normalize quoting or line wrapping if semantics are unchanged

---

## Testing Conventions

- Use pytest
- Shared fixtures live in `tests/conftest.py`
- Prefer focused tests for the exact behavior changed
- Use `tmp_path` for filesystem outputs
- Use `monkeypatch` for CLI isolation and dependency stubbing
- Hypothesis is already used for validator/property tests; extend existing strategies instead of inventing a second style
- When debugging, start with a single test node or `-k` filter before running the whole suite

---

## Data and YAML Conventions

- Top-level category file key is `categories:`
- Top-level algorithm file key is `algorithms:`
- Algorithm IDs must be lowercase, hyphenated, and unique across the entire repository
- Required algorithm fields are `id`, `name`, `description`, `purpose`, `time_complexity`, and `category`
- Supported optional algorithm fields are `space_complexity`, `year`, `paper_url`, `implementation_url`, `related_tools`, `tags`, `subcategory`, `difficulty`, `language`, and `references`
- Description length must remain within 50-500 characters after trimming
- `subcategory` must belong to the selected parent `category`
- `difficulty` must be one of `beginner`, `intermediate`, or `advanced`
- `references[*].type` should be one of `tutorial`, `blog`, `video`, `book`, `documentation`, or `slides`
- Preserve field ordering from `templates/algorithm_template.yaml` and `AlgorithmEntry.to_dict()` when possible
- Keep bilingual or Chinese-language content intact unless the task explicitly changes wording

---

## Generated Outputs

- `README.md` is generated content
- `mkdocs/docs/` contains generated documentation pages
- Do not hand-edit generated outputs unless the task is specifically about the generated artifact and the source generator is also updated when needed
- When generator inputs change, regenerate outputs before considering the work complete

---

## Code Generation Rules

- Any externally exposed API changes must update `/specs/api/` specifications
- When uncertain about technical details, consult `/specs/rfc/` architecture documents
- **No gold-plating**: implement only what is specified in specs
- Maintain document-code synchronization at all times

---

## Why These Rules Exist (为什么这些规则存在)

1. **Prevent AI hallucinations**: Forcing spec-first approach anchors AI thinking to documented requirements
2. **Ensure document-code synchronization**: Specs are updated before code, keeping documentation current
3. **Improve PR quality**: Implementation aligned with business logic through spec-defined acceptance criteria
4. **Reduce rework**: Clear specs prevent misunderstandings and unnecessary refactoring

**中文说明**:
1. **防止 AI 幻觉**: 强制优先查阅规范可以将 AI 的思考范围锚定在已 documented 的需求上
2. **确保文档与代码同步**: 先改规范再写代码，保证文档永远最新
3. **提高 PR 质量**: 按照 Spec 中的验收标准开发，确保实现与业务逻辑一致
4. **减少返工**: 清晰的规范避免理解偏差和不必要的重构
