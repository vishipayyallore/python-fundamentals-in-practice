# OpenCode — agentic-engineering-in-practice

OpenCode plugin config for this repository. Governance canonical sources: `.github/copilot-instructions.md`, `.cursor/rules/`, `.github/skills/`.

## Layout

```text
src/frontend/    src/backend/    src/mcp-server/
```

## Rules

`rules/` mirrors `.cursor/rules/` (01–09).

## Skills

Same bundles as `.github/skills/` — see `skills/README.md`.

## Agents

- `agent-ci-verify`
- `demo-roadmap-review`
- `docs-originality-review`
- `demo-code-audit` (OpenCode-only: frontend + backend + MCP spot check)

## CI workflows

| Workflow | Scope |
| -------- | ----- |
| `ci-python.yml` | Ruff + pytest |
| `ci-frontend.yml` | ESLint + Vite build |
| `ci-documentation.yml` | Markdown lint + links |
| `ci-skills-parity.yml` | Skills mirror parity |
| `ci-agent-docs-guard.yml` | Governance + agent mirrors |

Local runner: `skills/ci-checks/SKILL.md`.

## Package

`package.json` pins `@opencode-ai/plugin` for local OpenCode integration.
