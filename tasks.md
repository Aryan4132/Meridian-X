# Tasks — Universal Dynamic API Key & Secret Vault System

- [ ] Task 1: Add Custom Vault API Key Management methods in `meridian_backend/src/core/vault.py`
  - Acceptance: `save_custom_api_key`, `list_custom_api_keys`, `delete_custom_api_key`, and environment injection helpers.
  - Verify: Unit test in `tests/test_vault.py`.
  - Files: `meridian_backend/src/core/vault.py`

- [ ] Task 2: Add REST API endpoints in `meridian_backend/main.py` & dynamic LLM provider resolution in `llm_provider.py`
  - Acceptance: `GET /api/vault/keys`, `POST /api/vault/keys`, `DELETE /api/vault/keys/{env_var}` endpoints. Dynamic OpenAI-compatible client routing for custom providers with custom base URLs.
  - Verify: `python -c "import main; print('Backend loaded')"` & `pytest`.
  - Files: `meridian_backend/main.py`, `meridian_backend/src/core/llm_provider.py`

- [ ] Task 3: Build Universal API Key Vault Manager UI component in `meridian_frontend/src/views/Settings.tsx`
  - Acceptance: Form fields for Name, Env Var Name, Secret Key, Base URL, and Category. Live key listing table with show/hide toggle, category badges, and delete button.
  - Verify: `npm run build` succeeds cleanly.
  - Files: `meridian_frontend/src/views/Settings.tsx`

- [ ] Task 4: Verify end-to-end integration and update project Kanban board
  - Acceptance: `npm run build` and `pytest` pass with 0 errors; update `KANBAN.md` and `kanban_board.md`.
  - Verify: Run test suite & build check.
