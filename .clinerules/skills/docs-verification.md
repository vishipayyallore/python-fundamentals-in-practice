---
name: docs-verification
description: Verify markdown structure, demo documentation, folder naming, and alignment with docs/01-repository-structure.md for agentic-engineering-in-practice.
---

# Docs verification

## Canonical structure

Compare against:

- `docs/01-repository-structure.md`
- `README.md` (roadmap table and structure section)
- `.cursor/rules/03_repository-structure.mdc`

## Checklist

### Structure

- [ ] `src/frontend/`, `src/backend/`, `src/mcp-server/` documented consistently
- [ ] `presentation/demo-01` … `demo-05` folders exist or are planned with README stubs
- [ ] `docs/` topic files follow `NN-topic.md` pattern where applicable

### Roadmap alignment

- [ ] Demo status in README matches implemented features
- [ ] Git tag names in docs match `02-master-plan.md` / README
- [ ] No references to week bundles, notebooks, or ML-from-scratch layout

### Links and references

- [ ] Internal links resolve (run markdownlint / Lychee)
- [ ] Stack versions (Python 3.13, etc.) consistent across docs

### Teaching quality

- [ ] Agent concepts have plain-English explanation or worked example
- [ ] Architecture diagrams match described demo scope

## Output

Report gaps as a table: **Path | Issue | Suggested fix**
