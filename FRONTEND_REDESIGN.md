# Meridian-X Frontend — Complete Redesign Specification

> **Stack preserved:** Vite + React 19 + TypeScript + Tailwind CSS v4 + `motion/react` + `lucide-react` + Tauri v2  
> **Goal:** Rebuild from scratch. Every file deleted, every component rewritten. Futuristic, minimal, calm, NOT cluttered. One concept per screen region.

---

## 0. Philosophy & Core Rules

### The "One Region, One Job" Principle
The current UI mixes concerns in the same visual zone. The new UI must follow:

| Zone | One Responsibility |
|---|---|
| Left rail (icon-only) | Navigation **only** — no text, no stats |
| Top header bar | Page title + one action button |
| Main content | **Active tab only** — no persistent widgets from other views |
| Right drawer (collapsible) | Context-specific secondary panel (thoughts, hardware, nudges) |
| Bottom status bar | Global system pulse — daemon, CPU, model name only |

### Anti-Clutter Commandments
- No tab renders content from another tab.
- No global widgets (clock, nudge cards, pomodoro) floating over chat.
- Hardware meters live **only** in Settings and the status bar — nowhere else.
- The mascot **never** overlaps main content. It lives in its own Tauri window.
- Cards show at most **3 data points** before needing expansion.

---

## 1. File Structure (From Scratch)

```
meridian_frontend/src/
├── main.tsx                   # Entry point — unchanged logic
├── types.ts                   # All shared TypeScript interfaces
├── index.css                  # Global CSS: tokens, keyframes, utilities
│
├── components/
│   ├── Shell.tsx              # Root layout: sidebar + main + right panel + status bar
│   ├── NavRail.tsx            # Icon-only vertical nav with animated indicator
│   ├── StatusBar.tsx          # Bottom global status bar
│   ├── RightDrawer.tsx        # Collapsible context panel (thoughts, hardware)
│   └── ui/
│       ├── GlowCard.tsx       # Reusable glassmorphic card
│       ├── DataBadge.tsx      # Tiny metric pill (e.g., CPU: 24%)
│       ├── HoloButton.tsx     # Primary CTA button with scan-line effect
│       ├── TerminalLine.tsx   # Single log/thought line with type color
│       └── ProgressArc.tsx    # SVG circular arc progress for timers
│
├── views/
│   ├── Timeline.tsx           # Tab 1: Chat / ReAct thought stream
│   ├── Jobs.tsx               # Tab 2: Background scheduler
│   ├── Clipboard.tsx          # Tab 3: Clipboard history + analysis
│   ├── Productivity.tsx       # Tab 4: Pomodoro + dev stats
│   ├── SwarmDebate.tsx        # Tab 5: Multi-agent debate lobby
│   └── Settings.tsx           # Tab 6: Config + hardware meters
│
├── startup/
│   ├── BootSequence.tsx       # Animated startup splash (NEW)
│   └── SetupWizard.tsx        # 4-step first-run wizard (redesigned)
│
└── mascot/
    └── Mascot.tsx             # Mascot window — unchanged logic, new SVG art style
```

---

## 2. Design System

### 2.1 Color Tokens (`index.css`)

Replace all existing theme variables with these. Each theme has 10 tokens.

```css
:root {
  /* === MERIDIAN VOID (default) === */
  --bg-void:    #060810;   /* deepest background */
  --bg-base:    #0A0D17;   /* main app background */
  --bg-panel:   #0E1220;   /* card/panel surface */
  --bg-surface: #121828;   /* input, tag, hover surface */
  --bg-float:   #1A2236;   /* elevated elements */

  --accent:     #00E5FF;   /* primary: electric cyan */
  --accent-dim: #0094A8;   /* subdued accent */
  --accent-2:   #7C3AED;   /* secondary: deep violet */
  --accent-2-dim: #4C1D95;

  --text-bright: #F0F6FF;  /* headings */
  --text-main:   #B8C8E0;  /* body */
  --text-dim:    #5A6A80;  /* metadata */
  --text-ghost:  #2A3448;  /* placeholders */

  --border:      rgba(0, 229, 255, 0.06);   /* subtle cyan-tinted border */
  --border-glow: rgba(0, 229, 255, 0.20);   /* hover/active border */
  --danger:      #FF3B6E;
  --warning:     #FFB020;
  --success:     #00D97E;

  --radius-sm:   8px;
  --radius-md:   12px;
  --radius-lg:   20px;
  --radius-xl:   28px;

  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring:   cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

**Additional Themes (same token names, different values):**

| Theme Name | `--accent` | `--accent-2` | `--bg-base` | Vibe |
|---|---|---|---|---|
| `void` (default) | `#00E5FF` | `#7C3AED` | `#0A0D17` | Cyberpunk void |
| `aurora` | `#00FF9D` | `#FF6B6B` | `#050F0A` | Deep-space aurora |
| `ember` | `#FF6B35` | `#FFD60A` | `#0F0804` | Volcanic amber |
| `phantom` | `#C084FC` | `#F472B6` | `#090613` | Dark synthwave |
| `frost` | `#60A5FA` | `#34D399` | `#050A14` | Arctic blue |
| `paper` | `#6366F1` | `#EC4899` | `#F8FAFC` | Light mode |

### 2.2 Typography

```css
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');

body {
  font-family: 'Space Grotesk', system-ui, sans-serif;
}
.font-mono, code, pre {
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
```

### 2.3 Core Keyframe Animations

```css
/* Ambient background drift */
@keyframes void-drift {
  0%, 100% { transform: translate(0, 0) scale(1.0); }
  33%       { transform: translate(2%, -3%) scale(1.04); }
  66%       { transform: translate(-2%, 2%) scale(0.97); }
}

/* Scan line sweep (for buttons, panels) */
@keyframes scan-sweep {
  0%   { transform: translateY(-100%); opacity: 0.4; }
  100% { transform: translateY(200%); opacity: 0; }
}

/* Data pulse for terminal lines appearing */
@keyframes data-pulse {
  0%   { opacity: 0; transform: translateX(-6px); }
  100% { opacity: 1; transform: translateX(0); }
}

/* Holographic shimmer */
@keyframes holo-shimmer {
  0%, 100% { background-position: 0% 50%; }
  50%       { background-position: 100% 50%; }
}

/* Breathing core (mascot/idle) */
@keyframes breathe {
  0%, 100% { transform: scale(1); }
  50%       { transform: scale(1.015); }
}

/* Orbit ring */
@keyframes orbit {
  from { transform: rotate(0deg); }
  to   { transform: rotate(360deg); }
}

/* Cursor blink */
@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0; }
}
```

### 2.4 Global Utilities

```css
/* Ambient void background layer */
.void-bg {
  position: fixed; inset: -10%; width: 120%; height: 120%;
  z-index: -1; pointer-events: none;
  background:
    radial-gradient(ellipse 60% 50% at 15% 20%, color-mix(in srgb, var(--accent) 8%, transparent) 0%, transparent 100%),
    radial-gradient(ellipse 50% 60% at 85% 80%, color-mix(in srgb, var(--accent-2) 6%, transparent) 0%, transparent 100%),
    radial-gradient(ellipse 40% 40% at 50% 50%, color-mix(in srgb, var(--accent) 3%, transparent) 0%, transparent 100%);
  filter: blur(60px);
  animation: void-drift 28s ease-in-out infinite;
}

/* Glassmorphic panel */
.glass {
  background: linear-gradient(135deg,
    rgba(255,255,255,0.03) 0%,
    rgba(255,255,255,0.01) 100%);
  backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid var(--border);
  border-radius: var(--radius-md);
}

.glass:hover {
  border-color: var(--border-glow);
  box-shadow: 0 0 24px rgba(0, 229, 255, 0.05);
}

/* Neon text glow */
.text-glow {
  text-shadow: 0 0 20px currentColor;
}

/* Scan-line overlay on hover */
.scan-hover {
  position: relative; overflow: hidden;
}
.scan-hover::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(transparent 40%, rgba(0,229,255,0.04) 50%, transparent 60%);
  animation: scan-sweep 2.5s linear infinite;
  pointer-events: none;
}

/* Holographic animated gradient border */
.holo-border {
  position: relative;
}
.holo-border::before {
  content: '';
  position: absolute; inset: -1px;
  border-radius: inherit;
  background: linear-gradient(135deg, var(--accent), var(--accent-2), var(--accent));
  background-size: 200% 200%;
  animation: holo-shimmer 4s ease-in-out infinite;
  z-index: -1;
}
```

---

## 3. Startup Sequence — `startup/BootSequence.tsx`

> This is the most cinematic part of the new UI. Shown once every cold launch. After completion, smoothly transitions into either `SetupWizard` (first run) or the main `Shell`.

### 3.1 Boot Sequence Phases (timed, automatic)

```
Phase 0 (0–0.8s):   Black screen → void-bg fades in
Phase 1 (0.8–2.0s): Meridian-X logotype assembles letter-by-letter (staggered spans)
Phase 2 (2.0–3.5s): Holographic hexagon core appears, two orbiting rings spin up
Phase 3 (3.5–5.0s): Boot log lines scroll up one at a time, typewriter style:
                       [SYS] Initializing ReAct inference engine...  ✓
                       [SYS] Mounting SQLite + Turbovec vectors...   ✓
                       [SYS] Binding P2P swarm daemon...             ✓
                       [SYS] Checking Ollama endpoint...             ✓ / ⚠
                       [SYS] Loading Mascot companion core...        ✓
Phase 4 (5.0–5.4s): All lines fade out, hex core pulses once with peak glow
Phase 5 (5.4–5.8s): "SYSTEM ONLINE" text appears, blinks twice
Phase 6 (5.8s→):    Iris-wipe transition: clip-path circle expands from center
```

### 3.2 Boot Log Line Logic

```tsx
// Each boot line optionally hits a real API endpoint
interface BootLogLine {
  label: string;
  endpoint?: string;  // if set, GET this URL to determine real status
  status: 'pending' | 'ok' | 'warn' | 'fail';
}

const BOOT_LINES: BootLogLine[] = [
  { label: 'Initializing ReAct inference engine', endpoint: 'http://localhost:4132/api/health' },
  { label: 'Mounting SQLite + Turbovec vectors',  endpoint: 'http://localhost:4132/api/health' },
  { label: 'Binding P2P swarm daemon' },
  { label: 'Checking Ollama endpoint',  endpoint: 'http://localhost:4132/api/ollama-models' },
  { label: 'Loading Mascot companion core' },
];
// status → ✓ (ok), ⚠ (warn), ✗ (fail)
// Lines without endpoint auto-succeed after 300ms each
```

### 3.3 Hex Core SVG Structure

```svg
<!-- Outer ring: dashed, orbits clockwise, 24s -->
<circle r="80" stroke-dasharray="6 4" class="orbit-outer" />

<!-- Middle ring: dotted, orbits counter-clockwise, 16s -->
<circle r="60" stroke-dasharray="2 6" class="orbit-inner-reverse" />

<!-- Hexagon body -->
<polygon points="..." class="hex-body breathe" />

<!-- Core center glow dot -->
<circle r="12" class="core-dot pulse-glow" />
```

All CSS-animated. No canvas, no requestAnimationFrame loops.

### 3.4 Iris-Wipe Exit Transition

```css
/* Applied to the boot screen wrapper on exit */
.iris-exit {
  clip-path: circle(0% at 50% 50%);
  animation: iris-open 0.6s cubic-bezier(0.4, 0, 1, 1) forwards;
}

@keyframes iris-open {
  from { clip-path: circle(0% at 50% 50%); }
  to   { clip-path: circle(150% at 50% 50%); }
}
```

The iris exposes the main `Shell` beneath it.

### 3.5 Skip Behavior

- Skippable with any key press after Phase 2 (hex core has appeared)
- Skip → immediate iris-wipe to shell
- If `localStorage.getItem('bootSeen') === 'true'` AND app was not force-restarted: skip to Phase 3 instantly (still show boot log lines, but shorter)
- Detect cold launch from Tauri via URL param: `?coldBoot=1`

### 3.6 Boot Screen Layout

```
┌─────────────────────────────────────────────────────────┐
│                     [void-bg glow]                      │
│                                                         │
│              ╔══╗                                       │
│             ╔    ╗   ← outer dashed ring (orbiting)    │
│            ╔  ⬡  ╗  ← inner hex with glow + breathe   │
│             ╚    ╝   ← middle dotted ring (counter)    │
│              ╚══╝                                       │
│                                                         │
│         M E R I D I A N - X                            │
│       v0.1.0-alpha  ·  agentic core                    │
│                                                         │
│   ─────────────────────────────────────────            │
│   [SYS] Initializing ReAct engine...        ✓          │
│   [SYS] Mounting vector databases...        ✓          │
│   [SYS] Binding swarm daemon...             ✓          │
│   [SYS] Checking Ollama endpoint...         ⚠          │
│   [SYS] Mascot core loaded...               ✓          │
│   ─────────────────────────────────────────            │
│                                                         │
│               SYSTEM ONLINE                            │
│         [press any key to skip]                        │
└─────────────────────────────────────────────────────────┘
```

---

## 4. Setup Wizard (First Run) — `startup/SetupWizard.tsx`

> Replaces `FirstRunWizard.tsx`. Same 4-step logic, completely different aesthetic.

### 4.1 Layout

- Full screen, centered card, max-width 520px
- Background: void-bg + hex core (120px, 30% opacity, top-right corner, decorative)
- Card: `glass` + `holo-border` class — the animated gradient border makes it feel alive
- Step indicator: horizontal segmented bar at top (segments fill with accent), not "Step 2 of 4" text
- Navigation: "Back" (ghost HoloButton) + "Continue" (primary HoloButton) in bottom row

### 4.2 Step Designs

**Step 1 — Welcome**
- Large "Welcome to Meridian-X" heading (Space Grotesk, 700 weight)
- Subtitle: "Your autonomous local intelligence layer"
- Two feature chips with icons: `[🔒 Privacy-first]` `[📡 Offline-capable]`
- No form fields on this step

**Step 2 — Integrations**
- Heading: "Connect Your Services"
- Accordion sections (collapsed by default, expand on click with motion animation):
  - 🌐 **Web Search** → Tavily API key field
  - 💬 **Notifications** → Discord token, Telegram bot token, Telegram chat ID, WhatsApp phone (all in one accordion panel)
- Helper text: "All optional. Configure later in Settings."

**Step 3 — Brain Model**
- Heading: "Choose Intelligence Engine"
- Provider selector: **visual card grid** (not `<select>`) — 5 cards: Ollama, OpenAI, Anthropic, Gemini, DeepSeek
  - Each card: provider icon + name + descriptor ("Offline · Free" or "Cloud · API Key")
  - Selected card gets holo-border glow + filled background
- After selecting: inline form slides down (motion `height: auto`) with either:
  - Ollama: host URL field + Re-test Connection button + available model chips
  - Cloud providers: single API key field + pre-set model dropdown
- Ollama status shown as a live badge: `● Connected` / `✕ Offline`

**Step 4 — All Set**
- Animated celebration: small dots burst from center, fade
- "Configuration complete" heading
- 3 shortcut chips: `Alt+M` `Alt+V` `Alt+Shift+M`
- Full-width "Launch Meridian-X" `HoloButton` with scan-line effect + Bot icon

---

## 5. Main Shell Layout — `Shell.tsx`

### 5.1 Layout Grid

```
┌──────┬──────────────────────────────────────┬─────────────┐
│      │                                      │             │
│ Nav  │           Main Content               │   Right     │
│ Rail │           (active view)              │   Drawer    │
│ 64px │           flex-1, overflow-y-auto    │   320px     │
│      │                                      │(collapsible)│
├──────┴──────────────────────────────────────┴─────────────┤
│                  Status Bar (32px)                        │
└───────────────────────────────────────────────────────────┘
```

- NavRail: fixed, 64px wide, icon-only, `z-20`
- Main content: `flex-1`, `overflow-y-auto`, `padding: 32px`
- Right drawer: collapsible 0↔320px with motion layout animation
- Status bar: 32px, `position: sticky` at bottom, `border-top: 1px solid var(--border)`

### 5.2 NavRail — `NavRail.tsx`

```
┌─────────┐
│   ⬡    │  ← Meridian hex logo SVG (40px), glows on hover
│         │
│   💬   │  ← Timeline       (MessageSquare icon)
│   ⚡   │  ← Jobs           (Zap icon)
│   📋   │  ← Clipboard      (Clipboard icon)
│   ⏱    │  ← Productivity   (Timer icon)
│   🤖   │  ← Swarm Debate   (Bot icon)
│   ⚙    │  ← Settings       (Settings2 icon)
│         │
│  ─────  │  ← separator
│   👁    │  ← Switch to Mascot (Eye icon)
│   ─    │  ← separator
│   ↗    │  ← Minimize (Minus icon) — Tauri only
│   ✕    │  ← Close to tray (X icon) — Tauri only
└─────────┘
```

**NavRail active indicator:**
- `layoutId="active-tab-bg"` shared motion div — pill shape, slides between nav items
- Active icon: `--accent` color + `text-glow` class
- Inactive icon: `--text-dim`, hover → `--text-main`
- Left edge indicator: 2px wide, `--accent` colored bar that tracks with active tab

### 5.3 Right Drawer — `RightDrawer.tsx`

Content per active tab:

| Active Tab | Right Drawer Shows |
|---|---|
| Timeline | Live ReAct thought stream (SSE), model badge, stream status |
| Jobs | Last 5 run previews with status dots |
| Clipboard | Stats: total items captured, last capture time, search hit count |
| Productivity | CPU arc + RAM arc (live hardware meters) |
| Swarm Debate | Agent legend: Coder/Auditor/QA color chips + debate timer |
| Settings | Same CPU + RAM arcs as Productivity |

Drawer anatomy:
- Sticky header: `Section Title` + collapse `<` button
- Content: scrollable `flex-col gap-4` 
- Collapses to 0 width (not hidden — `overflow: hidden` + motion width)
- On collapse: main content smoothly expands to fill

### 5.4 Status Bar — `StatusBar.tsx`

```
[●] Backend Online      ⬡ MERIDIAN-X      Model: qwen2.5-coder:7b    [CPU 18%]  [RAM 42%]
```

- Left: `●` pulse dot + "Backend Online" OR "●" static red + "Backend Offline"
- Center: hex logo + "MERIDIAN-X" wordmark, `text-dim`
- Right: model name from `localStorage.MERIDIAN_MODEL` + two `DataBadge` pills for CPU/RAM
- Polls `/api/system-usage` every 5 seconds
- Height strictly 32px, no wrapping

---

## 6. View Specifications

### 6.1 Timeline — `views/Timeline.tsx`

**Layout (full height flex column):**
```
Header (48px): "Timeline Logs"  +  [Clear Logs]
────────────────────────────────────────────────
Messages scroll area (flex-1, overflow-y-auto)
────────────────────────────────────────────────
Input bar (64px, sticky bottom)
```

**Message bubble anatomy:**
- User messages: right-aligned, `--bg-surface` fill, 2px `--accent-2` left accent strip
- Bot messages: left-aligned, `--bg-panel` fill, 2px `--accent` left accent strip
- Avatars: 32×32 rounded squares (not circles)
  - Bot: mini SVG hex icon in `--accent` color
  - User: initials "U" in `--accent-2` color
- Timestamp: `text-dim`, 10px, `JetBrains Mono`, top-right corner
- During streaming: timestamp replaced with `[live ●]` blinking badge

**Thoughts block (collapsible, inside bubble):**
- Pill toggle: `▶ ReAct Thoughts (3)` — expands inline below message text
- When streaming: live thoughts appear in the **Right Drawer**, NOT inside a half-built bubble
- After stream ends: all thoughts move into the finalized bubble

**Safety gate (inside bot message):**
```
┌─ ⚠ SAFETY CONFIRMATION [TIER 2] ──────────────────┐
│ Tool: run_python                                    │
│ This operation will execute code on your machine.  │
│ [✓ Approve]  [✗ Reject]                           │
└─────────────────────────────────────────────────────┘
```
- Yellow-tinted border, `--warning` accent
- Rendered inside the bot message card, not as a separate card

**Heal proposal (inside bot message):**
```
┌─ 🩹 Auto-Healing Patch Proposal ───────────────────┐
│ File: /path/to/file.py                             │
│ ┌─ Original ─────┐ ┌─ Correction ────┐            │
│ │ old code here  │ │ new code here   │            │
│ │ ...            │ │ ...             │            │
│ └────────────────┘ └─────────────────┘            │
│ [Apply Heal]                                       │
└─────────────────────────────────────────────────────┘
```
- Two-column diff, `JetBrains Mono`, max-height 200px with scroll
- `[Apply Heal]`: small `HoloButton` variant `primary`

**Input bar:**
```
┌────────────────────────────────────────── [⊕] [↑] ┐
│  Ask Meridian-X to perform actions...              │
└────────────────────────────────────────────────────┘
```
- `[⊕]`: file upload trigger (paperclip icon) — triggers RAG ingest
- `[↑]`: send button (`HoloButton` 40×40, primary)
- Drag-drop: full-screen overlay when file is being dragged over the window

---

### 6.2 Jobs — `views/Jobs.tsx`

**Layout (two-column grid):**
```
┌────────────────────┬────────────────────────────────┐
│  Schedule Task     │  Active Run Logs               │
│  (col-span-1)      │  (col-span-2)                  │
│                    │                                 │
│  Goal Prompt       │  ● RUN #42 · success · 2m ago  │
│  [textarea      ]  │  "Check system memory..."      │
│                    │  [▶ View Log]                   │
│  Interval (sec)    │                                 │
│  [number        ]  │  ✕ RUN #41 · failed · 8m ago   │
│                    │  "Analyze codebase..."          │
│  [Schedule Agent]  │  [▶ View Log]                   │
│                    │                                 │
└────────────────────┴────────────────────────────────┘
```

**Run log card design:**
- Status dot: `●` green (success) or `✕` red (failed), before `RUN #N`
- Goal text: 2-line truncation, click to expand
- Time: relative (`2m ago`) via simple time-diff utility
- `[▶ View Log]`: ghost button that expands a `<pre>` block inline (max 80px height, scrollable)

---

### 6.3 Clipboard — `views/Clipboard.tsx`

**Layout:**
```
Header: "Clipboard History"
────────────────────────────────────────────────
🔍 [Filter clipboard events...]
────────────────────────────────────────────────
List of clipboard items (overflow-y-auto)
```

**Item card:**
- Monospace font, 1-line preview, truncated with `…`
- Click to expand to full text
- `[⚡ Analyze]` button: right-aligned, icon-only (compressed) → shows text on hover
- Timestamp: relative, `text-dim`
- Auto-tagging: if text starts with `http`, show `[url]` badge; if contains code keywords, show `[code]` badge

---

### 6.4 Productivity — `views/Productivity.tsx`

**Layout (two-column):**
```
┌─────────────────┬───────────────────────────────────┐
│  Focus Timer    │  Stats Grid                       │
│                 │  ┌──────┐ ┌──────┐ ┌──────┐      │
│  ProgressArc    │  │ 87%  │ │  12  │ │   7  │      │
│  (160px)        │  │Scess │ │Heals │ │ Git  │      │
│  24:59          │  └──────┘ └──────┘ └──────┘      │
│                 │  ┌──────┐                         │
│  [▶] [↺]       │  │ 🍅 3 │                         │
│                 │  │Pmdr  │                         │
│                 │  └──────┘                         │
│                 │                                   │
│                 │  System Diagnostics               │
│                 │  ┌─────────────────────────────┐  │
│                 │  │ AST Watcher:   ACTIVE       │  │
│                 │  │ Leak Guard:    ACTIVE       │  │
│                 │  └─────────────────────────────┘  │
└─────────────────┴───────────────────────────────────┘
```

**Pomodoro timer:**
- `ProgressArc` SVG, 160px, stroke `--accent`, countdown direction (full = 25:00 start)
- Time display centered inside arc: 28px, bold, `JetBrains Mono`
- Active state: outer ring pulses (CSS `@keyframes breathe` on a larger circle)
- `[▶ Start]` / `[⏸ Pause]` + `[↺ Reset]` — small pill buttons below arc
- Session complete: inline animation inside card ("Session Complete! 🎉"), no `alert()`

**Stats cards:**
- 4 cards in a grid, compact (48px tall)
- Each: bold number (top) + label (bottom, `text-dim`, 10px)
- Hover: `translateY(-2px)` + `border-glow`
- No bright background fills — just glass + 1px bottom accent line per card

---

### 6.5 Swarm Debate — `views/SwarmDebate.tsx`

**Layout:**
```
Header: "Consensus Debate Lobby"
────────────────────────────────────────────────
[Task input ___________________________] [Debate ▶]
────────────────────────────────────────────────
┌─────────────── DEBATE LOG ──────────────────┐
│ > Lobby initialized.                        │
│ > Invoking agents: Coder, Auditor, QA...    │
│                                             │
│ [CODER]    Suggest AES-256-GCM impl.        │  ← --success
│ [AUDITOR]  Salt params verified. No leak.   │  ← --warning
│ [QA]       Exit code 0. Parsed clean.       │  ← #60A5FA
│                                             │
│ ── CONSENSUS ─────────────────────────────  │
│ → Approved. Proceed with implementation.    │  ← --accent
│                                             │
│ _                                           │  ← blinking cursor
└─────────────────────────────────────────────┘
```

**Terminal log design:**
- Black background `--bg-void`, fixed height 360px, auto-scroll to bottom
- `TerminalLine` component handles per-type color
- Each new line: `data-pulse` animation (slide from left 6px, 120ms)
- Blinking `_` cursor: CSS `animation: blink 1s step-end infinite` when `debating === false`
- When debating: `> Running agent debate loops...` pulses with `--accent` color
- Right Drawer shows: agent legend pills (Coder=green, Auditor=yellow, QA=blue) + elapsed time counter

---

### 6.6 Settings — `views/Settings.tsx`

**Layout (two-column):**
```
Header: "Settings"
────────────────────────────────────────────────
┌──────────────────────────┬─────────────────────┐
│  AI Configuration        │  Hardware Vitals     │
│                          │                      │
│  Provider card grid      │  CPU   ╭──arc──╮ 18%│
│  [Ollama][OAI][ANT]...   │        ╰───────╯     │
│                          │  RAM   ╭──arc──╮ 42%│
│  Host / API key field    │        ╰───────╯     │
│  Brain model dropdown    │                      │
│  Vision model dropdown   │  ──────────────────  │
│                          │  Theme               │
│  ── Integrations ──      │  ◉ void  ○ aurora    │
│  Tavily / Discord /      │  ○ ember ○ phantom   │
│  Telegram / WhatsApp     │  ○ frost ○ paper     │
│                          │                      │
│  ── System ──            │                      │
│  [ ] Game Mode           │                      │
│                          │                      │
│  [Save Settings ✓]       │                      │
└──────────────────────────┴─────────────────────┘
```

**Left column design:**
- Section headers: `── Section Name ──` with `text-dim` lines, not `<h2>` headings
- Inputs: bottom-border animation on focus (1px `--text-ghost` → `--accent`, transition 200ms)
- Provider selector: same visual card grid as SetupWizard Step 3
- API key inputs: always `type="password"` with show/hide eye toggle button
- Save button: `HoloButton` full-width, states: idle → saving (spinner) → saved (checkmark, 2s) → idle

**Right column design:**
- Two `ProgressArc` at 80px radius, side-by-side (or stacked on narrow)
- Arcs are read-only, update every 3s from `/api/system-usage`
- Theme switcher: radio group, each option has a color swatch circle before the label

---

## 7. Reusable UI Components

### `GlowCard.tsx`
```tsx
interface GlowCardProps {
  children: React.ReactNode;
  glow?: 'accent' | 'danger' | 'warning' | 'success' | 'none';
  hover?: boolean;   // enables translateY(-2px) + border-glow on hover
  className?: string;
}
// Renders: <div class="glass [glow-class] [hover-class]">
```

### `HoloButton.tsx`
```tsx
interface HoloButtonProps {
  children: React.ReactNode;
  variant?: 'primary' | 'ghost' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  loading?: boolean;
  disabled?: boolean;
  onClick?: () => void;
  type?: 'button' | 'submit';
  className?: string;
}
// primary: gradient bg + scan-sweep ::after pseudo-element
// ghost: transparent + border 1px var(--border), hover → var(--border-glow)
// danger: --danger tint background
```

### `DataBadge.tsx`
```tsx
interface DataBadgeProps {
  label: string;
  value: string | number;
  color?: 'accent' | 'accent-2' | 'success' | 'danger' | 'warning' | 'dim';
}
// Renders pill: [CPU 18%] with colored left dot
```

### `TerminalLine.tsx`
```tsx
interface TerminalLineProps {
  text: string;
  type: 'system' | 'coder' | 'auditor' | 'qa' | 'consensus' | 'error' | 'ok';
  delay?: number;  // stagger animation delay in ms
}
// Animates in with data-pulse keyframe
// Colors: coder=--success, auditor=--warning, qa=#60A5FA, system=--text-dim,
//         consensus=--accent, error=--danger, ok=--success
```

### `ProgressArc.tsx`
```tsx
interface ProgressArcProps {
  value: number;       // current value
  max?: number;        // default 100
  size?: number;       // SVG viewBox size, default 160
  strokeWidth?: number;// default 8
  label?: string;      // text below the value number
  color?: string;      // stroke color, default var(--accent)
  animated?: boolean;  // breathing outer ring
}
// Pure SVG. Uses strokeDasharray + strokeDashoffset for arc fill.
// Center: shows value number (bold, 28px) + optional label (10px, text-dim)
```

---

## 8. Global State — `AppContext.tsx`

```tsx
interface AppContextValue {
  activeTab: 'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'lobby' | 'settings';
  setActiveTab: (tab: TabId) => void;
  theme: string;
  setTheme: (theme: string) => void;
  backendAlive: boolean;
  modelName: string;          // from localStorage.MERIDIAN_MODEL
  rightDrawerOpen: boolean;
  setRightDrawerOpen: (v: boolean) => void;
  systemUsage: { cpu: number; ram: number };
}
```

No Zustand, no Redux. Each view manages its own `useState`. AppContext only for shell-level globals that cross component boundaries.

---

## 9. Animation Rules

| Element | Animation | Duration | Easing |
|---|---|---|---|
| Tab switch | fade + slide Y (12px) via `AnimatePresence mode="wait"` | 180ms | `ease-out-expo` |
| Right drawer toggle | width 0↔320px via `motion` layout | 260ms | `ease-spring` |
| Message bubble appear | `data-pulse` + scale 0.98→1 | 240ms | `ease-out-expo` |
| Card hover elevation | `translateY(-2px)` | 120ms | `ease` |
| Boot log lines | staggered `data-pulse`, 80ms each | 80ms | `ease-out-expo` |
| Pomodoro arc | CSS `transition: stroke-dashoffset 800ms ease` | 800ms | `ease` |
| Safety gate appear | scale 0.95→1 + opacity 0→1 | 300ms | `ease-spring` |
| Iris wipe exit | `clip-path` circle expand | 600ms | `cubic-bezier(0.4,0,1,1)` |
| NavRail indicator | `layoutId` shared motion pill | auto | spring |
| Scan-line sweep | continuous `scan-sweep` on hover | 2.5s | `linear` |
| Holo border shimmer | continuous `holo-shimmer` | 4s | `ease-in-out` |

**Performance rules:**
- `will-change: transform` only on animated elements, removed after animation
- No JS `requestAnimationFrame` loops — CSS `@keyframes` or `motion/react` declarative variants
- `AnimatePresence mode="wait"` for tab transitions
- Shared layout animation (`layoutId`) ONLY for the NavRail active indicator

---

## 10. API Integration Map

All fetch URLs remain on `http://localhost:4132`. Zero backend changes needed.

| Feature | Endpoint | Method | View |
|---|---|---|---|
| Backend health + metrics | `/api/system-usage` | GET | StatusBar, Settings, Productivity Drawer |
| Chat stream (SSE) | `/api/chat/stream` | POST | Timeline |
| Clear chat | `/api/chat/clear` | POST | Timeline |
| Confirm safety gate | `/api/chat/confirm` | POST | Timeline |
| Apply heal patch | `/api/watcher/apply-heal` | POST | Timeline |
| RAG file ingest | `/api/rag/ingest-file` | POST (multipart) | Timeline |
| Scheduler run list | `/api/scheduler/runs` | GET | Jobs |
| Schedule new job | `/api/scheduler/win/create` | POST | Jobs |
| Clipboard history | `/api/clipboard/history` | GET | Clipboard |
| Analyze clipboard item | `/api/chat` | POST | Clipboard |
| Developer stats | `/api/developer/stats` | GET | Productivity |
| Pomodoro increment | `/api/profile/pomodoro/increment` | POST | Productivity |
| Swarm debate | `/api/lobby/debate` | POST | SwarmDebate |
| Ollama model list | `/api/ollama-models` | GET | Settings, SetupWizard |
| Save profile/settings | `/api/profile/save` | POST | Settings, SetupWizard |

---

## 11. What Changes vs What Stays

| Current File | Action |
|---|---|
| `src/App.tsx` (1597 lines) | **DELETE** → replaced by Shell + 6 view files |
| `src/FirstRunWizard.tsx` | **DELETE** → replaced by SetupWizard.tsx |
| `src/Mascot.tsx` | **KEEP logic, UPGRADE SVG art** |
| `src/main.tsx` | **MINIMAL EDIT** — add BootSequence + firstRun routing |
| `src/types.ts` | **KEEP + EXTEND** with new component prop types |
| `src/index.css` | **REWRITE COMPLETELY** |

---

## 12. Implementation Checklist

Build in this order — each phase is independently testable.

### Phase A — Foundation
- [ ] Rewrite `index.css` (all tokens, keyframes, utility classes)
- [ ] Create `components/ui/GlowCard.tsx`
- [ ] Create `components/ui/HoloButton.tsx`
- [ ] Create `components/ui/DataBadge.tsx`
- [ ] Create `components/ui/TerminalLine.tsx`
- [ ] Create `components/ui/ProgressArc.tsx`
- [ ] Create `AppContext.tsx` (global state provider)
- [ ] Create `NavRail.tsx` (static, all tabs wired, active state + layoutId working)
- [ ] Create `StatusBar.tsx` (hardcoded placeholders first, wire API later)
- [ ] Create `RightDrawer.tsx` (collapsible shell, content placeholder)
- [ ] Create `Shell.tsx` (full layout grid, wires NavRail + StatusBar + RightDrawer)
- [ ] Wire `AppContext` into Shell

### Phase B — Startup
- [ ] Create `startup/BootSequence.tsx`
  - [ ] Phase state machine (0–6)
  - [ ] Hex core SVG (orbiting rings, breathe, glow)
  - [ ] Logotype letter-stagger animation
  - [ ] Boot log lines with real API hits
  - [ ] Iris-wipe exit transition
  - [ ] Keypress skip handler
- [ ] Create `startup/SetupWizard.tsx`
  - [ ] Step indicator segmented bar
  - [ ] Step 1: Welcome (static)
  - [ ] Step 2: Integrations (accordion form)
  - [ ] Step 3: Provider card grid + inline API key / Ollama connection
  - [ ] Step 4: Completion celebration + Launch button
  - [ ] `saveSettings()` logic (same as existing code)
- [ ] Update `main.tsx`: cold boot → BootSequence → (firstRun ? SetupWizard : Shell)

### Phase C — Tab Views
- [ ] `views/Timeline.tsx` (messages, streaming, thoughts drawer, safety gate, heal diff, drag-drop)
- [ ] `views/Jobs.tsx` (schedule form + run log list)
- [ ] `views/Clipboard.tsx` (search + item list + analyze)
- [ ] `views/Productivity.tsx` (ProgressArc timer + stats grid + diagnostics)
- [ ] `views/SwarmDebate.tsx` (terminal log + debate form + agent legend drawer)
- [ ] `views/Settings.tsx` (config form + hardware arcs + theme radio)

### Phase D — Polish & Wiring
- [ ] Wire right drawer content per active tab
- [ ] Wire StatusBar to real `/api/system-usage`
- [ ] Add all micro-animations (card hover, tab switch, badge pulse, scan lines)
- [ ] Replace all `alert()` calls with inline UI feedback
- [ ] Test Tauri IPC: window controls, mascot toggle, game mode
- [ ] Upgrade Mascot SVG art style (hex head, antenna, chest core glow)
- [ ] Accessibility pass: focus rings, keyboard nav, `aria-label` on all icon buttons
- [ ] Verify all 6 themes apply correctly via CSS class on `<html>` element

---

## 13. Open Questions for You

> Answer these before starting Phase B:

1. **Boot sequence per-launch or first-launch only?**  
   Recommendation: every cold Tauri launch (max 6s, skippable after hex appears)

2. **Right drawer — default open or closed?**  
   Recommendation: open for Timeline (thoughts visible by default), closed for all other tabs

3. **Swarm Debate — SSE or JSON?**  
   Is `/api/lobby/debate` a regular POST returning JSON, or does it support Server-Sent Events streaming? SSE would allow real-time terminal line streaming.

4. **Mascot redesign depth?**  
   Full new character silhouette (hex head, new proportions) or style-only pass on existing SVG (better strokes, gradients, glow)?

5. **Theme switch mechanism?**  
   Current: class on `<body>`. Recommended: class on `<html>` element (or CSS custom properties on `:root` set via `document.documentElement.style.setProperty`). Which do you prefer?

---

*Spec written: 2026-06-29 · Meridian-X v0.1.0-alpha → v0.2.0 frontend redesign*
