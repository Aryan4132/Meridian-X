# Meridian-X — Release Checklist & Packaging Guide

This document captures the build validation steps, compilation requirements, and launch checklist to ensure stable desktop distribution across Windows, macOS, and Linux platforms.

---

## 1. Pre-Release Validation

Before building the installation binaries, execute the following validation steps locally:

1. **System Health Verification**:
   - Run the system verifier CLI to confirm your local development environment status:
     ```bash
     python verify_system.py
     ```
2. **Automated Test Coverage**:
   - Execute the backend python test suite:
     ```bash
     python meridian_backend/tests/run_tests.py
     ```
   - Ensure all tests pass.
3. **Frontend Compilation Check**:
   - In `meridian_frontend` directory, verify that typescript and frontend components build correctly:
     ```bash
     cd meridian_frontend
     npm run build
     ```
4. **Clean Workspace Logs**:
   - Clean up debug log files and temporary vector indexes to prevent packaging clutter:
     ```bash
     python cleanup.py
     ```

---

## 2. Compilation and Packaging

Meridian-X uses Tauri as a thin shell wrapping the React frontend, which in turn invokes/manages the FastAPI Python backend process sidecar.

### A. Windows Target (Primary Release)

1. **Compile Backend Standalone**:
   - Compiles the Python backend and virtual environment dependencies into a standalone executable:
     ```bash
     python build_standalone.py
     ```
   - This creates `meridian_backend.exe` under `executables` folder.
2. **Build Tauri Installer**:
   - Package frontend and sidecar into a Windows MSI/EXE installer:
     ```bash
     cd meridian_frontend
     npm run tauri build
     ```
   - The compiled installer will be saved under:
     `meridian_frontend/src-tauri/target/release/bundle/msi/`

### B. macOS Target (Secondary Release)

1. **Prerequisites**:
   - Xcode Command Line Tools installed (`xcode-select --install`).
   - Rust/Cargo and Node/npm configured.
2. **Compile Backend Standalone**:
   - Compile Python script into macOS bundle:
     ```bash
     python build_standalone.py
     ```
3. **Tauri Build & Code Signing**:
   - Generate macOS `.dmg` and `.app` bundles:
     ```bash
     cd meridian_frontend
     npm run tauri build
     ```
   - **Note**: For public distribution, Apple requires app signing and notarization via a valid Apple Developer Account certificate:
     ```bash
     # Define signing environment variables before building
     export APPLE_SIGNING_IDENTITY="Developer ID Application: Your Name (TeamID)"
     export APPLE_API_KEY_PATH="/path/to/AuthKey.p8"
     ```

### C. Linux Target (Tertiary Release)

1. **Build Debian & AppImage Packages**:
   - Ensure dependencies like `webkit2gtk` are installed:
     ```bash
     sudo apt-get install libwebkit2gtk-4.0-dev build-essential curl wget libssl-dev libgtk-3-dev libayatana-appindicator3-dev librsvg2-dev
     ```
   - Run the build command:
     ```bash
     cd meridian_frontend
     npm run tauri build
     ```
   - Binaries will be built under `src-tauri/target/release/bundle/deb/` and `src-tauri/target/release/bundle/appimage/`.

---

## 3. Post-Release Verification

Once installers are generated:

1. **Clean OS Installation**:
   - Install the generated package (e.g. MSI on Windows) on a fresh machine that lacks development dependencies.
2. **First-Run Setup Verification**:
   - Confirm the onboarding/setup wizard loads and registers initial settings.
   - Verify that the app correctly checks for local Ollama installation and nudges users to pull models if missing.
3. **Core Feature Smoke Tests**:
   - Test basic voice wake word response.
   - Check clipboard error monitoring and traceback notifications.
   - Check shell translation safety guard by attempting to run a destructive command.
