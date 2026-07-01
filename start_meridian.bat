@echo off
:menu
cls
color 0B
echo ============================================================================
echo                      Meridian-X: Autonomous Offline Companion
echo ============================================================================
echo.
echo    [1] Run Meridian-X CLI prompt
echo    [2] Start Daemon Server (Standalone)
echo    [3] Launch Tauri Desktop Shell
echo    [4] Run System Audit Diagnostics
echo    [5] Exit
echo.
echo ============================================================================
set /p choice="Select option [1-5]: "

if "%choice%"=="1" goto cliprompt
if "%choice%"=="2" goto startdaemon
if "%choice%"=="3" goto startdesktop
if "%choice%"=="4" goto auditrun
if "%choice%"=="5" goto exitapp
goto menu

:cliprompt
cls
echo ============================================================================
echo                       Meridian-X: Direct Prompt Input
echo ============================================================================
echo.
set /p userprompt="Enter your goal prompt for the agent: "
echo.
if not exist ".\meridian_backend\venv" (
    echo [System] Virtual environment not found. Please run Option 2 or 3 first to set it up.
    pause
    goto menu
)
call .\meridian_backend\venv\Scripts\python main.py --prompt "%userprompt%"
echo.
pause
goto menu

:startdaemon
cls
echo Starting Meridian-X Backend Daemon Process...
cd meridian_backend
if not exist venv (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [System] Checking dependencies...
    pip install -r requirements.txt
)
call venv\Scripts\activate.bat
python api.py
cd ..
pause
goto menu

:startdesktop
cls
echo Starting Meridian-X Backend Daemon Process...
cd meridian_backend
if not exist venv (
    echo [System] Creating Python virtual environment...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo [System] Checking dependencies...
    pip install -r requirements.txt
)
start "Meridian-X Daemon" /min cmd /c "call venv\Scripts\activate.bat && python api.py"
cd ..
timeout /t 2 /nobreak >nul

echo Starting Tauri Desktop Shell...
cd meridian_frontend
call npx tauri dev
cd ..
goto menu

:auditrun
cls
echo Running local hardware diagnostics and SQLite audit scans...
if not exist ".\meridian_backend\venv" (
    echo [System] Virtual environment not found. Please run Option 2 or 3 first.
    pause
    goto menu
)
call .\meridian_backend\venv\Scripts\python -c "import psutil, os; print('CPU Core Count:', psutil.cpu_count()); print('RAM Available:', round(psutil.virtual_memory().available / 1024**3, 2), 'GB'); print('SQLite database found:', os.path.exists('meridian_memory/metadata.db'))"
echo.
pause
goto menu

:exitapp
cls
echo Goodbye!
timeout /t 1 /nobreak >nul
exit
