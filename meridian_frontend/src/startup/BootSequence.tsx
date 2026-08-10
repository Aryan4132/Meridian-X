import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { API_BASE_URL } from '../config';

interface BootSequenceProps {
  onComplete: () => void;
}

type BootPhase = 0 | 1 | 2 | 3 | 4 | 5;

interface BootLine {
  label: string;
  endpoint?: string;
  status: 'pending' | 'ok' | 'warn' | 'fail';
}

const BOOT_LINES: BootLine[] = [
  { label: 'Initializing ReAct inference engine', endpoint: `${API_BASE_URL}/api/health`, status: 'pending' },
  { label: 'Mounting SQLite + Turbovec vectors',  endpoint: `${API_BASE_URL}/api/health`, status: 'pending' },
  { label: 'Binding P2P swarm daemon',            status: 'pending' },
  { label: 'Checking Ollama inference endpoint',  endpoint: `${API_BASE_URL}/api/ollama-models`, status: 'pending' },
  { label: 'Loading Mascot companion core',       status: 'pending' },
];

const TITLE = 'MERIDIAN-X';
const SUBTITLE = 'v0.3.9  ·  agentic core';

function KineticHexCore({ phase, progress }: { phase: BootPhase; progress: number }) {
  const visible = phase >= 1;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, scale: 0.5, rotate: -45 }}
          animate={{ opacity: 1, scale: 1, rotate: 0 }}
          transition={{ duration: 1.0, ease: [0.16, 1, 0.3, 1] }}
          style={{ position: 'relative', width: 180, height: 180, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 28 }}
        >
          {/* Pulsing Outer Glow Halo */}
          <motion.div
            animate={{ scale: [1, 1.25, 1], opacity: [0.2, 0.45, 0.2] }}
            transition={{ duration: 3, repeat: Infinity, ease: "easeInOut" }}
            style={{
              position: 'absolute',
              width: 170,
              height: 170,
              borderRadius: '50%',
              background: 'radial-gradient(circle, var(--accent) 0%, transparent 70%)',
              filter: 'blur(20px)',
            }}
          />

          {/* Outer Rotating Dash Ring */}
          <motion.svg
            width="170" height="170"
            viewBox="0 0 170 170"
            animate={{ rotate: 360 }}
            transition={{ duration: 20, repeat: Infinity, ease: 'linear' }}
            style={{ position: 'absolute', transformOrigin: 'center' }}
          >
            <circle cx="85" cy="85" r="78" fill="none" stroke="var(--accent)" strokeWidth="1.5" strokeDasharray="8 12" strokeOpacity="0.5" />
            <circle cx="85" cy="7" r="4" fill="var(--accent)" />
            <circle cx="85" cy="163" r="3" fill="var(--accent-2)" />
          </motion.svg>

          {/* Middle Counter-Rotating Wave Ring */}
          <motion.svg
            width="136" height="136"
            viewBox="0 0 136 136"
            animate={{ rotate: -360 }}
            transition={{ duration: 14, repeat: Infinity, ease: 'linear' }}
            style={{ position: 'absolute', transformOrigin: 'center' }}
          >
            <circle cx="68" cy="68" r="60" fill="none" stroke="var(--accent-2)" strokeWidth="1" strokeDasharray="4 8" strokeOpacity="0.4" />
            <circle cx="68" cy="8" r="3" fill="var(--accent-2)" opacity="0.9" />
          </motion.svg>

          {/* Double Hexagon Core */}
          <motion.svg
            width="104" height="104"
            viewBox="0 0 104 104"
            animate={{ scale: [1, 1.04, 1] }}
            transition={{ duration: 3.5, repeat: Infinity, ease: 'easeInOut' }}
            style={{ position: 'absolute', filter: 'drop-shadow(0 0 16px var(--accent))' }}
          >
            {/* Outer Hex */}
            <polygon
              points="52,6 90,28 90,76 52,98 14,76 14,28"
              fill="color-mix(in srgb, var(--accent) 12%, transparent)"
              stroke="var(--accent)"
              strokeWidth="2"
            />
            {/* Inner Hex */}
            <polygon
              points="52,20 76,34 76,70 52,84 28,70 28,34"
              fill="color-mix(in srgb, var(--accent) 8%, transparent)"
              stroke="var(--accent-2)"
              strokeWidth="1.2"
              strokeOpacity="0.6"
            />
          </motion.svg>

          {/* Central Glowing Core Sphere */}
          <motion.div
            animate={{ scale: [1, 1.2, 1] }}
            transition={{ duration: 2, repeat: Infinity, ease: 'easeInOut' }}
            style={{
              position: 'absolute',
              width: 22, height: 22,
              borderRadius: '50%',
              background: 'var(--accent)',
              boxShadow: '0 0 24px var(--accent), 0 0 48px var(--accent-2)',
            }}
          />
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function KineticLogotype({ phase }: { phase: BootPhase }) {
  const visible = phase >= 1;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          style={{ textAlign: 'center', marginBottom: 12 }}
        >
          <div style={{ display: 'flex', gap: 2, justifyContent: 'center', overflow: 'hidden' }}>
            {TITLE.split('').map((ch, i) => (
              <motion.span
                key={i}
                initial={{ opacity: 0, y: 16, filter: 'blur(8px)', scale: 0.8 }}
                animate={{ opacity: 1, y: 0, filter: 'blur(0px)', scale: 1 }}
                transition={{ delay: 0.06 * i, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  fontSize: ch === '-' ? 30 : 34,
                  fontWeight: 700,
                  fontFamily: "'Inter', sans-serif",
                  color: ch === '-' ? 'var(--accent)' : 'var(--text-bright)',
                  letterSpacing: '0.18em',
                  lineHeight: 1,
                  textShadow: ch === '-' ? '0 0 12px var(--accent)' : 'none',
                }}
              >
                {ch === ' ' ? '\u00A0' : ch}
              </motion.span>
            ))}
          </div>
          <motion.p
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.4 }}
            style={{
              fontSize: 11,
              color: 'var(--text-dim)',
              fontFamily: "'JetBrains Mono', monospace",
              letterSpacing: '0.12em',
              marginTop: 6,
            }}
          >
            {SUBTITLE}
          </motion.p>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function BootLog({ lines, phase, progress }: { lines: BootLine[]; phase: BootPhase; progress: number }) {
  const visible = phase >= 2;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, y: 16, scale: 0.96 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
          style={{
            marginTop: 16,
            width: 440,
            background: 'var(--bg-panel)',
            border: '1px solid var(--border)',
            borderRadius: 'var(--radius-md)',
            padding: '14px 18px',
            boxShadow: '0 8px 32px rgba(0, 0, 0, 0.4)',
          }}
        >
          {/* Progress Bar Header */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
            <span style={{ fontSize: 10, fontWeight: 600, color: 'var(--text-ghost)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.1em' }}>
              System Initialization
            </span>
            <span style={{ fontSize: 11, fontWeight: 700, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace" }}>
              {Math.round(progress)}%
            </span>
          </div>

          {/* Track */}
          <div style={{ width: '100%', height: 4, background: 'var(--bg-surface)', borderRadius: 99, overflow: 'hidden', marginBottom: 14 }}>
            <motion.div
              style={{
                height: '100%',
                background: 'linear-gradient(90deg, var(--accent-dim), var(--accent), var(--accent-2))',
                borderRadius: 99,
                width: `${progress}%`,
                transition: 'width 0.2s cubic-bezier(0.16, 1, 0.3, 1)',
              }}
            />
          </div>

          {/* Lines */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
            {lines.map((line, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -10 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: i * 0.15, duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                }}
              >
                <span style={{ color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: 8 }}>
                  <span style={{ color: 'var(--accent)', fontSize: 9, fontWeight: 700 }}>[SYS]</span>
                  {line.label}...
                </span>
                <span style={{
                  color: line.status === 'ok' ? 'var(--success)'
                       : line.status === 'warn' ? 'var(--warning)'
                       : line.status === 'fail' ? 'var(--danger)'
                       : 'var(--text-dim)',
                  fontWeight: 600,
                  fontSize: 12,
                }}>
                  {line.status === 'ok' ? '✓' : line.status === 'warn' ? '⚠' : line.status === 'fail' ? '✕' : '…'}
                </span>
              </motion.div>
            ))}
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

export default function BootSequence({ onComplete }: BootSequenceProps) {
  const [phase, setPhase] = useState<BootPhase>(0);
  const [lines, setLines] = useState<BootLine[]>(BOOT_LINES.map(l => ({ ...l })));
  const [progress, setProgress] = useState(0);
  const [showOnline, setShowOnline] = useState(false);
  const [exiting, setExiting] = useState(false);
  const skipRef = useRef(false);

  const doExit = () => {
    if (skipRef.current) return;
    skipRef.current = true;
    setExiting(true);
    setTimeout(onComplete, 650);
  };

  // Phase & Progress progression
  useEffect(() => {
    const timers: ReturnType<typeof setTimeout>[] = [];
    timers.push(setTimeout(() => setPhase(1), 200));
    timers.push(setTimeout(() => {
      setPhase(2);
      setProgress(15);
    }, 600));
    timers.push(setTimeout(() => {
      setPhase(3);
      checkBootLines();
    }, 1200));

    return () => timers.forEach(clearTimeout);
  }, []);

  const checkBootLines = async () => {
    // 1. Poll the backend health endpoint until it is online
    let backendOnline = false;
    for (let retry = 0; retry < 40; retry++) {
      try {
        const res = await fetch(`${API_BASE_URL}/api/health`).catch(() => null);
        if (res && res.ok) {
          backendOnline = true;
          break;
        }
      } catch (e) {
        // Ignored
      }
      setProgress(prev => Math.min(prev + 1.5, 45));
      await new Promise(r => setTimeout(r, 180));
    }

    // 2. Proceed to run sequential checks for all boot lines
    for (let i = 0; i < BOOT_LINES.length; i++) {
      const line = BOOT_LINES[i];
      let status: BootLine['status'] = 'ok';
      if (line.endpoint) {
        try {
          const res = await fetch(line.endpoint).catch(() => null);
          status = res?.ok ? 'ok' : 'warn';
        } catch {
          status = 'warn';
        }
      }
      setLines(prev => prev.map((l, j) => j === i ? { ...l, status } : l));
      setProgress(prev => Math.min(prev + 12, 95));
      await new Promise(r => setTimeout(r, 200));
    }

    // 3. Complete progress bar & trigger online banner
    setProgress(100);
    setPhase(4);
    await new Promise(r => setTimeout(r, 350));
    setShowOnline(true);
    await new Promise(r => setTimeout(r, 700));
    doExit();
  };

  // Skip on keypress after phase 2
  useEffect(() => {
    const handler = () => {
      if (phase >= 2 && !skipRef.current) doExit();
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [phase]);

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'var(--bg-void)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        clipPath: exiting ? undefined : 'none',
        animation: exiting ? 'iris-open 0.65s cubic-bezier(0.4, 0, 1, 1) forwards' : 'none',
      }}
      onClick={() => phase >= 2 && doExit()}
    >
      {/* Background ambient grid tint */}
      <div className="void-bg" />

      {/* Center Layout Stack */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative', zIndex: 1 }}>
        <KineticHexCore phase={phase} progress={progress} />
        <KineticLogotype phase={phase} />
        <BootLog lines={lines} phase={phase} progress={progress} />

        {/* SYSTEM ONLINE Banner */}
        <AnimatePresence>
          {showOnline && (
            <motion.div
              initial={{ opacity: 0, scale: 0.85, y: 10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95 }}
              transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
              style={{
                marginTop: 20,
                fontSize: 12,
                fontWeight: 700,
                fontFamily: "'JetBrains Mono', monospace",
                color: 'var(--accent)',
                letterSpacing: '0.28em',
                textTransform: 'uppercase',
                background: 'var(--accent-muted)',
                padding: '6px 16px',
                borderRadius: 99,
                border: '1px solid var(--border-active)',
              }}
            >
              SYSTEM ONLINE
            </motion.div>
          )}
        </AnimatePresence>

        {/* Skip hint */}
        <AnimatePresence>
          {phase >= 2 && !showOnline && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 0.35 }}
              exit={{ opacity: 0 }}
              transition={{ delay: 0.4 }}
              style={{ marginTop: 24, fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.05em' }}
            >
              press any key to skip
            </motion.p>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
