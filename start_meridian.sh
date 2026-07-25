#!/usr/bin/env bash
while true; do
    clear
    echo "============================================================================"
    echo "                     Meridian-X: Autonomous Offline Companion"
    echo "============================================================================"
    echo ""
    echo "   [1] Run Meridian-X CLI prompt"
    echo "   [2] Start Daemon Server (Standalone)"
    echo "   [3] Launch Tauri Desktop Shell"
    echo "   [4] Run System Audit Diagnostics"
    echo "   [5] Exit"
    echo ""
    echo "============================================================================"
    read -p "Select option [1-5]: " choice

    case $choice in
        1)
            clear
            echo "============================================================================"
            echo "                      Meridian-X: Direct Prompt Input"
            echo "============================================================================"
            echo ""
            read -p "Enter your goal prompt for the agent: " userprompt
            echo ""
            if [ ! -d "./meridian_backend/venv" ]; then
                echo "[System] Virtual environment not found. Please run Option 2 or 3 first to set it up."
                read -p "Press Enter to return..."
                continue
            fi
            source ./meridian_backend/venv/bin/activate
            python3 main.py --goal "$userprompt"
            echo ""
            read -p "Press Enter to return..."
            ;;
        2)
            clear
            echo "Starting Meridian-X Backend Daemon Process..."
            cd meridian_backend || exit 1
            if [ ! -d venv ]; then
                echo "[System] Creating Python virtual environment..."
                python3 -m venv venv
                source venv/bin/activate
                echo "[System] Checking dependencies..."
                pip install -r requirements.txt
            fi
            source venv/bin/activate
            python3 api.py
            cd ..
            read -p "Press Enter to return..."
            ;;
        3)
            clear
            chmod +x ./start_desktop.sh >/dev/null 2>&1 || true
            ./start_desktop.sh
            read -p "Press Enter to return..."
            ;;
        4)
            clear
            echo "Running local hardware diagnostics and SQLite audit scans..."
            if [ ! -d "./meridian_backend/venv" ]; then
                echo "[System] Virtual environment not found. Please run Option 2 or 3 first."
                read -p "Press Enter to return..."
                continue
            fi
            source ./meridian_backend/venv/bin/activate
            python3 -c "import psutil, os; print('CPU Core Count:', psutil.cpu_count()); print('RAM Available:', round(psutil.virtual_memory().available / 1024**3, 2), 'GB'); print('SQLite database found:', os.path.exists('meridian_memory/metadata.db'))"
            echo ""
            read -p "Press Enter to return..."
            ;;
        5)
            clear
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid option. Please select 1-5."
            sleep 1
            ;;
    esac
done
