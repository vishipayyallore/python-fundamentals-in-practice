# OpenCode - Python Fundamentals in Practice

OpenCode plugin config for this repository. Canonical governance sources are root `AGENTS.md`, `docs/02_RepositoryStructure.md`, `.cursor/rules/`, and `.github/copilot-instructions.md`.

**Python-only:** this repo is the **Python Fundamentals in Practice** curriculum — not AWS, cloud, Bedrock, or other non-Python tracks.

## Layout

```text
docs/sessions/L1/     src/L1/S*/     tools/psscripts/
```

## Rules

`rules/` contains OpenCode-facing summaries. Canonical rules remain `.cursor/rules/*.mdc`.

## Skills

See `skills/README.md`. This repo's canonical project skill is `.cursor/skills/python-fundamentals-curriculum/SKILL.md`.

## Agents

- `agent-ci-verify`
- `session-roadmap-review` (Level 1 session parity and meetup alignment; current focus S1–S6)
- `docs-originality-review`
- `demo-roadmap-review` (deprecated alias — use `session-roadmap-review`)

## CI Workflows

| Workflow | Scope |
| --- | --- |
| `python-quality.yml` | Ruff, `compileall`, calculator smoke checks |
| `docs-quality.yml` | Markdown lint + Lychee links |

Local runner: `skills/ci-checks/SKILL.md`.

## Package

`package.json` pins `@opencode-ai/plugin` for local OpenCode integration. `node_modules/` remains ignored by `.opencode/.gitignore`.
