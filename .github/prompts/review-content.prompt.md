---
mode: agent
description: Audit session documentation and practice code for quality, correctness, and policy compliance.
---

# Review Content

You are auditing educational content in **Python Fundamentals in Practice**.

## Required inputs (ask if not provided)

- **Scope** — level (`L1`), session (`L1/S3`), or `all`

## Workflow: OBSERVE → ANALYZE → REASON → VERIFY → ACT

### OBSERVE

1. List **every** file in scope — no sampling.
   - Session docs: `docs/sessions/L{level}/`
   - Practice files (sessions): `src/L{level}/S{session}/`
   - Practice files (mini projects): `src/L{level}/MP{number}/`

### ANALYZE

For **each** file individually:

#### Session documentation checklist

- [ ] Session Overview present (duration, level, session number)
- [ ] Learning Objectives are measurable
- [ ] Prerequisites listed
- [ ] Practice files referenced with correct session/mini-project paths (`src/L{level}/S{session}/...` or `src/L{level}/MP{number}/...`)
- [ ] Key Takeaways section present
- [ ] All links resolve to existing files
- [ ] File name format: `{nn}_S{session}.md` or `{nn}_MP{number}.md`

#### Practice file checklist

- [ ] Header comment includes filename + session reference
- [ ] Code runs without syntax errors
- [ ] Beginner-friendly comments explain the "why"
- [ ] File name format: ordered files use `{nn}_{name}.py` (non-numbered support scripts are allowed when intentional)
- [ ] No TODOs or placeholder code

#### Cross-cutting checklist

- [ ] Directory structure: `L{level}/S{session}/` or `L{level}/MP{number}/` as appropriate (not legacy `S{session}/`)
- [ ] Numeric prefixes (`01_`, `02_`, …) on ordered files (allow intentional non-numbered support files)
- [ ] Zero-Copy: no verbatim text, no mirrored outlines
- [ ] Reasoning visible: code decisions explain WHY, not just WHAT
- [ ] Session ordering follows learning dependencies (variables before operators, etc.)

### REASON

1. Identify patterns across files — systemic issues vs. one-offs.
2. Prioritise: **critical** (broken code, broken links) → **warning** (missing sections) → **info** (style).

### VERIFY

1. Cross-check every flagged path against the actual directory tree.
2. Re-run the checklist for any file you fixed.

### ACT

1. Fix all critical issues in-place.
2. Report a summary table:

   | File | Issue | Severity | Status |
   |------|-------|----------|--------|

3. After fixes, run:
   - `npx --yes markdownlint-cli2 "docs/**/*.md"`
   - `ruff check src` (Python files)

## Hard rules

- Review **every** file — never skip or sample.
- Do not remove educational content to "save space" — **split** instead.
- Update `docs/02_RepositoryStructure.md` if any file is renamed or moved.
