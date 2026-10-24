# Implementation Plan - Sprint 39: Intelligence & Telemetry Suite

## Overview
Implement the 5 core improvements across Meridian-X:
1. Hybrid Sparse-Dense RAG with Reciprocal Rank Fusion & in-process fallback (PL-08, PL-11)
2. Live Browser-Use Mini-HUD Streaming & Viewport Frame API
3. Perception Stream to Proactive Nudges Bridge (PL-03, PL-04)
4. Collapsible ReAct Step Accordions & Diff Viewer in Timeline (PL-19)
5. Heterogeneous Subagent Model Routing (PL-10)

## Architecture Decisions
- **Hybrid RAG**: Implement pure Python BM25 scoring inside `src/db/rag.py` and combine with Turbovec dense scores using Reciprocal Rank Fusion `rrf_score = 0.5/(60 + dense_rank) + 0.5/(60 + bm25_rank)`.
- **Browser-Use HUD**: Capture lightweight JPEG base64 frames during `BrowserUseAgent` step executions, cache last frame in memory, and broadcast over SSE and `GET /api/browser/frame`.
- **Perception Bridge**: In `src/api/perception.py`, when error sense or terminal crash endpoints are called, automatically call `publish_nudge_sync` to surface actionable suggestions to the user without manual triggers.
- **Timeline Accordions & Diffs**: Detect unified diffs in markdown blocks (`diff` or `patch`) and render with visual green/red lines. Group ReAct step logs into collapsible badges.
- **Heterogeneous Swarm**: Resolve model provider and model source per subagent role (`gemini` for researcher, `anthropic`/`deepseek` for auditor/planner) dynamically in `SwarmAgent.execute` and `lobby_debate`.

## Verification Checkpoints
- Checkpoint 1 (Backend RAG & Swarm): Pytest for hybrid RAG search and heterogeneous swarm routing.
- Checkpoint 2 (Browser & Perception): Pytest for browser frame capture and perception nudge bridge.
- Checkpoint 3 (Frontend): Typecheck with `tsc --noEmit` and build with `npm run build`.
