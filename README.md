# 🐍 Python Fundamentals: From clueless to curious

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![Python](https://img.shields.io/badge/Python-3.13+-44CC11?logo=python&logoColor=white)
![Educational](https://img.shields.io/badge/Educational-Course-3B82F6)
![Meetup](https://img.shields.io/badge/Meetup-Series-ED1C40?logo=meetup&logoColor=white)
![Maintainer](https://img.shields.io/badge/Maintainer-Viswanatha%20Swamy%20P%20K-blue)

A comprehensive, transformation-focused Python curriculum designed to take you from complete beginner to confident Python programmer through 9 progressive levels.

> **Format:** Each level contains 5 hours of training (10 sessions × 30 minutes) culminating in 2 hands-on mini projects.

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
   - Complete guide with 10 sessions (Sessions 1-3 available now)
   - Hands-on practice files and mini projects
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
- **🔧 scripts/**: PowerShell utility scripts for development
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
npx --yes markdownlint-cli2 "README.md" "docs/**/*.md" ".github/**/*.md"
```

This uses the repository's `.markdownlint.json` configuration automatically.

**Shortcut on Windows (PowerShell):**

```powershell
# Lint documentation
./scripts/docs-lint.ps1

# Auto-fix formatting issues where possible
./scripts/docs-lint.ps1 -Fix
```

### **Link Validation (Lychee)**

Run link checker to validate all links in documentation:

```powershell
# Validate all links (recommended; matches CI behavior)
docker run --rm -w /input -v "${PWD}:/input" lycheeverse/lychee:latest --config lychee.toml --no-progress README.md docs/**/*.md .github/**/*.md
```

**Shortcut on Windows (PowerShell):**

```powershell
# Validate all links
./scripts/docs-links.ps1

# Extract links only (does not validate)
./scripts/docs-links.ps1 -DumpOnly
```

### **CI/CD Quality Workflow**

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
.\scripts\show-tree.ps1 -Path "." -Depth 4 -OutFile "scripts\repo-structure.txt"

# View structure in terminal
.\scripts\show-tree.ps1 -Path "." -Depth 4
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
