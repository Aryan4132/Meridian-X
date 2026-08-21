#!/usr/bin/env bash
echo "=========================================================================="
echo "                 🪐 Downloading & Installing Meridian-X                    "
echo "=========================================================================="
echo ""

if ! command -v git &> /dev/null; then
    echo "[Error] Git is not installed. Please install Git first."
    exit 1
fi

if ! command -v python3 &> /dev/null; then
    echo "[Error] Python 3 is not installed. Please install Python 3.10+ first."
    exit 1
fi

if [ "$(uname -s)" = "Linux" ]; then
    if ! command -v xclip &> /dev/null && ! command -v xsel &> /dev/null; then
        echo "[Notice] 'xclip' or 'xsel' recommended for clipboard history monitoring on Linux."
    fi
    if ! command -v xdotool &> /dev/null; then
        echo "[Notice] 'xdotool' recommended for active window tracking on Linux."
    fi
fi

if [ ! -d "meridian_backend" ]; then
    echo "[1/3] Cloning Meridian-X repository..."
    git clone https://github.com/Aryan4132/Meridian-X.git
    cd Meridian-X || exit 1
fi

echo "[2/3] Setting up Python backend environment..."
cd meridian_backend || exit 1
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd ..

echo "[3/3] Setting up frontend dependencies..."
cd meridian_frontend || exit 1
npm install
cd ..

if [ ! -f ".env" ] && [ -f ".env.template" ]; then
    cp .env.template .env
    echo "[System] Created default .env from template."
fi

echo ""
echo "=========================================================================="
echo "      🪐 Meridian-X Installation Complete! Launching desktop...            "
echo "=========================================================================="
if [ "$(uname -s)" = "Darwin" ]; then
    echo "[System] macOS detected. Applying free ad-hoc signature & clearing Gatekeeper flags..."
    codesign --force --deep --sign - /Applications/meridian-x.app 2>/dev/null || true
    xattr -r -d com.apple.quarantine /Applications/meridian-x.app 2>/dev/null || true
    xattr -r -d com.apple.quarantine ~/Downloads/meridian-x.app 2>/dev/null || true
    xattr -r -d com.apple.quarantine . 2>/dev/null || true
fi

chmod +x start_desktop.sh start_meridian.sh restart_backend.sh >/dev/null 2>&1 || true
./start_desktop.sh
