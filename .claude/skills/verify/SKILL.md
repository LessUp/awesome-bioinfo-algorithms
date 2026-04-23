---
name: verify
description: Quick verification workflow — run lint and typecheck on the codebase
---

Run quick verification (lint + typecheck) on the codebase:

```bash
ruff check awesome_bioinfo/ tests/ && mypy awesome_bioinfo/ --ignore-missing-imports
```

This is a quick check without running the full test suite. Use for rapid iteration.
