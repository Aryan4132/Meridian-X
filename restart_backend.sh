#!/usr/bin/env bash
echo "========================================================"
echo " Restarting Meridian-X Backend Daemon...                "
echo "========================================================"

echo "[1/3] Terminating running backend instances..."
pkill -f "api.py" >/dev/null 2>&1 || true
pkill -f "api/api" >/dev/null 2>&1 || true
sleep 1

echo "[2/3] Starting Meridian-X daemon..."
cd "$(dirname "$0")/meridian_backend" || exit 1

if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
fi

nohup python3 api.py > /dev/null 2>&1 &
echo "[3/3] Backend daemon successfully restarted in background."
sleep 1
