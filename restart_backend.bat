 @echo off
title Restarting Meridian-X Backend Daemon...
rem FIX: resolve script directory so the batch works from any CWD
set "SCRIPT_DIR=%~dp0"
echo Terminating running Python backend instances...
taskkill /f /im api.exe >nul 2>&1
taskkill /f /im app.exe >nul 2>&1
powershell -Command "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe' or Name = 'pythonw.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1
timeout /t 1 /nobreak >nul

echo Starting Meridian-X daemon...
cd /d "%SCRIPT_DIR%meridian_backend"
start "Meridian-X Daemon" /min cmd /c "call venv\Scripts\activate.bat && python api.py"
cd /d "%SCRIPT_DIR%"
echo Backend daemon successfully restarted.
timeout /t 2 /nobreak >nul
exit
