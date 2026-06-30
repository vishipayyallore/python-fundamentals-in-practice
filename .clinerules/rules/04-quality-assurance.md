# Quality assurance

**Backend:** Ruff, pytest, Pydantic, no secrets in code. CI: `ci-python.yml`.
**MCP:** tool validation, unit tests, documented schemas (covered by `ci-python.yml`).
**Frontend:** TypeScript strict, ESLint, `npm run build`. CI: `ci-frontend.yml`.
**Docs:** README and diagrams match implementation. CI: `ci-documentation.yml`.
