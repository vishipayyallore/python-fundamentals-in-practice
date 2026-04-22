---
applyTo: src/**/*.py
---

# Python Practice File Instructions

These rules apply to every `.py` file under `src/`.

## Mandatory header

Every file must open with exactly these two comment lines:

```python
# Filename: src/L{level}/S{session}/{nn}_{name}.py
# Session {session}: {Session Title}
```

## Code quality

- All code must **run without syntax errors** — no TODOs, no placeholder values.
- Use **beginner-level vocabulary**: avoid any Python feature not yet introduced in previous sessions for this level.
- Include **inline comments** that explain the *why* behind code decisions, not just the *what*.
- Keep examples **minimal**: demonstrate one concept clearly rather than many concepts loosely.

## File naming

- Numeric prefix required: `01_`, `02_`, … matching position within the session.
- Descriptive suffix in snake_case: `01_hello.py`, `03_comparison_operators.py`.
- Location: `src/L{level}/S{session}/` — never `src/S{session}/` (legacy).

## Linting

CI runs `ruff check src` and `python -m compileall src`. Match that locally with:

```bash
ruff check src
python -m compileall src
```

Do not commit files that fail either check.

## Reasoning standard

Apply the ReAct pattern for each non-trivial code decision:

```text
THOUGHT: Why is this structure the right choice here?
ACTION:  Write code with a comment explaining the reasoning.
OBSERVE: Can a beginner understand the WHY, not just the WHAT?
```
