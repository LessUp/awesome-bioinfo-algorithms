# AGENTS.md

## Purpose

- This repository is a Python-based maintenance toolkit plus a curated bioinformatics algorithm dataset.
- The main executable surface is the `scripts` package and its CLI entrypoint: `python -m scripts ...`.
- Most changes touch one of three areas: Python maintenance code, YAML data, or generated documentation.
- Run repository-aware commands from the repository root.
- The CLI assumes an intact checkout containing `data/`, `templates/`, and generated docs paths.

## Rule Sources

- Primary source of truth: `pyproject.toml`.
- Pre-commit automation: `.pre-commit-config.yaml`.
- CI behavior: `.github/workflows/ci.yml` and `.github/workflows/pages.yml`.
- Contributor guidance: `CONTRIBUTING.md` and `docs/DEVELOPMENT.md`.
- PR expectations: `.github/PULL_REQUEST_TEMPLATE.md`.
- There is currently no `.cursorrules` file.
- There is currently no `.cursor/rules/` directory.
- There is currently no `.github/copilot-instructions.md` file.

## Repository Map

- `scripts/`: Python source for validation, registry loading, README generation, MkDocs generation, and CLI commands.
- `tests/`: pytest suite, including property-based tests with Hypothesis.
- `data/categories.yaml` and `data/algorithms/*.yaml`: category taxonomy and algorithm entries.
- `templates/readme_template.md`: source template for generated `README.md`.
- `mkdocs/` and `docs/`: MkDocs config, generated docs sources, and hand-written docs.
- `README.md`: generated repository landing document.
- `requirements.txt`: convenience wrapper around `-e .[dev]`.

## Environment Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
# or: pip install -r requirements.txt
```

## Build, Lint, Test, and Validation Commands

Use these commands from the repository root.

```bash
ruff format --check scripts/ tests/
ruff format scripts/ tests/
ruff check scripts/ tests/
ruff check --fix scripts/ tests/
mypy scripts/ --ignore-missing-imports
pre-commit run --all-files
python -m pytest tests/ -v --tb=short
python -m pytest tests/test_validate.py -v
python -m pytest tests/test_validate.py::test_category_missing_required_field -v
python -m pytest tests/test_validate.py -k missing_required -v
python -m pytest tests/ --cov=scripts --cov-branch --cov-report=term-missing
python -m scripts validate
python -m scripts stats
python -m scripts search smith
python -m scripts info smith-waterman
python -m scripts compare smith-waterman needleman-wunsch
python -m scripts export --format json > /tmp/algorithms.json
python -m scripts generate
python -m scripts mkdocs
python scripts/generate_mkdocs.py
mkdocs build -f mkdocs/mkdocs.yml -d ./_site
git diff --exit-code -- README.md mkdocs/docs/
```

## What CI Actually Runs

- Lint job runs `ruff format --check scripts/ tests/`.
- Lint job runs `ruff check scripts/ tests/`.
- Lint job runs `mypy scripts/ --ignore-missing-imports`.
- Test job runs on Python `3.9`, `3.10`, `3.11`, and `3.12`.
- Coverage is collected on Python `3.11` with `--cov=scripts --cov-branch --cov-report=term-missing`.
- Repository verification also runs CLI smoke checks for `validate`, `stats`, `search`, `info`, `compare`, `export`, `mkdocs`, and `generate`.
- CI then checks that generated outputs are up to date with `git diff --exit-code -- README.md mkdocs/docs/`.
- Pages deployment separately runs `python scripts/generate_mkdocs.py` and `mkdocs build -f mkdocs/mkdocs.yml -d ./_site`.

## Change-Based Command Checklist

- If you edit only Python under `scripts/` or tests, run Ruff, mypy, and the smallest relevant pytest target.
- If you edit validation logic, prefer a focused test file first, then the full suite.
- If you edit CLI behavior, run the relevant `python -m scripts ...` command directly and update smoke-style tests.
- If you edit `data/` YAML, run `python -m scripts validate`.
- If you edit `data/`, `templates/readme_template.md`, or `scripts/readme_generator.py`, run `python -m scripts generate`.
- If you edit MkDocs generation or pages content, run `python -m scripts mkdocs` and `mkdocs build -f mkdocs/mkdocs.yml -d ./_site`.
- `pre-commit run --all-files` is the closest local approximation to the repo hooks.

## Python Style and Formatting

- Target runtime declared in `pyproject.toml`: Python `>=3.9`.
- Ruff line length is `100`.
- Ruff lint rules selected: `E`, `F`, `W`, `I`, `N`, `UP`, `B`, `C4`.
- `E501` is ignored, but keep lines near the 100-column limit unless surrounding code clearly differs.
- Use `ruff format` for formatting.
- Let Ruff manage import sorting.
- Keep imports grouped as standard library, third-party, then local package imports.
- Inside `scripts/`, prefer relative imports such as `from .schema import AlgorithmEntry`.
- Preserve module-level docstrings; this codebase uses them consistently.
- Preserve docstrings on public classes and functions.
- Use `snake_case` for functions, methods, variables, modules, and CLI option names.
- Use `PascalCase` for classes and dataclasses.
- Use `UPPER_SNAKE_CASE` for module-level constants.
- Prefer explicit return annotations on public functions.
- Built-in generics like `list[str]` and `dict[str, int]` are common and acceptable.
- Some modules use `Optional[T]` while newer ones use `Path | None`; match the local file instead of restyling unrelated annotations.
- Favor straightforward loops, comprehensions, and small helpers over extra abstraction.
- Prefer dataclasses for simple structured records.
- Avoid introducing new dependencies unless the task truly requires them.

## Naming and Structure Conventions

- Public CLI wrappers generally return `int` exit codes.
- Internal state on classes commonly uses leading underscores, for example `_registry` or `_by_id`.
- Validation/statistics/result containers are represented as dataclasses.
- File names under `tests/` follow `test_*.py`.
- Test names are descriptive sentences in `snake_case`.
- Match the path API already used in the file: older modules often use `os.path`, newer ones often use `pathlib.Path`.

## Error Handling Conventions

- For CLI code, print actionable messages and return a non-zero status rather than raising uncaught exceptions.
- For invalid user data, prefer collecting issues in `ValidationResult.errors` and `ValidationResult.warnings`.
- Warnings are allowed without failing when that matches existing validator behavior.
- Raise specific exceptions for true invariant failures or missing resources.
- Existing examples include `FileNotFoundError` for missing inputs and `ValueError` for duplicate IDs.
- Avoid bare `except` blocks.
- Keep error text specific enough for tests to assert on substrings.

## File I/O and Serialization

- Open text files with `encoding="utf-8"`.
- Preserve Unicode content; the repository intentionally contains Chinese and English text.
- YAML writes in `scripts/data_io.py` use `yaml.safe_dump(..., allow_unicode=True, default_flow_style=False, sort_keys=False)`.
- Preserve stable field ordering when editing serialized structures.
- Do not rewrite files just to normalize quoting or line wrapping if semantics are unchanged.

## Testing Conventions

- Use pytest.
- Shared fixtures live in `tests/conftest.py`.
- Prefer focused tests for the exact behavior changed.
- Use `tmp_path` for filesystem outputs.
- Use `monkeypatch` for CLI isolation and dependency stubbing.
- Hypothesis is already used for validator/property tests; extend existing strategies instead of inventing a second style.
- When debugging, start with a single test node or `-k` filter before running the whole suite.

## Data and YAML Conventions

- Top-level category file key is `categories:`.
- Top-level algorithm file key is `algorithms:`.
- Algorithm IDs must be lowercase, hyphenated, and unique across the entire repository.
- Required algorithm fields are `id`, `name`, `description`, `purpose`, `time_complexity`, and `category`.
- Supported optional algorithm fields are `space_complexity`, `year`, `paper_url`, `implementation_url`, `related_tools`, `tags`, `subcategory`, `difficulty`, `language`, and `references`.
- Description length must remain within 50-500 characters after trimming.
- `subcategory` must belong to the selected parent `category`.
- `difficulty` must be one of `beginner`, `intermediate`, or `advanced`.
- `references[*].type` should be one of `tutorial`, `blog`, `video`, `book`, `documentation`, or `slides`.
- Preserve field ordering from `templates/algorithm_template.yaml` and `AlgorithmEntry.to_dict()` when possible.
- Keep bilingual or Chinese-language content intact unless the task explicitly changes wording.

## Generated Outputs

- `README.md` is generated content.
- `mkdocs/docs/` contains generated documentation pages.
- Do not hand-edit generated outputs unless the task is specifically about the generated artifact and the source generator is also updated when needed.
- When generator inputs change, regenerate outputs before considering the work complete.
