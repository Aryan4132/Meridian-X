#!/usr/bin/env python
"""
Meridian-X Standalone Desktop Builder
Compiles Python backend sidecar (PyInstaller) and packages Tauri desktop shell into executables/.
"""

import os
import sys
import glob
import json
import re
import shutil
import subprocess
import platform
from typing import Optional


def run_cmd(cmd: str, cwd: Optional[str] = None) -> None:
    """Run a shell command with error checking."""
    print(f"\n[Run] {cmd} (cwd: {cwd or '.'})")
    res = subprocess.run(cmd, shell=True, cwd=cwd)
    if res.returncode != 0:
        print(f"[Error] Command failed with exit code: {res.returncode}")
        sys.exit(res.returncode)


def get_current_version(root_dir: str) -> str:
    """Extract current app version from meridian_frontend/package.json."""
    pkg_path = os.path.join(root_dir, "meridian_frontend", "package.json")
    if os.path.exists(pkg_path):
        try:
            with open(pkg_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data.get("version", "")
        except Exception as e:
            print(f"[Warning] Failed to read version from package.json: {e}")
    return ""


def clean_old_version_executables(executables_dir: str, current_version: str) -> None:
    """Audit executables directory and clean outdated installer packages."""
    if not os.path.exists(executables_dir):
        os.makedirs(executables_dir, exist_ok=True)
        return

    print(f"Auditing executables directory for version '{current_version}'...")
    for f in os.listdir(executables_dir):
        file_path = os.path.join(executables_dir, f)

        # Check for version pattern in filename (e.g. meridian-x_0.1.2_x64-setup.exe)

        ver_match = re.search(r"(\d+\.\d+\.\d+)", f)
        if ver_match:
            file_ver = ver_match.group(1)
            if file_ver != current_version:
                print(f"Clearing old version executable: {f} (v{file_ver} != v{current_version})")
                try:
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)
                except Exception as e:
                    print(f"Failed to remove old file {f}: {e}")


def main() -> None:
    root_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root_dir, "meridian_backend")
    frontend_dir = os.path.join(root_dir, "meridian_frontend")
    
    sidecar_only = "--sidecar-only" in sys.argv or "--backend-only" in sys.argv

    # ---------------------------------------------------------
    # 1. Check/Install PyInstaller in backend virtual environment
    # ---------------------------------------------------------
    print("=== Step 1: Checking and Installing PyInstaller in Virtualenv ===")
    
    if platform.system() == "Windows":
        pip_exe = os.path.join(backend_dir, "venv", "Scripts", "pip.exe")
        pyinstaller_exe = os.path.join(backend_dir, "venv", "Scripts", "pyinstaller.exe")
    else:
        pip_exe = os.path.join(backend_dir, "venv", "bin", "pip")
        pyinstaller_exe = os.path.join(backend_dir, "venv", "bin", "pyinstaller")
        
    if not os.path.exists(pip_exe):
        print(f"[Error] Python virtual environment pip not found at: {pip_exe}")
        print("Please setup virtual environment first by running start_desktop.bat.")
        sys.exit(1)
        
    run_cmd(f'"{pip_exe}" install pyinstaller', cwd=backend_dir)

    # ---------------------------------------------------------
    # 2. Compile Backend with PyInstaller
    # ---------------------------------------------------------
    print("\n=== Step 2: Compiling Python Backend with PyInstaller ===")
    
    # Clear old build/dist directories
    for folder in ["build", "dist"]:
        path = os.path.join(backend_dir, folder)
        if os.path.exists(path):
            print(f"Clearing old {folder} directory...")
            shutil.rmtree(path)
            
    # Add wake word ONNX/TFLite model files as packaged data in the root
    sep = os.pathsep
    model_files = glob.glob(os.path.join(root_dir, "*.onnx")) + glob.glob(os.path.join(root_dir, "*.tflite"))
    add_data_args = [f'--add-data "{f}{sep}."' for f in model_files]
    add_data_str = " ".join(add_data_args)

    pyinstaller_cmd = (
        f'"{pyinstaller_exe}" --name api --onedir --clean --noconfirm '
        f'--collect-all fastapi --collect-all uvicorn --collect-all pydantic --collect-all starlette --collect-all websockets '
        f'{add_data_str} '
        f'api.py'
    )
    run_cmd(pyinstaller_cmd, cwd=backend_dir)
    
    # ---------------------------------------------------------
    # 3. Copy compiled backend directory to meridian_frontend/src-tauri/api
    # ---------------------------------------------------------
    print("\n=== Step 3: Copying Backend to Frontend Resources ===")
    frontend_api_dir = os.path.join(frontend_dir, "src-tauri", "api")
    if os.path.exists(frontend_api_dir):
        print("Clearing old frontend resources api directory...")
        shutil.rmtree(frontend_api_dir)
        
    compiled_backend = os.path.join(backend_dir, "dist", "api")
    print(f"Copying '{compiled_backend}' -> '{frontend_api_dir}'...")
    shutil.copytree(compiled_backend, frontend_api_dir)
    
    if platform.system() != "Windows":
        print(f"Granting executable permissions (chmod +x) to '{frontend_api_dir}' binaries...")
        for r, _, files in os.walk(frontend_api_dir):
            for file in files:
                file_path = os.path.join(r, file)
                if not file.endswith((".py", ".txt", ".json", ".md", ".onnx", ".tflite", ".png", ".jpg")):
                    try:
                        os.chmod(file_path, 0o755)
                    except Exception:
                        pass
    
    if sidecar_only:
        print("\n[Success] Standalone sidecar backend build process complete!")
        sys.exit(0)
        
    # ---------------------------------------------------------
    # 4. Build Tauri Desktop Wrapper
    # ---------------------------------------------------------
    print("\n=== Step 4: Compiling Standalone Tauri Desktop Shell ===")
    
    print("Terminating any running app instances...")
    if platform.system() == "Windows":
        subprocess.run("taskkill /f /im app.exe >nul 2>&1", shell=True)
        subprocess.run("taskkill /f /im api.exe >nul 2>&1", shell=True)
    else:
        subprocess.run("killall app >/dev/null 2>&1", shell=True)
        subprocess.run("killall api >/dev/null 2>&1", shell=True)
    
    # Clear old bundle output directory
    bundle_dir = os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle")
    if os.path.exists(bundle_dir):
        print("Clearing old installer bundle directory...")
        shutil.rmtree(bundle_dir)

    system = platform.system()
    if system == "Windows":
        bundles = "nsis,msi"
    elif system == "Darwin":
        bundles = "dmg,app"
    else:
        bundles = "deb,appimage"
    run_cmd(f"npm run tauri build -- --bundles {bundles}", cwd=frontend_dir)

    
    # ---------------------------------------------------------
    # 5. Move installers to executables/
    # ---------------------------------------------------------
    print("\n=== Step 5: Copying compiled installers to executables/ ===")
    executables_dir = os.path.join(root_dir, "executables")
    current_ver = get_current_version(root_dir)
    clean_old_version_executables(executables_dir, current_ver)
    
    patterns = {
        "NSIS Setup EXE": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "nsis", "meridian-x_*_x64-setup.exe"),
        "macOS DMG": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "dmg", "*.dmg"),
        "macOS App Bundle": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "macos", "*.app"),
        "Linux DEB Package": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "deb", "*.deb"),
        "Linux AppImage": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "appimage", "*.AppImage"),
    }

    found_any = False
    for label, pattern in patterns.items():
        files = glob.glob(pattern)
        if files:
            for f in files:
                dest = os.path.join(executables_dir, os.path.basename(f))
                if os.path.isdir(f):
                    if os.path.exists(dest):
                        shutil.rmtree(dest)
                    shutil.copytree(f, dest)
                else:
                    shutil.copy2(f, dest)
                print(f"Copied {label} to: {dest}")
                found_any = True

    if not found_any:
        print("[Warning] No compiled desktop installer packages were found in bundle output!")

    print("\n[Success] Standalone build process complete! Desktop EXE ready in executables/")


if __name__ == "__main__":
    main()
