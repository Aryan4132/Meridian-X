import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Trash2, Send, User, Bot, ShieldAlert, AlertTriangle, Check, X, Plus, Paperclip, ChevronDown, ChevronRight, Volume2, VolumeX, Square, RotateCcw, Eye, GitBranch, ClipboardCopy, Sparkles, Copy, CheckCheck, ShieldCheck, Cpu, Wand2 } from 'lucide-react';
import { emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { Message } from '../types';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';
import { marked } from 'marked';
import DOMPurify from 'dompurify';
import { API_BASE_URL } from '../config';
import { streamingAudio } from '../services/streamingAudioPlayer';
import CodeDiffViewer from '../components/ui/CodeDiffViewer';

// Preprocessor for LaTeX math symbols, arrows, and formatting (e.g. \rightarrow, $\rightarrow$, \Rightarrow, \textbf)
const preprocessLatex = (text: string): string => {
  if (!text) return text;

  // Split by code blocks / inline code to preserve code snippets
  const parts = text.split(/(```[\s\S]*?```|`[^`]+`)/g);

  const latexSymbols: [RegExp, string][] = [
    [/\\rightarrow\b/g, '→'],
    [/\\to\b/g, '→'],
    [/\\leftarrow\b/g, '←'],
    [/\\Rightarrow\b/g, '⇒'],
    [/\\Leftarrow\b/g, '⇐'],
    [/\\leftrightarrow\b/g, '↔'],
    [/\\Leftrightarrow\b/g, '⇔'],
    [/\\uparrow\b/g, '↑'],
    [/\\downarrow\b/g, '↓'],
    [/\\leq?\b/g, '≤'],
    [/\\geq?\b/g, '≥'],
    [/\\neq\b/g, '≠'],
    [/\\approx\b/g, '≈'],
    [/\\cdot\b/g, '·'],
    [/\\times\b/g, '×'],
    [/\\pm\b/g, '±'],
    [/\\infty\b/g, '∞'],
    [/\\checkmark\b/g, '✓'],
    [/\\degree\b/g, '°'],
    [/\\alpha\b/g, 'α'],
    [/\\beta\b/g, 'β'],
    [/\\gamma\b/g, 'γ'],
    [/\\delta\b/g, 'δ'],
    [/\\epsilon\b/g, 'ε'],
    [/\\theta\b/g, 'θ'],
    [/\\lambda\b/g, 'λ'],
    [/\\mu\b/g, 'μ'],
    [/\\pi\b/g, 'π'],
    [/\\sigma\b/g, 'σ'],
    [/\\tau\b/g, 'τ'],
    [/\\phi\b/g, 'φ'],
    [/\\omega\b/g, 'ω'],
    [/\\Delta\b/g, 'Δ'],
    [/\\Sigma\b/g, 'Σ'],
    [/\\Omega\b/g, 'Ω'],
    [/\\bullet\b/g, '•'],
    [/\\dots\b/g, '…'],
    [/\\ldots\b/g, '…'],
  ];

  const processed = parts.map((part, index) => {
    if (index % 2 === 1) return part; // Keep code blocks & inline code as-is

    let t = part;

    // Convert LaTeX text formatting commands
    t = t.replace(/\\textbf\{([^}]+)\}/g, '**$1**');
    t = t.replace(/\\textit\{([^}]+)\}/g, '*$1*');
    t = t.replace(/\\text\{([^}]+)\}/g, '$1');

    // Convert LaTeX symbol commands to Unicode equivalents
    for (const [regex, replacement] of latexSymbols) {
      t = t.replace(regex, replacement);
    }

    // Unwrap $...$ surrounding converted single symbols, arrows, or clean text expressions
    t = t.replace(/\$\s*([→←⇒⇐↔⇔↑↓≤≥≠≈·×±∞✓°αβγδεθλμπστφωΔΣΩ•…\w\s+\-=/\(\)]+?)\s*\$/g, (match, inner) => {
      if (!inner.includes('\\')) {
        return inner;
      }
      return match;
    });

    // Clean up leftover math block/inline delimiters \(...\) or \[...\]
    t = t.replace(/\\\(\s*(.*?)\s*\\\)/g, '$1');
    t = t.replace(/\\\[\s*(.*?)\s*\\\]/g, '$1');

    return t;
  });

  return processed.join('');
};

// High-performance LRU cache for rendered Markdown to eliminate re-parsing overhead during fast token streams
const markdownCache = new Map<string, { __html: string }>();
const MAX_MARKDOWN_CACHE_SIZE = 300;

const renderMarkdown = (text: string) => {
  if (markdownCache.has(text)) {
    return markdownCache.get(text)!;
  }
  try {
    const cleanText = preprocessLatex(text);
    const rawHtml = marked.parse(cleanText, { breaks: true, gfm: true }) as string;
    const cleanHtml = DOMPurify.sanitize(rawHtml);
    const result = { __html: cleanHtml };
    if (markdownCache.size >= MAX_MARKDOWN_CACHE_SIZE) {
      const firstKey = markdownCache.keys().next().value;
      if (firstKey !== undefined) markdownCache.delete(firstKey);
    }
    markdownCache.set(text, result);
    return result;
  } catch (e) {
    console.error("Markdown parse error:", e);
    return { __html: text };
  }
};

interface TimelineProps {
  onThoughtsUpdate: (feed: { thoughts: string[]; streaming: boolean }) => void;
}

// Helper to classify thought step type
const getThoughtMeta = (text: string) => {
  const t = text.toUpperCase();
  if (t.includes('[PLANNING]') || t.includes('PLANNING')) {
    return { label: 'PLAN', color: '#6366f1', bg: 'rgba(99, 102, 241, 0.15)' };
  }
  if (t.includes('[EXEC]') || t.includes('EXECUTING') || t.includes('<CALL:')) {
    return { label: 'EXEC', color: '#f59e0b', bg: 'rgba(245, 158, 11, 0.15)' };
  }
  if (t.includes('[OBSERVATION]') || t.includes('OBSERVATION') || t.includes('<OBSERVATION>')) {
    return { label: 'OBSERVE', color: '#10b981', bg: 'rgba(16, 185, 129, 0.15)' };
  }
  if (t.includes('[STATUS]')) {
    return { label: 'STATUS', color: '#8b5cf6', bg: 'rgba(139, 92, 246, 0.15)' };
  }
  if (t.includes('[WARNING]') || t.includes('ERROR:')) {
    return { label: 'WARN', color: '#ef4444', bg: 'rgba(239, 68, 68, 0.15)' };
  }
  return { label: 'STEP', color: 'var(--accent)', bg: 'color-mix(in srgb, var(--accent) 15%, transparent)' };
};

// Collapsible ReAct thoughts & step accordions
const ThoughtsBlock = React.memo(function ThoughtsBlock({ thoughts }: { thoughts: string[] }) {
  const [open, setOpen] = useState(false);
  return (
    <div style={{
      margin: '6px 0',
      border: '1px solid var(--border-subtle)',
      borderRadius: 'var(--radius-sm)',
      overflow: 'hidden',
      background: 'rgba(0, 0, 0, 0.2)'
    }}>
      <button
        type="button"
        onClick={() => setOpen(v => !v)}
        style={{
          width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between',
          padding: '6px 10px', background: 'none', border: 'none', cursor: 'pointer',
          color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", fontSize: 10, fontWeight: 600,
        }}
      >
        <span style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <motion.span animate={{ rotate: open ? 90 : 0 }} transition={{ duration: 0.15 }} style={{ display: 'inline-flex' }}>
            <ChevronRight size={11} />
          </motion.span>
          ReAct Reasoning Loop ({thoughts.length} steps)
        </span>
        <span style={{ fontSize: 9, opacity: 0.7, color: 'var(--text-dim)' }}>
          {open ? 'Collapse' : 'Expand'}
        </span>
      </button>
      <AnimatePresence initial={false}>
        {open && (
          <motion.div
            initial={{ height: 0 }} animate={{ height: 'auto' }} exit={{ height: 0 }}
            transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
            style={{ overflow: 'hidden' }}
          >
            <div style={{
              margin: 0, padding: '6px 10px 8px 10px', borderTop: '1px solid var(--border-subtle)',
              display: 'flex', flexDirection: 'column', gap: 6,
            }}>
              {thoughts.map((t, i) => {
                const meta = getThoughtMeta(t);
                return (
                  <div key={i} style={{
                    display: 'flex',
                    alignItems: 'flex-start',
                    gap: 8,
                    fontSize: 11,
                    color: 'var(--text-dim)',
                    fontFamily: "'JetBrains Mono', monospace",
                    lineHeight: 1.5,
                    wordBreak: 'break-word',
                    overflowWrap: 'anywhere',
                    whiteSpace: 'pre-wrap',
                    padding: '4px 6px',
                    borderRadius: '4px',
                    background: 'rgba(255, 255, 255, 0.02)'
                  }}>
                    <span style={{
                      display: 'inline-block',
                      padding: '1px 5px',
                      borderRadius: '3px',
                      fontSize: '9px',
                      fontWeight: 700,
                      color: meta.color,
                      background: meta.bg,
                      flexShrink: 0,
                      marginTop: 1
                    }}>
                      {meta.label} #{i + 1}
                    </span>
                    <span style={{ flex: 1 }}>{preprocessLatex(t)}</span>
                  </div>
                );
              })}
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
});

// MessageBody that renders markdown + syntax-highlighted diffs
const MessageBody = React.memo(function MessageBody({ content }: { content: string }) {
  if (!content) return null;

  // Detect ```diff ... ``` or ```patch ... ``` blocks
  const diffRegex = /```(?:diff|patch)\n([\s\S]*?)```/g;
  if (!diffRegex.test(content)) {
    return (
      <div
        className="markdown-content"
        style={{ fontSize: 13, color: 'var(--text-main)', margin: 0, lineHeight: 1.6 }}
        dangerouslySetInnerHTML={renderMarkdown(content)}
      />
    );
  }

  diffRegex.lastIndex = 0;
  const segments: React.ReactNode[] = [];
  let lastIndex = 0;
  let match: RegExpExecArray | null;

  while ((match = diffRegex.exec(content)) !== null) {
    const textBefore = content.substring(lastIndex, match.index);
    if (textBefore.trim()) {
      segments.push(
        <div
          key={`md-${lastIndex}`}
          className="markdown-content"
          style={{ fontSize: 13, color: 'var(--text-main)', margin: 0, lineHeight: 1.6 }}
          dangerouslySetInnerHTML={renderMarkdown(textBefore)}
        />
      );
    }
    const diffCode = match[1];
    segments.push(
      <CodeDiffViewer key={`diff-${match.index}`} diffText={diffCode} />
    );
    lastIndex = diffRegex.lastIndex;
  }

  const textAfter = content.substring(lastIndex);
  if (textAfter.trim()) {
    segments.push(
      <div
        key={`md-${lastIndex}`}
        className="markdown-content"
        style={{ fontSize: 13, color: 'var(--text-main)', margin: 0, lineHeight: 1.6 }}
        dangerouslySetInnerHTML={renderMarkdown(textAfter)}
      />
    );
  }

  return <div>{segments}</div>;
});


// Removed BrowserLiveHUD
/*
  const [active, setActive] = useState(false);
  const [open, setOpen] = useState(true);

  useEffect(() => {
    let interval: any;
    const checkFrame = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/browser/frame`);
        if (res.ok) {
          const data = await res.json();
          if (data.frame) {
            setFrame(data.frame);
            setActive(!!data.active);
          }
        }
      } catch {}
    };

    checkFrame();
    interval = setInterval(checkFrame, 3000);
    return () => clearInterval(interval);
  }, []);

  if (!frame) return null;

  return (
    <div style={{
      margin: '8px 0',
      borderRadius: '8px',
      border: '1px solid var(--border-subtle)',
      background: 'rgba(12, 14, 20, 0.85)',
      overflow: 'hidden'
    }}>
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '5px 10px',
        background: 'rgba(255, 255, 255, 0.03)',
        borderBottom: open ? '1px solid var(--border-subtle)' : 'none',
        fontSize: '11px',
        color: 'var(--text-main)'
      }}>
        <button
          type="button"
          onClick={() => setOpen(v => !v)}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: 6,
            background: 'none',
            border: 'none',
            color: 'var(--accent)',
            cursor: 'pointer',
            padding: 0,
            fontWeight: 600,
            fontSize: '11px'
          }}
        >
          {open ? <ChevronDown size={12} /> : <ChevronRight size={12} />}
          <span>Autonomous Browser Viewport</span>
          {active && (
            <span style={{
              display: 'inline-block',
              width: 6,
              height: 6,
              borderRadius: '50%',
              background: '#10b981',
              boxShadow: '0 0 6px #10b981'
            }} />
          )}
        </button>
      </div>
      {open && (
        <div style={{ padding: '6px', textAlign: 'center', background: '#000' }}>
          <img
            src={frame}
            alt="Browser Viewport"
            style={{
              maxWidth: '100%',
              maxHeight: '260px',
              borderRadius: '4px',
              objectFit: 'contain',
              display: 'block',
              margin: '0 auto'
            }}
          />
        </div>
      )}
    </div>
  );
});

*/

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
        <div style={{ background: 'var(--bg-panel)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', border: '1px solid var(--border-subtle)' }}>
          <p style={{ fontSize: 9, color: 'var(--danger)', fontFamily: 'JetBrains Mono', marginBottom: 4, fontWeight: 600 }}>ORIGINAL</p>
          <pre style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', margin: 0, whiteSpace: 'pre-wrap', wordBreak: 'break-all', maxHeight: 120, overflow: 'auto' }}>
            {heal.original_code || heal.original}
          </pre>
        </div>
        <div style={{ background: 'var(--bg-panel)', borderRadius: 'var(--radius-sm)', padding: '6px 8px', border: '1px solid var(--border-subtle)' }}>
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

interface StarterItem {
  icon: string;
  title: string;
  desc: string;
  prompt: string;
  tag?: string;
}

interface StarterCategory {
  title: string;
  badge: string;
  color: string;
  items: StarterItem[];
}

const STARTER_CATEGORIES: StarterCategory[] = [
  {
    title: 'Code & Architecture',
    badge: 'DEV',
    color: '#00f0ff',
    items: [
      {
        icon: '⚡',
        title: 'Workspace Quick Audit',
        desc: 'Review staged diffs, branch status & repository hygiene',
        prompt: 'Run workspace quick audit to inspect repository status, recent diffs, and health.',
        tag: 'GIT'
      },
      {
        icon: '🩺',
        title: 'System Pre-Flight Doctor',
        desc: 'Verify Python ML, ports, database WAL, and AI models',
        prompt: 'Run system doctor diagnostics and verify environment health.',
        tag: 'DOCTOR'
      }
    ]
  },
  {
    title: 'Vision & Perception',
    badge: 'MULTIMODAL',
    color: '#a855f7',
    items: [
      {
        icon: '👁️',
        title: 'Explain Active Screen',
        desc: 'Diagnose current editor, browser, or terminal output',
        prompt: 'Explain what is on my active screen right now and diagnose any errors or next steps.',
        tag: 'OCR'
      },
      {
        icon: '📋',
        title: 'Transform Clipboard',
        desc: 'Format messy stack traces, JSON, or code in clipboard',
        prompt: 'Inspect my clipboard content and format or diagnose it.',
        tag: 'CLIPBOARD'
      }
    ]
  },
  {
    title: 'Autonomous Swarm',
    badge: 'MULTI-AGENT',
    color: '#34d399',
    items: [
      {
        icon: '🤖',
        title: 'Multi-Agent Consensus Debate',
        desc: 'Engage 3 rival personas to evaluate engineering trade-offs',
        prompt: 'Start a multi-agent debate to evaluate architecture options for this project.',
        tag: 'CONSENSUS'
      },
      {
        icon: '🧠',
        title: 'Reflexion & Learned Rules',
        desc: 'Query persistent memory graph and user constraints',
        prompt: 'Search memory for recent learned rules, user preferences, and tasks.',
        tag: 'MEMORY'
      }
    ]
  }
];

const STARTER_PROMPTS = STARTER_CATEGORIES.flatMap(c => c.items);

export default function Timeline({ onThoughtsUpdate }: TimelineProps) {
  const [messages, setMessages] = useState<any[]>([{
    id: 'init', role: 'assistant', timestamp: Date.now(),
    content: 'System loaded. Standing by for autonomous instructions.',
  }]);
  const [input, setInput] = useState('');
  const [isInputFocused, setIsInputFocused] = useState(false);
  const [loading, setLoading] = useState(false);
  const [streaming, setStreaming] = useState('');
  const [streamThoughts, setStreamThoughts] = useState<string[]>([]);
  // Windowed rendering: cap DOM nodes for long histories (perf).
  const [visibleMsgCount, setVisibleMsgCount] = useState(100);
  const visibleMessages = messages.length > visibleMsgCount
    ? messages.slice(messages.length - visibleMsgCount)
    : messages;
  const hiddenMsgCount = messages.length - visibleMessages.length;
  const [dragActive, setDragActive] = useState(false);
  const chatEndRef = useRef<HTMLDivElement>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);
  const abortControllerRef = useRef<AbortController | null>(null);
  const [ttsEnabled, setTtsEnabled] = useState(() => localStorage.getItem('meridian_dashboard_tts') === 'true');
  const [taskQueue, setTaskQueue] = useState<{ id: number; text: string }[]>([]);
  const [stagedFile, setStagedFile] = useState<File | null>(null);
  const [copiedMsgId, setCopiedMsgId] = useState<string | number | null>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const generationIdRef = useRef(0);

  const stopActiveAudio = () => {
    generationIdRef.current++;
    streamingAudio.stopAllAudio();
  };

  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 120)}px`;
    }
  }, [input]);

  const speakMessage = async (text: string) => {
    if (!text.trim()) return;
    streamingAudio.resetSession();
    streamingAudio.dispatchImmediateText(text);
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
        if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__) {
          invoke('open_url', { url: href }).catch(err => {
            console.error("Failed to open URL externally:", err);
          });
        } else {
          window.open(href, '_blank', 'noopener,noreferrer');
        }
      }
    }
  };

  const clearChat = async () => {
    stopActiveAudio();
    if (abortControllerRef.current) {
      try { abortControllerRef.current.abort(); } catch { /* noop */ }
      abortControllerRef.current = null;
    }
    setLoading(false);
    setStreaming('');
    setStreamThoughts([]);
    try { await fetch(`${API_BASE_URL}/api/chat/clear`, { method: 'POST' }); } catch { /* noop */ }
    setMessages([]);
  };

  // The backend wraps final responses as {"chat":"...","speech":"...","lang":"..."}
  const deduplicateContent = (text: string): string => {
    const trimmed = text.trim();
    if (!trimmed) return text;
    const len = trimmed.length;
    if (len >= 20 && len % 2 === 0) {
      const half = len / 2;
      if (trimmed.slice(0, half) === trimmed.slice(half)) {
        return trimmed.slice(0, half);
      }
    }
    return trimmed;
  };

  // This extracts just the human-readable chat portion from that wrapper.
  const extractChatText = (raw: string): string => {
    const trimmed = raw.trim();
    if (trimmed.startsWith('{') || trimmed.startsWith('[')) {
      try {
        const parsed = JSON.parse(trimmed);
        if (parsed.type === 'error' || parsed.error) {
          return `\n✕ Error: ${parsed.error || parsed.message || parsed.detail || 'Execution failed'}`;
        }
        if (parsed.chat) return parsed.chat;
        if (parsed.text) return parsed.text;
        if (parsed.proactive_suggestions && Array.isArray(parsed.proactive_suggestions) && parsed.proactive_suggestions.length > 0) {
          const first = parsed.proactive_suggestions[0];
          return `Task processed. Recommended next step: ${first.title || first}.`;
        }
        if (parsed.title) {
          return `Suggested follow-up: ${parsed.title}.`;
        }
      } catch {
        // Not clean JSON - check if it is a leaked internal JSON dump or bracket fragment
        const titleMatch = trimmed.match(/"title"\s*:\s*"([^"]+)"/);
        if (titleMatch) {
          return `Task processed. Recommended next step: ${titleMatch[1]}.`;
        }
      }
    }
    return raw;
  };

  const executeTask = async (text: string) => {
    setLoading(true);
    setStreaming('');
    setStreamThoughts([]);

    if ((window as any).__TAURI_INTERNALS__) {
      await emit('agent-status-update', {
        isRunning: true,
        latestThought: { text: 'Initializing agent...', type: 'planning' },
        thoughts: [],
        timestamp: Date.now()
      }).catch(console.error);
    }

    const controller = new AbortController();
    abortControllerRef.current = controller;

    const provider = localStorage.getItem('MERIDIAN_PROVIDER') || localStorage.getItem('meridian_provider') || 'ollama';
    const brainModel = localStorage.getItem('MERIDIAN_MODEL') || localStorage.getItem('meridian_model') || '';
    const configuredSource = localStorage.getItem('meridian_model_source') || localStorage.getItem('MERIDIAN_MODEL_SOURCE');
    const modelSource = configuredSource || (provider === 'ollama' ? 'local' : 'cloud');

    const openaiKey = localStorage.getItem('OPENAI_API_KEY') || '';
    const anthropicKey = localStorage.getItem('ANTHROPIC_API_KEY') || '';
    const geminiKey = localStorage.getItem('GEMINI_API_KEY') || '';
    const deepseekKey = localStorage.getItem('DEEPSEEK_API_KEY') || '';

    try {
      const res = await fetch(`${API_BASE_URL}/api/chat/stream`, {
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

      const currentGen = ++generationIdRef.current;
      stopActiveAudio();
      if (ttsEnabled) {
        streamingAudio.resetSession();
      }

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
              const thoughtText = thoughtData.text !== undefined ? String(thoughtData.text) :
                                  thoughtData.thought !== undefined ? String(thoughtData.thought) :
                                  String(thoughtData);
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
                await emit('agent-status-update', {
                  isRunning: true,
                  latestThought: thoughtData,
                  thoughts: updatedThoughts,
                  timestamp: Date.now()
                }).catch(console.error);
              }
            } catch { /* non-JSON thought, skip */ }
          } else if (eventType === 'text') {
            // text events carry raw text chunks (not JSON) or the final JSON wrapper
            const trimmedPayload = payload.trim();
            const isJson = trimmedPayload.startsWith('{');
            const chunk = extractChatText(payload);

            if (isJson && chunk) {
              finalContent = chunk;
              if (ttsEnabled) {
                streamingAudio.dispatchImmediateText(chunk, currentGen);
              }
            } else if (chunk && finalContent && (chunk === finalContent || chunk.startsWith(finalContent))) {
              finalContent = chunk;
              if (ttsEnabled) {
                streamingAudio.dispatchImmediateText(chunk, currentGen);
              }
            } else {
              finalContent += chunk;
              if (ttsEnabled && chunk) {
                streamingAudio.feedText(chunk, currentGen);
              }
            }
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
          } else if (eventType === 'error') {
            try {
              const errData = JSON.parse(payload);
              const errMsg = errData.error || errData.message || payload;
              const issueHeader = String(errMsg).split('\n')[0].slice(0, 100);
              finalContent += `\n\n> [!WARNING]\n> ### ⚠️ Main Issue: ${issueHeader}\n> **What Happened**: Execution encountered an issue.\n> **Suggested Action**: Review the details or ask me to diagnose and fix it.\n>\n> <details>\n> <summary>Technical Details</summary>\n>\n> \`\`\`text\n> ${errMsg}\n> \`\`\`\n> </details>\n`;
              setStreaming(finalContent);
            } catch {
              finalContent += `\n\n> [!WARNING]\n> ### ⚠️ Main Issue: Execution Error\n> **What Happened**: ${payload}\n> **Suggested Action**: Check settings or ask me to propose a fix.\n`;
              setStreaming(finalContent);
            }
          }
        }
      }

      if (ttsEnabled) {
        streamingAudio.flush(currentGen);
      }

      // Final: extract chat text from any JSON wrapper and strip duplicate content
      // The backend may stream chunks then send the full text again as final event
      const thoughtsList = finalThoughts.map(t => t.text);
      const cleanedContent = deduplicateContent(extractChatText(finalContent));
      const fallbackText = thoughtsList.length > 0 
        ? 'Operation completed.' 
        : 'No response returned by AI model. Please verify your LLM model selection or API keys in Settings.';
      setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: cleanedContent || fallbackText, thoughts: thoughtsList }]);
      setStreaming('');
      setStreamThoughts([]);
      if ((window as any).__TAURI_INTERNALS__) {
        await emit('agent-status-update', {
          isRunning: false,
          latestThought: { text: 'Task completed', type: 'status' },
          thoughts: [],
          timestamp: Date.now()
        }).catch(console.error);
      }
    } catch (err: any) {
      if (err.name === 'AbortError') {
        setMessages(prev => {
          const lastMsg = prev[prev.length - 1];
          if (lastMsg && typeof lastMsg.content === 'string' && lastMsg.content.includes('stopped by user')) {
            return prev;
          }
          return [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: '⛔ **Execution stopped by user.**' }];
        });
      } else {
        setMessages(prev => [...prev, {
          id: Date.now(),
          role: 'assistant',
          timestamp: Date.now(),
          content: '> [!WARNING]\n> ### ⚠️ Main Issue: Cannot Connect to Meridian Backend (:4132)\n> **What Happened**: The local FastAPI server on port 4132 is not responding or currently restarting.\n> **Why**: The Python backend process is closed, or port 4132 is occupied.\n> **Suggested Fix**: Run `restart_backend.bat` or verify the Python backend is active.'
        }]);
      }
      setStreaming('');
      setStreamThoughts([]);
      if ((window as any).__TAURI_INTERNALS__) {
        await emit('agent-status-update', {
          isRunning: false,
          latestThought: { text: err.name === 'AbortError' ? 'Task interrupted' : 'Task failed', type: 'error' },
          thoughts: [],
          timestamp: Date.now()
        }).catch(console.error);
      }
    } finally {
      abortControllerRef.current = null;
      setLoading(false);
    }
  };

  // FIX: keep a ref to the latest executeTask so the window event listener
  // below never fires with a stale first-render closure (ttsEnabled etc.).
  const executeTaskRef = useRef(executeTask);
  useEffect(() => {
    executeTaskRef.current = executeTask;
  });

  useEffect(() => {
    const handleCustomPrompt = (e: Event) => {
      const customEvt = e as CustomEvent<{ prompt: string }>;
      if (customEvt.detail?.prompt) {
        const text = customEvt.detail.prompt;
        setMessages(prev => [...prev, { id: String(Date.now()), role: 'user', content: text, timestamp: Date.now() }]);
        executeTaskRef.current(text);
      }
    };
    window.addEventListener('meridian:send-chat', handleCustomPrompt);
    return () => window.removeEventListener('meridian:send-chat', handleCustomPrompt);
  }, []);

  useEffect(() => {
    if (!loading && taskQueue.length > 0) {
      const nextTask = taskQueue[0];
      setTaskQueue(prev => prev.slice(1));
      
      executeTask(nextTask.text);
    }
  }, [loading, taskQueue]);

  const onSubmitPrompt = async (e?: React.FormEvent) => {
    e?.preventDefault();
    const text = input.trim();
    if (!text && !stagedFile) return;

    setInput('');
    const fileToUpload = stagedFile;
    if (fileToUpload) {
      setStagedFile(null);
    }

    // Prepare prompt text
    let promptWithAttachment = text;
    if (fileToUpload) {
      promptWithAttachment = `[Attached File: ${fileToUpload.name}] ${text}`.trim();
    }

    // Add user message to UI
    const msgId = Date.now();
    const userMsg = { 
      id: msgId, 
      role: 'user' as const, 
      timestamp: msgId, 
      content: text,
      fileAttachment: fileToUpload ? {
        name: fileToUpload.name,
        status: 'ingesting' as const
      } : undefined
    };
    setMessages(prev => [...prev, userMsg]);

    if (fileToUpload) {
      setLoading(true);
      const fd = new FormData();
      fd.append('file', fileToUpload);
      try {
        const res = await fetch(`${API_BASE_URL}/api/rag/ingest-file-upload`, { 
          method: 'POST', 
          body: fd 
        });
        if (res.ok) {
          // Update the user message file attachment status to 'success'
          setMessages(prev => prev.map(m => m.id === msgId ? { ...m, fileAttachment: { name: fileToUpload.name, status: 'success' as const } } : m));
          // Proceed to execute the task with the agent
          await executeTask(promptWithAttachment);
        } else {
          let errMsg = `Failed to ingest ${fileToUpload.name}.`;
          try {
            const errJson = await res.json();
            if (errJson.detail) errMsg = errJson.detail;
          } catch {}
          // Update the user message file attachment status to 'failed'
          setMessages(prev => prev.map(m => m.id === msgId ? { ...m, fileAttachment: { name: fileToUpload.name, status: 'failed' as const } } : m));
          // Add system feedback message
          setMessages(prev => [...prev, {
            id: Date.now(),
            role: 'assistant' as const,
            timestamp: Date.now(),
            content: `✕ **${fileToUpload.name}** ingestion failed: ${errMsg}`
          }]);
          setLoading(false);
        }
      } catch (err: any) {
        setMessages(prev => prev.map(m => m.id === msgId ? { ...m, fileAttachment: { name: fileToUpload.name, status: 'failed' as const } } : m));
        setMessages(prev => [...prev, {
          id: Date.now(),
          role: 'assistant' as const,
          timestamp: Date.now(),
          content: `✕ Error reaching RAG backend for **${fileToUpload.name}**: ${err.message || err}`
        }]);
        setLoading(false);
      }
    } else {
      if (loading) {
        setTaskQueue(prev => [...prev, { id: Date.now(), text }]);
      } else {
        executeTask(text);
      }
    }
  };

  const handleInterrupt = async () => {
    stopActiveAudio();
    setTaskQueue([]);
    if (abortControllerRef.current) {
      try {
        abortControllerRef.current.abort();
      } catch {}
      abortControllerRef.current = null;
    }
    setLoading(false);
    setStreaming('');
    setStreamThoughts([]);
    setMessages(prev => [...prev, {
      id: Date.now(),
      role: 'assistant',
      timestamp: Date.now(),
      content: '⛔ **Execution stopped by user.**',
    }]);
    try {
      await fetch(`${API_BASE_URL}/api/chat/abort`, { method: 'POST' });
    } catch {}
    try {
      await fetch(`${API_BASE_URL}/api/voice/interrupt`, { method: 'POST' });
    } catch (e) {
      console.warn("Failed to send interrupt request:", e);
    }
    if ((window as any).__TAURI_INTERNALS__) {
      await emit('agent-status-update', {
        isRunning: false,
        latestThought: { text: 'Stopped by user', type: 'status' },
        thoughts: [],
        timestamp: Date.now()
      }).catch(console.error);
    }
  };

  const handleConfirm = async (id: string, approved: boolean) => {
    try {
      await fetch(`${API_BASE_URL}/api/chat/confirm`, {
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
      await fetch(`${API_BASE_URL}/api/watcher/apply-heal`, {
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
    if (file) {
      setStagedFile(file);
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
          <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: 'var(--font-heading)' }}>Timeline Logs</h1>
          <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Execution audit · ReAct thought stream</p>
        </div>

        <div style={{ display: 'flex', gap: 8 }}>
          <button
            type="button"
            onClick={async () => {
              try {
                const res = await fetch(`${API_BASE_URL}/api/action/undo`, {
                  method: 'POST',
                  headers: { 'Content-Type': 'application/json' },
                  body: JSON.stringify({})
                });
                if (res.ok) {
                  const data = await res.json();
                  setMessages(prev => [...prev, {
                    id: Date.now(),
                    role: 'assistant',
                    timestamp: Date.now(),
                    content: data.success ? `↺ **Undo Executed:** ${data.message}` : `✕ **Undo Warning:** ${data.message}`
                  }]);
                }
              } catch (err: any) {
                setMessages(prev => [...prev, { id: Date.now(), role: 'assistant', timestamp: Date.now(), content: `✕ **Undo Failed:** ${err.message || 'Server unreachable'}` }]);
              }
            }}
            style={{
              display: 'flex', alignItems: 'center', gap: 6, padding: '4px 10px', borderRadius: 'var(--radius-sm)',
              background: 'color-mix(in srgb, var(--warning) 12%, transparent)', border: '1px solid var(--warning)',
              color: 'var(--warning)', cursor: 'pointer', fontSize: 11, fontWeight: 600
            }}
            title="Undo last reversible action (BUTLER-14)"
          >
            <RotateCcw size={12} /> Undo Last Action
          </button>

          <HoloButton variant="danger" size="sm" onClick={clearChat}>
            <Trash2 size={12} /> Clear
          </HoloButton>
        </div>
      </div>

      {/* Messages */}
      <div
        onClick={handleTimelineClick}
        role="log"
        aria-live="polite"
        aria-label="Conversation messages"
        className="modern-scrollbar"
        style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 12, marginBottom: 12 }}
      >
        <AnimatePresence initial={false}>
          {hiddenMsgCount > 0 && (
            <button
              onClick={() => setVisibleMsgCount(c => c + 100)}
              style={{
                alignSelf: 'center', padding: '4px 12px', borderRadius: 'var(--radius-sm)',
                background: 'transparent', border: '1px solid var(--border)',
                color: 'var(--text-secondary)', cursor: 'pointer', fontSize: 12, fontWeight: 600,
              }}
            >
              Show {Math.min(100, hiddenMsgCount)} earlier messages ({hiddenMsgCount} hidden)
            </button>
          )}
          {visibleMessages.map((msg, i) => {
            const isUser = msg.role === 'user';
            return (
              <React.Fragment key={msg.id ?? i}>
                <motion.div
                  initial={{ opacity: 0, y: 8, scale: 0.98 }}
                  animate={{ opacity: 1, y: 0, scale: 1 }}
                  transition={{ duration: 0.22, ease: [0.16, 1, 0.3, 1] }}
                  style={{
                    display: 'flex',
                    flexDirection: isUser ? 'row-reverse' : 'row',
                    gap: 12,
                    alignItems: 'flex-start',
                    paddingLeft: isUser ? 64 : 0,
                    paddingRight: isUser ? 0 : 64,
                  }}
                >
                  {/* Avatar */}
                  <div style={{
                    width: 34, height: 34, borderRadius: 'var(--radius-md)', flexShrink: 0,
                    background: isUser ? 'color-mix(in srgb, var(--accent-2) 16%, transparent)' : 'color-mix(in srgb, var(--accent) 14%, transparent)',
                    border: `1px solid ${isUser ? 'color-mix(in srgb, var(--accent-2) 35%, transparent)' : 'color-mix(in srgb, var(--accent) 30%, transparent)'}`,
                    display: 'flex', alignItems: 'center', justifyContent: 'center',
                    color: isUser ? 'var(--accent-2)' : 'var(--accent)',
                    boxShadow: '0 2px 8px rgba(0, 0, 0, 0.25)',
                  }}>
                    {isUser ? <User size={16} /> : <Bot size={16} />}
                  </div>

                  {/* Bubble */}
                  <div style={{
                    flex: 1,
                    background: isUser ? 'color-mix(in srgb, var(--accent-2) 8%, var(--bg-surface))' : 'color-mix(in srgb, var(--bg-panel) 94%, transparent)',
                    border: isUser ? '1px solid color-mix(in srgb, var(--accent-2) 25%, transparent)' : '1px solid var(--border)',
                    borderLeft: `3px solid ${isUser ? 'var(--accent-2)' : 'var(--accent)'}`,
                    borderRadius: 'var(--radius-md)',
                    boxShadow: '0 4px 16px rgba(0, 0, 0, 0.25)',
                    padding: '12px 16px',
                  }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                      <span style={{ fontSize: 10, fontWeight: 600, color: isUser ? 'var(--accent-2)' : 'var(--accent)', fontFamily: "var(--font-mono, monospace)", textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                        {isUser ? 'Operator' : 'Meridian-X Core'}
                      </span>
                      <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "var(--font-mono, monospace)" }}>
                        {reltime(msg.timestamp)}
                      {msg.content && (
                        <button
                          type="button"
                          onClick={() => {
                            navigator.clipboard.writeText(msg.content);
                            setCopiedMsgId(msg.id ?? i);
                            setTimeout(() => setCopiedMsgId(null), 1800);
                          }}
                          title="Copy message content"
                          style={{
                            background: 'transparent',
                            border: 'none',
                            color: copiedMsgId === (msg.id ?? i) ? 'var(--success)' : 'var(--text-dim)',
                            cursor: 'pointer',
                            padding: 2,
                            marginLeft: 6,
                            display: 'inline-flex',
                            alignItems: 'center',
                          }}
                        >
                          {copiedMsgId === (msg.id ?? i) ? <Check size={11} /> : <Copy size={11} />}
                        </button>
                      )}
                      </span>
                    </div>

                    {msg.fileAttachment && (
                      <div style={{
                        display: 'flex',
                        alignItems: 'center',
                        gap: 10,
                        padding: '8px 12px',
                        background: 'color-mix(in srgb, var(--accent) 5%, var(--bg-panel))',
                        border: '1px solid color-mix(in srgb, var(--accent) 15%, transparent)',
                        borderRadius: 'var(--radius-sm)',
                        marginBottom: msg.content ? 8 : 0,
                      }}>
                        <Paperclip size={13} style={{ color: 'var(--accent)', flexShrink: 0 }} />
                        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 1 }}>
                          <span style={{ fontSize: 11, fontWeight: 500, color: 'var(--text-main)', fontFamily: "var(--font-mono, monospace)", wordBreak: 'break-all' }}>
                            {msg.fileAttachment.name}
                          </span>
                          <span style={{ fontSize: 9, color: 'var(--text-dim)' }}>
                            {msg.fileAttachment.status === 'ingesting' ? 'Ingesting into Turbovec RAG...' :
                             msg.fileAttachment.status === 'success' ? 'Ready in knowledge base' :
                             'Ingestion failed'}
                          </span>
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', flexShrink: 0 }}>
                          {msg.fileAttachment.status === 'ingesting' && (
                            <motion.div
                              animate={{ rotate: 360 }}
                              transition={{ repeat: Infinity, duration: 1.2, ease: 'linear' }}
                              style={{
                                width: 12, height: 12,
                                border: '2px solid var(--accent)',
                                borderTopColor: 'transparent',
                                borderRadius: '50%'
                              }}
                            />
                          )}
                          {msg.fileAttachment.status === 'success' && (
                            <Check size={13} style={{ color: 'var(--success)' }} />
                          )}
                          {msg.fileAttachment.status === 'failed' && (
                            <X size={13} style={{ color: 'var(--danger)' }} />
                          )}
                        </div>
                      </div>
                    )}

                    {msg.thoughts?.length > 0 && <ThoughtsBlock thoughts={msg.thoughts} />}
                    <MessageBody content={msg.content} />
                    {msg.confirmation && <SafetyGate gate={msg.confirmation} onConfirm={handleConfirm} />}
                    {msg.proposedHeal && <HealBlock heal={msg.proposedHeal} onApply={handleApplyHeal} />}
                  </div>
                </motion.div>

                {/* AI Agent Command Center Hero */}
                {i === 0 && messages.length <= 1 && (
                  <motion.div
                    initial={{ opacity: 0, y: 14 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ duration: 0.35, ease: [0.16, 1, 0.3, 1] }}
                    style={{
                      marginTop: 6,
                      marginBottom: 16,
                      display: 'flex',
                      flexDirection: 'column',
                      gap: 14,
                    }}
                  >
                    {/* Hero Header Card */}
                    <div
                      className="glass-card-premium"
                      style={{
                        padding: '24px 28px',
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        textAlign: 'center',
                        position: 'relative',
                        overflow: 'hidden',
                      }}
                    >
                      <div className="hero-radial-glow" />

                      <div style={{
                        width: 48,
                        height: 48,
                        borderRadius: '50%',
                        background: 'color-mix(in srgb, var(--accent) 15%, transparent)',
                        border: '1.5px solid var(--accent)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        color: 'var(--accent)',
                        marginBottom: 14,
                        boxShadow: '0 0 24px var(--accent-muted)',
                        position: 'relative',
                      }}>
                        <Bot size={24} />
                        <span className="pulse-ring-active" style={{
                          position: 'absolute',
                          inset: -4,
                          borderRadius: '50%',
                          border: '1.5px solid var(--accent)',
                          pointerEvents: 'none',
                        }} />
                      </div>

                      <h2 style={{
                        fontSize: 20,
                        fontWeight: 800,
                        fontFamily: "var(--font-heading, 'Outfit', sans-serif)",
                        color: 'var(--text-bright)',
                        margin: 0,
                        letterSpacing: '-0.02em',
                      }}>
                        Meridian-X Autonomous Control Center
                      </h2>

                      <p style={{
                        fontSize: 12,
                        color: 'var(--text-dim)',
                        maxWidth: 580,
                        margin: '6px 0 16px',
                        lineHeight: 1.6,
                      }}>
                        Full-stack ReAct agent orchestrating local tool execution, active screen vision perception, semantic RAG memory, and multi-agent debate.
                      </p>

                      {/* Live Readiness Pills */}
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8, justifyContent: 'center' }}>
                        <span className="glass-pill" style={{ cursor: 'default' }}>
                          <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--success)' }} />
                          <span>ReAct Core Engine Active</span>
                        </span>
                        <span className="glass-pill" style={{ cursor: 'default' }}>
                          <ShieldCheck size={12} color="var(--accent)" />
                          <span>Safety Gate: Tier 2 Guard</span>
                        </span>
                        <span className="glass-pill" style={{ cursor: 'default' }}>
                          <Cpu size={12} color="#a855f7" />
                          <span>FTS5 SQLite Memory</span>
                        </span>
                        <span className="glass-pill" style={{ cursor: 'default' }}>
                          <Wand2 size={12} color="#34d399" />
                          <span>Dynamic Tool Healing</span>
                        </span>
                      </div>
                    </div>

                    {/* Categorized Capability Starters */}
                    <div style={{
                      display: 'grid',
                      gridTemplateColumns: 'repeat(auto-fit, minmax(230px, 1fr))',
                      gap: 12,
                    }}>
                      {STARTER_CATEGORIES.map((cat, catIdx) => (
                        <div
                          key={catIdx}
                          style={{
                            display: 'flex',
                            flexDirection: 'column',
                            gap: 8,
                            padding: '14px',
                            background: 'color-mix(in srgb, var(--bg-panel) 70%, transparent)',
                            border: '1px solid var(--border-subtle)',
                            borderRadius: 'var(--radius-lg)',
                            backdropFilter: 'blur(12px)',
                          }}
                        >
                          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', paddingBottom: 4 }}>
                            <span style={{ fontSize: 11, fontWeight: 700, color: 'var(--text-bright)', letterSpacing: '0.02em' }}>
                              {cat.title}
                            </span>
                            <span style={{
                              fontSize: 9,
                              fontWeight: 700,
                              color: cat.color,
                              background: `color-mix(in srgb, ${cat.color} 12%, transparent)`,
                              border: `1px solid color-mix(in srgb, ${cat.color} 30%, transparent)`,
                              padding: '1px 6px',
                              borderRadius: 4,
                              fontFamily: 'var(--font-mono, monospace)',
                            }}>
                              {cat.badge}
                            </span>
                          </div>

                          <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                            {cat.items.map((item, itemIdx) => (
                              <button
                                key={itemIdx}
                                type="button"
                                onClick={() => {
                                  setInput(item.prompt);
                                  textareaRef.current?.focus();
                                }}
                                style={{
                                  display: 'flex',
                                  alignItems: 'flex-start',
                                  gap: 8,
                                  padding: '10px 12px',
                                  textAlign: 'left',
                                  background: 'var(--bg-surface)',
                                  border: '1px solid var(--border-subtle)',
                                  borderRadius: 'var(--radius-md)',
                                  cursor: 'pointer',
                                  transition: 'all 0.18s cubic-bezier(0.16, 1, 0.3, 1)',
                                }}
                                onMouseEnter={e => {
                                  e.currentTarget.style.borderColor = `color-mix(in srgb, ${cat.color} 40%, transparent)`;
                                  e.currentTarget.style.transform = 'translateY(-1px)';
                                  e.currentTarget.style.boxShadow = '0 4px 14px rgba(0, 0, 0, 0.3)';
                                }}
                                onMouseLeave={e => {
                                  e.currentTarget.style.borderColor = 'var(--border-subtle)';
                                  e.currentTarget.style.transform = 'none';
                                  e.currentTarget.style.boxShadow = 'none';
                                }}
                              >
                                <span style={{ fontSize: 16, lineHeight: 1.2 }}>{item.icon}</span>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 2, flex: 1, overflow: 'hidden' }}>
                                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                                    <span style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)' }}>
                                      {item.title}
                                    </span>
                                  </div>
                                  <span style={{ fontSize: 10, color: 'var(--text-dim)', lineHeight: 1.4 }}>
                                    {item.desc}
                                  </span>
                                </div>
                              </button>
                            ))}
                          </div>
                        </div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </React.Fragment>
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
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: streamThoughts.length > 0 ? 6 : 0 }}>
                <span style={{ fontSize: 10, fontWeight: 600, color: 'var(--accent)', fontFamily: "var(--font-mono, monospace)", display: 'flex', alignItems: 'center', gap: 6 }}>
                  <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--accent)', display: 'inline-block', opacity: 0.85 }} />
                  {streaming ? 'GENERATING RESPONSE...' : 'REASONING & THINKING...'}
                </span>
                {streamThoughts.length > 0 && (
                  <span style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "var(--font-mono, monospace)" }}>
                    Step {streamThoughts.length}
                  </span>
                )}
              </div>

              {streamThoughts.length > 0 && (
                <div style={{
                  padding: '6px 10px',
                  background: 'color-mix(in srgb, var(--accent) 5%, var(--bg-surface))',
                  border: '1px solid color-mix(in srgb, var(--accent) 15%, transparent)',
                  borderRadius: 'var(--radius-xs)',
                  fontSize: 11,
                  fontFamily: "var(--font-mono, monospace)",
                  color: 'var(--text-dim)',
                  lineHeight: 1.5,
                  maxHeight: 120,
                  overflowY: 'auto',
                  whiteSpace: 'pre-wrap',
                  marginBottom: streaming ? 8 : 0,
                }}>
                  {streamThoughts[streamThoughts.length - 1]}
                </div>
              )}

              {streaming && (
                <MessageBody content={streaming} />
              )}
            </div>
          </motion.div>
        )}


        <div ref={chatEndRef} />
      </div>

      {taskQueue.length > 0 && (
        <div style={{
          display: 'flex',
          gap: 8,
          alignItems: 'center',
          padding: '8px 12px',
          background: 'color-mix(in srgb, var(--warning) 8%, var(--bg-panel))',
          border: '1px dashed color-mix(in srgb, var(--warning) 30%, transparent)',
          borderRadius: 'var(--radius-sm)',
          marginBottom: 8,
          fontSize: 11,
          color: 'var(--text-dim)',
          fontFamily: 'var(--font-main)'
        }}>
          <span style={{ color: 'var(--warning)', fontWeight: 600 }}>Queued Tasks ({taskQueue.length}):</span>
          <div style={{ display: 'flex', gap: 6, overflowX: 'auto', flex: 1 }}>
            {taskQueue.map((task, idx) => (
              <span key={task.id} style={{
                background: 'var(--bg-surface)',
                padding: '2px 6px',
                borderRadius: 'var(--radius-xs)',
                whiteSpace: 'nowrap',
                border: '1px solid var(--border-subtle)'
              }}>
                #{idx + 1}: "{task.text.slice(0, 30)}..."
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Elevated Quick Action Floating Bar */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        gap: 8,
        overflowX: 'auto',
        padding: '3px 2px',
        marginBottom: 6,
        scrollbarWidth: 'none',
      }}>
        {[
          { label: 'Explain Active Screen', icon: Eye, color: '#00f0ff', prompt: 'Explain what is on my active screen right now and diagnose any errors or next steps.' },
          { label: 'Git Quick Audit', icon: GitBranch, color: '#34d399', prompt: 'Run workspace quick audit to inspect repository status, recent diffs, and health.' },
          { label: 'Transform Clipboard', icon: ClipboardCopy, color: '#fbbf24', prompt: 'Inspect my clipboard content and format or diagnose it.' },
          { label: 'System Doctor', icon: ShieldCheck, color: '#818cf8', prompt: 'Run system doctor diagnostics and verify environment health.' },
          { label: 'Swarm Debate', icon: Bot, color: '#f472b6', prompt: 'Start a multi-agent debate to evaluate architecture options for this project.' },
        ].map(({ label, icon: ActionIcon, color, prompt }, actIdx) => (
          <button
            key={actIdx}
            type="button"
            onClick={() => {
              setInput(prompt);
              textareaRef.current?.focus();
            }}
            className="glass-pill"
            style={{
              padding: '4px 11px',
              fontSize: '11px',
              background: `color-mix(in srgb, ${color} 10%, rgba(20, 24, 35, 0.75))`,
              borderColor: `color-mix(in srgb, ${color} 28%, transparent)`,
              color: color,
            }}
            onMouseEnter={e => {
              e.currentTarget.style.background = `color-mix(in srgb, ${color} 20%, rgba(20, 24, 35, 0.85))`;
              e.currentTarget.style.borderColor = `color-mix(in srgb, ${color} 50%, transparent)`;
              e.currentTarget.style.boxShadow = `0 0 12px color-mix(in srgb, ${color} 25%, transparent)`;
            }}
            onMouseLeave={e => {
              e.currentTarget.style.background = `color-mix(in srgb, ${color} 10%, rgba(20, 24, 35, 0.75))`;
              e.currentTarget.style.borderColor = `color-mix(in srgb, ${color} 28%, transparent)`;
              e.currentTarget.style.boxShadow = 'none';
            }}
          >
            <ActionIcon size={12} />
            <span>{label}</span>
          </button>
        ))}
      </div>

      {/* Input HUD */}
      <form onSubmit={onSubmitPrompt} style={{
        display: 'flex', flexDirection: 'column', gap: 8, flexShrink: 0,
        background: 'color-mix(in srgb, var(--bg-panel) 94%, transparent)',
        border: isInputFocused ? '1px solid var(--border-active)' : '1px solid var(--border)',
        boxShadow: isInputFocused ? '0 0 24px var(--accent-muted), 0 8px 32px rgba(0, 0, 0, 0.45)' : '0 4px 20px rgba(0, 0, 0, 0.3)',
        borderRadius: 'var(--radius-lg)', padding: '10px 14px',
        backdropFilter: 'blur(16px)',
        WebkitBackdropFilter: 'blur(16px)',
        transition: 'border-color 0.2s ease, box-shadow 0.2s ease',
      }}>
        {stagedFile && (
          <div style={{
            display: 'flex', alignItems: 'center', gap: 8,
            background: 'rgba(255, 255, 255, 0.05)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-sm)',
            padding: '4px 8px',
            alignSelf: 'flex-start',
            fontSize: 11,
            color: 'var(--text-main)',
            fontFamily: "var(--font-mono, monospace)",
          }}>
            <Paperclip size={12} style={{ color: 'var(--accent)' }} />
            <span style={{ maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
              {stagedFile.name}
            </span>
            <button
              type="button"
              onClick={() => setStagedFile(null)}
              title="Remove file"
              style={{
                background: 'none', border: 'none', cursor: 'pointer',
                color: 'var(--text-dim)', padding: 2, display: 'flex',
                alignItems: 'center', justifyContent: 'center',
                transition: 'color 0.15s ease'
              }}
              onMouseEnter={e => e.currentTarget.style.color = 'var(--danger)'}
              onMouseLeave={e => e.currentTarget.style.color = 'var(--text-dim)'}
            >
              <X size={12} />
            </button>
          </div>
        )}
        <div style={{ display: 'flex', gap: 8, alignItems: 'center', width: '100%' }}>
          <input
            ref={fileInputRef}
            type="file"
            style={{ display: 'none' }}
            onChange={e => {
              const file = e.target.files?.[0];
              if (file) {
                setStagedFile(file);
              }
              e.target.value = '';
            }}
          />
          <button type="button" onClick={() => fileInputRef.current?.click()}
            title="Attach file for RAG ingestion"
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 4, display: 'flex', flexShrink: 0 }}
          >
            <Paperclip size={16} />
          </button>
          <textarea
            ref={textareaRef}
            value={input}
            onChange={e => setInput(e.target.value)}
            onFocus={() => setIsInputFocused(true)}
            onBlur={() => setIsInputFocused(false)}
            onKeyDown={e => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                onSubmitPrompt();
              }
            }}
            placeholder="Ask Meridian-X to perform actions or analyze targets..."
            rows={1}
            style={{
              flex: 1, background: 'transparent', border: 'none', outline: 'none',
              color: 'var(--text-main)', fontSize: 13, fontFamily: 'var(--font-main)',
              resize: 'none', maxHeight: 120, minHeight: 24, paddingTop: 4, paddingBottom: 4,
              lineHeight: '1.5', overflowY: 'auto'
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
          {loading && (
            <HoloButton type="button" variant="danger" size="sm" onClick={handleInterrupt} title="Interrupt Current Task">
              <Square size={14} fill="currentColor" />
            </HoloButton>
          )}
          <HoloButton type="submit" variant="primary" size="sm" disabled={!input.trim() && !stagedFile} title="Send Task">
            <Send size={14} />
          </HoloButton>
        </div>
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          marginTop: 2,
          paddingTop: 6,
          borderTop: '1px solid var(--border-subtle)',
          fontSize: 10,
          color: 'var(--text-ghost)',
          fontFamily: "var(--font-mono, monospace)"
        }}>
          <div style={{ display: 'flex', gap: 12 }}>
            <span><strong style={{ color: 'var(--text-dim)' }}>↵ Enter</strong> send</span>
            <span><strong style={{ color: 'var(--text-dim)' }}>⇧ ↵</strong> newline</span>
            <span><strong style={{ color: 'var(--text-dim)' }}>⌘ / Ctrl+K</strong> palette</span>
          </div>
          <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
            <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--success)', boxShadow: '0 0 6px var(--success)' }} />
            <span style={{ color: 'var(--text-dim)' }}>Autonomous Agent Ready</span>
          </div>
        </div>
      </form>
    </div>
  );
}
