# Meridian-X Butler Skill Plugin SDK

The **Meridian-X Butler Skill Plugin SDK** enables developers to build signed, sandboxed third-party plugins that extend Meridian-X's capabilities with custom tools and butler skills.

---

## Directory Structure

Plugins are loaded dynamically from the root `plugins/` directory:

```text
Meridian-X/
└── plugins/
    ├── example_plugin.py
    └── custom_weather.py
```

---

## Plugin Manifest & Permission Tiers

Every plugin module should define a `PLUGIN_MANIFEST` dictionary:

```python
# plugins/custom_weather.py

def get_current_weather(city: str) -> str:
    """Fetch current weather for a specified city."""
    # Custom plugin logic here
    return f"Weather in {city}: 22°C, Sunny"

PLUGIN_MANIFEST = {
    "name": "Weather Butler Plugin",
    "version": "1.0.0",
    "author": "Meridian Contributor",
    "description": "Provides weather updates and forecast queries.",
    "permissions": ["NETWORK_ACCESS"],
    "tools": {
        "get_current_weather": {
            "tier": 1,
            "func": get_current_weather,
            "description": "Returns weather telemetry for a city."
        }
    }
}
```

### Permission Tiers

- **Tier 0 (Safe / Read-Only)**: Pure informational tools, string utilities, status checks.
- **Tier 1 (Standard)**: Read-only network requests, local filesystem reads, non-mutating searches.
- **Tier 2 (Elevated / Mutating)**: File writes, API mutation endpoints, system preferences changes.
- **Tier 3 (Critical / Protected)**: OS shell command execution, hardware state modification, financial transactions.

---

## Manifest Signature Verification

To distribute signed third-party plugins, add a `SIGNATURE` field computed over the plugin code:

```python
PLUGIN_MANIFEST = {
    "name": "Verified Secure Plugin",
    "version": "1.0.0",
    "signature": "SHA256:a4f8b9...",
    "tools": { ... }
}
```

---

## Loading & Hot-Reloading

Plugins are auto-discovered on startup or reloaded via REST API:

```http
POST /api/plugins/reload
```

---

## Best Practices

1. **Failure Safety**: Wrap all external I/O or API calls in `try/except` blocks.
2. **Namespace Isolation**: Avoid shadowing global modules or stdlib names.
3. **No Side Effects on Import**: Perform network or hardware initialization lazily inside tool functions.
