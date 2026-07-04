# Cline Core Context

**Repository:** `python-fundamentals-in-practice` (**meetup replica**)

**Curriculum source of truth:** `python-fundamentals` (Swamy-only development repo)

## Purpose

Beginner-focused **Python fundamentals** curriculum with session documentation, runnable practice scripts, and governance files for multiple coding assistants. Sync curriculum content from the dev repo; do not author new curriculum here first.

**Python-only boundary:** this repo is not for AWS, cloud, Bedrock, or other non-Python courses. Meetup content here is `docs/meetup/L1/` only. Ignore or skip non-Python files in `source-material/`.

| Area | Canonical path | Notes |
| --- | --- | --- |
| Structure | `docs/02_RepositoryStructure.md` | This repo's paths and inventory (not curriculum source of truth) |
| Session docs | `docs/sessions/L1/` | Level 1 sessions and plan |
| Practice code | `src/L1/S*/` | Python 3.13+ beginner scripts |
| Meetup status | `docs/meetup/L1/sessions.md` | Guard for completed vs planned content placement |
| Tooling | `tools/psscripts/` | Docs lint/link helper scripts |

## Governance Map

- Root `AGENTS.md`: full policy and agent entry.
- Root `CLAUDE.md` and `.claude/CLAUDE.md`: Claude-oriented brief and pointer.
- `.cursor/rules/*.mdc`: canonical modular rules.
- `.github/copilot-instructions.md`: Copilot alignment.
- `skills.md`: skill and assistant-layer index.
- `.clinerules/` and `.opencode/`: tool-specific mirrors and workflow notes.

## Quality Commands

```powershell
./tools/psscripts/docs-lint.ps1
./tools/psscripts/docs-links.ps1
ruff check src
python -m compileall -q src
```
