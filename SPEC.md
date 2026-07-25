# Spec: Meridian-X — Complete Backlog Mega Sprint (BK-11 to BK-19)

## Objective
Implement and deliver all 9 remaining backlog features in **Meridian-X**:
1. **BK-11 (Real-Time Duplex Voice & Barge-In)**: Low-latency streaming STT/TTS pipeline with real-time speech interruption handling.
2. **BK-12 (Autonomous Playwright Web Browser Agent)**: Web navigation, form filling, element interaction, and DOM snapshot extraction.
3. **BK-13 (Codebase Symbol AST Graph & RAG Indexer)**: Code symbol relationship graph parser and background sleep-cycle memory consolidation.
4. **BK-14 (Global Spotlight Command Palette)**: Quick action launcher component for commands, screen OCR, voice toggles, and Mascot control.
5. **BK-15 (Model Benchmarker & Hardware Governor)**: Startup model TTFT/tokens-sec probe and RAM/GPU thermal throttle governor.
6. **BK-16 (Zero-Trust Noise Protocol P2P & Biometric Vault)**: ECDH session key exchange and biometric enclave unlock fallbacks.
7. **BK-17 (One-Click MCP Server Registry UI)**: Dynamic MCP server installer and registry manager.
8. **BK-18 (Event-Action Workflow Automation Engine)**: User-defined trigger-action rules engine for automated background actions.
9. **BK-19 (Sub-10ms Frameless Game Overlay)**: Frameless floating HUD overlay widget for full-screen games and presentations.
10. **BK-20 (Custom ONNX Wake Word File Browser)**: Native OS & web file browser dialog with backend scanner for selecting custom `.onnx` wake word files.
11. **BK-21 (User-Configurable Token Context Limit)**: Selectable & custom token context limit controls in Settings UI and dynamic backend budget enforcement.
16. **BK-26 (Cross-Platform Tauri Binary Resolution)**: Dynamic `api.exe` vs `api` sidecar resolution.
17. **BK-27 (Unix Backend Restart Script)**: POSIX shell restart script and Rust spawner.
18. **BK-28 (Cross-Platform Tauri Installer Targets)**: Multi-OS bundle targets (`dmg`, `app`, `deb`, `appimage`, `nsis`, `msi`).
19. **BK-29 (Multi-OS Standalone Installer Packaging Script)**: Installer discovery for `.dmg`, `.app`, `.deb`, and `.AppImage`.
20. **BK-30 (Cross-Platform System Autostart)**: Support macOS `launchd` plist and Linux `.desktop` autostart.
21. **BK-31 (Cross-Platform POSIX Shell Launchers)**: Interactive and background bash scripts (`start_desktop.sh`, `install.sh`, `start_meridian.sh`).
22. **BK-32 (Linux Clipboard Fallback & Exception Handling)**: `xclip`/`xsel` dependency check and graceful `pyperclip` fallbacks.
23. **BK-33 (Linux Uncomposited Window Transparency Fallback)**: CSS solid background fallback styling for uncomposited Linux WMs.

## Tech Stack
- Backend: Python 3.13, PyTorch, faster-whisper, sounddevice, scipy, numpy, zeroconf, SQLite, Playwright.
- Frontend: React, TypeScript, Vite, Tailwind CSS, Lucide Icons.

## Commands
- Backend Tests: `pytest tests/`
- Frontend Build: `npm run build`

## Project Structure
```
meridian_backend/
├── src/
│   ├── core/
│   │   ├── governor.py            → BK-15 Model Benchmarker & Thermal Governor
│   │   ├── graph_rag.py           → BK-13 AST Symbol Graph & Memory Consolidation
│   │   ├── p2p_crypto.py          → BK-16 Noise Protocol ECDH P2P & Biometric Vault
│   │   └── triggers.py            → BK-18 Event-Action Workflow Automation Engine
│   ├── voice/
│   │   └── duplex.py              → BK-11 Low-Latency Duplex Voice & Barge-In Engine
│   └── tools/
│       ├── browser_agent.py       → BK-12 Autonomous Playwright Web Browser Agent
│       ├── mcp_marketplace.py     → BK-17 One-Click MCP Server Registry Manager
│       └── registry.py            → Tool registration
meridian_frontend/
└── src/
    ├── components/
    │   └── CommandPalette.tsx     → BK-14 Global Spotlight Command Palette (Cmd+K)
    └── views/
        └── GameOverlay.tsx        → BK-19 Sub-10ms Frameless Game Overlay (Alt+Space)
tests/                             → Comprehensive pytest suite
```

## Boundaries
- **Always**: Ensure zero breaking changes to existing REST endpoints and core agent loop.
- **Ask first**: Major database schema structural alterations.
- **Never**: Store unencrypted raw credentials or secrets in cleartext log files.

## Success Criteria
1. All 9 modules created, integrated, and registered cleanly.
2. `pytest` unit test suite passes with 0 failures across all backend modules.
3. `npm run build` succeeds cleanly in `meridian_frontend/`.
4. `KANBAN.md` updated with 100% backlog items completed.
