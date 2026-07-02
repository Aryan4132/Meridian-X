@echo off
title Meridian-X Desktop Companion Bootstrapper
color 0A
echo ============================================================================
echo                      Meridian-X: Autonomous Desktop Shell
echo ============================================================================
echo.

:: 1. Terminate any stale python backend instances to prevent port 4132 conflicts
echo [1/4] Terminating any running daemon instances...
taskkill /f /im python.exe /fi "WINDOWTITLE eq Meridian-X Daemon" >nul 2>&1
taskkill /f /im api.exe >nul 2>&1
taskkill /f /im app.exe >nul 2>&1
powershell -Command "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1
timeout /t 1 /nobreak >nul

:: 1.5 Sync root .env to meridian_backend/.env so API keys are loaded correctly
echo [1.5/4] Syncing environment configuration to backend...
if exist ".env" (
    copy /Y ".env" "meridian_backend\.env" >nul 2>&1
    echo [System] Root .env synced to meridian_backend\.env
)

:: 2. Launch the backend python daemon on port 4132
echo [2/4] Starting backend daemon server on port 4132 (minimized)...
cd meridian_backend
if not exist "venv\Scripts\python.exe" (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [System] Installing dependencies...
    pip install -r requirements.txt
)
start "Meridian-X Daemon" /min cmd /c "call venv\Scripts\activate.bat && python api.py"
cd ..

:: Wait 3 seconds to allow backend services and database connections to initialize
timeout /t 3 /nobreak >nul

:: 3. Launch Tauri desktop wrapper application
echo [3/4] Launching Tauri Desktop Shell...
cd meridian_frontend
call npx tauri dev
cd ..

echo.
echo Desktop Shell closed. Cleaning up background daemon...
powershell -Command "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1
echo Cleanup complete.
timeout /t 2 /nobreak >nul
exit
