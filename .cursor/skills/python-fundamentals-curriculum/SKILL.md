---
name: python-fundamentals-curriculum
description: >-
  Educational Python curriculum (levels L*, sessions in docs/sessions/, code in src/). Use
  when editing learning materials, session write-ups, practice files under src/L1, or
  structure/navigation that affects the course. Points to project rules; does not replace them.
---

# Python Fundamentals in Practice — workflow

**Python-only repository:** session docs, `src/L{level}/` practice scripts, and `docs/meetup/L1/` meetup summaries. Do not add or migrate AWS, cloud, Bedrock, or other non-Python course material.

## When to use

- `docs/sessions/`, `docs/images/`, `docs/0*_*.md`, or curriculum text in the repo root
- `src/L1/**` (and future levels) practice scripts
- `README`, `AGENTS.md`, or `docs/02_RepositoryStructure.md` when the change is **about the course** (not a one-line typo you can fix inline)

## Before you edit: read the source of truth

1. **`AGENTS.md`** (root) — policies, ReAct/CoT, two-repository model, where rules and CI live
2. **`python-fundamentals`** (dev repo) — **single source of truth** for curriculum content; sync from there unless Swamy explicitly edits here
3. **`docs/02_RepositoryStructure.md`** — authoritative for **this repo's** paths, naming, and inventory
4. Relevant **`.cursor/rules/*.mdc`** (especially `01_educational-content-rules` for teaching content, `04_markdown-standards` for docs, `03_quality-assurance` for `src/`)
5. **`CLAUDE.md`** for a short Claude-oriented brief if needed

## Non-negotiables

- **Two-repository model** — author curriculum in **`python-fundamentals`** (single source of truth); this repo is the **meetup replica** — sync scoped content; do not invent curriculum here first
- **Zero-copy, transformative only** — no long verbatim third-party text; own examples; brief quotes with attribution. See `01_educational-content-rules.mdc`.
- **Do not “compress away” teaching** — split or continue in the next part instead of cutting pedagogy
- **Paths and numbering** — match `L{level}/S{session}/` in `src/` and numbered session files under `docs/sessions/`
- **Python-only scope** — do not add AWS, cloud, or other non-Python tracks; skip non-Python `source-material/` intake

## Quality (when a significant doc or code change is done)

- Docs (paths under CI): `tools/psscripts/docs-lint.ps1` and `docs-links.ps1`, or the `npx`/Docker flow in `README.md`
- Python: `ruff check src` and `python -m compileall -q src` (see `pyproject.toml` and `python-quality.yml`)

## If unsure

Re-read the structure doc, then the relevant rule file, then the files you will change.
