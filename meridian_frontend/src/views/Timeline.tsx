import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Trash2, Send, User, Bot, ShieldAlert, AlertTriangle, Check, X, Plus, Paperclip, ChevronDown, ChevronRight, Volume2, VolumeX, Square } from 'lucide-react';
import { emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { Message } from '../types';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';
import { marked } from 'marked';
import DOMPurify from 'dompurify';

// Helper function to render Markdown safely
const renderMarkdown = (text: string) => {
  try {
    const rawHtml = marked.parse(text, { breaks: true, gfm: true }) as string;
    const cleanHtml = DOMPurify.sanitize(rawHtml);
    return { __html: cleanHtml };
  } catch (e) {
    console.error("Markdown parse error:", e);
    return { __html: text };
  }
};

interface TimelineProps {
  onThoughtsUpdate: (feed: { thoughts: string[]; streaming: boolean }) => void;
}

// Collapsible ReAct thoughts
function ThoughtsBlock({ thoughts }: { thoughts: string[] }) {
  const [open, setOpen] = useState(false);
  return (
    <div style={{
      margin: '6px 0',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-sm)',
      overflow: 'hidden',
    }}>
      <button
        type="button"
        onClick={() => setOpen(v => !v)}
        style={{
          width: '100%', display: 'flex', alignItems: 'center', gap: 6,
          padding: '5px 10px', background: 'none', border: 'none', cursor: 'pointer',
          color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", fontSize: 10, fontWeight: 600,
        }}
      >
        <motion.span animate={{ rotate: open ? 90 : 0 }} transition={{ duration: 0.15 }} style={{ display: 'inline-flex' }}>
          <ChevronRight size={11} />
        </motion.span>
        ReAct Thoughts ({thoughts.length})
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0 }} animate={{ height: 'auto' }} exit={{ height: 0 }}
            transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
            style={{ overflow: 'hidden' }}
          >
            <ol style={{
              margin: 0, padding: '6px 10px 8px 28px', borderTop: '1px solid var(--border-subtle)',
              display: 'flex', flexDirection: 'column', gap: 4,
            }}>
              {thoughts.map((t, i) => (
                <li key={i} style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.5 }}>{t}</li>
              ))}
            </ol>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

// Safety gate card (inside bot message)
function SafetyGate({ gate, onConfirm }: { gate: any; onConfirm: (id: string, approved: boolean) => void }) {
  return (
    <div style={{
      marginTop: 8, padding: '10px 12px', borderRadius: 'var(--radius-sm)',
      background: 'color-mix(in srgb, var(--warning) 8%, transparent)',
      border: '1px solid color-mix(in srgb, var(--warning) 25%, transparent)',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>
        <ShieldAlert size={13} style={{ color: 'var(--warning)' }} />
        <span style={{ fontSize: 10, fontWeight: 700, color: 'var(--warning)', fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.06em' }}>
          SAFETY CONFIRMATION [TIER {gate.tier}]
        </span>
      </div>
      <p style={{ fontSize: 11, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)', margin: '0 0 8px' }}>Tool: {gate.tool_name}</p>
      {gate.prompt && <p style={{ fontSize: 12, color: 'var(--text-main)', margin: '0 0 10px', lineHeight: 1.5 }}>{gate.prompt}</p>}
      <div style={{ display: 'flex', gap: 8 }}>
        <HoloButton variant="primary" size="sm" onClick={() => onConfirm(gate.id, true)}>
          <Check size={12} /> Approve
        </HoloButton>
        <HoloButton variant="danger" size="sm" onClick={() => onConfirm(gate.id, false)}>
          <X size={12} /> Reject
        </HoloButton>
      </div>
    </div>
  );
}

// Heal diff block (inside bot message)
function HealBlock({ heal, onApply }: { heal: any; onApply: (path: string, code: string) => void }) {
  return (
    <div style={{
      marginTop: 8, padding: '10px 12px', borderRadius: 'var(--radius-sm)',
      background: 'var(--bg-surface)', border: '1px solid color-mix(in srgb, var(--danger) 25%, transparent)',
    }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 6 }}>
        <AlertTriangle size={13} style={{ color: 'var(--danger)' }} />
        <span style={{ fontSize: 10, fontWeight: 700, color: 'var(--danger)', fontFamily: "'JetBrains Mono', monospace" }}>
          AUTO-HEALING PATCH
        </span>
      </div>
      <p style={{ fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: 'var(--text-dim)', margin: '0 0 8px' }}>{heal.file_path}</p>
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, marginBottom: 10 }}>
        <div style={{ background: 'rgba(0,0,0,0.3)', borderRadius: 'var(--radius-sm)', padding: '6px 8px' }}>
          <p style={{ fontSize: 9, color: 'var(--danger)', fontFamily: 'JetBrains Mono', marginBottom: 4, fontWeight: 600 }}>ORIGINAL</p>
          <pre style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-all', maxHeight: 120, overflow: 'auto' }}>
            {heal.original_code || heal.original}
          </pre>
        </div>
        <div style={{ background: 'rgba(0,0,0,0.3)', borderRadius: 'var(--radius-sm)', padding: '6px 8px' }}>
          <p style={{ fontSize: 9, color: 'var(--success)', fontFamily: 'JetBrains Mono', marginBottom: 4, fontWeight: 600 }}>CORRECTION</p>
          <pre style={{ fontSize: 10, color: 'var(--text-main)', fontFamily: 'JetBrains Mono', margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-all', maxHeight: 120, overflow: 'auto' }}>
            {heal.proposed_code || heal.proposed}
          </pre>
        </div>
      </div>
      <HoloButton variant="primary" size="sm" onClick={() => onApply(heal.file_path, heal.proposed_code || heal.proposed)}>
        Apply Heal
      </HoloButton>
    </div>
  );
}

export default function Timeline({ onThoughtsUpdate }: TimelineProps) {
  const [messages, setMessages] = useState<any[]>([{
    id: 'init', role: 'assistant', timestamp: Date.now(),
    content: 'System loaded. Standing by for autonomous instructions.',
  }]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [streaming, setStreaming] = useState('');
  const [streamThoughts, setStreamThoughts] = useState<string[]>([]);
  const [dragActive, setDragActive] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const abortControllerRef = useRef<AbortController | null>(null);
  const [ttsEnabled, setTtsEnabled] = useState(() => localStorage.getItem('meridian_dashboard_tts') === 'true');

  const speakMessage = async (text: string) => {
    if (!text.trim()) return;
    try {
      const voice = localStorage.getItem('meridian_tts_voice') || 'M1';
      const volume = parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5');
      const res = await fetch('http://localhost:4132/api/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, voice, lang: 'na' }),
      });
      if (res.ok) {
        const blob = await res.blob();
        const url = URL.createObjectURL(blob);
        const audio = new Audio(url);
        audio.volume = volume;
        await audio.play();
      }
    } catch (e) {
      console.warn("Failed to play TTS in Dashboard:", e);
    }
  };

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, streaming]);

  useEffect(() => {
    onThoughtsUpdate({ thoughts: streamThoughts, streaming: loading });
  }, [streamThoughts, loading]);

  const handleTimelineClick = (e: React.MouseEvent<HTMLDivElement>) => {
    const target = e.target as HTMLElement;
    const anchor = target.closest('a');
    if (anchor) {
      const href = anchor.getAttribute('href');
      if (href && !href.startsWith('#')) {
        e.preventDefault();
        invoke('open_url', { url: href }).catch(err => {
          console.error("Failed to open URL externally:", err);
        });
      }
    }
  };

  const clearChat = async () => {
    try { await fetch('http://localhost:4132/api/chat/clear', { method: 'POST' }); } catch { /* noop */ }
    setMessages([]);
  };

  // The backend wraps final responses as {"chat":"...","speech":"...","lang":"..."}
  // This extracts just the human-readable chat portion from that wrapper.
  const extractChatText = (raw: string): string => {
    const trimmed = raw.trim();
    if (trimmed.startsWith('{')) {
      try {
        const parsed = JSON.parse(trimmed);
        if (parsed.chat) return parsed.chat;
      } catch { /* not JSON, return as-is */ }
    }
    return raw;
  };

  const handleSend = async (e?: React.FormEvent) => {
    e?.preventDefault();
    if (!input.trim() || loading) return;
    const text = input.trim();
    setInput('');
    setLoading(true);
    setStreaming('');
    setStreamThoughts([]);

    const userMsg = { id: Date.now(), role: 'user', timestamp: Date.now(), content: text };
    setMessages(prev => [...prev, userMsg]);

    if ((window as any).__TAURI_INTERNALS__) {
      emit('agent-status-update', {
        isRunning: true,
        latestThought: { text: 'Initializing agent...', type: 'planning' },
        thoughts: []
      }).catch(console.error);
    }

    const controller = new AbortController();
    abortControllerRef.current = controller;

    const provider = localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama';
    const brainModel = localStorage.getItem('MERIDIAN_MODEL') || '';
    const modelSource = provider === 'ollama' ? 'local' : 'api';
    const openaiKey = localStorage.getItem('OPENAI_API_KEY') || '';
    const anthropicKey = localStorage.getItem('ANTHROPIC_API_KEY') || '';
    const geminiKey = localStorage.getItem('GEMINI_API_KEY') || '';
    const deepseekKey = localStorage.getItem('DEEPSEEK_API_KEY') || '';

    try {
      const res = await fetch('http://localhost:4132/api/chat/stream', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: text,
          modelSettings: {
            modelSource,
            apiProvider: provider,
            selectedModel: brainModel,
            brainModel,
            ocrModel: brainModel,
            openaiKey,
            anthropicKey,
            geminiKey,
            deepseekKey
          }
        }),
        signal: controller.signal,
      });
      if (!res.ok || !res.body) throw new Error('Stream failed');

      const reader = res.body.getReader();
      const decoder = new TextDecoder();
      let finalContent = '';
      let finalThoughts: { id: string; text: string }[] = [];
      // Buffer accumulates partial TCP chunks; we split on \n\n (SSE event separator)
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        // SSE events are delimited by double newline
        const events = buffer.split('\n\n');
        // Keep the last (possibly incomplete) event in the buffer
        buffer = events.pop() ?? '';

        for (const eventBlock of events) {
          if (!eventBlock.trim()) continue;
          const lines = eventBlock.split('\n');
          let eventType = 'text'; // default to text if no event: line
          const dataLines: string[] = [];

          for (const line of lines) {
            if (line.startsWith('event: ')) {
              eventType = line.slice(7).trim();
            } else if (line.startsWith('data: ')) {
              dataLines.push(line.slice(6));
            }
          }

          const payload = dataLines.join('\n');
          if (!payload) continue;

          if (eventType === 'thought') {
            try {
              const thoughtData = JSON.parse(payload);
              const thoughtText = thoughtData.text || thoughtData.thought || String(thoughtData);
              const id = thoughtData.id || `thought-fallback-${Date.now()}-${Math.random()}`;
              const existingIdx = finalThoughts.findIndex(t => t.id === id);
              if (existingIdx !== -1) {
                finalThoughts[existingIdx].text += thoughtText;
              } else {
                finalThoughts.push({ id, text: thoughtText });
              }
              const updatedThoughts = finalThoughts.map(t => t.text);
              setStreamThoughts(updatedThoughts);
              if ((window as any).__TAURI_INTERNALS__) {
                emit('agent-status-update', {
                  isRunning: true,
                  latestThought: thoughtData,
                  thoughts: updatedThoughts
                }).catch(console.error);
              }
            } catch { /* non-JSON thought, skip */ }
          } else if (eventType === 'text') {
            // text events carry raw text chunks (not JSON)
            // Some chunks may be the final JSON wrapper — extract the chat field
            const chunk = extractChatText(payload);
            finalContent += chunk;
            setStreaming(finalContent);
          } else if (eventType === 'confirmation') {
            try {
              const confData = JSON.parse(payload);
              setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: 'Security confirmation required:', confirmation: confData }]);
            } catch { /* noop */ }
          } else if (eventType === 'heal') {
            try {
              const healData = JSON.parse(payload);
              setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: 'Auto-healing patch proposal:', proposedHeal: healData }]);
            } catch { /* noop */ }
          }
        }
      }
      // Final: extract chat text from any JSON wrapper and strip duplicate content
      // The backend may stream chunks then send the full text again as final event
      const thoughtsList = finalThoughts.map(t => t.text);
      const cleanedContent = extractChatText(finalContent);
      setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: cleanedContent || 'Operation completed.', thoughts: thoughtsList }]);
      setStreaming('');
      setStreamThoughts([]);
      if ((window as any).__TAURI_INTERNALS__) {
        emit('agent-status-update', {
          isRunning: false,
          latestThought: { text: 'Task completed', type: 'status' },
          thoughts: []
        }).catch(console.error);
      }

      // If dashboard TTS is enabled, read response out loud
      if (ttsEnabled && cleanedContent) {
        speakMessage(cleanedContent);
      }
    } catch (err: any) {
      if (err.name === 'AbortError') {
        setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: 'Execution interrupted.' }]);
      } else {
        setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: 'Failed to reach local AI backend.' }]);
      }
      setStreaming('');
      setStreamThoughts([]);
      if ((window as any).__TAURI_INTERNALS__) {
        emit('agent-status-update', {
          isRunning: false,
          latestThought: { text: err.name === 'AbortError' ? 'Task interrupted' : 'Task failed', type: 'error' },
          thoughts: []
        }).catch(console.error);
      }
    } finally {
      abortControllerRef.current = null;
      setLoading(false);
    }
  };

  const handleInterrupt = async () => {
    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      abortControllerRef.current = null;
    }
    setLoading(false);
    setStreaming('');
    setStreamThoughts([]);
    try {
      await fetch('http://localhost:4132/api/voice/interrupt', { method: 'POST' });
    } catch (e) {
      console.warn("Failed to send interrupt request:", e);
    }
  };

  const handleConfirm = async (id: string, approved: boolean) => {
    try {
      await fetch('http://localhost:4132/api/chat/confirm', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id, approved }),
      });
      setMessages(prev => prev.map(m => m.confirmation?.id === id
        ? { ...m, content: `Confirmation resolved: ${approved ? 'APPROVED ✓' : 'REJECTED ✕'}`, confirmation: undefined }
        : m
      ));
    } catch { /* noop */ }
  };

  const handleApplyHeal = async (path: string, code: string) => {
    try {
      await fetch('http://localhost:4132/api/watcher/apply-heal', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_path: path, heal_code: code }),
      });
      setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: `✓ Heal applied to ${path}. Git snapshot created.` }]);
    } catch { /* noop */ }
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    setDragActive(false);
    const file = e.dataTransfer.files?.[0];
    if (!file) return;
    setMessages(prev => [...prev, { id: Date.now(), role: 'user', timestamp: Date.now(), content: `Ingesting: ${file.name}` }]);
    const fd = new FormData();
    fd.append('file', file);
    try {
      const res = await fetch('http://localhost:4132/api/rag/ingest-file', { method: 'POST', body: fd });
      setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(),
        content: res.ok ? `✓ ${file.name} indexed into SQLite/Turbovec.` : `✕ Failed to ingest ${file.name}.`,
      }]);
    } catch {
      setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: 'RAG backend unreachable.' }]);
    }
  };

  const reltime = (ts: number) => {
    const d = Math.floor((Date.now() - ts) / 1000);
    if (d < 10) return 'just now';
    if (d < 60) return `${d}s ago`;
    return new Date(ts).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
  };

  return (
    <div
      style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px' }}
      onDragEnter={e => { e.preventDefault(); setDragActive(true); }}
      onDragOver={e => e.preventDefault()}
      onDragLeave={() => setDragActive(false)}
      onDrop={handleDrop}
    >
      {/* Drag overlay */}
      <AnimatePresence>
        {dragActive && (
          <motion.div
            initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }}
            style={{
              position: 'fixed', inset: 0, zIndex: 50,
              background: 'rgba(0,0,0,0.7)', backdropFilter: 'blur(8px)',
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              border: '2px dashed var(--accent)',
            }}
          >
            <div style={{ textAlign: 'center', color: 'var(--accent)' }}>
              <Plus size={48} style={{ marginBottom: 12, filter: 'drop-shadow(0 0 16px var(--accent))' }} />
              <p style={{ fontSize: 16, fontWeight: 700, margin: 0 }}>Drop to vector-ingest</p>
              <p style={{ fontSize: 12, color: 'var(--text-dim)', marginTop: 4 }}>PDF · DOCX · CSV · JSON · TXT · MD</p>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Header */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16, flexShrink: 0 }}>
        <div>
          <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Timeline Logs</h1>
          <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Execution audit · ReAct thought stream</p>
        </div>
        <HoloButton variant="danger" size="sm" onClick={clearChat}>
          <Trash2 size={12} /> Clear
        </HoloButton>
      </div>

      {/* Messages */}
      <div
        onClick={handleTimelineClick}
        style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 12, marginBottom: 12 }}
      >
        <AnimatePresence initial={false}>
          {messages.map((msg, i) => {
            const isUser = msg.role === 'user';
            return (
              <motion.div
                key={msg.id ?? i}
                initial={{ opacity: 0, y: 8, scale: 0.98 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                transition={{ duration: 0.22, ease: [0.16, 1, 0.3, 1] }}
                style={{
                  display: 'flex',
                  flexDirection: isUser ? 'row-reverse' : 'row',
                  gap: 10,
                  alignItems: 'flex-start',
                  paddingLeft: isUser ? 48 : 0,
                  paddingRight: isUser ? 0 : 48,
                }}
              >
                {/* Avatar */}
                <div style={{
                  width: 32, height: 32, borderRadius: 'var(--radius-sm)', flexShrink: 0,
                  background: isUser ? 'color-mix(in srgb, var(--accent-2) 15%, transparent)' : 'color-mix(in srgb, var(--accent) 12%, transparent)',
                  border: `1px solid ${isUser ? 'color-mix(in srgb, var(--accent-2) 30%, transparent)' : 'color-mix(in srgb, var(--accent) 25%, transparent)'}`,
                  display: 'flex', alignItems: 'center', justifyContent: 'center',
                  color: isUser ? 'var(--accent-2)' : 'var(--accent)',
                }}>
                  {isUser ? <User size={15} /> : <Bot size={15} />}
                </div>

                {/* Bubble */}
                <div style={{
                  flex: 1,
                  background: isUser ? 'var(--bg-surface)' : 'var(--bg-panel)',
                  border: `1px solid var(--border-subtle)`,
                  borderLeft: `2px solid ${isUser ? 'var(--accent-2)' : 'var(--accent)'}`,
                  borderRadius: 'var(--radius-sm)',
                  padding: '10px 12px',
                }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                    <span style={{ fontSize: 10, fontWeight: 600, color: isUser ? 'var(--accent-2)' : 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                      {msg.role}
                    </span>
                    <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
                      {reltime(msg.timestamp)}
                    </span>
                  </div>

                  {msg.thoughts?.length > 0 && <ThoughtsBlock thoughts={msg.thoughts} />}
                  <div
                    className="markdown-content"
                    style={{ fontSize: 13, color: 'var(--text-main)', margin: 0, lineHeight: 1.6 }}
                    dangerouslySetInnerHTML={renderMarkdown(msg.content)}
                  />
                  {msg.confirmation && <SafetyGate gate={msg.confirmation} onConfirm={handleConfirm} />}
                  {msg.proposedHeal && <HealBlock heal={msg.proposedHeal} onApply={handleApplyHeal} />}
                </div>
              </motion.div>
            );
          })}
        </AnimatePresence>

        {/* Streaming indicator */}
        {(streaming || streamThoughts.length > 0) && (
          <motion.div
            initial={{ opacity: 0, y: 8 }} animate={{ opacity: 1, y: 0 }}
            style={{ display: 'flex', gap: 10, paddingRight: 48 }}
          >
            <div style={{
              width: 32, height: 32, borderRadius: 'var(--radius-sm)', flexShrink: 0,
              background: 'color-mix(in srgb, var(--accent) 12%, transparent)',
              border: '1px solid color-mix(in srgb, var(--accent) 25%, transparent)',
              display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--accent)',
            }}>
              <Bot size={15} />
            </div>
            <div style={{
              flex: 1, background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)',
              borderLeft: '2px solid var(--accent)', borderRadius: 'var(--radius-sm)', padding: '10px 12px',
            }}>
              <span style={{ fontSize: 10, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace', animation: 'blink-cursor 1s step-end infinite'" }}>
                THINKING...
              </span>
              {streaming && (
                <div
                  className="markdown-content"
                  style={{ fontSize: 13, color: 'var(--text-main)', margin: '6px 0 0', lineHeight: 1.6 }}
                  dangerouslySetInnerHTML={renderMarkdown(streaming)}
                />
              )}
            </div>
          </motion.div>
        )}

        <div ref={chatEndRef} />
      </div>

      {/* Input */}
      <form onSubmit={handleSend} style={{
        display: 'flex', gap: 8, alignItems: 'center', flexShrink: 0,
        background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)',
        borderRadius: 'var(--radius-md)', padding: '8px 8px 8px 14px',
      }}>
        <input
          ref={fileInputRef as any}
          type="file"
          style={{ display: 'none' }}
          onChange={async e => {
            const file = e.target.files?.[0];
            if (!file) return;
            const fd = new FormData();
            fd.append('file', file);
            setMessages(prev => [...prev, { id: Date.now(), role: 'user', timestamp: Date.now(), content: `Ingesting: ${file.name}` }]);
            try {
              const res = await fetch('http://localhost:4132/api/rag/ingest-file', { method: 'POST', body: fd });
              setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: res.ok ? `✓ ${file.name} indexed.` : `✕ Failed to ingest.` }]);
            } catch { /* noop */ }
          }}
        />
        <button type="button" onClick={() => (fileInputRef.current as any)?.click()}
          title="Attach file for RAG ingestion"
          style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 4, display: 'flex', flexShrink: 0 }}
        >
          <Paperclip size={16} />
        </button>
        <input
          type="text"
          value={input}
          onChange={e => setInput(e.target.value)}
          disabled={loading}
          placeholder="Ask Meridian-X to perform actions or analyze targets..."
          style={{
            flex: 1, background: 'transparent', border: 'none', outline: 'none',
            color: 'var(--text-main)', fontSize: 13, fontFamily: "'Space Grotesk', sans-serif",
          }}
        />
        {/* Speak Toggle Button */}
        <button
          type="button"
          onClick={() => {
            const nextVal = !ttsEnabled;
            setTtsEnabled(nextVal);
            localStorage.setItem('meridian_dashboard_tts', String(nextVal));
          }}
          title={ttsEnabled ? "Mute Speech Output" : "Enable Speech Output"}
          style={{
            background: 'none', border: 'none', cursor: 'pointer',
            color: ttsEnabled ? 'var(--accent)' : 'var(--text-dim)',
            padding: 4, display: 'flex', flexShrink: 0, transition: 'color 0.15s ease'
          }}
        >
          {ttsEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}
        </button>
        {loading ? (
          <HoloButton type="button" variant="danger" size="sm" onClick={handleInterrupt}>
            <Square size={14} fill="currentColor" />
          </HoloButton>
        ) : (
          <HoloButton type="submit" variant="primary" size="sm" disabled={!input.trim()}>
            <Send size={14} />
          </HoloButton>
        )}
      </form>
    </div>
  );
}
