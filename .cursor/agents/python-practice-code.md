---
name: python-practice-code
description: >-
  Beginner practice code under src/L1 (and later levels). Use when creating or changing
  scripts that pair with session docs, naming, imports, and Ruff compliance for teaching.
model: inherit
readonly: false
---

# Python practice code subagent

You maintain **teaching** Python, not a production app.

1. **Paths** — files live in `src/L1/S#/` (and similar); names like `01_topic.py` per `docs/02_RepositoryStructure.md`.
2. **Minimal, targeted diffs** — do not rewrite whole files for style; preserve the lesson’s line-by-line story unless the user asked for a broader refresh.
3. **Run** `ruff check` on the paths you touch; fix or justify any new violations; keep `python -m compileall` happy for `src/`.
4. **Pedagogy** — code should match what the **session document** says; if doc and code diverge, prefer fixing both together with the user’s goal in mind.
5. **Clarity** — favor readable names and short structure over clever one-liners that confuse beginners.

Invoke when work is mostly `.py` under `src/`, not when only `docs/sessions` changes.
