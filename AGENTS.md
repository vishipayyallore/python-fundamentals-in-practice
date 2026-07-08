# Agents — Python Fundamentals in Practice

**Version:** 1.1  
**Last updated:** July 2026

This file is the **entry point for AI coding agents** (Cursor, Claude Code, GitHub Copilot, and similar tools) working in this repository. It ties together project-specific rules, documentation, and how to reason about changes safely.

---

## 1. What this repository is

- **Purpose:** Educational **Python fundamentals** curriculum only (progressive levels, ~30-minute sessions, practice code under `src/`, session write-ups under `docs/sessions/`, Level 1 meetup summaries under `docs/meetup/L1/`).
- **Tone:** Beginner-friendly, hands-on, visually clear. Content must be **transformative**, not copied from third-party materials (see Zero-Copy Policy below).
- **Non-goals:** This is not a production app repository; code teaches concepts and must remain runnable and readable. This is **not** a home for AWS, cloud, Bedrock, or other non-Python course tracks.

**Python-only scope:** All curriculum work belongs in `docs/sessions/`, `src/L{level}/`, `docs/images/`, and `docs/meetup/L1/`. Do **not** add or migrate non-Python instructor intake (e.g. AWS/cloud meetup outlines) from ignored `source-material/` into this repository unless the user explicitly requests Python-related promotion.

### Two-repository model (workspace)

| Repository | Role | Who |
| --- | --- | --- |
| **`python-fundamentals`** | **Single source of truth** — Swamy-only development; author curriculum, migrate intake, run full quality gates | **Swamy only** |
| **`python-fundamentals-in-practice`** (this repo) | **Meetup replica** — synced copy of session docs and practice code for live meetup delivery | Meetup sessions |

**Workflow:** Develop and validate in **`python-fundamentals` first** → sync scoped content into this repo (current meetup focus: **Level 1 S1–S6**) → align delivery status with the dev repo when sessions complete. Do **not** treat this repo as authoritative for new curriculum authoring.

**Meetup parity:** Keep `docs/meetup/L1/sessions.md` identical in both repos — status table, session agendas, and **event date/URL** fields. Author meetup updates in the dev repo first; if event details are captured during live delivery here, back-sync them into **`python-fundamentals`** immediately.

**Structure and inventory for this repo:** `docs/02_RepositoryStructure.md` — when this repo's layout changes, update that document first, then align README, copilot instructions, and this file.

---

## 2. Where project instructions live (use the right layer)

| Layer | Path | Role |
| --- | --- | --- |
| **Structure (authoritative)** | `docs/02_RepositoryStructure.md` | Definitive tree, naming, status |
| **Agent entry (this file)** | `AGENTS.md` | How agents should behave; pointers to all rules |
| **Skills pointer** | `skills.md` | Index; project skill in `.cursor/skills/python-fundamentals-curriculum/SKILL.md` |
| **Cursor subagents** | `.cursor/agents/*.md` | Optional custom subagents (session content, practice code, doc verification) |
| **Cline mirror** | `.clinerules/` | Cline-facing rules, skills, agents, and workflows; root and `.cursor/` remain canonical |
| **OpenCode config** | `.opencode/` | OpenCode plugin config plus tool-facing rules, skills, agents, and prompts |
| **Claude / Anthropic (short form)** | `CLAUDE.md` (repo root) | Condensed guardrails; same project as this file |
| **Claude Code folder (optional)** | `.claude/CLAUDE.md` | Confirms root instructions; use when tools expect `.claude/` |
| **Cursor (modular rules)** | `.cursor/rules/*.mdc` | Mandatory and scoped rules; see `.cursor/rules/README.md` |
| **GitHub Copilot** | `.github/copilot-instructions.md` | In-browser / Copilot alignment with Cursor rules |
| **Copilot prompts (reusable)** | `.github/prompts/*.prompt.md` | Agent-mode starters: `create-session`, `review-content`, `create-practice-file`, `fix-references` |
| **Copilot instructions (scoped)** | `.github/instructions/*.instructions.md` | File-scoped rules: `python-practice` → `src/**/*.py`; `session-docs` → `docs/sessions/**` |
| **CI (docs)** | `.github/workflows/docs-quality.yml` | Markdown lint + Lychee on doc paths |
| **CI (Python)** | `.github/workflows/python-quality.yml` | Ruff + `compileall` on `src/` (no separate pytest suite) |
| **Contributing (humans + agents)** | `CONTRIBUTING.md` | How to contribute and review |

If anything in this table conflicts with **`docs/02_RepositoryStructure.md`**, treat the doc as correct and fix the other file.

---

## 3. Reasoning: ReAct and Chain-of-Thought (CoT)

This project **expects explicit reasoning** in learning material and in agent work. Use the same patterns as in `.github/copilot-instructions.md` and `.cursor/rules/01_educational-content-rules.mdc` (which contain the full tables).

**Content creation (teaching material and examples):**  
**THINK → REASON → ACT → VERIFY** (and iterate if a verification step fails).

- **THINK (CoT):** Objectives, chunk the topic, order from simple to complex, anticipate misconceptions.
- **REASON:** Prerequisites, links to other sessions, original examples, pitfalls.
- **ACT:** Write docs, `src/` practice files, Mermaid-first diagrams with ASCII fallback, exercises.
- **VERIFY:** Clarity, completeness, fit in the sequence, originality (zero-copy).

**Content or repo review (audits, “review everything” requests):**  
**OBSERVE → ANALYZE → REASON → VERIFY → ACT**

- **OBSERVE:** List every file in scope (no sampling).
- **ANALYZE:** Open and check each file against the checklists in `03_quality-assurance.mdc` and `01_educational-content-rules.mdc`.
- **REASON:** Explain issues and patterns; do not skip edge cases.
- **VERIFY:** Cross-check paths, links, and naming.
- **ACT:** Fix or report with paths and clear follow-ups.

**Code edits in this repo (not “write a new session”):** default to **minimal, targeted diffs** — read surrounding context, preserve pedagogy and formatting, and do not rename or restructure files unless the user asked or it is required to fix a bug.

---

## 4. Non-negotiable policies (all agents)

1. **Zero-copy (transformative only)**  
   No verbatim third-party text; no mirrored outline or example order; brief quotes only with quotation marks and citation. See `.cursor/rules/01_educational-content-rules.mdc`.

2. **Respect the curriculum**  
   Do not remove or condense teaching content to “save space” — **split** into parts if length is an issue. Session numbering must reflect real dependencies (e.g. variables before operators at L1).

3. **Paths and names**  
   Use `L{level}/S{session}/` (e.g. `src/L1/S1/01_hello.py`, `docs/sessions/L1/S1.md`). Validate references before commit.

4. **Automation and quality**  
   Prefer `tools/psscripts/docs-lint.ps1` and `tools/psscripts/docs-links.ps1` (or the `npx` / Docker commands in `README.md`) before large documentation merges. Match CI in `.github/workflows/docs-quality.yml` where possible. For practice code, CI runs **Ruff** and `compileall` (see `pyproject.toml` and `.github/workflows/python-quality.yml`).

5. **After structural or convention changes**  
   Update in order: `docs/02_RepositoryStructure.md` → `README.md` / `.github/copilot-instructions.md` as needed → `.cursor/rules/` cross-references → this file and `CLAUDE.md` if agent workflows changed.

6. **Session bucketing safety (new content placement)**  
   Treat `docs/meetup/L1/sessions.md` status table as the placement guard for Level 1 meetup updates. New **Python fundamentals** content from `source-material/` or `src/Working/` should go to planned/new sessions by default. Do not add newly authored content to completed sessions unless the user explicitly approves it in the current request.

7. **Python-only repository scope**  
   This repository is **Python Fundamentals in Practice only**. Do **not** add AWS, cloud platforms, Bedrock, or other non-Python course tracks. Do **not** migrate non-Python files from ignored `source-material/` into `docs/` or `src/`. Do **not** borrow app-stack conventions (React, FastAPI, MCP demos) from other repositories. If intake is clearly unrelated to Python fundamentals, skip migration or ask the user.

---

## 5. Cursor rules: reading order

1. `05_primary-directives.mdc` — what to do first, automation, update protocol  
2. `01_educational-content-rules.mdc` — zero-copy, CoT/ReAct, session structure  
3. `02_repository-structure.mdc` — context and links to the structure doc  
4. `04_markdown-standards.mdc` — links, encodings, session doc shape  
5. `03_quality-assurance.mdc` — checklists before commit  
6. `06_cross-level-integration.mdc` — prerequisites and “enables” links between sessions  

---

## 6. Python and environment notes

- Target **Python 3.13+** (see `README.md`). On Windows, prefer `py -m pip` and run practice files with the same interpreter students are expected to use.
- `__pycache__/` and bytecode are generated artifacts — do not treat them as source.

---

## 7. When unsure

Prefer **ask** over **guess** on large pedagogical rewrites, licensing-sensitive material, or repo-wide moves. For small, mechanical fixes (typos, broken links, wrong paths), fix and run lint/link checks when docs are touched.

---

**Bottom line:** Treat `docs/02_RepositoryStructure.md` as the map, `.cursor/rules/` and `.github/copilot-instructions.md` as the detailed law, and **AGENTS.md** / **CLAUDE.md** as the compass for any automated assistant in this repository.

**Precedence on conflict:** `docs/02_RepositoryStructure.md` → `.github/copilot-instructions.md` → `CLAUDE.md` → this file.
