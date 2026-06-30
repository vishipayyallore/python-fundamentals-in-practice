# Task Prompt - Python Fundamentals Audit

Use this template when requesting a structured repository audit.

```json
{
  "repo_name": "python-fundamentals-in-practice",
  "audit_type": "workspace | session | ci | docs | practice-code | governance",
  "level": "L1",
  "session": "S6",
  "focus_paths": ["docs/sessions/L1/S6.md", "src/L1/S6", ".clinerules", ".opencode"],
  "checks": [
    "structure_vs_docs_02_repository_structure",
    "session_doc_practice_parity",
    "meetup_status_guard",
    "governance_alignment",
    "ruff_check_src",
    "compileall_src",
    "markdownlint"
  ],
  "output_format": "executive_summary + table(Path, Status, Notes)"
}
```

Replace `level`, `session`, and `focus_paths` per task. Use `agent-ci-verify` subagent for CI-aligned runs.
