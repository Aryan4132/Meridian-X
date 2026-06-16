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
    
    bat_content = f"""@echo off
cd /d "{project_dir}"
echo [System] Starting FastAPI Backend...
cd meridian_backend
if not exist venv (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\\Scripts\\activate.bat
    echo [System] Checking dependencies...
    pip install -r requirements.txt
)
start /b cmd /c "call venv\\Scripts\\activate.bat && python api.py"
echo [System] Waiting for FastAPI Backend to bind to port 4132...
powershell -Command "while ($true) {{ try {{ $c = New-Object System.Net.Sockets.TcpClient('127.0.0.1', 4132); if ($c.Connected) {{ $c.Close(); break; }} }} catch {{}} Start-Sleep -Milliseconds 500 }}"
echo [System] FastAPI Backend online! Starting Tauri Desktop App...
cd ../meridain_frontend
npm run tauri dev
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
