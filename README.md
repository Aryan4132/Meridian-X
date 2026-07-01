# Meridian-X: Intelligent Desktop Workspace Companion

Meridian-X is an agentic, context-aware desktop development assistant built with **Tauri, React, FastAPI, SQLite, Turbovec, and local LLMs (Ollama)**. It is designed to act as an offline-first companion that monitors work progress, parses documents, executes secure python sandbox scripts, and secures local workspace environments.

---

## 🚀 Key Features

### 1. 🧠 ReAct Reasoning Agent Loop & Advanced Critique
* Runs an asynchronous **Reasoning ➔ Acting ➔ Observing** agent flow powered by local models (e.g., `qwen2.5-coder` or custom offline variants).
* Streams live reasoning timelines and thought patterns to the frontend using Server-Sent Events (SSE).
* **Critique & Self-Correction Engine**:
  * Intercepts tool calls and verifies parameter signatures in real-time using Python's `inspect.signature` against `TOOL_REGISTRY`. Automatically maps and heals parameter mismatches via `qwen2.5-coder:1.5b-instruct-q8_0`.
  * Validates code syntax using `ast.parse` for python executions (`run_python`), dynamic tool creations (`create_dynamic_tool`), and Python file writes (`write_file` targetting `.py` files).
  * Validates JSON format validity using `json.loads` for file writes targetting `.json` files.
  * Evaluates python scripts with a fast secondary LLM parser (`qwen2.5-coder:1.5b-instruct-q8_0`) to extract compiler warnings or logic bugs, feeding issues back to the main agent loop to trigger self-correction before execution.

### 2. ⚡ Speculative Concurrency Filtering
* Divides tool execution pathways between concurrent and sequential queues.
* **Tier 0 Read-Only Tools** (e.g. `read_file`, `list_directory`, `search_web`, `search_codebase`) run concurrently using `asyncio.gather()` to accelerate environment diagnostics and file inspection.
* **Tier >= 1 State-Modifying Tools** (e.g. `write_file`, `run_python`, `gui_click`) execute sequentially to maintain transaction integrity and prevent race conditions or database lockups.

### 3. 🦊 Interactive Mascot Companion & Island Mode
* A dedicated visual companion window that reflects the agent's active cognitive state in real-time.
* Supports visual reaction wardrobes:
  * 🕵️‍♂️ **Detective Hat**: Active during Security Auditor checks.
  * 👷‍♂️ **Construction Hat**: Active during codebase diagnostic audits and self-healing.
  * 🥱 **Tired State**: Triggers when offline fallbacks occur or during Pomodoro break cycles.
  * ✍️ **Typing State**: Reacts in real-time to user keystrokes.
* **Dashboard Close Redirection**: Closing the dashboard window (either via the UI's 'X' button or the native Close event) automatically prevents application shutdown and transitions the interface into mascot companion / island mode.

### 4. 🛡️ Security Auditor Consensus & Safety Gates
* Runs local security audits via an isolated validator model (`qwen2.5-coder:1.5b`) for any tool invocation of Tier 2 or higher.
* Uses an authorization safety gate for write/execution operations (Tier 3+), halting execution and awaiting explicit user validation from the chat pane.

### 5. 📊 P2P Swarm Dashboard & API Control
* Connects the local P2P mesh network daemon to FastAPI backend endpoints.
* View live telemetry of discovered LAN peer nodes, network host ports, connection latency status, and handshake validations directly from a dedicated "P2P Swarm" UI tab.
* Toggle the P2P daemon state or trigger manual synchronization across LAN peers on-demand.

### 6. ⚡ Context-Aware Resource Governor
* Monitors system usage to ensure developer performance is unaffected by background processes.
* Skips background intelligence tasks if:
  * System CPU utilization exceeds **85.0%**.
  * Foregrounds match heavy developer/gaming processes (e.g., *Valorant, Cyberpunk, Blender, Unity, Unreal, Visual Studio*).

### 7. 📄 Native Offline RAG Document Parser
* Deep file ingestion supporting `.txt`, `.md`, `.json`, `.csv`, `.pdf` (via `pypdf`), and `.docx` (via `python-docx`) natively.
* Seamlessly extracts and chunks documents, creating vector embeddings via local models (`nomic-embed-text`) and saving them into **Turbovec** (vector search) and **SQLite** (metadata storage).

### 8. ✏️ Rich Inline Code Merge Editor
* An interactive self-healing diff code panel.
* Displays character/line metadata count previews.
* Includes a **"Revert to Proposal"** button to allow instant resets of manual diff changes back to the original model proposal.

---

## 🏗️ Architecture Layout

```
                 +-----------------------------------+
                 |           Tauri Webview           |
                 |      (Vite + React Frontend)      |
                 +-----------------------------------+
                       /                       \
        Event Streams /                         \ IPC / HTTP
                     /                           \
                    v                             v
     +---------------------------+       +---------------------------+
     |      Mascot Companion     |       |      FastAPI Backend      |
     |          Window           |       |         (Python)          |
     +---------------------------+       +---------------------------+
                                           /           |           \
                                          /            |            \
                                         v             v             v
                              +------------+    +------------+    +------------+
                              |  Turbovec  |    |   SQLite   |    |  MongoDB   |
                              |  (Vectors) |    | (Metadata) |    |  (Graph)   |
                              +------------+    +------------+    +------------+
                                     \                 |                 /
                                      \                |                /
                                       v               v               v
                                    +-------------------------------------+
                                    |         Local Ollama Engine         |
                                    |     (Inference & Embeddings)        |
                                    +-------------------------------------+
```

---

## 🛠️ Getting Started

### Prerequisites
* **Python 3.10+** (in `meridian_backend/venv`)
* **Node.js** & **npm** (for the Tauri frontend)
* **Ollama** running locally with:
  * `ollama pull qwen2.5-coder:7b-instruct-q4_K_M` (standard reasoning)
  * `ollama pull qwen2.5-coder:1.5b-instruct-q8_0` (auditor validation & critique)
  * `ollama pull nomic-embed-text` (semantic RAG embeddings)

### Configuration (`.env`)
Create a `meridian_backend/.env` file with parameters:
```env
P2P_SECRET_TOKEN=your-secure-handshake-token
OLLAMA_HOST=http://127.0.0.1:11434
MERIDIAN_MODEL=qwen2.5-coder:7b-instruct-q4_K_M
```

### Running the System
You can launch the entire ecosystem using the main script in the workspace root:
```bash
# Start both backend and Tauri frontend
start_meridian.bat
```
Alternatively, run them in separate terminals:
1. **Backend**:
   ```bash
   cd meridian_backend
   venv\Scripts\python.exe api.py
   ```
2. **Frontend (Development Mode)**:
   ```bash
   cd meridian_frontend
   npm run tauri dev
   ```

---

## 📦 Production Builds & Startup Configuration

### Building the Installers
To build the optimized production version of the application:
1. Navigate to the frontend directory:
   ```bash
   cd meridian_frontend
   ```
2. Build the Tauri application:
   ```bash
   npm run tauri build
   ```
This compiles the Rust desktop wrapper and bundles the production binaries:
* **Setup EXE**: [meridian-x_0.1.0_x64-setup.exe](file:///C:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/executables/meridian-x_0.1.0_x64-setup.exe) (located in `executables/`)
* **MSI Installer**: [meridian-x_0.1.0_x64_en-US.msi](file:///C:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/executables/meridian-x_0.1.0_x64_en-US.msi) (located in `executables/`)

### ⚡ Launch on Startup
To configure the application to launch automatically when Windows starts up:
* **Via Settings UI**: Open the Meridian-X companion window, go to **Settings**, and toggle **Launch on Startup**.
* **Via CLI**: Run `python setup_startup.py` from the project root. (To disable, run `python setup_startup.py --disable`).

**How it works**: The startup script automatically checks for the compiled production binary (`meridian_frontend/src-tauri/target/release/app.exe`). If found, it runs the optimized binary directly without starting a dev server or recompiling Cargo, enabling an instant, silent boot. If not found, it falls back to development mode.

---
