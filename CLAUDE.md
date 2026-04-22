# 🤖 Claude AI Instructions for Python Fundamentals Project

**Project:** Python Fundamentals Curriculum  
**Owner:** Swamy's Tech Skills Academy  
**Purpose:** Educational content development and maintenance

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

## 🛠️ **DEVELOPMENT COMMANDS**

### **Linting**

```powershell
# Lint all Markdown documentation
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"

# Auto-fix linting issues
.\scripts\docs-lint.ps1 -Fix
```

### **Link Validation**

```powershell
# Validate all links in documentation
.\scripts\docs-links.ps1
```

### **Repository Structure**

```powershell
# Generate current repository structure
.\scripts\show-tree.ps1 -Path "." -Depth 4 -OutFile "scripts\repo-structure.txt"
```

---

## 📋 **PROJECT STRUCTURE OVERVIEW**

> **📋 Single Source of Truth**: For the complete and up-to-date repository structure, see [`docs/02_RepositoryStructure.md`](docs/02_RepositoryStructure.md). This is the authoritative documentation for all repository structure details.

**Quick Reference:**

- **Documentation**: `docs/sessions/L{level}/` - Session documentation organized by level
- **Practice Code**: `src/L{level}/S{session}/` - Python practice files organized by level and session
- **Images**: `docs/images/S{session}/` - Educational images organized by session
- **Scripts**: `scripts/` - PowerShell utility scripts for development

**Key File Relationships:**

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

| Phase       | Steps                                        |
| ----------- | -------------------------------------------- |
| **OBSERVE** | Scan and catalog ALL files in scope          |
| **ANALYZE** | Open and examine EVERY file individually     |
| **REASON**  | Apply logical reasoning to identify issues   |
| **VERIFY**  | Cross-check findings and validate compliance |
| **ACT**     | Document findings and update content         |

### **Reasoning in Educational Content:**

**CRITICAL**: All code examples and explanations must show the "Why" behind decisions, not just the "What".

**✅ DO**: Include explicit reasoning for code design decisions

- Show why a data structure was chosen
- Explain alternative approaches and trade-offs
- Make the thought process visible to learners

**❌ AVOID**: Stating facts without reasoning

- Don't just say "use a dictionary" — explain WHY
- Don't skip the reasoning chain from problem to solution

---

## 🔧 **EDITING GUIDELINES**

### **✅ SAFE EDITS:**

- Fixing typos and spelling errors
- Correcting broken links
- Updating file paths that are demonstrably wrong
- Fixing character encoding issues (corrupted emojis)
- Adding missing sections that are clearly incomplete

### **⚠️ CAREFUL EDITS:**

- Modifying code examples (ensure they still work)
- Changing file structure references
- Updating installation instructions
- Modifying pedagogical explanations

### **🚫 AVOID:**

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

---

## 📝 **FILE REFERENCE STANDARDS**

**CRITICAL**: All file references must:

- ✅ Include numeric prefixes (`01_`, `02_`, etc.) in file names
- ✅ Use correct `L{level}/S{session}/` directory structure
- ✅ Match actual file names exactly
- ✅ Be verified before committing

**Common Errors to Avoid:**

- ❌ Missing numeric prefixes: `S1.md` → ✅ `01_S1.md`
- ❌ Missing level identifier: `sessions/S1/` → ✅ `sessions/L1/01_S1.md`
- ❌ Incorrect path structure: `src/S1/` → ✅ `src/L1/S1/`

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

## 🔗 **Related Documentation**

- **📋 Repository Structure (Single Source of Truth)**: [`docs/02_RepositoryStructure.md`](docs/02_RepositoryStructure.md)
- **GitHub Copilot**: `.github/copilot-instructions.md` - GitHub Copilot-specific guidelines
- **Agent Tools**: `AGENTS.md` - OpenAI Codex and general agent guidelines
- **Cursor AI Rules**: `.cursor/rules/` - Comprehensive modular rules for Cursor AI
- **Main README**: `README.md` - Project overview and quick start guide

---

**Remember: This is educational content that transforms beginners into programmers. Every word matters, every example counts, and every student's learning journey depends on the quality and integrity of this curriculum.**

**🎯 When in doubt, preserve and ask. When certain, proceed with precision.**
