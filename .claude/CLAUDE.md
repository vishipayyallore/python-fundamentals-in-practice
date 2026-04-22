# .claude — instruction pointer

**Last updated:** April 2026

Some Claude Code or Anthropic workflows look for project context under **`.claude/`**. This repository keeps **canonical instructions at the repository root** so all tools share one source of truth.

**Read in this order:**

1. **`/CLAUDE.md`** (repo root) — short Claude-specific brief and guardrails  
2. **`/AGENTS.md`** (repo root) — full agent map, ReAct/CoT, and policy table  
3. **`/docs/02_RepositoryStructure.md`** — authoritative folder layout and naming  
4. **`/.cursor/rules/README.md`** — index of Cursor `.mdc` rules (educational content, QA, markdown, etc.)  
5. **`/.github/copilot-instructions.md`** — GitHub Copilot alignment (same project policies)

Do not duplicate long policy here; change root **`CLAUDE.md`** or **`AGENTS.md`** and update **`docs/02_RepositoryStructure.md`** if you document new top-level files.
