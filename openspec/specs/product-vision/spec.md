# Product Vision Specification

## Purpose

Define the product vision and high-level requirements for the Awesome Bioinformatics Algorithms project, ensuring comprehensive algorithm coverage, bilingual documentation, and automated tooling for the bioinformatics community.

`openspec/specs/` is the single source of truth for all product and technical requirements. The MkDocs site (`mkdocs/`) is the sole public documentation surface. Legacy `docs/` (Jekyll-based) has been removed and is not maintained.

## Requirements

### Requirement: Comprehensive Algorithm Coverage

The project SHALL maintain a comprehensive collection of bioinformatics algorithms.

#### Scenario: Algorithm collection size
- **GIVEN** the project data directory
- **WHEN** algorithms are counted
- **THEN** there SHALL be at least 100 algorithm entries
- **AND** algorithms SHALL be organized across 16 major categories

#### Scenario: Category coverage
- **GIVEN** the category taxonomy
- **WHEN** categories are listed
- **THEN** all major bioinformatics domains SHALL be represented
- **AND** categories SHALL include sequence-alignment, assembly, variant-calling, expression-analysis, protein-structure, phylogenetics, and others

### Requirement: Bilingual Documentation Support

The project SHALL support both English and Chinese audiences in appropriate forms.

#### Scenario: English primary README
- **GIVEN** the algorithm data
- **WHEN** `python -m awesome_bioinfo generate` is run
- **THEN** `README.md` (English) SHALL be generated as the primary project README

#### Scenario: Chinese portal README
- **GIVEN** the repository root
- **WHEN** a Chinese-language visitor reads `README.zh-CN.md`
- **THEN** they SHALL find a lightweight Chinese-language portal linking to the primary docs
- **AND** `README.zh-CN.md` is maintained manually as a portal, NOT auto-generated

#### Scenario: MkDocs documentation
- **GIVEN** the MkDocs generator
- **WHEN** documentation site is generated
- **THEN** site pages SHALL contain bilingual content where available (Chinese primary, English secondary fields)

### Requirement: Structured Machine-Readable Data

The project SHALL use YAML as the primary data format.

#### Scenario: YAML data structure
- **GIVEN** an algorithm entry
- **WHEN** the data is stored
- **THEN** it SHALL be in YAML format
- **AND** the schema SHALL be defined in JSON Schema
- **AND** validation SHALL be automated

### Requirement: Automated Validation and Generation

The project SHALL provide CLI tools for data management.

#### Scenario: Validation command
- **GIVEN** the CLI tool
- **WHEN** `python -m awesome_bioinfo validate` is executed
- **THEN** all YAML data SHALL be validated against the schema
- **AND** errors and warnings SHALL be reported with clear messages

#### Scenario: Documentation generation
- **GIVEN** valid algorithm data
- **WHEN** `python -m awesome_bioinfo generate` is executed
- **THEN** README.md SHALL be generated from templates
- **AND** generation SHALL be deterministic for CI diff checks

### Requirement: OpenSpec-Driven Development

The project SHALL use OpenSpec for all feature and architectural changes.

#### Scenario: Requirements source of truth
- **GIVEN** any proposed change to the project
- **WHEN** the change affects behavior, data schema, or documentation
- **THEN** a change proposal SHALL be created in `openspec/changes/`
- **AND** the relevant living spec in `openspec/specs/` SHALL be updated

#### Scenario: Anti-drift enforcement
- **GIVEN** the living specs and the implementation
- **WHEN** CI runs
- **THEN** generated outputs (README.md, mkdocs/docs/) SHALL match the re-generated outputs exactly
- **AND** `git diff --exit-code -- README.md mkdocs/docs/` SHALL pass

### Requirement: Open Source and Community-Driven

The project SHALL be open source with permissive licensing.

#### Scenario: License
- **GIVEN** the project repository
- **WHEN** the license is checked
- **THEN** it SHALL be CC0 1.0 (Public Domain dedication)
- **AND** contributions SHALL be welcomed

#### Scenario: Contribution guidelines
- **GIVEN** a new contributor
- **WHEN** they read CONTRIBUTING.md
- **THEN** clear instructions SHALL be provided for adding algorithms
- **AND** YAML templates SHALL be available

### Requirement: Quality Assurance

The project SHALL maintain high code and data quality.

#### Scenario: Test coverage
- **GIVEN** the test suite
- **WHEN** coverage is measured
- **THEN** code coverage SHALL exceed 85%
- **AND** all Python versions 3.9-3.12 SHALL be supported

#### Scenario: CI pipeline
- **GIVEN** a pull request
- **WHEN** CI runs
- **THEN** tests SHALL pass on all supported Python versions
- **AND** linting and type checking SHALL pass

## Target Users

### Primary Users
1. **Bioinformatics Researchers** - Need quick reference to algorithm complexity and use cases
2. **Students** - Learning bioinformatics algorithms and practical applications
3. **Software Engineers** - Implementing bioinformatics tools and pipelines

### Secondary Users
1. **Data Scientists** - Applying bioinformatics algorithms to other domains
2. **Educators** - Teaching bioinformatics courses
3. **Practitioners** - Choosing appropriate algorithms for specific analysis tasks

## Success Metrics

| Metric | Target |
|--------|--------|
| Algorithm Entries | 100+ (growing toward 200+) |
| Categories | 16 |
| Test Coverage | >85% |
| CI Pass Rate | 100% |
| Spec-Implementation Drift | 0 (enforced by CI diff checks) |

## Out of Scope

These features are explicitly NOT planned:
- Web application or GUI interface
- Algorithm implementations (only references)
- Execution benchmarking (only complexity analysis)
- Real-time data updates (static YAML files)
- Jekyll / legacy `docs/` site (removed)
