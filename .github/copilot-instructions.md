# 🤖 Copilot Instructions for Python Fundamentals Project

**Project:** Python Fundamentals Curriculum  
**Owner:** Swamy's Tech Skills Academy  
**Purpose:** Educational content development and maintenance  
**Last updated:** April 2026

---

## 📌 **Where these instructions sit**

| File | Use |
| --- | --- |
| `AGENTS.md` | **Primary agent entry** — ReAct/CoT expectations, policy map, links to all rules (Cursor, Copilot, Claude) |
| `skills.md` | Skills pointer; this repo includes one project skill pack at `.cursor/skills/python-fundamentals-curriculum/SKILL.md`, while policy remains in `AGENTS.md` and `.cursor/rules/` |
| `CLAUDE.md` | Short project brief for Claude/Anthropic-oriented tools; defers to `AGENTS.md` for the full map |
| `.claude/CLAUDE.md` | Optional pointer for workflows that look under `.claude/`; canonical text remains at the repo root |
| `.cursor/rules/*.mdc` | Mandatory modular rules; see `.cursor/rules/README.md` for the index (aligned with this file) |
| `.github/prompts/*.prompt.md` | **Reusable agent-mode starters** — `create-session`, `review-content`, `create-practice-file`, `fix-references` |
| `.github/instructions/*.instructions.md` | **Scoped rules** — `python-practice` (applies to `src/**/*.py`), `session-docs` (applies to `docs/sessions/**`) |

**Structure details:** Always use [`docs/02_RepositoryStructure.md`](../docs/02_RepositoryStructure.md) as the single source of truth for paths, naming, and inventory.

---

## 🚨 **CRITICAL RULES - READ FIRST**

### **1. 🛡️ DO NOT CORRUPT EXISTING FILES**

- **NEVER** make changes that break existing content
- **ALWAYS** preserve the original structure and formatting
- **VERIFY** changes are minimal and necessary before applying
- **TEST** understanding by reading the full context before editing
- **ASK FOR CONFIRMATION** if changes seem extensive or risky

### **2. 📖 UNDERSTAND BEFORE ACTING**

- **READ** the entire file or section before making any edits
- **ANALYZE** the existing structure and content quality
- **RESPECT** the pedagogical flow and curriculum design
- **PRESERVE** all educational content, examples, and explanations

### **3. 🎯 MAKE PRECISE, TARGETED CHANGES**

- **IDENTIFY** the exact issue to be fixed
- **ISOLATE** the specific text that needs modification
- **MINIMIZE** the scope of changes
- **MAINTAIN** surrounding context and formatting

### **4. 🚫 ZERO-COPY POLICY (Non-Negotiable)**

- **NEVER** copy text verbatim from books, articles, websites, videos, or third-party materials
- **NEVER** mirror a source's outline, section order, headings, or example sequence
- **NEVER** use "light paraphrasing" — must transform completely
- **ALWAYS** create diagrams in Mermaid-first style with ASCII fallback (never embed copyrighted figures)
- **ALWAYS** write fresh, minimal code from first principles
- Brief quotations allowed ONLY with quotation marks and source citation
- **Goal**: Create transformative educational content, not just reformative

**See `.cursor/rules/01_educational-content-rules.mdc` for complete Zero-Copy Policy and Transformative Workflow details.**

---

## 📋 **PROJECT STRUCTURE OVERVIEW**

> **📋 Single Source of Truth**: For the complete and up-to-date repository structure, see [`docs/02_RepositoryStructure.md`](../docs/02_RepositoryStructure.md). This is the authoritative documentation for all repository structure details.

**Quick Reference:**

- **Documentation**: `docs/sessions/L{level}/` - Session documentation organized by level
- **Practice Code**: `src/L{level}/S{session}/` - Python practice files organized by level and session
- **Images**: `docs/images/S{session}/` - Educational images organized by session
- **Scripts**: `tools/psscripts/` - PowerShell utility scripts for development

**File Relationships:**

- `docs/sessions/L1/01_S1.md` ↔ `src/L1/S1/` (practice files)
- `docs/sessions/L1/_Plan.md` → Overall curriculum structure
- `README.md` → Entry point with navigation links

---

## 🎓 **CURRICULUM PHILOSOPHY**

### **Educational Approach:**

- **30-minute sessions** - Realistic time constraints
- **Splitting over trimming** - If content is too long, split into multiple parts instead of removing educational material
- **Progressive complexity** - Each session builds on previous
- **Hands-on practice** - Every concept has practical application
- **Visual learning** - Emojis, diagrams, and clear formatting
- **Beginner-focused** - No assumptions about prior knowledge

**See `.cursor/rules/01_educational-content-rules.mdc` for details on the splitting policy.**

### **Content Quality Standards:**

- **Pedagogically sound** - Based on learning theory
- **Technically accurate** - All code examples work correctly
- **Professionally presented** - Industry-standard documentation
- **Accessible** - Clear language and multiple learning styles

---

## 🧠 **CoT/ReAct METHODOLOGY**

### **For Content CREATION (THINK → REASON → ACT → VERIFY):**

| Phase      | Steps                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------- |
| **THINK**  | Understand objective → Decompose into chunks → Sequence logically → Anticipate misconceptions |
| **REASON** | Check prerequisites → Map connections → Design examples → Identify pitfalls                   |
| **ACT**    | Write content → Create code examples → Add diagrams → Design exercises                        |
| **VERIFY** | Is it clear? → Complete? → Progressive? → Original?                                           |

### **For Content REVIEW (OBSERVE → ANALYZE → REASON → VERIFY → ACT):**

| Phase       | Steps                                         |
| ----------- | --------------------------------------------- |
| **OBSERVE** | Scan and catalog ALL files in scope           |
| **ANALYZE** | Open and examine EVERY file individually      |
| **REASON**  | Apply logical reasoning to identify issues    |
| **VERIFY**  | Cross-check findings and validate compliance  |
| **ACT**     | Document findings and update content          |

### **Decision Framework:**

```text
CREATION: THINK → REASON → ACT → VERIFY → (iterate if needed)
REVIEW:   OBSERVE → ANALYZE → REASON → VERIFY → ACT
```

### **Reasoning in Educational Content:**

**CRITICAL**: All code examples and explanations must show the "Why" behind decisions, not just the "What".

**✅ DO**: Include explicit reasoning for code design decisions

- Show why a data structure was chosen
- Explain alternative approaches and trade-offs
- Make the thought process visible to learners

**❌ AVOID**: Stating facts without reasoning

- Don't just say "use a dictionary" - explain WHY
- Don't skip the reasoning chain from problem to solution

**See `.cursor/rules/01_educational-content-rules.mdc` for full CoT/ReAct details and reasoning examples.**

---

## 🔧 **EDITING GUIDELINES**

### **When Making Changes:**

#### **✅ SAFE EDITS:**

- Fixing typos and spelling errors
- Correcting broken links
- Updating file paths that are demonstrably wrong
- Fixing character encoding issues (corrupted emojis)
- Adding missing sections that are clearly incomplete

#### **⚠️ CAREFUL EDITS:**

- Modifying code examples (ensure they still work)
- Changing file structure references
- Updating installation instructions
- Modifying pedagogical explanations

#### **🚫 AVOID:**

- Large-scale content reorganization without explicit request
- Changing the pedagogical approach or learning sequence
- Removing or significantly altering existing explanations
- Modifying time allocations or session structure
- Changing the emoji-based navigation system

### **Before Any Edit:**

1. **Read the full context** - Understand what you're changing
2. **Identify the specific problem** - What exactly needs fixing?
3. **Plan minimal changes** - What's the smallest fix that works?
4. **Preserve surrounding content** - Don't alter unrelated text
5. **Verify the change makes sense** - Does it improve the content?

### **File Path Corrections:**

- Current structure uses `L1/S1/` hierarchy
- Update references from old `S1/` to new `L1/S1/` structure
- Maintain consistency between documentation and code locations

---

## 📝 **COMMON TASKS**

### **Path Updates:**

> Legacy path examples in this section are intentionally incorrect and should never be reused directly.

```markdown
# LEGACY (incorrect)
src/S1/01_hello.py

# NEW (correct)
src/L1/S1/01_hello.py
```

### **Character Encoding Fixes:**

```markdown
# BROKEN
print("🚀 Advanced Python Preview")

# FIXED  
print("🚀 Advanced Python Preview")
```

### **Link Corrections:**

```markdown
# LEGACY (incorrect)
[Session 1](docs/sessions/S1.md)

# NEW (correct)
[Session 1](docs/sessions/L1/01_S1.md)
```

### **File Reference Validation:**

**CRITICAL**: All file references must:

- ✅ Include numeric prefixes (`01_`, `02_`, etc.) in file names
- ✅ Use correct `L{level}/S{session}/` directory structure
- ✅ Match actual file names exactly
- ✅ Be verified before committing

**Common Errors to Avoid:**

- ❌ Missing numeric prefixes: `S1.md` → ✅ `01_S1.md`
- ❌ Missing level identifier: `sessions/S1/` → ✅ `sessions/L1/01_S1.md`
- ❌ Incorrect path structure: `src/S1/` → ✅ `src/L1/S1/`

**See `.cursor/rules/04_markdown-standards.mdc` for detailed file reference validation patterns.**

---

## 🎯 **QUALITY CHECKLIST**

Before submitting any changes, verify:

- [ ] **Content preserved** - No educational material lost
- [ ] **Structure intact** - Formatting and organization maintained
- [ ] **Links work** - All file references are correct (include numeric prefixes)
- [ ] **File references validated** - All references use `L{level}/S{session}/` structure
- [ ] **Code examples** - All Python code is syntactically correct
- [ ] **Reasoning quality** - Code design decisions include explicit reasoning (why this approach?)
- [ ] **Consistency** - Changes align with overall project structure
- [ ] **Readability** - Changes improve rather than degrade clarity

**See `.cursor/rules/03_quality-assurance.mdc` for complete quality checklist.**

---

## 🚨 **EMERGENCY PROCEDURES**

### **If You Accidentally Corrupt Content:**

1. **STOP immediately** - Don't make additional changes
2. **INFORM the user** - Be transparent about what happened
3. **SUGGEST restoration** - Recommend reverting to previous version
4. **LEARN from the mistake** - Understand what went wrong

### **If Unsure About Changes:**

1. **ASK for clarification** - Better to check than assume
2. **DESCRIBE your plan** - Explain what you intend to change
3. **REQUEST confirmation** - Get approval before proceeding
4. **OFFER alternatives** - Suggest different approaches if needed

---

## 💡 **SUCCESS PRINCIPLES**

1. **Precision over Speed** - Take time to understand before acting
2. **Preservation over Innovation** - Maintain existing quality
3. **Communication over Assumption** - Ask questions when uncertain
4. **Incremental over Wholesale** - Make small, targeted changes
5. **Verification over Trust** - Double-check all modifications

---

## 📞 **WHEN IN DOUBT**

**ALWAYS:**

- Read more context
- Ask for clarification  
- Make smaller changes
- Preserve existing content
- Communicate your concerns

**NEVER:**

- Make assumptions about what's needed
- Change content you don't fully understand
- Rush through complex modifications
- Ignore the existing pedagogical structure
- Make changes without clear justification

---

## 🔗 **Related Documentation**

- **🤖 Agent entry (all tools)**: [`AGENTS.md`](../AGENTS.md) — how assistants navigate this repository; ReAct/CoT; update protocol
- **Claude short brief**: [`CLAUDE.md`](../CLAUDE.md) — compact guardrails; full detail in `AGENTS.md` and `.cursor/rules/`
- **📋 Repository Structure (Single Source of Truth)**: [`docs/02_RepositoryStructure.md`](../docs/02_RepositoryStructure.md) - **Authoritative repository structure documentation**
- **Cursor AI Rules**: `.cursor/rules/` - Comprehensive modular rules for Cursor AI
  - See `.cursor/rules/README.md` for overview of all rule files
  - Rules cover: educational content, repository structure, quality assurance, markdown standards, primary directives, cross-level integration
- **Reusable Copilot prompts**: `.github/prompts/` — `create-session`, `review-content`, `create-practice-file`, `fix-references`
- **Scoped Copilot instructions**: `.github/instructions/` — `python-practice` (src files), `session-docs` (docs/sessions files)
- **Main README**: `README.md` - Project overview and quick start guide
- **Level 1 Plan**: `docs/sessions/L1/_Plan.md` - Complete Level 1 curriculum plan

**Note**:

- `docs/02_RepositoryStructure.md` is the **single source of truth** for repository structure
- `AGENTS.md` and `CLAUDE.md` are the **entry points for human and AI readers**; keep them in sync when you change policies or file locations
- `.cursor/rules/` and `.github/copilot-instructions.md` should reference `docs/02_RepositoryStructure.md` for structure details
- Both provide guidance for AI assistants working with this repository

---

**Remember: This is educational content that transforms beginners into programmers. Every word matters, every example counts, and every student's learning journey depends on the quality and integrity of this curriculum.**

**🎯 When in doubt, preserve and ask. When certain, proceed with precision.**
