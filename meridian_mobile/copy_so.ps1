$soSrc = "src-tauri\target\aarch64-linux-android\release\libapp_lib.so"
$jniDir = "src-tauri\gen\android\app\src\main\jniLibs\arm64-v8a"

if (-not (Test-Path $jniDir)) {
    New-Item -ItemType Directory -Path $jniDir -Force | Out-Null
}

# Remove any existing symlink or file
$dest = Join-Path $jniDir "libapp_lib.so"
if (Test-Path $dest) {
    Remove-Item $dest -Force
}

Copy-Item -Path $soSrc -Destination $dest -Force
Write-Host "Copied .so to: $dest"
Write-Host "Size: $((Get-Item $dest).Length) bytes"

$tempAddrFile = Join-Path $env:TEMP "com.meridian.x.mobile-server-addr"
Set-Content -Path $tempAddrFile -Value "http://127.0.0.1:1420"
Write-Host "Created server-addr file at: $tempAddrFile"

