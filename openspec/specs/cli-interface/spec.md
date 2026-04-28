# CLI Interface Specification

## Purpose

Define the command-line interface contracts for the Awesome Bioinformatics Algorithms project, ensuring consistent behavior, exit codes, and output formats across all commands.

This spec is authoritative for the current implementation. Features listed here SHALL exist in `awesome_bioinfo/`. Anything not listed here is out of scope unless a new OpenSpec change explicitly adds it.

## Requirements

### Requirement: CLI Entry Point

The CLI SHALL be accessible via Python module execution.

#### Scenario: Standard invocation
- **GIVEN** the installed package
- **WHEN** a user executes `python -m awesome_bioinfo <command>`
- **THEN** the specified command SHALL be executed
- **AND** help SHALL be available via `--help` flag

> Note: There are no global `-v`/`--verbose` or `-q`/`--quiet` flags. Each command controls its own output verbosity.

### Requirement: Validate Command

The validate command SHALL validate all YAML data.

#### Scenario: Validation success
- **GIVEN** valid YAML data files
- **WHEN** `python -m awesome_bioinfo validate` is executed
- **THEN** exit code 0 SHALL be returned
- **AND** a summary of passed validations SHALL be displayed

#### Scenario: Validation failure
- **GIVEN** invalid YAML data
- **WHEN** validation is run
- **THEN** exit code 1 SHALL be returned
- **AND** specific error messages SHALL be displayed
- **AND** error messages SHALL include file and field information

#### Scenario: Validation warnings
- **GIVEN** data with missing optional fields
- **WHEN** validation is run
- **THEN** warnings SHALL be displayed
- **AND** exit code 0 SHALL be returned (warnings do not fail)

### Requirement: Stats Command

The stats command SHALL display collection statistics.

#### Scenario: Statistics output
- **GIVEN** the algorithm collection
- **WHEN** `python -m awesome_bioinfo stats` is executed
- **THEN** total algorithm count SHALL be displayed
- **AND** per-category algorithm counts SHALL be displayed
- **AND** unique tag count SHALL be displayed
- **AND** output SHALL be text-only (no `--format` flag)

### Requirement: Search Command

The search command SHALL find algorithms matching criteria.

#### Scenario: Search by name (positional or --keyword)
- **GIVEN** the algorithm collection
- **WHEN** `python -m awesome_bioinfo search <query>` is executed
- **OR** `python -m awesome_bioinfo search --keyword <query>` is executed
- **THEN** algorithms with matching names, descriptions, purposes, or tags SHALL be returned
- **AND** search SHALL be case-insensitive

> Note: Both forms are equivalent. The positional argument and `--keyword` flag resolve to the same search path.

#### Scenario: Filter by category
- **GIVEN** the search command
- **WHEN** `--category` option is provided
- **THEN** only algorithms in that category SHALL be returned

#### Scenario: Filter by tag
- **GIVEN** the search command
- **WHEN** `--tag` option is provided
- **THEN** algorithms with the specified tag SHALL be returned

#### Scenario: Filter by difficulty
- **GIVEN** the search command
- **WHEN** `--difficulty` option is provided
- **THEN** only algorithms with matching difficulty SHALL be returned

#### Scenario: No results
- **GIVEN** a search query
- **WHEN** no algorithms match
- **THEN** exit code 0 SHALL be returned
- **AND** a "no results" message SHALL be displayed

### Requirement: Info Command

The info command SHALL display detailed algorithm information as formatted text.

#### Scenario: Algorithm found by exact ID
- **GIVEN** a valid algorithm ID
- **WHEN** `python -m awesome_bioinfo info <id>` is executed
- **THEN** all algorithm fields SHALL be displayed as text
- **AND** exit code 0 SHALL be returned

#### Scenario: Fuzzy lookup on partial/approximate ID
- **GIVEN** a query that does not exactly match any ID
- **WHEN** info command is executed
- **THEN** the registry search SHALL be used as a fallback
- **AND** if exactly one match is found it SHALL be displayed (exit code 0)
- **AND** if multiple matches are found they SHALL be listed and exit code 1 SHALL be returned

#### Scenario: Algorithm not found
- **GIVEN** an ID with no exact or fuzzy match
- **WHEN** info command is executed
- **THEN** exit code 1 SHALL be returned
- **AND** an error message SHALL be displayed

> Note: Output is text-only. There is no `--format` flag for this command.

### Requirement: Compare Command

The compare command SHALL compare exactly two algorithms side by side.

#### Scenario: Successful comparison
- **GIVEN** exactly two valid algorithm IDs (or unambiguous partial names)
- **WHEN** `python -m awesome_bioinfo compare <id1> <id2>` is executed
- **THEN** a side-by-side comparison SHALL be displayed
- **AND** key differences SHALL be highlighted

#### Scenario: Fuzzy resolution for compare
- **GIVEN** an argument that does not exactly match an ID
- **WHEN** compare is executed
- **THEN** fuzzy search SHALL be used as fallback
- **AND** if exactly one match is found it SHALL be used transparently
- **AND** if zero or multiple matches are found exit code 1 SHALL be returned with an error message

#### Scenario: Algorithm not found
- **GIVEN** one or more IDs with no exact or fuzzy match
- **WHEN** compare is executed
- **THEN** exit code 1 SHALL be returned
- **AND** which algorithms were not found SHALL be indicated

> Note: Comparing more than two algorithms is not supported. The command takes exactly two positional arguments.

### Requirement: Export Command

The export command SHALL export data in JSON or CSV format.

#### Scenario: JSON export
- **GIVEN** the export command
- **WHEN** `--format json` is specified (or omitted, as `json` is default)
- **THEN** valid JSON SHALL be output to stdout
- **AND** all algorithms SHALL be included

#### Scenario: CSV export
- **GIVEN** the export command
- **WHEN** `--format csv` is specified
- **THEN** valid CSV with appropriate columns SHALL be output to stdout

#### Scenario: Output to file
- **GIVEN** the export command
- **WHEN** `--output <path>` option is provided
- **THEN** data SHALL be written to the specified file

> Note: YAML export is not supported. Supported formats are `json` and `csv` only. Category filtering via `--category` is not supported.

### Requirement: Generate Command

The generate command SHALL generate the English `README.md` from templates.

#### Scenario: README generation
- **GIVEN** valid algorithm data
- **WHEN** `python -m awesome_bioinfo generate` is executed
- **THEN** `README.md` SHALL be generated in the project root
- **AND** all algorithms SHALL be included
- **AND** table of contents SHALL be generated
- **AND** generation SHALL be deterministic (same output for same input)

#### Scenario: Custom output path
- **GIVEN** the generate command
- **WHEN** `--output <path>` is provided
- **THEN** README SHALL be written to the specified path instead

> Note: The `generate` command only generates the English README. Chinese portal `README.zh-CN.md` is maintained separately as a lightweight audience-facing document, not auto-generated from the same pipeline.

### Requirement: MkDocs Command

The mkdocs command SHALL generate documentation site source files.

#### Scenario: Site generation
- **GIVEN** valid algorithm data
- **WHEN** `python -m awesome_bioinfo mkdocs` is executed
- **THEN** MkDocs site files SHALL be generated in `mkdocs/docs/`
- **AND** category pages SHALL be created
- **AND** algorithm detail pages SHALL be created

> Note: There is no `--serve` flag. To preview the site, run `mkdocs serve -f mkdocs/mkdocs.yml` separately after generation.

### Requirement: Check-Links Command

The check-links command SHALL verify the validity of URLs in algorithm entries.

#### Scenario: Links valid
- **GIVEN** algorithm entries with URLs
- **WHEN** `python -m awesome_bioinfo check-links` is executed
- **THEN** all URLs SHALL be checked for reachability
- **AND** a summary SHALL be displayed
- **AND** exit code 0 SHALL be returned if all URLs are reachable

#### Scenario: Broken links found
- **GIVEN** algorithm entries with broken URLs
- **WHEN** check-links is executed
- **THEN** broken URLs SHALL be reported with their algorithm IDs
- **AND** exit code 1 SHALL be returned

### Requirement: Error Output Conventions

CLI commands SHOULD move toward consistent error formatting as a convergence goal.

#### Scenario: Error message format (target)
- **GIVEN** any CLI error
- **WHEN** an error occurs
- **THEN** the message SHOULD begin with `Error:` to aid scripting and readability
- **AND** a contextual hint or suggestion SHOULD accompany the error where helpful

> Note: Current implementation follows this convention in most but not all commands. New commands and future refactoring SHALL adopt this format. Tests SHOULD verify `Error:` prefix for error paths in new code, but MUST NOT assume it for all existing commands.

### Requirement: Exit Codes

All commands SHALL return appropriate exit codes.

#### Scenario: Success exit code
- **GIVEN** any CLI command
- **WHEN** execution succeeds
- **THEN** exit code 0 SHALL be returned

#### Scenario: Failure exit code
- **GIVEN** any CLI command
- **WHEN** execution fails (validation errors, not found, etc.)
- **THEN** exit code 1 SHALL be returned

#### Scenario: Invalid arguments exit code
- **GIVEN** any CLI command
- **WHEN** invalid arguments are provided
- **THEN** exit code 2 SHALL be returned
