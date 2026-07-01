# Meridian-X — Landing Page Website Copy & Content

This document outlines the structured website content, copy, and visuals to build a high-performance, modern product landing page for **Meridian-X**. You can feed this content directly into static site generators (like Astro, Next.js, Hugo, VitePress) or CMS editors to publish your website.

---

# Website Structure & Copy

## 1. Header (Navigation)
* **Logo**: Meridian-X Logo
* **Links**: Features | How It Works | Download | Docs
* **CTA Button**: Get Started (Scrolls to download section)

---

## 2. Hero Section
* **Tagline**: The Autonomous, Local Workspace Companion.
* **Sub-headline**: A context-aware desktop AI agent that reasons, self-corrects, and builds alongside you. 100% offline, secure, and privacy-first.
* **Primary CTA**: [Download for Windows (EXE)](#download)
* **Secondary CTA**: [View Source on GitHub](https://github.com/Aryan4132/Meridian-X)
* **Visual**: *[Placeholder: Interactive video/screenshot of the Tauri Desktop Shell with the Dynamic Island Mascot widget in action]*

---

## 3. Features Section (Grid Layout)

### 🧠 Offline-First Local Brain
* **Copy**: Powered by local LLMs via Ollama. Your code, prompts, and workspace context never leave your machine. No API keys, no subscriptions, zero data leaks.
* **Model Stack**: Optimized for `qwen2.5-coder:7b` (reasoning) and `nomic-embed-text` (semantic RAG).

### ⚡ Context-Aware Resource Governor
* **Copy**: Meridian-X works in harmony with your machine. It automatically scales down or pauses background scanning whenever high-CPU tasks, games (e.g., Valorant), or resource-heavy IDEs are active.

### 👷‍♂️ Self-Healing Diff Editor
* **Copy**: Features an inline merge editor that validates syntax and JSON formats in real-time. If an execution warning or bug is detected, the built-in critique engine automatically heals the code before executing it.

### 🦊 Interactive Mascot Widget
* **Copy**: A dynamic desktop island mascot that visually reflects the companion's current cognitive state (reasoning, auditing, or resting) and responds directly to your keystrokes.

### 🌐 Peer-to-Peer Swarm Sync
* **Copy**: Connect local workspace devices together over a secure, decentralized LAN peer-to-peer network. Synchronize memory state, code logs, and documents effortlessly.

---

## 4. How It Works (3-Step Guide)

### Step 1: Install the Companion
Download and run the compiled Windows installer. The Tauri shell registers global hotkeys (`Alt + M` to toggle dashboard) and launches a silent backend daemon.

### Step 2: Connect Local Ollama
Meridian-X uses local LLMs for inference. Open a terminal and run the standard model configuration:
```bash
ollama pull qwen2.5-coder:7b-instruct-q4_K_M
```

### Step 3: Start Building
Prompt the agent directly from the CLI, code pane, or desktop companion to analyze local files, run secure Python diagnostics, or search and audit your workspace.

---

## 5. Download Section (Call to Action) {#download}
* **Header**: Ready to meet your new development partner?
* **Subheader**: Free, open-source, and runs entirely on your local hardware.

| Platform | Installer Type | Direct Link | File Size |
| :--- | :--- | :--- | :--- |
| **Windows 10 / 11** | Standalone Installer (EXE) | [Download Setup EXE](https://github.com/Aryan4132/Meridian-X/raw/main/executables/meridian-x_0.1.0_x64-setup.exe) | ~2.8 MB |
| **Windows 10 / 11** | Enterprise Installer (MSI) | [Download MSI Installer](https://github.com/Aryan4132/Meridian-X/raw/main/executables/meridian-x_0.1.0_x64_en-US.msi) | ~3.8 MB |

---

## 6. System Requirements
* **Operating System**: Windows 10 or Windows 11 (with WebView2 Runtime installed).
* **AI Engine**: Ollama (v0.1.48+ recommended).
* **Developer Runtime**: Python 3.9+ (required to run secure python tools in the backend).
* **Hardware**: Recommended 16 GB+ RAM for smooth local model inference.

---

## 7. Footer
* © 2026 Meridian-X. Built by Aryan.
* Distributed under the MIT License.
