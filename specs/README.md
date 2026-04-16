# Specifications

This directory contains all specification documents for the Awesome Bioinformatics Algorithms project. Following **Spec-Driven Development (SDD)** principles, these documents serve as the single source of truth for all implementation decisions.

## Directory Structure

```
specs/
├── product/          # Product requirements and feature definitions (PRDs)
├── rfc/              # Technical design documents and architecture proposals (RFCs)
├── api/              # API specifications (CLI interface definitions)
├── db/               # Data schema definitions (YAML data structures)
└── testing/          # Test specifications and acceptance criteria
```

## How to Use Specs

### For Contributors
1. **Before implementing**: Read relevant specs in this directory
2. **Before proposing changes**: Update specs first, then get approval
3. **During implementation**: Follow specs exactly as written
4. **After implementation**: Verify against spec acceptance criteria

### For AI Agents
See `AGENTS.md` at the repository root for detailed workflow instructions.

## Spec Types

### Product Specs (`product/`)
- Define **what** features to build
- Include user stories and acceptance criteria
- Written from user perspective (not technical)

### RFC Specs (`rfc/`)
- Define **how** to implement technically
- Include architecture decisions and trade-offs
- Numbered sequentially (0001-, 0002-, etc.)

### API Specs (`api/`)
- Define CLI interface contracts
- Include command syntax, options, and output formats
- Machine-readable where possible

### Data Specs (`db/`)
- Define YAML data structure and schema
- Include validation rules and constraints
- Document category taxonomy

### Testing Specs (`testing/`)
- Define test strategies and coverage requirements
- Include BDD-style feature files
- Document property-based test invariants

## Workflow

1. **New Feature**: Create product spec → RFC → API/Data specs → Implementation → Tests
2. **Bug Fix**: Review existing specs → Update if needed → Fix → Add regression tests
3. **Refactoring**: Create RFC → Get approval → Refactor → Verify against specs

## Contributing

To contribute to specs:
1. Read existing specs first
2. Propose changes via RFC
3. Get community approval before implementation
4. Update specs and code together in same PR

See `CONTRIBUTING.md` for detailed guidelines.
