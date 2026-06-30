# Cline rules — agentic-engineering-in-practice

Mirrors Cursor/GitHub governance for Cline. **Canonical source:** `.cursor/rules/` and `.github/copilot-instructions.md`.

## Sync sources

| Cline path | Canonical |
|------------|-----------|
| `rules/` | `.cursor/rules/*.mdc` (same numbering, `.md` extension) |
| `skills/` | `.github/skills/*/SKILL.md` |
| `agents/` | `.github/agents/*.md` |
| `AGENTS.md` | Workspace entry for Cline |

## Bundled skills

- `agentic-engineering`
- `demo-companions`
- `ci-checks`
- `docs-verification`
- `workspace-review`
- `e2e-testing`

## Subagents

- `agent-ci-verify`
- `demo-roadmap-review`
- `docs-originality-review`

When editing governance, update canonical paths first, then resync this tree.

## CI workflows

`ci-python.yml`, `ci-frontend.yml`, `ci-documentation.yml`, `ci-skills-parity.yml`, `ci-agent-docs-guard.yml` — see `CLAUDE.md`.
