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
                     /
                    v                             v
     +---------------------------+       +---------------------------+
     |      Mascot Companion     |       |      FastAPI Backend      |
     |          Window           |       |         (Python)          |
     +---------------------------+       +---------------------------+
                                           /           |           \
                                          /
                                         v             v             v
                              +------------+    +------------+    +------------+
                              |  Turbovec  |    |   SQLite   |    |  MongoDB   |
                              |  (Vectors) |    | (Metadata) |    |  (Graph)   |
                              +------------+    +------------+    +------------+
                                     \
                                      \                |                /
                                       v               v               v
                                    +-------------------------------------+
                                    |         Local Ollama Engine         |
                                    |     (Inference & Embeddings)        |
                                    +-------------------------------------+
```

---

## 💻 System Requirements & Hardware Specifications

Meridian-X utilizes a hybrid architecture: voice activation, local vector database storage (Turbovec), and desktop vision loops run locally, while the cognitive engine can run on either local LLMs or cloud provider APIs.

### Hardware Specifications

| Component | Minimum Requirement | Recommended Specification |
| :--- | :--- | :--- |
| **CPU** | Intel Core i5 / AMD Ryzen 5<br>(AVX2 instruction support required) | Intel Core i7 / AMD Ryzen 7 or higher<br>(8+ cores, high clock speed) |
| **RAM** | 8 GB DDR4/DDR5 | 16 GB or 32 GB DDR5 |
| **GPU / VRAM** | Intel Iris Xe / AMD Radeon Vega<br>(Shared system memory) | NVIDIA RTX 3060/4060 or higher<br>(Dedicated 8 GB+ VRAM) |
| **Storage** | 10 GB available SSD space | 30 GB+ NVMe SSD space |
| **Audio** | Standard Microphone & Output | Noise-canceling directional Microphone<br>(Required for the "Hey Meridian" Wake Word and Voice Agent loops) |

> [!IMPORTANT]
> **CPU vs. GPU Execution:**
> Running local models entirely on a CPU will result in slower token generation speeds (~2-5 tokens/sec). Having an NVIDIA GPU enables CUDA acceleration, boosting speeds to 30-60 tokens/sec.

> [!TIP]
> **Hybrid Cloud Mode (Lowers System Requirements):**
> By entering API keys for supported cloud providers (**OpenAI**, **Gemini**, **DeepSeek**, or **Anthropic**), the heavy cognitive execution is offloaded to remote server endpoints. In this mode, you only need the **Minimum Requirement** hardware specifications (8 GB RAM, standard CPU, no GPU) since only audio preprocessing, local database lookups, and orchestration will run on your machine.

### Supported Operating Systems
* **Windows**: Windows 11 64-bit (AMD64)
* **Linux/macOS**: Core sidecar compiles, but desktop shell target is optimized for Windows platform bindings.

---

## 🛠️ Getting Started & Installation

### Option A: Install via Pre-compiled Installers (Recommended)

1. **Download the Installer Package**:
   Get the compiled executables from the official release repository:
   [Download Meridian-X Installers](https://drive.google.com/drive/folders/1DWsJWrMqpqPnQLPXalazm60jVw1QsI65)

2. **Run the Installer**:
   Choose between two packaging formats available in the `executables/` directory:
   * **NSIS Setup EXE**: [meridian-x_0.1.0_x64-setup.exe](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/executables/meridian-x_0.1.0_x64-setup.exe) — A simple wizard-based installer.
   * **MSI Installer**: [meridian-x_0.1.0_x64_en-US.msi](file:///c:/Users/aryan/OneDrive/Dokumen/Mini_Project/Meridian-X/executables/meridian-x_0.1.0_x64_en-US.msi) — Recommended for enterprise environments.

3. **Launch the App**:
   Double-click the **Meridian-X** desktop shortcut to launch the client interface.

### Option B: Run from Source (Developer Mode)

#### 1. Setup Prerequisites
* **Python 3.10+** (run within a virtual environment)
* **Node.js** & **npm** (for the Tauri frontend)
* **Ollama** running locally

#### 2. Configure Ollama & Local Models
1. Download the installer from the official website: [Ollama.com](https://ollama.com/download).
2. Run the installer and ensure the Ollama icon is visible in your Windows system tray.
3. Open your terminal and pull the models required for your hardware tier:

   * **For Minimum Tier (8 GB RAM / CPU-only)**:
     ```bash
     # Brain / Coder Model
     ollama pull qwen2.5-coder:1.5b-instruct
     
     # Vision / Auditor / Embeddings
     ollama pull moondream:1.8b
     ollama pull qwen2.5-coder:1.5b-instruct-q8_0
     ollama pull nomic-embed-text
     ```

   * **For Recommended Tier (16 GB+ RAM / Dedicated GPU)**:
     ```bash
     # Brain / Coder Model
     ollama pull qwen2.5-coder:7b-instruct-q4_K_M
     
     # Vision / Auditor / Embeddings
     ollama pull llama3.2-vision:11b
     ollama pull qwen2.5-coder:1.5b-instruct-q8_0
     ollama pull nomic-embed-text
     ```

#### 3. Configuration (`.env`)
Create a `meridian_backend/.env` file with the following parameters:
```env
P2P_SECRET_TOKEN=your-secure-handshake-token
OLLAMA_HOST=http://127.0.0.1:11434
MERIDIAN_MODEL=qwen2.5-coder:7b-instruct-q4_K_M
```

#### 4. Running the System
You can launch the entire ecosystem using the main script in the workspace root:
```bash
# Start both backend and Tauri frontend
start_meridian.bat
```
Alternatively, run them in separate terminals:
1. **Backend**:
   ```bash
   cd meridian_backend
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   python api.py
   ```
2. **Frontend (Development Mode)**:
   ```bash
   cd meridian_frontend
   npm install
   npm run tauri dev
   ```

---

## ⚙️ Post-Installation Configuration

### First-Run Settings
Upon first launching, navigate to the **Settings** gear icon in the top right:
1. **Ollama Host URL**: Default is `http://localhost:11434`. If Ollama is running on a different device or port, update this.
2. **Cloud API Configurations (Optional)**:
   * To bypass local hardware limits, enter API keys for your preferred cloud provider (OpenAI, DeepSeek, Gemini, or Anthropic).
   * Once a key is saved, the settings dropdown will dynamically query and list the models available under that API key.
3. **Select Your Models**:
   * Use the dropdowns to select your **Brain**, **Vision**, and **Auditor** models.
   * Toggle **"Show all models"** to bypass capability filters and use custom text-only or experimental models.

### Testing Voice Wake Word
1. Toggle the **Mascot Voice** switch to Enabled.
2. Say **"Hey Meridian"** clearly. The UI mascot indicator will light up and transition into the listening state.
3. Test a simple command: *"Check system health"* or *"Audit workspace safety."*

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

## 🔍 Troubleshooting & Diagnostics

### 1. Local LLM / Ollama Unreachable
* **Symptom**: The UI shows "Ollama server unreachable" or "Failed to connect to http://127.0.0.1:11434". Error in backend logs: `httpx.ConnectError: [Errno 61] Connection refused`.
* **Solutions**:
  1. **Verify Service is Running**: Check if Ollama is running in your task tray (Windows/macOS) or run `systemctl status ollama` (Linux). Try opening `http://127.0.0.1:11434` in your browser. It should output: `"Ollama is running"`.
  2. **Configure Custom Host**: If Ollama is running on a different port or machine, update `OLLAMA_HOST` in your `.env` file (e.g. `OLLAMA_HOST=http://192.168.1.50:11434`).
  3. **Verify Models are Downloaded**: The semantic cache and LLM loop require the models to be downloaded locally. Run:
     ```bash
     ollama pull nomic-embed-text
     ollama pull qwen2.5-coder:7b-instruct-q4_K_M
     ollama pull qwen2.5-coder:1.5b-instruct-q8_0
     ```

### 2. Database Locked Error (SQLite)
* **Symptom**: Error in backend logs: `sqlite3.OperationalError: database is locked`.
* **Cause**: SQLite locks the database file when one process is writing and another tries to access/write. In Meridian-X, this can occur if backend threads or multiple instances access SQLite simultaneously.
* **Solutions**:
  1. **WAL Mode Enabled**: Meridian-X attempts to enable Write-Ahead Logging (WAL) mode automatically on startup, which allows concurrent reads and writes safely. Ensure that the database file has not been marked read-only.
  2. **Increase Timeout**: The connection timeout is configured to `10.0` seconds in `database.py`. Do not run multiple developer processes of `api.py` at the same time. Check for ghost processes:
     ```powershell
     Get-Process -Name python | Stop-Process -Force
     ```

### 3. MongoDB Connectivity Failures
* **Symptom**: Warning logs: `[MongoDB Graph] MongoDB offline, skipped fact saving`.
* **Cause**: MongoDB is utilized for storing structured knowledge graphs and smart clipboard history. If MongoDB is offline, Meridian-X is designed with **graceful degradation** and will continue functioning, storing core state in SQLite and Turbovec files.
* **Solutions**:
  1. **Start MongoDB Service**:
     * On Windows: Open `services.msc`, locate `MongoDB Server`, right-click and choose **Start**.
     * On Linux/macOS: Run `sudo systemctl start mongod` or `brew services start mongodb-community`.
  2. **Verify Port**: Make sure MongoDB is listening on the default port `27017` or update `MONGODB_URI` in `.env`.

### 4. Audio Input / Microphone Capture Degradation
* **Symptom**: Voice assistant does not register wake words (`Hey Meridian`). STT (Speech-to-Text) loops do not transcribe or throw `sounddevice` or `pyaudio` exceptions.
* **Solutions**:
  1. **Check OS Permissions**: Go to System Settings -> Privacy & Security -> Microphone and ensure that your terminal application has permission to access the microphone.
  2. **Verify Microphone Device**: Run `python verify_system.py` to check for active input channels. If your default input device is muted or sample rate is mismatched (e.g. not 16000Hz), adjust your sound control panel properties to `1 channel, 16-bit, 16000Hz (CD Quality)`.

### 5. High RAM/CPU Usage & Lag
* **Symptom**: High CPU lag, system stuttering.
* **Solutions**: Check that you are not loading models larger than your RAM capacity (e.g. attempting to run a 14B model on an 8 GB RAM device). Switch `MERIDIAN_MODEL` in settings or `.env` to a smaller quantized model size (e.g. `1.5b-instruct` or `3b-instruct`). Refer to the hardware capabilities scale:
  * **8 GB RAM (No GPU)**: `qwen2.5-coder:1.5b` (Brain) <br> `moondream:1.8b` (Vision)
  * **16 GB RAM / 6GB VRAM**: `qwen2.5-coder:7b-instruct-q4` (Brain) <br> `moondream:1.8b` (Vision)
  * **32 GB+ RAM / 12GB+ VRAM**: `qwen2.5-coder:14b` or `llama3:8b` (Brain)

---

## 🗺️ Roadmap
- [ ] **Multi-Agent Orchestration**: Support for specialized sub-agents for different coding languages.
- [ ] **Enhanced GUI Automation**: Deeper integration with Accessibility APIs for complex app interactions.
- [ ] **Dynamic Plugin Market**: Ability to load third-party toolsets dynamically.
- [ ] **Advanced Memory Graph**: Integration of temporal-aware knowledge graphs to track project evolution.

## 🤝 Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---
© 2026 Built by Aryan.