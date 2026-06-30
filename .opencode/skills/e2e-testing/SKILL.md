---
name: e2e-testing
description: Legacy folder retained. Smoke verification for Python Fundamentals practice scripts - compileall plus selected interactive calculator input checks.
---

# Practice Smoke Testing

This repository has no web service or end-to-end browser flow. Use script-level smoke checks instead.

## Prerequisites

- Python 3.13+.
- Ruff available when linting is needed.

## Smoke steps

### 1. Compile all practice scripts

```powershell
python -m compileall -q src
```

### 2. Mini calculator

```powershell
printf "+\n10\n5\n" | python src/L1/S5/03_simple_calculator.py
```

### 3. Looping calculator

```powershell
printf "+\n10\n5\nq\n" | python src/L1/S6/04_calculator_loop.py
```

Add targeted script checks only when they match the session's introduced vocabulary and do not require unexplained setup.

## Report format

| Step | Status | Notes |
| --- | --- | --- |
| compileall | | |
| S5 calculator | | |
| S6 calculator loop | | |
