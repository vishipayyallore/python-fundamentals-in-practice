# Agentic core context

**Repository:** `agentic-engineering-in-practice`

## Purpose

Single **Agentic Engineering in Practice** application that grows through the **Swamy's Tech Skills Academy** curriculum:

| Session | Tag | Capability |
|---------|-----|------------|
| 1 | `v1.0-build-your-first-agent` | Agent Runtime, calculator + weather MCP |
| 2 | `v2.0-stateful-agents` | Conversation state, streaming, tracing |
| 3 | `v3.0-multi-provider-agents` | OpenAI + AWS Bedrock provider interface |
| 4 | `v4.0-context-engineering` | Application state, LLM context, context policies |
| 5 | `v5.0-knowledge-driven-agents` | RAG, vector store, knowledge tools |
| 6 | `v6.0-multi-agent-engineering` | Planner, specialists, coordinator |
| 7 | `v7.0-production-foundations` | Docker, CI, smoke tests, observability |
| 8 | `v8.0-evaluation-guardrails` | Evaluations, guardrails, quality gates |
| 9 | `v9.0-local-capstone` | Local capstone assembled from prior capabilities |
| 10-15 | `v10.0-distributed-persistence` … `v15.0-enterprise-capstone` | Phase II platform, cloud, Kubernetes, enterprise operations |

## Stack

- **Frontend:** React, TypeScript, Vite, Tailwind (`src/frontend/`)
- **Backend:** Python 3.13, FastAPI, OpenAI Agent SDK (`src/backend/`)
- **Tools:** MCP server (`src/mcp-server/`)

## Docs map

- `docs/01-repository-structure.md` — canonical layout
- `docs/04-introduction.md` … `docs/13-observability-dashboard.md` — topic guides
- `docs/02-master-plan.md` — series master plan

## Governance

Skills and agents mirror `.github/skills/` and `.github/agents/`.
