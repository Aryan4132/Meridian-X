import React, { useEffect, useState, useRef } from 'react';
import { ShieldAlert, X } from 'lucide-react';
import { API_BASE_URL } from '../config';

interface HogProcess {
  pid: number;
  name: string;
  memory_mb: number;
  memory_gb: number;
  recommendation: string;
}

interface ProactiveBannerNudge {
  id: string;
  type: string;
  title: string;
  message: string;
  action_hint?: string;
  icon?: string;
  action?: string;
  patch?: {
    file_path: string;
    original: string;
    proposed: string;
    error_message: string;
  };
}

export default function ProactiveGuardBanner() {
  const [hogs, setHogs] = useState<HogProcess[]>([]);
  const [dismissedPids, setDismissedPids] = useState<number[]>([]);
  const [nudges, setNudges] = useState<ProactiveBannerNudge[]>([]);
  const lastNotifiedRef = useRef<Map<number, number>>(new Map());

  useEffect(() => {
    // Request browser / desktop notification permission if supported
    if (typeof window !== 'undefined' && 'Notification' in window && Notification.permission === 'default') {
      Notification.requestPermission().catch(() => {});
    }
  }, []);

  // Listen to live proactive events stream
  useEffect(() => {
    let eventSource: EventSource | null = null;
    try {
      eventSource = new EventSource(`${API_BASE_URL}/api/proactive/stream`);
      eventSource.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data && data.title) {
            setNudges((prev) => [data, ...prev.filter((n) => n.id !== data.id)].slice(0, 3));
            if (data.action === 'start_voice_command' || data.nudge_type === 'wakeword') {
              window.dispatchEvent(new CustomEvent('meridian:start-voice-chat'));
              if ((window as any).__TAURI_INTERNALS__) {
                import('@tauri-apps/api/event').then(({ emit }) => {
                  emit('global-push-to-talk', {}).catch(() => {});
                }).catch(() => {});
              }
            }
            if (data.mascot_state && typeof window !== 'undefined') {
              window.dispatchEvent(new CustomEvent('meridian:mascot-state-changed', {
                detail: { state: data.mascot_state, mascot_state: data.mascot_state }
              }));
              if ((window as any).__TAURI_INTERNALS__) {
                import('@tauri-apps/api/event').then(({ emit }) => {
                  emit('mascot-state-changed', { state: data.mascot_state, mascot_state: data.mascot_state }).catch(() => {});
                }).catch(() => {});
              }
            }
          }
        } catch {
          /* ignore parse errors */
        }
      };
    } catch {
      /* ignore connection errors */
    }

    return () => {
      if (eventSource) {
        eventSource.close();
      }
    };
  }, []);

  useEffect(() => {
    const checkHogs = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/guard/resources`);
        if (res.ok) {
          const data = await res.json();
          if (data.hogs && Array.isArray(data.hogs)) {
            setHogs(data.hogs);
            const now = Date.now();
            const COOLDOWN_MS = 300000; // 5-minute cooldown to prevent notification spam loop
            for (const hog of data.hogs) {
              const lastNotified = lastNotifiedRef.current.get(hog.pid) || 0;
              if (
                typeof window !== 'undefined' &&
                'Notification' in window &&
                Notification.permission === 'granted' &&
                !dismissedPids.includes(hog.pid) &&
                now - lastNotified >= COOLDOWN_MS
              ) {
                try {
                  new Notification('🛡️ Meridian-X Proactive System Guard', {
                    body: `Hey, ${hog.name} is eating ${hog.memory_gb}GB of RAM for no reason, should I kill it?`,
                    silent: false,
                  });
                  lastNotifiedRef.current.set(hog.pid, now);
                } catch { /* noop */ }
              }
            }
          }
        }
      } catch {
        // Suppress background poll errors
      }
    };

    checkHogs();
    const interval = setInterval(checkHogs, 15000);
    return () => clearInterval(interval);
  }, [dismissedPids]);

  const handleKill = async (pid: number) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/guard/kill-process`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ pid }),
      });
      if (res.ok) {
        setHogs(prev => prev.filter(h => h.pid !== pid));
      }
    } catch (e) {
      console.error('Failed to kill process:', e);
    }
  };

  const handleExecuteAction = (action?: string) => {
    if (!action) return;
    window.dispatchEvent(new CustomEvent('meridian:run-prompt', { detail: { prompt: action } }));
  };

  const activeHogs = hogs.filter(h => !dismissedPids.includes(h.pid));
  if (activeHogs.length === 0 && nudges.length === 0) return null;

  return (
    <div style={{
      position: 'absolute',
      top: 12,
      left: '50%',
      transform: 'translateX(-50%)',
      zIndex: 9999,
      display: 'flex',
      flexDirection: 'column',
      gap: '8px',
      maxWidth: '650px',
      width: '90%',
    }}>
      {activeHogs.map(hog => (
        <div key={hog.pid} className="glass-card" style={{
          background: 'color-mix(in srgb, var(--danger) 15%, transparent)',
          border: '1px solid var(--danger)',
          backdropFilter: 'blur(12px)',
          padding: '12px 16px',
          borderRadius: 'var(--radius-md)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          color: 'var(--text-bright)',
          boxShadow: '0 8px 32px rgba(255, 0, 50, 0.25)',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <ShieldAlert className="w-5 h-5 animate-pulse" style={{ color: 'var(--danger)' }} />
            <div style={{ fontSize: '13px' }}>
              <span style={{ fontWeight: 700, color: 'var(--danger)' }}>System Guard Alert: </span>
              Hey, <strong style={{ color: 'var(--accent)' }}>{hog.name}</strong> is eating <strong>{hog.memory_gb}GB RAM</strong>. Should I kill it?
            </div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <button
              onClick={() => handleKill(hog.pid)}
              style={{
                background: 'var(--danger)',
                border: 'none',
                color: '#FFF',
                padding: '6px 14px',
                borderRadius: 'var(--radius-sm)',
                fontSize: '12px',
                fontWeight: 600,
                cursor: 'pointer',
              }}
            >
              Kill Process (PID {hog.pid})
            </button>
            <button
              onClick={() => setDismissedPids(prev => [...prev, hog.pid])}
              style={{
                background: 'transparent',
                border: 'none',
                color: 'var(--text-dim)',
                cursor: 'pointer',
                padding: '4px',
              }}
            >
              <X size={16} />
            </button>
          </div>
        </div>
      ))}
      {nudges.map(nudge => (
        <div key={nudge.id} className="glass-card" style={{
          background: 'color-mix(in srgb, var(--accent) 15%, rgba(20,25,35,0.85))',
          border: '1px solid var(--accent)',
          backdropFilter: 'blur(16px)',
          padding: '12px 16px',
          borderRadius: 'var(--radius-md)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          color: 'var(--text-bright)',
          boxShadow: '0 8px 32px rgba(0, 180, 255, 0.2)',
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
            <span style={{ fontSize: '20px' }}>{nudge.icon || '💡'}</span>
            <div style={{ fontSize: '13px' }}>
              <span style={{ fontWeight: 700, color: 'var(--accent)' }}>{nudge.title}: </span>
              {nudge.message}
            </div>
          </div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            {nudge.action_hint && (
              <button
                onClick={() => handleExecuteAction(nudge.action || nudge.action_hint)}
                style={{
                  background: 'var(--accent)',
                  border: 'none',
                  color: '#000',
                  padding: '6px 14px',
                  borderRadius: 'var(--radius-sm)',
                  fontSize: '12px',
                  fontWeight: 700,
                  cursor: 'pointer',
                }}
              >
                {nudge.action_hint}
              </button>
            )}
            <button
              onClick={() => setNudges(prev => prev.filter(n => n.id !== nudge.id))}
              style={{
                background: 'transparent',
                border: 'none',
                color: 'var(--text-dim)',
                cursor: 'pointer',
                padding: '4px',
              }}
            >
              <X size={16} />
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}
