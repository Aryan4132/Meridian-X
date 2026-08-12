# ⏳ Meridian-X — Day-by-Day Implementation Timeline

Daily schedule sequenced strictly by **priority/importance**, **security impact**, and **architectural dependency**.

---

## 📅 Day 1 — Foundation & Performance Boost (✅ Completed)
- **`OPT-01` — Ultra-Lightweight Frontend RAM & Performance Engine**
  - *Target*: `useMemoryOptimizer.ts`, `Settings.tsx`
  - *Deliverable*: Inactive tab unmounting, list virtualization, blob GC, and Low-RAM CSS toggle (<45MB RAM target).
- **`PL-30` — Geo-Location & Spatial Context Engine**
  - *Target*: `geo_location.py`, `web.py`
  - *Deliverable*: IP/OS location resolver, local spatial query bias, localized weather briefings.

---

## 📅 Day 2 — OAuth 2.0, External Connectors & n8n Workflow Engine (🔴 High Priority)
- **`SEC-25` — OAuth 2.0 Hybrid Auth & External Connector Engine**
  - *Target*: `oauth_manager.py`, `external_connectors.py`
  - *Deliverable*: Dual API key + Bearer JWT auth, PKCE login flow, encrypted OAuth token vault for Gmail, Calendar, Contacts, GitHub, and Cloudflare.
- **`WKF-01` — n8n-Style Node Workflow & Automation Engine**
  - *Target*: `workflow_engine.py`, `WorkflowBuilder.tsx`
  - *Deliverable*: Trigger/Action visual workflow runner (Webhook/Schedule/Email trigger $\rightarrow$ Filter $\rightarrow$ External Service Node $\rightarrow$ LLM step) executing n8n-style multi-step automation pipelines.

---

## 📅 Day 3 — Security Approval Gates, Sandbox & System Defense (🔴 High Priority)
- **`PL-12` — Interactive Approval Gates for Destructive Actions**
  - *Target*: `loop.py`
  - *Deliverable*: HITL UI approval modal for dangerous shell and database operations.
- **`SEC-27` — Ephemeral Sandboxed Code Execution Runner**
  - *Target*: `sandbox_runner.py`
  - *Deliverable*: Ephemeral Docker/WASM container sandbox with memory, CPU, and network bounds for unsafe code execution.
- **`JARVIS-07` — Self-Healing System Defense & Thermal Governor**
  - *Target*: `system_defense.py`
  - *Deliverable*: Real-time RAM/CPU cache purging, rogue process killer, and threat port isolation.
- **`PL-18` — Native OS System Toast Notification Integration**
  - *Target*: `communication.py`
  - *Deliverable*: Windows OS Balloon/Toast popups for background AI task completions.

---

## 📅 Day 4 — Execution Controls, Model Auditor & Auto PR Reviewer (🔴 High Priority)
- **`PL-07` — Unified LLM Provider Code Auditor**
  - *Target*: `review.py`
  - *Deliverable*: Route code review tools dynamically via `llm_provider.py` instead of hardcoded Ollama.
- **`PL-23` — User-Selected Model for Task Decomposition & Loop Helpers**
  - *Target*: `loop.py`
  - *Deliverable*: Bind internal loop helpers to user's selected `brain_model`.
- **`PL-24` — Frontend Dynamic Model Source Lookup & LocalStorage Setter**
  - *Target*: `Timeline.tsx`, `Mascot.tsx`
  - *Deliverable*: Dynamic execution mode resolution from `localStorage`.
- **`PL-25` — Settings Page Execution Mode Toggle (Local vs Cloud/API)**
  - *Target*: `Settings.tsx`
  - *Deliverable*: Explicit UI switch for `Local` vs `Cloud/API` model execution mode.
- **`PL-26` — Backend API Settings & Model Source Synchronization**
  - *Target*: `api.py`
  - *Deliverable*: Persist `MERIDIAN_MODEL_SOURCE` in profile DB and sync with ReAct stream handler.
- **`JARVIS-11` — Autonomous PR Reviewer & Automated Unit Test Generator**
  - *Target*: `auto_reviewer.py`
  - *Deliverable*: Writes pytest/jest unit tests for unstaged git diffs & generates pre-commit code review feedback.

---

## 📅 Day 5 — Full-Duplex Voice, Biometrics & Conversation Window (🔴 High Priority)
- **`AST-15` — Full-Duplex Voice & Live Voice Interrupt**
  - *Target*: `duplex_voice.py`
  - *Deliverable*: Full-duplex WebSocket audio streaming engine supporting instant barge-in voice interruption mid-sentence.
- **`AST-08` — Continuous Conversation Window**
  - *Target*: `wakeword.py`
  - *Deliverable*: 10-second active listening window following responses for follow-up speech without wake word.
- **`JARVIS-03` — Voice Biometric Identity & Speaker Verification**
  - *Target*: `voice_biometrics.py`
  - *Deliverable*: Voiceprint embedding matcher blocking unauthorized background voice commands.

---

## 📅 Day 6 — Codebase AST Graph, Neural RAG & PaperCoder (🔴 High Priority)
- **`DEV-05` — Tree-Sitter Offline Codebase AST Graph**
  - *Target*: `code_graph.py`
  - *Deliverable*: AST dependency graph visualizer, symbol search, caller/callee tracing, & instant impact analysis.
- **`JARVIS-09` — Subconscious Codebase Memory & Neural RAG Synthesizer**
  - *Target*: `neural_rag.py`
  - *Deliverable*: Background AST semantic synthesizer building real-time project intent knowledge graphs.
- **`DEV-04` — Paper2Code (PaperCoder) Integration**
  - *Target*: `papercoder.py`, `registry.py`
  - *Deliverable*: 3-stage paper-to-repository multi-agent generator converting arXiv/PDFs into runnable code repos.

---

## 📅 Day 7 — Multi-Provider RAG, PDF Extractor & Vault Fallback (🔴 High Priority)
- **`PL-08` — Multi-Provider RAG Vector Embeddings Pipeline**
  - *Target*: `database.py`
  - *Deliverable*: OpenAI `text-embedding-3-small` and in-memory `fastembed` fallback when local Ollama is offline.
- **`PL-11` — Hybrid Sparse-Dense RAG & AST Code Chunking**
  - *Target*: `doc_indexer.py`
  - *Deliverable*: BM25 keyword matching + Turbovec dense vectors + AST function/class boundary chunking.
- **`PL-17` — Native Pure-Python PDF Layout & Table Extractor**
  - *Target*: `documents.py`, `doc_indexer.py`
  - *Deliverable*: Pure-Python XY-Cut reading order sorting and bounding box table parser.
- **`PL-09` — Multi-Cloud Vault Fallback Chain**
  - *Target*: `llm_provider.py`
  - *Deliverable*: Automated failover chain across vault API keys (Primary Cloud $\rightarrow$ Secondary Cloud $\rightarrow$ Ollama).

---

## 📅 Day 8 — Ambient Perception, Vision Sense & Gesture Control (🔴 High Priority)
- **`PL-01` — Facial Recognition & Presence Engine**
  - *Target*: `vision_face.py`
  - *Deliverable*: Real-time face recognition embeddings, emotion tracking, and workspace user presence.
- **`PL-02` — Continuous Ambient Listener**
  - *Target*: `ambient_listener.py`
  - *Deliverable*: Background VAD with `webrtcvad` + continuous `faster-whisper` transcription stream.
- **`PL-03` — Real-Time Screen & Window Sense**
  - *Target*: `screen_sense.py`
  - *Deliverable*: Active window metadata tracking + vision LLM screen parsing on app switches.
- **`PL-04` — Proactive Nudge Engine Expansion**
  - *Target*: `proactive.py`
  - *Deliverable*: Event-driven context synthesis combining face, audio, screen, and system metrics.
- **`PL-06` — Provider-Aware Multimodal Screen Vision**
  - *Target*: `vision.py`
  - *Deliverable*: Direct screen capture routing to OpenAI `gpt-4o`, Gemini `gemini-1.5-flash`, or Claude `claude-3-5-sonnet`.
- **`PL-29` — Vision Motion & Hand Gesture Control Sentinel**
  - *Target*: `vision_gesture.py`
  - *Deliverable*: MediaPipe/OpenCV hand gesture recognizer (thumbs up for HITL, open palm stop, wave) + desk motion tracker.
- **`JARVIS-02` — Eye-Tracking & Spatial Gaze Control Sentinel**
  - *Target*: `gaze_tracker.py`
  - *Deliverable*: MediaPipe Iris gaze tracker for hands-free window selection & gaze-based screen dimming.

---

## 📅 Day 9 — Predictive AI, Financial Sentinel & Mobile Sync (🔴 High Priority)
- **`JARVIS-04` — Predictive Action Pre-Execution & Context Pre-Warmer**
  - *Target*: `predictive_engine.py`
  - *Deliverable*: Habit model pre-warming LLM context, opening dev tools, and pre-scaffolding git diffs.
- **`FIN-03` — Real-Time Financial News Sentiment & Stock Sentinel**
  - *Target*: `finance_sentinel.py`
  - *Deliverable*: Financial news sentiment classifier & hybrid stock trend forecasting engine.
- **`ECO-01` — Mobile Companion App & QR P2P Sync**
  - *Target*: `p2p.py`
  - *Deliverable*: Mobile QR pairing, remote voice command relay, and phone camera video stream ingestion.

---

## 📅 Day 10 — Subagent Model Binding, RTSP Camera & Polyglot (🟡 Medium Priority)
- **`PL-10` — Heterogeneous Subagent Model Binding**
  - *Target*: `swarm.py`
  - *Deliverable*: Role-based subagent model binding (DeepSeek Coder for Auditor, Gemini Flash for Researcher).
- **`JARVIS-05` — Smart Camera & RTSP Security Vision Sentinel**
  - *Target*: `camera_sentinel.py`
  - *Deliverable*: RTSP security camera stream object detector notifying room entry or visitors.
- **`JARVIS-06` — Room Arrival Auto-Briefing & Voice Synthesizer**
  - *Target*: `presence_briefing.py`
  - *Deliverable*: Presence-triggered 15-second executive voice report upon entering workspace.
- **`JARVIS-10` — Multi-Lingual Whisper & Real-Time Code Polyglot**
  - *Target*: `polyglot.py`
  - *Deliverable*: 50+ language real-time speech-to-code translator.

---

## 📅 Day 11 — AR Bridge, Workspace Layout & Perception HUD (🟡 Medium Priority)
- **`JARVIS-08` — Dynamic AR Smart Glasses & Headset Mirroring Bridge**
  - *Target*: `ar_bridge.py`
  - *Deliverable*: WebSockets HUD streaming for XREAL, Meta Ray-Ban, and Apple Vision Pro headsets.
- **`SYS-01` — Smart Workspace Window Auto-Organizer**
  - *Target*: `workspace_layout.py`
  - *Deliverable*: Auto-arranges editor, terminal, browser, and Meridian HUD windows into mode presets.
- **`PL-05` — Frontend Perception HUD & Hardware Toggles**
  - *Target*: `PerceptionHUD.tsx`, `NavRail.tsx`
  - *Deliverable*: Visual webcam/mic indicators and hardware mute switches.
- **`PL-20` — Active Brain Model & Execution Mode Header Pill**
  - *Target*: `StatusBar.tsx`, `NavRail.tsx`
  - *Deliverable*: Persistent status badge showing active loaded model and execution mode.
- **`PL-22` — Inline Connection & API Key Health Checks**
  - *Target*: `Settings.tsx`
  - *Deliverable*: Real-time connection status badges for Ollama and API keys.

---

## 📅 Day 12 — Mascot Expressions, Visualizer & UI Polish (🟡 Medium & 🟢 Low Priority)
- **`PL-13` — Mascot Visor Expressions & Micro-Emotions**
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Dynamic SVG visor eyes (`^ _ ^`, `> _ <`, `- _ -`) and sleeping particle animations.
- **`PL-14` — Mascot Real-Time Voice Audio Visualizer**
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Circular 8-bar audio equalizer reacting to STT/TTS frequencies.
- **`PL-15` — Agent Loop Action Auras for Mascot**
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Action-specific visual aura effects (browsing particles, vision sonar beam, auditing shield).
- **`PL-16` — Desktop Floating Pet Edge-Snapping & Drag Physics**
  - *Target*: `Mascot.tsx`
  - *Deliverable*: Screen edge-snapping, drag physics, and interactive pet click behaviors.
- **`PL-19` — Collapsible Timeline Step Accordions & Diff Preview**
  - *Target*: `Timeline.tsx`
  - *Deliverable*: Collapsible agent step accordions and code diff previews.
- **`PL-21` — Command Palette View Navigation & Action Toggles**
  - *Target*: `CommandPalette.tsx`
  - *Deliverable*: Extended `Ctrl+K` command palette with navigation and mode toggles.
- **`PL-27` — Anime.js UI Animation Integration**
  - *Target*: `meridian_website/package.json`, `src/`
  - *Deliverable*: Anime.js timeline animations, SVG morphing, and staggered transitions.
