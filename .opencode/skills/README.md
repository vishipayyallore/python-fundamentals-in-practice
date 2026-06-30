# Agent skills (canonical)

This directory is the **source of truth** for bundled agent skills used with Cursor and GitHub Copilot (see `.github/copilot-instructions.md`).

## Mirror

`.cursor/skills/` must stay **identical** to `.github/skills/` (same paths, same `SKILL.md` and `README.md` bytes). After editing here, copy the updated tree to `.cursor/skills/`.

## Bundled skills

| Folder | Purpose |
|--------|---------|
| `agentic-engineering` | Domain context for this repository |
| `demo-companions` | Demo docs + presentation + code parity SOP |
| `ci-checks` | Local commands aligned with `.github/workflows/ci-*.yml` |
| `docs-verification` | Docs structure vs `docs/01-repository-structure.md` |
| `workspace-review` | Full audit checklist |
| `e2e-testing` | Smoke tests when stack is runnable |

**CI:** Pushes that touch skills run `.github/workflows/ci-skills-parity.yml`; agent docs changes also run `.github/workflows/ci-agent-docs-guard.yml`. Application CI: `ci-python.yml`, `ci-frontend.yml`, `ci-documentation.yml`.
