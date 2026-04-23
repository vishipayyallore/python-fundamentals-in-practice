# CLAUDE.md — Python Fundamentals in Practice

**Version:** 1.0  
**Last updated:** April 2026

Use this file as the **short, Claude-oriented** project brief. The full agent map and ReAct/CoT guidance live in **`AGENTS.md`**.

---

## Project

Educational **Python** curriculum: levels `L*`, sessions `S*`, session docs in `docs/sessions/`, practice code in `src/`, images under `docs/images/`, utilities in `tools/psscripts/` (PowerShell on Windows).

---

## Authoritative structure

- **`docs/02_RepositoryStructure.md`** is the **single source of truth** for paths, naming, and what exists. If you change layout or naming rules, update that file, then align README, `.github/copilot-instructions.md`, and any broken references.

---

## Rules you must follow

1. **Zero-copy, transformative only** — See `.cursor/rules/01_educational-content-rules.mdc` (no verbatim third-party text; no mirrored outlines; original examples).
2. **Minimal diffs** for fixes unless the user requests refactors; preserve pedagogy, headings, and session flow.
3. **Correct paths** — e.g. `src/L1/S1/01_hello.py`, `docs/sessions/L1/01_S1.md` (not legacy `src/S1/` or session names without numeric prefix).
4. **Reasoning in teaching material** — Prefer “why” and trade-offs, not only syntax (see CoT section in the same `01_` rules file and in `AGENTS.md`).
5. **Quality before merge** (when changing Markdown under CI paths): lint and link-check as in `README.md` / `tools/psscripts/docs-lint.ps1` and `docs-links.ps1`. For `src/`, run `ruff check src` (see `pyproject.toml`).

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
| `CONTRIBUTING.md` | Human and review expectations |

If a tool also reads **`.claude/CLAUDE.md`**, that file defers to this repository root and **`AGENTS.md`**.

---

## When stuck

Read **`docs/02_RepositoryStructure.md`**, then the relevant **`.mdc`** rule, then open the files you will edit. Do not invent paths or session numbers.
