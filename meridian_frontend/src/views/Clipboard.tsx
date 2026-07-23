import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Search, Zap, Copy, Check } from 'lucide-react';
import { ClipboardRecord } from '../types';
import { useApp } from '../AppContext';
import HoloButton from '../components/ui/HoloButton';

function reltime(ts: number) {
  const d = Math.floor((Date.now() - ts) / 1000);
  if (d < 60) return `${d}s ago`;
  if (d < 3600) return `${Math.floor(d / 60)}m ago`;
  return new Date(ts).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function detectType(text: string): string | null {
  if (text.startsWith('http://') || text.startsWith('https://')) return 'url';
  if (/\b(const|let|var|def|class|import|function|return)\b/.test(text)) return 'code';
  return null;
}

export default function Clipboard() {
  const { setActiveTab } = useApp();
  const [items, setItems] = useState<ClipboardRecord[]>([]);
  const [query, setQuery] = useState('');
  const [expanded, setExpanded] = useState<number | null>(null);
  const [copiedIdx, setCopiedIdx] = useState<number | null>(null);

  const fetch_ = async () => {
    try {
      const res = await fetch('http://localhost:4132/api/clipboard/history').catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        setItems(data.history || []);
      }
    } catch { /* noop */ }
  };

  useEffect(() => {
    fetch_();
    const t = setInterval(fetch_, 5000);
    return () => clearInterval(t);
  }, []);

  const analyze = (text: string) => {
    setActiveTab('timeline');
    const prompt = `Analyze this clipboard content:\n\n"${text}"`;
    window.dispatchEvent(new CustomEvent('meridian:send-chat', { detail: { prompt } }));
  };

  const copyToClipboard = (text: string, idx: number) => {
    navigator.clipboard.writeText(text).catch(() => {});
    setCopiedIdx(idx);
    setTimeout(() => setCopiedIdx(null), 2000);
  };

  const filtered = items.filter(it => it.text.toLowerCase().includes(query.toLowerCase()));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px' }}>
      <div style={{ marginBottom: 16, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Clipboard History</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Real-time pastebuffer surveillance · 1.5s polling</p>
      </div>

      {/* Search */}
      <div style={{ position: 'relative', marginBottom: 16, flexShrink: 0 }}>
        <Search size={14} style={{ position: 'absolute', left: 12, top: '50%', transform: 'translateY(-50%)', color: 'var(--text-dim)', pointerEvents: 'none' }} />
        <input
          type="text"
          value={query}
          onChange={e => setQuery(e.target.value)}
          placeholder="Filter clipboard events..."
          className="input-base"
          style={{ paddingLeft: 34 }}
        />
      </div>

      {/* Items */}
      <div style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 8 }}>
        {filtered.length === 0 ? (
          <div style={{ textAlign: 'center', padding: 60, color: 'var(--text-dim)', fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>
            {items.length === 0 ? 'Clipboard polling active. No entries captured yet.' : 'No items match your filter.'}
          </div>
        ) : (
          <AnimatePresence initial={false}>
            {filtered.map((item, idx) => {
              const tag = detectType(item.text);
              const isExp = expanded === idx;
              const isCopied = copiedIdx === idx;
              return (
                <motion.div
                  key={`${item.timestamp}-${idx}`}
                  initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: idx * 0.02, duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
                  style={{
                    background: 'var(--bg-panel)',
                    border: '1px solid var(--border-subtle)',
                    borderRadius: 'var(--radius-sm)',
                    padding: '10px 12px',
                    cursor: 'pointer',
                    transition: 'border-color 0.15s ease',
                  }}
                  onClick={() => setExpanded(isExp ? null : idx)}
                  onMouseEnter={e => (e.currentTarget as HTMLElement).style.borderColor = 'var(--border-glow)'}
                  onMouseLeave={e => (e.currentTarget as HTMLElement).style.borderColor = 'var(--border-subtle)'}
                >
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', gap: 8 }}>
                    <div style={{ flex: 1, minWidth: 0 }}>
                      <p style={{
                        fontSize: 12, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-main)',
                        margin: '0 0 4px', wordBreak: 'break-all',
                        overflow: 'hidden', display: '-webkit-box',
                        WebkitLineClamp: isExp ? 999 : 1, WebkitBoxOrient: 'vertical',
                        whiteSpace: isExp ? 'pre-wrap' : 'nowrap',
                        textOverflow: isExp ? 'unset' : 'ellipsis',
                      }}>
                        {item.text}
                      </p>
                      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                        <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
                          {reltime(item.timestamp)}
                        </span>
                        {tag && (
                          <span className={`badge badge-${tag === 'url' ? 'accent' : 'dim'}`}>{tag}</span>
                        )}
                      </div>
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                      <HoloButton
                        variant="ghost" size="sm"
                        onClick={e => { e.stopPropagation(); copyToClipboard(item.text, idx); }}
                        title="Copy to clipboard"
                      >
                        {isCopied ? <Check size={11} style={{ color: '#10b981' }} /> : <Copy size={11} />}
                      </HoloButton>
                      <HoloButton
                        variant="ghost" size="sm"
                        onClick={e => { e.stopPropagation(); analyze(item.text); }}
                        title="Analyze in Chatbot"
                      >
                        <Zap size={11} />
                      </HoloButton>
                    </div>
                  </div>
                </motion.div>
              );
            })}
          </AnimatePresence>
        )}
      </div>
    </div>
  );
}

