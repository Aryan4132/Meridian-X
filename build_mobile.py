#!/usr/bin/env python
"""
Meridian-X Flutter Mobile App Builder
Automates environment detection (Flutter, Android SDK, JDK 17), dependency sync,
automated test execution, release APK / platform compilation, and executable packaging.
"""

import os
import sys
import glob
import json
import shutil
import hashlib
import argparse
import subprocess
from typing import Optional, Tuple


def get_project_root() -> str:
    """Return the absolute path of the repository root."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if os.path.basename(current_dir) == "meridian_mobile":
        return os.path.dirname(current_dir)
    return current_dir


def find_android_sdk() -> Optional[str]:
    """Find Android SDK path across standard environment variables and locations."""
    candidates = [
        os.environ.get("ANDROID_HOME"),
        os.environ.get("ANDROID_SDK_ROOT"),
        os.path.expandvars(r"%LOCALAPPDATA%\Android\Sdk"),
        os.path.expanduser("~/AppData/Local/Android/Sdk"),
        os.path.expanduser("~/Android/Sdk"),
        r"C:\Android\Sdk",
        r"C:\Program Files (x86)\Android\android-sdk",
    ]
    for path in candidates:
        if path and os.path.isdir(path):
            return os.path.abspath(path)
    return None


def find_compatible_jdk() -> Optional[str]:
    """Find a JDK compatible with Gradle (preferring JDK 17/21)."""
    env_java_home = os.environ.get("JAVA_HOME")
    candidates = []

    # Common Adoptium JDK 17 / 21 locations
    adoptium_pattern = r"C:\Program Files\Eclipse Adoptium\jdk-17*"
    candidates.extend(glob.glob(adoptium_pattern))

    adoptium_21 = r"C:\Program Files\Eclipse Adoptium\jdk-21*"
    candidates.extend(glob.glob(adoptium_21))

    # Standard Java dirs
    java_pattern = r"C:\Program Files\Java\jdk-17*"
    candidates.extend(glob.glob(java_pattern))

    # Android Studio embedded jbr
    as_jbr = [
        r"C:\Program Files\Android\Android Studio\jbr",
        r"C:\Program Files\Android\Android Studio\jre",
        os.path.expandvars(r"%LOCALAPPDATA%\Programs\Android Studio\jbr"),
    ]
    candidates.extend([p for p in as_jbr if os.path.isdir(p)])

    if env_java_home and os.path.isdir(env_java_home):
        if "17" in env_java_home:
            candidates.insert(0, env_java_home)
        else:
            candidates.append(env_java_home)

    for c in candidates:
        java_bin = os.path.join(c, "bin", "java.exe" if os.name == "nt" else "java")
        if os.path.isfile(java_bin):
            return os.path.abspath(c)

    return None


def find_flutter_bin() -> str:
    """Find the flutter binary path."""
    flutter_cmd = shutil.which("flutter")
    if flutter_cmd:
        return flutter_cmd
    
    fallbacks = [
        os.path.expandvars(r"%LOCALAPPDATA%\Flutter\bin\flutter.bat"),
        r"C:\src\flutter\bin\flutter.bat",
        r"C:\flutter\bin\flutter.bat",
        os.path.expanduser(r"~\flutter\bin\flutter.bat"),
    ]
    for fb in fallbacks:
        if os.path.isfile(fb):
            return fb
    return "flutter"


def run_command(cmd: list, cwd: str, env: dict, desc: str, check: bool = True) -> subprocess.CompletedProcess:
    """Run a shell command with proper logging and status handling."""
    print(f"\n[Task] {desc}")
    print(f"       Command: {' '.join(cmd)}")
    print(f"       Working Dir: {cwd}")
    
    res = subprocess.run(cmd, cwd=cwd, env=env, shell=(os.name == "nt"))
    if check and res.returncode != 0:
        print(f"\n[ERROR] {desc} failed with exit code {res.returncode}")
        sys.exit(res.returncode)
    return res


def compute_file_sha256(filepath: str) -> str:
    """Compute SHA-256 checksum of a file."""
    hasher = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def build_flutter_app():
    parser = argparse.ArgumentParser(description="Meridian-X Flutter App Builder")
    parser.add_argument("--target", choices=["apk", "appbundle", "windows", "web"], default="apk",
                        help="Build target (default: apk)")
    parser.add_argument("--skip-tests", action="store_true", help="Skip running unit tests before build")
    parser.add_argument("--clean", action="store_true", help="Run 'flutter clean' before building")
    args = parser.parse_args()

    root_dir = get_project_root()
    mobile_dir = os.path.join(root_dir, "meridian_mobile")
    executables_dir = os.path.join(root_dir, "executables")

    # Ensure central executables directory exists
    os.makedirs(executables_dir, exist_ok=True)

    # Clean legacy/subfolder executables to prevent scattered binaries
    legacy_mobile_exec = os.path.join(mobile_dir, "executables")
    if os.path.exists(legacy_mobile_exec):
        shutil.rmtree(legacy_mobile_exec, ignore_errors=True)

    print("=" * 68)
    print("           MERIDIAN-X FLUTTER MOBILE APP BUILDER")
    print(f"  Target Output: {executables_dir}")
    print("=" * 68)

    # 1. Check flutter installation
    flutter_bin = find_flutter_bin()
    print(f"  [+] Flutter Binary : {flutter_bin}")

    # 2. Setup build environment
    build_env = os.environ.copy()

    # Detect Android SDK & JDK
    sdk_path = find_android_sdk()
    if sdk_path:
        build_env["ANDROID_HOME"] = sdk_path
        build_env["ANDROID_SDK_ROOT"] = sdk_path
        print(f"  [+] Android SDK    : {sdk_path}")
    else:
        print("  [!] Android SDK not detected in standard locations.")

    jdk_path = find_compatible_jdk()
    if jdk_path:
        build_env["JAVA_HOME"] = jdk_path
        jdk_bin_dir = os.path.join(jdk_path, "bin")
        build_env["PATH"] = f"{jdk_bin_dir}{os.pathsep}{build_env.get('PATH', '')}"
        print(f"  [+] JAVA_HOME      : {jdk_path}")
    else:
        print("  [!] Custom JDK 17 not found, using system default Java.")

    # 3. Clean if requested
    if args.clean:
        run_command([flutter_bin, "clean"], cwd=mobile_dir, env=build_env, desc="Cleaning Flutter build cache")

    # 4. Sync Dependencies
    run_command([flutter_bin, "pub", "get"], cwd=mobile_dir, env=build_env, desc="Syncing Dart dependencies (pub get)")

    # 5. Run Test Suite
    if not args.skip_tests:
        run_command([flutter_bin, "test"], cwd=mobile_dir, env=build_env, desc="Executing Flutter test suite")
    else:
        print("\n[Skip] Skipping Flutter unit tests as requested.")

    # 6. Execute Build
    print(f"\n[Build] Compiling release target: {args.target.upper()}...")
    build_cmd = [flutter_bin, "build", args.target, "--release"]
    run_command(build_cmd, cwd=mobile_dir, env=build_env, desc=f"Building Flutter Release {args.target.upper()}")

    # 7. Locate & Distribute Output Artifacts directly to executables/
    output_files = []
    if args.target == "apk":
        apk_candidates = [
            os.path.join(mobile_dir, "build", "app", "outputs", "flutter-apk", "app-release.apk"),
            os.path.join(mobile_dir, "build", "app", "outputs", "apk", "release", "app-release.apk"),
        ]
        found_apk = None
        for cand in apk_candidates:
            if os.path.isfile(cand):
                found_apk = cand
                break
        
        if not found_apk:
            apk_glob = glob.glob(os.path.join(mobile_dir, "build", "**", "*.apk"), recursive=True)
            for cand in apk_glob:
                if "release" in cand.lower() and "unaligned" not in cand.lower():
                    found_apk = cand
                    break

        if found_apk:
            dest_root_apk = os.path.join(executables_dir, "meridian-x_mobile.apk")
            shutil.copy2(found_apk, dest_root_apk)

            size_mb = os.path.getsize(dest_root_apk) / (1024 * 1024)
            sha256_hash = compute_file_sha256(dest_root_apk)

            output_files.append({
                "path": dest_root_apk,
                "size_mb": round(size_mb, 2),
                "sha256": sha256_hash
            })
            print(f"\n[Artifact] Successfully packaged APK: {dest_root_apk}")
            print(f"           Size: {size_mb:.2f} MB")
            print(f"           SHA-256: {sha256_hash}")
        else:
            print("\n[Warning] Build completed but release APK artifact could not be located.")

    elif args.target == "windows":
        windows_release_dir = os.path.join(mobile_dir, "build", "windows", "x64", "runner", "Release")
        if os.path.isdir(windows_release_dir):
            dest_bundle_dir = os.path.join(executables_dir, "meridian_mobile_windows")
            if os.path.exists(dest_bundle_dir):
                shutil.rmtree(dest_bundle_dir)
            shutil.copytree(windows_release_dir, dest_bundle_dir)
            print(f"\n[Artifact] Windows release bundle copied to: {dest_bundle_dir}")

    elif args.target == "web":
        web_release_dir = os.path.join(mobile_dir, "build", "web")
        if os.path.isdir(web_release_dir):
            dest_web_dir = os.path.join(executables_dir, "meridian_mobile_web")
            if os.path.exists(dest_web_dir):
                shutil.rmtree(dest_web_dir)
            shutil.copytree(web_release_dir, dest_web_dir)
            print(f"\n[Artifact] Web release bundle copied to: {dest_web_dir}")

    print("\n" + "=" * 68)
    print("                 FLUTTER BUILD COMPLETE")
    print("=" * 68)
    return 0


if __name__ == "__main__":
    sys.exit(build_flutter_app())
