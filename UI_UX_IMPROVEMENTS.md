# 🎨 Meridian-X — UI/UX Improvement Specification & Roadmap

Last Updated: 2026-07-23

---

## 1. Tabbed & Uncluttered Settings Navigation

To resolve visual clutter in **Settings**, the settings screen has been redesigned into **5 focused sub-categories**:

```
 ┌─────────────────────────────────────────────────────────────────────────────┐
 │ ⚙️ Settings: Configuration · Models · Appearance · Guard                    │
 ├─────────────┬──────────────────┬─────────────────┬──────────────┬───────────┤
 │ 💻 AI Models│ 🦊 Mascot & Style│ 🎤 Voice & Audio│ 🛡️ Guard & Sys│ 🔌 Connect│
 └─────────────┴──────────────────┴─────────────────┴──────────────┴───────────┘
```

### Category Breakdown

1. 💻 **AI Models**:
   - Primary Intelligence Provider selection (Ollama, OpenAI, Anthropic, Gemini, DeepSeek).
   - Brain Model, Vision Model, and Auditor/Fallback Model options.
   - Workspace override options (`.meridian.json`).

2. 🦊 **Mascot & Style**:
   - **Dynamic Island Screen Position** dropdown (`Top-Center`, `Bottom-Center`, `Top-Right`, `Bottom-Right`, `Top-Left`, `Bottom-Left`).
   - Theme Selection (Frost, Tokyo Storm, Abyss, Carbon, Noir OLED).
   - Mascot Sound FX toggle, TTS Voice Engine, and Speech Volume slider.

3. 🎤 **Voice & Audio**:
   - STT Whisper Model selection (`base`, `small`, `medium`, `large-v3`, `turbo`).
   - Wake Word ONNX model filename, phrase, and score threshold.
   - Voice Activity Detection (VAD) silence timeouts and amplitude thresholds.

4. 🛡️ **System Guard**:
   - Proactive Warning Limits (CPU %, RAM %, Disk %).
   - Distraction websites blocklist.
   - Desktop Game Mode toggle (hotkey suspension).
   - Launch on Startup toggle, Log Level, and MongoDB URI configuration.

5. 🔌 **Integrations & MCP**:
   - API Keys & Tokens (Tavily Search, Discord Bot Token, Telegram Bot & Chat ID).
   - Email Configuration (SMTP Email Address, App Password, Server & Port, IMAP).
   - Web Browser Tool viewport settings.
   - **Stdio MCP Servers Manager** (Add/Remove dynamic MCP tools).

---

## 2. Configurable Dynamic Island Screen Positioning

The **Dynamic Island** mascot window positioning system allows users to select their preferred screen location with instant live repositioning:

| Preset | Coordinates Math | Visual Aesthetic |
|---|---|---|
| 🍏 **Top-Center** | `x = (screenWidth - width) / 2`, `y = 16` | Apple Notch / Header style at the top of the display. |
| 📱 **Bottom-Center** | `x = (screenWidth - width) / 2`, `y = screenHeight - height - 60` | macOS Dock / Windows Taskbar center floating pill. |
| ↗️ **Top-Right** | `x = screenWidth - width - 16`, `y = 16` | Top-right HUD notification widget. |
| 📍 **Bottom-Right** | `x = screenWidth - width - 16`, `y = screenHeight - height - 60` | Tray corner floating widget *(Default)*. |
| ↖️ **Top-Left** | `x = 16`, `y = 16` | Top-left ambient status pill. |
| ↙️ **Bottom-Left** | `x = 16`, `y = screenHeight - height - 60` | Bottom-left status widget. |

---

## 3. Visual & Interactive Enhancements Roadmap

### A. Micro-Animations & Visual Aesthetics
- 🌊 **Audio Equalizer Waveform**: 3-bar animated sound wave in the Dynamic Island header when speech or ambient listening is active.
- 🟢 **Webcam & User Presence Glow Ring**: Dynamic status ring around the mascot orb (Emerald for recognized user, Amber for guest, Crimson for alert).
- 💎 **Glassmorphic Depth & Custom HSL Accents**: Translucent cards using `backdrop-filter: blur(16px)` and glowing border strokes.

### B. Interactive HUD & Proactive Nudge Cards
- ⚡ **Actionable Quick-Fix Buttons on Nudge Cards**: Single-click execution buttons (`[Fix Build Error]`, `[Mute Camera]`, `[Explain Code]`).
- 🔍 **Command Palette Overlay (`Ctrl+K` / `Cmd+K`)**: Global command search spotlight.
- ⌨️ **Keyboard Shortcuts Cheatsheet Overlay (`?` key)**: Quick hotkey modal for desktop navigation.

### C. System Telemetry & Perception HUD
- 📊 **Hardware Telemetry Mini-Gauges**: GPU VRAM and NPU utilization meters alongside CPU/RAM arcs.
- 🛡️ **Perception Status Bar**: Quick status indicators in `NavRail.tsx` (`📷 Face ON`, `🎤 Mic VAD ON`, `💻 Screen Sense ON`).
