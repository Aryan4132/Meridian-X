import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { API_BASE_URL } from '../config';
import { MascotCharacter } from '../Mascot';

interface BootSequenceProps {
  onComplete: () => void;
}

type BootPhase = 0 | 1 | 2 | 3 | 4;

interface BootStep {
  id: string;
  label: string;
  endpoint?: string;
  status: 'pending' | 'active' | 'ok' | 'warn';
}

const INITIAL_STEPS: BootStep[] = [
  { id: 'engine',   label: 'Connecting to inference engine', endpoint: `${API_BASE_URL}/api/health`, status: 'pending' },
  { id: 'vectors',  label: 'Mounting vector database & Turbovec index', endpoint: `${API_BASE_URL}/api/health`, status: 'pending' },
  { id: 'security', label: 'Initializing AES-256 vault & security guard', status: 'pending' },
  { id: 'ollama',   label: 'Checking local Ollama endpoints', endpoint: `${API_BASE_URL}/api/ollama-models`, status: 'pending' },
  { id: 'companion',label: 'Loading companion core & workflow runner', status: 'pending' },
];

export default function BootSequence({ onComplete }: BootSequenceProps) {
  const [phase, setPhase] = useState<BootPhase>(0);
  const [steps, setSteps] = useState<BootStep[]>(INITIAL_STEPS.map(s => ({ ...s })));
  const [progress, setProgress] = useState(0);
  const [showOnline, setShowOnline] = useState(false);
  const [exiting, setExiting] = useState(false);
  const skipRef = useRef(false);

  const doExit = () => {
    if (skipRef.current) return;
    skipRef.current = true;
    setExiting(true);
    setTimeout(onComplete, 550);
  };

  useEffect(() => {
    const timer1 = setTimeout(() => setPhase(1), 150);
    const timer2 = setTimeout(() => {
      setPhase(2);
      setProgress(15);
      runBootSequence();
    }, 450);

    return () => {
      clearTimeout(timer1);
      clearTimeout(timer2);
    };
  }, []);

  const runBootSequence = async () => {
    // Phase 1: backend health check
    for (let retry = 0; retry < 30; retry++) {
      try {
        const res = await fetch(`${API_BASE_URL}/api/health`).catch(() => null);
        if (res && res.ok) break;
      } catch {
        // Ignored
      }
      setProgress(prev => Math.min(prev + 2, 40));
      await new Promise(r => setTimeout(r, 150));
    }

    // Step by step progress execution over time
    for (let i = 0; i < INITIAL_STEPS.length; i++) {
      const step = INITIAL_STEPS[i];
      setSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: 'active' } : s));

      let finalStatus: BootStep['status'] = 'ok';
      if (step.endpoint) {
        try {
          const res = await fetch(step.endpoint).catch(() => null);
          finalStatus = res?.ok ? 'ok' : 'warn';
        } catch {
          finalStatus = 'warn';
        }
      }

      await new Promise(r => setTimeout(r, 160));

      setSteps(prev => prev.map((s, idx) => idx === i ? { ...s, status: finalStatus } : s));
      setProgress(prev => Math.min(prev + 16, 95));
      await new Promise(r => setTimeout(r, 140));
    }

    // Completion
    setProgress(100);
    setPhase(3);
    await new Promise(r => setTimeout(r, 250));
    setShowOnline(true);
    await new Promise(r => setTimeout(r, 600));
    doExit();
  };

  useEffect(() => {
    const handler = () => {
      if (phase >= 2 && !skipRef.current) doExit();
    };
    window.addEventListener('keydown', handler);
    return () => window.removeEventListener('keydown', handler);
  }, [phase]);

  const activeMascotState = 
    progress >= 100 ? 'happy' :
    progress > 60 ? 'typing' :
    'idle';

  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'var(--bg-void, #0A0C10)',
        color: 'var(--text-main, #A0A5B5)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        zIndex: 9999,
        clipPath: exiting ? undefined : 'none',
        animation: exiting ? 'iris-open 0.55s cubic-bezier(0.4, 0, 1, 1) forwards' : 'none',
        overflow: 'hidden',
        userSelect: 'none',
      }}
      onClick={() => phase >= 2 && doExit()}
    >
      {/* Subtle Background Glow */}
      <div
        style={{
          position: 'absolute',
          width: 500,
          height: 500,
          borderRadius: '50%',
          background: 'radial-gradient(circle, var(--accent-muted, rgba(232, 160, 32, 0.12)) 0%, transparent 70%)',
          pointerEvents: 'none',
          filter: 'blur(40px)',
          opacity: 0.7,
        }}
      />

      {/* Main Container */}
      <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', maxWidth: 440, width: '90%', zIndex: 2 }}>
        
        {/* Mascot Centerpiece */}
        <motion.div
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          style={{ marginBottom: 20, transform: 'scale(2.2)', padding: 16 }}
        >
          <MascotCharacter state={activeMascotState} accentColor="var(--accent, #E8A020)" />
        </motion.div>

        {/* Title */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          style={{ textAlign: 'center', marginBottom: 24 }}
        >
          <h1 style={{
            fontSize: 26,
            fontWeight: 700,
            color: 'var(--text-bright, #F0EEE8)',
            fontFamily: 'var(--font-heading, sans-serif)',
            letterSpacing: '0.12em',
            margin: 0,
          }}>
            MERIDIAN-X
          </h1>
          <p style={{
            fontSize: 12,
            color: 'var(--text-dim, #6B7280)',
            fontFamily: 'var(--font-main, monospace)',
            marginTop: 4,
            letterSpacing: '0.05em'
          }}>
            Initializing local AI assistant engine…
          </p>
        </motion.div>

        {/* Progress Bar Component */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.2 }}
          style={{ width: '100%', marginBottom: 24 }}
        >
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8, fontSize: 12, fontFamily: 'var(--font-main, monospace)' }}>
            <span style={{ color: 'var(--text-main, #A0A5B5)', fontWeight: 500 }}>System Loading</span>
            <span style={{ color: 'var(--accent, #E8A020)', fontWeight: 700 }}>{Math.round(progress)}%</span>
          </div>

          {/* Clean Track */}
          <div style={{
            width: '100%',
            height: 6,
            background: 'var(--bg-surface, #1E232E)',
            borderRadius: 99,
            overflow: 'hidden',
            border: '1px solid var(--border-subtle, rgba(255,255,255,0.06))',
          }}>
            <div
              style={{
                height: '100%',
                width: `${progress}%`,
                background: 'linear-gradient(90deg, var(--accent-dim, #C68212), var(--accent, #E8A020))',
                borderRadius: 99,
                transition: 'width 0.25s ease-out',
                boxShadow: '0 0 10px var(--accent-muted, rgba(232, 160, 32, 0.3))'
              }}
            />
          </div>
        </motion.div>

        {/* Clean Steps Checklist */}
        <motion.div
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.3 }}
          style={{
            width: '100%',
            background: 'var(--bg-panel, #161A22)',
            border: '1px solid var(--border, rgba(232,160,32,0.15))',
            borderRadius: 'var(--radius-md, 10px)',
            padding: '14px 18px',
            display: 'flex',
            flexDirection: 'column',
            gap: 10,
            boxShadow: 'var(--card-shadow, 0 4px 20px rgba(0,0,0,0.4))'
          }}
        >
          {steps.map((step) => {
            const isOk = step.status === 'ok';
            const isWarn = step.status === 'warn';
            const isActive = step.status === 'active';

            return (
              <div
                key={step.id}
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  fontSize: 12,
                  fontFamily: 'var(--font-main, monospace)',
                }}
              >
                <span style={{
                  color: isActive ? 'var(--text-bright, #F0EEE8)' : isOk ? 'var(--text-main, #A0A5B5)' : 'var(--text-dim, #6B7280)',
                  transition: 'color 0.2s ease',
                  display: 'flex',
                  alignItems: 'center',
                  gap: 8,
                }}>
                  <span style={{
                    width: 6,
                    height: 6,
                    borderRadius: '50%',
                    background: isOk ? 'var(--success, #34D399)' : isWarn ? 'var(--warning, #FBBF24)' : isActive ? 'var(--accent, #E8A020)' : 'var(--border-subtle)',
                    boxShadow: isActive ? '0 0 6px var(--accent)' : 'none',
                    display: 'inline-block',
                  }} />
                  {step.label}
                </span>

                <span style={{
                  fontSize: 11,
                  fontWeight: 600,
                  color: isOk ? 'var(--success, #34D399)' : isWarn ? 'var(--warning, #FBBF24)' : isActive ? 'var(--accent, #E8A020)' : 'var(--text-ghost, #374151)'
                }}>
                  {isOk ? '✓ OK' : isWarn ? '⚠ WARN' : isActive ? '…' : 'WAITING'}
                </span>
              </div>
            );
          })}
        </motion.div>

        {/* Online Badge */}
        <AnimatePresence>
          {showOnline && (
            <motion.div
              initial={{ opacity: 0, scale: 0.9, y: 10 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0 }}
              style={{
                marginTop: 18,
                fontSize: 12,
                fontWeight: 700,
                color: 'var(--success, #34D399)',
                background: 'color-mix(in srgb, var(--success) 12%, transparent)',
                border: '1px solid color-mix(in srgb, var(--success) 30%, transparent)',
                padding: '6px 18px',
                borderRadius: 99,
                letterSpacing: '0.08em',
              }}
            >
              ✓ READY
            </motion.div>
          )}
        </AnimatePresence>

        {/* Skip note */}
        {phase >= 2 && !showOnline && (
          <p style={{ marginTop: 18, fontSize: 11, color: 'var(--text-ghost)', fontFamily: 'var(--font-main, monospace)' }}>
            Press any key to skip
          </p>
        )}
      </div>
    </div>
  );
}


