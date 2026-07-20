# 🚀 Meridian-X — Improvements & Additions Backlog

> A deep-dive analysis of the entire codebase — what can be added, improved, or hardened across every layer of the stack.
> Categorized by area with rationale and suggested implementation direction.

---

## Table of Contents

1. [🧠 Agent / ReAct Loop](#-agent--react-loop)
2. [🔒 Security & Vault](#-security--vault)
3. [📡 P2P & Networking](#-p2p--networking)
4. [🎤 Voice Engine](#-voice-engine)
5. [🦊 Mascot & Frontend UX](#-mascot--frontend-ux)
6. [📄 Document & RAG Pipeline](#-document--rag-pipeline)
7. [🔧 Tool Registry & Plugin System](#-tool-registry--plugin-system)
8. [💾 Database & Memory](#-database--memory)
9. [⚙️ Scheduler & Resource Governor](#️-scheduler--resource-governor)
10. [🌐 Bridges (Telegram / Discord)](#-bridges-telegram--discord)
11. [🧪 Testing & Quality Assurance](#-testing--quality-assurance)
12. [📦 Build, Packaging & DevOps](#-build-packaging--devops)
13. [📊 Observability & Logging](#-observability--logging)
14. [🆕 New Features to Add](#-new-features-to-add)

---

## 🧠 Agent / ReAct Loop

### Current State
`loop.py` is a 1900-line monolith implementing ReAct reasoning, SSE streaming, tool dispatch, syntax validation, and self-correction all in one file.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Split `loop.py` into sub-modules** (`loop_parser.py`, `loop_dispatcher.py`, `loop_stream.py`). A 1900-line file is hard to maintain and test. | 🔴 High | Medium |
| 2 | **Retry budget per tool** — instead of a global `max_iterations` cap, give each tool call its own retry counter so one broken tool cannot exhaust the full loop budget. | 🟡 Medium | Low |
| 3 | **Structured `<thought>` introspection** — persist agent thought blocks to SQLite alongside the conversation. This enables "replay mode" to understand exactly why the agent took a particular path. | 🟡 Medium | Low |
| 4 | **Tool call batching safety** — `asyncio.gather()` is used for Tier 0 tools, but results are not tagged per-tool. If order changes, outputs can be mismatched. Add explicit per-call tagging. | 🔴 High | Low |
| 5 | **Streaming cancellation** — allow the user to send a `cancel` signal mid-stream via SSE without killing the entire backend process. No graceful abort exists currently. | 🟡 Medium | Medium |
| 6 | **Add `PLANNER` cognitive mode** — a mode where the agent always breaks goals into a named task list before acting, preventing premature execution on complex multi-step requests. | 🟢 Low | High |
| 7 | **Token budget tracking** — estimate token usage per turn using `tiktoken` or character heuristics and auto-summarize long conversation history before hitting the model context window. | 🔴 High | Medium |
| 8 | **Model benchmarking at startup** — run a lightweight probe query on startup to measure real token/sec for the configured model and surface this in the Settings UI. | 🟢 Low | Low |

---

## 🔒 Security & Vault

### Current State
`vault.py` uses AES-GCM with PBKDF2 (100k iterations). The P2P layer uses Fernet encryption.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Vault passphrase caching** — every `vault_get` call requires the passphrase re-supplied. Add a short-lived (5 min TTL) in-memory cache of the derived key, invalidated on restart via a `secrets.token_bytes` session nonce. | 🔴 High | Low |
| 2 | **PBKDF2 → Argon2id** — upgrade key derivation to Argon2id (`argon2-cffi`) for significantly stronger resistance to GPU cracking. | 🟡 Medium | Low |
| 3 | **Vault backup & export** — add a `vault_export_encrypted(output_path)` tool that exports the encrypted vault blob for off-site backup. | 🟡 Medium | Low |
| 4 | **Rate-limit passphrase attempts** — exponential backoff + lockout counter after N failed decryption attempts to mitigate brute force. | 🟡 Medium | Low |
| 5 | **Audit log for vault access** — every `vault_get` / `vault_set` call must write to `audit_logger.py` with timestamp and key name (never the value). | 🔴 High | Low |
| 6 | **Security auditor false-positive suppression** — the `qwen2.5-coder:1.5b` auditor fires on benign patterns. Add a whitelist/suppression mechanism for frequently approved patterns. | 🟡 Medium | Medium |

---

## 📡 P2P & Networking

### Current State
`p2p.py` uses raw TCP sockets for sync and UDP broadcasts for peer discovery. Peer list is an in-memory Python `set`.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Persist peer list to SQLite** — the peer set is lost on restart. Store known peers in a `peers` table and auto-reconnect on daemon startup. | 🔴 High | Low |
| 2 | **mDNS / zeroconf discovery** — replace raw UDP broadcasts with `python-zeroconf` for reliable LAN peer discovery that respects network topology. | 🟡 Medium | Medium |
| 3 | **P2P sync conflict resolution** — when two nodes both write the same key simultaneously, there is no merge strategy. Implement last-write-wins with Lamport timestamps. | 🔴 High | Medium |
| 4 | **Bandwidth throttle for sync** — large knowledge graph syncs can saturate slow WiFi. Add a configurable transfer rate limit using a token-bucket approach. | 🟢 Low | Medium |
| 5 | **P2P connection health pings** — ping known peers every 30s and auto-remove stale peers failing 3 consecutive attempts. | 🟡 Medium | Low |
| 6 | **WebRTC transport option** — optional WebRTC data channel for P2P through NAT/firewalls, enabling sync between machines on different networks. | 🟢 Low | High |

---

## 🎤 Voice Engine

### Current State
Uses `faster-whisper` for STT, a custom ONNX/TFLite wake word model, and `sounddevice` for audio capture.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Background noise gate** — add a configurable RMS silence threshold before feeding audio to Whisper to avoid transcribing ambient noise. | 🔴 High | Low |
| 2 | **VAD (Voice Activity Detection)** — integrate `webrtcvad` or `silero-vad` to detect end-of-utterance instead of fixed silence timeouts. Dramatically improves responsiveness on slow hardware. | 🔴 High | Medium |
| 3 | **Streaming Whisper transcription** — use `faster-whisper`'s streaming API to show partial transcription in the UI while the user is still speaking. | 🟡 Medium | Medium |
| 4 | **TTS voice selection** — expose multiple TTS engine options in Settings (`pyttsx3` for offline, `edge-tts` for Microsoft Neural voices, ElevenLabs for premium). | 🟡 Medium | Medium |
| 5 | **Wake-word false-positive logging** — log every wake-word detection event with confidence score so users can tune sensitivity. | 🟢 Low | Low |
| 6 | **Multi-language STT routing** — detect spoken language via Whisper's `language` output and route to the correct language model prompt. | 🟢 Low | Medium |
| 7 | **Audio input device auto-selection** — at startup, select the microphone with the best signal-to-noise ratio instead of the system default. | 🟢 Low | Medium |

---

## 🦊 Mascot & Frontend UX

### Current State
`Mascot.tsx` (39 KB) handles companion window, island mode, proactive nudges, and state transitions. `Timeline.tsx` (36 KB) handles the main chat view.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Split `Mascot.tsx` into sub-components** — extract `MascotWindow.tsx`, `IslandMode.tsx`, `NudgeToast.tsx`, and `MascotStateManager.tsx`. | 🔴 High | Medium |
| 2 | **Persistent chat scroll position** — switching tabs resets scroll to top. Store and restore per-conversation scroll position in `sessionStorage`. | 🟡 Medium | Low |
| 3 | **Keyboard shortcut reference overlay** — a `?` hotkey that shows a cheat sheet of all global shortcuts. | 🟡 Medium | Low |
| 4 | **Message search / filter** — a search bar in Timeline that filters messages by keyword in real-time. | 🟡 Medium | Medium |
| 5 | **Code block copy button** — messages with code blocks should show a one-click "Copy" button. | 🔴 High | Low |
| 6 | **Conversation branching** — fork the conversation from any message to explore an alternative line of reasoning without losing the original. | 🟢 Low | High |
| 7 | **Dark / Light / System theme toggle** — currently forced dark mode. Add system-aware theme respecting Windows 11 color scheme preference. | 🟡 Medium | Low |
| 8 | **Accessibility improvements** — ARIA labels, focus ring styles, and keyboard-navigable tool call panels. | 🟡 Medium | Medium |
| 9 | **Mascot animation expansion** — add states: `celebrating`, `confused`, `reading`, and `writing` to cover more cognitive states. | 🟢 Low | Medium |
| 10 | **First-run onboarding wizard** — visual step-by-step guide for Ollama setup, model selection, microphone test, and email config instead of manual `.env` editing. | 🟡 Medium | High |

---

## 📄 Document & RAG Pipeline

### Current State
`doc_indexer.py` chunks and embeds documents via `nomic-embed-text` into Turbovec. `documents.py` provides read/create/edit for PDF, DOCX, XLSX, PPTX.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Incremental re-indexing** — add SHA-256 hash-based change detection so only modified chunks are re-embedded on document updates. | 🔴 High | Medium |
| 2 | **Chunk overlap tuning** — expose `chunk_size` and `chunk_overlap` as configurable settings instead of hardcoded values. | 🟡 Medium | Low |
| 3 | **Multi-modal RAG** — extract images from PDFs with `pdfplumber`, describe them via the vision model, and include descriptions in the index. | 🟡 Medium | High |
| 4 | **URL ingestion tool** — `ingest_url(url)` that fetches a page, converts to markdown via `selectolax`, and indexes into the knowledge base. | 🔴 High | Low |
| 5 | **Duplicate detection** — compute SHA-256 before ingestion and skip if the document is already indexed. | 🟡 Medium | Low |
| 6 | **RAG result re-ranking** — apply a cross-encoder re-ranker after vector search to improve chunk relevance ordering. | 🟢 Low | High |
| 7 | **Document version history** — keep previous chunk versions in a `versions` collection when a document is re-indexed. | 🟢 Low | Medium |
| 8 | **Ingestion progress streaming** — stream large document ingestion progress via SSE instead of blocking until complete. | 🟡 Medium | Low |

---

## 🔧 Tool Registry & Plugin System

### Current State
`registry.py` statically imports ~80 tools. `plugins.py` hot-loads Python files from `plugins/`. `dynamic_manager.py` supports LLM-generated tools.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Plugin manifest format** — require a `PLUGIN_MANIFEST` dict with `name`, `version`, `description`, `author`, `min_meridian_version` for UI display and compatibility checks. | 🟡 Medium | Low |
| 2 | **Plugin sandboxing** — plugins run with full backend privileges. Use `RestrictedPython` or the existing subprocess sandbox to isolate community plugins. | 🔴 High | High |
| 3 | **Auto hot-reload via watchdog** — add a `watchdog` observer on `plugins/` so new `.py` files load automatically without an explicit API call. | 🟡 Medium | Low |
| 4 | **Plugin dependency declaration** — allow plugins to declare required packages in their manifest; the system calls `install_package` if any are missing. | 🟡 Medium | Medium |
| 5 | **Tool deprecation aliases** — register renamed tool aliases in `registry.py` that still work but emit a deprecation warning in the agent's thought stream. | 🟢 Low | Low |
| 6 | **MCP server hot-reload** — reload MCP connections when `mcp_config.json` changes without restarting the backend. | 🟡 Medium | Medium |

---

## 💾 Database & Memory

### Current State
`database.py` (909 lines) combines Turbovec, SQLite (WAL), MongoDB, embedding generation, and user profile management in a single file.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Split `database.py` into modules** — create `db_sqlite.py`, `db_mongo.py`, `db_vector.py`, `db_profiles.py`. A 909-line file mixing 4 databases is a maintenance risk. | 🔴 High | Medium |
| 2 | **Database migration framework** — use `alembic` for SQLite schema versioning so column additions and renames are tracked and auto-applied on upgrade. | 🔴 High | Medium |
| 3 | **Conversation pruning** — add auto-archiving of older conversation turns to `conversations_archive` to prevent unbounded table growth. | 🟡 Medium | Low |
| 4 | **Semantic cache TTL** — add a `ttl_hours` column to the semantic cache and invalidate stale entries automatically. | 🟡 Medium | Low |
| 5 | **Vector index health check** — background checksum validation for Turbovec `.tq` files to detect corruption before silent bad search results. | 🔴 High | Low |
| 6 | **PostgreSQL backend option** — allow swapping SQLite for PostgreSQL via a `DB_BACKEND=postgres` env option, using the existing `sqlalchemy` dependency. | 🟢 Low | High |
| 7 | **User profile schema validation** — define a `UserProfile` `TypedDict` and validate on every `save_user_profile` write. | 🟡 Medium | Low |

---

## ⚙️ Scheduler & Resource Governor

### Current State
APScheduler with SQLite jobstore. The Resource Governor throttles above 85% CPU or when heavy apps are in foreground.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **GPU utilization check** — add `pynvml` / `py3nvml` for NVIDIA GPU load polling. CPU-only checks miss GPU-heavy gaming scenarios. | 🟡 Medium | Low |
| 2 | **Thermal throttling** — check CPU temperature via WMI on Windows and throttle when thermally constrained. | 🟢 Low | Medium |
| 3 | **Job priority levels** — add `priority: high/normal/low` to `schedule_task` so urgent jobs preempt background ones. | 🟡 Medium | Low |
| 4 | **Missed job UI notifications** — surface missed-while-offline job notifications in the frontend so users know what was skipped. | 🟡 Medium | Low |
| 5 | **Configurable throttle threshold** — make the 85% CPU cutoff configurable in Settings instead of hardcoded. | 🟢 Low | Low |

---

## 🌐 Bridges (Telegram / Discord)

### Current State
`telegram_bridge.py` uses long-polling. `discord_bridge.py` uses `discord.py`. Both run in daemon threads.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Telegram webhook mode** — replace long-polling with webhook mode via a configurable public URL. Lower latency and more reliable. | 🟢 Low | Medium |
| 2 | **Message rate limiting** — add a per-user token bucket to both bridges. Currently any user can flood the ReAct loop. | 🔴 High | Low |
| 3 | **Bot command registry** — define explicit slash commands (`/status`, `/cancel`, `/help`) instead of routing all free-form text through NLP. | 🟡 Medium | Low |
| 4 | **Response chunking** — Telegram has a 4096-char message limit. Split long agent responses with continuation markers. | 🔴 High | Low |
| 5 | **Discord embed formatting** — format agent responses as Discord embeds with tool call fields and status indicators. | 🟢 Low | Medium |
| 6 | **Slack bridge** — add `slack_bridge.py` using `slack_bolt` to extend to Slack workspaces. | 🟢 Low | Medium |

---

## 🧪 Testing & Quality Assurance

### Current State
Only `tests/test_document_tools.py` exists. No CI pipeline is configured.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Backend unit test suite** — add `pytest` tests for all core modules: `test_loop.py`, `test_database.py`, `test_vault.py`, `test_p2p.py`, `test_scheduler.py`, `test_proactive.py`. | 🔴 High | High |
| 2 | **Agent loop integration tests** — mock Ollama responses via `unittest.mock` and verify correct tool dispatch and `<finish>` JSON output. | 🔴 High | High |
| 3 | **Frontend component tests** — add `vitest` + `@testing-library/react` for `Timeline`, `Settings`, and `Mascot` components. | 🟡 Medium | High |
| 4 | **E2E tests with Playwright** — automate the startup flow using Playwright's Python API (already a dependency). | 🟡 Medium | High |
| 5 | **CI/CD pipeline** — add `.github/workflows/ci.yml` running `pytest` on every push and PR. | 🔴 High | Low |
| 6 | **Coverage reports** — integrate `pytest-cov` with a minimum threshold (e.g. 60%) to prevent regression. | 🟡 Medium | Low |
| 7 | **Fuzz testing for tool input parsing** — fuzz the LLM output parser with malformed JSON to catch edge cases. | 🟢 Low | Medium |

---

## 📦 Build, Packaging & DevOps

### Current State
`build_standalone.py` handles PyInstaller packaging. NSIS and MSI installers via Tauri build.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Pin all dependency versions** — `requirements.txt` is mostly unpinned. Run `pip freeze > requirements.lock` and commit it to prevent silent upstream breakage. | 🔴 High | Low |
| 2 | **Docker Compose dev environment** — `docker-compose.yml` with Python backend + MongoDB + mock Ollama stub for GPU-free local development. | 🟡 Medium | Medium |
| 3 | **`pyproject.toml` migration** — migrate from `requirements.txt` to PEP 517/518 `pyproject.toml` with `uv` for reproducible builds. | 🟢 Low | Medium |
| 4 | **Auto-update mechanism** — background checker polling the GitHub releases API with a one-click update trigger in the UI. | 🟡 Medium | High |
| 5 | **Startup time profiling** — instrument the `api.py` startup sequence to identify slow synchronous imports. Lazy-load non-critical modules. | 🟡 Medium | Low |
| 6 | **Linux / macOS compatibility layer** — audit all `pywin32`, `win32api`, and WMI calls and add conditional import fallbacks. | 🟢 Low | High |

---

## 📊 Observability & Logging

### Current State
`logging_config.py` configures standard Python logging. `audit_logger.py` handles sensitive events.

### Improvements

| # | Improvement | Priority | Effort |
|---|---|---|---|
| 1 | **Structured JSON logging** — replace plain-text log lines with structured JSON (`python-json-logger`) for Grafana Loki / Datadog ingestion. | 🟡 Medium | Low |
| 2 | **Log rotation** — add `RotatingFileHandler` to `app_stdout.log` and `app_stderr.log` to prevent unbounded growth. | 🔴 High | Low |
| 3 | **Prometheus metrics endpoint** — expose `/api/metrics` with counters for tool call counts, loop iterations, model latency, cache hit rate, and active P2P peers. | 🟡 Medium | Medium |
| 4 | **Opt-in error telemetry** — optional anonymous error reporting to a self-hosted Sentry instance for catching bugs users never report. | 🟢 Low | Medium |
| 5 | **Agent replay from logs** — a `replay_session(session_id)` tool that re-runs a saved conversation's tool calls deterministically for debugging. | 🟢 Low | High |

---

## 🆕 New Features to Add

These are net-new capabilities not currently present in any form.

| # | Feature | Description | Priority |
|---|---|---|---|
| 1 | **Habit & Productivity Tracker** | Monitor daily coding patterns from the proactive engine. Surface weekly summaries ("You coded 4.2h/day on average, peak focus at 10–12 AM"). | 🟡 Medium |
| 2 | **Auto-generated Project Wiki** | Analyze a codebase and auto-generate `WIKI.md` with architecture diagrams, module summaries, and API docs using `doc_generator.py`. | 🟡 Medium |
| 3 | **Ambient Sound Mode** | Play lofi/focus audio via the TTS subsystem; pause automatically on wake word detection. | 🟢 Low |
| 4 | **Smart Clipboard Pipeline** | Auto-summarize copied URLs; proactively offer fixes when copied code contains a syntax error — extending the existing clipboard monitor. | 🔴 High |
| 5 | **Goal Decomposition & Tracking** | A "Goals" panel in the frontend. Meridian breaks high-level objectives into sub-tasks, tracks progress, and sends reminders. | 🟡 Medium |
| 6 | **Local Fine-tune Dataset Builder** | UI panel (Settings) to review, rate, and curate exported conversations for RLHF fine-tuning. `export_finetune_data` already provides the data. | 🟢 Low |
| 7 | **Git Commit Autopilot** | When watched files are saved, auto-generate a conventional commit message from the diff. User approves before committing. | 🟡 Medium |
| 8 | **Multi-monitor Mascot** | Mascot follows the active window across monitors. Currently fixed to one screen. | 🟢 Low |
| 9 | **Calendar Integration** | Connect to Google Calendar or Outlook via OAuth. Surface upcoming meetings as proactive nudges and block inference during them. | 🟡 Medium |
| 10 | **Voice Command Macros** | User-defined wake phrases (e.g. "Hey Meridian, deploy") that map to fixed goal strings, bypassing full NLP for frequent commands. | 🟡 Medium |
| 11 | **Side-by-side Code Review Panel** | Dedicated frontend panel showing original file, AI suggestion, and three-way merge editor. More structured than the ad-hoc diff in Timeline. | 🟡 Medium |
| 12 | **Workspace Snapshot & Restore** | Save and restore workspace state (open files, agent memory, active tasks) for switching between projects. | 🟢 Low |
| 13 | **API Server Mode** | Authenticated REST API exposing the agent so local apps (e.g. a VS Code extension) can submit goals and receive streamed results headlessly. | 🟡 Medium |
| 14 | **Cross-device Sync via Cloud Relay** | Optional self-hostable encrypted relay FastAPI instance for cross-network sync beyond LAN P2P. | 🟢 Low |
| 15 | **Plugin Marketplace UI** | "Store" tab in Settings showing community plugins from a GitHub index with one-click install and hot-reload. | 🟢 Low |

---

## Priority Summary

```
🔴 High Priority  (address soon, clear impact)
   - loop.py splitting, token budget tracking, tool result tagging
   - Vault audit logging, passphrase caching
   - P2P peer persistence, conflict resolution
   - VAD integration for voice, noise gate
   - Code block copy button, Mascot.tsx splitting
   - requirements.txt pinning, log rotation
   - URL ingestion tool, Smart Clipboard Pipeline
   - Rate-limiting on bridges, response chunking
   - Backend unit test suite + CI/CD pipeline

🟡 Medium Priority (schedule for next sprints)
   - Plugin manifest format, hot-reload watcher
   - Semantic cache TTL, database.py splitting
   - Streaming Whisper, TTS engine selection
   - Conversation search, dark/light theme toggle
   - Habit tracker, Git commit autopilot, Calendar integration

🟢 Low Priority (future roadmap)
   - WebRTC P2P, Argon2id vault, GPU/thermal throttling
   - Plugin marketplace, Slack bridge
   - Ambient sound mode, multi-monitor mascot
   - Fine-tune dataset UI, workspace snapshots
```

---

*Last updated: 2026-07-21 | Analyzed by: Antigravity AI | Project: Meridian-X v0.2.0*
