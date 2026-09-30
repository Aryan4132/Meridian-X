#!/usr/bin/env python
"""
Meridian-X Mobile APK Builder
Builds a real Android APK via Tauri v2's Android toolchain.
Requires: Android SDK, NDK, JDK, Rust with Android targets.
"""

import os
import sys
import shutil
import subprocess


# Common Android SDK install locations on Windows
ANDROID_SDK_SEARCH_PATHS = [
    os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk"),
    os.path.expandvars(r"%USERPROFILE%\AppData\Local\Android\Sdk"),
    r"C:\Android\Sdk",
    os.path.expandvars(r"%USERPROFILE%\Android\Sdk"),
]


def find_android_sdk():
    """Auto-detect ANDROID_HOME from env or common paths."""
    for var in ("ANDROID_HOME", "ANDROID_SDK_ROOT"):
        path = os.environ.get(var)
        if path and os.path.isdir(path):
            return path
    for path in ANDROID_SDK_SEARCH_PATHS:
        if os.path.isdir(path) and os.path.isdir(os.path.join(path, "platform-tools")):
            return path
    return None


def find_ndk(sdk_path):
    """Find latest NDK inside SDK directory."""
    ndk_dir = os.path.join(sdk_path, "ndk")
    if not os.path.isdir(ndk_dir):
        return None
    versions = sorted(os.listdir(ndk_dir), reverse=True)
    for v in versions:
        candidate = os.path.join(ndk_dir, v)
        if os.path.isdir(candidate):
            return candidate
    return None


def find_compatible_jdk():
    """Auto-detect JDK 17 or JDK 21 compatible with Gradle 8.x."""
    search_dirs = [
        r"C:\Program Files\Eclipse Adoptium",
        r"C:\Program Files\Java",
        r"C:\Program Files\Android\Android Studio\jbr",
        os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk\jbr"),
    ]
    # Look for JDK 17 or 21 folders
    for base in search_dirs:
        if os.path.isdir(base):
            for entry in sorted(os.listdir(base), reverse=True):
                full_path = os.path.join(base, entry)
                if os.path.isdir(full_path) and os.path.exists(os.path.join(full_path, "bin", "java.exe")):
                    if any(v in entry.lower() for v in ["17", "21", "jbr"]):
                        return full_path
    # Fallback to current JAVA_HOME
    java_home = os.environ.get("JAVA_HOME")
    if java_home and os.path.isdir(java_home):
        return java_home
    return None



def check_rust_targets():
    """Verify Rust Android targets are installed."""
    try:
        result = subprocess.run(
            ["rustup", "target", "list", "--installed"],
            capture_output=True, text=True, shell=True
        )
        installed = result.stdout.strip().split("\n")
        return "aarch64-linux-android" in installed
    except Exception:
        return False


def validate_prerequisites(script_dir: str) -> tuple[str, str]:
    """Validate all build prerequisites. Returns (sdk_path, ndk_path) or exits."""
    errors = []

    # 1. Android SDK
    sdk_path = find_android_sdk()
    if not sdk_path:
        errors.append(
            "[MISSING] Android SDK not found.\n"
            "  Fix: Install Android Studio or set ANDROID_HOME environment variable.\n"
            "  Expected locations: " + ", ".join(ANDROID_SDK_SEARCH_PATHS)
        )

    # 2. NDK
    ndk_path = find_ndk(sdk_path) if sdk_path else None
    if sdk_path and not ndk_path:
        errors.append(
            "[MISSING] Android NDK not found inside SDK.\n"
            "  Fix: Open Android Studio → SDK Manager → SDK Tools → NDK (Side by side) → Install"
        )

    # 3. Java
    if not shutil.which("java"):
        errors.append(
            "[MISSING] Java/JDK not found.\n"
            "  Fix: Install JDK 17+ (Eclipse Adoptium or Oracle JDK)"
        )

    # 4. Rust Android targets
    if not check_rust_targets():
        errors.append(
            "[MISSING] Rust Android target 'aarch64-linux-android' not installed.\n"
            "  Fix: Run 'rustup target add aarch64-linux-android'"
        )

    # 5. Tauri Android init
    gen_android = os.path.join(script_dir, "src-tauri", "gen", "android")
    if not os.path.isdir(gen_android):
        errors.append(
            "[MISSING] Tauri Android project not initialized.\n"
            "  Fix: Run 'npx tauri android init' in meridian_mobile/"
        )

    if errors:
        print("=" * 60)
        print("  MERIDIAN-X APK BUILD — PREREQUISITE CHECK FAILED")
        print("=" * 60)
        for err in errors:
            print(f"\n  {err}")
        print("\n" + "=" * 60)
        sys.exit(1)

    assert sdk_path is not None
    assert ndk_path is not None
    return sdk_path, ndk_path


def build_apk(target_dir=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)

    exec_dirs = [
        os.path.join(script_dir, "executables"),
        os.path.join(root_dir, "executables")
    ]
    if target_dir:
        exec_dirs.append(target_dir)

    for ed in exec_dirs:
        os.makedirs(ed, exist_ok=True)

    print("=" * 60)
    print("      MERIDIAN-X MOBILE APK BUILDER (Native)")
    print("=" * 60)

    # Validate all prerequisites
    sdk_path, ndk_path = validate_prerequisites(script_dir)

    # Set environment for Tauri/Gradle
    os.environ["ANDROID_HOME"] = sdk_path
    os.environ["ANDROID_SDK_ROOT"] = sdk_path
    os.environ["NDK_HOME"] = ndk_path
    
    jdk_path = find_compatible_jdk()
    if jdk_path:
        os.environ["JAVA_HOME"] = jdk_path
        print(f"  JAVA_HOME    = {jdk_path}")
    print(f"  ANDROID_HOME = {sdk_path}")
    print(f"  NDK_HOME     = {ndk_path}")

    primary_output_apk = os.path.join(exec_dirs[0], "meridian-x-mobile.apk")

    # Step 1: Build frontend
    print("\n[1/2] Building mobile frontend (Vite)...")
    npm_cmd = shutil.which("npm") or "npm"
    build_res = subprocess.run([npm_cmd, "run", "build"], cwd=script_dir, shell=True)
    if build_res.returncode != 0:
        print("[ERROR] Vite build failed. Fix npm errors above.")
        sys.exit(build_res.returncode)
    print("[OK] Frontend compiled to dist/")

    # Step 2: Native Tauri Android build
    print("\n[2/2] Building native Android APK via Tauri...")
    print("  (First build takes 5-15 minutes — Rust cross-compilation + Gradle)")

    cmd = ["npx", "tauri", "android", "build", "--apk"]
    res = subprocess.run(cmd, cwd=script_dir, shell=True)
    if res.returncode != 0:
        # Check if native .so was compiled (symlink failure on Windows non-dev mode)
        so_src = os.path.join(script_dir, "src-tauri", "target", "aarch64-linux-android", "release", "libapp_lib.so")
        gen_android_dir = os.path.join(script_dir, "src-tauri", "gen", "android")
        
        if os.path.exists(so_src) and os.path.isdir(gen_android_dir):
            print("\n[NOTE] Tauri CLI stopped due to Windows symlink permission. Running Gradle assembly fallback...")
            
            # Copy .so manually
            jni_dir = os.path.join(gen_android_dir, "app", "src", "main", "jniLibs", "arm64-v8a")
            os.makedirs(jni_dir, exist_ok=True)
            dest_so = os.path.join(jni_dir, "libapp_lib.so")
            shutil.copy2(so_src, dest_so)
            print(f"  [OK] Copied native library to {dest_so}")
            
            # Write server address temp file required by Tauri Gradle plugin
            temp_dir = os.environ.get("TEMP", os.environ.get("TMP", "C:\\Windows\\Temp"))
            temp_addr = os.path.join(temp_dir, "com.meridian.x.mobile-server-addr")
            with open(temp_addr, "w") as f:
                f.write("http://127.0.0.1:1420")
            print(f"  [OK] Created server addr file at {temp_addr}")
            
            # Invoke Gradlew directly for arm64
            gradlew_cmd = os.path.join(gen_android_dir, "gradlew.bat" if os.name == "nt" else "gradlew")
            gradle_res = subprocess.run([gradlew_cmd, "assembleArm64Release"], cwd=gen_android_dir, shell=True)
            if gradle_res.returncode != 0:
                print("\n[ERROR] Gradle assembleArm64Release failed!")
                sys.exit(gradle_res.returncode)
        else:
            print("\n[ERROR] Native Android APK build failed!")
            print("  Check errors above.")
            sys.exit(res.returncode)


    # Find the built APK
    apk_search_paths = [
        os.path.join(script_dir, "src-tauri", "gen", "android", "app", "build", "outputs", "apk", "arm64", "release", "app-arm64-release.apk"),
        os.path.join(script_dir, "src-tauri", "gen", "android", "app", "build", "outputs", "apk", "release", "app-release.apk"),
        os.path.join(script_dir, "src-tauri", "gen", "android", "app", "build", "outputs", "apk", "arm64", "release", "app-arm64-release-unsigned.apk"),
        os.path.join(script_dir, "src-tauri", "gen", "android", "app", "build", "outputs", "apk", "release", "app-release-unsigned.apk"),
    ]

    found_apk = None
    for src in apk_search_paths:
        if os.path.exists(src):
            found_apk = src
            break

    if not found_apk:
        # Broad search fallback
        gen_android = os.path.join(script_dir, "src-tauri", "gen", "android")
        for root, dirs, files in os.walk(gen_android):
            for f in files:
                if f.endswith(".apk"):
                    found_apk = os.path.join(root, f)
                    break
            if found_apk:
                break

    if not found_apk:
        print("\n[ERROR] Build succeeded but APK file not found!")
        print("  Searched in: src-tauri/gen/android/app/build/outputs/apk/")
        sys.exit(1)

    # Copy to executables
    shutil.copy2(found_apk, primary_output_apk)
    apk_size_mb = os.path.getsize(primary_output_apk) / (1024 * 1024)
    print(f"\n[SUCCESS] Native Android APK built: {primary_output_apk} ({apk_size_mb:.1f} MB)")

    # Sync to other output dirs
    for ed in exec_dirs[1:]:
        dest_apk = os.path.join(ed, "meridian-x-mobile.apk")
        shutil.copy2(primary_output_apk, dest_apk)
        print(f"[SYNCED] {dest_apk}")

    print(f"\n{'=' * 60}")
    print(f"  APK ready! Transfer to Android device and install.")
    print(f"  Note: Enable 'Install from Unknown Sources' on phone.")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    build_apk()
