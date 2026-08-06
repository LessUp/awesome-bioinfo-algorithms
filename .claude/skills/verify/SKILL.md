---
name: verify
description: Quick verification workflow - run lint on the codebase
---

Run quick lint verification on the codebase:

```bash
ruff check awesome_bioinfo/ tests/ && ruff format --check awesome_bioinfo/ tests/
```

This is a quick check without running the full test suite. Use for rapid iteration.
