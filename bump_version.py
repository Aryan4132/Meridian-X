import json
import re
import sys
import os

def bump_version(new_version):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    
    tauri_conf_path = os.path.join(root_dir, "meridian_frontend", "src-tauri", "tauri.conf.json")
    cargo_toml_path = os.path.join(root_dir, "meridian_frontend", "src-tauri", "Cargo.toml")
    package_json_path = os.path.join(root_dir, "meridian_frontend", "package.json")
    
    print(f"Bumping version to {new_version}...")
    
    # 1. Update tauri.conf.json
    if os.path.exists(tauri_conf_path):
        try:
            with open(tauri_conf_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["version"] = new_version
            with open(tauri_conf_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"  [OK] Updated {os.path.relpath(tauri_conf_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update tauri.conf.json: {e}")
            
    # 2. Update package.json
    if os.path.exists(package_json_path):
        try:
            with open(package_json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            data["version"] = new_version
            with open(package_json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            print(f"  [OK] Updated {os.path.relpath(package_json_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update package.json: {e}")
            
    # 3. Update Cargo.toml
    if os.path.exists(cargo_toml_path):
        try:
            with open(cargo_toml_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = re.sub(
                r'(^\[package\].*?\bversion\s*=\s*")[^"]+(")',
                r'\g<1>' + new_version + r'\g<2>',
                content,
                count=1,
                flags=re.DOTALL | re.MULTILINE
            )
            with open(cargo_toml_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [OK] Updated {os.path.relpath(cargo_toml_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update Cargo.toml: {e}")

    # 4. Update api.py (CURRENT_VERSION = "x.y.z")
    api_py_path = os.path.join(root_dir, "meridian_backend", "api.py")
    if os.path.exists(api_py_path):
        try:
            with open(api_py_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = re.sub(
                r'CURRENT_VERSION\s*=\s*"[^"]+"',
                f'CURRENT_VERSION = "{new_version}"',
                content
            )
            with open(api_py_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [OK] Updated {os.path.relpath(api_py_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update api.py: {e}")

    # 5. Update README.md version badge
    readme_path = os.path.join(root_dir, "README.md")
    if os.path.exists(readme_path):
        try:
            with open(readme_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = re.sub(
                r'version-[0-9]+\.[0-9]+\.[0-9]+',
                f'version-{new_version}',
                content
            )
            with open(readme_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [OK] Updated {os.path.relpath(readme_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update README.md: {e}")

    # 6. Update BootSequence.tsx SUBTITLE version string
    boot_seq_path = os.path.join(root_dir, "meridian_frontend", "src", "startup", "BootSequence.tsx")
    if os.path.exists(boot_seq_path):
        try:
            with open(boot_seq_path, "r", encoding="utf-8") as f:
                content = f.read()
            new_content = re.sub(
                r"const SUBTITLE = 'v[0-9]+\.[0-9]+\.[0-9]+([^']*)'",
                f"const SUBTITLE = 'v{new_version}\\1'",
                content
            )
            with open(boot_seq_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [OK] Updated {os.path.relpath(boot_seq_path, root_dir)}")
        except Exception as e:
            print(f"  [Error] Failed to update BootSequence.tsx: {e}")

    print("Version bump complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bump_version.py <new_version>")
        sys.exit(1)
    bump_version(sys.argv[1])
