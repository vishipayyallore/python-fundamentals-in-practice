---
name: curriculum-practice-parity
description: >-
  Verify session docs reference the correct src/L1 practice files; align _Plan.md
  and meetup status with on-disk inventory in python-fundamentals-in-practice.
---

# curriculum-practice-parity (skill)

**Scope:** `python-fundamentals-in-practice` only.

## When to use

- After adding or renaming practice files under `src/L1`
- Before meetup delivery or when auditing doc ↔ code parity

## Checklist

1. Open `docs/02_RepositoryStructure.md` for expected file counts per session.
2. For each `docs/sessions/L1/S{n}.md`, every cited `src/L1/S{n}/` path exists and runs.
3. Cross-check `docs/sessions/L1/_Plan.md` three-axis status vs `docs/meetup/L1/sessions.md`.
4. Flag orphan files under `src/L1` not referenced in session docs.
5. New Level 1 content respects completed vs planned status in `docs/meetup/L1/sessions.md`.

## Session bundle

| Layer | Path | Contains |
| --- | --- | --- |
| Docs | `docs/sessions/L1/S{session}.md` | Teaching narrative, objectives, practice mapping |
| Practice | `src/L1/S{session}/` | Runnable Python scripts |
| Images | `docs/images/S{session}/` | Diagrams/screenshots when used |
| Status | `docs/meetup/L1/sessions.md` | Placement guard for completed vs planned work |

## References

- Structure: `docs/02_RepositoryStructure.md`
- Subagent: `.opencode/agents/session-roadmap-review.md`
