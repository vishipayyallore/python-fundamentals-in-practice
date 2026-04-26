# Pull Request

## 📋 Description

**What does this PR do?**

- [ ] Bug fix
- [ ] New feature
- [ ] Documentation improvement
- [ ] Code example enhancement
- [ ] New session content
- [ ] Other: `...`

**Brief description of changes:**

---

## 🔗 Related Issues

Closes #(issue number)
Related to #(issue number)

---

## 📍 Files Changed

**Documentation:**

- `docs/...`

**Practice Code:**

- `src/...`

**Configuration:**

- `.github/...`
- `.cursor/...`

**Other:**

- `...`

---

## ✅ Quality Checklist

### **Content Quality**

- [ ] Zero-copy policy verified (no verbatim text from sources)
- [ ] Content is transformative and original
- [ ] 30-minute session compliance (if applicable)
- [ ] Beginner-friendly language and explanations
- [ ] Learning objectives are clear

### **Technical Quality**

- [ ] All Python code runs without errors
- [ ] File naming follows conventions (`01_`, `02_`, `_Plan.md`)
- [ ] Directory structure uses `L{level}/S{session}/` format
- [ ] Python baseline policy is aligned across docs + tooling (`README.md`, `AGENTS.md`, `pyproject.toml`, `.github/workflows/python-quality.yml`)
- [ ] All file references are correct and validated
- [ ] Markdown linting passes: `./tools/psscripts/docs-lint.ps1`
- [ ] Link validation passes: `./tools/psscripts/docs-links.ps1`

### **File References**

- [ ] All practice file references point to existing files
- [ ] All documentation links work correctly
- [ ] Numeric prefixes included in all file references (`01_`, `02_`, etc.)
- [ ] Paths use correct `L{level}/S{session}/` structure

### **Documentation Updates**

- [ ] Updated `_Plan.md` if adding new sessions
- [ ] Updated Master Plan if adding new content
- [ ] Updated [Repository Structure](../docs/02_RepositoryStructure.md) if layout, naming, or agent doc inventory changed
- [ ] Updated `README.md` if contributor-facing structure or commands changed
- [ ] Updated `AGENTS.md` / `CLAUDE.md` (and `.claude/CLAUDE.md` if used) if agent entry points or policies changed
- [ ] Updated [Copilot instructions](copilot-instructions.md) and/or [.cursor/rules](../.cursor/rules/) if needed for consistency
- [ ] All cross-references updated

---

## 🧪 Testing

**How was this tested?**

- [ ] Ran all Python files locally
- [ ] Tested markdown rendering
- [ ] Verified all links work
- [ ] Checked file references manually
- [ ] Reviewed content for clarity

**Test results:**

```text
(Describe test results or paste output)
```

---

## 📸 Screenshots (if applicable)

Add screenshots to help explain your changes.

---

## 📚 Educational Impact

**How does this help learners?**

- What concepts does this teach?
- What learning objectives does it support?
- How does it fit into the curriculum progression?

---

## 🔍 Review Notes

**Anything specific you'd like reviewers to focus on?**

- Areas of concern
- Questions for maintainers
- Alternative approaches considered

---

## ✅ Pre-Submission Checklist

- [ ] I've read the [Contributing Guidelines](../CONTRIBUTING.md)
- [ ] I've reviewed the [Educational Content Rules](../.cursor/rules/01_educational-content-rules.mdc)
- [ ] I've completed the quality checklist above
- [ ] I've tested my changes locally
- [ ] I've updated related documentation
- [ ] My code follows the repository's style guidelines

---

**Thank you for contributing to Python Fundamentals!** 🐍✨
