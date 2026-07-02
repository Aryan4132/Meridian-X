import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'motion/react';
import { Play, Pause, RefreshCw } from 'lucide-react';
import { DeveloperStats } from '../types';
import ProgressArc from '../components/ui/ProgressArc';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';

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

export default function Productivity() {
  const [stats, setStats] = useState<DeveloperStats>({ total: 0, success: 0, failed: 0, audits: 0, heals: 0, gitCommits: 0, pomodoros: 0 });
  const [durationMins, setDurationMins] = useState(25);
  const [secsLeft, setSecsLeft] = useState(25 * 60);
  const [active, setActive] = useState(false);
  const intervalRef = useRef<any>(null);

  const fetchStats = async () => {
    try {
      const res = await fetch('http://localhost:4132/api/developer/stats').catch(() => null);
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

  useEffect(() => { fetchStats(); }, []);

  useEffect(() => {
    if (active && secsLeft > 0) {
      intervalRef.current = setInterval(() => setSecsLeft(s => s - 1), 1000);
    } else if (secsLeft === 0) {
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
                onClick={() => setActive(v => !v)}
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
                onClick={() => { setActive(false); setSecsLeft(durationMins * 60); }}
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

          {/* Diagnostics */}
          <GlowCard className="glass" style={{ padding: 16, display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div className="section-label">System Diagnostics</div>
            {[
              { name: 'AST Syntax Watcher', desc: 'Auto-compiles workspace files on save. Syntax errors trigger self-healing diff patches.', color: 'var(--danger)', status: 'ACTIVE' },
              { name: 'Secure Port Check', desc: 'Prevents credential leaks. Audits outgoing connections and blocks restricted file access.', color: 'var(--warning)', status: 'ACTIVE' },
              { name: 'Security Auditor', desc: 'Tier 2+ operations run through an isolated validator model before execution.', color: 'var(--accent)', status: 'ACTIVE' },
            ].map(({ name, desc, color, status }) => (
              <div key={name} style={{ padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', borderLeft: `2px solid ${color}` }}>
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                  <span style={{ fontSize: 11, fontWeight: 600, color, fontFamily: "'JetBrains Mono', monospace" }}>{name}</span>
                  <span className="badge badge-success" style={{ borderColor: color, color }}>{status}</span>
                </div>
                <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: 0, lineHeight: 1.5 }}>{desc}</p>
              </div>
            ))}
          </GlowCard>
        </div>
      </div>
    </div>
  );
}
