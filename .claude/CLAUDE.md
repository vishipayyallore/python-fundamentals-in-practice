# .claude — instruction pointer

**Last updated:** July 2026

Some Claude Code or Anthropic workflows look for project context under **`.claude/`**. This repository keeps **canonical instructions at the repository root** so all tools share one source of truth.

**Read in this order:**

1. **`/CLAUDE.md`** (repo root) — short Claude-specific brief and guardrails  
2. **`/AGENTS.md`** (repo root) — full agent map, ReAct/CoT, and policy table  
3. **`/skills.md`** — pointer to skills/rules: this repo includes one project skill pack at `/.cursor/skills/python-fundamentals-curriculum/SKILL.md`; rules + `AGENTS.md` are canonical  
4. **`/docs/02_RepositoryStructure.md`** — this repo's folder layout and naming (not curriculum source of truth)
5. **`python-fundamentals`** — **single source of truth** for curriculum development (Swamy-only dev repo)
6. **`/.cursor/rules/README.md`** — index of Cursor `.mdc` rules (educational content, QA, markdown, etc.)
7. **`/.github/copilot-instructions.md`** — GitHub Copilot alignment (same project policies)
8. **`/.clinerules/`** and **`/.opencode/`** — tool-specific mirrors; do not treat them as canonical over root/`.cursor` files

Do not duplicate long policy here; change root **`CLAUDE.md`** or **`AGENTS.md`** and update **`docs/02_RepositoryStructure.md`** if you document new top-level files.

## Two-repository model

- **`python-fundamentals`** = single source of truth (Swamy-only development).
- **`python-fundamentals-in-practice`** (this repo) = meetup replica — sync from the dev repo; do not author new curriculum here first.

## Python-only repository scope

This repository is **Python Fundamentals in Practice only** — session docs (`docs/sessions/`), practice scripts (`src/L{level}/`), and Level 1 meetup summaries (`docs/meetup/L1/`). Do **not** add AWS, cloud platforms, Bedrock, or other non-Python course tracks here. Non-Python files in ignored `source-material/` are **out of scope** for migration into this repo.

Placement guardrail: use `docs/meetup/L1/sessions.md` status table for Level 1 meetup updates, place new content in planned/new sessions first, and ask permission before touching completed sessions.
