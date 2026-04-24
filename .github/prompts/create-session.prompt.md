---
mode: agent
description: Create a new session document and matching practice files for the Python Fundamentals curriculum.
---

# Create Session

You are creating educational content for the **Python Fundamentals in Practice** curriculum.

## Required inputs (ask if not provided)

- **Level** — `L1`–`L9`
- **Session number** — `S1`–`S8` or `MP1`/`MP2`
- **Topic** — brief description of the concept to teach

## Authoritative paths

- Session doc (regular session) → `docs/sessions/L{level}/{nn}_S{session}.md` (e.g. `docs/sessions/L1/06_S5.md`)
- Session doc (mini project) → `docs/sessions/L{level}/{nn}_MP{project}.md` (e.g. `docs/sessions/L1/05_MP1.md`)
- Practice code (regular session) → `src/L{level}/S{session}/` (e.g. `src/L1/S5/`)
- Practice code (mini project) → `src/L{level}/MP{project}/` (e.g. `src/L1/MP1/`)
- Structure ref → `docs/02_RepositoryStructure.md`

## Workflow: THINK → REASON → ACT → VERIFY

### THINK

1. State the learning objective in one sentence.
2. Decompose the topic into 3–5 digestible chunks ordered simple → complex.
3. Anticipate the top two beginner misconceptions.

### REASON

1. List prerequisite sessions — verify they are numbered **before** this one.
2. List sessions this content **enables** — verify they are numbered **after** this one.
3. Sketch two original examples (no copying from books, tutorials, or prior art).

### ACT

1. Write the session document path that matches the input:
   - Regular session: `docs/sessions/L{level}/{nn}_S{session}.md`
   - Mini project: `docs/sessions/L{level}/{nn}_MP{project}.md`
   with this structure:
   - Session Overview (30 min, level, session number)
   - Learning Objectives (measurable)
   - Prerequisites
   - Content Sections (progressive)
   - Practice Files (references to `src/`)
   - Key Takeaways
   - Troubleshooting (common errors)
2. Write each practice file in the matching directory:
   - Regular session: `src/L{level}/S{session}/{nn}_{name}.py`
   - Mini project: `src/L{level}/MP{project}/{nn}_{name}.py`
   - Header comment: `# Filename: ...` + session/project reference
   - Educational comments explaining the "why" of each decision
   - Working code (no syntax errors, no TODOs)

### VERIFY

1. All code runs without errors — test mentally or with `python <file>`.
2. All file references inside the markdown resolve to **existing** files.
3. Session numbering respects the learning-dependency order in `01_educational-content-rules.mdc`.
4. Zero-Copy: no sentence or example structure borrowed from external sources.

## Hard rules

- **Never trim content** — if material becomes hard to navigate in one file, split into `Part A`, `Part B` files.
- **Numeric prefixes mandatory** — `01_`, `02_`, … on all files.
- **Path format** — `src/L1/S5/` not `src/S5/` or `src/L1/5/`.
- After creating files, update `docs/02_RepositoryStructure.md` if the tree changes.
