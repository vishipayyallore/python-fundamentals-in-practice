# 📋 Repository Structure

> **🎯 Single Source of Truth**: This document (`docs/02_RepositoryStructure.md`) is the authoritative source for repository structure, naming, and current tracked inventory.

---

## 📁 Current Tracked Repository Inventory (Exact)

Snapshot source: `git ls-files` (current branch).

```text
python-fundamentals-in-practice/
├── .claude/
│   └── CLAUDE.md
├── .copilot/
│   └── settings.json
├── .cursor/
│   ├── agents/
│   │   ├── docs-verifier.md
│   │   ├── python-practice-code.md
│   │   └── session-content.md
│   ├── rules/
│   │   ├── 01_educational-content-rules.mdc
│   │   ├── 02_repository-structure.mdc
│   │   ├── 03_quality-assurance.mdc
│   │   ├── 04_markdown-standards.mdc
│   │   ├── 05_primary-directives.mdc
│   │   ├── 06_cross-level-integration.mdc
│   │   └── README.md
│   └── skills/
│       └── python-fundamentals-curriculum/
│           └── SKILL.md
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── config.yml
│   │   ├── documentation_improvement.md
│   │   └── feature_request.md
│   ├── instructions/
│   │   ├── python-practice.instructions.md
│   │   └── session-docs.instructions.md
│   ├── prompts/
│   │   ├── create-practice-file.prompt.md
│   │   ├── create-session.prompt.md
│   │   ├── fix-references.prompt.md
│   │   └── review-content.prompt.md
│   ├── workflows/
│   │   ├── docs-quality.yml
│   │   └── python-quality.yml
│   ├── copilot-instructions.md
│   └── pull_request_template.md
├── docs/
│   ├── images/
│   │   └── S1/
│   │       ├── Help_V1.PNG
│   │       ├── Help_V2.PNG
│   │       └── Py_Source_ByteCode.PNG
│   ├── meetup/
│   │   └── L1/
│   │       └── meetup-sessions.md
│   ├── sessions/
│   │   └── L1/
│   │       ├── 01_S1.md
│   │       ├── 02_S2.md
│   │       ├── 03_S3.md
│   │       ├── 04_S4.md
│   │       ├── 05_MP1.md
│   │       └── _Plan.md
│   ├── 01_Python-Fundamentals-MasterPlan.md
│   └── 02_RepositoryStructure.md
├── src/
│   ├── L1/
│   │   ├── S1/
│   │   │   ├── 01_hello.py
│   │   │   ├── 02_interactive_hello.py
│   │   │   └── bytecode_demo.py
│   │   ├── S2/
│   │   │   ├── 01_variables.py
│   │   │   ├── 02_data_types.py
│   │   │   └── 03_type_conversion.py
│   │   ├── S3/
│   │   │   ├── 01_arithmetic.py
│   │   │   ├── 02_comparisons.py
│   │   │   └── 03_mini_calculator.py
│   │   └── S4/
│   │       ├── 01_conditionals.py
│   │       ├── 02_boolean_logic.py
│   │       └── 03_number_guessing_game.py
│   └── L2/
│       └── .gitkeep
├── tools/
│   └── psscripts/
│       ├── docs-links.ps1
│       ├── docs-lint.ps1
│       ├── repo-structure.txt
│       └── show-tree.ps1
├── .gitignore
├── .markdownlint-cli2.yaml
├── .markdownlint.json
├── .markdownlintignore
├── AGENTS.md
├── CLAUDE.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── SECURITY.md
├── lychee.toml
├── pyproject.toml
└── skills.md
```

---

## 📦 Planned / Future (Not Yet Tracked as Files)

The following are roadmap items and may be referenced in planning docs, but they are not currently present as tracked files:

- `docs/sessions/L1/06_S5.md` (planned)
- `docs/sessions/L1/07_S6.md` (planned)
- `docs/sessions/L1/08_S7.md` (planned)
- `docs/sessions/L1/09_S8.md` (planned)
- `docs/sessions/L1/10_MP2.md` (planned)
- Level 2+ session docs and practice packs (planned)

---

## 📝 Naming Conventions

### Session documentation

- Location: `docs/sessions/L{level}/`
- Pattern: `{nn}_S{session}.md` (for example `01_S1.md`)
- Mini projects: `{nn}_MP{number}.md` (for example `05_MP1.md`)
- Level plan: `_Plan.md`

### Practice files

- Location: `src/L{level}/S{session}/`
- Default pattern: `{nn}_{descriptive_name}.py`
- Allowed special-case non-numbered filename (current tracked example): `src/L1/S1/bytecode_demo.py`

### Tools and policy files

- PowerShell tooling: `tools/psscripts/`
- CI workflows: `.github/workflows/`
- Scoped Copilot instructions: `.github/instructions/`
- Cursor modular rules: `.cursor/rules/`

---

## 🔗 Quick Navigation

- **README**: [../README.md](../README.md)
- **Master Plan**: [01_Python-Fundamentals-MasterPlan.md](01_Python-Fundamentals-MasterPlan.md)
- **Level 1 Plan**: [sessions/L1/_Plan.md](sessions/L1/_Plan.md)
- **Session 1**: [sessions/L1/01_S1.md](sessions/L1/01_S1.md)
- **Session 2**: [sessions/L1/02_S2.md](sessions/L1/02_S2.md)
- **Session 3**: [sessions/L1/03_S3.md](sessions/L1/03_S3.md)
- **Session 4**: [sessions/L1/04_S4.md](sessions/L1/04_S4.md)
- **Mini Project 1 (stub)**: [sessions/L1/05_MP1.md](sessions/L1/05_MP1.md)

---

## 🔄 Update Protocol

When structure changes (add/move/rename/delete files), update in this order:

1. `docs/02_RepositoryStructure.md` (this file)
2. Contributor-facing references (`README.md`, `CONTRIBUTING.md`)
3. Agent policy references (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.cursor/rules/*`)

---

**Last Updated**: April 2026
