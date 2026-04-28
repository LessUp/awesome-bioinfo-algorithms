---
name: updating-algorithm-data
description: Use when editing data/algorithms/*.yaml, data/categories.yaml, or algorithm templates in this repository
---

# Updating Algorithm Data

## Overview

Use local CLI commands for repository data changes. Do not use MCP for this work: the source of truth is in-repo YAML plus generated outputs.

## Checklist

1. If the change adds/removes a top-level category, changes validation rules, or affects multiple specs, run `/opsx:propose` first.
2. Edit only source files in `data/` or `templates/`. Do **not** hand-edit `README.md` or `mkdocs/docs/`.
3. Treat `README.zh-CN.md` as hand-maintained. Never include it in generated-output diff checks.
4. Run:
   ```bash
   python -m awesome_bioinfo validate
   python -m awesome_bioinfo generate && python -m awesome_bioinfo mkdocs
   git diff --exit-code -- README.md mkdocs/docs/
   ```
5. If `data/categories.yaml` changed, confirm all affected algorithm entries still validate under the updated taxonomy.
6. Use `/review` only when the change also touches Python code or living specs.

## Common Mistakes

- Adding a category directly without `/opsx:propose`
- Treating `README.zh-CN.md` as generated
- Editing `README.md` or `mkdocs/docs/` by hand
- Skipping regeneration after template or taxonomy changes
