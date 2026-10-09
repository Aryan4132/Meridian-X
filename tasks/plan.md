# Plan: Phase 1 Finish Hardening & Cleanups

## Overview
Elevate backend and frontend stability with three non-breaking hardening items from `fixes.md`:
1. **Consensus Debate Decoupling (`src/core/consensus_engine.py` & `src/core/loop.py`)**:
   - Implement `should_run_debate(tool_calls, goal, is_voice)` gating function.
   - Skip debate for greetings, simple Q&A, voice queries, and read-only checks.
   - Trigger debate only on code mutations, destructive actions, or multi-step execution.
   - Wire into `loop.py` and add unit test suite `tests/test_consensus_gate.py`.
2. **Audio Streaming Singleton (`meridian_frontend/src/services/streamingAudioPlayer.ts` & `Mascot.tsx`)**:
   - Eliminate redundant local `new Audio()` instances and custom queue logic in `Mascot.tsx`.
   - Route all voice audio through `streamingAudio` singleton.
3. **Structured Logging (Zero Bare Exceptions)**:
   - Purge bare `except Exception: pass` in `doc_indexer.py`, `cognitive_graph.py`, `tts.py`, `stt.py`.
   - Replace with structured logging (`logger.warning(..., exc_info=True)`).
