# ⏳ Meridian-X — Day-by-Day Implementation Timeline

Daily schedule sequenced by **architectural dependency**, **user priority**, and **test verification**.

---

## 📅 Day 1 — Foundation & Performance Boost
- **`OPT-01` — Ultra-Lightweight Frontend RAM & Performance Engine**
  - *Target*: `useMemoryOptimizer.ts`, `Settings.tsx`
  - *Deliverable*: Inactive tab unmounting, list virtualization, blob GC, and Low-RAM CSS toggle (<45MB RAM target).
- **`PL-30` — Geo-Location & Spatial Context Engine**
  - *Target*: `geo_location.py`, `web.py`
  - *Deliverable*: IP/OS location resolver, local spatial query bias, localized weather briefings.

---

## 📅 Day 2 — Vision Controls & Eye-Tracking
- **`PL-29` — Vision Motion & Hand Gesture Control Sentinel**
  - *Target*: `vision_gesture.py`
  - *Deliverable*: Hand gesture recognizer (thumbs up HITL approval, open palm stop, wave, swipes) + desk presence tracker.
- **`JARVIS-02` — Eye-Tracking & Spatial Gaze Control Sentinel**
  - *Target*: `gaze_tracker.py`
  - *Deliverable*: MediaPipe Iris gaze tracker for hands-free window selection & automatic gaze-based screen dimming.

---

## 📅 Day 3 — Voice Biometrics & Predictive AI
- **`JARVIS-03` — Voice Biometric Identity & Speaker Verification**
  - *Target*: `voice_biometrics.py`
  - *Deliverable*: Voiceprint embedding matcher blocking unauthorized background voice commands.
- **`JARVIS-04` — Predictive Action Pre-Execution & Context Pre-Warmer**
  - *Target*: `predictive_engine.py`
  - *Deliverable*: Habit model pre-warming LLM context, opening dev tools, and pre-scaffolding git diffs.

---

## 📅 Day 4 — Financial Sentiment & Research Paper Generators
- **`FIN-03` — Real-Time Financial News Sentiment & Hybrid Stock Trend Sentinel**
  - *Target*: `finance_sentinel.py`
  - *Deliverable*: Financial news sentiment classifier & hybrid stock trend forecasting engine (arXiv:1607.01958 & CEUR Vol-3026).
- **`DEV-04` — Paper2Code (PaperCoder) Integration**
  - *Target*: `papercoder.py`, `registry.py`
  - *Deliverable*: 3-stage paper-to-repository multi-agent generator converting arXiv/PDFs into runnable code repos.

---

## 📅 Day 5 — Codebase Graph & Autonomous Testing
- **`DEV-05` — Tree-Sitter Offline Codebase AST Graph**
  - *Target*: `code_graph.py`
  - *Deliverable*: AST dependency graph visualizer, symbol search, caller/callee tracing, & instant impact analysis.
- **`JARVIS-11` — Autonomous PR Reviewer & Automated Unit Test Generator**
  - *Target*: `auto_reviewer.py`
  - *Deliverable*: Writes pytest/jest unit tests for unstaged git diffs & generates pre-commit code review feedback.

---

## 📅 Day 6 — Ephemeral Sandbox & Full-Duplex Voice
- **`SEC-27` — Ephemeral Sandboxed Code Execution Runner**
  - *Target*: `sandbox_runner.py`
  - *Deliverable*: Ephemeral Docker/WASM container sandbox with memory, CPU, and network bounds for unsafe code.
- **`AST-15` — Full-Duplex Voice & Live Voice Interrupt**
  - *Target*: `duplex_voice.py`
  - *Deliverable*: Full-duplex WebSocket audio streaming engine supporting instant barge-in voice interruption mid-sentence.

---

## 📅 Day 7 — Room Security & Presence Intelligence
- **`JARVIS-06` — Room Arrival Auto-Briefing & Voice Synthesizer**
  - *Target*: `presence_briefing.py`
  - *Deliverable*: Presence-triggered 15-second executive voice report upon entering workspace.
- **`JARVIS-05` — Smart Camera & RTSP Security Vision Sentinel**
  - *Target*: `camera_sentinel.py`
  - *Deliverable*: RTSP security camera stream object detector notifying room entry, package deliveries, or unknown visitors.
- **`JARVIS-07` — Self-Healing System Defense & Thermal Governor**
  - *Target*: `system_defense.py`
  - *Deliverable*: Real-time RAM/CPU cache purging, rogue subprocess termination, and automated threat port isolation.

---

## 📅 Day 8 — Subconscious Memory, AR & Workspace Automation
- **`JARVIS-09` — Subconscious Codebase Memory & Neural RAG Synthesizer**
  - *Target*: `neural_rag.py`
  - *Deliverable*: Background AST semantic synthesizer building real-time project intent knowledge graphs.
- **`JARVIS-10` — Multi-Lingual Whisper & Real-Time Code Polyglot**
  - *Target*: `polyglot.py`
  - *Deliverable*: 50+ language real-time speech-to-code translator.
- **`JARVIS-08` — Dynamic AR Smart Glasses & Headset Mirroring Bridge**
  - *Target*: `ar_bridge.py`
  - *Deliverable*: WebSockets HUD streaming for XREAL, Meta Ray-Ban, and Apple Vision Pro headsets.
- **`SYS-01` — Smart Workspace Window Auto-Organizer**
  - *Target*: `workspace_layout.py`
  - *Deliverable*: Auto-arranges editor, terminal, browser, and Meridian HUD windows into mode presets (Dev, Research, Review).
