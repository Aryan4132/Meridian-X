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

- [ ] Task 2.4: Verification Gate
  - Acceptance: All test suites green across backend and frontend build clean.
  - Verify: `pytest meridian_backend/tests/`, `npm --prefix meridian_frontend run build`, `npx --prefix meridian_frontend tsc --noEmit`.
