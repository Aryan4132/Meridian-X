# Tasks: Meridian-X Implementation Plan

## Phase 0: Day 1 — Foundation & Performance Boost

- [x] **Task 0.1: Ultra-Lightweight Frontend RAM & Performance Engine (`OPT-01`)** — `meridian_frontend/src/hooks/useMemoryOptimizer.ts`, `Settings.tsx`, `index.css`
- [x] **Task 0.2: Geo-Location & Spatial Context Engine (`PL-30`)** — `meridian_backend/src/tools/geo_location.py`, `web.py`, `registry.py`
- [x] **Task 0.3: Geo-Location Unit Test Verification** — `meridian_backend/tests/test_geo_location.py`

## Phase 1: Biometric & Perception Modules

- [x] **Task 1: Eye-Tracking & Gaze Control (`JARVIS-02`)** — `meridian_backend/src/core/gaze_tracker.py`
- [x] **Task 2: Voice Biometric Verification (`JARVIS-03`)** — `meridian_backend/src/voice/voice_biometrics.py`
- [x] **Task 3: Smart Camera & RTSP Vision (`JARVIS-05`)** — `meridian_backend/src/core/camera_sentinel.py`
- [x] **Task 4: AR Smart Glasses Bridge (`JARVIS-08`)** — `meridian_backend/src/core/ar_bridge.py`
- [x] **Task 5: Multi-Lingual Polyglot (`JARVIS-10`)** — `meridian_backend/src/voice/polyglot.py`

## Phase 2: Predictive, Neural & Defense Modules

- [x] **Task 6: Predictive Pre-Execution (`JARVIS-04`)** — `meridian_backend/src/core/predictive_engine.py`
- [x] **Task 7: Room Arrival Auto-Briefing (`JARVIS-06`)** — `meridian_backend/src/core/presence_briefing.py`
- [x] **Task 8: Self-Healing System Defense (`JARVIS-07`)** — `meridian_backend/src/core/system_defense.py`
- [x] **Task 9: Subconscious Codebase Memory (`JARVIS-09`)** — `meridian_backend/src/core/neural_rag.py`
- [x] **Task 10: Autonomous PR & Test Generator (`JARVIS-11`)** — `meridian_backend/src/core/auto_reviewer.py`

## Phase 3: Verification Checkpoint

- [x] **Task 11: Run Full Backend Test Suite**

## Phase 4: OAuth 2.0 & n8n-Style Workflow Engine (`SEC-25`, `SEC-26`, `WKF-01`-`04`)

- [x] **Task 12.1: Backend OAuth 2.0 Core & Token Auto-Rotator (`oauth_manager.py`)** — `meridian_backend/src/core/oauth_manager.py`
- [x] **Task 12.2: External Service Agent Connectors (`external_connectors.py`)** — Gmail, Calendar, Contacts, GitHub, Cloudflare, Slack, Discord, Telegram, Notion, Airtable tools in `meridian_backend/src/tools/external_connectors.py`
- [x] **Task 12.3: n8n-Style Workflow Automation Engine & Webhook Gateway (`workflow_engine.py`)** — Node pipeline engine, Webhook gateway, triggers, and action executor in `meridian_backend/src/core/workflow_engine.py`
- [x] **Task 12.4: FastAPI Dual Auth & Workflow API Integration (`auth.py` & `api.py`)** — `meridian_backend/src/core/auth.py`, `meridian_backend/api.py`

## Phase 5: Day 4 — Execution Controls, Model Auditor & Auto PR Reviewer (`PL-07`, `PL-23`, `PL-24`, `PL-25`, `PL-26`, `JARVIS-11`)

- [x] **Task 13.1: Unified Sync LLM Call Helper (`llm_provider.py`)** — Implement `call_llm_sync` / `call_llm` in `src/core/llm_provider.py` supporting both local Ollama & cloud API providers.
- [x] **Task 13.2: Unified LLM Code Auditor (`PL-07`)** — Refactor `src/tools/review.py` to route code review via unified `llm_provider`.
- [x] **Task 13.3: User-Selected Model in Task Decomposition & Loop Helpers (`PL-23`)** — Update `src/core/loop.py` to bind internal decomposition, planning, and helper prompts to user's selected `brain_model` and model source.
- [x] **Task 13.4: Backend API Settings & Model Source Synchronization (`PL-26`)** — Update `api.py` and `database.py` to persist and sync `MERIDIAN_MODEL_SOURCE` (`local` vs `cloud`) across user profiles and streaming endpoints.
- [x] **Task 13.5: Autonomous PR Reviewer & Unit Test Generator (`JARVIS-11`)** — Implement `src/tools/auto_reviewer.py` with `generate_unit_tests` & `review_git_changes`, registered in `registry.py`.
- [x] **Task 13.6: Frontend Settings Execution Mode Toggle & Dynamic Resolution (`PL-24`, `PL-25`)** — Update `Settings.tsx`, `Timeline.tsx`, and `Mascot.tsx` with explicit `Local` vs `Cloud/API` execution mode toggle & localStorage sync.
- [x] **Task 13.7: Day 4 Unit Test Suite Verification** — Create `meridian_backend/tests/test_day4_features.py` and verify all tests pass.

## Phase 6: Day 5 — Full-Duplex Voice, Biometrics & Conversation Window (`AST-15`, `AST-08`, `JARVIS-03`)

- [x] **Task 14.1: Low-Latency Full-Duplex Engine & Voice Response Toggle (`AST-15`)** — Fix method scoping in `meridian_backend/src/voice/duplex.py`, add 50ms VAD window barge-in handling, fast streaming, and `voice_response_enabled` state control.
- [x] **Task 14.2: Continuous Conversation Window API Synchronization (`AST-08`)** — Synchronize thread-safe continuous window timing in `meridian_backend/src/voice/wakeword.py`.
- [x] **Task 14.3: Voice Biometric Identity & Speaker Verification (`JARVIS-03`)** — Implement `meridian_backend/src/voice/voice_biometrics.py` with 128-dim voiceprint embeddings, speaker registration, cosine similarity matching, and unauthorized voice rejection.
- [x] **Task 14.4: FastAPI Voice Endpoints Integration (`api.py`)** — Expose REST/WebSocket endpoints for full-duplex session control, barge-in trigger, voice response toggle, continuous conversation window, and biometrics management.
- [x] **Task 14.5: Day 5 Unit Test Suite & Verification** — Create `meridian_backend/tests/test_day5_features.py` and run full test suite to verify 100% pass rate.

## Phase 7: Day 6 — Codebase AST Graph, Neural RAG & PaperCoder (`DEV-05`, `JARVIS-09`, `DEV-04`)

- [x] **Task 15.1: Offline Codebase AST Graph Expansion (`DEV-05`)** — Enhance `meridian_backend/src/core/code_graph.py` with Python AST parsing, symbol search, caller/callee tracing, and change impact prediction.
- [x] **Task 15.2: Subconscious Codebase Memory & Neural RAG Synthesizer (`JARVIS-09`)** — Implement `meridian_backend/src/core/neural_rag.py` to synthesize background project intent knowledge graphs.
- [x] **Task 15.3: Paper2Code (PaperCoder) Integration (`DEV-04`)** — Implement `meridian_backend/src/tools/papercoder.py` 3-stage paper-to-repo generator and register in `registry.py`.
- [x] **Task 15.4: FastAPI REST Endpoints Integration (`api.py`)** — Expose endpoints for CodeGraph AST symbol search, trace, impact, Neural RAG intent graph, and PaperCoder generation.
- [x] **Task 15.5: Day 6 Unit Test Suite Verification** — Create `meridian_backend/tests/test_day6_features.py` and run full backend test suite to verify 100% pass rate.

## Phase 8: Comprehensive Brain Audit & Stability Hardening

- [x] **Task 16.1: Fix `loop.py` Streaming Producer Queue Deadlock & Exception Handling (A1)**
- [x] **Task 16.2: Fix `loop.py` Tier 2 Audit+Execute Race Condition (A2)**
- [x] **Task 16.3: Harden `database.py` SQLite Concurrency & Fix Unbounded Memory Cache (A3, A4)**
- [x] **Task 16.4: Wire `/api/chat` Non-Streaming Endpoint to Real ReAct Loop (A5)**
- [x] **Task 16.5: Fix `call_llm_sync` Event Loop Deadlock Risk (A6)**
- [x] **Task 16.6: Optimize MCTS Scorer to Skip Tier 0 Read-Only Tools (A7)**
- [x] **Task 16.7: Deduplicate Consensus Debate Logic & Refactor `loop.py` Helpers (B1, B3, B7, C1, C4, C5)**
- [x] **Task 16.8: Centralize `get_ollama_client_host()` and `ENV_KEY_MAP` (B6, C3)**
- [x] **Task 16.9: Add Database Caching & Batch Turbovec Index Writes (B4, B5)**
- [x] **Task 16.10: Modularize `api.py` into Cleaner Sub-Routers (B2)**
- [x] **Task 16.11: Verification & Test Suite Pass Check (Phase 8)**

## Phase 9: Multi-OS Support & Codebase Hardening

- [x] **Task 17.1: Fix Windows-Only Imports & Open File Handlers in `src/tools/system.py`** — Safely guard `winreg`, `psutil.win_service_iter()`, replace `os.startfile()` with cross-platform open dispatch (`open`/`xdg-open`), fix `ping -n`/`-c` flag, and guard `wmic`/`netsh`.
- [x] **Task 17.2: Cross-Platform Task Scheduler in `src/tools/task_scheduler.py`** — Add Linux `cron`/`at` and macOS `launchd` / `at` abstractions alongside Windows `schtasks`.
- [x] **Task 17.3: Dynamic Venv Executable Resolver in `src/tools/developer.py`** — Replace hardcoded `venv/Scripts/*.exe` with cross-platform `_get_venv_executable()` and platform binary suffix handling.
- [x] **Task 17.4: Cross-Platform Shell Execution & Process Monitor in `src/tools/shell.py`** — Fix `monitor_process()` hardcoded PowerShell command to use `/bin/sh` or `/bin/bash` on Linux/macOS, fix self-healing prompt, and fix `shell=True` list arguments.
- [x] **Task 17.5: Linux & macOS Active Window Tracking & Game Mode in `src/core/proactive.py`** — Implement `xdotool`/`xprop` (Linux) and `osascript` (macOS) active window, PID, and fullscreen state detection.
- [x] **Task 17.6: Hardware & Security Defense Generalization** — Update `src/core/hardware_detector.py` (Apple Silicon & AMD ROCm detection), `src/core/system_defense.py` (cross-platform disk root & system process exclusions), and `src/tools/recording.py` (`Cmd+V` vs `Ctrl+V` clipboard paste).
- [x] **Task 17.7: Requirements, CI Pipeline & Script Cleanup** — Update `requirements.txt` platform markers for `pynvml`, update `.github/workflows/release.yml` with `appimage` bundle, update `install.sh` Linux dependencies (`xclip`, `xdotool`).
- [x] **Task 17.8: Multi-OS Verification Test Suite** — Create `meridian_backend/tests/test_multi_os.py` and run full backend test suite to verify 100% pass rate.

## Phase 10: Repository Cleanup, Audit Fixes, & v0.1.0 Release

- [x] **Task 18.1: Directory & Dead Code Cleanup** — Delete `agent/temporal_consensus_guard.py`, `test_temporal_consensus.py`, runtime junk folders (`test_database_dir/`, `test_logging_dir/`, `test_tools_dir/`), and log files (`*.log`). Preserve `KANBAN.md` and `TIMELINE.md`.
- [x] **Task 18.2: Gitignore & Security Fixes** — Update `.gitignore` with `vault.enc`, test dirs, logs, and target build folders. Fix CORS origins in `meridian_backend/api.py`.
- [x] **Task 18.3: Clean Frontend Package & Version Reset** — Remove `express` and duplicate `vite` from `meridian_frontend/package.json`. Reset version to `0.1.0` in `package.json` and `tauri.conf.json`. Run `npm install` in `meridian_frontend`.
- [x] **Task 18.4: Overhaul README.md** — Create high-quality, professional `README.md` for Meridian-X v0.1.0.
- [x] **Task 18.5: Fix GitHub Release Workflow** — Update `.github/workflows/release.yml`.
- [x] **Task 18.6: Verification & Git Tag Push (`v0.1.0`)** — Run full pytest and frontend lint, commit clean changes, and push tag `v0.1.0` to GitHub repository.
