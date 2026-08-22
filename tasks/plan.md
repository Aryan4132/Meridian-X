# Implementation Plan: Tasks PL-23 to PL-26

## Overview
Implement configurable Model Execution Mode (`local` vs `cloud`/`api`) and bind task decomposition to the user active `brain_model`.

## Tasks
1. **PL-23**: Bind `decompose_goal_to_checklist` and internal loop helpers to active `brain_model` in `meridian_backend/src/core/loop.py`.
2. **PL-24**: Dynamic `MERIDIAN_MODEL_SOURCE` lookup in `Timeline.tsx` and `Mascot.tsx`.
3. **PL-25**: Execution Mode UI toggle in `Settings.tsx`.
4. **PL-26**: Backend API profile & stream synchronization in `api.py`.
