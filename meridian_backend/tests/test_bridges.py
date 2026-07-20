import time
import pytest
from src.core.telegram_bridge import _is_rate_limited
from src.core.discord_bridge import _is_rate_limited_discord

def test_telegram_rate_limiter():
    chat_id = 99999
    
    # First 5 calls within the window should not be limited
    for i in range(5):
        assert _is_rate_limited(chat_id) is False
        
    # 6th call should be rate limited
    assert _is_rate_limited(chat_id) is True

def test_discord_rate_limiter():
    user_id = 88888
    
    # First 5 calls within the window should not be limited
    for i in range(5):
        assert _is_rate_limited_discord(user_id) is False
        
    # 6th call should be rate limited
    assert _is_rate_limited_discord(user_id) is True
