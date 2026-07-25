#!/usr/bin/env bash
echo "============================================================================"
echo "                     Meridian-X: Autonomous Desktop Shell                    "
echo "============================================================================"
echo ""

# 1. Terminate any stale python backend instances to prevent port 4132 conflicts
echo "[1/4] Terminating any running daemon instances..."
pkill -f "api.py" >/dev/null 2>&1 || true
pkill -f "api/api" >/dev/null 2>&1 || true
sleep 1

# 1.5 Sync root .env to meridian_backend/.env
echo "[1.5/4] Syncing environment configuration to backend..."
if [ -f ".env" ]; then
    cp ".env" "meridian_backend/.env"
    echo "[System] Root .env synced to meridian_backend/.env"
fi

# 2. Launch the backend python daemon on port 4132
echo "[2/4] Starting backend daemon server on port 4132..."
cd meridian_backend || exit 1
if [ ! -f "venv/bin/python" ]; then
    echo "[System] Creating Python virtual environment..."
    python3 -m venv venv
    source venv/bin/activate
    echo "[System] Installing dependencies..."
    pip install -r requirements.txt
fi

source venv/bin/activate
python3 api.py &
BACKEND_PID=$!
cd ..

# Wait for FastAPI Backend to bind to port 4132
echo "Waiting for backend daemon to initialize..."
for i in {1..60}; do
    if nc -z 127.0.0.1 4132 >/dev/null 2>&1 || curl -s http://127.0.0.1:4132/api/health >/dev/null 2>&1; then
        echo "[System] Backend daemon online!"
        break
    fi
    sleep 0.5
done

# 3. Launch Tauri desktop wrapper application
echo "[3/4] Launching Tauri Desktop Shell..."
cd meridian_frontend || exit 1
if [ ! -d "node_modules" ]; then
    npm install
fi
npx tauri dev
cd ..

echo "Desktop Shell closed. Cleaning up background daemon..."
kill $BACKEND_PID >/dev/null 2>&1 || true
pkill -f "api.py" >/dev/null 2>&1 || true
echo "Cleanup complete."
