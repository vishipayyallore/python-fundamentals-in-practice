# Skills — pointer for this repository

**Last updated:** April 2026

Machine-readable guidance lives in **`.cursor/`** and the root entry files. [Cursor **skills**](https://cursor.com/docs) and [**subagents**](https://cursor.com/docs/subagents) add optional, discoverable layers on top of rules.

| Location | Purpose |
| --- | --- |
| [`AGENTS.md`](AGENTS.md) | Agent entry: policies, ReAct/CoT, where rules live |
| [`.cursor/rules/`](.cursor/rules/) | Modular `.mdc` rules (educational content, QA, markdown, directives) |
| [`.cursor/skills/`](.cursor/skills/) | One project skill: [`python-fundamentals-curriculum/SKILL.md`](.cursor/skills/python-fundamentals-curriculum/SKILL.md) — when to read which doc before editing the course |
| [`.cursor/agents/`](.cursor/agents/) | Custom subagents: session docs, `src/L1` practice code, doc verification (read-only) |
| [`.github/copilot-instructions.md`](.github/copilot-instructions.md) | GitHub Copilot alignment with the same curriculum rules |
| [`CLAUDE.md`](CLAUDE.md) | Short brief for Claude-oriented tools |
| [`docs/meetup/L1/meetup-sessions.md`](docs/meetup/L1/meetup-sessions.md) | Session status guard for meetup content placement (completed vs planned) |

**Personal** skills can also live under your user `~/.cursor/skills/`; this repo’s **policy** still comes from `AGENTS.md` and **`.cursor/rules/`** so those stay the single source of truth for policies.

When adding new educational content, default placement is planned/new sessions; do not inject into completed sessions without explicit user permission.
