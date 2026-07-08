import os
import sys
import subprocess

def enable_startup():
    startup_dir = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    
    # 1. Clean up old VBScript if it exists
    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    if os.path.exists(vbs_path):
        try:
            os.remove(vbs_path)
            print("[Info] Removed old VBScript startup file.")
        except Exception:
            pass
            
    # 2. Create the start_silent.bat file in AppData (to avoid cluttering the project directory)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    appdata_dir = os.path.join(os.environ["APPDATA"], "Meridian")
    os.makedirs(appdata_dir, exist_ok=True)
    bat_path = os.path.join(appdata_dir, "start_silent.bat")
    
    release_exe_relative = r"meridian_frontend\src-tauri\target\release\app.exe"
    
    bat_content = f"""@echo off
cd /d "{project_dir}"

:: 1. Clean up any stale backend/frontend instances before startup
taskkill /f /im api.exe >nul 2>&1
taskkill /f /im app.exe >nul 2>&1
powershell -Command "Get-CimInstance Win32_Process -Filter \\"Name = 'python.exe' or Name = 'pythonw.exe'\\" | Where-Object {{$_.CommandLine -like '*api.py*'}} | ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}" >nul 2>&1

:: 2. Sync the root .env configuration to backend and production AppData folder
if exist ".env" (
    copy /Y ".env" "meridian_backend\\.env" >nul 2>&1
    if not exist "%LOCALAPPDATA%\\com.meridian.x\\Meridian" (
        mkdir "%LOCALAPPDATA%\\com.meridian.x\\Meridian" >nul 2>&1
    )
    copy /Y ".env" "%LOCALAPPDATA%\\com.meridian.x\\Meridian\\.env" >nul 2>&1
)

:: 3. Launch compiled release or fallback to development mode
if exist "{release_exe_relative}" (
    echo [System] Starting compiled production release...
    cd meridian_frontend\\src-tauri\\target\\release
    start "" "app.exe"
) else (
    echo [System] Production binary not found. Falling back to development mode...
    echo [System] Starting FastAPI Backend...
    cd meridian_backend
    if not exist venv (
        echo [System] Creating Python virtual environment...
        python -m venv venv
        call venv\\Scripts\\activate.bat
        echo [System] Checking dependencies...
        pip install -r requirements.txt
    )
    start "" "venv\\Scripts\\pythonw.exe" api.py
    echo [System] Waiting for FastAPI Backend to bind to port 4132...
    powershell -Command "$retry = 0; while ($retry -lt 120) {{ try {{ $c = New-Object System.Net.Sockets.TcpClient('127.0.0.1', 4132); if ($c.Connected) {{ $c.Close(); break; }} }} catch {{}} Start-Sleep -Milliseconds 500; $retry++ }}"
    echo [System] FastAPI Backend online! Starting Tauri Desktop App...
    cd /d "{project_dir}"
    cd meridian_frontend
    call npx tauri dev
)
"""
    
    try:
        with open(bat_path, "w", newline="\r\n", encoding="utf-8") as f:
            f.write(bat_content)
        print(f"[Success] Silent batch file created at: {bat_path}")
    except Exception as e:
        print(f"[Error] Failed to write silent batch file: {e}")
        return

    # 3. Create the VBScript file in the Startup folder to launch the batch file completely hidden
    lnk_path = os.path.join(startup_dir, "Meridian.lnk")
    if os.path.exists(lnk_path):
        try:
            os.remove(lnk_path)
            print("[Info] Removed old shortcut startup file.")
        except Exception:
            pass

    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    vbs_content = f'Set WshShell = CreateObject("WScript.Shell")\r\nWshShell.Run "cmd.exe /c ""{bat_path}""", 0, False\r\n'
    
    try:
        with open(vbs_path, "w", newline="\r\n", encoding="utf-8") as f:
            f.write(vbs_content)
        print(f"[Success] Autostart VBScript successfully created at: {vbs_path}")
    except Exception as e:
        print(f"[Error] Failed to create startup VBScript: {e}")

def disable_startup():
    startup_dir = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")
    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    shortcut_path = os.path.join(startup_dir, "Meridian.lnk")
    
    project_dir = os.path.dirname(os.path.abspath(__file__))
    legacy_bat_path = os.path.join(project_dir, "start_silent.bat")
    
    appdata_dir = os.path.join(os.environ["APPDATA"], "Meridian")
    bat_path = os.path.join(appdata_dir, "start_silent.bat")
    
    removed_any = False
    
    for path in [vbs_path, shortcut_path, bat_path, legacy_bat_path]:
        if os.path.exists(path):
            try:
                os.remove(path)
                print(f"[Success] Removed startup file: {os.path.basename(path)}")
                removed_any = True
            except Exception as e:
                print(f"[Error] Failed to remove {os.path.basename(path)}: {e}")
                
    if os.path.exists(appdata_dir) and not os.listdir(appdata_dir):
        try:
            os.rmdir(appdata_dir)
        except Exception:
            pass
            
    if not removed_any:
        print("[Info] Autostart was not enabled.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--disable":
        disable_startup()
    else:
        enable_startup()
