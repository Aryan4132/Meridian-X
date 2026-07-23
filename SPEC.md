# Spec: Top-Left Mascot Logo Integration

## Objective
Replace the static top-left hexagon SVG logo in `NavRail.tsx` with the animated, glowing `MascotCharacter` orb companion.

## Tech Stack
React, TypeScript, Motion, Lucide Icons, Vite.

## Commands
- Build: `npm run build`
- Dev: `npm run dev`

## Boundaries
- Always: Preserve layout alignment, maintain click capability to toggle mascot window.
- Ask first: Major sidebar layout changes.
- Never: Cause visual misalignment in `NavRail.tsx`.

## Success Criteria
1. The static hexagon logo in `NavRail.tsx` is replaced by `<MascotCharacter />`.
2. The mascot animates smoothly in the top-left logo spot.
3. `npm run build` succeeds with 0 errors.
