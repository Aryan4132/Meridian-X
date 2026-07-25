# Tasks — Meridian-X Complete Backlog Mega Sprint (BK-11 to BK-19)

- [x] Task 1: **BK-11 — Real-Time Duplex Voice & Barge-In Engine (`src/voice/duplex.py`)**
  - Acceptance: Implement `DuplexVoiceEngine` with continuous low-latency STT/TTS streaming, VAD barge-in speech cancellation, and turn state management.
  - Verify: Python import check `python -c "import src.voice.duplex"`.
  - Files: `meridian_backend/src/voice/duplex.py`

- [x] Task 2: **BK-12 — Autonomous Playwright Web Browser Agent (`src/tools/browser_agent.py`)**
  - Acceptance: Implement `AutonomousWebBrowser` tool with element interaction, page navigation, form filling, and DOM text snapshot extraction.
  - Verify: Python import check `python -c "import src.tools.browser_agent"`.
  - Files: `meridian_backend/src/tools/browser_agent.py`, `meridian_backend/src/tools/registry.py`

- [x] Task 3: **BK-13 — Codebase Symbol AST Graph & Memory RAG (`src/core/graph_rag.py`)**
  - Acceptance: Implement `CodebaseASTGraph` for symbol dependency parsing and background sleep-cycle memory consolidation.
  - Verify: Python import check `python -c "import src.core.graph_rag"`.
  - Files: `meridian_backend/src/core/graph_rag.py`

- [x] Task 4: **BK-14 — Global Spotlight Command Palette UI Component (`src/components/CommandPalette.tsx`)**
  - Acceptance: Build React `CommandPalette.tsx` modal component with `Cmd+K` / `Ctrl+K` keyboard shortcut, fuzzy search, and tool action triggering.
  - Verify: `npm run build`.
  - Files: `meridian_frontend/src/components/CommandPalette.tsx`

- [x] Task 5: **BK-15 — Model Benchmarker & Hardware Governor (`src/core/governor.py`)**
  - Acceptance: Implement `HardwareGovernor` for startup TTFT/tokens-sec model benchmark probing and RAM/GPU thermal throttle monitoring.
  - Verify: Python import check `python -c "import src.core.governor"`.
  - Files: `meridian_backend/src/core/governor.py`

- [x] Task 6: **BK-16 — Zero-Trust Noise Protocol P2P & Biometric Vault (`src/core/p2p_crypto.py`)**
  - Acceptance: Implement `NoiseP2PCrypto` ECDH session key exchange and biometric enclave unlock fallbacks.
  - Verify: Python import check `python -c "import src.core.p2p_crypto"`.
  - Files: `meridian_backend/src/core/p2p_crypto.py`

- [x] Task 7: **BK-17 — One-Click MCP Server Registry UI & Manager (`src/tools/mcp_marketplace.py`)**
  - Acceptance: Implement `MCPMarketplaceManager` for 1-click dynamic MCP server installation and tool registration.
  - Verify: Python import check `python -c "import src.tools.mcp_marketplace"`.
  - Files: `meridian_backend/src/tools/mcp_marketplace.py`, `meridian_backend/src/tools/registry.py`

- [x] Task 8: **BK-18 — Event-Action Workflow Automation Engine (`src/core/triggers.py`)**
  - Acceptance: Implement `WorkflowTriggerEngine` for background condition monitoring and automated action execution.
  - Verify: Python import check `python -c "import src.core.triggers"`.
  - Files: `meridian_backend/src/core/triggers.py`

- [x] Task 9: **BK-19 — Sub-10ms Frameless Game Overlay (`src/views/GameOverlay.tsx`)**
  - Acceptance: Build React `GameOverlay.tsx` frameless transparent HUD view triggered via `Alt+Space`.
  - Verify: `npm run build`.
  - Files: `meridian_frontend/src/views/GameOverlay.tsx`

- [x] Task 10: **Verify Full Suite & Update Kanban Board**
  - Acceptance: All unit tests pass cleanly (`pytest`), frontend builds without error (`npm run build`), and update `KANBAN.md`.
  - Verify: `pytest` and `npm run build`.
  - Files: `KANBAN.md`

- [x] Task 11: **BK-20 — Custom ONNX Wake Word File Browser UI & Backend Scanner**
  - Acceptance: Enable native OS & web file folder browser in `Settings.tsx` to pick custom `.onnx` wake word files, update backend path loading in `wakeword.py` to support absolute paths, and add `/api/voice/onnx-models` scanner endpoint in `api.py`.
  - Verify: Python import check and `npm run build`.
  - Files: `meridian_frontend/src/views/Settings.tsx`, `meridian_backend/src/voice/wakeword.py`, `meridian_backend/api.py`

- [x] Task 12: **BK-21 — User-Configurable Token Context Limit UI & Backend Enforcement**
  - Acceptance: Add token context limit dropdown presets (4k, 8k, 16k, 32k, 64k, 128k, Custom) in `Settings.tsx` and dynamically load user setting in `loop.py` for token estimation & 80% threshold compression warnings.
  - Verify: `pytest` and `npm run build`.
  - Files: `meridian_frontend/src/views/Settings.tsx`, `meridian_backend/src/core/loop.py`

- [x] Task 13: **BK-22 — Active MCP Tool Execution Engine (`src/core/mcp_executor.py`)**
  - Acceptance: Implement `McpToolExecutor` to manage active MCP client tool discovery, multi-server tool invocation, execution state tracking, and JSON-RPC tool result formatting.
  - Verify: Python import check `python -c "import src.core.mcp_executor"`.
  - Files: `meridian_backend/src/core/mcp_executor.py`

- [x] Task 14: **BK-23 — Reusable System Prompt & Tool Definition Library (`src/core/prompt_templates.py`)**
  - Acceptance: Implement template engine and registry for standardized agent system prompts and reusable tool JSON schemas.
  - Verify: Python import check `python -c "import src.core.prompt_templates"`.
  - Files: `meridian_backend/src/core/prompt_templates.py`

- [x] Task 15: **BK-24 — RAG Pipeline Context & Reranking Optimizer (`src/core/rag_optimizer.py`)**
  - Acceptance: Implement `RAGContextOptimizer` with BM25 + vector hybrid scoring, top-k relevance reranking, and token noise reduction.
  - Verify: Python import check `python -c "import src.core.rag_optimizer"`.
  - Files: `meridian_backend/src/core/rag_optimizer.py`

- [x] Task 16: **BK-25 — Temporal Memory Graph Engine (`src/core/temporal_memory.py`)**
  - Acceptance: Implement `TemporalMemoryGraph` to record timestamped entity state changes, temporal relationship links, and time-decay relevance scoring.
  - Verify: Python import check `python -c "import src.core.temporal_memory"`.
  - Files: `meridian_backend/src/core/temporal_memory.py`

- [x] Task 17: **Verify Backlog Suite & Update KANBAN.md to 100% Complete**
  - Acceptance: Run backend test suite (`pytest`) and update `KANBAN.md` moving completed backlog items to Done.
  - Verify: `pytest`.
  - Files: `KANBAN.md`



