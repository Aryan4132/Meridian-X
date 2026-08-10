import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'motion/react';
import { Play, Pause, RefreshCw } from 'lucide-react';
import { DeveloperStats } from '../types';
import ProgressArc from '../components/ui/ProgressArc';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';
import { API_BASE_URL } from '../config';

const POMODORO_SECS = 25 * 60;

function StatCard({ label, value, sub, color }: { label: string; value: string | number; sub: string; color: string }) {
  return (
    <div
      className="glass glass-hover"
      style={{ padding: '14px 16px', textAlign: 'center', position: 'relative', overflow: 'hidden' }}
    >
      <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: 1, background: color, opacity: 0.6 }} />
      <div style={{ fontSize: 26, fontWeight: 700, color, fontFamily: "'Space Grotesk', sans-serif", lineHeight: 1 }}>{value}</div>
      <div style={{ fontSize: 10, fontWeight: 600, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.08em', marginTop: 4 }}>{label}</div>
      <div style={{ fontSize: 10, color: 'var(--text-ghost)', marginTop: 2 }}>{sub}</div>
    </div>
  );
}

const PRESET_DISTRACTIONS = [
  { id: 'youtube', label: 'YouTube', target: 'youtube.com' },
  { id: 'reddit', label: 'Reddit', target: 'reddit.com' },
  { id: 'twitter', label: 'Twitter / X', target: 'x.com' },
  { id: 'twitch', label: 'Twitch', target: 'twitch.tv' },
  { id: 'discord', label: 'Discord App', target: 'discord.exe' },
  { id: 'steam', label: 'Steam', target: 'steam.exe' },
];

export default function Productivity() {
  const [stats, setStats] = useState<DeveloperStats>({ total: 0, success: 0, failed: 0, audits: 0, heals: 0, gitCommits: 0, pomodoros: 0 });
  const [durationMins, setDurationMins] = useState(25);
  const [secsLeft, setSecsLeft] = useState(25 * 60);
  const [active, setActive] = useState(false);
  const intervalRef = useRef<any>(null);

  const [blockedTargets, setBlockedTargets] = useState<string[]>(() => {
    const saved = localStorage.getItem('distraction_targets');
    return saved ? JSON.parse(saved) : ['youtube.com', 'reddit.com', 'x.com'];
  });
  const [customTarget, setCustomTarget] = useState('');

  const toggleTarget = (target: string) => {
    const next = blockedTargets.includes(target)
      ? blockedTargets.filter(t => t !== target)
      : [...blockedTargets, target];
    setBlockedTargets(next);
    localStorage.setItem('distraction_targets', JSON.stringify(next));
  };

  const addCustomTarget = () => {
    const clean = customTarget.trim().toLowerCase();
    if (!clean || blockedTargets.includes(clean)) return;
    const next = [...blockedTargets, clean];
    setBlockedTargets(next);
    localStorage.setItem('distraction_targets', JSON.stringify(next));
    setCustomTarget('');
  };

  const fetchStats = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/developer/stats`).catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        // Safe-merge with defaults so partial responses never produce NaN in UI
        setStats(prev => ({
          ...prev,
          total:      data.total_tasks      ?? prev.total,
          success:    data.success_tasks    ?? prev.success,
          failed:     data.failed_tasks     ?? prev.failed,
          audits:     data.security_audits  ?? prev.audits,
          heals:      data.successful_heals ?? prev.heals,
          gitCommits: data.git_commits      ?? prev.gitCommits,
          pomodoros:  data.pomodoros        ?? prev.pomodoros,
        }));
      }
    } catch { /* noop */ }
  };

  const syncPomodoro = async () => {
    try {
      const res = await fetch('http://localhost:4132/api/pomodoro/status').catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        setActive(data.active);
        if (data.active) {
          const limit = data.state === "work" ? data.work_duration : data.break_duration;
          setSecsLeft(Math.max(0, limit - data.elapsed));
        }
      }
    } catch { /* noop */ }
  };

  useEffect(() => {
    fetchStats();
    syncPomodoro();
    const pollId = setInterval(syncPomodoro, 3000);
    return () => clearInterval(pollId);
  }, [durationMins]);

  useEffect(() => {
    if (active && secsLeft > 0) {
      intervalRef.current = setInterval(() => setSecsLeft(s => s - 1), 1000);
    } else if (secsLeft === 0 && active) {
      setActive(false);
      setSecsLeft(durationMins * 60);
      fetch('http://localhost:4132/api/profile/pomodoro/increment', { method: 'POST' }).then(() => fetchStats()).catch(() => {});
    }
    return () => clearInterval(intervalRef.current);
  }, [active, secsLeft, durationMins]);

  const handleDurationChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const mins = parseInt(e.target.value, 10);
    setDurationMins(mins);
    setSecsLeft(mins * 60);
  };

  const successRate = stats.total > 0 ? Math.round((stats.success / stats.total) * 100) : 0;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px', overflow: 'hidden' }}>
      <div style={{ marginBottom: 20, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Productivity HUD</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Performance auditing metrics · Focus intervals</p>
      </div>

      <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 20 }}>
        {/* Stats grid */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 10 }}>
          <StatCard label="Success Rate" value={`${successRate}%`} sub={`${stats.success}/${stats.total} tasks`} color="var(--success)" />
          <StatCard label="Heals Applied" value={stats.heals} sub="Autonomous patches" color="var(--accent-2)" />
          <StatCard label="Git Snapshots" value={stats.gitCommits} sub="Rollback points" color="var(--text-main)" />
          <StatCard label="Pomodoros" value={stats.pomodoros} sub="Focus blocks" color="var(--warning)" />
        </div>

        {/* Timer + diagnostics */}
        <div style={{ display: 'grid', gridTemplateColumns: '220px 1fr', gap: 16 }}>
          {/* Pomodoro timer */}
          <GlowCard className="glass" style={{ padding: 20, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16 }}>
            <div style={{ fontSize: 10, fontWeight: 600, color: 'var(--text-dim)', textTransform: 'uppercase', letterSpacing: '0.08em', fontFamily: "'JetBrains Mono', monospace" }}>
              Focus Timer
            </div>
            <ProgressArc
              value={secsLeft}
              max={durationMins * 60}
              size={140}
              strokeWidth={7}
              color={active ? 'var(--accent)' : 'var(--text-dim)'}
              animated={active}
              label="POMODORO"
            />
            <div style={{ display: 'flex', gap: 10 }}>
              <button
                onClick={async () => {
                  try {
                    if (active) {
                      await fetch('http://localhost:4132/api/pomodoro/stop', { method: 'POST' });
                      setActive(false);
                      setSecsLeft(durationMins * 60);
                    } else {
                      await fetch('http://localhost:4132/api/pomodoro/start', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ work_duration: durationMins * 60, break_duration: 5 * 60 })
                      });
                      setActive(true);
                      setSecsLeft(durationMins * 60);
                    }
                  } catch { /* noop */ }
                }}
                style={{
                  width: 40, height: 40, borderRadius: '50%', border: 'none', cursor: 'pointer',
                  background: active ? 'var(--warning)' : 'var(--accent)',
                  color: 'var(--bg-void)', display: 'flex', alignItems: 'center', justifyContent: 'center',
                  boxShadow: active ? '0 0 16px var(--warning)' : '0 0 16px var(--accent)',
                  transition: 'all 0.2s ease',
                }}
              >
                {active ? <Pause size={18} /> : <Play size={18} />}
              </button>
              <button
                onClick={async () => {
                  try {
                    await fetch('http://localhost:4132/api/pomodoro/stop', { method: 'POST' });
                    setActive(false);
                    setSecsLeft(durationMins * 60);
                  } catch { /* noop */ }
                }}
                style={{
                  width: 40, height: 40, borderRadius: '50%', border: '1px solid var(--border-subtle)',
                  background: 'var(--bg-surface)', cursor: 'pointer', color: 'var(--text-dim)',
                  display: 'flex', alignItems: 'center', justifyContent: 'center', transition: 'all 0.15s ease',
                }}
              >
                <RefreshCw size={16} />
              </button>
            </div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, width: '100%' }}>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Duration
              </label>
              <select
                value={durationMins}
                onChange={handleDurationChange}
                disabled={active}
                style={{
                  fontSize: 11,
                  padding: '4px 8px',
                  background: 'var(--bg-surface)',
                  color: 'var(--text-main)',
                  border: '1px solid var(--border-subtle)',
                  borderRadius: 'var(--radius-sm)',
                  cursor: active ? 'not-allowed' : 'pointer',
                  width: '80%',
                  textAlign: 'center',
                  outline: 'none',
                  fontFamily: "'JetBrains Mono', monospace",
                }}
              >
                <option value={15} style={{ background: 'var(--bg-surface)', color: 'var(--text-main)' }}>15 mins</option>
                <option value={25} style={{ background: 'var(--bg-surface)', color: 'var(--text-main)' }}>25 mins</option>
                <option value={45} style={{ background: 'var(--bg-surface)', color: 'var(--text-main)' }}>45 mins</option>
                <option value={60} style={{ background: 'var(--bg-surface)', color: 'var(--text-main)' }}>60 mins</option>
              </select>
            </div>
          </GlowCard>

          {/* Distraction Blocker (Websites & Apps) */}
          <GlowCard className="glass" style={{ padding: 16, display: 'flex', flexDirection: 'column', gap: 14 }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div>
                <div className="section-label" style={{ margin: 0 }}>Focus Distraction Blocker</div>
                <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                  Block distracting sites & background apps during focus blocks.
                </div>
              </div>
              <span style={{
                fontSize: 9,
                fontFamily: 'JetBrains Mono',
                padding: '2px 8px',
                borderRadius: 4,
                background: active ? 'rgba(239, 68, 68, 0.15)' : 'rgba(52, 211, 153, 0.15)',
                color: active ? 'var(--danger)' : 'var(--success)',
                fontWeight: 600,
                border: `1px solid ${active ? 'var(--danger)' : 'var(--success)'}`,
              }}>
                {active ? '🛡️ FOCUS SHIELD ACTIVE' : '⚡ READY (IDLE)'}
              </span>
            </div>

            {/* Presets */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Preset Distraction Targets
              </label>
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                {PRESET_DISTRACTIONS.map(item => {
                  const isBlocked = blockedTargets.includes(item.target);
                  return (
                    <button
                      key={item.id}
                      type="button"
                      onClick={() => toggleTarget(item.target)}
                      style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 6,
                        padding: '5px 10px',
                        borderRadius: 'var(--radius-sm)',
                        fontSize: 11,
                        fontFamily: "'JetBrains Mono', monospace",
                        cursor: 'pointer',
                        background: isBlocked ? 'rgba(239, 68, 68, 0.14)' : 'var(--bg-surface)',
                        border: isBlocked ? '1px solid var(--danger)' : '1px solid var(--border-subtle)',
                        color: isBlocked ? 'var(--danger)' : 'var(--text-main)',
                        transition: 'all 0.15s ease',
                      }}
                    >
                      <span>{isBlocked ? '⛔' : '🌐'}</span>
                      <span>{item.label}</span>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Custom Targets Add */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Custom Domains & App Processes
              </label>
              <div style={{ display: 'flex', gap: 8, marginBottom: 8 }}>
                <input
                  type="text"
                  value={customTarget}
                  onChange={e => setCustomTarget(e.target.value)}
                  onKeyDown={e => e.key === 'Enter' && addCustomTarget()}
                  placeholder="e.g. instagram.com or chrome.exe"
                  className="input-base"
                  style={{ flex: 1, fontSize: 11, fontFamily: "'JetBrains Mono', monospace" }}
                />
                <HoloButton type="button" variant="primary" size="sm" onClick={addCustomTarget} disabled={!customTarget.trim()}>
                  + Add
                </HoloButton>
              </div>

              {/* Active Target Tags List */}
              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6, maxHeight: 90, overflowY: 'auto' }}>
                {blockedTargets.map(t => (
                  <span
                    key={t}
                    style={{
                      fontSize: 10,
                      fontFamily: "'JetBrains Mono', monospace",
                      padding: '3px 8px',
                      borderRadius: 4,
                      background: 'var(--bg-surface)',
                      border: '1px solid var(--border-subtle)',
                      color: 'var(--text-bright)',
                      display: 'flex',
                      alignItems: 'center',
                      gap: 6,
                    }}
                  >
                    {t}
                    <button
                      type="button"
                      onClick={() => toggleTarget(t)}
                      style={{ background: 'none', border: 'none', color: 'var(--text-dim)', cursor: 'pointer', padding: 0, fontSize: 10, lineHeight: 1 }}
                    >
                      ✕
                    </button>
                  </span>
                ))}
              </div>
            </div>
          </GlowCard>
        </div>
      </div>
    </div>
  );
}
