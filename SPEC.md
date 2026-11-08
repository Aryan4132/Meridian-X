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
10. **Local Model Stopping Tokens & Anti-Hallucination**: Stop sequences (`stop=["</call>", "</call:"]`) and context window settings (`num_ctx: 8192`) on Ollama stream calls to eliminate simulated observation hallucinations.
11. **Fast-Boot Lazy Daemon Lifecycles**: Guard wakeword audio listeners, P2P network threads, and clipboard monitors behind user preference toggles to achieve <1s backend boot time and <250MB idle RAM.
12. **Headless CI Resilience & Pytest-Asyncio Test Collection**: Safely handle PortAudio / PulseAudio initialization errors (`PortAudioError`) on headless runners in `src.voice.wakeword`, ignore hardware-dependent voice tests during CI collection, and install `pytest-asyncio` for `@pytest.mark.asyncio` support.

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

### Mobile APK Objectives

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
   - Graceful fallback for audio amplitude visualizer, camera vision preview, and secure storage read exceptio    - Set Android `minSdk = 23` in `build.gradle.kts` for modern API compatibility.

4. **Production Build Pipeline**:
   - Execute clean build via `build_mobile.py` with tests verification.
   - Distribute signed/release APK to `executables/meridian-x_mobile.apk` with SHA-256 hash.

### Verification Commands

- **Flutter Tests**: `flutter test` in `meridian_mobile`
- **APK Build**: `python build_mobile.py --target apk`

---

## Sub-Spec: Ultra-Low Latency Voice Engine & Accurate Multilingual Language Triage

### Voice Engine Objectives

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

### Architecture Hardening Objectives

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

### Phase 2 Refactoring Objectives

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

---

## Sub-Spec: Sprint 21 - System Polish, Atomic Data Resilience, Repo Hygiene & Settings Modularization

### Sprint 21 Objectives

1. **Repo Hygiene & Git Ignore**:
   - Remove accidental stray folder `meridian_backend/meridian_frontend/` containing `ProfileHeader.tsx`.
   - Update `.gitignore` to ignore `meridian_mobile/android/build/`, `brag-output/`, `skills-lock.json`.
2. **Frontend Dynamic Import Standardization**:
   - In `meridian_frontend/src/components/ProactiveGuardBanner.tsx`, replace dynamic `@tauri-apps/api/event` import with static import to eliminate Vite build chunking warnings.
3. **Atomic JSON Storage**:
   - Create `src/core/atomic_storage.py` with `atomic_write_json(filepath, data, indent=2)` using temporary file write + atomic replace (`os.replace`) to prevent corrupted files on unexpected shutdown.
4. **Browser Tool Consolidation & Exception Transparency**:
   - Modernize `src/tools/browser_agent.py` to route all web interactions through `browser_use_task` / `web_browser` with structured logger warning instead of silent error swallowing.
5. **Frontend Settings Modularization**:
   - Modularize monolithic `Settings.tsx` (3,115 lines) by extracting tab components into `meridian_frontend/src/views/settings/`:
     - `MascotTab.tsx`
     - `VoiceTab.tsx`
     - `IntegrationsTab.tsx`
     - `PasswordInput.tsx`
   - Maintain 100% backward compatibility of state, handlers, themes, and settings persistence.

---

## Sub-Spec: Sprint 22 - Background Three.js Optimization, Settings Completion & Signal Pruning

### Sprint 22 Objectives

1. **Three.js Background Render Loop Optimization**:
   - In `meridian_frontend/src/Mascot3DCharacter.tsx`, pause `requestAnimationFrame` loop when `document.hidden` is true using `visibilitychange` event listener.
2. **Lazy-Load Settings in Shell**:
   - In `meridian_frontend/src/components/Shell.tsx`, lazy-load `Settings` view with `React.lazy()` and `Suspense` to reduce initial bundle evaluation overhead.
3. **Structured Logging & Linter Hygiene**:
   - In `meridian_backend/src/voice/wakeword.py`, replace console `print()` with `logger.info()`.
   - In `meridian_backend/tests/test_tools.py`, remove duplicate `import os`.
4. **Cancellation Signal Pruning & Memory Safety**:
   - In `meridian_backend/src/core/loop_stream.py`, store cancel signals with timestamps and prune entries older than 1 hour.
5. **Complete Settings Modularization (Phase 2)**:
   - Extract `AiModelsTab.tsx`, `SystemGuardTab.tsx`, and `SpendAirGapTab.tsx` from `Settings.tsx` into `meridian_frontend/src/views/settings/`.
   - Reduce `Settings.tsx` to a clean tab container under 250 lines.

---

## Sub-Spec: Sprint 23 - Daemon Logging Hygiene, Voice Error Transparency & Settings Dead State Pruning

### Sprint 23 Objectives

1. **Voice Daemon Structured Logging**:
   - In `meridian_backend/src/voice/wakeword.py` and `meridian_backend/src/voice/stt.py`, replace all raw `print()` statements in audio loops and model loaders with structured logging (`logger.info()`, `logger.warning()`, `logger.debug()`) to prevent stdout buffer stalling and process deadlocks on Windows Tauri daemons.
2. **Voice Delegate Exception Transparency**:
   - In `meridian_backend/src/api/voice.py`, convert raw `print("Failed to delegate/initialize Supertonic engine:", e)` to `logger.error("Failed to delegate/initialize Supertonic engine: %s", e, exc_info=True)`.
3. **Hardened Audio Tempfile Cleanup**:
   - In `meridian_backend/src/voice/stt.py`, ensure temporary fallback audio file write & transcribe cleanly unlinks files across Windows file-locking scenarios with explicit error handling.
4. **Settings Frontend Dead State Elimination**:
   - In `meridian_frontend/src/views/Settings.tsx`, remove unused state hooks `scannedOnnxModels`, `isScanningOnnx`, `fetchScannedOnnxModels`, and redundant `handleBrowseOnnxFile` / `handleFileInputChange` duplications, eliminating unnecessary re-renders.

---

## Sub-Spec: Sprint 24 - Enterprise Security Hardening, Binary Swap Resilience, Perception API Safety, Session Interruption Isolation & Frontend Strict Type Safety

### Sprint 24 Objectives

1. **Security Hardening (CORS & Vault Auth Gates)**:
   - In `meridian_backend/api.py`, remove dangerous wildcard `allow_origin_regex=r"https?://.*"` that permits arbitrary websites to access local daemon. Restrict to local interfaces (`localhost`, `127.0.0.1`, `[::1]`) and Tauri desktop schemes (`tauri://*`, `https?://tauri.localhost`).
   - In `meridian_backend/src/api/vault.py`, guard vault endpoints (`/api/vault/keys`, `/api/vault/keys/{env_var}`, etc.) with `require_permission(["admin", "user"])` or loopback verification to prevent unauthorized secret scraping.
   - Remove plaintext secret dumping to `os.environ["SMTP_PASSWORD"]` in `save_google_app_password_api`.
2. **Updater Reliability & Windows File Locking**:
   - In `meridian_backend/src/core/updater.py`, fix `safe_swap_binary`: on Windows, rename active `target_binary` to `target_binary.bak` before copying `new_binary`, avoiding `PermissionError [WinError 32]`.
   - In `check_for_updates`, use `packaging.version.parse` for semantic version comparison to prevent bogus update triggers.
3. **Perception API Safety & Robustness**:
   - In `meridian_backend/src/api/perception.py`, replace `subprocess.Popen(["cmd", "/c", "start", "", target_url])` with Python standard `webbrowser.open(target_url)` to eliminate Windows shell injection vulnerabilities.
   - In `api_vision_screenshot`, replace static temp file path with `tempfile.NamedTemporaryFile(suffix=".png", delete=False)` to prevent concurrent capture collisions.
   - Provide structured Pydantic schemas for `/api/telephony/call`, `/api/crm/contact`, and `/api/sos/trigger`.
4. **Agent Loop Session Isolation & Vault Durability**:
   - In `meridian_backend/src/core/loop.py`, replace global `_interrupt_event` with session-scoped cancellation registry (`_session_interrupts`) keyed by `session_id`.
   - In `meridian_backend/src/core/vault.py`, use `atomic_write_json` from `src.core.atomic_storage` to write `VAULT_FILE` atomically, preventing vault truncation on system crashes.
5. **Frontend Strict Type Safety & Quality**:
   - In `meridian_frontend/tsconfig.json`, enable `"strict": true` and `"noImplicitAny": true`, resolving any typing gaps across views and components.

---

## Sub-Spec: Sprint 25 - Loop Multi-Alias Remapping, VRAM Memoization, Stream Disconnect Hygiene & Frontend Compiler Hardening

### Sprint 25 Objectives

1. **Tool Argument Multi-Alias Remapping**:
   - In `meridian_backend/src/core/loop_executor.py`, eliminate premature `break` in `PARAM_ALIASES` iteration so tool calls with multiple aliased parameters (e.g. `filepath` and `content_str`) are completely remapped rather than truncated.
2. **Subprocess VRAM Query Memoization**:
   - In `meridian_backend/src/core/llm_clients.py`, add a 5-second TTL cache to `get_gpu_vram_usage()`, eliminating high-frequency process spawning and `FileNotFoundError` exceptions on machines without NVIDIA GPUs.
3. **SSE Stream Cancellation Hygiene & Daemon Logging**:
   - In `meridian_backend/src/api/swarm.py`, cleanly catch `(asyncio.CancelledError, GeneratorExit)` in `swarm_stream` and `proactive_stream` and replace raw `print()` with structured `logger.debug()` calls.
4. **TypeScript Compiler Enterprise Flags**:
   - In `meridian_frontend/tsconfig.json`, enable `"noFallthroughCasesInSwitch": true` and `"forceConsistentCasingInFileNames": true`.

---

## Sub-Spec: Sprint 26 - Tool Ecosystem Modernization (Dynamic Signatures, Canonical Aliases & Execution Timeouts)

### Sprint 26 Objectives

1. **Dynamic Parameter Signature Reflection**:
   - In `meridian_backend/src/core/loop_stream.py`, enhance `generate_tools_doc()` so that any tool without a hardcoded entry in `TOOL_SIGNATURES` automatically extracts its parameter names and default values via `inspect.signature(func)`. Ensure the LLM always receives exact `name(param="<...>", ...)` signatures for all 100+ registered tools.
2. **Canonical Tool Aliases in Registry**:
   - In `meridian_backend/src/tools/registry.py`, register missing canonical aliases for shell execution (`"shell"`, `"terminal"`, `"run_command"`) pointing to `nl_run`.
3. **Execution Timeout Guard**:
   - In `meridian_backend/src/tools/registry.py`, wrap tool execution in `asyncio.wait_for(..., timeout=timeout_seconds)` with an intelligent default (60s standard, 180s for browser and long-running test suites) to prevent hung subprocesses or frozen sockets from stalling the agent loop.

---

## Sub-Spec: Sprint 27 - High-Impact Engineering Modernization & Immediate ROI Hardening

### Sprint 27 Objectives

1. **CI Pipeline Modernization & Code Quality Gate**:
   - Enhance `.github/workflows/verify.yml` with `ruff check` linting and formatting verification in the backend job, preserving existing pytest, frontend typecheck/build, and Flutter pipelines.
2. **Dependency Hygiene & Tool Configuration**:
   - Create root `pyproject.toml` with project metadata, dependencies version constraints, and configurations for `ruff`, `mypy`, and `pytest`.
3. **Unified Structured Logging**:
   - Create `meridian_backend/src/core/logger.py` providing standard `get_logger(name)` with structured format, level management, and clean console handlers.
4. **Chat Router Modularity**:
   - Extract chat and stream endpoints from `meridian_backend/api.py` into `meridian_backend/src/api/chat.py` with `APIRouter(prefix="/api/chat", tags=["chat"])`, keeping `api.py` as clean orchestrator.
5. **Declarative `@tool` Registration Decorator**:
   - Implement `@tool(name=None, tier=1, description=None)` decorator in `meridian_backend/src/tools/registry.py` for standard declarative tool registration.

---

## Sub-Spec: Sprint 28 - Stream Back-Pressure, Architecture & Contributor Docs, Dead Code Pruning & Type Safety

### Sprint 28 Objectives

1. **SSE Stream Generator Cooperative Back-Pressure**:
   - In `meridian_backend/src/api/chat.py`, add `await asyncio.sleep(0)` within the SSE event streaming loop to yield control cooperatively back to the asyncio event loop between emitted tokens, preventing event loop starvation.
2. **Architecture Specification**:
   - Create `docs/architecture.md` detailing the 5-layer autonomous agent architecture (Sensors $\to$ ReAct Reasoning & Consensus $\to$ Tool Execution Registry $\to$ Memory & Cognitive Graph $\to$ Client Interfaces & WebSocket bus).
3. **Contributor Guidelines**:
   - Create `CONTRIBUTING.md` documenting developer workflow, setup instructions, linting via `ruff`, test verification via `pytest`, and PR hygiene.
4. **Dead Script Pruning**:
   - Remove obsolete standalone scripts `cleanup.py` and `create_shortcut.py`.
5. **Type Safety & Model Hardening**:
   - Add explicit return type annotations and schema validation across core database and dependency routines.

---

## Sub-Spec: Sprint 29 - Silero VAD Integration for Whisper Transcription & Real-Time Voice Streaming

### Sprint 29 Objectives

1. **Faster-Whisper Silero VAD Filter**:
   - Enable `vad_filter=True` with `VadOptions` in `src.voice.stt:transcribe_audio_file` and `src.voice.stt:transcribe_audio_array` to eliminate silence hallucinations.
2. **Unified Silero VAD Evaluator**:
   - Create `src.voice.vad` with `SileroVADDetector` leveraging faster-whisper's bundled ONNX model (`faster_whisper.vad.get_vad_model`) with graceful heuristic fallback (RMS + pitch centroid) if unavailable.
3. **Live Microphone Recording Integration**:
   - Integrate Silero speech probability detection into `src.voice.stt:record_and_transcribe` for rapid speech start detection and silence timeout termination.
4. **Duplex Voice Engine Barge-In Hardening**:
   - Enhance `src.voice.duplex:DuplexVoiceEngine.check_barge_in` with Silero neural speech confidence to eliminate false-trigger interruptions from background noise.
5. **Ambient Listener Speech Segmentation**:
   - Wire Silero speech detector into `src.voice.ambient_listener:ContinuousAmbientListener.is_speech_chunk`.

---

## Sub-Spec: Sprint 30 - Production Keystore Signing & LAN Subnet Auto-Discovery for Mobile APK

### Sprint 30 Objectives

1. **Production Keystore Signing Configuration (`build.gradle.kts`)**:
   - Load `key.properties` from `meridian_mobile/android/key.properties` if present.
   - Bind `signingConfigs.create("release")` dynamically with keystore path, storePassword, keyAlias, keyPassword.
   - Gracefully fallback to `signingConfigs.getByName("debug")` if `key.properties` is absent so developer workflow remains unbroken.
2. **Automated Keystore Helper & Builder Extension (`build_mobile.py`)**:
   - Add `--generate-keystore` flag and automated detection for release keystore properties.
   - Ensure `key.properties`, `*.jks`, `*.keystore` are protected in `.gitignore`.
3. **LAN Subnet Host Discovery Service (`lan_discovery.dart`)**:
   - Discover active local network interface IPv4 address and calculate subnet prefix (e.g. `192.168.1.0/24`).
   - Probe active HTTP endpoints (`/api/health`) across subnet candidates with low-latency asynchronous concurrent socket/HTTP checks.
   - Return found desktop endpoints (`ws://<IP>:4132/ws`).
4. **Pairing Modal UX Integration (`remote_pairing_modal.dart`)**:
   - Add 1-click "SCAN LOCAL NETWORK" / "AUTO-DISCOVER DESKTOP" button with progress indicator.
   - Automatically autofill detected desktop IP into host field and suggest one-tap pairing link.
5. **Unit & Integration Verification**:
   - Add tests in `meridian_mobile/test/` verifying URL normalization, network discovery parsing, and signing config resolution.

---

## Sub-Spec: Sprint 31 - Headless Web Research Optimization & Redundant Browser Suppression

### Sprint 31 Objectives

1. **Headless-First Research Directives (`src/core/mode.py`)**:
   - Update `MODE_DIRECTIVES["RESEARCHER"]` to prioritize fast headless search (`search_web`, `search_news`, `autonomous_research`).
   - Restrict `browser_use_task` to interactive flows (logins, form submission, visual UI tasks) or when explicitly requested by user.
   - Update `MODE_DIRECTIVES["AUTO"]` to differentiate headless information retrieval vs live browser automation.
2. **Parallel Browser Call De-duplication (`src/core/loop_dispatcher.py`)**:
   - When user turn contains both headless search tools (`search_web`, `search_news`, `autonomous_research`) AND `browser_use_task`, suppress redundant `browser_use_task` unless prompt explicitly asks for browser UI interaction.
   - Prevent disruptive Playwright window popup on desktop during ordinary research tasks.
3. **Verification**:
   - Unit tests verifying directive formatting, dispatcher tool conflict suppression, and regression safety.

---

## Sub-Spec: Sprint 32 - Full Audit Remediation & Core System Hardening

### Sprint 32 Objectives

1. **Critical Syntax & Python 3.10 Compatibility**:
   - In `meridian_backend/src/core/lsp_client.py`: Remove backslash escape sequence from inside f-string at line 59 (`root_uri = f"file:///{self.root_dir.replace('\\', '/')}"`) by computing normalized path prior to string interpolation, ensuring compatibility with Python 3.10+.
2. **Security Hardening**:
   - In `meridian_backend/src/tools/dynamic_manager.py`: Add AST security validation to `create_dynamic_tool` forbidding dangerous calls (`eval`, `exec`, `__import__`, `open`, `__subclasses__`, `__globals__`) and unsafe system modules (`ctypes`, `socket`, `subprocess`) to prevent arbitrary code execution from untrusted LLM outputs.
   - In `meridian_backend/src/core/workspace_orchestrator.py`: Remove `shell=True` from `Popen` calls, using safe argument lists with `shell=False`.
   - In `meridian_backend/src/api/deps.py`: Remove `shell=True` from port clearance and taskkill execution, using sanitized integer PID list and direct process execution.
   - In `meridian_backend/src/tools/external_connectors.py`: Make author name in `generate_draft_reply` configurable via `MERIDIAN_USER_NAME` or user profile instead of hardcoded string.
3. **High & Medium Lint Remediation**:
   - Fix empty f-strings (F541) across backend modules.
   - Eliminate shadow import redefinitions (F811) in `meridian_backend/src/core/auth.py`, `meridian_backend/src/tools/registry.py` (duplicate `universal_search`), and `meridian_backend/src/tools/system_windows.py` (`game_mode_active`).
   - Eliminate dead local variable assignments (F841) in `meridian_backend/src/api/deps.py` (`res`), `meridian_backend/src/core/loop_executor.py` (`has_var_positional`), `meridian_backend/src/core/lsp_client.py` (`init_res`), `meridian_backend/src/core/scheduler.py` (`status`), `meridian_backend/src/core/workflow_engine.py` (`edges`, `node_map`), `meridian_backend/src/tools/browser_use_agent.py` (`lower_task`), `meridian_backend/src/tools/expiry_sentinel.py` (`exp_dt`), `meridian_backend/src/tools/web.py` (`url`), `meridian_backend/database.py` (`ollama_host`).
   - Fix membership test anti-pattern in `meridian_backend/src/core/consensus_engine.py:221`: `not x in y` -> `x not in y` (E713).
   - In `meridian_backend/api.py`: Replace naive line-by-line `.env` parsing with `python-dotenv` `load_dotenv(env_path)`.
4. **Silent Exception Transparency & Logging**:
   - In `meridian_backend/src/core/proactive/guard.py`: Replace silent `except Exception: pass` blocks with `logger.debug` structured logs.
5. **Frontend Package Hygiene**:
   - Move `@types/three` from `dependencies` to `devDependencies` in `meridian_frontend/package.json`.
6. **Verification Gate**:
   - Verify all unit and integration tests pass cleanly and frontend typechecks/builds without errors.

---

## Sub-Spec: Sprint 33 - Anti-Hallucination, Tool Enforcement & Finish Parsing Resilience

### Sprint 33 Objectives

1. **System Prompt Anti-Hallucination & Physical File Creation Enforcement (`src/core/mode.py`)**:
   - Instruct the LLM explicitly that it possesses full physical file system execution via local tools (`write_file`, `scaffold_project`, `nl_run`, `open_file`, etc.).
   - Explicitly forbid the standard LLM disclaimer: "Since I cannot create physical folders on your machine...".
   - Mandate that when the user asks to create, build, or write files/projects, the agent MUST call `<call:write_file>` or `<call:scaffold_project>` or `<call:nl_run>` rather than merely printing code or claiming completion without execution.
   - Mandate that inside `<finish>`, `proactive_suggestions`'s `action` field must be a valid raw CLI command or prompt string without pseudocode wrapping (e.g. `shell(...)` or unescaped nested double quotes).

2. **Resilient JSON Recovery & Leakage Prevention (`src/core/loop_parser.py`)**:
   - In `process_final_response()`, implement robust JSON sanitization:
     - Repair unescaped quotes inside string values (e.g., `"action": "shell("...")"` -> `"action": "shell(\"...\")"` or strip outer wrapper).
     - Handle truncated or trailing bracket JSON fragments (e.g., `[{"title": ...}]}`).
     - Fallback extraction: if JSON parsing still fails, ensure raw internal JSON schemas (`{"title":...}`, `{"proactive_suggestions":...}`, `{"chat":...}`) never leak raw JSON syntax into user-facing chat text. Extract readable text or generate a clean user message.

3. **Frontend Timeline Fallback Hardening (`meridian_frontend/src/views/Timeline.tsx`)**:
   - In `formatFinalText()`, detect unparsed JSON fragments or raw suggestion syntax and sanitize display so raw JSON code blocks are not rendered as conversational chat text.

4. **Unit Verification Suite (`meridian_backend/tests/test_response_resilience.py`)**:
   - Add unit tests verifying prompt anti-hallucination directives, JSON repair of unescaped quotes, trailing bracket repair, and zero raw JSON leakage.

---

## Sub-Spec: Sprint 34 - Full Code Audit Bug Remediation & Resilience Hardening

### Sprint 34 Objectives

1. **Non-Streaming Endpoint SSE Accumulation Resilience (`meridian_backend/src/api/chat.py`)**:
   - Properly parse SSE events by splitting on `\n\n` boundaries and extracting `event:` and `data:` components.
   - For `event: text`, extract `"chat"` from parsed JSON payloads when emitted from `<finish>` turn completion, or append raw multiline chunks while preserving line breaks.
   - Guard against non-text SSE events (errors, confirmations, suggestions) polluting conversational text.

2. **Concurrent Read-Only Tool Isolation & Non-Backtracking (`meridian_backend/src/core/loop_dispatcher.py`)**:
   - Prevent Tier-0 concurrent read-only tool failures from triggering Tree-of-Thoughts (`tot_failed = True`) backtracks.
   - Preserve valid observations from concurrent tools that succeeded in the same batch.

3. **LLM Linting False-Positive Elimination (`meridian_backend/src/core/loop_executor.py`)**:
   - Replace brittle `"OK" not in lint_resp.upper()` with structured acceptance matching (`OK`, `NO ISSUES`, `CODE IS VALID`) and explicit error/warning keyword detection.

4. **Race-Free Temporary System Message Cleanup (`meridian_backend/src/core/loop.py`)**:
   - Replace stale integer index popping (`temp_sys_idx`) with safe identity-based message removal (`temp_sys_msg in history`).

5. **Approval Gate Coverage for Shell Aliases (`meridian_backend/src/core/confirmations.py`)**:
   - Expand `check_approval_gate` to check dangerous command patterns for `"shell"`, `"terminal"`, `"nl_to_shell"`, in addition to `"run_command"` and `"nl_run"`.
   - Initialize `_confirmations_lock` deterministically at module level.

6. **Thread-Safe Stream Backpressure in Async Queue (`meridian_backend/src/core/loop_stream.py`)**:
   - Replace lossy `loop.call_soon_threadsafe(queue.put_nowait)` with `asyncio.run_coroutine_threadsafe(queue.put(item), loop).result()` for true thread-safe backpressure without dropped tokens.

---

## Sub-Spec: Sprint 35 - Exhaustive Fallback & Anti-Surrender Resilience Engine

### Sprint 35 Objectives

1. **Interactive/CLI Turn Limit Elevation (`src/core/loop.py`)**:
   - Raise default turn limit from `1` to `10` when autonomous mode is disabled, enabling multi-step fallback problem solving during interactive and CLI sessions.
2. **Exhaustion & Anti-Surrender Prompt Directives (`src/core/mode.py`)**:
   - Enforce an explicit EXHAUSTION RULE in system prompts: models must attempt at least 2 alternative tools/methods (e.g. `run_command`, `search_files`, python scripts) before giving up or concluding with `<finish>`.
3. **Imperative ToT Backtrack Recovery (`src/core/loop_dispatcher.py`)**:
   - Strengthen Tree-of-Thoughts backtrack observations with actionable, imperative directives preventing premature surrender and forcing alternative tool selection.
4. **MCTS Pruning Threshold Optimization (`src/core/loop_dispatcher.py`)**:
   - Lower MCTS branch pruning cutoff from `0.35` to `0.15` and skip pruning if only a single candidate action is proposed.
5. **Granular Per-Tool Argument Retry Budgets (`src/core/loop_dispatcher.py`)**:
   - Track tool retries by signature `(session_id, tool_name, args_hash)` rather than just `(session_id, tool_name)`, allowing agents to try the same tool with different arguments.
6. **Graceful Wake Word Fallback Cascade (`src/voice/wakeword.py`)**:
   - If custom ONNX model is missing or fails to load, gracefully fall back to pre-trained built-in models or Silero VAD energy detection without shutting down monitoring.

---

## Sub-Spec: Sprint 36 - Voice Pipeline Hardening & Neural VAD Integration

### Sprint 36 Objectives

1. **Neural Silero VAD Integration (`src/voice/wakeword.py`)**:
   - Wire `get_silero_detector()` into wakeword fallback, evaluating audio chunks with real neural speech probability (0.0 to 1.0) and graceful heuristic fallback.
2. **Audio Input Device Failover & User Mic Selection (`src/voice/wakeword.py`)**:
   - Query user profile `audio_input_device`. Fallback to system default input device if missing or invalid, avoiding stream crashes when USB/BT mics toggle.
3. **Post-Trigger Debounce & Buffer Cooldown (`src/voice/wakeword.py`)**:
   - Implement cooldown timestamp to prevent echo double-triggers after waking.
4. **Dynamic Speech Activity Continuous Window Extension (`src/voice/wakeword.py`)**:
   - Extend continuous window duration (`extend_continuous_window`) dynamically when speech activity is detected.

---

## Sub-Spec: Sprint 37 - System-Wide Reliability, Tool Output Budgeting & Parity Hardening

### Sprint 37 Objectives

1. **CLI Cloud/Local Configuration Parity (`main.py`)**:
   - Resolve active `model_source` and `api_provider` from SQLite database, enabling CLI execution against cloud providers (Gemini, Claude, OpenAI) when configured.
   - Fall back to `get_brain_model()` if CLI `--model` argument is empty.
2. **Safe Tool Output Truncator Guard (`src/core/loop_dispatcher.py`)**:
   - Add `truncate_tool_observation()` to bound single tool outputs to 12,000 characters, retaining head and tail while omitting the middle to prevent context window blowout.
3. **Immediate TTS Audio Interrupt on Barge-in (`src/voice/wakeword.py` & `src/core/loop.py`)**:
   - Call `stop_active_tts()` when wake word triggers or agent loop receives interrupt signal, instantly killing audio playback.
4. **Fuzzy Python/JSON Tool Call Auto-Healer (`src/core/loop_executor.py`)**:
   - Implement `sanitize_tool_args_str()` with AST literal evaluation and Python dictionary repair (`True`/`False`/`None` and single quotes), auto-healing formatting mistakes before LLM critique.

---

## Sub-Spec: Sprint 38 - Multi-Mode Dynamic Task & Provider Routing

### Sprint 38 Objectives

1. **Database Task Route Configuration (`meridian_backend/database.py`)**:
   - Implement `get_task_routing_enabled()` and `set_task_routing_enabled(enabled: bool)`.
   - Implement `get_task_model_routes()` and `set_task_model_routes(routes: Dict[str, Dict[str, str]])` storing custom provider/model/source mappings per cognitive mode (`ENGINEER`, `REVIEWER`, `RESEARCHER`, `OPERATOR`, `ANALYST`, `PROACTIVE`).
2. **Task-Based Dynamic Turn Router (`src/core/loop_planning.py`)**:
   - Implement `resolve_route_for_task(prompt, brain_model, api_provider, model_source) -> Tuple[str, str, str, str]`.
   - Matches prompt against `classify_mode()` and swaps model and provider dynamically per task when task routing is enabled.
3. **Agent Loop Multi-Provider Integration (`src/core/loop.py`)**:
   - Call `resolve_route_for_task()` in `run_react_agent_loop` and emit SSE thought notice when task routing activates.
4. **Task Routes REST Endpoints (`meridian_backend/api.py`)**:
   - Expose `GET /api/settings/task-routes` and `POST /api/settings/task-routes`.
5. **Multi-Mode Routing Settings UI (`meridian_frontend/src/views/settings/MultiModeTab.tsx`)**:
   - Build responsive, premium glassmorphism settings tab with master enable toggle, per-task provider and model selectors, preset options, and real-time route simulator.

---

## Sub-Spec: Sprint 39 - Intelligence & Telemetry Suite

### Sprint 39 Objectives

1. **Hybrid Sparse-Dense RAG with Reciprocal Rank Fusion (PL-08, PL-11)**:
   - Extend [`src/db/rag.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/rag.py) to perform hybrid search: BM25 keyword matching + Turbovec dense embeddings combined via Reciprocal Rank Fusion (RRF).
   - Expose `hybrid_search_knowledge_base(query: str, limit: int = 5, bm25_weight: float = 0.5)` alongside pure vector search.
   - Guarantee deterministic in-memory CPU fallback embeddings in [`src/db/embeddings.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/embeddings.py) when Ollama and OpenAI are offline.

2. **Live Browser-Use Mini-HUD Streaming & Viewport Frames**:
   - Add `browser_capture_b64()` in [`src/tools/web_browser.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/web_browser.py) to extract base64-encoded JPEG viewports during automation.
   - Add live viewport capture and step event hooks in [`src/tools/browser_use_agent.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/browser_use_agent.py) to stream step state to event bus.
   - Expose endpoint `GET /api/browser/frame` in [`meridian_backend/api.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py).
   - Render live Browser Mini-HUD overlay card in [`meridian_frontend/src/views/Timeline.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Timeline.tsx).

3. **Perception Stream to Proactive Nudges Bridge (PL-03, PL-04)**:
   - Bridge [`src/api/perception.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/api/perception.py) active window events, screen OCR errors, and terminal crashes directly into [`src/core/proactive/dispatcher.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/proactive/dispatcher.py).
   - Trigger auto-fix suggestion nudges when error patterns or crashes are perceived in active window sense.

4. **Collapsible ReAct Step Accordions & Diff Viewer in Timeline (PL-19)**:
   - Build [`CodeDiffViewer.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/components/ui/CodeDiffViewer.tsx) to render syntax-highlighted diffs (unified additions/deletions).
   - Enhance [`meridian_frontend/src/views/Timeline.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/views/Timeline.tsx) to detect markdown diff code blocks and auto-render interactive diffs and collapsible step accordions.

5. **Heterogeneous Subagent Model Routing (PL-10)**:
   - Enhance [`src/core/swarm.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/swarm.py) and [`src/api/swarm.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/api/swarm.py) with dynamic provider and source resolution per subagent role (`auditor` -> DeepSeek Coder / Claude, `planner` -> Claude Sonnet / Qwen, `researcher` -> Gemini Flash / Ollama).
   - Support custom per-role model and provider overrides in `LobbyDebateRequest` and `SwarmAgent.execute`.

---

## Sub-Spec: Sprint 40 - System-Wide Polish, Performance & Resilience Suite

### Sprint 40 Objectives

1. **Router & Lifespan Clean Extraction (`meridian_backend/api.py`, `src/api/websockets.py`, `src/core/lifespan.py`)**:
   - Extract `/ws`, `/api/ws/mobile`, `/ws/agent-status`, and custom swagger docs into [`meridian_backend/src/api/websockets.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/api/websockets.py).
   - Move lifespan daemon startup/teardown logic into [`meridian_backend/src/core/lifespan.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/lifespan.py).
   - Shrink [`meridian_backend/api.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/api.py) to under 250 lines of pure router mounting and middleware configuration.
   - Update [`tasks/todo.md`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/tasks/todo.md) Task 2.3 status to complete.

2. **Frontend Bundle Optimization & Reconnection HUD (`meridian_frontend/src/`)**:
   - Code-split Three.js mascot canvas using `React.lazy` and `Suspense` in [`Mascot.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/components/Mascot.tsx) / [`App.tsx`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_frontend/src/App.tsx) to reduce initial vendor bundle.
   - Dynamic lazy loading for heavy views: `Settings`, `WorkflowBuilder`, `MemoryEditor`, `SwarmDebate`.
   - Add visual connection status indicator / auto-reconnect banner component with exponential backoff HUD.

3. **Subprocess Orphan Clean-up & Concurrent Tool Timeout Guard (`src/core/loop.py`, `src/core/loop_dispatcher.py`)**:
   - In [`interrupt_agent_loop()`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/loop.py), scan and terminate all active spawned subagent child processes and Playwright browser instances via `psutil`.
   - In [`loop_dispatcher.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/loop_dispatcher.py), wrap individual concurrent Tier-0 tool calls in `asyncio.wait_for(timeout=15.0)` to eliminate hangs from stalled tool responses.

4. **Native SQLite FTS5 for Hybrid RAG (`src/db/connection.py`, `src/db/rag.py`)**:
   - Implement `knowledge_base_fts` SQLite virtual table via FTS5 with transparent fallback in [`src/db/connection.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/connection.py).
   - In [`src/db/rag.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/db/rag.py), query SQLite FTS5 for C-level BM25 scoring before falling back to in-memory tokenizer.

5. **Hardware-Backed Vault Master Key (`src/core/vault.py`)**:
   - Add OS Keyring storage lookup in [`src/core/vault.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/core/vault.py) using the Python `keyring` library, with transparent zero-crash fallback to env/file persistence.

6. **Playwright Shadow DOM & Bounding Box Element Resolution (`src/tools/web_browser.py`)**:
   - Enhance element indexing in [`src/tools/web_browser.py`](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/meridian_backend/src/tools/web_browser.py) to query open Shadow Roots and evaluate client bounding boxes for custom web components.

---

## Sub-Spec: Sprint 41 - User Delight, High-Leverage Compound Tools & Interactive Action HUD

### Sprint 41 Objectives

1. **High-Leverage Screen Diagnosis (`src/tools/desktop.py`)**:
   - Implement `explain_active_screen(focus_area: Optional[str] = None) -> str`.
   - Captures active screen snapshot, gathers active window context metadata via `get_active_window_sense()`, extracts visible errors/code/content via vision model with graceful OCR fallback, and returns structured diagnosis.

2. **One-Shot Workspace Health Audit (`src/tools/developer.py`)**:
   - Implement `workspace_quick_audit(repo_path: Optional[str] = None) -> str`.
   - Executes consolidated git status check, diff inspection, recent commit log, and uncommitted secrets/syntax check, returning complete developer briefing with proposed atomic commits in a single roundtrip.

3. **Smart Clipboard Transformer (`src/tools/clipboard.py`)**:
   - Implement `smart_clipboard_action(mode: str = "auto") -> str`.
   - Inspects clipboard content, identifies data type (JSON, code, stack trace, URL, SQL), and produces formatted/beautified output or diagnosis.

4. **Tool Registry & Dynamic Signature Parity (`src/tools/registry.py`, `src/core/loop_stream.py`)**:
   - Register `explain_active_screen`, `workspace_quick_audit`, and `smart_clipboard_action` in `TOOL_REGISTRY`.
   - Add to `CORE_TOOLS_LIST` and `TOOL_SIGNATURES` in `loop_stream.py`.

5. **Frontend Quick-Action Floating Chips (`meridian_frontend/src/views/Timeline.tsx`)**:
   - Add sleek glassmorphism quick-action chips above chat input (Screen Explain, Git Audit, Clipboard Transform) for 1-click execution.

6. **Unit Tests & Quality Verification**:
   - Author `meridian_backend/tests/test_user_delight_tools.py` verifying execution, fallbacks, and signature resolution.
   - Run pytest and frontend typecheck.



---

## Sub-Spec: Sprint 42 - Semantic Tool Retrieval & Pre-Execution Parameter Auto-Healing

### Sprint 42 Objectives

1. **Semantic Inverted Tool Indexer (`src/core/tool_indexer.py`)**:
   - Parse all tool names, descriptions, and docstrings from `TOOL_REGISTRY`.
   - Index terms and synonyms, providing BM25 / token similarity scoring.
   - Implement `find_relevant_tools(prompt: str, top_k: int = 5) -> List[str]`.
   - Dynamically surface relevant niche tools (e.g. `calculate_leave_by_time`, `detonate_attachment_sample`, `screen_incoming_call`) even when user prompt lacks hardcoded keywords.

2. **Semantic Dynamic Tool Injection (`src/core/loop_stream.py`)**:
   - Integrate `find_relevant_tools()` into `generate_tools_doc(mode, prompt)`.
   - Automatically inject top semantic tool matches alongside core tools, keeping prompt token budget tight while achieving 100% recall.

3. **Pre-Execution Parameter Auto-Healing & Path Normalizer (`src/core/loop_executor.py`)**:
   - Implement `auto_heal_tool_args(sig: inspect.Signature, args: Dict[str, Any]) -> Tuple[Dict[str, Any], bool]`.
   - Auto-coerce string digits to `int`/`float` when parameter annotation expects numeric type.
   - Auto-coerce string booleans (`"true"`, `"false"`) to `bool`.
   - Normalize path separators (`\` -> `/`) and trim stray surrounding quotation marks.

4. **Unit Tests & Quality Verification**:
   - Create `meridian_backend/tests/test_tool_intelligence.py` testing semantic retrieval recall, parameter auto-coercion, and path sanitization.
   - Quality gate: `pytest meridian_backend/tests/test_tool_intelligence.py`.


---

## Sub-Spec: Sprint 43 - Continuous Self-Improvement & Reflexion Engine

### Sprint 43 Objectives

1. **Reflexion & Lesson Extraction Engine (`src/core/reflection_engine.py`)**:
   - Implement `ReflectionEngine` using `UnifiedCognitiveGraph` to store `learned_rule` and `task_experience` nodes.
   - Implement `detect_user_correction(text: str) -> Optional[str]` to detect user corrections and extract persistent rules.
   - Implement `record_learned_lesson(rule: str, category: str, context: Optional[str])`.
   - Implement `record_task_experience(goal: str, tools_used: List[str], outcome: str)`.
   - Implement `get_relevant_lessons(query: str, limit: int = 4)` and `get_relevant_experiences(query: str, limit: int = 2)`.

2. **Context Enrichment Integration (`src/core/loop_planning.py`)**:
   - In `enrich_system_prompt()`, inject retrieved lessons (`[LEARNED LESSONS & USER CONSTRAINTS]`) and past trajectories (`[PROVEN PAST TRAJECTORIES (FEW-SHOT)]`).

3. **Agent Loop Lifecycle Hooks (`src/core/loop.py`)**:
   - Check incoming prompts with `detect_user_correction()`; auto-save user constraints immediately.
   - Record successful task trajectory upon valid `<finish>`.
   - Record anti-pattern lesson on tool failure or critical exception.

4. **Unit Tests & Quality Verification**:
   - Create `meridian_backend/tests/test_reflection_engine.py` testing correction detection, lesson persistence, FTS5 retrieval, experience recording, and prompt injection.
   - Quality gate: `pytest meridian_backend/tests/test_reflection_engine.py`.


---

## Sub-Spec: Sprint 44 - Root Cause Error Diagnostics & Explainable Issue Cards

### Sprint 44 Objectives

1. **Root Cause Error Diagnostic Engine (`src/core/error_diagnostics.py`)**:
   - Parse raw exceptions, stack traces, and tool failure logs into structured explanations.
   - Categorize failures: `FILE_NOT_FOUND`, `MODEL_UNAVAILABLE`, `CONNECTION_REFUSED`, `PERMISSION_DENIED`, `SYNTAX_ERROR`, `TIMEOUT`, `COMMAND_FAILED`.
   - Provide `diagnose_error_root_cause(raw_error: str) -> Dict[str, str]` returning `main_issue`, `why`, `how_to_fix`, and `raw_details`.
   - Provide `format_explainable_error_markdown(raw_error: str, tool_name: Optional[str]) -> str`.

2. **Backend Error Emission Integration (`src/core/loop_dispatcher.py` & `src/core/loop.py`)**:
   - In `loop_dispatcher.py`, format tool observations and failure thoughts using `format_explainable_error_markdown` instead of raw exception strings.
   - In `loop.py`, format API failures and loop crashes with root cause explanation.

3. **Frontend Explainable Issue Card (`meridian_frontend/src/views/Timeline.tsx`)**:
   - Parse error events and network disconnects into human-friendly cards.
   - Render `ExplainableIssueCard` showing **Main Issue**, **Why It Happened**, **Suggested Fix**, and collapsible Technical Trace.
   - Add 1-click **Ask Agent to Fix** action button.

4. **Unit Tests & Quality Verification**:
   - Author `meridian_backend/tests/test_error_diagnostics.py` verifying categorization and markdown formatting across all error types.
   - Quality gate: `pytest meridian_backend/tests/test_error_diagnostics.py` and `npm run build`.


---

## Sub-Spec: Sprint 45 - Universal Doctor, Turnkey Docker Production Stack & Mobile QR Pairing

### Sprint 45 Objectives

1. **Universal System Doctor CLI (`doctor.py`)**:
   - Provide standalone CLI script in repo root: `python doctor.py [--fix] [--verbose] [--json]`.
   - Comprehensive diagnostic checks:
     - Python runtime & virtualenv environment.
     - Critical native dependencies: PyTorch, ONNX, sounddevice, portaudio.
     - Database health: SQLite schema integrity, FTS5 extensions, WAL mode.
     - AI runtime: Ollama daemon status (11434) and locally pulled models.
     - Network port availability: 4132 (Backend API/WS), 4133 (Companion/Frontend), 11434 (Ollama).
     - Frontend asset readiness: `meridian_frontend/dist/index.html` and Node/npm version.
     - Mobile Flutter toolchain availability.
   - Self-healing mode (`--fix`):
     - Terminate stale/hung processes holding ports 4132/4133.
     - Initialize missing data directories and SQLite database schemas.
     - Ensure required directories exist.

2. **Turnkey Docker Production Stack (`docker-compose.prod.yml` & `Caddyfile`)**:
   - Modernize `Caddyfile` to serve static SPA files from `/srv` with client-side fallback `try_files {path} /index.html`.
   - Route `/api/*` and `/ws/*` endpoints with full WebSocket header upgrades to `meridian-backend:4132`.
   - Update `docker-compose.prod.yml` with automated frontend static build/volume mount, backend healthchecks, and persistent Ollama model storage.

3. **LAN Mobile Companion QR Pairing (`src/api/system.py` & Frontend Pairing Modal)**:
   - Implement `GET /api/system/pairing-info` and `GET /api/mobile/pairing-info` returning:
     - Auto-detected LAN IP address (via UDP probe).
     - WebSocket agent endpoint (`ws://<lan_ip>:4132/ws/agent`).
     - HTTP base URL (`http://<lan_ip>:4132`).
     - Vault/system auth token.
     - Standardized URI scheme `meridian://pair?url=...&token=...`.
     - ASCII terminal QR code rendering fallback.
   - Add "Pair Mobile" button and QR display in frontend settings/shell.

4. **Unit Tests & Verification Gate**:
   - Create `meridian_backend/tests/test_sprint45.py` validating doctor diagnostics, pairing info generation, and config files.
   - Quality gate: `python doctor.py`, `pytest meridian_backend/tests/test_sprint45.py`, and `npm run build`.

---

## Sub-Spec: Sprint 46 - UI, Layout & Visual Design System Elevation

### Sprint 46 Objectives

1. **Design System & Aesthetics Modernization (`index.css`)**:
   - Upgrade cyber-slate and dark palettes with deep OLED contrast, multi-tiered surface depths, and crisp luminescent border accents.
   - Introduce `.glass-card-premium`, `.glow-subtle`, `.action-pill`, and modern scrollbars.
   - Establish consistent typography hierarchy across `Outfit` (headings/hero), `Inter` (prose), and `JetBrains Mono` (technical metrics/code).

2. **Elevated NavRail & Shell Navigation (`NavRail.tsx` & `Shell.tsx`)**:
   - Sleek translucent navigation rail with active pill indicators and soft ambient backglow.
   - Tooltips with hotkey indicators, smooth hover transitions, and clean bottom section with version tag and connection health.

3. **Timeline Agent Command Center & Starter Hub (`Timeline.tsx`)**:
   - Redesign fresh state into a premier **AI Agent Command Center Hero**:
     - Radiant animated mascot status badge and greeting.
     - Categorized 1-click starter prompts: *Coding & Architecture*, *Multimodal & Screen Sense*, *Git & Quality Audit*, *Clipboard & Tools*.
     - Real-time capability indicators (RAG Knowledge, Brain Model, Local Hardware Guard).
   - Enhance chat bubbles:
     - User message: refined pill layout with user avatar and timestamp.
     - Assistant message: distinct step headers, collapsible ReAct thought drawers with timing badges, and code blocks with quick-copy.
   - Compound Quick Action Bar: upgraded floating action pills with distinct accent icons for Screen Sense, Git Audit, Smart Clipboard, and Terminal commands.

4. **Floating Input Dock & Action Toolbar (`Timeline.tsx`)**:
   - Floating frosted glass input dock with multi-line auto-expand.
   - Integrated quick actions: file attachment pill with drag-and-drop indicator, autonomous mode toggle, voice input button, and luminous dynamic Send button.

5. **StatusBar & Drawer Polish (`StatusBar.tsx` & `RightDrawer.tsx`)**:
   - Refined status bar with live pulsing status indicators, air-gap security pill, mini-meters for CPU & RAM, and mobile pairing trigger.
   - Polished right drawer with smooth transitions and real-time streaming vitals.

6. **Quality Verification Gate**:
   - Frontend typecheck: `npm --prefix meridian_frontend run lint` (`tsc --noEmit`).
   - Production bundle compile: `npm --prefix meridian_frontend run build`.

---

## Sub-Spec: Sprint 47 - Native Browser Extension Bridge (Manifest V3)

### Sprint 47 Objectives

1. **Manifest V3 Chrome Extension (`meridian_extension/`)**:
   - `manifest.json`: Manifest V3 specification with `activeTab`, `scripting`, `storage`, and `tabs` permissions.
   - `background.js`: Service worker with auto-reconnecting WebSocket client connected to `ws://localhost:4132/api/browser/extension` (with fallback to `ws://localhost:8000/api/browser/extension`).
   - `content.js`: Injected script for extracting active tab DOM content, visible text, form fields, taking viewport snapshots, Set-of-Marks visual badges, and executing clicks/inputs directly in the user's logged-in session.
   - `popup.html` & `popup.js`: Polished Meridian HUD popup displaying live connection status, current tab info, 1-click "Send Page to Meridian", and quick actions.

2. **Backend Extension Bridge Hub (`meridian_backend/src/api/browser_extension.py`)**:
   - WebSocket router mounted at `/api/browser/extension` with bidirectional JSON messaging.
   - Live extension connection tracking with ping/pong heartbeats to keep Manifest V3 service workers awake.
   - RPC request/response handling with correlation IDs for async tool calls (`get_active_tab`, `extract_page_text`, `click_element`, `fill_input`, `take_screenshot`).

3. **Agent Extension Tool Suite (`meridian_backend/src/tools/browser_extension_tools.py`)**:
   - `extension_get_active_tab()`: Returns current active URL, title, and page summary from user's logged-in Chrome.
   - `extension_extract_page(selector: Optional[str])`: Returns clean text and interactive element map from current page.
   - `extension_click(selector_or_text: str)`: Clicks button/link on active tab using real user session.
   - `extension_fill(selector: str, value: str, submit: bool)`: Types value into input field and optionally submits.
   - Auto-registers in `src/tools/registry.py` and `src/core/loop_stream.py`.

4. **Automated Fallback Cascade in Browser Agent**:
   - When user asks to browse or interact with a logged-in site (Google, YouTube, GitHub, Jira), agent first checks if Chrome extension is connected.
   - If connected: executes action via user's live browser session with zero profile locks.
   - If not connected: falls back cleanly to Playwright browser engine with helpful prompt explaining how to load extension.

5. **Unit Tests & Verification Gate**:
   - `meridian_backend/tests/test_browser_extension.py` with mock WebSocket extension client.
   - Pytest pass + frontend typecheck + extension manifest validation.

