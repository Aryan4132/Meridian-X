 @echo off
title Restarting Meridian-X Backend Daemon...
echo Terminating running Python backend instances...
taskkill /f /im api.exe >nul 2>&1
taskkill /f /im app.exe >nul 2>&1
powershell -Command "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" >nul 2>&1
timeout /t 1 /nobreak >nul

echo Starting Meridian-X daemon...
cd meridian_backend
start "Meridian-X Daemon" /min cmd /c "call venv\Scripts\activate.bat && python api.py"
cd ..
echo Backend daemon successfully restarted.
timeout /t 2 /nobreak >nul
exit
