import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Search, Zap, Copy, Check, Trash2 } from 'lucide-react';
import { ClipboardRecord } from '../types';
import { useApp } from '../AppContext';
import HoloButton from '../components/ui/HoloButton';
import { API_BASE_URL } from '../config';

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
      const res = await fetch(`${API_BASE_URL}/api/clipboard/history?limit=50`).catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        setItems(data.history || []);
      }
    } catch { /* noop */ }
  };

  const clearHistory = async () => {
    setItems([]);
    try {
      await fetch(`${API_BASE_URL}/api/clipboard/clear`, { method: 'POST' }).catch(() => {});
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
  const urlCount = items.filter(it => detectType(it.text) === 'url').length;
  const codeCount = items.filter(it => detectType(it.text) === 'code').length;

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px' }}>
      <div style={{ marginBottom: 14, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Clipboard History</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Real-time pastebuffer surveillance · 50 slots persistent</p>
      </div>

      {/* Quick Stats Summary Bar */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr auto', gap: 10, marginBottom: 14, flexShrink: 0, alignItems: 'center' }}>
        <div style={{ padding: '8px 12px', background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-sm)' }}>
          <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase' }}>Total Clips</div>
          <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent)', fontFamily: "'Space Grotesk', sans-serif" }}>{items.length}</div>
        </div>
        <div style={{ padding: '8px 12px', background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-sm)' }}>
          <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase' }}>URLs</div>
          <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent-2)', fontFamily: "'Space Grotesk', sans-serif" }}>{urlCount}</div>
        </div>
        <div style={{ padding: '8px 12px', background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-sm)' }}>
          <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase' }}>Code Snippets</div>
          <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--warning)', fontFamily: "'Space Grotesk', sans-serif" }}>{codeCount}</div>
        </div>
        <HoloButton type="button" variant="ghost" size="sm" onClick={clearHistory} disabled={items.length === 0} title="Clear all clipboard history">
          <Trash2 size={12} /> Clear All
        </HoloButton>
      </div>

      {/* Search */}
      <div style={{ position: 'relative', marginBottom: 14, flexShrink: 0 }}>
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

      {/* Items Grid */}
      <div style={{ flex: 1, overflowY: 'auto', paddingRight: 2 }}>
        {filtered.length === 0 ? (
          <div style={{ textAlign: 'center', padding: 60, color: 'var(--text-dim)', fontSize: 12, fontFamily: "'JetBrains Mono', monospace" }}>
            {items.length === 0 ? 'Clipboard polling active. No entries captured yet.' : 'No items match your filter.'}
          </div>
        ) : (
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))', gap: 12, paddingBottom: 16 }}>
            <AnimatePresence initial={false}>
              {filtered.map((item, idx) => {
                const tag = detectType(item.text);
                const isExp = expanded === idx;
                const isCopied = copiedIdx === idx;
                return (
                  <motion.div
                    key={`${item.timestamp}-${idx}`}
                    initial={{ opacity: 0, y: 6 }} animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: Math.min(idx * 0.015, 0.2), duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
                    style={{
                      background: 'var(--bg-panel)',
                      border: '1px solid var(--border-subtle)',
                      borderRadius: 'var(--radius-md)',
                      padding: '12px',
                      cursor: 'pointer',
                      display: 'flex',
                      flexDirection: 'column',
                      justify: 'space-between',
                      gap: 10,
                      transition: 'all 0.15s ease',
                      boxShadow: 'var(--card-shadow)',
                    }}
                    onClick={() => setExpanded(isExp ? null : idx)}
                    onMouseEnter={e => (e.currentTarget as HTMLElement).style.borderColor = 'var(--accent)'}
                    onMouseLeave={e => (e.currentTarget as HTMLElement).style.borderColor = 'var(--border-subtle)'}
                  >
                    {/* Header: Timestamp & Badge */}
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                      <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
                        {reltime(item.timestamp)}
                      </span>
                      {tag && (
                        <span className={`badge badge-${tag === 'url' ? 'accent' : 'dim'}`} style={{ fontSize: 9 }}>{tag}</span>
                      )}
                    </div>

                    {/* Body: Truncated Content */}
                    <p style={{
                      fontSize: 11,
                      fontFamily: "'JetBrains Mono', monospace",
                      color: 'var(--text-main)',
                      margin: 0,
                      wordBreak: 'break-all',
                      overflow: 'hidden',
                      display: '-webkit-box',
                      WebkitLineClamp: isExp ? 999 : 3,
                      WebkitBoxOrient: 'vertical',
                      whiteSpace: isExp ? 'pre-wrap' : 'normal',
                      lineHeight: 1.45,
                    }}>
                      {item.text}
                    </p>

                    {/* Footer: Action Buttons */}
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 6, borderTop: '1px solid var(--border-subtle)', paddingTop: 8 }}>
                      <HoloButton
                        variant="ghost" size="sm"
                        onClick={e => { e.stopPropagation(); copyToClipboard(item.text, idx); }}
                        title="Copy to clipboard"
                      >
                        {isCopied ? <Check size={11} style={{ color: 'var(--success)' }} /> : <Copy size={11} />}
                      </HoloButton>
                      <HoloButton
                        variant="ghost" size="sm"
                        onClick={e => { e.stopPropagation(); analyze(item.text); }}
                        title="Analyze in Chatbot"
                      >
                        <Zap size={11} /> Analyze
                      </HoloButton>
                    </div>
                  </motion.div>
                );
              })}
            </AnimatePresence>
          </div>
        )}
      </div>
    </div>
  );
}

