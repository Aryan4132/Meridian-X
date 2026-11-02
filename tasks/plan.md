# Implementation Plan - Sprint 40: System-Wide Polish, Performance & Resilience Suite

## Overview

Implement the 6 strategic system-wide improvements:

1. Pure Router Aggregator: Extract WebSocket endpoints to `meridian_backend/src/api/websockets.py`, move lifecycle logic to `meridian_backend/src/core/lifespan.py`, shrinking `api.py` under 250 lines.
2. Frontend Bundle & Connection Polish: Lazy load Three.js mascot canvas, code-split heavy views, and add reconnect HUD with exponential backoff on WebSocket / SSE drops.
3. Subprocess & Concurrency Guard: Kill orphan subagents and browser instances on interrupt, add timeout wrappers on Tier-0 concurrent tool dispatches.
4. Native SQLite FTS5 for Hybrid RAG: Setup FTS5 virtual table for lightning-fast keyword search with transparent fallback.
5. Hardware-Backed Vault Security: OS Keyring lookup with zero-crash fallback.
6. Playwright Shadow DOM & Bounding Box Element Resolution: Enhance element indexing to inspect Shadow DOM and client bounding rects.

## Architecture Decisions

- **WebSockets & Lifespan**: Create `meridian_backend/src/api/websockets.py` with `APIRouter()` mounting `/ws`, `/api/ws/mobile`, `/ws/agent-status`. Create `meridian_backend/src/core/lifespan.py` holding `lifespan(app: FastAPI)` context manager.
- **Frontend Code Splitting**: In `meridian_frontend/src/App.tsx`, load views with `React.lazy()` and `Suspense`. In `Mascot.tsx`, lazy-load Three.js components. Add `ConnectionBanner.tsx` for connection tracking.
- **Process Guard & Timeouts**: In `meridian_backend/src/core/loop.py`, `interrupt_agent_loop` terminates children of current process matching browser/python subagents. In `loop_dispatcher.py`, `asyncio.wait_for(task, timeout=15.0)` around concurrent tool executions.
- **SQLite FTS5**: In `src/db/connection.py`, create `CREATE VIRTUAL TABLE IF NOT EXISTS knowledge_base_fts USING fts5(...)` with graceful `sqlite3.OperationalError` handling if compile option omitted. In `src/db/rag.py`, query FTS5 if present, falling back to pure Python BM25.
- **Vault Keyring**: In `src/core/vault.py`, attempt `import keyring` and retrieve/store vault master secret. Fall back silently to existing file/env key.
- **Browser DOM Inspection**: In `src/tools/web_browser.py`, expand JS evaluation script to recursively traverse `element.shadowRoot` to capture interactive buttons and inputs inside web components.

## Verification Checkpoints

- Checkpoint 1 (Backend Modularization & FTS5): Pytest for websockets router, lifespan, and FTS5 hybrid RAG.
- Checkpoint 2 (Interrupt & Keyring): Pytest for loop interrupt and vault keyring resolution.
- Checkpoint 3 (Frontend Build & Typecheck): Verify `tsc --noEmit` and `npm run build` succeeds with reduced bundle chunks.
