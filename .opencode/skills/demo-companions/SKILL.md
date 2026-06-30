---
name: demo-companions
description: Demo companion architecture for agentic-engineering-in-practice — parity checks between docs, presentation assets, and src/ code for each session milestone (demo-01 … demo-15).
---

# Demo companions

**Scope:** `agentic-engineering-in-practice` only.

## Three-layer demo bundle

Each session milestone should have aligned artifacts:

| Layer | Path | Contains |
|-------|------|----------|
| Docs | `docs/` | Concept guides; demo-specific doc when applicable |
| Presentation | `presentation/demo-0N/` | Session slides, scripts, diagrams |
| Code | `src/frontend`, `src/backend`, `src/mcp-server` | Runnable features for that session |

## Definition of done (per session)

- [ ] README session row updated (status, topics)
- [ ] Relevant `docs/NN-*.md` sections reflect new capabilities
- [ ] `presentation/demo-0N/` has session assets (or placeholder README if pre-session)
- [ ] Code implements advertised features
- [ ] Git tag applied (`vN.N-…`) when milestone is complete
- [ ] `.env.example` updated if new env vars are required

## Parity checks

1. **README ↔ code** — listed tools and features exist and run
2. **docs ↔ code** — architecture diagrams match routes and MCP tools
3. **presentation ↔ docs** — session narrative matches documented flow

## Cross-session rules

- Session N builds on Session N−1 — no duplicate parallel implementations
- Retire or gate incomplete features behind clear "planned" labels in docs

## Related

- Structure: `docs/01-repository-structure.md`
- Subagent: `.cursor/agents/demo-roadmap-review.md`
