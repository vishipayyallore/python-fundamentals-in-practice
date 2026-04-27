---
mode: agent
description: Find and fix broken file paths, links, and cross-references across the repository.
---

# Fix References

You are correcting broken paths and links in **Python Fundamentals in Practice**.

## Scope (ask if not provided)

- Specific file, level, or `all`

## Authoritative source of truth

`docs/02_RepositoryStructure.md` — check actual tree here before changing any reference.

## Common error patterns and corrections

| Wrong (legacy) | Correct |
| --- | --- |
| `src/S1/01_hello.py` | `src/L1/S1/01_hello.py` |
| `docs/sessions/S1.md` | `docs/sessions/L1/S1.md` |
| `docs/sessions/L1/S2.md` | `docs/sessions/L1/S2.md` |
| `[Session 1](docs/sessions/S1.md)` | `[Session 1](docs/sessions/L1/S1.md)` |

## Workflow

1. **SCAN** — find every file reference in the target scope:
   - Markdown links `[text](path)` and image refs `![alt](path)`
   - Python `import` / `open()` statements (if cross-file)
   - Code comments that cite filenames
2. **VERIFY** — for each reference, check the path resolves against the actual tree.
3. **FIX** — apply the smallest targeted edit: change only the broken segment.
4. **CROSS-CHECK** — if a file was renamed, find all other files that reference the old name.
5. **VALIDATE** — after fixes run:
   - `npx --yes markdownlint-cli2 "docs/**/*.md"`
   - Lychee link checker (see `lychee.toml`)

## Path rules (non-negotiable)

- All Python practice files live under `src/L{level}/S{session}/`
- All session docs live under `docs/sessions/L{level}/`
- File names include numeric prefix — `01_`, `02_`, … (never bare `S1.md`)
- Directory names use `L{number}` and `S{number}` (no hyphens, no spaces)

## After fixing

Update `docs/02_RepositoryStructure.md` if any file was renamed or moved (not just referenced incorrectly).
