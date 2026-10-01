---
name: health
version: 1.0.0
description: Wearable ingestion, wellness scoring, hydration, and breaks.
keywords: [health, step, steps, sleep, heart, heartrate, hydration, water, workout, calories, wellness, ergonomic, break reminder]
---

# Health Skill

Wearable health and ergonomics butler. Loaded lazily on health,
fitness, sleep, or hydration prompts.

## Tools

| Tool | Tier | Purpose |
| ---- | ---- | ------- |
| `sync_wearable_health_data` | 1 | Ingest wearable metrics. |
| `get_health_metrics_summary` | 0 | Summarize health metrics. |
| `track_hydration` | 0 | Log water intake. |
| `trigger_ergonomic_break` | 0 | Nudge an ergonomic break. |
| `calculate_daily_wellness_score` | 0 | Daily holistic wellness score. |
