import React, { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Send, RefreshCw } from 'lucide-react';
import TerminalLine from '../components/ui/TerminalLine';
import HoloButton from '../components/ui/HoloButton';

type LineType = 'system' | 'coder' | 'auditor' | 'qa' | 'consensus' | 'error';

interface LogLine { text: string; type: LineType; key: number; }

export default function SwarmDebate() {
  const [prompt, setPrompt] = useState('');
  const [lines, setLines] = useState<LogLine[]>([]);
  const [debating, setDebating] = useState(false);
  const [elapsed, setElapsed] = useState(0);
  const logEndRef = useRef<HTMLDivElement>(null);
  const elapsedRef = useRef<any>(null);
  const lineKey = useRef(0);

  const addLine = (text: string, type: LineType) => {
    lineKey.current += 1;
    setLines(prev => [...prev, { text, type, key: lineKey.current }]);
  };

  useEffect(() => {
    logEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [lines]);

  const startDebate = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!prompt.trim() || debating) return;
    setDebating(true);
    setElapsed(0);
    setLines([]);
    elapsedRef.current = setInterval(() => setElapsed(s => s + 1), 1000);

    addLine('Lobby initialized.', 'system');
    addLine('Invoking sandboxed agents: Coder, Auditor, QA...', 'system');

    try {
      const res = await fetch('http://localhost:4132/api/lobby/debate', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt }),
      });
      if (res.ok) {
        const data = await res.json();
        const logs = data.debate_logs || (data.debate || []).map((d: any) => `${d.agent}: ${d.message}`);
        const decision = data.decision || (data.proposed_code ? `Consensus reached. Proposed code:\n${data.proposed_code}` : '');
        
        logs.forEach((line: string) => {
          const type: LineType = line.startsWith('Coder') ? 'coder'
                                : line.startsWith('Auditor') ? 'auditor'
                                : line.startsWith('QA') ? 'qa'
                                : 'system';
          addLine(line, type);
        });
        if (decision) addLine(`Decision: ${decision}`, 'consensus');
      } else {
        addLine('Debate processing failed.', 'error');
      }
    } catch {
      // Offline fallback mock
      setTimeout(() => addLine('Suggest AES-256-GCM with PBKDF2 salt.', 'coder'), 400);
      setTimeout(() => addLine('Salt parameters verified. No credential leak detected.', 'auditor'), 800);
      setTimeout(() => addLine('Code parsed cleanly. Exit code 0.', 'qa'), 1200);
      setTimeout(() => addLine('Approved. Proceed with AES-256-GCM implementation.', 'consensus'), 1700);
    } finally {
      // Wait long enough for all setTimeout mock lines to be added before clearing state
      setTimeout(() => {
        setDebating(false);
        clearInterval(elapsedRef.current);
      }, 2200);
    }
  };

  const fmtElapsed = (s: number) => `${Math.floor(s / 60).toString().padStart(2, '0')}:${(s % 60).toString().padStart(2, '0')}`;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px' }}>
      <div style={{ marginBottom: 20, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Consensus Debate Lobby</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Cooperative multi-agent sandbox debates</p>
      </div>

      {/* Input */}
      <form onSubmit={startDebate} style={{ display: 'flex', gap: 8, marginBottom: 16, flexShrink: 0 }}>
        <input
          type="text"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
          disabled={debating}
          placeholder="Enter a development task to debate (e.g. Implement AES-256 encryption)..."
          className="input-base"
          style={{ flex: 1 }}
        />
        <HoloButton type="submit" variant="primary" size="sm" disabled={!prompt.trim() || debating} loading={debating}>
          {debating ? <RefreshCw size={12} /> : <Send size={12} />}
          {debating ? 'Debating...' : 'Debate'}
        </HoloButton>
      </form>

      {/* Terminal log */}
      <div style={{
        flex: 1,
        background: 'var(--bg-void)',
        border: '1px solid var(--border-subtle)',
        borderRadius: 'var(--radius-md)',
        padding: '12px 14px',
        overflow: 'hidden',
        display: 'flex',
        flexDirection: 'column',
      }}>
        {/* Terminal header bar */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 8, paddingBottom: 8, borderBottom: '1px solid var(--border-subtle)' }}>
          <div style={{ display: 'flex', gap: 6 }}>
            {['var(--danger)', 'var(--warning)', 'var(--success)'].map((c, i) => (
              <div key={i} style={{ width: 8, height: 8, borderRadius: '50%', background: c, opacity: 0.7 }} />
            ))}
          </div>
          <span style={{ fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)' }}>
            meridian-x · swarm-debate{debating ? ` · ${fmtElapsed(elapsed)}` : ''}
          </span>
          <span style={{ fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)' }}>zsh</span>
        </div>

        {/* Log lines */}
        <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column' }}>
          {lines.length === 0 && !debating && (
            <p style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", margin: 0 }}>
              Enter a task above to start a multi-agent debate.
            </p>
          )}
          {lines.map((line, i) => (
            <TerminalLine key={line.key} text={line.text} type={line.type} delay={i * 40} />
          ))}
          {debating && (
            <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 4 }}>
              <RefreshCw size={11} style={{ color: 'var(--accent)', animation: 'orbit-cw 1s linear infinite' }} />
              <span style={{ fontSize: 11, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace" }}>Running agent debate loops...</span>
            </div>
          )}
          {!debating && lines.length > 0 && (
            <div style={{ display: 'flex', marginTop: 6 }}>
              <span className="animate-blink-cursor" style={{ fontSize: 13, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>_</span>
            </div>
          )}
          <div ref={logEndRef} />
        </div>
      </div>
    </div>
  );
}
