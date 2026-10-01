# SPEC: Meridian-X Advanced Core Features

## Objective

Implement core enterprise-grade agent capabilities in Meridian-X:

1. **Local Model Management with Quantization Options**: Local LLM management supporting model discovery, quantization tag selection (`Q4_K_M`, `Q4_0`, `Q5_K_M`, `Q8_0`, `F16`), pull progress streaming, active local model switching, and hardware resource estimation.
2. **Conversation Summarization and Memory Consolidation API**: Automatic and on-demand conversation summarization, semantic memory node extraction, graph memory consolidation, and status tracking.
3. **Desktop Automation Endpoints for Common Dev Tasks**: REST APIs for developer task automation including git repository status checks, code formatting, running unit tests, project builds, and dev server lifecycle management.
4. **Real-Time Agent Status and Activity Stream**: WebSocket/REST real-time activity streaming for agent state transitions (idle, thinking, executing_tool, verifying, error), subagent status, and live activity logs.
5. **Standalone Resilient Bridge Architecture**: Decouple Mobile WebSocket Bridge, Telegram Bot, and Discord Bot into independent, zero-crash background daemons on port 4133 so mobile companion app and bot connections stay alive when `api.exe` closes, restarts, or crashes.
6. **Expanded Design System & Custom Theme Engine**: Add Tokyo Night Minimalist, Pure OLED Black, and VS Code Dark Pro themes, along with dynamic custom accent color overrides.
7. **Primary Autonomous Web Browser Engine**: Default agent browsing and research workflows to `BrowserUseAgent` (`browser_use_task`), utilizing Set-of-Marks visual DOM indexing and multi-step reasoning.
8. **Retire Butler Music Player Tool**: Remove `play_youtube_music` and `verify_media_playing` from tool registry, routing general media hotkey actions strictly through `src.tools.system.control_media_playback`.
9. **Best-in-Class Tool Consolidation**: Where multiple duplicate or overlapping tools exist across browser automation, code reviews, notifications, scheduling, clipboard, and search, standardize and route all calls to the best-performing, most resilient implementation.

## Tech Stack

- **Backend**: Python 3.10+, FastAPI, AsyncIO, Pytest, Pydantic, HTTPX, SQLite / Graph Memory
- **Frontend**: React 19, TypeScript, Vite, Tailwind CSS v4 + Glassmorphism UI tokens, WebSocket API

## Commands

- **Backend Tests**: `pytest meridian_backend/tests/test_new_features.py`
- **Frontend Build**: `npm --prefix meridian_frontend run build`
- **Frontend Typecheck**: `npx --prefix meridian_frontend tsc --noEmit`

## Project Structure

```text
meridian_backend/
  src/core/
    local_model_manager.py     # Local model registry & quantization engine
    memory_consolidation.py    # Conversation summarizer & memory node consolidator
    dev_automation.py          # Developer desktop task automation engine
    agent_status_stream.py     # Real-time event bus & activity stream
  api.py                       # FastAPI endpoint routes
  tests/
    test_new_features.py       # Comprehensive pytest suite
meridian_frontend/
    src/components/
      LocalModelManager.tsx    # Quantization & local model management UI
      MemoryConsolidationView.tsx # Memory summarization & consolidation UI
      DevAutomationPanel.tsx   # Developer automation quick task widget
      AgentStatusStream.tsx    # Real-time agent status & activity stream panel
```

## Code Style

- Strictly typed Python dataclasses & Pydantic models.
- Modular FastAPI router handlers with standard HTTP error codes.
- React components using custom hooks, clean visual dark mode aesthetics, frosted glass cards, and status indicators.

## Testing Strategy

- **Unit & Integration Tests**: Pytest tests targeting model manager, summarizer/consolidation logic, dev automation endpoints, and WebSocket activity broadcaster.
- **Frontend Verification**: TypeScript type checking via `tsc --noEmit`.

## Boundaries

- **Always**: Validate input parameters, handle subprocess timeouts gracefully, stream long-running actions.
- **Ask first**: System-level destructive actions or deleting non-temporary model files.
- **Never**: Block main FastAPI event loop, expose unvalidated shell injection vulnerabilities.

## Success Criteria

- [ ] Endpoints for local model listing, quantization options, model pulling, and active model selection work without errors.
- [ ] Summarization API compresses chat logs into memory nodes and updates long-term storage.
- [ ] Dev automation endpoints execute git status, code formatting, test runs, and build tasks cleanly.
- [ ] WebSocket `/ws/agent-status` streams real-time agent execution events to UI.
- [ ] UI components render cleanly with rich visual aesthetics and pass TypeScript checks.

---

## Sub-Spec: Meridian-X Flutter Mobile App Builder

### Objective: Mobile App Builder

Provide automated, cross-platform build script (`build_mobile.py` and `meridian_mobile/build_apk.py`) for Meridian-X Flutter mobile application:

- Auto-detect Android SDK (`LOCALAPPDATA\Android\Sdk`), compatible JDK 17 (`C:\Program Files\Eclipse Adoptium\jdk-17.0.20.8-hotspot` or standard paths), and Flutter toolchain.
- Verify environment, auto-accept SDK licenses, run pub get & flutter tests.
- Compile release APK (`flutter build apk --release`), copy artifact to `executables/meridian-x_mobile.apk`, calculate SHA-256 and package size.
- Support CLI arguments (`--apk`, `--windows`, `--web`, `--clean`).

### Commands: Mobile App Builder

- Run Flutter App Builder: `python build_mobile.py` (or `python meridian_mobile/build_apk.py`)
- Run Flutter App in Debug: `flutter run -d windows` or `flutter run -d chrome` in `meridian_mobile`
- Flutter Test Suite: `flutter test` in `meridian_mobile`

### Boundaries: Mobile App Builder

- Do not modify existing user configs or corrupt git status.
- Ensure built binaries output cleanly into `executables/` directory.

---

## Sub-Spec: Browser-Use Autonomous Web Automation Engine

### Objective: Autonomous Web Automation

Provide a robust, visible, and autonomous web browsing capability inspired by Browser-Use:

1. **Autonomous Web Agent (`browser_use_task`)**: Executes multi-step browser tasks from natural language goals (e.g., search, click links, fill forms, press enter, extract data) in an autonomous loop.
2. **Visible Browser Window by Default**: Default to `visible=True` with user profile support so users can watch the agent operate live in their browser.
3. **Set-of-Marks Visual & DOM Indexing**:
   - Injects visual element badges `[1]`, `[2]`, `[3]` onto interactable elements (buttons, inputs, links, select menus) currently in viewport.
   - Generates element map: `{1: {tag, text, selector, coords}}`.
   - Supports direct index actions: `click(index)`, `type(index, text, press_enter=True)`.
4. **Resilient Session Management**: Auto-initialize/re-open browser sessions if closed or stale whenever a browser tool is invoked.
5. **Complete Action Toolkit**: Support navigation, index-based and selector-based clicking, typing, pressing special keys (`Enter`, `Tab`, `Escape`), scrolling (`up`, `down`), waiting, and extracting structured DOM/interactive elements.
6. **Tool Registry & LLM Signatures**: Document parameter signatures in `tools_doc` so local and cloud LLMs know exactly how to invoke browser tools with proper arguments.

### Commands: Autonomous Web Automation

- Backend Browser Tests: `pytest meridian_backend/tests/test_browser_use.py meridian_backend/tests/test_browser_agent.py`

---

## Sub-Spec: Browser Engine Resilience, Tool Schema Tolerance & Provider Auto-Recovery

### Objective: Browser Engine Resilience

Fix runtime failures in autonomous web automation, tool execution, and consensus debate:

1. **Playwright Multi-Tier Engine Fallback**: In standalone/frozen and standard environments, prevent missing Chromium executable crashes by auto-configuring `PLAYWRIGHT_BROWSERS_PATH` and falling back through Playwright Chromium -> System Google Chrome (`channel="chrome"`) -> System Microsoft Edge (`channel="msedge"`) -> explicit executable path.
2. **Persistent Context Resilience**: Handle missing binaries when `profile=True` by falling back to system Chrome/Edge channels.
3. **Autonomous Browser-Use Auto-Recovery**: Ensure `BrowserUseAgent.run()` gracefully recovers and retries browser launch if the default engine fails.
4. **Tool Schema Tolerance in `nl_run`**: Accept `command` / `cmd` parameter aliases in addition to `natural_language` to eliminate signature validation rejections.
5. **Provider Resolution & Consensus Debate Guard**: Prevent fallback to unconfigured OpenRouter in `call_llm` by respecting `MERIDIAN_PROVIDER` / available keys (Gemini, DeepSeek, Groq, Ollama), and ignore error strings in consensus debate critiques.

---

## Sub-Spec: Proactive Cognitive Mode & Autonomous Suggestions in Meridian Agent Loop

### Objective: Proactive Cognitive Mode

Enable proactive autonomous intelligence in the Meridian Agent loop and cognitive modes (`mode.py`, `loop.py`, `loop_parser.py`):

1. **Dedicated PROACTIVE Cognitive Mode**: A first-class mode in `MODE_DIRECTIVES` directing the agent to anticipate unstated user requirements, identify system/project optimization opportunities, and formulate actionable next steps.
2. **Dynamic Trigger & Preference Support**: Add heuristic keyword triggers in `classify_mode()` to detect proactive requests ("proactive", "suggest", "what next", "what should i do", "anticipate", "autonomous", "butler", "take initiative", "proactive mode", etc.), plus `get_proactive_mode()` and `set_proactive_mode(enabled: bool)` to elevate default `AUTO` mode into `PROACTIVE`.
3. **Structured Proactive Suggestions Protocol**: Extend `<finish>` protocol schema in `SYSTEM_PROMPT_TEMPLATE` with optional `proactive_suggestions` (list of objects containing `title`, `action`, `type`), parsed and validated in `process_final_response()`.
4. **Agent Loop Event Dispatch**: In `loop.py`, when proactive suggestions are parsed from the finish response, dispatch them via `event_bus` / `publish_nudge_sync` and stream an SSE `proactive_suggestion` event so client interfaces can render instant action prompts.

### Commands: Proactive Cognitive Mode

- **Unit & Integration Tests**: `pytest meridian_backend/tests/test_proactive_mode.py`
- **Full Backend Regression Suite**: `pytest meridian_backend/tests/test_proactive.py meridian_backend/tests/test_tool_regression.py`

---

## Sub-Spec: Full Meridian-X Proactive Intelligence Suite

### Objective: Proactive Intelligence Suite

Implement end-to-end proactive automation across 6 key subsystems:

1. **Room Arrival & Presence Briefing**: Connect user return detection (>5 min away) and camera presence events to `PresenceBriefingEngine.generate_presence_briefing()`, dispatching voice executive briefings.
2. **Developer Commit & Breakage Guardian**:
   - `CommitWhisperer`: Detect uncommitted staged changes or successful test runs and proactively push semantic commit recommendations.
   - `WhatBrokeDetective`: Proactively diagnose build/test breakage and dispatch auto-fix patch suggestions.
3. **Predictive Context Pre-Warmer**: Enhance `predictive_engine.py` to pre-warm git diffs, RAG chunks, and AST summaries upon developer app switches.
4. **Ambient Butler & Focus Automation**: Proactively track continuous active work duration and push Pomodoro / ergonomic stretch nudges at 45 min intervals; auto-manage focus mode.
5. **Self-Evolving Tool Synthesizer**: Sequence pattern detector in `self_evolving_tooling.py` that discovers recurring tool sequences and proactively proposes synthesizing compound macro tools.
6. **Continuous Tool Regression Sentinel**: Sentinel in `tool_regression_sentinel.py` continuously validating `tests/tool_scenarios.yaml` against the registry and alerting on tool routing regressions.

### Commands: Proactive Intelligence Suite

- **Suite Tests**: `pytest meridian_backend/tests/test_full_proactive_suite.py`
- **Full Backend Regression Suite**: `pytest meridian_backend/tests/test_proactive.py meridian_backend/tests/test_proactive_mode.py meridian_backend/tests/test_tool_regression.py`

### Boundaries: Proactive Intelligence Suite

- Zero disruption: All background monitors must be non-blocking and catch all exceptions gracefully.
- Rate-limiting: Every proactive notification must strictly obey its debounce and cooldown timers to prevent spam.

---

## Sub-Spec: Advanced Proactive Automation & Reactive UI Suite

### Objective: Advanced Proactive Automation

Implement Phase 2 proactive capabilities across workspace watching, mobile bridge, autonomous memory, resource healing, and frontend action execution:

1. **Active Workspace Watcher & Ghost Assistant**: Real-time file change scanner in `watcher.py` & `silent_workflow_guardian.py` that immediately flags syntax errors, stray debug logs (`print(DEBUG...)`, `console.log`), and route mismatches on file save with ghost toasts.
2. **Proactive Mobile Away-Bridge**: In `mobile_bridge.py`, automatically broadcast proactive nudges, task completions, and action prompts to paired mobile companions when the user is away from desktop (`idle_seconds >= 300`).
3. **Milestone Autonomous Memory Consolidator**: Automatically trigger background semantic memory consolidation every 5-8 conversation turns in `memory_consolidation.py` / `proactive.py` to keep knowledge graphs fresh without waiting for idle sleep cycles.
4. **Proactive Resource Auto-Healer**: In `proactive_system_guard.py`, detect rogue runaway processes (>2GB memory hogs, zombie loops) and low disk space; dispatch 1-click remediation action cards (`resource_auto_heal`).

---

## Sub-Spec: Comprehensive UI/UX, Typography, and Fluid Ergonomics Overhaul

### Objective: UI/UX & Ergonomics Overhaul

Elevate Meridian-X UI/UX to a world-class, premium developer HUD standard:

1. **Typography & Readability**: Replace the harsh global monospace font for body copy, buttons, inputs, and prose with modern, balanced proportional typography (`Inter`, `Outfit`, `DM Sans`). Retain crisp monospace (`JetBrains Mono`, `IBM Plex Mono`) specifically for code blocks, terminal lines, system timestamps, and status chips.
2. **Smooth Tab Transitions & Layout Space**: Upgrade view switches in `Shell.tsx` from instant `display: none` to smooth, fluid `AnimatePresence` crossfades. Optimize container width and responsive padding so large 1080p/1440p displays feel cohesive and purposeful rather than empty or disjointed.
3. **Timeline & Prompt Ergonomics**:
   - Welcome Hero & Quick Starter Chips: When conversation is fresh, display interactive prompt suggestion chips ("Audit Git Changes", "Review Codebase", "Run Dev Health Check", "Start Focus Sprint") that populate the input instantly.
   - Luxury Floating Input HUD: Auto-growing input box with backdrop blur, glowing focus ring, keyboard hints (`Ctrl+K` for Palette, `Enter` to send, `Shift+Enter` for multiline), and clear status badges.
   - Polish chat bubbles, fix thinking cursor animation syntax typo in `Timeline.tsx`.
4. **Tactile Micro-Interactions & Glassmorphism**: Add responsive micro-physics to buttons (`whileTap={{ scale: 0.96 }}`), improve contrast on borders (`0.10 - 0.15` opacity), and refine ambient glow depth across dark themes.

### Commands: UI/UX & Ergonomics Overhaul

- **Frontend Typecheck**: `npx --prefix meridian_frontend tsc --noEmit`
- **Frontend Build**: `npm --prefix meridian_frontend run build`

---

## Sub-Spec: Instant Agent Cancellation & Stop Interruption Pipeline

### Objective: Instant Cancellation Pipeline

Guarantee instant, deterministic cancellation when the user clicks the Stop/Interrupt button or disconnects:

1. **Frontend Abort Binding in `Timeline.tsx`**: Pass `signal: controller.signal` to `fetch('/api/chat/stream')`. When `handleInterrupt` is clicked, immediately abort HTTP stream, reset loading/streaming states, display a clear "⛔ Execution stopped by user" message, and dispatch both `/api/chat/abort` and `/api/voice/interrupt`.
2. **Backend Stream Cancellation & Client Disconnect in `api.py`**:
   - Add explicit `/api/chat/abort` and `/api/chat/stop` endpoints that call `interrupt_agent_loop()`.
   - Wrap `StreamingResponse` in `chat_stream` to catch `asyncio.CancelledError` and `GeneratorExit`, triggering `interrupt_agent_loop()` on browser disconnect.
3. **Pervasive Checkpoints in `src/core/loop.py` & `src/tools/browser_use_agent.py`**:
   - Check `_interrupt_event.is_set()` before dispatching tool calls, before each sequential tool execution, after each tool completion, and on each step of `BrowserUseAgent.run()`.
   - When detected, safely exit generator immediately without running remaining tool steps.

### Commands: Instant Cancellation Pipeline

- **Backend Tests**: `pytest meridian_backend/tests/test_advanced_proactive.py`
- **Frontend Build**: `npm --prefix meridian_frontend run build`

---

## Sub-Spec: Core Backend Architecture & Reliability Improvements

### Reliability Objectives

Resolve architecture, security, and testing gaps across core Meridian-X backend components:

1. **Tool Regression & Test Decoupling (`test_tool_regression.py` & `tool_regression_sentinel.py`)**:
   - Update `test_tool_regression.py` to test through `ToolRegressionSentinel` directly.
   - Support tool argument schema validation (`input_schema`) and registry checks against scenario expectations.
2. **Hardware Detection Optimization (`src/core/hardware_detector.py`)**:
   - Query exact `AdapterRAM` on Windows via CIM / PowerShell for accurate VRAM calculation instead of 50% RAM approximation.
   - Implement memoization/caching with TTL/LRU to prevent repeated expensive PowerShell process spawns.
3. **Configurable Workspace Orchestrator (`src/core/workspace_orchestrator.py`)**:
   - Add preset configuration schema supporting dynamic presets (`coding`, `research`, `debugging`, `focus`).
   - Add binary existence verification (`shutil.which`) before launching commands (`code`, `docker`).
   - Implement `stop_preset()` for teardown.
4. **Provider-Agnostic Browser Use Planning (`src/tools/browser_use_agent.py`)**:
   - Decouple `_plan_with_llm` from hardcoded Ollama client; utilize unified `call_llm` or configured provider from `llm_provider.py` with fallback.
   - Increase default planning timeout to 15s.
5. **Comprehensive Secret Redaction & Performance (`src/core/llm_provider.py`)**:
   - Expand regex patterns to detect and redact Anthropic (`sk-ant-`), Google Gemini (`AIzaSy`), and Hugging Face (`hf_`) keys.
   - Hoist `log_sensitive_action` import outside the inner match loop for performance.

### Reliability Commands

- **Backend Tests**: `pytest meridian_backend/tests/test_tool_regression.py meridian_backend/tests/test_backend_improvements.py -v`

---

## Sub-Spec: Unified Cognitive Graph Memory System

### Cognitive Graph Objectives

Replace siloed vector RAG with an interconnected, multi-hop SQLite Cognitive Graph that links code AST symbols, API routes, user memories, and task outcomes into a unified associative network:

1. **SQLite Graph Schema (`meridian_backend/src/core/cognitive_graph.py`)**:
   - `cognitive_nodes`: `id`, `type`, `name`, `metadata`, `created_at`, `updated_at`.
   - `cognitive_edges`: `id`, `source`, `target`, `relation`, `weight`, `timestamp`.
2. **Associative Multi-Hop Traversal**:
   - Breadth-first graph walk across connected nodes up to N hops.
   - Relation filtering (`calls`, `implements`, `imports`, `modifies`, `references`, `relates_to`).
3. **Automated Inter-System Linking**:
   - Link frontend endpoints to backend API routes.
   - Link user memories and task executions to affected project modules.
4. **Agent Integration & Prompt Context Injection**:
   - Expose `query_cognitive_graph` in `ToolRegistry`.
   - Inject graph-linked context blocks into `run_react_agent_loop`.

### Cognitive Graph Commands

- **Backend Tests**: `pytest meridian_backend/tests/test_cognitive_graph.py -v`

---

## Sub-Spec: Ultra-Low Latency & Anti-Chaos Voice I/O System

### Voice System Objectives

Drastically reduce voice roundtrip latency (<250ms TTFA output, <100ms input) and eliminate audio overlap/scrambling chaos:

1. **Voice Output (TTS) Optimization & Anti-Chaos Sequencing**:
   - **In-Memory Audio Streaming (`api.py`)**: Eliminate temp WAV disk file I/O in `/api/tts`; encode and stream directly from `io.BytesIO` in RAM.
   - **Sequenced Queue Player (`meridian_frontend/src/Mascot.tsx`)**:
     - Index chunks monotonically (`seq: 0, 1, 2...`). Fetch TTS in parallel but play back strictly in mathematical index sequence.
     - **Generation ID Locking**: Invalidate stale TTS promises on barge-in, new prompt, or interrupt so zombie audio never overlaps.
     - **Early Clause Chunking**: Trigger chunk 0 on first 3–5 words or clause mark (`,`, `;`, `:`) for instant sub-250ms TTFA.
     - **Strict Single-Track Audio Controller**: Clean up active `Audio` instance and revoke URLs on playback complete or cancel.

2. **Voice Input (STT) Acceleration**:
   - **Browser Web Speech API (`Mascot.tsx`)**: Real-time streaming transcription directly in browser for zero-delay speech recognition (<50ms).
   - **Faster Whisper Engine Tuning (`stt.py`)**: Default CPU fallback to `tiny.en` for 80ms inference; remove 8.0s timeout hang when speech is below threshold; add instant stop on key release (PTT).

### Voice System Commands

- **Backend Tests**: `pytest meridian_backend/tests/test_voice_speed.py -v`
- **Frontend Typecheck**: `npm --prefix meridian_frontend run build`

---

## Sub-Spec: Full-System Production Hardening, Anti-Chaos Audio & Cognitive Graph Overhaul

### Objectives

1. **System Guard & Security Immunity**:
   - Add critical system process protection whitelist to `ProactiveSystemGuard` (`os.getpid()`, parent PID, `explorer.exe`, `dwm.exe`, `csrss.exe`, `svchost.exe`, `python.exe` self) to prevent accidental OS shell or backend process termination.
   - Add 5-minute notification cooldown per PID in `ProactiveGuardBanner.tsx` to eliminate 15-second desktop notification spam.
   - Implement memory zeroization in `src/core/vault.py` when clearing derived key caches.

2. **Ultra-Low Latency Voice & Anti-Chaos Streamlining**:
   - Stream chunked clause TTS in `Timeline.tsx` Dashboard matching `Mascot.tsx` sequenced queue player (sub-250ms TTFA on first 3 words).
   - Implement `stop_active_tts()` with `threading.Event` + `sounddevice.stop()` in `src/voice/tts.py` and bind to `/api/voice/interrupt` and `/api/chat/abort`.
   - Ensure instant audio cutoff when user clicks Stop/Interrupt in `Timeline.tsx`.
   - Global `AudioCoordinator` bus to ensure Mascot and Timeline never play simultaneous conflicting audio tracks.

3. **Cognitive Graph Concurrency & Associative Search**:
   - Configure SQLite WAL mode (`PRAGMA journal_mode=WAL;`) and busy timeout in `cognitive_graph.py` to prevent database locks.
   - Implement FTS5 keyword indexing and temporal weight decay in `cognitive_graph.py`.

4. **Agent Reliability & Workspace Safety**:
   - Add automated git snapshot / rollback checkpoint in `src/core/loop.py` before task execution to enable instant 1-click recovery from failed tool steps.

### Hardening & Production Commands

- **Backend Tests**: `pytest meridian_backend/tests/test_voice_speed.py meridian_backend/tests/test_backend_improvements.py -v`
- **Frontend Typecheck & Build**: `npm --prefix meridian_frontend run build`

---

## Sub-Spec: Meridian-X Mobile APK & Companion Bridge Production Fix

### Objectives

1. **Android Manifest & Permissions**:
   - Add required Android permissions: `RECORD_AUDIO`, `CAMERA`, `MODIFY_AUDIO_SETTINGS`, `ACCESS_WIFI_STATE`, `VIBRATE`.
   - Specify `android:required="false"` on `android.hardware.camera`, `android.hardware.camera.autofocus`, and `android.hardware.microphone` so APK installs cleanly on all devices.
   - Add `res/xml/network_security_config.xml` to allow cleartext LAN and localhost WebSocket traffic on Android 9+ (API 28+).

2. **Resilient Network & WebSocket Connection**:
   - Normalize user entered URLs (auto-convert `http://` to `ws://`, `https://` to `wss://`, automatically append `/ws` if missing).
   - Robust query param preservation in `WebSocketClient` (prevent duplicate `?token=...` mangling).
   - Multi-target pairing support: auto-probe both port 4132 (FastAPI main) and 4133 (mobile bridge daemon) with clear error messaging.
   - Quick connection preset chips for Emulator (`ws://10.0.2.2:4132/ws`), Localhost, and LAN IP.

3. **Crash Prevention & Runtime Safety**:
   - Graceful fallback for audio amplitude visualizer, camera vision preview, and secure storage read exceptions.
   - Set Android `minSdk = 23` in `build.gradle.kts` for modern API compatibility.

4. **Production Build Pipeline**:
   - Execute clean build via `build_mobile.py` with tests verification.
   - Distribute signed/release APK to `executables/meridian-x_mobile.apk` with SHA-256 hash.

### Verification Commands
- **Flutter Tests**: `flutter test` in `meridian_mobile`
- **APK Build**: `python build_mobile.py --target apk`

---

## Sub-Spec: Ultra-Low Latency Voice Engine & Accurate Multilingual Language Triage

### Objectives
1. **Accurate Language Detection (Fix Hindi False Positives)**:
   - Purge English stopwords (`"hi"`, `"to"`, `"ab"`, `"se"`, `"ko"`, `"ki"`, `"ka"`, `"ke"`) from Hinglish keyword dictionary in `meridian_backend/src/core/mode.py`.
   - Prevent false `HINGLISH` triggering on common English greetings (`"Hi"`, `"Hi Meridian"`), prepositions (`"to"`), and short command phrases.
   - Require high-confidence multi-word Hinglish vocabulary or explicit Devanagari script for Hindi directives.
   - If user input is English, strictly enforce English directives with no transliteration.

2. **Ultra-Low Latency Speech Streaming**:
   - In `meridian_backend/src/core/loop_parser.py`: Skip `transliterate_to_devanagari` when language is `en`/`na` or when text is already in target script, saving 2-6s of LLM latency.
   - In `meridian_frontend/src/Mascot.tsx`: Fix `event: text` JSON block consumption so `speech`/`chat` text is immediately fed to chunked TTS instead of dropping chunks via early `continue`.
   - In `meridian_frontend/src/views/Timeline.tsx`: Stream and synthesize speech for final response blocks directly so TTS plays without delay.

---

## Sub-Spec: 10/10 Architecture & Performance Hardening

### Objectives
1. **Intelligent Consensus Debate Gate ([`consensus_engine.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/consensus_engine.py))**:
   - Decouple consensus debate from monolithic `loop.py` into `consensus_engine.py`.
   - Only trigger consensus debate when code mutations, filesystem alterations, or explicit multi-step problem solving occurred.
   - Bypass consensus debate for conversational voice turns, simple Q&A, and direct status checks to achieve sub-500ms voice response times.

2. **Unified Frontend Audio Engine ([`streamingAudioPlayer.ts`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/services/streamingAudioPlayer.ts))**:
   - Eliminate duplicated, buggy audio chunk queues in `Timeline.tsx` and `Mascot.tsx`.
   - Provide a shared, bulletproof `StreamingAudioPlayer` singleton with sequential chunk queuing, automatic volume control, fast URL revocation, and interruption handling (`stopAllAudio()`).

3. **Eliminate Silent Exception Swallowing**:
   - Replace bare `except Exception: pass` in RAG search, document indexing, and speech pipeline with explicit structured warnings via `logging.getLogger("meridian")`.

---

## Sub-Spec: Phase 2 God Files Refactoring (Zero Behavior Changes)

### Objectives
Split oversized backend modules (>1,000 lines) into modular subpackages with pure separation of concerns and strict backward-compatible re-exports:
1. **`proactive.py` (1,360 lines) -> `src/core/proactive/` package**:
   - `ergonomics.py`: Focus guardian, eye-strain (20-20-20), posture, hydration reminders.
   - `commits.py`: Git commit whisperer, workspace change tracker, daily/evening review digests.
   - `guard.py`: Background system monitoring, process immunity checks, memory leak detection.
   - `__init__.py`: Facade preserving all existing public functions, types, and patch targets (`publish_nudge_sync`, `synthesize_ambient_nudge`, `generate_meeting_prep_briefing`, `set_main_event_loop`, `record_user_activity`, etc.).
2. **`loop.py` (2,037 lines) -> Orchestrator (<400 lines)**:
   - `confirmations.py`: User approval gating, command risk classification, safety tier confirmation.
   - `llm_clients.py`: Model dispatch, provider routing, multi-model streaming token parsers.
   - `checkpoints.py`: Git snapshot state capture, rollback, checkpoint commit management.
   - `loop.py`: Lean ReAct loop orchestrator calling modular helpers while maintaining exact `run_react_agent_loop(...)` signature.
3. **`api.py` (4,427 lines) -> Modular FastAPI Routers (`meridian_backend/api/`)**:
   - `chat.py`: Chat execution, live SSE loop streaming (`/api/chat`, `/api/chat/stream`).
   - `voice.py`: Speech synthesis, transcription, duplex audio endpoints.
   - `rag.py`: Document ingestion, Turbovec search, graph sync.
   - `vault.py`: Secrets vault, credential rotation, AES encryption.
   - `scheduler.py`: Task scheduler, CRON triggers, workflow triggers.
   - `mcp.py`: Model Context Protocol server endpoints.
   - `system.py`: Process guard, system health, telemetry, diagnostics.
   - `api.py`: FastAPI application root mounting sub-routers via `app.include_router(...)`.

### Invariants & Boundaries
- **Always**: Preserve all public API paths, HTTP methods, status codes, and JSON schemas.
- **Always**: Preserve all function signatures and module-level re-exports so existing imports and pytest patches work transparently.
- **Never**: Alter runtime behavior, default parameters, or response payloads.

### Verification
- Backend pytest suite: `pytest meridian_backend/tests/` passes without regressions.
- Frontend build & typecheck: `npm --prefix meridian_frontend run build` and `npx --prefix meridian_frontend tsc --noEmit` pass cleanly.




