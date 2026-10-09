# Contributing to Meridian-X

Thank you for contributing to Meridian-X! This guide provides everything you need to set up your development environment, run tests, adhere to code standards, and submit pull requests.

---

## 1. Prerequisites

- **Python**: `>= 3.10` (tested on 3.10, 3.11, 3.12, 3.13)
- **Node.js**: `>= 20.x`
- **Rust & Cargo**: (required if building the native Tauri v2 desktop shell)
- **Ollama**: (recommended for local offline model execution)

---

## 2. Setting Up the Environment

### Backend Setup

```bash
# Clone the repository
git clone https://github.com/Aryan4132/Meridian-X.git
cd Meridian-X

# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies and dev tools
pip install --upgrade pip
pip install -r meridian_backend/requirements.txt
pip install -e ".[dev]"
```

### Frontend Setup

```bash
cd meridian_frontend
npm install
```

---

## 3. Development Commands

### Backend

```bash
# Start backend API server
python meridian_backend/api.py

# Run backend test suite
pytest meridian_backend/tests/ -v

# Run targeted test files
pytest meridian_backend/tests/test_tool_modernization.py -v
pytest meridian_backend/tests/test_sprint27_hardening.py -v

# Run linter
ruff check meridian_backend/src
ruff format --check meridian_backend/src
```

### Frontend

```bash
# Start Vite development server
npm --prefix meridian_frontend run dev

# Run strict TypeScript typecheck
npx --prefix meridian_frontend tsc --noEmit

# Production build
npm --prefix meridian_frontend run build
```

---

## 4. Code Standards & Best Practices

1. **Strict Type Safety**:
   - Python: Use explicit type hints for function signatures and return types.
   - TypeScript: Maintain strict typing without `any` where possible (`strict: true` is enforced in `tsconfig.json`).

2. **Tool Development**:
   - Register new tools using the declarative `@tool` decorator in `meridian_backend/src/tools/registry.py`.
   - Provide descriptive docstrings; parameter names and defaults will be automatically reflected to LLMs via `inspect.signature`.

3. **No Code Truncation**:
   - Never commit placeholders, ellipses (`...`), or unresolved `// TODO` blocks.

4. **Continuous Integration**:
   - All PRs are automatically verified via GitHub Actions (`.github/workflows/verify.yml`), running Ruff linting, Pytest, TypeScript checks, and Vite bundle compilation.
