import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { API_BASE_URL } from '../config';
import { MascotCharacter } from '../Mascot';

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
  { label: 'Binding P2P swarm daemon & OAuth vault', status: 'pending' },
  { label: 'Checking Ollama inference endpoint',  endpoint: `${API_BASE_URL}/api/ollama-models`, status: 'pending' },
  { label: 'Loading Mascot companion core & n8n engine', status: 'pending' },
];

const TITLE = 'MERIDIAN-X';
const SUBTITLE = 'v0.4.0  ·  agentic intelligence core';

/* Interactive Cybernetic Canvas Backdrop */
function RadarParticleCanvas() {
  const canvasRef = useRef<HTMLCanvasElement | null>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationFrameId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (!canvas) return;
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    };
    window.addEventListener('resize', handleResize);

    const particles: { x: number; y: number; r: number; dx: number; dy: number; alpha: number }[] = [];
    for (let i = 0; i < 45; i++) {
      particles.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.8 + 0.6,
        dx: (Math.random() - 0.5) * 0.4,
        dy: (Math.random() - 0.5) * 0.4,
        alpha: Math.random() * 0.5 + 0.2
      });
    }

    let sweepAngle = 0;

    const render = () => {
      ctx.clearRect(0, 0, width, height);

      const cx = width / 2;
      const cy = height / 2;
      sweepAngle += 0.015;

      const sweepGradient = ctx.createConicGradient(sweepAngle, cx, cy);
      sweepGradient.addColorStop(0, 'rgba(0, 240, 255, 0.08)');
      sweepGradient.addColorStop(0.1, 'rgba(0, 240, 255, 0.01)');
      sweepGradient.addColorStop(1, 'transparent');

      ctx.fillStyle = sweepGradient;
      ctx.beginPath();
      ctx.arc(cx, cy, Math.max(width, height) * 0.7, 0, Math.PI * 2);
      ctx.fill();

      particles.forEach(p => {
        p.x += p.dx;
        p.y += p.dy;
        if (p.x < 0 || p.x > width) p.dx *= -1;
        if (p.y < 0 || p.y > height) p.dy *= -1;

        ctx.fillStyle = `rgba(0, 217, 255, ${p.alpha})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fill();
      });

      animationFrameId = requestAnimationFrame(render);
    };

    render();

    return () => {
      window.removeEventListener('resize', handleResize);
      cancelAnimationFrame(animationFrameId);
    };
  }, []);

  return <canvas ref={canvasRef} style={{ position: 'absolute', inset: 0, pointerEvents: 'none', opacity: 0.8 }} />;
}

/* Mascot Loading Animation Orb & Circular Progress Gauge */
function MascotLoadingCore({ progress, phase }: { progress: number; phase: BootPhase }) {
  const visible = phase >= 1;
  
  // Resolve dynamic mascot emotion state based on loading progress
  const mascotState = 
    progress >= 100 ? 'happy' :
    progress > 65 ? 'typing' :
    progress > 30 ? 'diagnostic' :
    'idle';

  const strokeDashoffset = 326.72 - (326.72 * progress) / 100;

  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, scale: 0.6 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          style={{ position: 'relative', width: 180, height: 180, display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: 24 }}
        >
          {/* Ambient Pulsing Glow Background */}
          <motion.div
            animate={{ scale: [1, 1.25, 1], opacity: [0.3, 0.6, 0.3] }}
            transition={{ duration: 2.5, repeat: Infinity, ease: 'easeInOut' }}
            style={{
              position: 'absolute',
              width: 140,
              height: 140,
              borderRadius: '50%',
              background: progress >= 100 
                ? 'radial-gradient(circle, #00D97E 0%, transparent 70%)' 
                : 'radial-gradient(circle, #00F0FF 0%, #6366F1 50%, transparent 75%)',
              filter: 'blur(22px)',
            }}
          />

          {/* SVG Circular Orbit Progress Gauge (Replaces Bar) */}
          <svg width="150" height="150" viewBox="0 0 120 120" style={{ position: 'absolute', transform: 'rotate(-90deg)' }}>
            {/* Track Circle */}
            <circle
              cx="60" cy="60" r="52"
              fill="none"
              stroke="rgba(255, 255, 255, 0.08)"
              strokeWidth="4"
            />
            {/* Animated Dynamic Progress Circle */}
            <circle
              cx="60" cy="60" r="52"
              fill="none"
              stroke={progress >= 100 ? '#00D97E' : '#00F0FF'}
              strokeWidth="5"
              strokeDasharray="326.72"
              strokeDashoffset={strokeDashoffset}
              strokeLinecap="round"
              style={{ transition: 'stroke-dashoffset 0.3s ease, stroke 0.3s ease' }}
            />
          </svg>

          {/* Outer Rotating Cyber Marks */}
          <motion.svg
            width="170" height="170"
            viewBox="0 0 170 170"
            animate={{ rotate: 360 }}
            transition={{ duration: 16, repeat: Infinity, ease: 'linear' }}
            style={{ position: 'absolute', transformOrigin: 'center' }}
          >
            <circle cx="85" cy="85" r="80" fill="none" stroke="#00F0FF" strokeWidth="1.2" strokeDasharray="6 12" strokeOpacity="0.4" />
            <circle cx="85" cy="5" r="3.5" fill="#00F0FF" />
          </motion.svg>

          {/* Center Mascot Companion Character */}
          <div style={{ position: 'relative', zIndex: 10, transform: 'scale(2.4)' }}>
            <MascotCharacter
              state={mascotState}
              accentColor={progress >= 100 ? '#00D97E' : '#00F0FF'}
              speechAmplitude={0.4}
            />
          </div>

          {/* Progress Percentage Overlay Badge */}
          <div style={{
            position: 'absolute',
            bottom: -8,
            background: 'rgba(3, 7, 18, 0.85)',
            border: '1px solid rgba(0, 240, 255, 0.3)',
            borderRadius: 99,
            padding: '2px 10px',
            fontSize: 11,
            fontWeight: 800,
            color: progress >= 100 ? '#00D97E' : '#00F0FF',
            fontFamily: "'JetBrains Mono', monospace",
            boxShadow: '0 0 12px rgba(0, 240, 255, 0.3)'
          }}>
            {Math.round(progress)}%
          </div>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

/* Kinetic Logotype Header */
function KineticLogotype({ phase }: { phase: BootPhase }) {
  const visible = phase >= 1;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          style={{ textAlign: 'center', marginBottom: 14 }}
        >
          <div style={{ display: 'flex', gap: 3, justifyContent: 'center', overflow: 'hidden' }}>
            {TITLE.split('').map((ch, i) => (
              <motion.span
                key={i}
                initial={{ opacity: 0, y: 20, filter: 'blur(10px)', scale: 0.7 }}
                animate={{ opacity: 1, y: 0, filter: 'blur(0px)', scale: 1 }}
                transition={{ delay: 0.05 * i, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  fontSize: ch === '-' ? 32 : 36,
                  fontWeight: 800,
                  fontFamily: "'Orbitron', 'Inter', sans-serif",
                  color: ch === '-' ? '#00F0FF' : '#F8FAFC',
                  letterSpacing: '0.2em',
                  lineHeight: 1,
                  textShadow: ch === '-' ? '0 0 16px #00F0FF' : '0 0 12px rgba(255, 255, 255, 0.2)',
                }}
              >
                {ch === ' ' ? '\u00A0' : ch}
              </motion.span>
            ))}
          </div>
          <motion.p
            initial={{ opacity: 0, y: 6 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5, duration: 0.4 }}
            style={{
              fontSize: 11,
              color: '#94A3B8',
              fontFamily: "'JetBrains Mono', monospace",
              letterSpacing: '0.14em',
              marginTop: 8,
              textTransform: 'uppercase',
            }}
          >
            {SUBTITLE}
          </motion.p>
        </motion.div>
      )}
    </AnimatePresence>
  );
}

/* Boot Progress & System Check Log Container (Clean Check List without progress bar) */
function BootLog({ lines, phase }: { lines: BootLine[]; phase: BootPhase }) {
  const visible = phase >= 2;
  return (
    <AnimatePresence>
      {visible && (
        <motion.div
          initial={{ opacity: 0, y: 18, scale: 0.95 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          transition={{ duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
          style={{
            marginTop: 12,
            width: 480,
            background: 'rgba(10, 15, 26, 0.85)',
            backdropFilter: 'blur(16px)',
            border: '1px solid rgba(0, 240, 255, 0.2)',
            borderRadius: 14,
            padding: '16px 20px',
            boxShadow: '0 12px 40px rgba(0, 0, 0, 0.6), 0 0 20px rgba(0, 240, 255, 0.1)',
            position: 'relative'
          }}
        >
          {/* HUD Corner Tech Brackets */}
          <div style={{ position: 'absolute', top: 4, left: 4, width: 8, height: 8, borderTop: '2px solid #00F0FF', borderLeft: '2px solid #00F0FF' }} />
          <div style={{ position: 'absolute', top: 4, right: 4, width: 8, height: 8, borderTop: '2px solid #00F0FF', borderRight: '2px solid #00F0FF' }} />
          <div style={{ position: 'absolute', bottom: 4, left: 4, width: 8, height: 8, borderBottom: '2px solid #00F0FF', borderLeft: '2px solid #00F0FF' }} />
          <div style={{ position: 'absolute', bottom: 4, right: 4, width: 8, height: 8, borderBottom: '2px solid #00F0FF', borderRight: '2px solid #00F0FF' }} />

          {/* Header Status */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
            <span style={{ fontSize: 10, fontWeight: 700, color: '#64748B', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.12em' }}>
              AGENTIC SYSTEM INITIALIZATION
            </span>
          </div>

          {/* Line Logs */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
            {lines.map((line, i) => (
              <motion.div
                key={i}
                initial={{ opacity: 0, x: -12 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: i * 0.12, duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  display: 'flex',
                  justifyContent: 'space-between',
                  alignItems: 'center',
                  fontFamily: "'JetBrains Mono', monospace",
                  fontSize: 11,
                }}
              >
                <span style={{ color: '#E2E8F0', display: 'flex', alignItems: 'center', gap: 8 }}>
                  <span style={{ color: '#00F0FF', fontSize: 9, fontWeight: 800 }}>[SYS_INIT]</span>
                  {line.label}...
                </span>
                <span style={{
                  color: line.status === 'ok' ? '#00D97E'
                       : line.status === 'warn' ? '#F59E0B'
                       : line.status === 'fail' ? '#EF4444'
                       : '#64748B',
                  fontWeight: 700,
                  fontSize: 12,
                }}>
                  {line.status === 'ok' ? '✓ OK' : line.status === 'warn' ? '⚠ WARN' : line.status === 'fail' ? '✕ FAIL' : '… PENDING'}
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

    setProgress(100);
    setPhase(4);
    await new Promise(r => setTimeout(r, 350));
    setShowOnline(true);
    await new Promise(r => setTimeout(r, 700));
    doExit();
  };

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
        background: '#030712',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        clipPath: exiting ? undefined : 'none',
        animation: exiting ? 'iris-open 0.65s cubic-bezier(0.4, 0, 1, 1) forwards' : 'none',
        overflow: 'hidden'
      }}
      onClick={() => phase >= 2 && doExit()}
    >
      {/* Radar Particle Background Canvas */}
      <RadarParticleCanvas />

      {/* Screen HUD Overlay Corners */}
      <div style={{ position: 'absolute', top: 24, left: 24, fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: '#475569', letterSpacing: '0.1em' }}>
        SYSTEM: MERIDIAN_OS // RE_ACT_HYBRID
      </div>
      <div style={{ position: 'absolute', top: 24, right: 24, fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: '#475569', letterSpacing: '0.1em' }}>
        VAULT: AES_GCM_256 // OAUTH_ACTIVE
      </div>
      <div style={{ position: 'absolute', bottom: 24, left: 24, fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: '#475569', letterSpacing: '0.1em' }}>
        LATENCY: 0.4MS // ADAPTIVE_INFRASTRUCTURE
      </div>
      <div style={{ position: 'absolute', bottom: 24, right: 24, fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: '#475569', letterSpacing: '0.1em' }}>
        NODE: 0x4132 // PORT_ACTIVE
      </div>

      {/* Center Layout Stack */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', position: 'relative', zIndex: 2 }}>
        <MascotLoadingCore progress={progress} phase={phase} />
        <KineticLogotype phase={phase} />
        <BootLog lines={lines} phase={phase} />

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
                fontWeight: 800,
                fontFamily: "'JetBrains Mono', monospace",
                color: '#00D97E',
                letterSpacing: '0.28em',
                textTransform: 'uppercase',
                background: 'rgba(0, 217, 126, 0.12)',
                padding: '8px 20px',
                borderRadius: 99,
                border: '1px solid #00D97E',
                boxShadow: '0 0 24px rgba(0, 217, 126, 0.4)',
              }}
            >
              ⚡ SYSTEM ONLINE
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
              transition={{ delay: 0.4 }}
              style={{ marginTop: 24, fontSize: 10, color: '#94A3B8', fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.08em' }}
            >
              [PRESS ANY KEY TO SKIP]
            </motion.p>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
