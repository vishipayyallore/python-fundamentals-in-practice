---
mode: agent
description: Create a new Python practice file in the correct src/L{level}/S{session}/ location.
---

# Create Practice File

You are adding a Python practice file to **Python Fundamentals in Practice**.

## Required inputs (ask if not provided)

- **Level and session** — e.g. `L1/S3`
- **Concept to demonstrate** — e.g. "comparison operators"
- **File number** — next available `{nn}` in the session folder

## Authoritative path

`src/L{level}/S{session}/{nn}_{descriptive_name}.py`

Example: `src/L1/S3/03_comparison_operators.py`

## File template

```python
# Filename: src/L{level}/S{session}/{nn}_{name}.py
# Session {session}: {Session Title}
# Concept: {concept being demonstrated}

# --- Why this example? ---
# <one-line rationale: what misconception or skill does this address?>

# === SECTION: {name} ===

# <working code with educational inline comments>
```

## Rules

1. **Header required** — filename + session reference on lines 1–2.
2. **Educational comments** — explain *why* each design decision was made, not just *what*.
3. **Working code only** — no syntax errors, no TODOs, no placeholder values.
4. **Beginner vocabulary** — avoid jargon not yet introduced in earlier sessions.
5. **Original examples** — no examples copied from books, tutorials, or Stack Overflow.
6. **Numeric prefix** — `{nn}_` prefix matching the next available number in the session.
7. **Path validation** — after writing, confirm `src/L{level}/S{session}/` exists; create if needed.
8. **Update session doc** — add a reference to the new file in `docs/sessions/L{level}/{nn}_S{session}.md` under the Practice Files section.

## ReAct pattern for code design

```text
THOUGHT: Why is this code structure optimal for teaching this concept?
ACTION:  Write the code with comments explaining the reasoning.
OBSERVE: Does a beginner understand the WHY, not just the WHAT?
REPEAT:  Until the example teaches clearly.
```
