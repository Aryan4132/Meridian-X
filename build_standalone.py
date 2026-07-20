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
    
    run_cmd("npm run tauri build", cwd=frontend_dir)
    
    # 5. Move installers to executables/
    print("\n=== Step 5: Copying compiled installers to executables/ ===")
    executables_dir = os.path.join(root_dir, "executables")
    os.makedirs(executables_dir, exist_ok=True)
    
    import glob
    msi_pattern = os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "msi", "meridian-x_*_x64_en-US.msi")
    exe_pattern = os.path.join(frontend_dir, "src-tauri", "target", "release", "bundle", "nsis", "meridian-x_*_x64-setup.exe")
    
    msi_files = glob.glob(msi_pattern)
    exe_files = glob.glob(exe_pattern)
    
    if msi_files:
        msi_src = sorted(msi_files)[-1]
        shutil.copy2(msi_src, executables_dir)
        print(f"Copied MSI installer to: {os.path.join(executables_dir, os.path.basename(msi_src))}")
    else:
        print("[Warning] MSI installer output not found!")
        
    if exe_files:
        exe_src = sorted(exe_files)[-1]
        shutil.copy2(exe_src, executables_dir)
        print(f"Copied NSIS setup EXE to: {os.path.join(executables_dir, os.path.basename(exe_src))}")
    else:
        print("[Warning] NSIS setup EXE output not found!")
        
    print("\n[Success] Standalone build process complete!")

if __name__ == "__main__":
    main()
