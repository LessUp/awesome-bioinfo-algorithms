---
title: Changelog
layout: default
nav_order: 6
description: "Version release history and changes"
---

# Changelog
{: .no_toc }

This document records all notable changes to the Awesome Bioinformatics Algorithms project. It follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
{: .fs-6 .fw-300 }

<details open markdown="block">
  <summary>Table of Contents</summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

---

## Current Version

### v1.0.2 — 2026-04-16

**Changes:**

- Fixed Python 3.9 compatibility by replacing union type syntax with `Optional[X]`
- Fixed search inconsistency by adding `purpose` field to search logic
- Consolidated duplicated `difficulty_labels` mapping across 4 files
- Fixed incorrect test expectations for MkDocs generation
- Fixed flaky hypothesis test with `HealthCheck.too_slow` suppression
- Fixed mypy type stub issue for PyYAML

[See detailed changelog →](../../changelog/en/2026-04-16_code-review.md)

---

## Version History

### v1.0.1 — 2026-02-13

**Changes:**

- Fixed `requirements.txt` alignment with `pyproject.toml` (replaced `black`/`flake8` with `ruff`)
- Fixed incorrect API signatures in `docs/API.md`
- Fixed incomplete category list in `docs/FAQ.md` (4→8 categories)
- Fixed `CHANGELOG.md` section order and incomplete lists
- Fixed `pyproject.toml` Development Status from Beta to Production/Stable
- Updated `.pre-commit-config.yaml` hook versions
- Added `SECURITY.md` security policy
- Added Pull Request and Bug Report templates
- Added `changelog/` directory for detailed change tracking

[See detailed changelog →](../../changelog/2026-02-13_content_enhancement.md)

### v1.0.0 — 2026-01-07

**Initial Release:**

- Algorithm registry for managing algorithm entries
- Category manager for organizing algorithms
- Validation system for data integrity
- README auto-generation from YAML data
- Property-based testing with Hypothesis
- GitHub Actions CI/CD pipeline
- Multi-Python version testing (3.9, 3.10, 3.11, 3.12)
- Code quality tools (ruff, mypy)
- Pre-commit hooks configuration
- Community templates (PR, Issues)
- Code of Conduct
- Security Policy
- API documentation
- FAQ documentation

**Initial Statistics:**

- 16 algorithm categories
- 201 algorithms
- 399 unique tags

---

## Detailed Changelogs

For detailed information about each release, see the `changelog/` directory:

| Date | File | Description |
|:-----|:-----|:------------|
| 2026-04-16 | [code-review](../../changelog/en/2026-04-16_code-review.md) | Code review and bug fixes |
| 2026-03-10 | [pages-optimization](../../changelog/2026-03-10_pages-optimization.md) | GitHub Pages optimization |
| 2026-03-10 | [workflow-deep-standardization](../../changelog/2026-03-10_workflow-deep-standardization.md) | CI/CD workflow standardization |
| 2026-02-13 | [content-enhancement](../../changelog/2026-02-13_content_enhancement.md) | Content enhancement and bug fixes |
| 2026-02-13 | [project-optimization](../../changelog/2026-02-13_project_optimization.md) | Project optimization |
| 2026-01-08 | [maintenance](../../changelog/2026-01-08-maintenance.md) | Project maintenance |

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- **MAJOR** version — Incompatible API changes
- **MINOR** version — Added functionality (backwards compatible)
- **PATCH** version — Bug fixes (backwards compatible)

---

## Upcoming

### Planned for v2.0.0

- [ ] Interactive web interface
- [ ] Algorithm comparison tools
- [ ] Enhanced search with filters
- [ ] Algorithm performance benchmarks
- [ ] RESTful API

---

See also: [Full CHANGELOG.md](../../CHANGELOG.md) | [Historical Details](../../changelog/)
