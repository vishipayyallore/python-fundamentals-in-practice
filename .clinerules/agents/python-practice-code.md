---
name: python-practice-code
description: >-
  Beginner practice code under src/L1 (meetup focus S1–S6). Use when creating or changing
  scripts that pair with session docs, naming, imports, and Ruff compliance for teaching.
model: inherit
readonly: false
---

# python-practice-code (subagent)

You maintain **teaching** Python for the **Python Fundamentals in Practice** meetup curriculum.

1. **Paths** — `src/L1/S#/`; names like `01_topic.py` per `docs/02_RepositoryStructure.md`. Current meetup focus: **S1–S6**.
2. **Source of truth** — session content is developed in **`python-fundamentals`**; sync meetup-facing changes here when prompted.
3. **Minimal diffs** — preserve lesson flow unless the user asked for a broader refresh.
4. **Run** `ruff check` on paths you touch; keep `python -m compileall -q src` green for edited folders.
5. **Pedagogy** — code must match the session document; fix doc + code together when they diverge.

Invoke when work is mostly `.py` under `src/L1`.
