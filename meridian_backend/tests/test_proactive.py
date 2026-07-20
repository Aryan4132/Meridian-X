import pytest
import asyncio
from src.core.bus import event_bus
import src.core.proactive as proactive

def test_game_mode_suppression():
    async def run_test():
        # 1. Enable game mode
        proactive.game_mode_active = True
        
        # Subscribe to topic to get queue
        queue = event_bus.subscribe("proactive_nudge")
        
        # 2. Try publishing a regular nudge while in game mode (should be suppressed)
        proactive.publish_nudge_sync(
            nudge_type="system_health",
            title="High CPU Load",
            message="CPU load is high",
            mascot_state="worried"
        )
        
        # Check if queue has items (should have none)
        await asyncio.sleep(0.1)
        assert queue.qsize() == 0
        
        # 3. Publish a game mode state update nudge (should NOT be suppressed)
        proactive.publish_nudge_sync(
            nudge_type="game_mode_changed",
            title="Game Mode Disabled",
            message="Game mode has been turned off.",
            mascot_state="happy"
        )
        
        # Wait and read from queue
        try:
            event = await asyncio.wait_for(queue.get(), timeout=1.0)
            assert event["type"] == "game_mode_changed"
        except asyncio.TimeoutError:
            pytest.fail("Nudge was not published to the event bus.")
        
        # Restore default state
        proactive.game_mode_active = False

    asyncio.run(run_test())
