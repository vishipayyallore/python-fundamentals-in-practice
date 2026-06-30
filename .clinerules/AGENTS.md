# AGENTS.md - Cline Entry

**Canonical index:** root [`AGENTS.md`](../AGENTS.md).

**Repository:** `python-fundamentals-in-practice`

Educational **Python Fundamentals** curriculum for Swamy's Tech Skills Academy. This repo is documentation plus beginner-friendly practice scripts, not a web application.

## Read First

1. `AGENTS.md` - full agent map, ReAct/CoT, zero-copy and placement guardrails
2. `docs/02_RepositoryStructure.md` - authoritative paths, names, and current inventory
3. `.cursor/rules/*.mdc` - canonical modular rules
4. `.github/copilot-instructions.md` - Copilot-aligned policy summary
5. `CLAUDE.md` and `.claude/CLAUDE.md` - short Claude-oriented pointers

## Structure

```text
docs/sessions/L1/     src/L1/S1/     src/L1/S6/
docs/images/S1/       tools/psscripts/
```

## Cline Subagents

These are Cline-facing mirrors of the repo's current assistant roles.

| Agent | Use when |
| --- | --- |
| `agent-ci-verify` | After docs, Python, or governance edits |
| `session-roadmap-review` | Reviewing session docs, plans, and practice-file parity |
| `docs-originality-review` | Checking docs for zero-copy and source-integrity risk |

## CI Workflows

| Workflow | Scope |
| --- | --- |
| `docs-quality.yml` | Markdown lint + Lychee links |
| `python-quality.yml` | Ruff, `compileall`, calculator smoke checks |

Local runners: `./tools/psscripts/docs-lint.ps1`, `./tools/psscripts/docs-links.ps1`, `ruff check src`, and `python -m compileall -q src`.

## Rules

Canonical rules live in `.cursor/rules/`. Files under `.clinerules/rules/` are compact Cline-facing summaries.

## Do Not

- Apply React, FastAPI, MCP, notebook, or demo-roadmap conventions from other repositories.
- Use legacy `src/S1/` paths.
- Add new Level 1 meetup content to completed sessions without explicit user approval.
