# 📋 Repository Structure

> **🎯 Single Source of Truth**: This document (`docs/02_RepositoryStructure.md`) is the authoritative source for repository structure, naming, and current tracked inventory.

---

## 📁 Current Tracked Repository Inventory (Exact)

Snapshot source: `git ls-files` (current branch).

```text
python-fundamentals-in-practice/
├── .claude/
│   └── CLAUDE.md
├── .clinerules/
│   ├── agents/
│   │   ├── agent-ci-verify.md
│   │   ├── demo-roadmap-review.md
│   │   └── docs-originality-review.md
│   ├── rules/
│   │   ├── 01-repository-purpose.md
│   │   ├── 02-educational-content-rules.md
│   │   ├── 03-repository-structure.md
│   │   ├── 04-quality-assurance.md
│   │   ├── 05-markdown-standards.md
│   │   ├── 06-primary-directives.md
│   │   ├── 07-reference-docs-rules.md
│   │   ├── 08-file-naming-conventions.md
│   │   ├── 09-copilot-instructions-extract.md
│   │   └── README.md
│   ├── skills/
│   │   ├── README.md
│   │   ├── agentic-engineering.md
│   │   ├── ci-checks.md
│   │   ├── demo-companions.md
│   │   ├── docs-verification.md
│   │   ├── e2e-testing.md
│   │   └── workspace-review.md
│   ├── workflows/
│   │   ├── demo-roadmap-review.md
│   │   ├── run-ci-checks.md
│   │   └── workspace-review.md
│   ├── AGENTS.md
│   ├── README.md
│   └── agentic-core-context.md
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
├── .opencode/
│   ├── agents/
│   │   ├── agent-ci-verify.md
│   │   ├── demo-code-audit.md
│   │   ├── demo-roadmap-review.md
│   │   └── docs-originality-review.md
│   ├── prompts/
│   │   ├── smart-prompt-framework-guide.md
│   │   └── task-prompt.md
│   ├── rules/
│   │   ├── 01-repository-purpose.md
│   │   ├── 02-educational-content-rules.md
│   │   ├── 03-repository-structure.md
│   │   ├── 04-quality-assurance.md
│   │   ├── 05-markdown-standards.md
│   │   ├── 06-primary-directives.md
│   │   ├── 07-reference-docs-rules.md
│   │   ├── 08-file-naming-conventions.md
│   │   ├── 09-copilot-instructions-extract.md
│   │   └── README.md
│   ├── skills/
│   │   ├── agentic-engineering/
│   │   │   └── SKILL.md
│   │   ├── ci-checks/
│   │   │   └── SKILL.md
│   │   ├── demo-companions/
│   │   │   └── SKILL.md
│   │   ├── docs-verification/
│   │   │   └── SKILL.md
│   │   ├── e2e-testing/
│   │   │   └── SKILL.md
│   │   ├── workspace-review/
│   │   │   └── SKILL.md
│   │   └── README.md
│   ├── .gitignore
│   ├── README.md
│   ├── package-lock.json
│   └── package.json
├── docs/
│   ├── images/
│   │   └── S1/
│   │       ├── Help_V1.PNG
│   │       ├── Help_V2.PNG
│   │       └── Py_Source_ByteCode.PNG
│   ├── meetup/
│   │   └── L1/
│   │       └── sessions.md
│   ├── sessions/
│   │   └── L1/
│   │       ├── S1.md
│   │       ├── S2.md
│   │       ├── S3.md
│   │       ├── S4.md
│   │       ├── S5.md
│   │       ├── S6.md
│   │       └── _Plan.md
│   ├── 01_Python-Fundamentals-MasterPlan.md
│   └── 02_RepositoryStructure.md
├── src/
│   ├── L1/
│   │   ├── S5/
│   │   │   ├── 01_PEP8_naming_and_spacing.py
│   │   │   ├── 02_del_and_bool_arithmetic.py
│   │   │   ├── 03_simple_calculator.py
│   │   │   └── calculator_utils.py
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
│   │   ├── S4/
│   │   │   ├── 01_conditionals.py
│   │   │   ├── 02_boolean_logic.py
│   │   │   └── 03_number_guessing_game.py
│   │   └── S6/
│   │       ├── 01_for_loops.py
│   │       ├── 02_while_loops.py
│   │       ├── 03_loop_controls_fizzbuzz.py
│   │       ├── 04_calculator_loop.py
│   │       ├── 05_values_to_variables.py
│   │       ├── 06_chained_and_multi_assignment.py
│   │       ├── 07_conversion_limits.py
│   │       ├── 08_boolean_logic_precedence.py
│   │       └── 09_non_bool_values.py
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

- `docs/sessions/L1/S7.md` (planned)
- `docs/sessions/L1/S8.md` (planned)
- `docs/sessions/L1/S9.md` (planned)
- `docs/sessions/L1/S10_MP2.md` (planned)
- Level 2+ session docs and practice packs (planned)

---

## 📝 Naming Conventions

### Session documentation

- Location: `docs/sessions/L{level}/`
- Pattern: `S{session}.md` (for example `S1.md`)
- Mini projects: often `S{n}.md` for the curriculum slot (for example `S5.md` for Mini Project 1), or `S{session}_MP{number}.md` when you want an explicit suffix (for example `S10_MP2.md`)
- Level plan: `_Plan.md`

### Practice files

- Location: `src/L{level}/S{session}/`
- Default pattern: `{nn}_{descriptive_name}.py`
- Allowed special-case non-numbered filename (current tracked example): `src/L1/S1/bytecode_demo.py`
- Mini-project packs use `src/L{level}/S{session}/` alongside other session practice (for example `src/L1/S5/03_simple_calculator.py`); alternate layout `S{session}_MP{number}/` is allowed when a pack spans multiple starter files

### Tools and policy files

- PowerShell tooling: `tools/psscripts/`
- CI workflows: `.github/workflows/`
- Scoped Copilot instructions: `.github/instructions/`
- Cursor modular rules: `.cursor/rules/`
- Cline-facing mirrors: `.clinerules/`
- OpenCode plugin and mirrors: `.opencode/`

---

## 🔗 Quick Navigation

- **README**: [../README.md](../README.md)
- **Master Plan**: [01_Python-Fundamentals-MasterPlan.md](01_Python-Fundamentals-MasterPlan.md)
- **Level 1 Plan**: [sessions/L1/_Plan.md](sessions/L1/_Plan.md)
- **Session 1**: [sessions/L1/S1.md](sessions/L1/S1.md)
- **Session 2**: [sessions/L1/S2.md](sessions/L1/S2.md)
- **Session 3**: [sessions/L1/S3.md](sessions/L1/S3.md)
- **Session 4**: [sessions/L1/S4.md](sessions/L1/S4.md)
- **Mini Project 1 (doc slot S5)**: [sessions/L1/S5.md](sessions/L1/S5.md)
- **Session 6 (loops)**: [sessions/L1/S6.md](sessions/L1/S6.md)

---

## 🔄 Update Protocol

When structure changes (add/move/rename/delete files), update in this order:

1. `docs/02_RepositoryStructure.md` (this file)
2. Contributor-facing references (`README.md`, `CONTRIBUTING.md`)
3. Agent policy references (`AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, `.cursor/rules/*`)

---

**Last Updated**: April 2026
