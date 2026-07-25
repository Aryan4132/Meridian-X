import os
import sys
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database import save_user_profile, get_user_profile

def test_context_token_limit_profile_persistence():
    save_user_profile("context_token_limit", 16384)
    val = get_user_profile("context_token_limit")
    assert val == 16384 or val == "16384"
    
    # Calculate 80% threshold
    limit = int(val)
    warn_limit = int(limit * 0.8)
    assert limit == 16384
    assert warn_limit == 13107

def test_custom_token_limit_calculation():
    custom_limit = 32768
    warn_limit = int(custom_limit * 0.8)
    assert warn_limit == 26214
    
    estimated_tokens = 27000
    assert estimated_tokens > warn_limit
    pct = (estimated_tokens / custom_limit) * 100
    assert round(pct, 1) == 82.4
