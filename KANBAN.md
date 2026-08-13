# 📌 Meridian-X — Project Kanban Board

Last Updated: 2026-08-10

---

## 📋 Backlog (Future & Enhancements)

*All 28 Backlog items have been fully implemented, test-verified, and moved to the Completed section below!*

---

## 🎯 Planned (Active Sprint Roadmap & Core Architecture)

| ID | Task Name | Priority | Category | Target File(s) | Acceptance Criteria |
|---|---|---|---|---|---|
| **WAP-01** | **Local WhatsApp Contact Directory & Auto-Resolver** | 🔴 High | Communication/DB | `meridian_backend/src/tools/whatsapp_manager.py`, `database.py` | Store contact records (name, phone number, aliases like "Mom"/"Boss") in local MongoDB (`whatsapp_contacts`) and auto-resolve recipient names/aliases. |
| **WAP-02** | **Playwright WhatsApp Web Session & Message Puller** | 🔴 High | Communication/Web | `meridian_backend/src/tools/whatsapp_manager.py`, `registry.py` | Persistent WhatsApp Web session profile (`/meridian_memory/whatsapp_session`). Read recent messages (`read_whatsapp_messages`) and unread chat list (`list_whatsapp_chats`). |
| **WAP-03** | **Cross-Platform Smart WhatsApp Sender** | 🔴 High | Communication/Tools | `meridian_backend/src/tools/communication.py` | Upgrade `send_whatsapp_message()` with auto-contact resolution, multiline support, and WhatsApp Web URL / Desktop fallback for Windows, macOS, and Linux. |
| **AST-08** | **Continuous Conversation Window** | 🔴 High | Voice | `meridian_backend/src/voice/wakeword.py` | Keep an active 10-second listening window after responses so users can ask follow-ups without re-triggering the wake word. |
| **ECO-01** | **Mobile Companion App & QR P2P Sync** | 🔴 High | Cross-Device | `meridian_backend/src/core/p2p.py` | QR pairing with mobile devices, allowing mobile voice commands and streaming phone camera video into Meridian's vision engine. |
| **PL-01** | **Facial Recognition & Presence Engine** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision_face.py` | Real-time user presence, face recognition embeddings, and emotion tracking via MediaPipe/OpenCV. |
| **PL-02** | **Continuous Ambient Listener** | 🔴 High | Audio/STT | `meridian_backend/src/voice/ambient_listener.py` | Background VAD with `webrtcvad` + continuous `faster-whisper` transcription stream. |
| **PL-03** | **Real-Time Screen & Window Sense** | 🔴 High | Vision/Context | `meridian_backend/src/core/screen_sense.py` | Active window metadata tracking + vision LLM automated screen parsing on app switch/error. |
| **PL-04** | **Proactive Nudge Engine Expansion** | 🔴 High | Intelligence | `meridian_backend/src/core/proactive.py` | Event-driven context synthesis combining face, sound, screen, and system metrics. |
| **PL-05** | **Frontend Perception HUD & Hardware Toggles** | 🟡 Medium | UI/UX | `meridian_frontend/src/components/PerceptionHUD.tsx` | Visual webcam/mic indicators and hardware mute switches in `NavRail.tsx`. |
| **PL-06** | **Provider-Aware Multimodal Screen Vision** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision.py` | Route screen capture images directly to OpenAI (`gpt-4o`), Gemini (`gemini-1.5-flash`), or Anthropic (`claude-3-5-sonnet`) when API keys are used without Ollama. |
| **PL-07** | **Unified LLM Provider Code Auditor** | 🔴 High | Audit/Tools | `meridian_backend/src/tools/review.py` | Refactor code review tools to execute via `llm_provider.py` instead of hardcoded `ollama.Client()` calls. |
| **PL-08** | **Multi-Provider RAG Vector Embeddings Pipeline** | 🔴 High | Memory/RAG | `meridian_backend/database.py` | Add OpenAI `text-embedding-3-small` and in-memory CPU fallback (`fastembed`) when local Ollama `nomic-embed-text` is offline. |
| **PL-09** | **Multi-Cloud Vault Fallback Chain** | 🟡 Medium | AI Engine | `meridian_backend/src/core/llm_provider.py` | Fallback chain across vault API keys (Primary Cloud Provider $\rightarrow$ Secondary Cloud Provider $\rightarrow$ Local Ollama). |
| **PL-10** | **Heterogeneous Subagent Model Binding** | 🟡 Medium | Multi-Agent | `meridian_backend/src/core/swarm.py` | Bind subagent roles (Researcher, Auditor, Planner) to specific models (e.g. DeepSeek Coder for Auditor, Gemini Flash for Researcher). |
| **PL-11** | **Hybrid Sparse-Dense RAG & AST Code Chunking** | 🔴 High | RAG/Memory | `meridian_backend/src/core/doc_indexer.py` | Combine BM25 keyword matching with Turbovec dense vectors and AST function/class chunking. |
| **PL-12** | **Interactive Approval Gates for Destructive Actions** | 🔴 High | Security/Engine | `meridian_backend/src/core/loop.py` | Add UI human-in-the-loop (HITL) approval gates for destructive shell/database actions in the ReAct loop. |
| **PL-13** | **Mascot Visor Expressions & Micro-Emotions** | 🟡 Medium | UI/Mascot | `meridian_frontend/src/Mascot.tsx` | Dynamic SVG HUD visor eyes (`^ _ ^`, `> _ <`, `- _ -`) and sleeping `Zzz` particle micro-animations. |
| **PL-14** | **Mascot Real-Time Voice Audio Visualizer** | 🟡 Medium | UI/Audio | `meridian_frontend/src/Mascot.tsx` | Circular 8-bar audio equalizer orbit surrounding mascot reacting to STT/TTS audio frequencies. |
| **PL-15** | **Agent Loop Action Auras for Mascot** | 🟡 Medium | UI/Agent | `meridian_frontend/src/Mascot.tsx` | Action-specific mascot states (`browsing` web particles, `vision_scanning` sonar beam, `auditing` shield polygon). |
| **PL-16** | **Desktop Floating Pet Edge-Snapping & Drag Physics** | 🟢 Low | UI/Desktop | `meridian_frontend/src/Mascot.tsx` | Magnetic screen edge-snapping, drag physics, and interactive click reactions for floating pet mode. |
| **PL-17** | **Native Pure-Python PDF Layout & Table Extractor** | 🔴 High | RAG/Memory | `meridian_backend/src/tools/documents.py`, `meridian_backend/src/core/doc_indexer.py` | Native Python XY-Cut layout sorting (multi-column reading order) and bounding box table extraction for RAG indexing without Java or external repos. |
| **PL-18** | **Native OS System Toast Notification Integration** | 🔴 High | Integration/System | `meridian_backend/src/tools/communication.py` | Native Windows OS Toast / Balloon notification invocation (`System.Windows.Forms.NotifyIcon` / `BurntToast`) in `send_notification()` so AI background tasks trigger desktop system popups. |
| **PL-19** | **Collapsible Timeline Step Accordions & Diff Preview** | 🟡 Medium | UI/UX | `meridian_frontend/src/views/Timeline.tsx` | Group multi-step agent logs into collapsible step accordions and render syntax-highlighted code diff preview blocks. |
| **PL-20** | **Active Brain Model & Execution Mode Header Pill** | 🟡 Medium | UI/UX | `meridian_frontend/src/components/StatusBar.tsx`, `meridian_frontend/src/components/NavRail.tsx` | Persistent status badge showing active loaded model (e.g. Ollama vs Claude) and execution mode (Local vs Cloud/API). |
| **PL-21** | **Command Palette View Navigation & Action Toggles** | 🟢 Low | UI/UX | `meridian_frontend/src/components/CommandPalette.tsx` | Expand `Ctrl+K` command palette with view switching, model execution mode toggles, and shortcut indicators. |
| **PL-22** | **Inline Connection & API Key Health Checks** | 🟡 Medium | UI/UX | `meridian_frontend/src/views/Settings.tsx` | Real-time connection status badges for Ollama endpoint ping and vault API key validations directly within Settings. |
| **PL-23** | **User-Selected Model for Task Decomposition & Loop Helpers** | 🔴 High | AI Engine | `meridian_backend/src/core/loop.py` | Bind `decompose_goal_to_checklist` and internal loop helpers to active `brain_model` instead of hardcoded auditor model `qwen2.5-coder`. |
| **PL-24** | **Frontend Dynamic Model Source Lookup & LocalStorage Setter** | 🔴 High | UI/UX | `meridian_frontend/src/views/Timeline.tsx`, `meridian_frontend/src/Mascot.tsx` | Dynamically resolve execution mode from `MERIDIAN_MODEL_SOURCE` in `localStorage` instead of forcing `provider === 'ollama' ? 'local' : 'api'`. |
| **PL-25** | **Settings Page Execution Mode Toggle (Local vs Cloud/API)** | 🔴 High | UI/Settings | `meridian_frontend/src/views/Settings.tsx` | Add explicit UI toggle for Model Execution Mode (`Local` vs `Cloud/API`), allowing any provider to be configured in cloud mode. |
| **PL-26** | **Backend API Settings & Model Source Synchronization** | 🔴 High | Backend/API | `meridian_backend/api.py` | Read `MERIDIAN_MODEL_SOURCE` from user profile DB or env, persist updates, and pass to ReAct loop stream handler. |
| **PL-27** | **Anime.js UI Animation Integration** | 🟡 Medium | UI/UX | `meridian_website/package.json`, `meridian_website/src/` | Install `animejs` & `@types/animejs`, integrate Anime.js timeline animations, SVG morphing, and staggered transitions across website components. |
| **DEV-04** | **Paper2Code (PaperCoder) Integration** | 🔴 High | Multi-Agent AI | `meridian_backend/src/core/papercoder.py`, `meridian_backend/src/tools/registry.py`, `meridian_backend/api.py` | Scientific paper-to-repository multi-agent generator (Planning $\rightarrow$ Analysis $\rightarrow$ Code Generation) converting papers/arXiv into full runnable code repos. |
| **FIN-03** | **Real-Time Financial News Sentiment & Hybrid Stock Trend Sentinel** | 🔴 High | Personal Finance | `meridian_backend/src/core/finance_sentinel.py` | Financial news sentiment classifier & hybrid stock trend forecasting engine based on arXiv:1607.01958 & CEUR Vol-3026. |

| **PL-29** | **Vision Motion & Hand Gesture Control Sentinel** | 🔴 High | Vision/AI | `meridian_backend/src/core/vision_gesture.py` | MediaPipe/OpenCV hand gesture recognizer (thumbs up for HITL approve, open palm stop, wave, swipes) + desk motion presence tracker. |
| **PL-30** | **Geo-Location & Spatial Context Engine** | 🔴 High | Context / Web | `meridian_backend/src/core/geo_location.py`, `meridian_backend/src/tools/web.py` | IP & OS geolocation resolver injecting local spatial context (city, country, region) into web searches, local news, and executive weather briefings. |
| **JARVIS-02** | **Eye-Tracking & Spatial Gaze Control Sentinel** | 🔴 High | Vision/Perception | `meridian_backend/src/core/gaze_tracker.py` | MediaPipe Iris gaze tracker for hands-free window selection & automatic gaze-based screen dimming. |
| **JARVIS-03** | **Voice Biometric Identity & Speaker Verification** | 🔴 High | Voice/Security | `meridian_backend/src/voice/voice_biometrics.py` | Voiceprint embedding matcher blocking unauthorized background voice commands. |
| **JARVIS-04** | **Predictive Action Pre-Execution & Context Pre-Warmer** | 🔴 High | Intelligence | `meridian_backend/src/core/predictive_engine.py` | Workflow habit model pre-warming LLM context, opening dev tools, and pre-scaffolding git diffs. |
| **JARVIS-05** | **Smart Camera & RTSP Security Vision Sentinel** | 🟡 Medium | Vision/Security | `meridian_backend/src/core/camera_sentinel.py` | RTSP security camera stream object detector notifying room entry, package deliveries, or unknown visitors. |
| **JARVIS-06** | **Room Arrival Auto-Briefing & Voice Synthesizer** | 🟡 Medium | Voice/Assistant | `meridian_backend/src/core/presence_briefing.py` | Presence-triggered 15-second executive voice report upon entering workspace. |
| **JARVIS-07** | **Self-Healing System Defense & Thermal Governor** | 🔴 High | Security/System | `meridian_backend/src/core/system_defense.py` | Real-time RAM/CPU cache purging, rogue subprocess termination, and automated threat port isolation. |
| **JARVIS-08** | **Dynamic AR Smart Glasses & Headset Mirroring Bridge** | 🟡 Medium | AR / Hardware | `meridian_backend/src/core/ar_bridge.py` | WebSockets HUD streaming for XREAL, Meta Ray-Ban, and Apple Vision Pro headsets. |
| **JARVIS-09** | **Subconscious Codebase Memory & Neural RAG Synthesizer** | 🔴 High | Memory/RAG | `meridian_backend/src/core/neural_rag.py` | Background AST semantic synthesizer building real-time project intent knowledge graphs. |
| **JARVIS-10** | **Multi-Lingual Whisper & Real-Time Code Polyglot** | 🟡 Medium | Voice | `meridian_backend/src/voice/polyglot.py` | 50+ language real-time speech-to-code translator. |
| **JARVIS-11** | **Autonomous PR Reviewer & Automated Unit Test Generator** | 🔴 High | Developer Tools | `meridian_backend/src/core/auto_reviewer.py` | Writes pytest/jest unit tests for unstaged git diffs & generates pre-commit code review feedback. |
| **AST-15** | **Full-Duplex Voice & Live Voice Interrupt** | 🔴 High | Voice | `meridian_backend/src/voice/duplex_voice.py` | Full-duplex WebSocket audio streaming engine supporting instant barge-in voice interruption mid-sentence. |
| **DEV-05** | **Tree-Sitter Offline Codebase AST Graph** | 🔴 High | Developer Tools | `meridian_backend/src/core/code_graph.py` | AST dependency graph visualizer, symbol search, caller/callee tracing, & instant impact analysis. |
| **SYS-01** | **Smart Workspace Window Auto-Organizer** | 🟡 Medium | System Automation | `meridian_backend/src/core/workspace_layout.py` | Auto-arranges editor, terminal, browser, and Meridian HUD windows into mode presets (Dev, Research, Review). |
| **SEC-27** | **Ephemeral Sandboxed Code Execution Runner** | 🔴 High | Security / Sandbox | `meridian_backend/src/core/sandbox_runner.py` | Ephemeral Docker/WASM container sandbox with memory, CPU, and network bounds for unsafe code. |
| **OPT-01** | **Ultra-Lightweight Frontend RAM & Performance Engine** | 🔴 High | UI / Performance | `meridian_frontend/src/hooks/useMemoryOptimizer.ts`, `meridian_frontend/src/views/Settings.tsx` | View unmounting, list virtualization, blob GC, and Low-RAM CSS toggle reducing frontend RAM footprint to <45MB. |
---

## ⏳ In Progress

| ID | Task Name | Priority | Category | Target File(s) | Assignee / Status |
|---|---|---|---|---|---|
*(Ready for Day 3 implementation)*

---

## ✅ Completed (Code Implemented & Test-Verified)

| ID | Task Name | Priority | Category | Date Completed | Key Outcome |
|---|---|---|---|---|---|
| **WAP-01** | **Local WhatsApp Contact Directory & Auto-Resolver** | 🔴 High | Communication / DB | 2026-08-13 | Local MongoDB contact directory (`whatsapp_contacts`), contact resolution engine ("Mom" $\rightarrow$ `+1234567890`), and `manage_whatsapp_contacts` tool passing unit tests. |
| **WAP-02** | **Playwright WhatsApp Web Session & Message Puller** | 🔴 High | Communication / Web | 2026-08-13 | Persistent Playwright browser session (`/meridian_memory/whatsapp_session`), message reader (`read_whatsapp_messages`), and chat directory list tool passing unit tests. |
| **WAP-03** | **Cross-Platform Smart WhatsApp Sender** | 🔴 High | Communication / Tools | 2026-08-13 | Auto-resolving WhatsApp message tool (`send_whatsapp_message`) with cross-platform fallbacks (Desktop app & Web URL dispatch) passing unit tests. |
| **PL-12** | **Interactive Approval Gates for Destructive Actions** | 🔴 High | Security / Engine | 2026-08-13 | Human-in-the-loop (HITL) approval gate interceptor (`check_approval_gate`, `active_confirmations`) in `loop.py` passing unit tests. |
| **SEC-27** | **Ephemeral Sandboxed Code Execution Runner** | 🔴 High | Security / Sandbox | 2026-08-13 | Ephemeral process sandbox wrapper (`run_sandboxed_command`) in `sandbox_runner.py` with resource bounds passing unit tests. |
| **JARVIS-07** | **Self-Healing System Defense & Thermal Governor** | 🔴 High | Security / System | 2026-08-13 | Memory GC cache purger (`purge_system_caches`), health metrics monitoring, and rogue process isolate logic in `system_defense.py` passing unit tests. |
| **PL-18** | **Native OS System Toast Notification Integration** | 🔴 High | Integration / System | 2026-08-13 | Native OS Toast / Balloon notification popup runner (`send_native_toast_notification`) in `communication.py` passing unit tests. |
| **SEC-25** | **OAuth 2.0 Hybrid Auth & External Connector Engine** | 🔴 High | Security / OAuth | 2026-08-12 | PKCE flow, JWT validation in `auth.py`, encrypted token vault, external connectors for Gmail, Calendar, Contacts, GitHub, Cloudflare, Chat apps, and `/api/auth/oauth/*` endpoints passing unit tests (`test_oauth.py`). |
| **WKF-01** | **n8n-Style Node Workflow & Automation Engine** | 🔴 High | Automation / Engine | 2026-08-12 | Workflow DAG pipeline engine (`workflow_engine.py`), variable interpolation, webhook ingress gateway, `/api/workflows/*` API endpoints, and visual node builder component (`WorkflowBuilder.tsx`) passing unit tests (`test_workflow.py`). |
| **PL-28** | **Multi-Channel Proactive Event & Notification Engine** | 🔴 High | Intelligence / Notifications | 2026-08-09 | Multi-channel event bus dispatcher (`proactive.py`), main event loop binder (`set_main_event_loop`), terminal crash hook (`on_terminal_crash`), desk motion return trigger (`on_user_motion_return`), `send_proactive_notification` tool, and `POST /api/proactive/notify` API endpoint. |


| **DEV-01** | **Autonomous Background Bug Fixer & Auto-PR Agent** | 🔴 High | Autonomous AI | 2026-08-04 | `AutonomousBugFixer` pytest failure parser, git branch/commit manager, tool registry & `/api/swarm/auto-fix` API endpoint in `swarm.py`. |
| **SEC-07** | **Security Dashboard UI Panel** | 🟡 Medium | UI/Security | 2026-07-26 | Masked API key, audit log viewer & vault status panel in `SecurityPanel.tsx`. |
| **SEC-19** | **Localhost TLS (HTTPS) for Backend API** | 🟢 Low | Security / Infrastructure | 2026-07-26 | `configure_localhost_tls_cert` self-signed cert generator in `api.py`. |
| **SEC-21** | **HTTP Security Headers Middleware** | 🟢 Low | Security | 2026-07-26 | `HTTPSecurityHeadersMiddleware` injecting security headers in `security_middleware.py`. |
| **AST-09** | **Custom Voice Persona Engine** | 🟡 Medium | Voice | 2026-07-26 | `load_custom_voice_persona` voice model signature loader in `tts.py`. |
| **AST-14** | **Meeting Transcriber & Note Synthesizer** | 🟡 Medium | Audio / RAG | 2026-07-26 | `transcribe_meeting_call` multi-speaker meeting note synthesizer in `duplex.py`. |
| **DEV-03** | **Continuous Tech-Debt & Code Smell Radar** | 🟡 Medium | Developer Tools | 2026-07-26 | `scan_codebase_tech_debt_radar` AST code smell scanner in `graph_rag.py`. |
| **GAM-01** | **Real-Time AI Game Coach (`Alt+Space`)** | 🟡 Medium | Gaming / Vision | 2026-07-26 | Screen OCR and vision strategy tips panel in `GameOverlay.tsx`. |
| **GAM-02** | **Smart Power & Thermal Profile Switcher** | 🟢 Low | Hardware Control | 2026-07-26 | `switch_power_thermal_profile` FPS & thermal governor in `governor.py`. |
| **CRT-01** | **Local AI Visual Studio (ComfyUI / FLUX)** | 🟢 Low | Creative AI | 2026-07-26 | Graphic asset and icon synthesis panel in `LocalStudio.tsx`. |
| **CRT-03** | **Real-Time Voice Call Translator** | 🟡 Medium | Voice / AI | 2026-07-26 | `translate_voice_call_stream` speech translation engine in `duplex.py`. |
| **SEC-12** | **P2P Peer Authentication Challenge-Response** | 🔴 High | Networking / Security | 2026-07-26 | `authenticate_p2p_peer_challenge` HMAC challenge-response handshake in `p2p.py`. |
| **SEC-14** | **SSE Stream Session Integrity Token** | 🟡 Medium | Security | 2026-07-26 | `generate_sse_session_token` & `validate_sse_session_token` in `api.py`. |
| **SEC-15** | **Dependency Vulnerability Scanner (pip-audit)** | 🟡 Medium | Security / DevOps | 2026-07-26 | `run_pip_audit_vulnerability_scanner` background CVE scanner in `api.py`. |
| **SEC-22** | **Automatic API Key Rotation Scheduler** | 🟢 Low | Security | 2026-07-26 | `/api/security/rotate-key` endpoint & `rotate_meridian_api_key` helper in `api.py` & `auth.py`. |
| **FIN-02** | **Autonomous Tech & Market Research Digest** | 🟡 Medium | Research / AI | 2026-07-26 | `generate_tech_market_digest` briefing cards generator in `web_browser.py`. |
| **SEC-09** | **Shell Command AST-Parsed Denylist Engine** | 🔴 High | Security / Tools | 2026-07-26 | `validate_shell_ast_denylist` grammar-aware AST shell parser in `shell.py`. |
| **SEC-20** | **Immutable Audit Log with HMAC Chain** | 🟢 Low | Security / Compliance | 2026-07-26 | `_compute_hmac` & `verify_audit_chain` HMAC log chaining in `audit_logger.py`. |
| **SEC-23** | **Rogue Subprocess Isolation Monitor** | 🟢 Low | Security / Monitoring | 2026-07-26 | `monitor_rogue_subprocesses` child process monitor in `audit_logger.py`. |
| **AST-07** | **Adaptive Emotion & Tone Voice Modulation** | 🟡 Medium | Voice | 2026-07-26 | `get_adaptive_voice_params` pitch, pace & emotion modulator in `tts.py`. |
| **AST-12** | **Smart Home / Home Assistant Controller** | 🟢 Low | Integration | 2026-07-26 | `control_smart_home_device` device control dispatcher in `system.py`. |
| **FIN-01** | **Local Subscription & Expense Sentinel** | 🟡 Medium | Personal Finance | 2026-07-26 | `parse_receipt_subscription` local receipt & recurring expense parser in `documents.py`. |
| **CRT-02** | **Voice-Guided Presentation & Slide Deck Generator** | 🟡 Medium | Creative AI | 2026-07-26 | `generate_presentation_slide_deck` interactive Reveal.js deck generator in `exporter.py`. |
| **SEC-06** | **Trusted Origin Header Check Middleware** | 🟡 Medium | Security | 2026-07-26 | `TrustedOriginMiddleware` validating `Origin`/`Referer` headers on state-mutating requests in `security_middleware.py`. |
| **SEC-17** | **Telegram & Discord Bridge Sender Allowlist** | 🟡 Medium | Security / Messaging | 2026-07-26 | `MERIDIAN_ALLOWED_TELEGRAM_IDS` and `MERIDIAN_ALLOWED_DISCORD_IDS` sender allowlist checks in `telegram_bridge.py` & `discord_bridge.py`. |
| **SEC-24** | **Indirect Prompt Injection via Web Content** | 🔴 High | AI Security | 2026-07-26 | `sanitize_web_content_injection` stripping HTML comments & injection attacks in `web_browser.py`. |
| **AST-03** | **Daily Interaction & Thought Summarizer** | 🟡 Medium | Memory | 2026-07-26 | `summarize_daily_journal_entry` markdown journal compiler in `database.py`. |
| **AST-06** | **Smart Focus Guard & Digest** | 🟡 Medium | Productivity | 2026-07-26 | `toggle_focus_guard` & `generate_focus_digest` notification suppressor in `proactive.py`. |
| **AST-11** | **Media & Music Playback Controller** | 🟢 Low | Tools | 2026-07-26 | `control_media_playback` playback controls (play, pause, next, prev, volume) in `system.py`. |
| **SEC-11** | **Secrets Entropy Scanner for Prompt & Tool Output** | 🔴 High | AI Security | 2026-07-26 | `scan_and_redact_secrets` high-entropy token scanner & redactor in `llm_provider.py`. |
| **SEC-16** | **Clipboard Content Poison Detector** | 🟡 Medium | AI Security | 2026-07-26 | `sanitize_clipboard_poison` prompt injection stripper in `clipboard.py`. |
| **ECO-02** | **Universal Multi-Device Clipboard & File Drop** | 🟡 Medium | Cross-Device | 2026-07-26 | `sync_clipboard_to_peer` encrypted multi-device clipboard sync helper in `clipboard.py`. |
| **SEC-26** | **LLM Output Anomaly Detection Pre-Executor** | 🟡 Medium | AI Security | 2026-07-26 | `check_llm_tool_output_anomaly` pre-executor path & command anomaly detector in `loop.py`. |
| **AST-01** | **Personal Knowledge & Preference Graph** | 🔴 High | Personal Memory | 2026-07-26 | `extract_user_preference_node` entity-relationship graph in `temporal_memory.py`. |
| **AST-02** | **Daily Morning Executive Briefing** | 🔴 High | Assistant UI/Voice | 2026-07-26 | `generate_morning_briefing` aggregate digest in `proactive.py`. |
| **AST-04** | **Smart Workspace Macro Presets ("Modes")** | 🔴 High | Automation | 2026-07-26 | `apply_workspace_preset` macro presets in `system.py`. |
| **AST-05** | **Error-Aware Ghost Assistant** | 🔴 High | Proactive AI | 2026-07-26 | Compiler crash and terminal error analyzer in `watcher.py`. |
| **AST-10** | **Calendar & Email Assistant Integration** | 🔴 High | Integration | 2026-07-26 | Email drafting and calendar meeting invite parsing in `communication.py`. |
| **AST-13** | **Natural Language Tool Auto-Creator** | 🔴 High | Dynamic AI | 2026-07-26 | `create_dynamic_tool` AST validator & safe hot-reload register in `dynamic_manager.py`. |
| **DEV-02** | **Meridian-as-an-MCP-Server Integration** | 🔴 High | Developer Tools | 2026-07-26 | `/api/mcp/v1/tools` endpoint exposing Meridian tools as an MCP server for external IDEs in `api.py`. |
| **SEC-13** | **Filesystem Path Traversal Guard** | 🟡 Medium | Security / Tools | 2026-07-26 | `safe_path` validator blocking directory traversal attempts in `filesystem.py`. |
| **SEC-18** | **Database Query Injection Hardening** | 🟡 Medium | Security / Tools | 2026-07-26 | `validate_sql_safety` SQL injection guard in `db_query.py`. |

| **SEC-01** | **Global API Key Middleware Enforcement** | 🔴 High | Security | 2026-07-26 | Global `require_api_key` dependency on FastAPI routes with public endpoint whitelist (`/api/health`, `/api/debug/log`). |
| **SEC-02** | **Per-Endpoint Rate Limiting (slowapi)** | 🔴 High | Security | 2026-07-26 | Integrated `slowapi` rate limiter (20/min chat, 10/min vault, 60/min general) returning 429 on limit breach. |
| **SEC-03** | **Request Size & Input Validation Middleware** | 🟡 Medium | Security | 2026-07-26 | `MaxBodySizeMiddleware` 10MB payload cap + Pydantic `Field(max_length=...)` bounds on request models. |
| **SEC-04** | **Expanded Audit Logging (Auth & System Events)** | 🟡 Medium | Security | 2026-07-26 | Structured IP & request path audit logging for `AUTH_FAILURE`, `SHUTDOWN`, `PROMPT_INJECTION`, `CODE_EXEC_BLOCKED`. |
| **SEC-05** | **Vault Passphrase Hardening (Machine-Bound Derivation)** | 🔴 High | Security | 2026-07-26 | `HMAC-SHA256(MERIDIAN_API_KEY, hostname+user)` passphrase derivation with auto-migration from legacy passphrase. |
| **SEC-08** | **Prompt Injection Detection & Sanitizer** | 🔴 High | AI Security | 2026-07-26 | `prompt_injection.py` classifier & sanitizer stripping jailbreak signatures & zero-width unicode before LLM execution. |
| **SEC-10** | **Sandboxed `run_python` Host Fallback Lockdown** | 🔴 High | Security / Tools | 2026-07-26 | `MERIDIAN_ALLOW_HOST_CODE_EXEC` gate in `developer.py` blocking un-sandboxed host code execution when Docker is absent. |
| **SEC-25** | **Tool Call Permission Tier Enforcement Gate** | 🔴 High | AI Security / UX | 2026-07-26 | Tier 2 tool execution permission gate with audit logging and human-in-the-loop confirmation. |
| **BK-33** | **Linux Uncomposited Window Transparency Fallback** | 🟢 Low | UI/Desktop | 2026-07-26 | CSS `@supports` background fallback styling for uncomposited Linux window managers. |
| **BK-32** | **Linux Clipboard Fallback & Exception Handling** | 🟡 Medium | Tools | 2026-07-26 | `xclip`/`xsel`/`wl-clipboard` system checks and graceful `pyperclip` try/except error handling. |
| **BK-31** | **Cross-Platform POSIX Shell Launchers** | 🟢 Low | Developer Script | 2026-07-26 | POSIX bash scripts (`start_desktop.sh`, `start_meridian.sh`, `install.sh`) for macOS and Linux. |
| **BK-30** | **Cross-Platform System Autostart** | 🟡 Medium | System | 2026-07-26 | macOS `launchd` plist (`~/Library/LaunchAgents`) and Linux `.desktop` (`~/.config/autostart`) autostart support. |
| **BK-29** | **Multi-OS Standalone Installer Packaging Script** | 🟡 Medium | Build Script | 2026-07-26 | Updated installer discovery in `build_standalone.py` to copy `.dmg`, `.app`, `.deb`, and `.AppImage` packages. |
| **BK-28** | **Cross-Platform Tauri Installer Targets** | 🟡 Medium | Packaging | 2026-07-26 | Enabled `dmg`, `app`, `deb`, `appimage` bundle targets in `tauri.conf.json`. |
| **BK-27** | **Unix Backend Restart Script** | 🟡 Medium | Packaging | 2026-07-26 | Added `restart_backend.sh` shell script and updated Rust spawner in `lib.rs`. |
| **BK-26** | **Cross-Platform Tauri Binary Resolution** | 🔴 High | Packaging | 2026-07-26 | Dynamic `api.exe` (Windows) vs `api` (macOS/Linux) binary resolution in Tauri spawner. |
|---|---|---|---|---|---|
| **BK-25** | **Temporal Memory Graph Engine** | 🟡 Medium | Memory / Graph | 2026-07-25 | Time-aware knowledge graph tracking entity states, timestamped relationships, and exponential time-decay scoring in `temporal_memory.py`. |
| **BK-24** | **RAG Pipeline Context & Reranking Optimizer** | 🔴 High | Memory / RAG | 2026-07-25 | Hybrid dense-sparse BM25 retrieval, top-k relevance reranking, and noise reduction in `rag_optimizer.py`. |
| **BK-23** | **Reusable System Prompt & Tool Definition Library** | 🟡 Medium | AI Engine / Prompts | 2026-07-25 | Role-based system prompt template renderer and reusable tool JSON schemas in `prompt_templates.py`. |
| **BK-22** | **Active MCP Tool Execution Engine** | 🔴 High | Integration / Tools | 2026-07-25 | Async MCP tool discovery, execution state tracking, and JSON-RPC formatting in `mcp_executor.py`. |
| **BK-21** | **User-Configurable Token Context Limit UI & Backend Enforcement** | 🔴 High | AI Engine / UI | 2026-07-25 | Customizable context token limit controls (4k-128k, Custom) in `Settings.tsx` and dynamic budget enforcement in `loop.py`. |
| **BK-20** | **Custom ONNX Wake Word File Browser UI & Backend Scanner** | 🔴 High | Voice / UI | 2026-07-25 | Native OS file picker dialog & backend `.onnx` model scanner for custom wake words in `Settings.tsx` & `wakeword.py`. |
| **MC-01** | **Custom MCP Server Registration & Manager UI** | 🔴 High | Integration / UI | 2026-07-25 | Dynamic custom MCP server form (Name, Cmd, Args, Env), active server list, and `mcp_config.json` persistence. |
| **VK-02** | **Categorized API Key Navigation (AI Models & Voice Tabs)** | 🔴 High | UI/UX / AI | 2026-07-25 | Dedicated API key controls for Groq/OpenRouter/Mistral in AI Models tab, ElevenLabs/Deepgram in Voice tab, and secret vault integration. |
| **BK-19** | **Sub-10ms Frameless Game Overlay (`Alt+Space`)** | 🟢 Low | UI/UX | 2026-07-24 | Frameless transparent HUD component (`GameOverlay.tsx`) for full-screen games. |
| **BK-18** | **Event-Action Workflow Automation Engine** | 🟡 Medium | Automation | 2026-07-24 | Background metric trigger rules & automated action evaluator in `triggers.py`. |
| **BK-17** | **One-Click MCP Server Registry UI** | 🟡 Medium | Integration | 2026-07-24 | Dynamic catalog & installer for MCP servers (GitHub, Postgres, Linear, Slack) in `mcp_marketplace.py`. |
| **BK-16** | **Zero-Trust Noise Protocol P2P & Biometric Vault** | 🔴 High | Security/P2P | 2026-07-24 | ECDH key exchange & biometric enclave unlock fallbacks in `p2p_crypto.py`. |
| **BK-15** | **Model Benchmarker & Hardware Governor** | 🔴 High | System/AI | 2026-07-24 | Startup TTFT/tokens-sec benchmark probe & RAM/GPU thermal throttle governor in `governor.py`. |
| **BK-14** | **Global Spotlight Command Palette (`Cmd+K`)** | 🟢 Low | UI/UX | 2026-07-24 | Spotlight search modal component (`CommandPalette.tsx`) with fuzzy action execution. |
| **BK-13** | **Codebase Symbol AST Graph & RAG Indexer** | 🟡 Medium | Memory/RAG | 2026-07-24 | AST symbol relationship graph parser & background sleep-cycle memory consolidation in `graph_rag.py`. |
| **BK-12** | **Autonomous Playwright Web Browser Agent** | 🟡 Medium | Web/Tools | 2026-07-24 | Playwright browser agent tool (`browser_agent.py`) for page navigation & form interaction. |
| **BK-11** | **Real-Time Full-Duplex Voice & Barge-In** | 🔴 High | Voice | 2026-07-24 | Low-latency streaming STT/TTS pipeline with real-time speech interruption in `duplex.py`. |
| **BK-10** | **Multi-Agent Swarm Orchestration** | 🔴 High | Multi-Agent | 2026-07-24 | Spawns concurrent subagents (researcher, auditor, browser) via `asyncio.gather()` with report synthesis. |
| **BK-09** | **Background Noise Gate & Audio Thresholding** | 🔴 High | Audio | 2026-07-24 | Dynamic RMS spectral noise floor filter & attenuation in `stt.py`. |
| **BK-08** | **Structured `<thought>` Introspection Persistence** | 🟡 Medium | Agent Loop | 2026-07-24 | SQLite `thought_logs` table schema and SSE thought emitter hook. |
| **BK-07** | **Zeroconf/mDNS P2P LAN Discovery** | 🟡 Medium | Networking | 2026-07-24 | mDNS `zeroconf` service registration/discovery with UDP fallback in `p2p.py`. |
| **BK-04** | **Speaker Pitch Centroid Filtering** | 🟢 Low | Audio | 2026-07-24 | Pitch frequency ($F_0$) centroid tracker ($80\text{ Hz}-350\text{ Hz}$) in `stt.py`. |
| **VK-01** | **Universal Encrypted Secret Vault System** | 🔴 High | Security / AI | 2026-07-23 | Dynamic key manager in Settings with AES-GCM vault encryption & automatic Groq/OpenRouter/Mistral/SerpAPI resolution. |
| **IP-01** | Top-Left Mascot Logo Integration | 🔴 High | UI/UX | 2026-07-23 | Replaced SVG logo with glowing interactive `<MascotCharacter />` in `NavRail.tsx` (verified `npm run build`). |
| **IP-02** | CodeGraph Indexing & Symbol Sync | 🟡 Medium | DX / Tooling | 2026-07-23 | AST knowledge graph synchronization for workspace symbols. |
| **CB-01** | **Clipboard AI Analysis & Chatbot Routing** | 🟡 Medium | UX / Feature | 2026-07-23 | Routed automated clipboard monitoring analysis to main chatbot view with interactive copy controls. |
| **BK-01** | Split `loop.py` Monolith into Sub-modules | 🔴 High | Architecture | 2026-07-23 | Extracted `loop_parser.py`, `loop_dispatcher.py`, and `loop_stream.py`. |
| **BK-02** | Vault PBKDF2 to Argon2id Key Derivation | 🟡 Medium | Security | 2026-07-23 | Upgraded vault key derivation to `Argon2id` with PBKDF2 fallback. |
| **BK-03** | Persist P2P Peer List to SQLite | 🔴 High | Networking | 2026-07-23 | SQLite peer persistence table and health ping pruning daemon. |
| **BK-05** | Adaptive Token Budget Tracker & Context Trimming | 🔴 High | AI Engine | 2026-07-23 | Heuristic token estimator and history sliding-window budget trimmer in `loop_stream.py`. |
| **BK-06** | Vault Access Audit Logger | 🔴 High | Security | 2026-07-23 | Auditing read/write events via `audit_logger.py`. |
| **DN-01** | ReAct Reasoning Loop (`loop.py`) | 🔴 High | Core Engine | 2026-07-20 | Multi-step tool use, SSE streaming, syntax checks, self-correction. |
| **DN-02** | Voice Engine (STT & TTS & WakeWord) | 🔴 High | Audio | 2026-07-21 | Whisper STT, Edge/Coqui TTS, "Hey Meridian" wake word detection. |
| **DN-03** | Encrypted Vault (`vault.py`) | 🔴 High | Security | 2026-07-19 | AES-GCM credential & API key encryption. |
| **DN-04** | Discord & Telegram Bridges | 🟡 Medium | Messaging | 2026-07-22 | Bot integrations for remote command & control. |
| **DN-05** | Screen Vision Capture (`vision.py`) | 🟡 Medium | Vision | 2026-07-22 | On-demand screen capture via `mss`/`pyautogui` to Ollama Vision models. |
| **DN-06** | System Metrics Proactive Monitor | 🟡 Medium | Monitoring | 2026-07-22 | Background CPU/RAM/Disk anomaly alerts and idle checks. |
| **DN-07** | Vector Memory & RAG Pipeline | 🔴 High | Memory | 2026-07-18 | SQLite + ChromaDB memory vector storage. |
