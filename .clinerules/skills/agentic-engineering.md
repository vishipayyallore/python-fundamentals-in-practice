---
name: agentic-engineering
description: Work on the Agentic Engineering in Practice repository — React frontend, FastAPI backend, OpenAI Agent SDK, MCP server, and 15-session curriculum (Swamy's Tech Skills Academy).
---

# Agentic Engineering in Practice

**Scope:** Agentic Engineering in Practice repository. Live curriculum: Swamy's Tech Skills Academy. See `README.md` and `.cursor/rules/01_repository-purpose.mdc`.

## Layout

```text
src/
├── frontend/       # React + TypeScript + Vite + Tailwind
├── backend/        # FastAPI + OpenAI Agent SDK
└── mcp-server/     # MCP tools

docs/               # 01-repository-structure.md … 13-observability-dashboard.md
presentation/       # demo-01 … demo-15
```

## Session roadmap

| Session | Git tag | Focus |
| ------- | ------- | ----- |
| 1 | `v1.0-build-your-first-agent` | Agent Runtime, calculator + weather MCP |
| 2 | `v2.0-stateful-agents` | Conversation state, streaming, tracing |
| 3 | `v3.0-multi-provider-agents` | OpenAI + AWS Bedrock provider interface, optional Azure OpenAI |
| 4 | `v4.0-context-engineering` | Application state, LLM context, context policies |
| 5 | `v5.0-knowledge-driven-agents` | RAG, vector store, knowledge tools |
| 6 | `v6.0-multi-agent-engineering` | Planner, specialists, coordinator |
| 7 | `v7.0-production-foundations` | Docker, CI, smoke tests, observability |
| 8 | `v8.0-evaluation-guardrails` | Evaluations, guardrails, quality gates |
| 9 | `v9.0-local-capstone` | Local capstone assembled from prior capabilities |
| 10-15 | `v10.0-distributed-persistence` … `v15.0-enterprise-capstone` | Phase II platform, cloud, Kubernetes, enterprise operations |

Extend the **single app** — do not create parallel `demoN/` code trees.

## Teaching quality

- Explain agent patterns in plain English before SDK APIs
- Ground examples in realistic business scenarios
- Use Mermaid + ASCII for agent flows and tool calling
- Keep docs aligned with runnable code

## Related

- **Demo SOP:** `.github/skills/demo-companions/SKILL.md`
- **CI commands:** `.github/skills/ci-checks/SKILL.md`
- **Subagent:** `.cursor/agents/demo-roadmap-review.md`
