# Meridian-X Architecture

Meridian-X is an autonomous, multimodal, local-first desktop operating system and intelligent agent framework. It bridges host operating systems, multi-modal perception engines, local LLMs, and real-time frontend interfaces into a coherent reactive operating system.

---

## 1. Five-Layer Architecture Overview

```
┌────────────────────────────────────────────────────────────────────────┐
│                      Layer 5: Presentation & HUD                       │
│  Tauri v2 + React 19 + Vite | Three.js Mascot | SSE Streams | WebSockets│
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                    Layer 4: Cognitive & Reasoning Loop                 │
│  ReAct Agent Loop | Cognitive Modes | Consensus Debate | Swarm Teams  │
│          Multi-Provider LLM Orchestrator (Ollama / Cloud)             │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                  Layer 3: Tool Registry & Execution                    │
│   100+ Core Tools | Dynamic Inspection | Timeout Guard (60s/180s)      │
│     Host OS Shell (Powershell/Bash) | Playwright Browser Automation    │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                  Layer 2: Memory, Storage & Knowledge                  │
│  Unified Cognitive Graph | Turbovec Vector DB | Encrypted Vault (AES) │
│                Episodic Memory | Atomic JSON Storage                  │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │
┌───────────────────────────────────▼────────────────────────────────────┐
│                   Layer 1: Perception & System Guard                   │
│  Screen Sense / OCR | Whisper STT | OpenWakeWord | Gaze Tracking      │
│      Proactive Watchdog Observer | Hardware & Battery Sensors          │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Subsystems

### Layer 1: Perception & System Guard
- **Audio & Speech**: `src/voice/` manages hotword listening (`openwakeword`), local voice transcription (`faster-whisper`), and speech synthesis (`supertonic` / `pyttsx3`).
- **Vision & Screen**: `src/core/screen_sense.py` and `src/core/vision.py` capture real-time viewport frames, perform OCR, detect active windows, and provide multimodal situational awareness.
- **Proactive System Guard**: `src/core/proactive_system_guard.py` continuously monitors RAM, CPU, GPU VRAM, battery health, and anomalies.

### Layer 2: Memory, Storage & Knowledge
- **Unified Cognitive Graph**: `src/core/cognitive_graph.py` maps workspace AST symbols, backend endpoints, UI views, and conversational memories into a queryable relational graph.
- **Encrypted Secrets Vault**: `src/core/vault.py` provides AES-256 GCM encrypted storage (`vault.enc`) with atomic multi-process file writing (`src/core/atomic_storage.py`).
- **Vector Memory**: `database.py` and Turbovec indexing for dense semantic vector retrieval over historical sessions and indexed documentation.

### Layer 3: Tool Execution & Dynamic Capability
- **Tool Registry**: `src/tools/registry.py` provides centralized dispatch, tier permission gating (Tier 0: read-only, Tier 1: safe mutation, Tier 2: execution, Tier 3: destructive/gated), and declarative `@tool` registration.
- **Dynamic Reflection**: `src/core/loop_stream.py` inspects tool signatures at runtime (`inspect.signature`) so LLMs receive exact argument names.
- **Execution Resilience**: `call_tool()` wraps all synchronous and asynchronous operations with an `asyncio.wait_for` timeout guard (60s standard, 180s for browser and test suites).

### Layer 4: Cognitive & Reasoning Loop
- **ReAct Loop**: `src/core/loop.py` coordinates thought, tool selection, observation, critique, and answer generation.
- **Cognitive Modes**: `src/core/mode.py` dynamically steers the system prompt across specialized operational modes (`AUTO`, `PROACTIVE`, `ENGINEER`, `REVIEWER`, `OPERATOR`, `RESEARCHER`, `ANALYST`).
- **Consensus Debate**: `src/core/consensus_engine.py` invokes dual-model peer critique for mutating actions and code changes.
- **Swarm Orchestrator**: `src/core/swarm.py` spawns concurrent subagents (auditors, researchers, coders) for parallel multi-step goals.

### Layer 5: Presentation & Client Interfaces
- **Desktop HUD**: Tauri v2 wrapper hosting a React 19 application (`meridian_frontend/`), featuring 3D avatar animations via Three.js (`Mascot3DCharacter.tsx`), fluid Framer Motion transitions, and a cybernetic dark HUD.
- **Event Streaming**: SSE stream pipeline (`/api/chat/stream`) transmitting thoughts, text chunks, tool invocation indicators, and proactive suggestion chips with cooperative generator yields.
- **Mobile Bridge**: Full-duplex WebSocket bridge (`/ws/mobile`) for Tauri v2 Android companion integration.
