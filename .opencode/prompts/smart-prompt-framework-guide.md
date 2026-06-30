# SMART prompt framework — Agentic Engineering

Short guide for effective prompts in this repository.

## Roles

| Role | Focus |
|------|-------|
| **Agent Engineer** | OpenAI Agent SDK, instructions, tool routing |
| **MCP Tool Author** | `src/mcp-server/tools/`, schemas, tests |
| **FastAPI Integrator** | Routes, Pydantic models, streaming |
| **Frontend Builder** | Agent Dashboard UI, hooks, services |

## SMART pattern

- **Specific:** Layer (`frontend` / `backend` / `mcp-server`) and session (1–15)
- **Measurable:** e.g. "weather tool called when user asks about Seattle"
- **Achievable:** One capability per change when possible
- **Relevant:** Aligns with README session roadmap
- **Time-bound:** Scoped to current demo unless explicitly future work

## Example prompts

**Demo 1 — tool wiring**

> In `src/backend/app/agent_runtime/`, ensure the agent runtime calls the calculator MCP tool when the user message contains arithmetic. Add a pytest that mocks the MCP client and asserts `calculate` is invoked.

**Demo 2 — streaming**

> Add SSE streaming from `POST /chat` in FastAPI and consume it in `useChatStream` so tokens render incrementally in `ConversationPanel`.

**Docs**

> Update `docs/08-tool-calling.md` with a Mermaid sequence diagram and ASCII fallback for calculator tool calling that matches the current `src/mcp-server/tools/calculator.py` schema.

## Avoid

- Week-bundle / notebook / from-scratch ML phrasing from other repos
- New `demo2/` application folders
- Undocumented environment variables (update `.env.example`)
