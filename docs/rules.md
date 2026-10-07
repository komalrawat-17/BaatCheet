# BaatCheet — Project Rules & Conventions

> **Last Updated**: 2026-10-06

## 1. Code Style
- **Python**: Follow PEP 8. Use `black` for formatting and `flake8` for linting. Enforce type hints for all function signatures.
- **JavaScript/React**: Use ESLint and Prettier. Prefer functional components and Hooks.

## 2. Git Workflow
- **Conventional Commits**: Use `feat:`, `fix:`, `docs:`, `style:`, `refactor:`, `test:`, `chore:`.
- **Branching**: Use `feature/branch-name` or `bugfix/branch-name`. Merge via Pull Requests.

## 3. Architecture Rules
- **State**: Backend must remain stateless. All persistent state goes to PostgreSQL; all ephemeral/shared state goes to Redis.
- **Dependencies**: Pin all dependencies in `requirements.txt` and `package.json`.
- **Secrets**: Never commit `.env` files or hardcode secrets in code.
