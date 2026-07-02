import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Zap, ChevronDown, ChevronUp } from 'lucide-react';
import { JobRun } from '../types';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';

interface JobsProps {
  onRunsUpdate: (runs: { id: string | number; status: string; goal: string }[]) => void;
}

function reltime(ts: number) {
  const d = Math.floor((Date.now() - ts) / 1000);
  if (d < 60) return `${d}s ago`;
  if (d < 3600) return `${Math.floor(d / 60)}m ago`;
  return `${Math.floor(d / 3600)}h ago`;
}

function RunCard({ run }: { run: JobRun; key?: React.Key }) {
  const [expanded, setExpanded] = useState(false);
  const ok = run.status === 'success';
  return (
    <motion.div
      initial={{ opacity: 0, x: -8 }}
      animate={{ opacity: 1, x: 0 }}
      style={{
        background: 'var(--bg-panel)',
        border: '1px solid var(--border-subtle)',
        borderLeft: `2px solid ${ok ? 'var(--success)' : 'var(--danger)'}`,
        borderRadius: 'var(--radius-sm)',
        padding: '10px 12px',
      }}
    >
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <span style={{
            width: 7, height: 7, borderRadius: '50%', flexShrink: 0,
            background: ok ? 'var(--success)' : 'var(--danger)',
            boxShadow: ok ? '0 0 6px var(--success)' : 'none',
            display: 'inline-block',
          }} />
          <span style={{ fontSize: 11, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)' }}>
            RUN #{run.id} · {run.status}
          </span>
        </div>
        <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
          {reltime(run.timestamp)}
        </span>
      </div>
      <p style={{
        fontSize: 12, color: 'var(--text-main)', margin: '0 0 6px', lineHeight: 1.4,
        overflow: 'hidden', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical',
      }}>
        {run.goal}
      </p>
      {run.log && (
        <>
          <button
            type="button"
            onClick={() => setExpanded(v => !v)}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', fontSize: 10, fontFamily: "'JetBrains Mono', monospace", padding: 0, display: 'flex', alignItems: 'center', gap: 4 }}
          >
            {expanded ? <ChevronUp size={11} /> : <ChevronDown size={11} />}
            {expanded ? 'Hide log' : 'View log'}
          </button>
          <AnimatePresence>
            {expanded && (
              <motion.pre
                initial={{ height: 0, opacity: 0 }} animate={{ height: 'auto', opacity: 1 }} exit={{ height: 0, opacity: 0 }}
                style={{
                  margin: '6px 0 0', padding: '8px', background: 'var(--bg-void)', borderRadius: 'var(--radius-sm)',
                  fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)',
                  overflow: 'auto', maxHeight: 120, whiteSpace: 'pre-wrap', wordBreak: 'break-all',
                }}
              >{run.log}</motion.pre>
            )}
          </AnimatePresence>
        </>
      )}
    </motion.div>
  );
}

export default function Jobs({ onRunsUpdate }: JobsProps) {
  const [runs, setRuns] = useState<JobRun[]>([]);
  const [goal, setGoal] = useState('');
  const [interval, setIntervalSec] = useState('');
  const [loading, setLoading] = useState(false);

  const fetchRuns = async () => {
    try {
      const res = await fetch('http://localhost:4132/api/scheduler/runs').catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        const runsArray = data.runs || [];
        setRuns(runsArray);
        onRunsUpdate(runsArray);
      }
    } catch { /* noop */ }
  };

  useEffect(() => {
    fetchRuns();
    const t = setInterval(fetchRuns, 8000);
    return () => clearInterval(t);
  }, []);

  const handleSchedule = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!goal.trim() || !interval.trim() || loading) return;
    setLoading(true);
    try {
      const res = await fetch('http://localhost:4132/api/scheduler/create', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal, interval_seconds: parseInt(interval) || 60 }),
      });
      if (res.ok) { setGoal(''); setIntervalSec(''); fetchRuns(); }
    } catch { /* noop */ }
    finally { setLoading(false); }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px' }}>
      <div style={{ marginBottom: 20, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Background Jobs</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>APScheduler · OS-level task automations</p>
      </div>

      <div style={{ flex: 1, display: 'grid', gridTemplateColumns: '240px 1fr', gap: 16, overflow: 'hidden' }}>
        {/* Schedule form */}
        <GlowCard className="glass" style={{ padding: 16, display: 'flex', flexDirection: 'column', gap: 12, height: 'fit-content' }}>
          <div className="section-label">Schedule Task</div>
          <form onSubmit={handleSchedule} style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>GOAL PROMPT</label>
              <textarea
                value={goal}
                onChange={e => setGoal(e.target.value)}
                placeholder="Check system memory every 5 minutes..."
                className="textarea-base"
                rows={3}
              />
            </div>
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>INTERVAL (SECONDS)</label>
              <input type="number" value={interval} onChange={e => setIntervalSec(e.target.value)} placeholder="300" className="input-base" />
            </div>
            <HoloButton type="submit" variant="primary" size="sm" loading={loading} disabled={!goal.trim() || !interval.trim()}>
              <Zap size={12} /> Schedule Agent
            </HoloButton>
          </form>
        </GlowCard>

        {/* Run list */}
        <div style={{ overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 8, paddingRight: 4 }}>
          <div className="section-label">Active Run Logs</div>
          {runs.length === 0 ? (
            <div style={{ textAlign: 'center', padding: 40, color: 'var(--text-dim)', fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>
              No job runs registered yet.
            </div>
          ) : (
            runs.map((r, i) => <RunCard key={r.id ?? i} run={r} />)
          )}
        </div>
      </div>
    </div>
  );
}
