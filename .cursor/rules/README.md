# Cursor AI Project Rules - Python Fundamentals

**Version**: 1.1  
**Last Updated**: April 2026

This directory contains modular rule files for Cursor AI, customized for the **Python Fundamentals** educational curriculum repository.

**Python-only:** this repo teaches Python fundamentals only — not AWS, cloud, Bedrock, or other non-Python tracks. See `05_primary-directives.mdc` §6 and `01_educational-content-rules.mdc` for intake boundaries.

---

## 📋 Rule Files

### `01_educational-content-rules.mdc`

**Priority**: MANDATORY  
**Content**: Zero-Copy Policy, Transformative Workflow, 30-minute sessions, session structure requirements, educational excellence standards, Python code standards

### `02_repository-structure.mdc`

**Content**: Python Fundamentals repository context, structure overview (L{level}/S{session}/), support resources

### `03_quality-assurance.mdc`

**Content**: Quality checklists (content, technical, documentation), Python code testing requirements

### `04_markdown-standards.mdc`

**Content**: Markdown authoring standards, session documentation structure, file reference validation, encoding requirements

### `05_primary-directives.mdc`

**Content**: Primary directives, automation-first approach, update verification protocol, file naming validation

### `06_cross-level-integration.mdc`

**Content**: Cross-level integration requirements, session connection patterns, prerequisite relationships

---

## 🎯 Repository-Specific Rules

This rule set is customized for the **Python Fundamentals** repository:

- **Structure**: Uses `L{level}/S{session}/` directory format
- **Sessions**: 30-minute focused learning sessions
- **Code**: Working Python practice files in `src/L{level}/S{session}/`
- **Documentation**: Session docs in `docs/sessions/L{level}/`
- **Levels**: 9 progressive levels (Noob → Nerd → ... → Curious Learner)

---

## 📝 Adding New Rules

1. Create new `.mdc` file in this directory
2. Use descriptive name with numeric prefix: `07_new-rule-name.mdc`
3. Follow existing file structure
4. Update this README with new rule description

---

## 🔗 Related Files

- **Agent entry (all tools)**: `AGENTS.md` (policy map, ReAct/CoT, how to use these rules)
- **Skills pointer**: `skills.md` (this repo includes one project skill pack at `.cursor/skills/python-fundamentals-curriculum/SKILL.md`)
- **Claude short brief**: `CLAUDE.md` and `.claude/CLAUDE.md` (optional pointer; root is canonical)
- **GitHub Copilot**: `.github/copilot-instructions.md` (rules aligned with this directory)
- **Repository structure (source of truth)**: `docs/02_RepositoryStructure.md`
- **Main README**: `README.md` (repository overview and structure)
- **Session documentation**: `docs/sessions/L1/_Plan.md` (Level 1 curriculum plan)

---

## 🚀 Quick Reference

**File Naming**:

- Python files: `01_name.py`, `02_name.py`
- Session docs: `S1.md`, `S2.md`, `_Plan.md` (underscore prefix sorts first)
- Directories: `L1/S1/`, `L1/S2/`

**Path References**:

- Practice files: `src/L1/S1/01_hello.py`
- Session docs: `docs/sessions/L1/S1.md`
- Images: `docs/images/S1/Help_V1.PNG`

**Quality Checks**:

- Markdown linting: `npx --yes markdownlint-cli2 "docs/**/*.md"`
- Link checking: Use lychee with `lychee.toml`
- Python quality checks: `ruff check src` and `python -m compileall -q src`

---

**Note**: Cursor AI automatically reads all `.mdc` files in `.cursor/rules/` directory. No additional configuration needed.
