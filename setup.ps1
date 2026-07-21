# Meridian-X: Autonomous Offline Companion Setup Script
# Run this script to set up your local development environment.
# Usage: powershell -ExecutionPolicy Bypass -File .\setup.ps1

$ErrorActionPreference = "Stop"

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "                  🪐 Meridian-X Environment Setup                        " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

# Helper to check for command availability
function Test-Command {
    param ([string]$name)
    return [bool](Get-Command $name -ErrorAction SilentlyContinue)
}

# 1. Verification of Prerequisites
Write-Host "`n[1/5] Checking System Prerequisites..." -ForegroundColor Yellow

$prereqs = @{
    "git" = "Git (for repository management)"
    "python" = "Python (required for backend service)"
    "node" = "Node.js (required for front-end & Tauri)"
    "npm" = "npm (Node Package Manager)"
    "cargo" = "Rust Compiler/Cargo (required for Tauri builds)"
    "ollama" = "Ollama (required for local AI model execution)"
}

$missing = @()
foreach ($cmd in $prereqs.Keys) {
    if (Test-Command $cmd) {
        Write-Host "  [OK] $($prereqs[$cmd]) is installed" -ForegroundColor Green
    } else {
        Write-Host "  [MISSING] $($prereqs[$cmd])" -ForegroundColor Red
        $missing += $cmd
    }
}

if ($missing.Count -gt 0) {
    Write-Host "`n[!] Some prerequisites are missing: $($missing -join ', ')." -ForegroundColor Yellow
    Write-Host "    Please ensure they are installed and available in your PATH before continuing." -ForegroundColor Yellow
}

# 2. Configuration Setup (.env)
Write-Host "`n[2/5] Setting up Environment Variables..." -ForegroundColor Yellow
if (-not (Test-Path ".env")) {
    if (Test-Path ".env.template") {
        Copy-Item ".env.template" ".env"
        Write-Host "  [OK] Created .env file from .env.template" -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] .env.template not found. Skipping environment creation." -ForegroundColor Red
    }
} else {
    Write-Host "  [OK] .env file already exists." -ForegroundColor Green
}

# 3. Backend Setup (Python venv & dependencies)
Write-Host "`n[3/5] Building Python Virtual Environment..." -ForegroundColor Yellow
$backendDir = Join-Path (Get-Location) "meridian_backend"
$venvPath = Join-Path $backendDir "venv"

if (-not (Test-Path $venvPath)) {
    if (Test-Command "python") {
        Write-Host "  Creating venv in $venvPath..." -ForegroundColor Cyan
        Start-Process python -ArgumentList "-m venv $venvPath" -Wait -NoNewWindow
        Write-Host "  [OK] Virtual environment created." -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] Python not found. Cannot create virtual environment." -ForegroundColor Red
    }
} else {
    Write-Host "  [OK] Virtual environment already exists." -ForegroundColor Green
}

if (Test-Path $venvPath) {
    $pipPath = Join-Path $venvPath "Scripts\pip.exe"
    $reqsPath = Join-Path $backendDir "requirements.txt"
    if (Test-Path $reqsPath) {
        Write-Host "  Installing Python dependencies (this may take a few minutes)..." -ForegroundColor Cyan
        Start-Process $pipPath -ArgumentList "install -r `"$reqsPath`"" -Wait -NoNewWindow
        Write-Host "  [OK] Python dependencies installed." -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] requirements.txt not found in backend directory." -ForegroundColor Red
    }
}

# 4. Frontend Setup (npm install)
Write-Host "`n[4/5] Setting up Frontend Dependencies..." -ForegroundColor Yellow
$frontendDir = Join-Path (Get-Location) "meridian_frontend"
$nodeModulesPath = Join-Path $frontendDir "node_modules"

if (-not (Test-Path $nodeModulesPath)) {
    if (Test-Command "npm") {
        Write-Host "  Running npm install in $frontendDir (this may take a few minutes)..." -ForegroundColor Cyan
        Push-Location $frontendDir
        Start-Process npm -ArgumentList "install" -Wait -NoNewWindow
        Pop-Location
        Write-Host "  [OK] Frontend dependencies installed." -ForegroundColor Green
    } else {
        Write-Host "  [FAIL] npm not found. Skipping frontend dependencies install." -ForegroundColor Red
    }
} else {
    Write-Host "  [OK] node_modules already exists." -ForegroundColor Green
}

# 5. Ollama Models Setup (Optional / Background Pull)
Write-Host "`n[5/5] Checking Ollama Models..." -ForegroundColor Yellow
if (Test-Command "ollama") {
    # Check if Ollama is running
    $ollamaRunning = $false
    try {
        $response = Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags" -Method Get -TimeoutSec 3
        $ollamaRunning = $true
    } catch {
        Write-Host "  [WARNING] Ollama server is not running on port 11434. Start Ollama to pull models." -ForegroundColor Yellow
    }

    if ($ollamaRunning) {
        $installedModels = $response.models | ForEach-Object { $_.name }
        $modelsToPull = @("nomic-embed-text", "qwen2.5-coder:1.5b-instruct-q8_0", "moondream:1.8b")

        foreach ($model in $modelsToPull) {
            # Check if model already exists (could be exact match or prefix)
            $hasModel = $false
            foreach ($inst in $installedModels) {
                if ($inst -like "*$model*") {
                    $hasModel = $true
                    break
                }
            }

            if ($hasModel) {
                Write-Host "  [OK] Ollama model '$model' is already pulled." -ForegroundColor Green
            } else {
                Write-Host "  Pulling Ollama model '$model' in background..." -ForegroundColor Cyan
                # Run pulling as non-blocking background job or prompt user
                Start-Process ollama -ArgumentList "pull $model" -NoNewWindow
            }
        }
    }
} else {
    Write-Host "  [FAIL] Ollama is not installed. Skipping model checks." -ForegroundColor Red
}

Write-Host "`n==========================================================================" -ForegroundColor Green
Write-Host "🪐 Setup process completed!" -ForegroundColor Green
Write-Host "To start Meridian-X, run: .\start_meridian.bat" -ForegroundColor Green
Write-Host "==========================================================================" -ForegroundColor Green
