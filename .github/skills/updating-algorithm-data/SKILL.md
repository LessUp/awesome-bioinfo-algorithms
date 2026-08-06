---
name: updating-algorithm-data
description: Use when editing data/algorithms/*.yaml, data/categories.yaml, or algorithm templates in this repository
---

# Updating Algorithm Data

## Overview

Use local CLI commands for repository data changes. Do not use MCP for this work: the source of truth is in-repo YAML plus the generated README.

## Checklist

1. Edit only source files in `data/` or `templates/`. Do **not** hand-edit `README.md`.
2. Run:
   ```bash
   python -m awesome_bioinfo validate
   python -m awesome_bioinfo generate && git diff --exit-code -- README.md
   ```
3. If `data/categories.yaml` changed, confirm all affected algorithm entries still validate under the updated taxonomy.

## Common Mistakes

- Editing `README.md` by hand
- Skipping regeneration after template or taxonomy changes
