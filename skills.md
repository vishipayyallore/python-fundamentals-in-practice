# Skills — pointer for this repository

**Last updated:** July 2026

Machine-readable guidance lives in **`.cursor/`** and the root entry files. [Cursor **skills**](https://cursor.com/docs) and [**subagents**](https://cursor.com/docs/subagents) add optional, discoverable layers on top of rules.

**Python-only repository:** `python-fundamentals-in-practice` teaches Python fundamentals only — session docs (`docs/sessions/`), practice scripts (`src/L{level}/`), and Level 1 meetup summaries (`docs/meetup/L1/`). Not AWS, cloud, Bedrock, or other non-Python tracks. Do not migrate non-Python `source-material/` intake into this repo.

**Authoritative dev repo:** Curriculum is developed in **`python-fundamentals`** (Swamy-only single source of truth). This repo is the **meetup replica** — sync from the dev repo; do not author new curriculum here first. Current meetup focus: **Level 1 S1–S6**.

| Location | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Agent entry: policies, ReAct/CoT, where rules live |
| [`.cursor/rules/`](.cursor/rules/) | Modular `.mdc` rules (educational content, QA, markdown, directives) |
| [`.cursor/skills/`](.cursor/skills/) | One project skill: [`python-fundamentals-curriculum/SKILL.md`](.cursor/skills/python-fundamentals-curriculum/SKILL.md) — when to read which doc before editing the course |
| [`.cursor/agents/`](.cursor/agents/) | Cursor subagents: `session-content`, `python-practice-code`, `docs-verifier` |
| [`.clinerules/agents/`](.clinerules/agents/) | Cline mirrors: `agent-ci-verify`, `session-roadmap-review`, `python-practice-code`, `docs-originality-review` |
| [`.opencode/agents/`](.opencode/agents/) | OpenCode mirrors (same four agent roles) |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | GitHub Copilot alignment with the same curriculum rules |
| [`CLAUDE.md`](CLAUDE.md) | Short brief for Claude-oriented tools |
| [`.clinerules/`](.clinerules/) | Cline-facing entry, agents, skills, workflows; canonical policy remains root/`.cursor` |
| [`.opencode/`](.opencode/) | OpenCode plugin config and tool-facing mirrors |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Human and agent contribution expectations |
| [`docs/02_RepositoryStructure.md`](docs/02_RepositoryStructure.md) | Authoritative paths, naming, and current inventory |
| [`docs/meetup/L1/sessions.md`](docs/meetup/L1/sessions.md) | Session status guard for meetup content placement (completed vs planned) |

**Personal** skills can also live under your user `~/.cursor/skills/`; this repo's **policy** still comes from `AGENTS.md` and **`.cursor/rules/`** so those stay the single source of truth for policies.

When adding new educational content, default placement is planned/new sessions; do not inject into completed sessions without explicit user permission. Only promote **Python fundamentals** material from `source-material/` or `src/Working/` into formal `src/L{level}/S{session}/` paths.
