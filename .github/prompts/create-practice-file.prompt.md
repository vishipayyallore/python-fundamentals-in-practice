---
mode: agent
description: Create a new Python practice file in the correct session or mini-project src location.
---

# Create Practice File

You are adding a Python practice file to **Python Fundamentals in Practice**.

## Required inputs (ask if not provided)

- **Level and target** — e.g. `L1/S3` or `L1/MP1`
- **Concept to demonstrate** — e.g. "comparison operators"
- **File number** — next available `{nn}` in the target folder (if creating an ordered practice file)

## Authoritative path

Session file path: `src/L{level}/S{session}/{nn}_{descriptive_name}.py`  
Mini-project file path: `src/L{level}/S{session}_MP{project}/{nn}_{descriptive_name}.py`

Examples: `src/L1/S3/03_comparison_operators.py`, `src/L1/S5/03_simple_calculator.py`

## File template

```python
# Filename: src/L{level}/S{session}/{nn}_{name}.py  OR  src/L{level}/S{session}_MP{project}/{nn}_{name}.py
# Session {session} or Mini Project {project}: {Title}
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
6. **Numeric prefix** — `{nn}_` prefix for ordered practice files; intentional support/helper files may be non-numbered.
7. **Path validation** — after writing, confirm the correct target folder exists (`src/L{level}/S{session}/` or `src/L{level}/S{session}_MP{project}/`); create if needed.
8. **Update doc reference** — add a reference to the new file in the matching session/mini-project document under Practice Files.

## ReAct pattern for code design

```text
THOUGHT: Why is this code structure optimal for teaching this concept?
ACTION:  Write the code with comments explaining the reasoning.
OBSERVE: Does a beginner understand the WHY, not just the WHAT?
REPEAT:  Until the example teaches clearly.
```
