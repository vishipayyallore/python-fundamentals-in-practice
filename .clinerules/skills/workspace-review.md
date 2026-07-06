---
name: workspace-review
description: Comprehensive workspace review for Python Fundamentals in Practice - structure, curriculum status, governance mirrors, docs links, and Python practice health.
---

# Workspace Review

Full audit checklist for this repository.

## 1. Repository structure

- [ ] Current tracked inventory matches `docs/02_RepositoryStructure.md`.
- [ ] Session docs use `docs/sessions/L{level}/S{session}.md`.
- [ ] Practice files use `src/L{level}/S{session}/`.
- [ ] No stale app-stack, demo-roadmap, notebook, or week-bundle conventions remain in agent docs.
- [ ] No AWS, cloud, Bedrock, or other non-Python course content was added outside ignored `source-material/`.

## 2. Curriculum roadmap

- [ ] README quick start reflects implemented sessions.
- [ ] `docs/sessions/L1/_Plan.md` and `docs/meetup/L1/sessions.md` are used appropriately.
- [ ] Planned sessions are marked clearly.

## 3. Governance parity

- [ ] Root `AGENTS.md`, `CLAUDE.md`, `.claude/CLAUDE.md`, `.github/copilot-instructions.md`, and `skills.md` agree on canonical paths.
- [ ] `.cursor/rules/` remains canonical for modular rules.
- [ ] `.clinerules/` and `.opencode/` are tool-specific mirrors, not alternate sources of truth.
- [ ] Docs CI includes tracked assistant customization Markdown.
- [ ] `docs/meetup/L1/sessions.md` matches `python-fundamentals` (SSOT) byte-for-byte — status table, agendas, event date/URL.

## 4. Python health

- [ ] `ruff check src` passes.
- [ ] `python -m compileall -q src` passes.
- [ ] Calculator smoke checks pass when relevant.

## 5. Documentation

- [ ] No broken internal links
- [ ] Markdown lint passes for docs and tracked customization files
- [ ] Getting started and structure sections in README are accurate

## 6. Security

- [ ] No committed secrets.
- [ ] `.gitignore` covers `.env`, generated caches, `.venv/`, and tool dependency folders where applicable.

## Output

Executive summary plus prioritized action list: P0 blocking, P1 before commit, P2 nice-to-have.
