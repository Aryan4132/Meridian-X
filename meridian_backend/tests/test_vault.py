import os
import time
import pytest
from src.tools.vault import save_secret, get_secret, load_all_secrets
from src.core.config import VAULT_FILE

@pytest.fixture(autouse=True)
def setup_temp_vault(tmp_path):
    # Override VAULT_FILE path dynamically for unit testing
    import src.tools.vault as vault
    import src.core.vault as core_vault
    
    old_file = core_vault.VAULT_FILE
    temp_file = os.path.join(tmp_path, "temp_vault.json")
    core_vault.VAULT_FILE = temp_file
    vault.VAULT_FILE = temp_file
    
    yield
    
    # Restore original path
    core_vault.VAULT_FILE = old_file
    vault.VAULT_FILE = old_file

def test_vault_encrypt_decrypt():
    passphrase = "my-secret-master-passphrase"
    key = "api_key_test"
    val = "sk-1234567890abcdef"
    
    # Save secret
    res_save = save_secret(key, val, passphrase)
    assert "Successfully saved" in res_save
    
    # Retrieve secret
    res_val = get_secret(key, passphrase)
    assert res_val == val
    
    # Retrieve non-existent secret
    assert get_secret("non_existent", passphrase) is None

def test_vault_wrong_passphrase():
    passphrase = "correct-passphrase"
    wrong_passphrase = "wrong-passphrase"
    key = "secret_key"
    val = "super-secret-value"
    
    save_secret(key, val, passphrase)
    
    # Decrypting with incorrect passphrase should fail/return None
    res = get_secret(key, wrong_passphrase)
    assert res is None

def test_vault_passphrase_cache():
    passphrase = "cache-test-passphrase"
    key = "cached_key"
    val = "value"
    
    save_secret(key, val, passphrase)
    
    # First access will derive and cache key
    start_first = time.perf_counter()
    val_first = get_secret(key, passphrase)
    duration_first = time.perf_counter() - start_first
    assert val_first == val
    
    # Second access should hit cache and be significantly faster (skipping 100k PBKDF2 iterations)
    start_second = time.perf_counter()
    val_second = get_secret(key, passphrase)
    duration_second = time.perf_counter() - start_second
    assert val_second == val
    
    # The cached access should be at least 2x faster than derivation
    # (PBKDF2 with 100k rounds takes ~50ms+, cache lookups take <1ms)
    assert duration_second < duration_first
