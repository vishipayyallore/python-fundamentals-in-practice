---
applyTo: docs/sessions/**/*.md
---

# Session Documentation Instructions

These rules apply to every `.md` file under `docs/sessions/`.

## Required content coverage

Session docs must include all of the following content, but heading names and exact order can be adapted to the authored teaching style:

1. **Session context** — duration (30 min), type, level, session number
2. **Learning objectives/outcomes** — measurable, specific ("Students will be able to…")
3. **Prerequisites/builds-on** — link to prior sessions when applicable
4. **Core teaching content** — progressive: simple → complex
5. **Practice file mapping** — explicit references to `src/L{level}/S{session}/` files (or `src/L{level}/MP{number}/` for mini projects)
6. **Wrap-up summary** — key takeaways / progress check / "what you can do now"
7. **Troubleshooting guidance** — common errors and fixes (required from S3 onwards; encouraged earlier)

Examples of acceptable heading variants:

- "Session mission", "Outcome", or "Before you begin" for session context
- "Learning objectives", "What you will learn", or "Outcomes" for objectives
- "Prerequisites", "Builds on", or "Before you begin" for prerequisites/builds-on
- "Concepts", "Core content", or "Parts 1..N" for core teaching content
- "Practice files", "Hands-on practice", or "Practice file structure" for file mapping
- "Key takeaways", "What you can do now", or "Progress check" for wrap-up summary
- "Troubleshooting", "Common mistakes", or "Common errors" for troubleshooting guidance

YAML front-matter is **optional**; clear content coverage and pedagogical flow take priority over rigid heading templates.

## File naming

- Regular session format: `S{session}.md` — e.g. `S3.md`
- Mini project format: `S{session}_MP{number}.md` — e.g. `S5_MP1.md`
- Level plan file: `_Plan.md`
- Mini-project numbering follows curriculum sequence within the level (for example `S5_MP1.md`, `S10_MP2.md`).
- Stored at: `docs/sessions/L{level}/` — never `docs/sessions/` root
- Session number in the filename must match curriculum sequence

## Links and references

- Session links to practice files must use `src/L{level}/S{session}/{nn}_name.py` format.
- Mini-project links to practice files must use `src/L{level}/MP{number}/{nn}_name.py` format.
- Verify every linked file **exists** before committing.
- Image refs: `../../images/S{session}/filename.png` (relative from session doc).

## Content standards

- **Zero-Copy**: no verbatim text from books, tutorials, or other third-party sources.
- **Split, never trim**: avoid hard line caps; split into `Part A` / `Part B` when content becomes hard to navigate in one file, and do not delete educational content.
- **Reasoning visible**: code design decisions must explain the *why*, not just state the *what*.
- **Mermaid-first diagrams**: use Mermaid for conceptual diagrams; add ASCII fallback.

## Linting

CI runs `npx markdownlint-cli2 "docs/**/*.md"`. Run locally before committing:

```bash
npx --yes markdownlint-cli2 "docs/**/*.md"
```

Fix all errors before opening a PR.

## Learning order guard

Session numbering must respect logical dependencies:

> Variables (S2) → Operators (S3) → Conditionals (S4) → Loops (S5) → Lists (S7) → Dictionaries (S8)

A session must not reference concepts from a higher-numbered session as a **prerequisite**.
