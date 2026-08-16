import os
import sys
import shutil
import subprocess
import platform

def run_cmd(cmd, cwd=None):
    print(f"\n[Run] {cmd} (cwd: {cwd or '.'})")
    res = subprocess.run(cmd, shell=True, cwd=cwd)
    if res.returncode != 0:
        print(f"[Error] Command failed with exit code: {res.returncode}")
        sys.exit(res.returncode)

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    backend_dir = os.path.join(root_dir, "meridian_backend")
    frontend_dir = os.path.join(root_dir, "meridian_frontend")
    
    sidecar_only = "--sidecar-only" in sys.argv or "--backend-only" in sys.argv
    
    # 1. Check/Install PyInstaller in backend virtual environment
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

    # 2. Compile Backend with PyInstaller
    print("\n=== Step 2: Compiling Python Backend with PyInstaller ===")
    
    # Clear any old build/dist files in backend
    for folder in ["build", "dist"]:
        path = os.path.join(backend_dir, folder)
        if os.path.exists(path):
            print(f"Clearing old {folder} directory...")
            shutil.rmtree(path)
            
    # Run PyInstaller to package into a single folder ('onedir')
    # Add wake word ONNX/TFLite model files as packaged data in the root of the api folder
    # Use cross-platform path separator
    sep = os.pathsep
    import glob
    model_files = glob.glob(os.path.join(root_dir, "*.onnx")) + glob.glob(os.path.join(root_dir, "*.tflite"))
    add_data_args = []
    for f in model_files:
        filename = os.path.basename(f)
        add_data_args.append(f'--add-data "../{filename}{sep}."')
    
    add_data_str = " ".join(add_data_args)
    pyinstaller_cmd = (
        f'"{pyinstaller_exe}" --name api --onedir --clean --noconfirm '
        f'{add_data_str} '
        f'api.py'
    )
    run_cmd(pyinstaller_cmd, cwd=backend_dir)
    
    # 3. Copy compiled backend directory to meridian_frontend/api
    print("\n=== Step 3: Copying Backend to Frontend Resources ===")
    frontend_api_dir = os.path.join(frontend_dir, "src-tauri", "api")
    if os.path.exists(frontend_api_dir):
        print("Clearing old frontend resources api directory...")
        shutil.rmtree(frontend_api_dir)
        
    compiled_backend = os.path.join(backend_dir, "dist", "api")
    print(f"Copying '{compiled_backend}' -> '{frontend_api_dir}'...")
    shutil.copytree(compiled_backend, frontend_api_dir)
    
    if platform.system() != "Windows":
        api_bin = os.path.join(frontend_api_dir, "api")
        if os.path.exists(api_bin):
            print(f"Granting executable permissions (chmod +x) to '{api_bin}'...")
            os.chmod(api_bin, 0o755)
    
    if sidecar_only:
        print("\n[Success] Standalone sidecar backend build process complete!")
        sys.exit(0)
        
    # 4. Build Tauri Desktop Wrapper
    print("\n=== Step 4: Compiling Standalone Tauri Desktop Shell ===")
    
    # Terminate any running app.exe instances to prevent file locking
    print("Terminating any running instances...")
    if platform.system() == "Windows":
        subprocess.run("taskkill /f /im app.exe >nul 2>&1", shell=True)
        subprocess.run("taskkill /f /im api.exe >nul 2>&1", shell=True)
    else:
        subprocess.run("killall app >/dev/null 2>&1", shell=True)
        subprocess.run("killall api >/dev/null 2>&1", shell=True)
    
    # Clear old bundle output directory to avoid duplicating past version packages
    bundle_dir = os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle")
    if os.path.exists(bundle_dir):
        print("Clearing old installer bundle directory...")
        shutil.rmtree(bundle_dir)

    run_cmd("npm run tauri build", cwd=frontend_dir)
    
    # 5. Move installers to executables/
    print("\n=== Step 5: Copying compiled installers to executables/ ===")
    executables_dir = os.path.join(root_dir, "executables")
    if os.path.exists(executables_dir):
        print("Clearing old executables directory...")
        shutil.rmtree(executables_dir)
    os.makedirs(executables_dir, exist_ok=True)
    
    import glob
    patterns = {
        "MSI Installer": os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "msi", "meridian-x_*_x64_en-US.msi"),
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
        print("[Warning] No compiled installer packages were found in bundle output!")

    print("\n[Success] Standalone build process complete!")

if __name__ == "__main__":
    main()
