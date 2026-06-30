# Task prompt — agentic-engineering-in-practice audit

Use this template when requesting a structured repository audit.

```json
{
  "repo_name": "agentic-engineering-in-practice",
  "audit_type": "workspace | demo | ci | docs",
  "demo_number": 1,
  "focus_paths": ["src/backend", "docs"],
  "checks": [
    "structure_vs_docs_01_repository_structure",
    "demo_readme_parity",
    "governance_mirrors",
    "backend_ruff_pytest",
    "frontend_lint_build",
    "mcp_tool_tests",
    "markdownlint"
  ],
  "output_format": "executive_summary + table(Path, Status, Notes)"
}
```

Replace `demo_number` and `focus_paths` per task. Use `agent-ci-verify` subagent for CI-aligned runs.
