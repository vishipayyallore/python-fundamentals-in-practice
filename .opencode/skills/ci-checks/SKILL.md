---
name: ci-checks
description: Run CI-aligned checks for Python Fundamentals in Practice - Ruff, compileall, calculator smoke checks, markdownlint, and Lychee. Use when asked to run CI, lint, or verify quality.
---

# CI Checks - Local Runner

Commands mirror `.github/workflows/python-quality.yml` and `.github/workflows/docs-quality.yml`.

Run all checks from the repository root.

## Policy

- Quality expectations: `.cursor/rules/03_quality-assurance.mdc`, `.github/copilot-instructions.md`, and `README.md`.

## Prerequisites

- **Python:** Python 3.13+ with Ruff installed or available on PATH.
- **Node.js:** available for `markdownlint-cli2` through `npx`.
- **Link checks:** Docker for `lycheeverse/lychee`, or skip locally and rely on CI if Docker is unavailable.

## Checks to run

Report each as PASS, FAIL, or SKIP.

### 1. Ruff

```powershell
ruff check src
```

### 2. Compileall

```powershell
python -m compileall -q src
```

### 3. Runtime smoke checks

```powershell
printf "+\n10\n5\n" | python src/L1/S5/03_simple_calculator.py
printf "+\n10\n5\nq\n" | python src/L1/S6/04_calculator_loop.py
```

### 4. markdownlint-cli2

```powershell
./tools/psscripts/docs-lint.ps1
```

### 5. Lychee

```powershell
./tools/psscripts/docs-links.ps1
```

## Summary format

| # | Check | Status | Notes |
| --- | -------- | -------- | ------- |
| 1 | ruff | | |
| 2 | compileall | | |
| 3 | calculator smoke | | |
| 4 | markdownlint | | |
| 5 | Lychee | | |
