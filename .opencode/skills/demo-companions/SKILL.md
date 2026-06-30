---
name: demo-companions
description: Legacy folder retained. Session companion checklist for Python Fundamentals in Practice - parity between session docs, practice scripts, images, README references, and meetup status.
---

# Session Companions

**Scope:** `python-fundamentals-in-practice` only.

## Session bundle

Each session should keep aligned artifacts:

| Layer | Path | Contains |
| --- | --- | --- |
| Docs | `docs/sessions/L{level}/S{session}.md` | Teaching narrative, objectives, practice mapping |
| Practice | `src/L{level}/S{session}/` | Runnable Python scripts |
| Images | `docs/images/S{session}/` | Diagrams/screenshots when used |
| Status | `docs/meetup/L1/sessions.md` | Placement guard for completed vs planned work |

## Definition of done (per session)

- [ ] Session doc has context, objectives, prerequisites, teaching content, practice mapping, wrap-up, and troubleshooting where expected.
- [ ] Practice files exist and match the session doc references.
- [ ] README and structure docs are updated only when inventory or public navigation changes.
- [ ] New Level 1 content respects `docs/meetup/L1/sessions.md`.
- [ ] Code runs with `ruff check src` and `python -m compileall -q src`.

## Parity checks

1. **Docs to practice** - listed files exist and demonstrate the described concept.
2. **Practice to docs** - scripts do not introduce unexplained concepts too early.
3. **Status to placement** - completed sessions are not silently expanded with new content.

## Cross-session rules

- Session N builds on earlier prerequisites.
- Planned future sessions must be marked clearly and not treated as implemented inventory.

## Related

- Structure: `docs/02_RepositoryStructure.md`
- Subagent: `.cursor/agents/session-content.md`
