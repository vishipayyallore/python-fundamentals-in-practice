# Cline Rules - Python Fundamentals in Practice

This folder adapts the repository's agent governance for Cline. It is a tool-facing mirror, not the canonical policy source.

**Python-only:** `python-fundamentals-in-practice` teaches Python fundamentals only — not AWS, cloud, or other non-Python tracks.

## Canonical Sources

| Cline path | Source of truth |
| --- | --- |
| `AGENTS.md` | Root `AGENTS.md` |
| `agentic-core-context.md` | Root `AGENTS.md`, `CLAUDE.md`, `skills.md` |
| `rules/` | `.cursor/rules/*.mdc` plus `docs/02_RepositoryStructure.md` |
| `skills/` | `.cursor/skills/python-fundamentals-curriculum/SKILL.md` and `skills.md` |
| `agents/` | `.cursor/agents/*.md` |
| `workflows/` | `README.md`, `.github/workflows/*.yml`, and `tools/psscripts/` |

## Bundled Skills

- `python-fundamentals-curriculum`
- `ci-checks`
- `docs-verification`
- `workspace-review`
- `session-companions`
- `practice-smoke-testing`

## Subagents

- `agent-ci-verify`
- `session-roadmap-review`
- `docs-originality-review`

## Local Checks

- Docs: `./tools/psscripts/docs-lint.ps1` and `./tools/psscripts/docs-links.ps1`
- Python: `ruff check src` and `python -m compileall -q src`

When governance changes, update canonical files first, then keep this folder aligned.
