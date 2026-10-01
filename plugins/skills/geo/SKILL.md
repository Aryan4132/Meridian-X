---
name: geo
version: 1.0.0
description: Geolocation, local weather, and spatial query biasing.
keywords: [weather, location, geo, nearby, address, coordinates, where is, forecast]
---

# Geo Skill

Location and weather routing. Loaded lazily on where/weather/nearby
prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `resolve_location` | 0 | Resolve a place to coordinates. |
| `get_localized_weather` | 0 | Weather for a location. |
| `bias_query_spatially` | 0 | Bias a query to a locale. |
