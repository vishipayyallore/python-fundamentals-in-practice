---
name: docs-verification
description: Verify markdown structure, links, file references, originality, and alignment with docs/02_RepositoryStructure.md for Python Fundamentals in Practice.
---

# Docs Verification

## Canonical structure

Compare against:

- `docs/02_RepositoryStructure.md`
- `README.md` quick start and structure section
- `.cursor/rules/02_repository-structure.mdc`
- `.cursor/rules/04_markdown-standards.mdc`

## Checklist

### Structure

- [ ] `docs/sessions/L{level}/` and `src/L{level}/S{session}/` paths are documented consistently.
- [ ] Planned sessions are listed as planned, not implemented.
- [ ] Images referenced from session docs exist under `docs/images/S{session}/`.

### Roadmap alignment

- [ ] README quick start matches implemented sessions.
- [ ] Level plan and meetup status agree where they overlap.
- [ ] No references to frontend, FastAPI, MCP, week bundles, or notebook layouts.

### Links and references

- [ ] Internal links resolve with markdownlint and Lychee.
- [ ] Python version guidance stays consistent with `pyproject.toml`.

### Teaching quality

- [ ] Teaching content is original and beginner-friendly.
- [ ] Code examples explain why, not only what.

## Output

Report gaps as a table: **Path | Issue | Suggested fix**
