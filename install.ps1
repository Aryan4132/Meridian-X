# Meridian-X: Pre-compiled App Installer Script
# This script downloads the latest setup installer and runs it.
# Usage: powershell -ExecutionPolicy Bypass -Command "irm https://meridian-x.pages.dev/install.ps1 | iex"

$ErrorActionPreference = "Stop"

Write-Host "==========================================================================" -ForegroundColor Cyan
Write-Host "                🪐 Downloading & Installing Meridian-X                    " -ForegroundColor Cyan
Write-Host "==========================================================================" -ForegroundColor Cyan

try {
    # 1. Fetch latest release assets from GitHub API
    Write-Host "Fetching latest release metadata..." -ForegroundColor Cyan
    $release = Invoke-RestMethod -Uri "https://api.github.com/repos/Aryan4132/Meridian-X/releases/latest"
    
    # 2. Find the setup executable
    $asset = $release.assets | Where-Object { $_.name -like "*setup.exe" } | Select-Object -First 1
    if (-not $asset) {
        throw "No suitable installer (*setup.exe) found in the latest release assets."
    }

    
    $downloadUrl = $asset.browser_download_url
    $outputPath = Join-Path $env:TEMP $asset.name
    
    # 3. Download the file
    Write-Host "Downloading $($asset.name) (size: $([Math]::Round($asset.size / 1MB, 2)) MB)..." -ForegroundColor Cyan
    Invoke-WebRequest -Uri $downloadUrl -OutFile $outputPath
    
    # 4. Launch the installer
    Write-Host "Launching installer..." -ForegroundColor Green
    Start-Process -FilePath $outputPath -Wait
    
    Write-Host "`nInstallation launcher completed!" -ForegroundColor Green
} catch {
    Write-Host "`n[ERROR] Setup failed: $_" -ForegroundColor Red
}
