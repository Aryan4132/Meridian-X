# Task Checklist - Phase 2: Refactor God Files (Pure Split, Zero Behavior Changes)

## Completed - Phase 1 Hardening
- [x] Task 1: Consensus debate gate decoupling & unit test (`pytest meridian_backend/tests/test_consensus_gate.py` passes 8/8)
- [x] Task 2: Structured logging (eliminate bare `except Exception: pass`) across target files
- [x] Task 3: Unified audio streaming singleton in Mascot & Timeline
- [x] Task 4: Full verification gate run (23/23 tests green, frontend build clean)
- [x] Task 5: Phase 5 Workspace Hygiene & .gitignore fix

---

## Active - Phase 2: Refactor God Files
- [x] Task 2.1: Refactor `meridian_backend/src/core/proactive.py` (1,360 lines) into modular `src/core/proactive/` package
  - Acceptance:
    - `src/core/proactive/ergonomics.py`: Focus guardian, 20-20-20 eye strain, posture, hydration reminders.
    - `src/core/proactive/commits.py`: Git commit whisperer, workspace change tracker, daily/evening review digests.
    - `src/core/proactive/guard.py`: Background system monitoring, process immunity checks, memory leak detection.
    - `src/core/proactive/__init__.py`: Clean re-export of all public functions and state variables so `@patch("src.core.proactive.publish_nudge_sync")` and all existing imports work identically.
    - No file in `src/core/proactive/` exceeds 500 lines.
  - Verify: `pytest meridian_backend/tests/test_proactive*.py meridian_backend/tests/test_advanced_proactive.py meridian_backend/tests/test_multi_os.py` passes (32/32 green).

- [x] Task 2.2: Refactor `meridian_backend/src/core/loop.py` into Orchestrator + decoupled sub-modules
  - Acceptance:
    - `src/core/confirmations.py`: User approval gating, command risk classification, safety tier confirmation.
    - `src/core/llm_clients.py`: Model dispatch, client caching, GPU VRAM tracking.
    - `src/core/checkpoints.py`: Git snapshot state capture, rollback, checkpoint commit management.
    - `src/core/loop_planning.py`: HTP decomposition, MCTS branch scoring, prompt complexity routing, memory summarization.
    - `src/core/loop_executor.py`: Tool output anomaly checking, signature critique & healing, history compression, async tool execution.
    - `src/core/loop.py`: Orchestrator coordinating ReAct flow while preserving exact `run_react_agent_loop` signature and return values.
  - Verify: `pytest meridian_backend/tests/test_consensus_gate.py meridian_backend/tests/test_loop*.py meridian_backend/tests/test_day*.py meridian_backend/tests/test_sprint2_features.py` passes (58/58 green).

- [ ] Task 2.3: Refactor `meridian_backend/api.py` (4,427 lines) into modular router package (`meridian_backend/api/`)
  - Acceptance:
    - `meridian_backend/api/chat.py`: Chat execution, live SSE loop streaming (`/api/chat`, `/api/chat/stream`).
    - `meridian_backend/api/voice.py`: Speech synthesis, transcription, duplex audio endpoints.
    - `meridian_backend/api/rag.py`: Document ingestion, Turbovec search, graph sync.
    - `meridian_backend/api/vault.py`: Secrets vault, credential rotation, AES encryption.
    - `meridian_backend/api/scheduler.py`: Task scheduler, CRON triggers, workflow triggers.
    - `meridian_backend/api/mcp.py`: Model Context Protocol server endpoints.
    - `meridian_backend/api/system.py`: Process guard, system health, telemetry, diagnostics.
    - `meridian_backend/api.py`: Orchestrator mounting sub-routers via `app.include_router(...)`.
    - No route paths, query params, schemas, or behaviors altered.
  - Verify: FastAPI app imports cleanly, endpoints respond identically, `pytest meridian_backend/tests/` passes.

- [x] Task 2.3.5: Refactor & Harden `meridian_backend/database.py` (1,736 lines) into modular `src/db/` package + Facade
  - Acceptance:
    - `src/db/connection.py`: SQLite connection factory with `@contextmanager` + WAL/PRAGMA + self-healing schema + test isolation.
    - `src/db/embeddings.py`: Multi-provider embedding generator (OpenAI, Ollama, FastEmbed, feature hashing fallback).
    - `src/db/vectors.py`: Turbovec index management, read/write thread locking, health checks, and quarantine.
    - `src/db/cache.py`: Thread-safe Tier-1 `_exact_match_cache` (`threading.RLock`) + Tier-2 vector cache (no write `DELETE` in read paths).
    - `src/db/profile.py`: Thread-safe user profile cache, Fernet encryption/decryption, user preferences, budget caps.
    - `src/db/rag.py`: Knowledge base chunking & semantic search.
    - `src/db/logs.py`: Task logs, background runs, thought logs, token spend tracking.
    - `src/db/contacts.py`: WhatsApp contacts management and resolution.
    - `src/db/memory.py`: Sleep cycle memory distillation.
    - `src/db/parsers.py`: Document extraction (`extract_text_from_file`).
    - `database.py`: Clean Facade re-exporting all symbols for 100% backward compatibility (shrunk from 1,736 lines to 98 lines).
    - No file in `src/db/` exceeds 250 lines.
  - Verify: `pytest tests/test_database.py ...` (36/36 passed clean).


- [x] Task 3.1: Local Model Stopping Tokens & Anti-Hallucination (`src/core/loop_stream.py`, `src/core/loop_parser.py`)
  - Acceptance:
    - Pass `stop=["</call>", "</call:"]` and `num_ctx: 8192` to Ollama chat stream options so models never emit hallucinated `<observation>` blocks.
    - Add parser guard in `StreamingXMLParser` to drop unprompted simulated observations.
  - Verify: Unit test verifies stop tokens passed in Ollama options and parser blocks simulated observations.

- [x] Task 3.2: Lazy Boot Daemon Lifecycle (`meridian_backend/api.py`, `src/voice/wakeword.py`)
  - Acceptance:
    - `wakeword`: Only start audio listener thread when `wakeword_enabled` is true in user profile/env. Provide clean toggle endpoint.
    - `p2p_node`: Guard behind `P2P_ENABLED` flag.
    - `smart_clipboard`: Guard behind `smart_clipboard_enabled` preference.
  - Verify: FastAPI startup completes in <1s without audio device or socket conflicts.

- [x] Task 3.3: Tool Registry Pruning & Consolidation (`src/tools/registry.py`)
  - Acceptance:
    - Retire legacy `play_youtube_music` and `verify_media_playing`.
    - Consolidate browser and scraper tools into best-in-class primary implementations.
    - Clean tool documentation signatures in `loop_stream.py`.
  - Verify: Tool count pruned, zero broken imports, all core tests green.

- [x] Task 3.4: Comprehensive Verification Gate
  - Acceptance: All test suites green across backend and frontend build clean.
  - Verify: `pytest meridian_backend/tests/`, `npm --prefix meridian_frontend run build`, `npx --prefix meridian_frontend tsc --noEmit`.

---

## Active - Sprint 39: Intelligence & Telemetry Suite

- [x] Task 39.1: Hybrid Sparse-Dense RAG with Reciprocal Rank Fusion (PL-08, PL-11)
  - Acceptance:
    - Pure-Python BM25 keyword matching + Turbovec dense embeddings in `src/db/rag.py` using Reciprocal Rank Fusion.
    - Expose `hybrid_search_knowledge_base(query, limit=5, bm25_weight=0.5)` returning top matches.
    - Re-export in `database.py`.
  - Verify: Pytest in `meridian_backend/tests/test_hybrid_rag.py` (3/3 passed).
  - Files: `meridian_backend/src/db/rag.py`, `meridian_backend/database.py`, `meridian_backend/tests/test_hybrid_rag.py`

- [x] Task 39.2: Live Browser-Use Mini-HUD Streaming & Viewport Frame API
  - Acceptance:
    - Add `browser_capture_b64()` in `src/tools/web_browser.py` returning base64 JPEG of current page.
    - Broadcast step events and frame in `BrowserUseAgent.run()`.
    - Expose `GET /api/browser/frame` in `meridian_backend/api.py`.
  - Verify: Pytest in `meridian_backend/tests/test_browser_frame.py` (3/3 passed).
  - Files: `meridian_backend/src/tools/web_browser.py`, `meridian_backend/src/tools/browser_use_agent.py`, `meridian_backend/api.py`

- [x] Task 39.3: Perception Stream to Proactive Nudges Bridge (PL-03, PL-04)
  - Acceptance:
    - In `src/api/perception.py`, bridge active window error sense and terminal crashes to `publish_nudge_sync`.
    - Expose endpoint `POST /api/perception/error-sense` triggering automated fix suggestions.
  - Verify: Pytest in `meridian_backend/tests/test_perception_bridge.py` (2/2 passed).
  - Files: `meridian_backend/src/api/perception.py`, `meridian_backend/tests/test_perception_bridge.py`

- [x] Task 39.4: Collapsible ReAct Step Accordions & Diff Viewer in Timeline (PL-19)
  - Acceptance:
    - Create `CodeDiffViewer.tsx` component in `meridian_frontend/src/components/ui/CodeDiffViewer.tsx` for colored unified diffs.
    - Enhance `Timeline.tsx` to group thought steps into structured accordions and render code diff blocks with `CodeDiffViewer`.
  - Verify: Frontend typecheck `npx tsc --noEmit` (passed with 0 errors) and build `npm run build`.
  - Files: `meridian_frontend/src/components/ui/CodeDiffViewer.tsx`, `meridian_frontend/src/views/Timeline.tsx`

- [x] Task 39.5: Heterogeneous Subagent Model Routing (PL-10)
  - Acceptance:
    - Resolve model provider (`ollama`, `openai`, `anthropic`, `gemini`, `deepseek`) and model source per subagent role in `src/core/swarm.py` and `src/api/swarm.py`.
    - Support per-role model bindings in `LobbyDebateRequest` and `SwarmAgent.execute`.
  - Verify: Pytest in `meridian_backend/tests/test_swarm_routing.py` (3/3 passed).
  - Files: `meridian_backend/src/core/swarm.py`, `meridian_backend/src/api/swarm.py`, `meridian_backend/tests/test_swarm_routing.py`

- [x] Task 39.6: Comprehensive Sprint 39 Verification & Quality Gate
  - Acceptance: All backend pytest suites pass 100%, frontend compiles with 0 errors.
  - Verify: `pytest meridian_backend/tests/` (19/19 passed), `npm --prefix meridian_frontend run build` (built cleanly).




