import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';

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
  { label: 'Initializing ReAct inference engine', endpoint: 'http://localhost:4132/api/health', status: 'pending' },
  { label: 'Mounting SQLite + Turbovec vectors',  endpoint: 'http://localhost:4132/api/health', status: 'pending' },
  { label: 'Binding P2P swarm daemon',            status: 'pending' },
  { label: 'Checking Ollama inference endpoint',  endpoint: 'http://localhost:4132/api/ollama-models', status: 'pending' },
  { label: 'Loading Mascot companion core',       status: 'pending' },
];

const TITLE = 'MERIDIAN-X';
const SUBTITLE = 'v0.1.0-alpha  ·  agentic core';

function HexCore({ phase }: { phase: BootPhase }) {
  const visible = phase >= 2;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, scale: 0.6 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          style={{ position: 'relative', width: 160, height: 160, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 32 }}
        >
          {/* Outer ring - orbits clockwise */}
          <svg
            width="160" height="160"
            viewBox="0 0 160 160"
            style={{
              position: 'absolute',
              animation: 'orbit-cw 24s linear infinite',
              transformOrigin: 'center',
            }}
          >
            <circle cx="80" cy="80" r="72" fill="none" stroke="var(--accent)" strokeWidth="1" strokeDasharray="6 8" strokeOpacity="0.4" />
            {/* Small indicator dot */}
            <circle cx="80" cy="8" r="3" fill="var(--accent)" opacity="0.8" />
          </svg>

          {/* Middle ring - orbits counter-clockwise */}
          <svg
            width="130" height="130"
            viewBox="0 0 130 130"
            style={{
              position: 'absolute',
              animation: 'orbit-ccw 16s linear infinite',
              transformOrigin: 'center',
            }}
          >
            <circle cx="65" cy="65" r="58" fill="none" stroke="var(--accent-2)" strokeWidth="1" strokeDasharray="3 10" strokeOpacity="0.35" />
            <circle cx="65" cy="7" r="2.5" fill="var(--accent-2)" opacity="0.7" />
          </svg>

          {/* Hexagon body */}
          <svg
            width="96" height="96"
            viewBox="0 0 96 96"
            style={{ position: 'absolute', animation: 'breathe 4s ease-in-out infinite', filter: 'drop-shadow(0 0 12px var(--accent))' }}
          >
            <polygon
              points="48,6 82,25 82,71 48,90 14,71 14,25"
              fill="color-mix(in srgb, var(--accent) 8%, transparent)"
              stroke="var(--accent)"
              strokeWidth="1.5"
            />
            <polygon
              points="48,18 70,30 70,66 48,78 26,66 26,30"
              fill="color-mix(in srgb, var(--accent) 5%, transparent)"
              stroke="var(--accent)"
              strokeWidth="1"
              strokeOpacity="0.4"
            />
          </svg>

          {/* Core center */}
          <div style={{
            position: 'absolute',
            width: 20, height: 20,
            borderRadius: '50%',
            background: 'var(--accent)',
            boxShadow: '0 0 20px var(--accent), 0 0 40px color-mix(in srgb, var(--accent) 40%, transparent)',
            animation: 'pulse-glow-kf 2s ease-in-out infinite',
          }} />
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function Logotype({ phase }: { phase: BootPhase }) {
  const visible = phase >= 1;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          style={{ textAlign: 'center', marginBottom: 8 }}
        >
          <div style={{ display: 'flex', gap: 0, justifyContent: 'center', overflow: 'hidden' }}>
            {TITLE.split('').map((ch, i) => (
              <motion.span
                key={i}
                initial={{ opacity: 0, y: 8, filter: 'blur(4px)' }}
                animate={{ opacity: 1, y: 0, filter: 'blur(0px)' }}
                transition={{ delay: 0.05 * i, duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  fontSize: ch === '-' ? 28 : 32,
                  fontWeight: 700,
                  fontFamily: "'Space Grotesk', sans-serif",
                  color: ch === '-' ? 'var(--accent)' : 'var(--text-bright)',
                  letterSpacing: '0.15em',
                  lineHeight: 1,
                }}
              >
                {ch === ' ' ? '\u00A0' : ch}
              </motion.span>
            ))}
          </div>
          <motion.p
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.7 }}
            style={{
              fontSize: 11,
              color: 'var(--text-dim)',
              fontFamily: "'JetBrains Mono', monospace",
              letterSpacing: '0.1em',
              marginTop: 4,
            }}
          >
            {SUBTITLE}
          </motion.p>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

function BootLog({ lines, phase }: { lines: BootLine[]; phase: BootPhase }) {
  const visible = phase >= 3;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
          style={{
            marginTop: 24,
            width: 420,
            background: 'rgba(0,0,0,0.3)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-md)',
            padding: '12px 16px',
          }}
        >
          <div style={{ height: 1, background: 'var(--border-subtle)', marginBottom: 12 }} />
          {lines.map((line, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, x: -12 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.25, duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
              style={{
                display: 'flex',
                justifyContent: 'space-between',
                alignItems: 'center',
                padding: '3px 0',
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: 11,
              }}
            >
              <span style={{ color: 'var(--text-dim)' }}>
                <span style={{ color: 'var(--accent-dim)', marginRight: 8 }}>[SYS]</span>
                {line.label}...
              </span>
              <span style={{
                color: line.status === 'ok' ? 'var(--success)'
                     : line.status === 'warn' ? 'var(--warning)'
                     : line.status === 'fail' ? 'var(--danger)'
                     : 'var(--text-dim)',
                marginLeft: 12,
              }}>
                {line.status === 'ok' ? '✓' : line.status === 'warn' ? '⚠' : line.status === 'fail' ? '✕' : '…'}
              </span>
            </motion.div>
          ))}
          <div style={{ height: 1, background: 'var(--border-subtle)', marginTop: 12 }} />
        </motion.div>
      )}
    </AnimatePresence>
  );
}

export default function BootSequence({ onComplete }: BootSequenceProps) {
  const [phase, setPhase] = useState<BootPhase>(0);
  const [lines, setLines] = useState<BootLine[]>(BOOT_LINES.map(l => ({ ...l })));
  const [showOnline, setShowOnline] = useState(false);
  const [exiting, setExiting] = useState(false);
  const skipRef = useRef(false);

  const doExit = () => {
    if (skipRef.current) return;
    skipRef.current = true;
    setExiting(true);
    setTimeout(onComplete, 680);
  };

  // Phase progression
  useEffect(() => {
    const timers: ReturnType<typeof setTimeout>[] = [];
    timers.push(setTimeout(() => setPhase(1), 300));
    timers.push(setTimeout(() => setPhase(2), 1000));
    timers.push(setTimeout(() => {
      setPhase(3);
      // Run API checks
      checkBootLines();
    }, 2000));

    return () => timers.forEach(clearTimeout);
  }, []);

  const checkBootLines = async () => {
    // 1. Poll the backend health endpoint until it is online
    let backendOnline = false;
    for (let retry = 0; retry < 60; retry++) {
      try {
        const res = await fetch('http://localhost:4132/api/health').catch(() => null);
        if (res && res.ok) {
          backendOnline = true;
          break;
        }
      } catch (e) {
        // Ignored
      }
      await new Promise(r => setTimeout(r, 250));
    }

    // 2. Proceed to run sequential checks for all boot lines with a nice visual delay
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
      await new Promise(r => setTimeout(r, 250));
    }

    // 3. Trigger final exit sequence
    setPhase(4);
    await new Promise(r => setTimeout(r, 600));
    setShowOnline(true);
    await new Promise(r => setTimeout(r, 800));
    doExit();
  };

  // Skip on keypress after phase 2
  useEffect(() => {
    const handler = (e: KeyboardEvent) => {
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
        animation: exiting ? 'iris-open 0.65s cubic-bezier(0.4,0,1,1) forwards' : 'none',
      }}
      onClick={() => phase >= 2 && doExit()}
    >
      <div className="void-bg" />

      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative', zIndex: 1 }}>
        <HexCore phase={phase} />
        <Logotype phase={phase} />
        <BootLog lines={lines} phase={phase} />

        {/* SYSTEM ONLINE text */}
        <AnimatePresence>
          {showOnline && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: [0, 1, 1, 0], scale: 1 }}
              transition={{ duration: 0.8, times: [0, 0.2, 0.7, 1] }}
              style={{
                marginTop: 24,
                fontSize: 13,
                fontWeight: 700,
                fontFamily: "'JetBrains Mono', monospace",
                color: 'var(--accent)',
                letterSpacing: '0.3em',
                textTransform: 'uppercase',
                textShadow: '0 0 20px var(--accent)',
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
              animate={{ opacity: 0.4 }}
              exit={{ opacity: 0 }}
              transition={{ delay: 0.5 }}
              style={{ marginTop: 32, fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}
            >
              press any key to skip
            </motion.p>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
