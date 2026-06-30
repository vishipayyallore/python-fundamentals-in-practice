---
name: e2e-testing
description: Smoke verification for Agentic Engineering in Practice — environment, service health, chat flow, and MCP tool calls when the stack is runnable.
---

# E2E smoke testing

Run when `src/backend`, `src/mcp-server`, and `src/frontend` are scaffolded.

## Prerequisites

- `.env` configured from `.env.example` (OpenAI API key, etc.)
- `uv sync --all-groups` from **repository root**
- `npm install` in `src/frontend`

## Smoke steps

### 1. MCP server (manual smoke only)

```powershell
$env:PYTHONPATH = "src/mcp-server"
uv run python src/mcp-server/server.py
```

Verify server starts without import errors (Ctrl+C after health check). In Demo 1 the backend starts MCP via stdio automatically.

### 2. Backend (from repo root)

```powershell
uv run uvicorn app.main:app --app-dir src/backend --reload --port 8000
```

- `GET /health` returns OK
- Chat endpoint accepts a test message

### 3. Frontend

```powershell
cd src/frontend
npm run dev
```

- Chat UI loads at [http://localhost:5173](http://localhost:5173)
- Send a message that triggers a tool call

### 4. Tool-call verification (Demo 1)

| User message | Expected tool |
|--------------|---------------|
| "What is 15 * 23?" | calculate |
| "Weather in Seattle" | get_weather |

## Report format

| Step | Status | Notes |
|------|--------|-------|
| MCP start | | |
| Backend start | | |
| Frontend load | | |
| Chat round-trip | | |
| Tool call | | |
