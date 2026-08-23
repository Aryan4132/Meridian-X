# SPEC: Meridian-X Day 1 & Core Expansion

## Objective

Implement **Day 1 features (OPT-01, PL-30)** and **JARVIS-02 through JARVIS-11** intelligence modules in Meridian-X.

## Core Modules & Requirements

### 0. Day 1 — Foundation & Performance Boost

- **`OPT-01` Frontend RAM & Performance Engine** (`useMemoryOptimizer.ts`, `Settings.tsx`, `index.css`):
  - Inactive tab unmounting/suspension.
  - Virtualized list helper & Blob URL auto-GC.
  - Low-RAM CSS toggle (<45MB RAM target).
- **`PL-30` Geo-Location & Spatial Context Engine** (`geo_location.py`, `web.py`, `registry.py`):
  - IP/OS location resolver with caching and fallback.
  - Spatial query biasing for search.
  - Localized weather briefing engine.

### 1. Eye-Tracking & Gaze Control (`JARVIS-02` in `gaze_tracker.py`)

- MediaPipe Iris tracking for window selection & gaze-based screen dimming.

### 2. Voice Biometrics (`JARVIS-03` in `voice_biometrics.py`)

- Voiceprint speaker verification protecting voice command execution.

### 3. Predictive Pre-Execution (`JARVIS-04` in `predictive_engine.py`)

- Habit model pre-warming LLM context & dev environments.

### 4. Smart Camera & RTSP Vision (`JARVIS-05` in `camera_sentinel.py`)

- RTSP security camera vision processing & object detection alerts.

### 5. Room Arrival Auto-Briefing (`JARVIS-06` in `presence_briefing.py`)

- Presence-triggered 15-second executive voice briefing.

### 6. Self-Healing System Defense (`JARVIS-07` in `system_defense.py`)

- Thermal governor, rogue process killer, & automated threat port isolation.

### 7. AR Smart Glasses Bridge (`JARVIS-08` in `ar_bridge.py`)

- WebSockets HUD streaming for AR smart glasses & headsets.

### 8. Subconscious Codebase Memory (`JARVIS-09` in `neural_rag.py`)

- Background AST semantic synthesizer & neural project intent graph.

### 9. Multi-Lingual Polyglot (`JARVIS-10` in `polyglot.py`)

- 50+ language real-time speech-to-code translator.

### 10. Autonomous PR & Test Generator (`JARVIS-11` in `auto_reviewer.py`)

- Automated unit test generator & pre-commit code reviewer.

### 11. OAuth 2.0 & External Service Integration Engine (`SEC-25`, `SEC-26` in `oauth_manager.py` & `external_connectors.py`)

- Hybrid auth mode (JWT Bearer tokens + API key support).
- OAuth 2.0 & OIDC PKCE authorization flow for login and remote connections.
- Encrypted provider token vault integration (`vault.py`) for third-party OAuth access.
- Background OAuth Token Auto-Rotator (`SEC-26`) proactively refreshing expiring tokens.
- External service connectors for Meridian-X tools: Google Workspace (Gmail, Calendar, Contacts), GitHub (Repos/PRs), Cloudflare (DNS/Domains), Chat Apps (Slack, Discord, Telegram), Workspace Sync (Notion, Airtable).

### 12. n8n-Style Workflow Automation Engine (`WKF-01`, `WKF-02`, `WKF-03`, `WKF-04` in `workflow_engine.py`)

- Event-driven node pipeline runner (Triggers $\rightarrow$ Filters $\rightarrow$ External Service Actions $\rightarrow$ LLM steps).
- Webhook Ingress Gateway (`WKF-02`) for external trigger HTTP POSTs.
- Built-in triggers (Webhook, Cron/Schedule, Event bus).
- Visual node graph builder (`WorkflowBuilder.tsx`) & execution monitoring log panel (`WKF-04`).

### 13. Day 4 — Execution Controls, Model Auditor & Auto PR Reviewer (`PL-07`, `PL-23`, `PL-24`, `PL-25`, `PL-26`, `JARVIS-11`)

- **`PL-07` — Unified LLM Provider Code Auditor** (`review.py`): Dynamic LLM provider routing via `llm_provider.py` replacing hardcoded Ollama client calls.
- **`PL-23` — User-Selected Model for Task Decomposition & Loop Helpers** (`loop.py`): Internal planning, decomposition, and reasoning helpers dynamically bind to user's selected `brain_model` and execution mode.
- **`PL-24` — Frontend Dynamic Model Source Lookup & LocalStorage Setter** (`Timeline.tsx`, `Mascot.tsx`): Model source resolution from `localStorage` (`meridian_model_source`, `meridian_brain_model`, `meridian_llm_provider`).
- **`PL-25` — Settings Page Execution Mode Toggle** (`Settings.tsx`): Explicit UI switch for `Local` (Ollama) vs `Cloud/API` (OpenAI, OpenRouter, Gemini, Anthropic, DeepSeek, etc.) execution mode.
- **`PL-26` — Backend API Settings & Model Source Synchronization** (`api.py`): Persist `MERIDIAN_MODEL_SOURCE` (`local` vs `cloud`) in profile DB and sync with ReAct stream handler and user profile endpoints.
- **`JARVIS-11` — Autonomous PR Reviewer & Automated Unit Test Generator** (`auto_reviewer.py`): Tool for unit test generation (pytest/jest) for unstaged git diffs & pre-commit automated code review feedback.

### 14. Day 5 — Full-Duplex Voice, Biometrics & Conversation Window (`AST-15`, `AST-08`, `JARVIS-03`)

- **`AST-15` — Full-Duplex Voice & Live Voice Interrupt** (`duplex.py`, `api.py`): Real-time streaming voice session with low-latency (50ms window) VAD barge-in speech interruption mid-sentence.
- **Voice Response Toggle & Speed Optimization** (`duplex.py`, `api.py`): Configurable voice response state (`voice_response_enabled`) with enable/disable API endpoints and ultra-fast non-blocking stream delivery.
- **`AST-08` — Continuous Conversation Window** (`wakeword.py`, `api.py`): 10-second active listening window following responses for follow-up speech without wake word, exposed via REST endpoints.
- **`JARVIS-03` — Voice Biometric Identity & Speaker Verification** (`voice_biometrics.py`, `api.py`): Voiceprint embedding matcher blocking unauthorized background voice commands with cosine similarity verification.

### 15. Day 6 — Codebase AST Graph, Neural RAG & PaperCoder (`DEV-05`, `JARVIS-09`, `DEV-04`)
- **`DEV-05` — Tree-Sitter Offline Codebase AST Graph** (`code_graph.py`): AST dependency graph visualizer, symbol search, caller/callee tracing, & instant impact analysis.
- **`JARVIS-09` — Subconscious Codebase Memory & Neural RAG Synthesizer** (`neural_rag.py`): Background AST semantic synthesizer building real-time project intent knowledge graphs.
- **`DEV-04` — Paper2Code (PaperCoder) Integration** (`papercoder.py`, `registry.py`): 3-stage paper-to-repository multi-agent generator converting arXiv/PDFs into runnable code repos.

### 16. Multi-OS Support & Full Codebase Audit (`CROSS-01` through `CROSS-12`)
- Cross-Platform Parity for Windows, macOS, and Linux.
- Eliminate module-level Windows-only import crashes (`winreg`, `os.startfile`, `psutil.win_service_iter`).
- Generalize executable path resolution across platforms (`Scripts` vs `bin`).
- Add platform-native task scheduling, active window tracking, fullscreen game mode detection, and hardware capabilities detection (Apple Silicon unified memory, AMD ROCm).
- Generalize shell command execution (`monitor_process`, `ping`, `open_app`, `open_file`).

### 17. Butler AI & Media Automation Engine (`BUTLER-01` in `media_player.py`, `chrome_manager.py`, `database.py`)
- **Butler Account & Preferences Memory**: Store persistent user account rules (e.g., `media_account_email`: `aryanshukla4132@gmail.com`, default streaming platforms) in SQLite/MongoDB profile memory with `save_user_preference` and `get_user_preference` API.
- **Chrome Persistent User Data Profile Bridge**: Launch Chrome browser using local Chrome User Data directory (`%LOCALAPPDATA%\Google\Chrome\User Data`) or persistent Playwright context (`meridian_memory/chrome_profile`) so logged-in Google accounts (`aryanshukla4132@gmail.com`) stay authenticated.
- **YouTube Music Playback Automation**: Dedicated `play_youtube_music(song_query: str, account_email: Optional[str] = None)` tool to search YT Music (`https://music.youtube.com/search?q=...`), select the track, trigger playback in non-headless Chrome window, and manage media controls (play/pause/skip).
- **Butler Visual Verification & Auto-Retry Loop**: Closed-loop verification (`verify_media_playing` / `screenshot` + `vision_analyze` / `ocr_screen`) that takes a screenshot after executing open/play actions. If the target track/media is not actively playing, automatically retry by clicking the top song result play button or executing fallback hotkeys until verified.

## Verification Strategy

- Pytest test suite for backend modules (`test_geo_location.py`, `test_oauth.py`, `test_day4_features.py`, `test_day5_features.py`, `test_day6_features.py`, `test_multi_os.py`, `test_butler_media.py`).
- Frontend build check (`npm run build`).

## Success Criteria

- [ ] Day 1 modules (OPT-01 and PL-30) implemented and passing unit tests.
- [ ] All JARVIS intelligence modules pass unit test verification.
- [ ] OAuth 2.0 connection engine passes unit tests (`test_oauth.py`) and maintains backwards compatibility with API key auth.
- [ ] Day 4 execution controls, model auditor, model source toggle, and autonomous PR reviewer pass unit test suite.
- [ ] Day 5 full-duplex voice, continuous window, voice response toggle, and biometrics pass unit test suite (`test_day5_features.py`).
- [ ] Day 6 AST code graph, Neural RAG intent synthesizer, and PaperCoder paper-to-code tool pass unit test suite (`test_day6_features.py`).
- [ ] Multi-OS cross-platform unit test suite (`test_multi_os.py`) passes 100% on Windows, macOS, and Linux.
- [ ] BUTLER-01 persistent Chrome account profile, YouTube Music automation tool, and preference memory pass unit tests (`test_butler_media.py`).


