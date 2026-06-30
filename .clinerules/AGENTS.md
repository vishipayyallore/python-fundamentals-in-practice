# AGENTS.md — agentic-engineering-in-practice

**Canonical index:** root [`AGENTS.md`](../AGENTS.md) (precedence, skills, subagents, recovery).

**Repository:** `D:\GitHub\agentic-engineering-in-practice`

Hands-on **Agentic Engineering in Practice** codebase — one evolving app (React + FastAPI + OpenAI Agent SDK + MCP) through a 15-session **Swamy's Tech Skills Academy** curriculum.

## Read first

1. `README.md` — demo roadmap and stack
2. `docs/01-repository-structure.md` — folder layout
3. `.github/copilot-instructions.md` — development guidelines
4. `CLAUDE.md` — governance map

## Structure

```text
src/frontend/    src/backend/    src/mcp-server/
docs/            presentation/demo-0N/
```

## Subagents

Canonical definitions live in `.github/agents/`; `.clinerules/agents/` is a Cline-facing mirror.

| Agent | Use when |
|-------|----------|
| `agent-ci-verify` | After code or governance edits |
| `demo-roadmap-review` | Reviewing a Session 1–15 milestone |
| `docs-originality-review` | Doc rewrites under `docs/` |

## CI workflows

| Workflow | Scope |
| -------- | ----- |
| `ci-python.yml` | Ruff + pytest |
| `ci-frontend.yml` | ESLint + Vite build |
| `ci-documentation.yml` | Markdown lint + links |
| `ci-skills-parity.yml` | Skills mirror parity |
| `ci-agent-docs-guard.yml` | Governance + agent mirrors |

Local runner: `.github/skills/ci-checks/SKILL.md` (Cline mirror: `.clinerules/skills/ci-checks.md`).

## Rules

Canonical rules live in `.github/rules/`; `.clinerules/rules/` is a Cline-facing mirror.

Numbered `01`–`09` — aligned with `.cursor/rules/`.

## Do not

- Create `demo1/`, `demo2/` parallel app folders
- Apply ML week-bundle or notebook conventions from other repos
