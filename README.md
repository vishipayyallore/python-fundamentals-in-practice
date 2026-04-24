# 🐍 Python Fundamentals: From clueless to curious

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.13+-44CC11?logo=python&logoColor=white)
![Educational](https://img.shields.io/badge/Educational-Course-3B82F6)
![Meetup](https://img.shields.io/badge/Meetup-Series-ED1C40?logo=meetup&logoColor=white)
![Maintainer](https://img.shields.io/badge/Maintainer-Viswanatha%20Swamy%20P%20K-blue)

A comprehensive, transformation-focused Python curriculum designed to take you from complete beginner to confident Python programmer through 9 progressive levels.

> **Format:** Each level contains ~5–6 hours of training (8 sessions × 30 minutes plus 2 mini projects × 30–45 minutes).

---

## 📌 Disclaimer

This is **Swamy's personal learning** repository, not official course material or a structured curriculum.

---

## 🚀 **Quick Start**

**New to Python?** Start your journey here:

1. **📋 [Master Plan](docs/01_Python-Fundamentals-MasterPlan.md)** - Explore the complete 9-level curriculum
   - See the full transformation journey (Noob → Curious Learner)
   - Understand learning progression across all levels
   - Check current implementation status

2. **📖 [Level 1 Plan](docs/sessions/L1/_Plan.md)** - Begin with Level 1: Noob → Nerd
   - Full L1 roadmap: 10 sessions; **Sessions 1–4** (docs and `src/L1/S1`–`S4/` practice) are in-repo
   - [Mini Project 1](docs/sessions/L1/05_MP1.md) is a stub for now; goals live in the plan
   - Step-by-step learning path

3. **🎥 [Watch Level 1 Playlist](https://www.youtube.com/watch?v=Cy6DqbRjsF0&list=PLdLQDTLMjAzpRBxP4q1XJOuLhFG4pSfBB)** - Video walkthroughs for Level 1 sessions
   - Follow along with live coding
   - Visual explanations and demonstrations

---

## 📋 **Repository Structure**

For detailed repository structure, see **[Repository Structure](docs/02_RepositoryStructure.md)**.

**Quick Overview:**

- **📚 docs/**: Educational documentation (sessions, images, master plan)
- **💻 src/**: Practice code files organized by level and session
- **🔧 tools/psscripts/**: PowerShell utility scripts for development (docs lint, link check, tree)
- **⚙️ .github/**: CI/CD workflows and copilot instructions
- **⚙️ .cursor/**: Cursor AI configuration and rules
- **📄 AGENTS.md** / **CLAUDE.md** / **.claude/**: AI agent entry points (aligned with [Repository Structure](docs/02_RepositoryStructure.md))

---

## 📚 **Documentation**

- **📋 Master Plan:** [docs/01_Python-Fundamentals-MasterPlan.md](docs/01_Python-Fundamentals-MasterPlan.md) - Complete 9-level curriculum overview
- **📁 Repository Structure:** [docs/02_RepositoryStructure.md](docs/02_RepositoryStructure.md) - Detailed structure and file organization

---

## 🛠️ **Development & Quality Assurance**

### **Python & pip Usage (Windows)**

On Windows, it’s usually safest to run pip through the Python launcher so you install packages into the Python you intend to use:

```powershell
# Show pip help / available options
py -m pip
```

Example (install `uv`):

```powershell
py -m pip install uv
```

### **Developer Git Setup**

To keep commit authorship consistent across machines, set your global Git identity once per machine:

```bash
git config --global user.email "yourname@youremail.com"
git config --global user.name "Your Name"
```

### **Documentation Quality Checks (Local)**

Run Markdown lint against README and all documentation before opening a PR:

```powershell
# From repo root - lint all markdown files
npx --yes markdownlint-cli2 "README.md" "AGENTS.md" "CLAUDE.md" "skills.md" "docs/**/*.md" ".github/**/*.md" ".claude/**/*.md"
```

This uses the repository's `.markdownlint.json` configuration automatically.

**Shortcut on Windows (PowerShell):**

```powershell
# Lint documentation
./tools/psscripts/docs-lint.ps1

# Auto-fix formatting issues where possible
./tools/psscripts/docs-lint.ps1 -Fix
```

### **Link Validation (Lychee)**

Run link checker to validate all links in documentation:

```powershell
# Validate all links (recommended; matches CI behavior)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress README.md AGENTS.md CLAUDE.md skills.md docs/**/*.md .github/**/*.md .claude/**/*.md
```

**Shortcut on Windows (PowerShell):**

```powershell
# Validate all links
./tools/psscripts/docs-links.ps1

# Extract links only (does not validate)
./tools/psscripts/docs-links.ps1 -DumpOnly
```

### **Python static checks (Ruff)**

This repository does not ship `pytest` tests; practice scripts are run manually. CI runs **Ruff** (covers common **flake8**- / **isort**-class checks) and `python -m compileall` on `src/`. Locally (optional: activate `.venv` first, then `pip install ruff` or use your global tool):

```powershell
ruff check src
python -m compileall -q src
```

Config: `pyproject.toml` · Workflow: `.github/workflows/python-quality.yml`  
There is **no** `package.json` or front-end stack; see the workflow job “Frontend (N/A)” for ESLint/TypeScript.

### **CI/CD Quality Workflow (Docs)**

GitHub Actions automatically runs documentation quality checks on:

- **Pull Requests** that modify documentation
- **Pushes** to main branch that modify documentation
- **Manual triggers** via GitHub UI

**Manual Trigger:**

1. Open GitHub → Actions → "Docs Quality" workflow
2. Click "Run workflow" (no inputs required)
3. View markdownlint + Lychee results; download the `lychee-report` artifact for details

### **Repository Structure Generation**

Generate current repository structure for documentation:

```powershell
# Generate structure tree and save to file
.\tools\psscripts\show-tree.ps1 -Path "." -Depth 4 -OutFile "tools\psscripts\repo-structure.txt"

# View structure in terminal
.\tools\psscripts\show-tree.ps1 -Path "." -Depth 4
```

---

## 🤝 **Contributing**

We welcome contributions! Whether it's:

- 🐛 Bug fixes
- 📝 Documentation improvements
- 💡 New practice exercises
- 🎯 Additional learning resources

---

## 📞 **About & Get In Touch**

### [ShyvnTech](https://www.linkedin.com/company/shyvntech) & [Swamy's Tech Skills Academy](https://www.linkedin.com/company/swamy-s-tech-skills-academy)

_Ready to become curious about Python? Let's begin your transformation!_ 🚀

**Ready to take your Python skills to the next level? Join our advanced courses and workshops!**

- 🌐 Visit our website for more courses
- 📧 Contact us for custom training programs
- 🏆 Get certified in Python fundamentals
- 👥 Join our learning community

Happy Coding! 🐍✨
