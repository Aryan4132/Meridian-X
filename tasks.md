# Tasks: Autonomous Browser-Use Engine for Meridian-X

## Task 1: Auto-Recovery, Set-of-Marks & Core Browser Actions in `src/tools/web_browser.py`

- [x] Ensure browser auto-opens (visible by default) if closed or uninitialized when any browser action is called.
- [x] Implement Set-of-Marks visual DOM indexing: `browser_get_interactive_elements()` and `browser_highlight_elements()` that injects numbered badges `[1]`, `[2]`, `[3]` over interactable buttons, inputs, links, select menus.
- [x] Support direct element actions by index: `browser_click_element(index_or_selector: str)` and `browser_type_element(index_or_selector: str, text: str, press_enter: bool = False)`.
- [x] Add `browser_press_key(key: str)` (supports "Enter", "Tab", "Escape", "ArrowDown", etc.).
- [x] Add `browser_scroll(direction: str = "down", amount: int = 500)`.
- [x] Add `browser_wait(seconds: float = 2.0)`.
- [x] Fix `test_web_browser_dom_fallback_click` mock in `tests/test_browser_agent.py`.

## Task 2: Autonomous "Browser Use" Agent Engine (`src/tools/browser_use_agent.py`)

- [x] Create `BrowserUseAgent` class inspired by `browser-use`:
  - Takes natural language instruction/goal (e.g. "search for latest AI papers on Google and get top 3 results", "go to youtube and play lofi").
  - Autonomous multi-step loop in real visible window:
    1. Extract page state & Set-of-Marks interactive element map `[1..N]`.
    2. Decide next action (`click(index)`, `type(index, text, enter=True)`, `press_key(key)`, `scroll()`).
    3. Execute action via Playwright on the live window.
    4. Observe feedback and verify goal progress.
  - Visible window execution with human-friendly logging so user watches actions happen live.
  - Auto-extracts target summaries, tables, or navigation outcomes.
- [x] Expose `browser_use_task(task: str, start_url: Optional[str] = None, max_steps: int = 10, visible: bool = True) -> str`.

## Task 3: Tool Registry & Signature Documentation

- [x] Register new browser tools in `src/tools/registry.py`:
  - `browser_use_task`
  - `browser_press_key`
  - `browser_scroll`
  - `browser_wait`
  - `browser_navigate`
  - `browser_interact`
- [x] Enhance `generate_tools_doc()` in `src/core/loop_parser.py` and `src/core/loop.py`:
  - Include parameter names and brief documentation for browser tools so LLM knows how to call `<call:browser_use_task>{"task": "..."}</call:browser_use_task>` or `<call:browser_open>{"url": "..."}</call:browser_open>`.
- [x] Update mode directives in `src/core/mode.py` to route web/browser tasks to browser tools.

## Task 4: Comprehensive Test Suite & Verification

- [x] Add unit and mock tests in `meridian_backend/tests/test_browser_use.py`.
- [x] Fix existing test failure in `tests/test_browser_agent.py`.
- [x] Verify test suite passes with `pytest`.
- [x] Verify frontend build and typecheck.

## Task 5: Browser Engine Multi-Tier Fallback & Environment Resilience

- [x] Auto-configure `PLAYWRIGHT_BROWSERS_PATH` to `%LOCALAPPDATA%\ms-playwright` in `src/tools/web_browser.py` if not set.
- [x] Add automatic fallback cascade in `_launch_engine` and persistent context in `browser_open`: Playwright Chromium -> Google Chrome channel -> Microsoft Edge channel -> binary path.
- [x] Update `BrowserUseAgent.run()` to catch browser launch errors and retry across alternative engines.
- [x] Update `nl_run` in `src/tools/shell.py` to accept `command` and `cmd` parameter aliases to prevent signature validation rejection.
- [x] Update `call_llm` in `src/core/llm_provider.py` to respect `MERIDIAN_PROVIDER` / user profile and check available API keys before blindly defaulting to `openrouter`.
- [x] Update `loop.py` to discard `Error:...` critique strings from consensus debate.
- [x] Add pytest tests in `tests/test_browser_fallback.py` to verify engine fallback, tool tolerance, and provider resolution.

## Task 6: Default to BrowserUseAgent & Remove Music Player Tool

- [x] Remove `play_youtube_music` and `verify_media_playing` from `src/tools/registry.py` and remove `src/tools/media_player.py`.
- [x] Ensure `control_media_playback` is provided by `src.tools.system` without reliance on `media_player.py`.
- [x] Set `BrowserUseAgent` (`browser_use_task`) as primary default browser engine in `mode.py` and `loop_parser.py`.
- [x] Update `tests/tool_scenarios.yaml`, `tests/test_tool_regression.py`, and `tests/test_butler_media.py`.
- [x] Run pytest to verify all tests pass.

## Task 7: Best-in-Class Tool Consolidation

- [x] Unify Browser Interaction: Route `browser_navigate` and `browser_interact` to use `web_browser.py` and Set-of-Marks visual actions rather than disconnected instances.
- [x] Upgrade Desktop Notifications: Route `send_notification` to `send_native_toast_notification` so real OS notifications fire.
- [x] Consolidate Code Review: Upgrade `review_diff` to use `auto_reviewer.py` (`review_git_changes`) for staged+unstaged coverage with secret redaction.
- [x] Register Universal Search: Add `universal_search` to `TOOL_REGISTRY` and `TOOL_SIGNATURES`.
- [x] Unify Clipboard Persistence: Update `clipboard_set` in `system.py` to record into `smart_clipboard` history.
- [x] Unify Scheduling Persistence: Route `schedule_task` and `schedule_once` through OS native scheduler with fallback.
- [x] Verify test suite passes.

## Task 8: Proactive Cognitive Mode & Autonomous Suggestions in Agent Loop

- [x] Add `PROACTIVE` cognitive mode to `MODE_DIRECTIVES` in `src/core/mode.py`.
- [x] Add proactive trigger keyword heuristics in `classify_mode()` in `src/core/mode.py`.
- [x] Implement `get_proactive_mode()` and `set_proactive_mode(enabled: bool)` with persistent user preference in `src/core/mode.py`.
- [x] Extend `<finish>` schema in `SYSTEM_PROMPT_TEMPLATE` with `proactive_suggestions` and proactive intelligence directive.
- [x] Update `process_final_response()` in `src/core/loop_parser.py` to preserve and validate `proactive_suggestions`.
- [x] Update `loop.py` to dispatch proactive suggestions via `event_bus` / `publish_nudge_sync` and stream SSE events.
- [x] Write comprehensive unit and integration tests in `tests/test_proactive_mode.py`.
- [x] Verify test suite passes with `pytest`.

## Task 9: Full Meridian-X Proactive Intelligence Suite

- [x] Task 9.1: Connect user desk arrival & camera presence to `PresenceBriefingEngine.generate_presence_briefing()`.
- [x] Task 9.2: Add proactive commit recommendations (`CommitWhisperer`) and breakage auto-fix suggestions (`WhatBrokeDetective`).
- [x] Task 9.3: Enhance `PredictiveContextPrewarmer` in `predictive_engine.py` for pre-warming diffs and RAG context.
- [x] Task 9.4: Implement 45-min continuous work ergonomics / stretch tracker & ambient focus mode in `proactive.py`.
- [x] Task 9.5: Add recurring tool sequence tracking and macro synthesis proposals in `self_evolving_tooling.py`.
- [x] Task 9.6: Create `tool_regression_sentinel.py` to continuously test tool matching heuristics.
- [x] Task 9.7: Add comprehensive test suite in `tests/test_full_proactive_suite.py` and verify all tests pass.

## Task 10: Advanced Proactive Automation & Reactive UI Suite

- [x] Task 10.1: Implement active workspace file scanning & ghost assistant alerts in `watcher.py` & `silent_workflow_guardian.py`.
- [x] Task 10.2: Implement mobile companion proactive away-bridge in `mobile_bridge.py` & `proactive.py`.
- [x] Task 10.3: Implement milestone autonomous memory consolidator in `memory_consolidation.py` / `proactive.py`.
- [x] Task 10.4: Implement proactive resource auto-healer in `proactive_system_guard.py`.
- [x] Task 10.5: Enhance frontend proactive action chips in `ProactiveGuardBanner.tsx` and dynamic mascot state propagation.
- [x] Task 10.6: Add comprehensive test suite in `tests/test_advanced_proactive.py` and verify all tests pass.

## Task 11: Production Daemon & Mascot Reactivity Integration

- [x] Hook `check_continuous_work_ergonomics` and `check_proactive_commits` into APScheduler in `src/core/scheduler.py` & `src/core/proactive.py`.
- [x] Wire live `watchdog.observers.Observer` with recursive workspace file watching, debouncing, and anomaly ghost scanner in `src/core/watcher.py`.
- [x] Synchronize real-time SSE proactive `mascot_state` through custom browser events into `Mascot.tsx` & `ProactiveGuardBanner.tsx`.
- [x] Run full test suite regression and TypeScript build validation.

## Task 12: Comprehensive UI/UX, Typography, and Fluid Ergonomics Overhaul

- [x] Task 12.1: Typography & Visual Design System in `index.css`:
  - Upgrade default `--font-main` to clean proportional font (`Inter`, -apple-system, sans-serif) for UI text, chat prose, buttons, and inputs.
  - Keep `--font-mono` (`JetBrains Mono`, `IBM Plex Mono`) for code snippets, badges, and timestamps.
  - Refine border contrast, elevation shadows, and glassmorphism styling.
- [x] Task 12.2: Smooth Tab Motion & Container Layout in `Shell.tsx`:
  - Replace abrupt `display: none` switches with smooth `AnimatePresence` and subtle fade-scale view transitions.
  - Ensure balanced responsive width filling across large monitor resolutions.
- [x] Task 12.3: Chat & Timeline HUD Redesign in `Timeline.tsx`:
  - Fix thinking cursor animation typo (`fontFamily` quote collision).
  - Add Empty State Hero with actionable quick-start chips (Audit Git, Review Code, Run Health Check, Start Focus).
  - Upgrade input HUD with floating glass card, auto-grow feeling, keyboard shortcuts hints, and focus glow ring.
  - Enhance message bubble distinction between User and Assistant.
- [x] Task 12.4: Tactile Micro-Interactions in `HoloButton.tsx` and interactive controls:
  - Add active tap scale physics (`whileTap={{ scale: 0.96 }}`) and smooth hover glow transitions.
- [x] Task 12.5: Verification & Quality Gate:
  - Run `npx --prefix meridian_frontend tsc --noEmit` and `npm --prefix meridian_frontend run build`.

## Task 13: Instant Agent Cancellation & Stop Interruption Pipeline

- [x] Task 13.1: Frontend Abort Binding in `Timeline.tsx`:
  - Pass `signal: controller.signal` to `fetch('/api/chat/stream')`.
  - In `handleInterrupt`: abort controller, clear task queue, post to `/api/chat/abort` and `/api/voice/interrupt`, display immediate stopped feedback card.
- [x] Task 13.2: Backend Cancellation Endpoints & Stream Disconnect in `api.py`:
  - Add `@app.post("/api/chat/abort")` and `/api/chat/stop`.
  - Catch `asyncio.CancelledError` and `GeneratorExit` in `run_react_agent_loop_wrapped` to interrupt the loop on client disconnect.
- [x] Task 13.3: Pervasive Checkpoints in `src/core/loop.py` & `src/tools/browser_use_agent.py`:
  - Check `_interrupt_event.is_set()` before processing tool calls, before each sequential tool call, after each tool call completes, and in `BrowserUseAgent.run()`.
- [x] Task 13.4: Verification:
  - Run `npm --prefix meridian_frontend run build` and `pytest meridian_backend/tests/test_advanced_proactive.py`.

## Task 14: Core Backend Architecture & Reliability Improvements

- [x] Task 14.1: Expand Secret Redaction & Hoist Imports in `src/core/llm_provider.py`
  - Add Anthropic (`sk-ant-`), Gemini (`AIzaSy`), and Hugging Face (`hf_`) regex patterns.
  - Hoist `log_sensitive_action` import outside inner pattern matching loop.
- [x] Task 14.2: Optimize Hardware Detection & VRAM Query in `src/core/hardware_detector.py`
  - Query `AdapterRAM` via PowerShell CIM on Windows to accurately calculate dedicated VRAM.
  - Add cached/memoized hardware profile with TTL to eliminate repeated slow process launches.
- [x] Task 14.3: Configurable Presets & Safe Process Execution in `src/core/workspace_orchestrator.py`
  - Support multiple presets (`coding`, `research`, `debugging`, `focus`) with customizable configurations.
  - Check executable paths using `shutil.which` before execution.
  - Add `stop_preset()` teardown capability.
- [x] Task 14.4: Provider-Agnostic LLM Planning in `src/tools/browser_use_agent.py`
  - Make `_plan_with_llm` use configured LLM provider from `src/core/llm_provider.py` instead of direct Ollama client hardcoding.
  - Increase LLM call timeout to 15s to avoid premature timeouts during DOM analysis.
- [x] Task 14.5: Decouple Tool Regression Suite in `test_tool_regression.py` & `tool_regression_sentinel.py`
  - Use `ToolRegressionSentinel.check_regressions()` and validate tool schemas against ToolRegistry.
  - Create `test_backend_improvements.py` to test hardware detection cache, workspace presets, secret redaction, and browser-use LLM fallback.
- [x] Task 14.6: Verification & Quality Gate
  - Run targeted backend pytest suites to ensure 100% test pass.

## Task 15: Unified Cognitive Graph Memory System

- [x] Task 15.1: Create `UnifiedCognitiveGraph` Engine in `src/core/cognitive_graph.py`
  - Implement SQLite backing (`cognitive_nodes`, `cognitive_edges`) with WAL mode.
  - Implement node/edge upsert, bidirectional lookups, and N-hop BFS graph traversal.
- [x] Task 15.2: Automated Cross-System Linking & Context Extraction
  - Add `auto_link_endpoints()` linking frontend routes to backend handlers.
  - Add `get_unified_context(query, max_hops=2)` returning formatted relationship subgraphs for LLM prompt injection.
- [x] Task 15.3: Register `query_cognitive_graph` Tool in `src/tools/registry.py`
  - Expose graph traversal and entity exploration as callable agent tool.
- [x] Task 15.4: Integrate Cognitive Graph in Agent Loop (`src/core/loop.py`)
  - Query cognitive graph for query entities and inject structured relationship context.
- [x] Task 15.5: Test Suite & Verification (`tests/test_cognitive_graph.py`)
  - Verify graph persistence, edge traversal, multi-hop discovery, and prompt enrichment.

## Task 16: Ultra-Low Latency & Anti-Chaos Voice I/O System

- [x] Task 16.1: Backend In-Memory Audio Streaming (`meridian_backend/api.py`)
  - Replace disk WAV file creation in `/api/tts` with direct `io.BytesIO` streaming.
  - Return streaming WAV response with zero disk footprint.
- [x] Task 16.2: Frontend Anti-Chaos Sequenced Audio Player (`meridian_frontend/src/Mascot.tsx`)
  - Implement `SequencedAudioPlayer` with monotonic sequence tracking (`expectedSeq`, `pendingChunks`).
  - Add `generationId` check on fetch completion to discard stale zombie audio.
  - Implement early clause chunking (trigger chunk 0 on first 3–5 words or comma).
  - Add explicit track cleanup on pause/interrupt/new prompt.
- [x] Task 16.3: Voice Input Speed & Web Speech API Integration (`Mascot.tsx` & `src/voice/stt.py`)
  - Add browser `webkitSpeechRecognition` support in `Mascot.tsx` for real-time local STT.
  - Optimize `stt.py`: default CPU fallback to `tiny.en`, eliminate 8.0s timeout hang on silence, and expose push-to-talk cutoff.
- [x] Task 16.4: Backend Voice Latency Unit Tests (`meridian_backend/tests/test_voice_speed.py`)
  - Test in-memory WAV generation, STT model fallback, and audio response headers.
- [x] Task 16.5: End-to-End Verification & Quality Gate
  - Run `pytest meridian_backend/tests/test_voice_speed.py`.
  - Run `npm --prefix meridian_frontend run build`.

## Task 17: Full-System Production Hardening, Anti-Chaos Audio & Cognitive Graph Overhaul

- [x] Task 17.1: Critical Process Kill Immunity & Guard Safety (`src/core/proactive_system_guard.py`)
  - Add explicit process whitelist (`os.getpid()`, parent PID, `explorer.exe`, `dwm.exe`, `csrss.exe`, `svchost.exe`, `python.exe` self, `System`).
  - Reject termination requests for protected processes with clear error.
- [x] Task 17.2: Desktop Notification Cooldown (`meridian_frontend/src/components/ProactiveGuardBanner.tsx`)
  - Implement per-PID notification timestamp tracking with 5-minute cooldown to prevent 15s notification loops.
- [x] Task 17.3: In-Memory Plaintext Key Zeroization (`src/core/vault.py`)
  - Add explicit zeroization for derived keys when cache expires or `freeze_vault()` is invoked.
- [x] Task 17.4: Streaming Clause TTS in Dashboard & Instant Stop (`meridian_frontend/src/views/Timeline.tsx`)
  - Replace full-response monolithic TTS with streaming clause chunking (<250ms TTFA on first words).
  - Clean up active audio immediately on interrupt or stop button click.
- [x] Task 17.5: Host-Level Audio Stop (`src/voice/tts.py` & `meridian_backend/api.py`)
  - Add `stop_active_tts()` with `threading.Event` and `sounddevice.stop()`.
  - Wire into `/api/voice/interrupt` and `/api/chat/abort`.
- [x] Task 17.6: Cognitive Graph FTS5 Search & Temporal Decay (`src/core/cognitive_graph.py`)
  - Enable FTS5 virtual table indexing for cognitive nodes.
  - Implement time-decayed scoring for transient task memories.
- [x] Task 17.7: Pre-Task Git Snapshot Rollback (`src/core/loop.py`)
  - Snapshot unstaged/staged workspace state before multi-step tasks to allow instant recovery on error.
- [x] Task 17.8: Full Verification & Quality Gate
  - Run all backend tests (`pytest`).
  - Run frontend typecheck and production build (`npm run build`).

## Task 18: Mobile APK Production Hardening, Android Permissions & Resilient WebSocket Pairing

- [x] Task 18.1: Android Manifest Permissions & Hardware Features (`meridian_mobile/android/app/src/main/AndroidManifest.xml`)
  - Add `RECORD_AUDIO`, `CAMERA`, `MODIFY_AUDIO_SETTINGS`, `ACCESS_WIFI_STATE`, `VIBRATE`.
  - Add non-blocking hardware features (`android.hardware.camera`, `android.hardware.microphone` with `required="false"`).
- [x] Task 18.2: Android Cleartext & LAN Network Security Config (`meridian_mobile/android/app/src/main/res/xml/network_security_config.xml`)
  - Create network security config allowing cleartext traffic for local networks and localhost.
  - Link in `AndroidManifest.xml` via `android:networkSecurityConfig="@xml/network_security_config"`.
- [x] Task 18.3: Resilient WebSocket URI Normalization & Query Parameters (`meridian_mobile/lib/core/websocket_client.dart`)
  - Automatically convert `http://` / `https://` schemas to `ws://` / `wss://`.
  - Ensure query parameters (`?token=...`, `?device_id=...`) are properly preserved and encoded without duplicate question marks.
- [x] Task 18.4: Remote Pairing Modal UX & Auto-Port Detection (`meridian_mobile/lib/views/remote_pairing_modal.dart`)
  - Add auto-fallback from port 4132 to port 4133 if primary port connection fails.
  - Add quick preset buttons for Emulator (`10.0.2.2`), Localhost (`127.0.0.1`), and standard LAN port (`4132` / `4133`).
- [x] Task 18.5: Flutter Unit Tests & Verification (`meridian_mobile/test/`)
  - Verify WebSocket client URI normalization and model serialization.
  - Run `flutter test`.
- [x] Task 18.6: Production APK Rebuild & Executable Packaging (`build_mobile.py`)
  - Run full release build to package verified APK into `executables/meridian-x_mobile.apk`.

## Task 19: Ultra-Low Latency Voice Engine & Accurate Multilingual Language Triage

- [x] Task 19.1: Fix False-Positive Hindi Detection (`meridian_backend/src/core/mode.py`)
  - Remove English stopwords (`"hi"`, `"to"`, `"ab"`, `"se"`, `"ko"`, `"ki"`, `"ka"`, `"ke"`) from `hinglish_keywords`.
  - Prevent 1-3 word English queries from triggering Hindi mode.
  - Require genuine multi-word Hinglish keywords or Devanagari script.
- [x] Task 19.2: Eliminate Unnecessary Transliteration Latency (`meridian_backend/src/core/loop_parser.py`)
  - Guard `transliterate_to_devanagari` to only execute when user/output language is explicitly Hindi with non-Devanagari text.
  - Never call transliteration on English responses, saving 2-6s LLM latency roundtrip.
- [x] Task 19.3: Fix Frontend Speech Chunking & Stream Dispatch (`meridian_frontend/src/Mascot.tsx` & `Timeline.tsx`)
  - In `Mascot.tsx`: feed incoming JSON finish response speech/chat directly to TTS chunk queue instead of dropping via `continue`.
  - In `Timeline.tsx`: feed JSON finish block speech to `feedTTS()` so voice response plays immediately.
- [x] Task 19.4: Unit Tests & Verification
  - Add pytest cases in `test_voice_speed.py` testing language detection accuracy on English sentences ("Hi", "Hi Meridian", "Talk to me", "How to run tests") vs Hinglish sentences ("kaise ho", "mera naam").
  - Verify TTS response streaming and run frontend typecheck.

## Task 20: 10/10 Architecture & Performance Hardening

- [x] Task 20.1: Decouple Consensus Debate into `consensus_engine.py` & Add Smart Gate
  - Extract debate logic out of monolithic `loop.py` into `meridian_backend/src/core/consensus_engine.py`.
  - Only run debate when code/system-mutating tools were executed or explicit code-generation occurred.
  - Skip debate for voice queries, greetings, and plain Q&A to eliminate 2-5s latency.
- [x] Task 20.2: Implement Unified Frontend Streaming Audio Player (`streamingAudioPlayer.ts`)
  - Create `meridian_frontend/src/services/streamingAudioPlayer.ts`.
  - Replace divergent ad-hoc audio chunk logic in `Timeline.tsx` and `Mascot.tsx` with shared player singleton.
  - Support instant interruption, sequential ordered playback, and memory cleanup.
- [x] Task 20.3: Replace Bare Silent Exceptions with Structured Logging
  - In `doc_indexer.py`, `cognitive_graph.py`, and `tts.py`, replace bare `except Exception: pass` with explicit structured logger warnings.
- [x] Task 21: Full-System Polish, Atomic Resilience, Repo Hygiene & Settings Modularization
  - [x] Task 21.1: Repo Hygiene: Delete accidental `meridian_backend/meridian_frontend/` and update `.gitignore`.
  - [x] Task 21.2: Frontend Dynamic Import: Fix `@tauri-apps/api/event` chunking warning in `ProactiveGuardBanner.tsx`.
  - [x] Task 21.3: Atomic JSON Storage: Implement `src/core/atomic_storage.py` and write unit tests in `tests/test_atomic_storage.py`.
  - [x] Task 21.4: Browser Agent Tool Cleanliness: Modernize `src/tools/browser_agent.py` to route to `browser_use_task` / `web_browser` with structured warning logs on fallbacks.
  - [x] Task 21.5: Frontend Settings Modularization: Extract tab views from `Settings.tsx` into `src/views/settings/` tabs.
  - [x] Task 21.6: Verification & Quality Gate: Run pytest and frontend build (`tsc --noEmit && vite build`).
- [x] Task 22: Background Three.js Optimization, Settings Decomposition & Signal Pruning
  - [x] Task 22.1: Pause Three.js render loop when `document.hidden` is true in `Mascot3DCharacter.tsx`.
  - [x] Task 22.2: Lazy-load `Settings` view with `React.lazy()` in `Shell.tsx`.
  - [x] Task 22.3: Convert console `print()` to `logger.info()` in `src/voice/wakeword.py` & clean imports in `tests/test_tools.py`.
  - [x] Task 22.4: Add timestamp TTL auto-pruning for `_cancel_signals` in `src/core/loop_stream.py`.
  - [x] Task 22.5: Extract `AiModelsTab.tsx`, `SystemGuardTab.tsx`, and `SpendAirGapTab.tsx` to complete Settings decomposition.
  - [x] Task 22.6: Verification & Quality Gate: Run pytest and frontend build (`tsc --noEmit && vite build`).
- [x] Task 23: Voice Daemon Logging Hygiene, Error Transparency & Settings Dead State Pruning
  - [x] Task 23.1: Replace all raw `print()` statements in `meridian_backend/src/voice/wakeword.py` with structured `logger` calls.
  - [x] Task 23.2: Replace all raw `print()` statements in `meridian_backend/src/voice/stt.py` with structured `logger` calls and harden temp audio cleanup.
  - [x] Task 23.3: Replace raw `print()` in `meridian_backend/src/api/voice.py` with `logger.error(..., exc_info=True)`.
  - [x] Task 23.4: Prune dead state hooks and orphaned handlers (`scannedOnnxModels`, `fetchScannedOnnxModels`) from `meridian_frontend/src/views/Settings.tsx`.
  - [x] Task 23.5: Run complete test suite and frontend typecheck / build verification.

## Task 24: Enterprise Security Hardening, Binary Swap Resilience, Perception API Safety, Session Interruption Isolation & Frontend Strict Type Safety

- [x] Task 24.1: Security Hardening: Remove wildcard CORS in `meridian_backend/api.py`, gate vault read/write routes in `meridian_backend/src/api/vault.py` with `require_permission(["admin", "user"])`, remove plaintext password dump in `save_google_app_password_api`.
- [x] Task 24.2: Updater Reliability: Windows binary rename-swap + `packaging.version.parse` in `meridian_backend/src/core/updater.py`.
- [x] Task 24.3: Perception API Safety: Use `webbrowser.open` in `meridian_backend/src/api/perception.py`, use `tempfile.NamedTemporaryFile` for screenshots, add Pydantic schemas for untyped endpoints.
- [x] Task 24.4: Agent Loop Session Isolation & Vault Durability: Session-scoped interruption tracking in `meridian_backend/src/core/loop.py` (`_session_interrupts`) + wire `atomic_write_json` in `meridian_backend/src/core/vault.py`.
- [x] Task 24.5: Frontend Strict Type Safety: Enable `"strict": true`, `"noImplicitAny": true` in `meridian_frontend/tsconfig.json` and resolve type checks.
- [x] Task 24.6: Verification & Quality Gate: Run pytest test suite and frontend typecheck & production build.

## Task 25: Loop Multi-Alias Remapping, VRAM Memoization, Stream Disconnect Hygiene & Frontend Compiler Hardening

- [x] Task 25.1: Multi-Alias Remapping: Remove premature `break` in `PARAM_ALIASES` in `meridian_backend/src/core/loop_executor.py`.
- [x] Task 25.2: VRAM Memoization: Add 5-second TTL cache for `get_gpu_vram_usage()` in `meridian_backend/src/core/llm_clients.py`.
- [x] Task 25.3: Stream Cancellation Hygiene: Cleanly handle `asyncio.CancelledError` and `GeneratorExit` with `logger.debug` in `meridian_backend/src/api/swarm.py`.
- [x] Task 25.4: Frontend Compiler Hardening: Add `"noFallthroughCasesInSwitch": true` and `"forceConsistentCasingInFileNames": true` in `meridian_frontend/tsconfig.json`.
- [x] Task 25.5: Verification & Quality Gate: Run pytest test suite and frontend typecheck & production build.

## Task 26: Tool Ecosystem Modernization, Dynamic Parameter Reflection & Execution Timeout Guard

- [x] Task 26.1: Dynamic Parameter Signatures: Upgrade `generate_tools_doc()` in `meridian_backend/src/core/loop_stream.py` with `inspect.signature` fallback for all tools.
- [x] Task 26.2: Canonical Tool Aliasing: Register `"shell"`, `"terminal"`, `"run_command"`, `"nl_run"`, and `"nl_to_shell"` in `TOOL_REGISTRY` in `meridian_backend/src/tools/registry.py`.
- [x] Task 26.3: Tool Execution Timeout Guard: Wrap `call_tool()` in `meridian_backend/src/tools/registry.py` with `asyncio.wait_for` (60s default, 180s extended) and graceful timeout recovery.
- [x] Task 26.4: Unit Test Suite: Create `meridian_backend/tests/test_tool_modernization.py` covering dynamic signatures, alias dispatch, and timeout handling.
- [x] Task 26.5: Verification & Quality Gate: Run pytest to verify all new and existing tool tests pass cleanly.

## Task 27: High-Impact Engineering Modernization & Immediate ROI Hardening

- [x] Task 27.1: CI Pipeline Modernization: Enhance `.github/workflows/verify.yml` with `ruff check` linting and formatting verification in backend job.
- [x] Task 27.2: Dependency Hygiene & pyproject.toml: Create root `pyproject.toml` with project metadata, version constraints, and ruff/mypy/pytest configs.
- [x] Task 27.3: Unified Structured Logging: Create `meridian_backend/src/core/logger.py` providing standard `get_logger(name)` with clean formatting and level configuration.
- [x] Task 27.4: Chat Router Extraction: Extract chat endpoints (`/api/chat/stream`, `/api/chat/abort`, `/api/chat/history`, etc.) from `meridian_backend/api.py` into `meridian_backend/src/api/chat.py`.
- [x] Task 27.5: Declarative `@tool` Decorator: Implement `@tool(name=None, tier=1, description=None)` decorator in `meridian_backend/src/tools/registry.py`.
- [x] Task 27.6: Verification & Quality Gate: Run full pytest suite, ruff lint check, and frontend production build.

## Task 28: Stream Back-Pressure, Architecture & Contributor Docs, Dead Code Pruning & Type Safety

- [x] Task 28.1: SSE Stream Cooperative Back-Pressure: Add `await asyncio.sleep(0)` after event yield in `meridian_backend/src/api/chat.py`.
- [x] Task 28.2: Architecture Documentation: Author `docs/architecture.md` detailing the 5-layer autonomous agent architecture.
- [x] Task 28.3: Contributor Guide: Author `CONTRIBUTING.md` documenting developer onboarding, ruff linting, pytest, and PR standards.
- [x] Task 28.4: Dead Code Pruning: Purge obsolete legacy scripts `cleanup.py` and `create_shortcut.py`.
- [x] Task 28.5: Type Safety & Validation: Add explicit types and docstrings across `meridian_backend/database.py` and `src/api/deps.py`.
- [x] Task 28.6: Verification & Quality Gate: Run full pytest suite, ruff linting, and frontend production build.

## Task 29: Silero VAD Integration for Whisper Transcription & Real-Time Audio Streaming

- [x] Task 29.1: Faster-Whisper VAD: Enable `vad_filter=True` and `VadOptions` in `meridian_backend/src/voice/stt.py` (`transcribe_audio_file` and `transcribe_audio_array`).
- [x] Task 29.2: Silero VAD Module: Implement `meridian_backend/src/voice/vad.py` with `SileroVADDetector` providing real-time frame speech probability calculation using bundled ONNX model and robust fallback.
- [x] Task 29.3: Live Recording Silence Cutoff: Update `record_and_transcribe` in `meridian_backend/src/voice/stt.py` to use `SileroVADDetector` for intelligent speech onset and silence termination.
- [x] Task 29.4: Duplex Barge-In & Ambient Detection: Enhance `DuplexVoiceEngine.check_barge_in` in `meridian_backend/src/voice/duplex.py` and `ContinuousAmbientListener` in `meridian_backend/src/voice/ambient_listener.py` with Silero VAD confidence.
- [x] Task 29.5: Unit Test Suite: Create `meridian_backend/tests/test_silero_vad.py` verifying transcription VAD, live frame detection, duplex barge-in, and ambient listener integration.
- [x] Task 29.6: Verification & Quality Gate: Run pytest test suite, ruff check, and verify all voice tests pass cleanly.

## Task 30: Production Keystore Signing & LAN Subnet Auto-Discovery for Mobile APK

- [x] Task 30.1: Production Keystore Signing in Gradle: Enhance `meridian_mobile/android/app/build.gradle.kts` to load `key.properties` for production release signing, falling back gracefully to debug keystore if absent.
- [x] Task 30.2: Keystore Automation & Gitignore: Update `meridian_mobile/.gitignore` and `build_mobile.py` with `--generate-keystore` helper and environment variable detection.
- [x] Task 30.3: LAN Subnet Discovery Service: Implement `meridian_mobile/lib/core/lan_discovery.dart` to discover local device IP subnet and probe for running Meridian Desktop endpoints (`:4132/api/health`, `:8765`).
- [x] Task 30.4: Remote Pairing Modal UX Integration: Update `meridian_mobile/lib/views/remote_pairing_modal.dart` with 1-click LAN Scan, visual feedback, and auto-population.
- [x] Task 30.5: Mobile Unit Tests: Expand `meridian_mobile/test/models_test.dart` to test LAN discovery candidate generation and keystore configuration checks.
- [x] Task 30.6: Verification & Quality Gate: Run `flutter analyze` and `flutter test` across mobile suite to ensure zero regressions.

## Task 31: Headless Web Research Optimization & Redundant Browser Suppression

- [x] Task 31.1: Mode Directives Update: Refine `MODE_DIRECTIVES["RESEARCHER"]` and `MODE_DIRECTIVES["AUTO"]` in `meridian_backend/src/core/mode.py` to prioritize headless tools and forbid parallel browser popping for queries.
- [x] Task 31.2: Dispatcher Redundant Call Suppression: Add guard in `meridian_backend/src/core/loop_dispatcher.py` to drop redundant `browser_use_task` when search tools are present in the same turn without explicit browser prompt.
- [x] Task 31.3: Unit Test Suite: Create `meridian_backend/tests/test_research_optimization.py` verifying mode directives, tool suppression logic, and non-suppression when browser is explicitly requested.
- [x] Task 31.4: Verification & Quality Gate: Run pytest test suite to ensure zero regressions across backend tests.

## Task 32: Audit Remediation & Core System Hardening

- [x] Task 32.1: Python 3.10 Syntax Fix in `meridian_backend/src/core/lsp_client.py` (eliminate backslash escape in f-string).
- [x] Task 32.2: Security Hardening:
  - Add AST validation & security filter in `meridian_backend/src/tools/dynamic_manager.py`.
  - Remove `shell=True` from `meridian_backend/src/core/workspace_orchestrator.py` & `meridian_backend/src/api/deps.py`.
  - Make draft reply author configurable in `meridian_backend/src/tools/external_connectors.py`.
- [x] Task 32.3: Lint & Code Quality Fixes:
  - Fix empty f-strings (F541) across backend files.
  - Fix duplicate imports / redefinitions (F811) in `auth.py`, `registry.py`, and `system_windows.py`.
  - Clean unused variables (F841) in `deps.py`, `loop_executor.py`, `lsp_client.py`, `scheduler.py`, `workflow_engine.py`, `browser_use_agent.py`, `expiry_sentinel.py`, `web.py`, `database.py`.
  - Fix `x not in y` membership test in `consensus_engine.py`.
  - Use `dotenv.load_dotenv` in `api.py`.
- [x] Task 32.4: Silent Exception Transparency:
  - Add structured `logger.debug` in `meridian_backend/src/core/proactive/guard.py`.
- [x] Task 32.5: Frontend Dependency Hygiene:
  - Move `@types/three` to `devDependencies` in `meridian_frontend/package.json`.
- [x] Task 32.6: Verification & Quality Gate:
  - Run pytest test suite, ruff check, and frontend build.
