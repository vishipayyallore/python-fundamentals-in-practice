# SMART Prompt Framework - Python Fundamentals

Short guide for effective prompts in this repository.

## Roles

| Role | Focus |
| --- | --- |
| **Session Author** | `docs/sessions/L{level}/`, objectives, examples, exercises |
| **Practice Code Author** | `src/L{level}/S{session}/`, beginner Python scripts, Ruff |
| **Docs Verifier** | links, file references, Markdown standards, Lychee |
| **Governance Maintainer** | `.cursor`, `.github`, `.clinerules`, `.opencode`, `AGENTS.md` |

## SMART pattern

- **Specific:** Level/session and path, such as `docs/sessions/L1/S6.md` or `src/L1/S6/`.
- **Measurable:** e.g. "practice file runs with `python -m compileall -q src` and is linked from the session doc".
- **Achievable:** One capability per change when possible
- **Relevant:** Aligns with the Level 1 plan and repository structure document.
- **Time-bound:** Scoped to current session unless explicitly future work.

## Example prompts

### Session Doc

> Review `docs/sessions/L1/S6.md` against `.github/instructions/session-docs.instructions.md`; report missing practice mappings, troubleshooting gaps, and any concepts introduced too early.

### Practice Code

> Update `src/L1/S6/04_calculator_loop.py` so the loop behavior matches the session doc, then run `ruff check src` and `python -m compileall -q src`.

### Docs

> Verify all links from `README.md`, `skills.md`, `.clinerules/**/*.md`, and `.opencode/**/*.md` point to existing files or clearly external URLs.

## Avoid

- Week-bundle, notebook, frontend, FastAPI, MCP, or demo-app phrasing from other repos
- Legacy `src/S1/` paths
- Adding new Level 1 content to completed meetup sessions without explicit approval
