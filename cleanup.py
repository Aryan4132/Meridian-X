import os
import shutil

def cleanup_workspace():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    print("[Cleanup] Starting Meridian-X workspace cleanup...")
    
    # 1. Clean LanceDB / vector databases
    memory_paths = [
        os.path.join(root_dir, "meridian_memory"),
        os.path.join(root_dir, "meridian_backend", "meridian_memory")
    ]
    for memory_dir in memory_paths:
        if os.path.exists(memory_dir):
            try:
                shutil.rmtree(memory_dir)
                print(f"  [Clean] Removed LanceDB memory directory: {os.path.relpath(memory_dir, root_dir)}")
            except Exception as e:
                print(f"  [Error] Failed to remove LanceDB ({memory_dir}): {e}")
            
    # 2. Clean temporary screen recordings
    recordings_dir = os.path.join(root_dir, "recordings")
    if os.path.exists(recordings_dir):
        try:
            shutil.rmtree(recordings_dir)
            print("  [Clean] Removed screen recordings directory.")
        except Exception as e:
            print(f"  [Error] Failed to remove screen recordings: {e}")
            
    # 3. Clean Secrets Vault
    vault_paths = [
        os.path.join(root_dir, "vault.enc"),
        os.path.join(root_dir, "meridian_backend", "vault.enc")
    ]
    for vault_file in vault_paths:
        if os.path.exists(vault_file):
            try:
                os.remove(vault_file)
                print(f"  [Clean] Removed encrypted secrets vault file: {os.path.relpath(vault_file, root_dir)}")
            except Exception as e:
                print(f"  [Error] Failed to remove secrets vault ({vault_file}): {e}")
            
    # 4. Clean Fine-Tuning data
    finetune_file = os.path.join(root_dir, "finetune_data.jsonl")
    if os.path.exists(finetune_file):
        try:
            os.remove(finetune_file)
            print("  [Clean] Removed fine-tuning data log file.")
        except Exception as e:
            print(f"  [Error] Failed to remove fine-tuning logs: {e}")

    # 5. Clean frontend build outputs (dist)
    dist_dir = os.path.join(root_dir, "meridian_frontend", "dist")
    if os.path.exists(dist_dir):
        try:
            shutil.rmtree(dist_dir)
            print("  [Clean] Removed frontend dist directory.")
        except Exception as e:
            print(f"  [Error] Failed to remove frontend dist: {e}")

    # 6. Clean Tauri Rust target directory
    tauri_target_dir = os.path.join(root_dir, "meridian_frontend", "src-tauri", "target")
    if os.path.exists(tauri_target_dir):
        try:
            shutil.rmtree(tauri_target_dir)
            print("  [Clean] Removed Tauri Rust target directory.")
        except Exception as e:
            print(f"  [Error] Failed to remove Tauri Rust target directory: {e}")

    # 7. Clean backend temporary audio files
    wav_file = os.path.join(root_dir, "meridian_backend", "test_api_f1.wav")
    if os.path.exists(wav_file):
        try:
            os.remove(wav_file)
            print("  [Clean] Removed backend temporary WAV file.")
        except Exception as e:
            print(f"  [Error] Failed to remove temporary WAV file: {e}")
            
    # 8. Clean Python __pycache__ and test cache folders
    pycache_count = 0
    pytest_cache_count = 0
    for root, dirs, files in os.walk(root_dir):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                pycache_count += 1
            except Exception:
                pass
        if ".pytest_cache" in dirs:
            pytest_path = os.path.join(root, ".pytest_cache")
            try:
                shutil.rmtree(pytest_path)
                pytest_cache_count += 1
            except Exception:
                pass
                
    if pycache_count > 0:
        print(f"  [Clean] Purged {pycache_count} Python __pycache__ folders.")
    if pytest_cache_count > 0:
        print(f"  [Clean] Purged {pytest_cache_count} pytest cache folders.")
    
    print("[Cleanup] Cleanup process complete. Workspace is back to default state.")

if __name__ == "__main__":
    cleanup_workspace()
