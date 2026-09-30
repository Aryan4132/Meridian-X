import os
import sys
import platform
import subprocess

def enable_startup_windows():
    appdata = os.environ.get("APPDATA", os.path.expanduser("~"))
    startup_dir = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
    
    # 1. Clean up old VBScript if it exists
    vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
    if os.path.exists(vbs_path):
        try:
            os.remove(vbs_path)
            print("[Info] Removed old VBScript startup file.")
        except Exception:
            pass
            
    # 2. Create the start_silent.bat file in AppData
    project_dir = os.path.dirname(os.path.abspath(__file__))
    appdata_dir = os.path.join(appdata, "Meridian")
    os.makedirs(appdata_dir, exist_ok=True)
    bat_path = os.path.join(appdata_dir, "start_silent.bat")
    
    release_exe = os.path.join(project_dir, r"meridian_frontend\src-tauri\target\release\app.exe")
    release_sidecar = os.path.join(project_dir, r"meridian_frontend\src-tauri\target\release\api\api.exe")
    
    bat_content = f"""@echo off
cd /d "{project_dir}"

:: 1. Clean up any stale backend/frontend instances before startup
taskkill /f /im api.exe >nul 2>&1
taskkill /f /im app.exe >nul 2>&1
powershell -Command "Get-CimInstance Win32_Process -Filter \\"Name = 'python.exe' or Name = 'pythonw.exe'\\" | Where-Object {{$_.CommandLine -like '*api.py*' -or $_.CommandLine -like '*mobile_bridge_service.py*'}} | ForEach-Object {{ Stop-Process -Id $_.ProcessId -Force }}" >nul 2>&1
powershell -Command "Get-NetTCPConnection -LocalPort 4132, 4133, 8765 -ErrorAction SilentlyContinue | ForEach-Object {{ Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }}" >nul 2>&1

:: 2. Sync the root .env configuration to backend and production AppData folder
if exist ".env" (
    copy /Y ".env" "meridian_backend\\.env" >nul 2>&1
    if not exist "%LOCALAPPDATA%\\com.meridian.x\\Meridian" (
        mkdir "%LOCALAPPDATA%\\com.meridian.x\\Meridian" >nul 2>&1
    )
    copy /Y ".env" "%LOCALAPPDATA%\\com.meridian.x\\Meridian\\.env" >nul 2>&1
)

:: 3. Launch compiled release if both binary and sidecar exist
if exist "{release_exe}" (
    if exist "{release_sidecar}" (
        echo [System] Starting compiled production release...
        cd /d "{os.path.dirname(release_exe)}"
        start "" "{release_exe}"
        goto :EOF
    )
)

:: 4. Fallback to live source mode: Start backend daemons with environment activated
echo [System] Starting FastAPI Backend from live source...
cd /d "{project_dir}\\meridian_backend"
if not exist "venv\\Scripts\\activate.bat" (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\\Scripts\\activate.bat
    echo [System] Checking dependencies...
    pip install -r requirements.txt
)

:: Ensure venv is activated for python environment variables and PATH
call venv\\Scripts\\activate.bat

:: Start mobile bridge daemon on 4133 silently
start "Meridian-X Mobile Bridge" /min cmd /c "call venv\\Scripts\\activate.bat && python mobile_bridge_service.py"

:: Start FastAPI backend on 4132 silently
start "Meridian-X Backend" /min cmd /c "call venv\\Scripts\\activate.bat && python api.py"

echo [System] Waiting for FastAPI Backend to bind to port 4132...
powershell -Command "$retry = 0; while ($retry -lt 120) {{ try {{ $c = New-Object System.Net.Sockets.TcpClient('127.0.0.1', 4132); if ($c.Connected) {{ $c.Close(); break; }} }} catch {{}} Start-Sleep -Milliseconds 500; $retry++ }}"

echo [System] FastAPI Backend online! Starting Desktop Frontend...
cd /d "{project_dir}\\meridian_frontend"
if exist "src-tauri\\target\\release\\app.exe" (
    start "" "src-tauri\\target\\release\\app.exe"
) else (
    start "Meridian-X Dev Frontend" cmd /c "npx tauri dev"
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
    vbs_content = (
        'Set WshShell = CreateObject("WScript.Shell")\r\n'
        f'WshShell.CurrentDirectory = "{project_dir}"\r\n'
        f'WshShell.Run "cmd.exe /s /c " & Chr(34) & "{bat_path}" & Chr(34), 0, False\r\n'
    )
    
    try:
        with open(vbs_path, "w", newline="\r\n", encoding="utf-8") as f:
            f.write(vbs_content)
        print(f"[Success] Autostart VBScript successfully created at: {vbs_path}")
    except Exception as e:
        print(f"[Error] Failed to create startup VBScript: {e}")

def enable_startup_macos():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    start_script = os.path.join(project_dir, "start_desktop.sh")
    launch_agents_dir = os.path.expanduser("~/Library/LaunchAgents")
    os.makedirs(launch_agents_dir, exist_ok=True)
    
    plist_path = os.path.join(launch_agents_dir, "com.meridian.x.plist")
    plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.meridian.x</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>{start_script}</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
    <key>WorkingDirectory</key>
    <string>{project_dir}</string>
</dict>
</plist>
"""
    try:
        with open(plist_path, "w", encoding="utf-8") as f:
            f.write(plist_content)
        print(f"[Success] macOS launchd plist created at: {plist_path}")
    except Exception as e:
        print(f"[Error] Failed to create macOS launchd plist: {e}")

def enable_startup_linux():
    project_dir = os.path.dirname(os.path.abspath(__file__))
    start_script = os.path.join(project_dir, "start_desktop.sh")
    autostart_dir = os.path.expanduser("~/.config/autostart")
    os.makedirs(autostart_dir, exist_ok=True)
    
    desktop_path = os.path.join(autostart_dir, "meridian-x.desktop")
    desktop_content = f"""[Desktop Entry]
Type=Application
Name=Meridian-X Desktop Companion
Exec=/bin/bash "{start_script}"
Path={project_dir}
Terminal=false
X-GNOME-Autostart-enabled=true
Comment=Meridian-X Autonomous AI Desktop Companion
"""
    try:
        with open(desktop_path, "w", encoding="utf-8") as f:
            f.write(desktop_content)
        os.chmod(desktop_path, 0o755)
        print(f"[Success] Linux autostart entry created at: {desktop_path}")
    except Exception as e:
        print(f"[Error] Failed to create Linux autostart entry: {e}")

def enable_startup():
    system = platform.system()
    if system == "Windows":
        enable_startup_windows()
    elif system == "Darwin":
        enable_startup_macos()
    elif system == "Linux":
        enable_startup_linux()
    else:
        print(f"[Warning] Autostart is not supported on platform: {system}")

def disable_startup():
    system = platform.system()
    if system == "Windows":
        appdata = os.environ.get("APPDATA", os.path.expanduser("~"))
        startup_dir = os.path.join(appdata, r"Microsoft\Windows\Start Menu\Programs\Startup")
        vbs_path = os.path.join(startup_dir, "MeridianStartup.vbs")
        shortcut_path = os.path.join(startup_dir, "Meridian.lnk")
        project_dir = os.path.dirname(os.path.abspath(__file__))
        legacy_bat_path = os.path.join(project_dir, "start_silent.bat")
        appdata_dir = os.path.join(appdata, "Meridian")
        bat_path = os.path.join(appdata_dir, "start_silent.bat")
        
        for path in [vbs_path, shortcut_path, bat_path, legacy_bat_path]:
            if os.path.exists(path):
                try:
                    os.remove(path)
                    print(f"[Success] Removed startup file: {os.path.basename(path)}")
                except Exception as e:
                    print(f"[Error] Failed to remove {os.path.basename(path)}: {e}")
    elif system == "Darwin":
        plist_path = os.path.expanduser("~/Library/LaunchAgents/com.meridian.x.plist")
        if os.path.exists(plist_path):
            try:
                os.remove(plist_path)
                print(f"[Success] Removed macOS launchd plist: {plist_path}")
            except Exception as e:
                print(f"[Error] Failed to remove launchd plist: {e}")
    elif system == "Linux":
        desktop_path = os.path.expanduser("~/.config/autostart/meridian-x.desktop")
        if os.path.exists(desktop_path):
            try:
                os.remove(desktop_path)
                print(f"[Success] Removed Linux autostart file: {desktop_path}")
            except Exception as e:
                print(f"[Error] Failed to remove autostart entry: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--disable":
        disable_startup()
    else:
        enable_startup()

