---
name: workspace-review
description: Comprehensive workspace review for Agentic Engineering in Practice — structure, demo roadmap, governance mirrors, stack scaffolding, and docs/code alignment.
---

# Workspace review

Full audit checklist for this repository.

## 1. Repository structure

- [ ] `src/frontend/`, `src/backend/`, `src/mcp-server/` match `docs/01-repository-structure.md`
- [ ] No stray ML/week-bundle folders from other repos
- [ ] `presentation/demo-0N/` present for planned sessions

## 2. Demo roadmap

- [ ] README table reflects actual demo status
- [ ] Code implements current demo scope only (no half-finished future-demo leaks without docs)
- [ ] Git tags documented for completed milestones

## 3. Governance parity

- [ ] `.github/skills/` ↔ `.cursor/skills/` byte-identical
- [ ] `.github/agents/` ↔ `.cursor/agents/` byte-identical
- [ ] `.github/rules/` ↔ `.cursor/rules/` aligned
- [ ] `CLAUDE.md` references current rule and skill paths
- [ ] `.github/copilot-instructions.md` matches repo purpose

## 4. Stack health (when scaffolded)

- [ ] Backend: Ruff + pytest pass
- [ ] MCP: tests pass; tools documented
- [ ] Frontend: lint + build pass
- [ ] `.env.example` complete

## 5. Documentation

- [ ] No broken internal links
- [ ] Agent architecture diagrams current
- [ ] Getting started section in README accurate

## 6. Security

- [ ] No committed secrets
- [ ] `.gitignore` covers `.env`, `node_modules/`, `.venv/`

## Output

Executive summary + prioritized action list (P0 blocking, P1 before next demo, P2 nice-to-have).
