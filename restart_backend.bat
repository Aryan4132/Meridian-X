@echo off
title Meridian-X Backend Restarter
echo ===================================================
echo   Stopping existing Meridian Backend processes...
echo ===================================================
powershell -Command "Get-CimInstance Win32_Process -Filter \"Name = 'python.exe'\" | Where-Object {$_.CommandLine -like '*api.py*'} | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }" 2>nul

echo.
echo ===================================================
echo   Starting new Backend instance in the background...
echo ===================================================
cd meridian_backend
powershell -Command "Start-Process cmd -ArgumentList '/c call venv\Scripts\activate.bat && python api.py' -WorkingDirectory '.' -WindowStyle Hidden"

echo Done! Backend has been restarted.
timeout /t 3
