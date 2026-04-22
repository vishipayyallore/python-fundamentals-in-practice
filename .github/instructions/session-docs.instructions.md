---
applyTo: docs/sessions/**/*.md
---

# Session Documentation Instructions

These rules apply to every `.md` file under `docs/sessions/`.

## Required sections (in order)

1. **Session Overview** — duration (30 min), type, level, session number
2. **Learning Objectives** — measurable, specific ("Students will be able to…")
3. **Prerequisites** — link to prior sessions if applicable
4. **Content Sections** — progressive: simple → complex
5. **Practice Files** — explicit links to `src/L{level}/S{session}/` files
6. **Key Takeaways** — 3–5 bullet summary
7. **Troubleshooting** — common errors and fixes (include for S3 onwards)

YAML front-matter is **optional**; clear headings take priority over metadata.

## File naming

- Format: `{nn}_S{session}.md` — e.g. `03_S3.md`, `_Plan.md`
- Stored at: `docs/sessions/L{level}/` — never `docs/sessions/` root
- Numeric prefix `{nn}` must match session number two-digit padded

## Links and references

- All links to practice files must use `src/L{level}/S{session}/{nn}_name.py` format.
- Verify every linked file **exists** before committing.
- Image refs: `../../images/S{session}/filename.png` (relative from session doc).

## Content standards

- **Zero-Copy**: no verbatim text from books, tutorials, or other third-party sources.
- **Split, never trim**: if a session exceeds ~150 lines, split into `Part A` / `Part B` files; do not delete content.
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
