# Spec: Universal Dynamic API Key & Secret Vault System

## Objective
Provide a universal dynamic API key and secret vault system where users can register ANY third-party API key or cloud provider (LLMs, Search, Audio, Vision, Vector DBs, Custom Tools) via a dynamic form specifying:
1. **Provider / Key Name** (e.g. `Groq`, `OpenRouter`, `Mistral`, `Perplexity`, `SerpAPI`)
2. **Environment Variable Name** (e.g. `GROQ_API_KEY`, `OPENROUTER_API_KEY`)
3. **API Key Secret** (encrypted via AES-GCM)
4. **Base URL / Endpoint (Optional)** (e.g. `https://api.groq.com/openai/v1`)
5. **Category** (`LLM Provider`, `Search & Web`, `Audio & Voice`, `Vision & Media`, `Custom Tool`)

## Tech Stack
- Backend: Python, FastAPI/Uvicorn, AES-GCM Encrypted Vault (`vault.py`), SQLite/JSON storage.
- Frontend: React, TypeScript, Lucide Icons, Vite, `GlowCard`, `HoloButton`.

## Commands
- Backend Test: `pytest tests/test_vault.py`
- Frontend Build: `npm run build`

## Boundaries
- **Always**: Encrypt raw API keys via AES-GCM before saving to disk. Mask key strings in UI displays (`sk-••••••••`).
- **Ask first**: Major changes to master passphrase handling.
- **Never**: Store raw API key strings unencrypted in clear text logs or JSON files.

## Success Criteria
1. Backend REST API endpoints (`GET /api/vault/keys`, `POST /api/vault/keys`, `DELETE /api/vault/keys/{env_var}`) manage custom key entries cleanly.
2. Saved keys automatically inject into `os.environ` and `llm_provider.py` provider resolution.
3. Settings UI under **Integrations** renders a dynamic key manager table allowing adding, searching, masking/unmasking, and deleting key entries.
4. `npm run build` and `pytest` pass with 0 errors.
