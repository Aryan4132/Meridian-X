@echo off
title Meridian-X: Control Center
echo ===================================================
echo   Meridian-X: Autonomous Offline Desktop Agent
echo ===================================================
echo.
echo 1. Start Python API Backend (FastAPI on Port 4132)
echo 2. Start Tauri Desktop App (Dev Mode)
echo 3. Start Both Backend and Frontend
echo 4. Exit
echo.
set /p choice="Enter your choice (1-4): "

if "%choice%"=="1" goto start_backend
if "%choice%"=="2" goto start_frontend
if "%choice%"=="3" goto start_both
if "%choice%"=="4" goto exit

:start_backend
echo.
echo [System] Starting FastAPI Backend...
cd meridian_backend
if not exist venv (
    echo [System] Creating Python virtual environment...
    python -m venv venv
)
call venv\Scripts\activate.bat
echo [System] Checking dependencies...
pip install -r requirements.txt
python api.py
pause
goto exit

:start_frontend
echo.
echo [System] Starting Tauri Desktop App...
cd meridain_frontend
npm run tauri dev
pause
goto exit

:start_both
echo.
cd meridian_backend
if not exist venv (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [System] Checking dependencies...
    pip install -r requirements.txt
)
cd ..
echo [System] Spawning FastAPI Backend in the same terminal...
start /b cmd /c "cd meridian_backend && call venv\Scripts\activate.bat && python api.py"
echo [System] Waiting for FastAPI Backend to bind to port 4132...
powershell -Command "while ($true) { try { $c = New-Object System.Net.Sockets.TcpClient('127.0.0.1', 4132); if ($c.Connected) { $c.Close(); break; } } catch {} Start-Sleep -Milliseconds 500 }"
echo [System] FastAPI Backend online! Starting Tauri Desktop App...
cd meridain_frontend
npm run tauri dev
pause
goto exit

:exit
echo.
echo Goodbye!
