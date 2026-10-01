---
name: travel
version: 1.0.0
description: Trip planning, leave calculation, and upcoming-travel tracking.
keywords: [flight, trip, travel, leave, vacation, itinerary, hotel, journey]
---

# Travel Skill

Plans trips and computes leave windows. Loaded lazily on travel,
flight, or vacation prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `create_trip` | 1 | Create a trip plan with dates and legs. |
| `calculate_leave_by_time` | 0 | Compute leave required for a window. |
| `get_upcoming_trips` | 0 | List upcoming trips. |
