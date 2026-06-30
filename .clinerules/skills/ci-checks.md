---
name: ci-checks
description: Run CI-aligned checks for Agentic Engineering in Practice (backend Ruff/pytest, frontend lint/build when scaffolded, markdown lint, optional Lychee). Use when asked to run CI, lint, or verify code quality.
---

# CI Checks — Local Runner

Commands mirror `.github/workflows/ci-python.yml`, `.github/workflows/ci-frontend.yml`, and `.github/workflows/ci-documentation.yml`.

Run Python checks from the **repository root** (`pyproject.toml` + `uv.lock`).

## Policy

- Quality expectations: `.cursor/rules/04_quality-assurance.mdc` and `.github/copilot-instructions.md`

## Prerequisites

- **Python:** `uv` at repo root — `uv sync --all-groups`
- **Node.js:** 20.x for frontend and markdownlint
- **Link checks:** Docker + `lycheeverse/lychee` when `lychee.toml` exists

## Checks to run

Report each as PASS, FAIL, or SKIP (if not yet scaffolded).

### 1. Ruff (backend + MCP)

```powershell
uv run ruff check src/backend src/mcp-server
uv run ruff format --check src/backend src/mcp-server
```

### 2. pytest (all Python tests)

```powershell
uv run pytest -q
```

### 3. Frontend (when `src/frontend/package.json` exists)

```powershell
cd src/frontend
npm ci
npm run lint
npm run build
```

### 4. markdownlint-cli2

```powershell
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" "presentation/**/*.md" ".cursor/**/*.md" ".github/**/*.md" "CLAUDE.md"
```

### Optional — Lychee

```powershell
docker run --rm -v "${PWD}:/workspace" -w /workspace lycheeverse/lychee:latest --config lychee.toml --cache --max-cache-age 1d '**/*.md'
```

## Summary format

| # | Check | Status | Notes |
|---|--------|--------|-------|
| 1 | ruff | | |
| 2 | pytest | | |
| 3 | frontend lint/build | | |
| 4 | markdownlint | | |
