# CLAUDE.md — Python Fundamentals in Practice

**Version:** 1.1  
**Last updated:** July 2026

Use this file as the **short, Claude-oriented** project brief. The full agent map and ReAct/CoT guidance live in **`AGENTS.md`**.

---

## Project

Educational **Python fundamentals** curriculum for **live meetup delivery**: levels `L*`, sessions `S*`, session docs in `docs/sessions/`, practice code in `src/`, images under `docs/images/`, Level 1 meetup summaries in `docs/meetup/L1/`, utilities in `tools/psscripts/` (PowerShell on Windows).

**Repository role:** This repo (**`python-fundamentals-in-practice`**) is the **meetup replica**. **`python-fundamentals`** is the **single source of truth** (Swamy-only development) — author and validate there first, then sync scoped content here.

**Not in scope:** AWS, cloud platforms, Bedrock, or other non-Python course tracks. Non-Python files in ignored `source-material/` are not migrated here.

---

## Authoritative structure

- **`docs/02_RepositoryStructure.md`** — authoritative for **this repo's** paths, naming, and inventory.
- **`python-fundamentals`** — authoritative for **curriculum content** and development workflow.

---

## Rules you must follow

1. **Zero-copy, transformative only** — See `.cursor/rules/01_educational-content-rules.mdc` (no verbatim third-party text; no mirrored outlines; original examples).
2. **Minimal diffs** for fixes unless the user requests refactors; preserve pedagogy, headings, and session flow.
3. **Correct paths** — e.g. `src/L1/S1/01_hello.py`, `docs/sessions/L1/S1.md` (not legacy `src/S1/` or session names without numeric prefix).
4. **Reasoning in teaching material** — Prefer “why” and trade-offs, not only syntax (see CoT section in the same `01_` rules file and in `AGENTS.md`).
5. **Quality before merge** (when changing Markdown under CI paths): lint and link-check as in `README.md` / `tools/psscripts/docs-lint.ps1` and `docs-links.ps1`. For `src/`, run `ruff check src` (see `pyproject.toml`).
6. **Session-bucketing safety** — Add new content to planned/new sessions by default; do not add new material to completed sessions without explicit user approval.
7. **Python-only scope** — Do not add or migrate AWS, cloud, Bedrock, or other non-Python course material. Curriculum intake and `src/Working/` promotion happen in **`python-fundamentals`** (single source of truth); sync scoped content here after validation.

---

## ReAct / CoT (one-line)

- **Create lesson content:** THINK → REASON → ACT → VERIFY (iterate if verify fails).  
- **Review or audit:** OBSERVE → ANALYZE → REASON → VERIFY → ACT.  
- Details and tables: **`AGENTS.md`**, **`.github/copilot-instructions.md`**, **`.cursor/rules/01_educational-content-rules.mdc`**.

---

## Related files

| File | Use |
| --- | --- |
| `AGENTS.md` | Full agent entry (Cursor, Copilot, Claude) |
| `.cursor/rules/README.md` | Index of `.mdc` rules |
| `.github/copilot-instructions.md` | Copilot-specific instructions (aligned with this repo) |
| `.clinerules/` | Cline-facing mirrors; canonical policy remains root/`.cursor` |
| `.opencode/` | OpenCode config and tool-facing mirrors; canonical policy remains root/`.cursor` |
| `CONTRIBUTING.md` | Human and review expectations |

If a tool also reads **`.claude/CLAUDE.md`**, that file defers to this repository root and **`AGENTS.md`**.

---

## When stuck

Read **`docs/02_RepositoryStructure.md`**, then the relevant **`.mdc`** rule, then open the files you will edit. Do not invent paths or session numbers.

For meetup content placement in Level 1, use `docs/meetup/L1/sessions.md` status table and ask permission before editing completed sessions.
