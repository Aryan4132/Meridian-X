# Example Plugin
TIER = 1

async def custom_echo_tool(text: str) -> str:
    """A custom echo tool that returns your text reversed."""
    return f"Echo from plugin: {text[::-1]}"
