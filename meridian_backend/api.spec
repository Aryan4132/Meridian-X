# -*- mode: python ; coding: utf-8 -*-
# Portable PyInstaller spec for the Meridian-X backend sidecar.
#
# FIX: previously this file hardcoded absolute C:\Users\... paths (breaking on
# any other machine) and enabled UPX (AV false positives). Paths are now
# resolved relative to the repo root so `pyinstaller api.spec` works anywhere.
# Note: CI and build_standalone.py drive PyInstaller via CLI flags; this spec
# is for manual/local builds only.
import os

from PyInstaller.utils.hooks import collect_all

BACKEND_DIR = os.path.dirname(os.path.abspath(SPEC))
REPO_ROOT = os.path.dirname(BACKEND_DIR)

datas = [
    (os.path.join(REPO_ROOT, 'hey_meridian.onnx'), '.'),
    (os.path.join(REPO_ROOT, 'hey_meridian.tflite'), '.'),
]
binaries = []
hiddenimports = []
for pkg in ('fastapi', 'uvicorn', 'pydantic', 'starlette'):
    tmp_ret = collect_all(pkg)
    datas += tmp_ret[0]
    binaries += tmp_ret[1]
    hiddenimports += tmp_ret[2]


a = Analysis(
    ['api.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='api',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='api',
)
