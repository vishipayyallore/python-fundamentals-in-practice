# Quality Assurance

Canonical detail: `.cursor/rules/03_quality-assurance.mdc`, `README.md`, and `.github/workflows/`.

- Python practice: `ruff check src` and `python -m compileall -q src`.
- Runtime smoke checks: use the calculator examples documented in `README.md` when relevant.
- Docs: `./tools/psscripts/docs-lint.ps1` and `./tools/psscripts/docs-links.ps1`.
- Links and paths must match real files under `docs/02_RepositoryStructure.md`.
- This repo has no frontend, FastAPI, MCP server, or pytest suite.
