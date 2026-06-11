/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { 
  Terminal, 
  Settings, 
  Trash2, 
  Mic, 
  MicOff, 
  Send, 
  Square, 
  Cpu, 
  Database,
  CheckCircle2, 
  AlertCircle, 
  Loader2, 
  Command, 
  Sparkles, 
  Activity,
  CornerDownLeft,
  Settings2,
  Maximize2,
  Minimize2,
  ChevronDown,
  X,
  Minus,
  Search,
  RefreshCw,
  Crown,
  Link,
  Share2,
  Clock,
  MessageSquare,
  Trophy,
  BookOpen,
  Shirt,
  Clipboard,
  Code,
  Briefcase
} from 'lucide-react';
import { Message, ThoughtStep, ModelSettings, SystemResource, ProactiveNudge } from './types';

import { listen, emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { getCurrentWindow } from '@tauri-apps/api/window';
import { WebviewWindow } from '@tauri-apps/api/webviewWindow';
import { marked } from 'marked';
import { MascotCharacter } from './Mascot';

const API_PROVIDERS = [
  { id: 'gemini', name: 'Gemini' },
  { id: 'openai', name: 'ChatGPT' },
  { id: 'anthropic', name: 'Claude' },
  { id: 'deepseek', name: 'DeepSeek' }
];

const PROVIDER_MODELS: Record<string, string[]> = {
  gemini: [
    'gemini-3.5-flash',
    'gemini-2.5-pro',
    'gemini-2.0-flash-exp',
    'gemini-1.5-pro'
  ],
  openai: [
    'gpt-4o',
    'gpt-4o-mini',
    'o1-mini',
    'gpt-3.5-turbo'
  ],
  anthropic: [
    'claude-3-5-sonnet-latest',
    'claude-3-5-haiku-latest',
    'claude-3-opus-20240229'
  ],
  deepseek: [
    'deepseek-chat',
    'deepseek-coder'
  ]
};

const LOCAL_BRAIN_MODELS = [
  'Llama-3.1-Instruct-v3',
  'Qwen-2.5-Coder-14B',
  'DeepSeek-Coder-V2-7B',
  'Mistral-Nemo-12B',
  'gemma-2-9b-it'
];

const LOCAL_OCR_MODELS = [
  'Florence-2-large',
  'MiniCPM-V-2.6-Vision',
  'PaddleOCR-v4',
  'Tesseract-OCR'
];

const getSimulatedResponse = (prompt: string, brainModel: string, ocrModel: string) => {
  const normalized = prompt.toLowerCase();
  let text = "";
  let steps: { type: string; text: string; tool?: string; command?: string; status: 'pending' | 'running' | 'completed' | 'failed' }[] = [];

  if (normalized.includes("open") || normalized.includes("start") || normalized.includes("run")) {
    text = "I have successfully launched and positioned the requested program in your viewport. You can see its window handle active in the background environment logs.";
    steps = [
      {
        type: "planning",
        text: "Analyzing desktop space for window placement...",
        tool: "screencapture",
        command: "screencapture -x /tmp/active_screen.png",
        status: "completed"
      },
      {
        type: "ocr",
        text: `Parsing OCR for potential window overlaps and active dock/menu dimensions using ${ocrModel}`,
        tool: ocrModel,
        command: `python parse_layout.py --image /tmp/active_screen.png`,
        status: "completed"
      },
      {
        type: "exec",
        text: "Locating and resolving shell executable path for application",
        tool: "bash",
        command: "which xterm || which terminal",
        status: "completed"
      },
      {
        type: "exec",
        text: "Spawning desktop process with isolated child shell",
        tool: "bash",
        command: "nohup open -a 'Terminal' > /dev/null 2>&1 &",
        status: "completed"
      },
      {
        type: "status",
        text: "Process spawned successfully. PID: 49204. Monitoring window visibility...",
        tool: "system_api",
        command: "osascript -e 'tell application \"System Events\" to get name of first process whose frontmost is true'",
        status: "completed"
      }
    ];
  } else if (normalized.includes("find") || normalized.includes("search") || normalized.includes("file") || normalized.includes("pdf")) {
    text = "I searched your file system and organized the matching files as requested. Multiple PDF structures and document handles have been updated.";
    steps = [
      {
        type: "planning",
        text: "Indexing folder hierarchies across user space paths (~/Documents, ~/Downloads)",
        tool: "file_system",
        command: "find ~ -maxdepth 3 -name '*.pdf'",
        status: "completed"
      },
      {
        type: "exec",
        text: "Scanning metadata structures on discovered filesystem elements",
        tool: "bash",
        command: "ls -laT ~/Downloads/*.pdf",
        status: "completed"
      },
      {
        type: "info",
        text: "Discovered 4 files matching target file descriptor rules.",
        tool: "file_system",
        command: "cat /tmp/search_results.json",
        status: "completed"
      },
      {
        type: "exec",
        text: "Executing structural alignment script to group documents by date/extension",
        tool: "bash",
        command: "mkdir -p ~/Documents/Receipts && mv ~/Downloads/*receipt*.pdf ~/Documents/Receipts/",
        status: "completed"
      },
      {
        type: "status",
        text: "Discovered documents remapped. Integrity and links check complete.",
        tool: "file_system",
        command: "ls ~/Documents/Receipts/",
        status: "completed"
      }
    ];
  } else if (normalized.includes("web") || normalized.includes("search") || normalized.includes("weather") || normalized.includes("browser")) {
    text = "I completed a localized background browser search query. System logs verify navigation, network stack requests, and target data extraction of search pages.";
    steps = [
      {
        type: "planning",
        text: "Spawning headless browser container for sandbox safe scraping",
        tool: "chrome_driver",
        command: "google-chrome --headless --remote-debugging-port=9222",
        status: "completed"
      },
      {
        type: "exec",
        text: "Querying search engine via background navigation context...",
        tool: "chrome_driver",
        command: "navigate 'https://www.google.com/search?q=latest+weather+updates'",
        status: "completed"
      },
      {
        type: "ocr",
        text: `OCR Screen scanning of search viewport for structured weather cards using ${ocrModel}`,
        tool: ocrModel,
        command: "ocr_extract --target '.g-card'",
        status: "completed"
      },
      {
        type: "info",
        text: "Extracted: Weather shows 24°C, Humidity: 62%, Mild breeze",
        tool: "web_search",
        status: "completed"
      },
      {
        type: "status",
        text: "Closing background web container session cleanly. Telemetry stored.",
        tool: "chrome_driver",
        status: "completed"
      }
    ];
  } else {
    text = `I have received and logged your laptop task: "${prompt}". I've initialized the system agent to map, inspect, and execute these rules safely within your secure sandbox enclosure. Let me know if you need any adjustments.`;
    steps = [
      {
        type: "planning",
        text: `Parsing input script semantic objectives and variables on model: ${brainModel}...`,
        tool: "brain_model",
        status: "completed"
      },
      {
        type: "exec",
        text: "Validating current laptop host metrics and window constraints",
        tool: "system_api",
        command: "uname -a && uptime",
        status: "completed"
      },
      {
        type: "info",
        text: "Active workspace: Host environment verified. Secure user execution state is Green.",
        tool: "system_api",
        status: "completed"
      },
      {
        type: "status",
        text: "Assistant loop idle, standing by for user command integration...",
        status: "completed"
      }
    ];
  }
  return { text, steps };
};

const getStreamingChatText = (text: string): string => {
  const match = text.match(/"chat"\s*:\s*"((\\.|[^"\\])*)/);
  if (match && match[1]) {
    return match[1].replace(/\\n/g, '\n').replace(/\\"/g, '"').replace(/\\\\/g, '\\');
  }
  if (text.trim().startsWith('{')) {
    return '';
  }
  return text;
};

const getStreamingSpeechText = (text: string): string => {
  const match = text.match(/"speech"\s*:\s*"((\\.|[^"\\])*)/);
  if (match && match[1]) {
    return match[1].replace(/\\n/g, '\n').replace(/\\"/g, '"').replace(/\\\\/g, '\\');
  }
  return getStreamingChatText(text);
};

const getFinalLangCode = (text: string): string => {
  const match = text.match(/"lang"\s*:\s*"([^"]*)"/);
  if (match && match[1]) {
    return match[1];
  }
  return 'na';
};

const playUISound = (type: 'hover' | 'click' | 'success' | 'error') => {
  try {
    const isEnabled = localStorage.getItem('meridian_ui_sound_effects') !== 'false';
    if (!isEnabled) return;

    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
    if (!AudioContextClass) return;

    const ctx = new AudioContextClass();
    const now = ctx.currentTime;

    if (type === 'hover') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(1400, now);
      gain.gain.setValueAtTime(0.015, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.01);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.01);
    } 
    else if (type === 'click') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(800, now);
      osc.frequency.exponentialRampToValueAtTime(400, now + 0.04);
      gain.gain.setValueAtTime(0.04, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.04);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start(now);
      osc.stop(now + 0.04);
    } 
    else if (type === 'success') {
      const notes = [523.25, 659.25, 783.99]; // C5, E5, G5
      notes.forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.06);
        gain.gain.setValueAtTime(0.03, now + idx * 0.06);
        gain.gain.exponentialRampToValueAtTime(0.0001, now + idx * 0.06 + 0.12);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + idx * 0.06);
        osc.stop(now + idx * 0.06 + 0.12);
      });
    } 
    else if (type === 'error') {
      const osc1 = ctx.createOscillator();
      const osc2 = ctx.createOscillator();
      const gain = ctx.createGain();
      osc1.type = 'sawtooth';
      osc2.type = 'sawtooth';
      osc1.frequency.setValueAtTime(150, now);
      osc2.frequency.setValueAtTime(155, now);
      gain.gain.setValueAtTime(0.05, now);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.2);
      osc1.connect(gain);
      osc2.connect(gain);
      gain.connect(ctx.destination);
      osc1.start(now);
      osc2.start(now);
      osc1.stop(now + 0.2);
      osc2.stop(now + 0.2);
    }
  } catch (err) {
    console.warn("Web Audio sound generation failed:", err);
  }
};

const renderDiffLines = (text: string, type: 'red' | 'green') => {
  if (!text) return null;
  const lines = text.split('\n');
  return lines.map((line, idx) => {
    const bgClass = type === 'red' 
      ? 'bg-rose-950/20 text-rose-300 border-l-2 border-rose-500/50' 
      : 'bg-emerald-950/20 text-emerald-300 border-l-2 border-emerald-500/50';
    return (
      <div key={idx} className={`font-mono text-[10px] py-0.5 px-2 select-text ${bgClass} hover:bg-opacity-40 transition-colors`}>
        <span className="text-zinc-650 select-none mr-3 inline-block w-6 text-right font-medium">{idx + 1}</span>
        <span>{line}</span>
      </div>
    );
  });
};

function BackgroundCanvas({ theme }: { theme: 'default' | 'cyberpunk' | 'amber' | 'slate' }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    if (!ctx) return;

    let animationId: number;
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    const handleResize = () => {
      if (canvas) {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
      }
    };
    window.addEventListener('resize', handleResize);

    const fps = 24;
    const interval = 1000 / fps;
    let lastTime = 0;

    // --- standard (neural net) ---
    const points: { x: number; y: number; vx: number; vy: number }[] = [];
    const maxPoints = 30;
    for (let i = 0; i < maxPoints; i++) {
      points.push({
        x: Math.random() * width,
        y: Math.random() * height,
        vx: (Math.random() - 0.5) * 0.3,
        vy: (Math.random() - 0.5) * 0.3
      });
    }

    // --- cyberpunk (matrix code rain) ---
    const fontSize = 12;
    const columns = Math.floor(width / fontSize) + 1;
    const rainDrops: number[] = Array(columns).fill(1).map(() => Math.floor(Math.random() * -100));

    // --- slate (drifting space dust) ---
    const stars: { x: number; y: number; r: number; alpha: number; speed: number }[] = [];
    for (let i = 0; i < 40; i++) {
      stars.push({
        x: Math.random() * width,
        y: Math.random() * height,
        r: Math.random() * 1.5 + 0.5,
        alpha: Math.random(),
        speed: Math.random() * 0.04 + 0.015
      });
    }

    let amberScanlineY = 0;

    const animate = (timestamp: number) => {
      animationId = requestAnimationFrame(animate);

      const delta = timestamp - lastTime;
      if (delta < interval) return;
      lastTime = timestamp - (delta % interval);

      ctx.clearRect(0, 0, width, height);

      if (theme === 'default') {
        ctx.strokeStyle = 'rgba(234, 88, 12, 0.05)';
        ctx.fillStyle = 'rgba(234, 88, 12, 0.06)';
        ctx.lineWidth = 1;

        points.forEach((p, idx) => {
          p.x += p.vx;
          p.y += p.vy;

          if (p.x < 0 || p.x > width) p.vx *= -1;
          if (p.y < 0 || p.y > height) p.vy *= -1;

          ctx.beginPath();
          ctx.arc(p.x, p.y, 1.5, 0, Math.PI * 2);
          ctx.fill();

          for (let j = idx + 1; j < points.length; j++) {
            const p2 = points[j];
            const dist = Math.hypot(p.x - p2.x, p.y - p2.y);
            if (dist < 130) {
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(p2.x, p2.y);
              ctx.stroke();
            }
          }
        });
      } 
      else if (theme === 'cyberpunk') {
        ctx.font = `${fontSize}px monospace`;

        for (let i = 0; i < rainDrops.length; i++) {
          const char = Math.random() > 0.5 ? '0' : '1';
          const x = i * fontSize;
          const y = rainDrops[i] * fontSize;

          if (y > 0) {
            ctx.fillStyle = Math.random() > 0.98 ? 'rgba(0, 240, 255, 0.07)' : 'rgba(255, 0, 127, 0.05)';
            ctx.fillText(char, x, y);
          }

          if (y > height && Math.random() > 0.98) {
            rainDrops[i] = 0;
          }
          rainDrops[i]++;
        }
      } 
      else if (theme === 'amber') {
        ctx.fillStyle = 'rgba(255, 176, 0, 0.02)';
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = 'rgba(255, 176, 0, 0.04)';
        ctx.fillRect(0, amberScanlineY, width, 2);
        amberScanlineY = (amberScanlineY + 1) % height;
      } 
      else if (theme === 'slate') {
        stars.forEach(s => {
          s.x -= s.speed * 8;
          if (s.x < 0) s.x = width;

          s.alpha += (Math.random() - 0.5) * 0.03;
          s.alpha = Math.max(0.1, Math.min(0.6, s.alpha));

          ctx.fillStyle = `rgba(20, 184, 166, ${s.alpha * 0.15})`;
          ctx.beginPath();
          ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
          ctx.fill();
        });
      }
    };

    animationId = requestAnimationFrame(animate);

    return () => {
      cancelAnimationFrame(animationId);
      window.removeEventListener('resize', handleResize);
    };
  }, [theme]);

  return <canvas ref={canvasRef} className="absolute inset-0 w-full h-full pointer-events-none z-0" style={{ mixBlendMode: 'screen' }} />;
}

export default function App() {
  const [messages, setMessages] = useState<Message[]>([
    {
      id: 'welcome-msg',
      sender: 'assistant',
      text: "Hello! I am Meridian, your intelligent workspace companion. Let me know if you would like to analyze layouts, organize documents, inspect system configurations, or run tests.",
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    }
  ]);
  const [inputText, setInputText] = useState('');
  const [isRunning, setIsRunning] = useState(false);
  const [abortController, setAbortController] = useState<AbortController | null>(null);
  const [pendingConfirmation, setPendingConfirmation] = useState<any | null>(null);
  const [backendConnected, setBackendConnected] = useState(false);

  // Custom visual theme switcher states
  const [theme, setTheme] = useState<'default' | 'cyberpunk' | 'amber' | 'slate'>(() => {
    try {
      const saved = localStorage.getItem('meridian_theme');
      return (saved as any) || 'default';
    } catch {
      return 'default';
    }
  });

  const [uiSoundEnabled, setUiSoundEnabled] = useState<boolean>(() => {
    try {
      const saved = localStorage.getItem('meridian_ui_sound_effects');
      return saved !== 'false';
    } catch {
      return true;
    }
  });

  useEffect(() => {
    localStorage.setItem('meridian_ui_sound_effects', String(uiSoundEnabled));
  }, [uiSoundEnabled]);

  useEffect(() => {
    localStorage.setItem('meridian_theme', theme);
  }, [theme]);

  useEffect(() => {
    const handleContextMenu = (e: MouseEvent) => {
      e.preventDefault();
    };
    document.addEventListener('contextmenu', handleContextMenu);
    return () => {
      document.removeEventListener('contextmenu', handleContextMenu);
    };
  }, []);

  // Tabbed sidebar states
  const [sidebarTab, setSidebarTab] = useState<'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'sandbox' | 'lobby' | 'codemap' | 'docs' | 'closet'>('timeline');
  const [lobbyPrompt, setLobbyPrompt] = useState<string>('');
  const [lobbyDebate, setLobbyDebate] = useState<{ agent: string; avatar: string; message: string }[]>([]);
  const [lobbyProposedCode, setLobbyProposedCode] = useState<string>('');
  const [isLobbyRunning, setIsLobbyRunning] = useState<boolean>(false);
  const [codeGraph, setCodeGraph] = useState<{ nodes: any[]; links: any[] }>({ nodes: [], links: [] });
  const [selectedNode, setSelectedNode] = useState<any | null>(null);
  const [draggedNodeId, setDraggedNodeId] = useState<string | null>(null);
  const [clipboardHistory, setClipboardHistory] = useState<any[]>([]);
  const [clipboardSearch, setClipboardSearch] = useState<string>('');
  const [devStats, setDevStats] = useState<any>({
    total_tasks: 0,
    success_tasks: 0,
    failed_tasks: 0,
    security_audits: 0,
    pomodoros: 0
  });
  const [sandboxCode, setSandboxCode] = useState<string>(
    '# Write Python code here\nprint("Hello from Sandbox!")\nimport os\nprint("Current PID:", os.getpid())'
  );
  const [sandboxStatus, setSandboxStatus] = useState<'idle' | 'auditing' | 'executing' | 'success' | 'failed' | 'blocked' | 'syntax_error'>('idle');
  const [sandboxOutput, setSandboxOutput] = useState<string>('');
  const [sandboxAuditorReasoning, setSandboxAuditorReasoning] = useState<string>('');
  const [sandboxSyntaxErr, setSandboxSyntaxErr] = useState<any | null>(null);
  const [backgroundRuns, setBackgroundRuns] = useState<any[]>([]);
  const [expandedRunIds, setExpandedRunIds] = useState<Record<number, boolean>>({});

  const [isAutomating, setIsAutomating] = useState(false);
  const [automatingTool, setAutomatingTool] = useState('');

  // ── Code Map Filter and Search states ──────────────────────────────────────
  const [codeMapFilter, setCodeMapFilter] = useState<'all' | 'py' | 'ts' | 'js'>('all');
  const [codeMapSearch, setCodeMapSearch] = useState<string>('');

  // ── Offline docs search states ─────────────────────────────────────────────
  const [docsQuery, setDocsQuery] = useState('');
  const [docsResults, setDocsResults] = useState<any[]>([]);
  const [isSearchingDocs, setIsSearchingDocs] = useState(false);
  const [isDragging, setIsDragging] = useState(false);
  const [ingestStatus, setIngestStatus] = useState<'idle' | 'ingesting' | 'success' | 'error'>('idle');
  const [ingestMessage, setIngestMessage] = useState('');

  // ── Sync mascot states locally for VAD and display ─────────────────────────
  const [mascotState, setMascotState] = useState<string>('default');
  const [speechAmplitude, setSpeechAmplitude] = useState<number>(0);

  useEffect(() => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      const unlistenAutomation = listen('automation-state-changed', (event: any) => {
        setIsAutomating(!!event.payload?.active);
        setAutomatingTool(event.payload?.tool || '');
      });
      const unlistenMascotState = listen('mascot-state-changed', (event: any) => {
        setMascotState(event.payload?.state || 'default');
      });
      const unlistenMascotAmp = listen('mascot-amplitude-changed', (event: any) => {
        setSpeechAmplitude(event.payload?.amplitude || 0);
      });
      const unlistenDragDrop = listen('tauri://drag-drop', async (event: any) => {
        const paths: string[] = event.payload?.paths || (Array.isArray(event.payload) ? event.payload : []);
        if (paths && paths.length > 0) {
          setIngestStatus('ingesting');
          playUISound('click');
          try {
            for (const path of paths) {
              const res = await fetch('http://127.0.0.1:8000/api/rag/ingest-file', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ file_path: path })
              });
              if (!res.ok) {
                const errData = await res.json();
                throw new Error(errData.detail || `Ingestion failed: ${res.statusText}`);
              }
            }
            setIngestStatus('success');
            setIngestMessage(`Successfully ingested ${paths.length} file(s) into RAG.`);
            playUISound('success');
          } catch (err: any) {
            setIngestStatus('error');
            setIngestMessage(err.message || 'Error ingesting files via Tauri drop.');
            playUISound('error');
          }
        }
      });
      return () => {
        unlistenAutomation.then(fn => fn());
        unlistenMascotState.then(fn => fn());
        unlistenMascotAmp.then(fn => fn());
        unlistenDragDrop.then(fn => fn());
      };
    }
  }, []);

  const fetchBackgroundRuns = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/scheduler/runs?limit=15');
      if (res.ok) {
        const data = await res.json();
        if (data.runs) {
          setBackgroundRuns(data.runs);
        }
      }
    } catch (err) {
      console.error("Failed to fetch background runs:", err);
    }
  };

  useEffect(() => {
    if (sidebarTab === 'jobs' && backendConnected) {
      fetchBackgroundRuns();
      const interval = setInterval(fetchBackgroundRuns, 4000);
      return () => clearInterval(interval);
    }
  }, [sidebarTab, backendConnected]);

  const [thoughts, setThoughts] = useState<ThoughtStep[]>([
    {
      id: 'init-thought-1',
      type: 'status',
      text: 'Workspace context loaded. Connection to local brain established.',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
      status: 'completed'
    },
    {
      id: 'init-thought-2',
      type: 'info',
      text: 'Secure sandbox environment verified.',
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
      status: 'completed'
    }
  ]);

  const [localOllamaModels, setLocalOllamaModels] = useState<string[]>(LOCAL_BRAIN_MODELS);
  const [swarmThoughts, setSwarmThoughts] = useState<{ agent: string; thought: string; timestamp: string }[]>([]);

  // ── Proactive Nudge State ─────────────────────────────────────────────────
  const [nudges, setNudges] = useState<ProactiveNudge[]>([]);

  // ── Pomodoro Focus & Break Overlay States ──────────────────────────────────
  const [pomodoroTime, setPomodoroTime] = useState<number>(25 * 60);
  const [pomodoroActive, setPomodoroActive] = useState<boolean>(false);
  const [showBreakOverlay, setShowBreakOverlay] = useState<boolean>(false);
  const [breakTimer, setBreakTimer] = useState<number>(20);

  // ── Self-Healing Diff Modal States ────────────────────────────────────────
  const [showDiffModal, setShowDiffModal] = useState<boolean>(false);
  const [diffData, setDiffData] = useState<{
    filePath: string;
    errorMessage: string;
    original: string;
    proposed: string;
    nudgeId: string;
  } | null>(null);
  const [initialProposed, setInitialProposed] = useState<string>('');
  const [isFetchingHeal, setIsFetchingHeal] = useState<boolean>(false);
  const [credentialSecret, setCredentialSecret] = useState<string | null>(null);

  const [mascotWardrobe, setMascotWardrobe] = useState<string>(() => {
    try {
      return localStorage.getItem('meridian_mascot_wardrobe') || 'auto';
    } catch {
      return 'auto';
    }
  });

  useEffect(() => {
    localStorage.setItem('meridian_mascot_wardrobe', mascotWardrobe);
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('mascot-wardrobe-changed', { item: mascotWardrobe }).catch(console.error);
    }
  }, [mascotWardrobe]);

  // ── Vocalize Alerts State ──────────────────────────────────────────────────
  const [alertVocalizerEnabled, setAlertVocalizerEnabled] = useState<boolean>(() => {
    try {
      const saved = localStorage.getItem('meridian_vocalize_alerts');
      return saved ? JSON.parse(saved) : false;
    } catch {
      return false;
    }
  });

  useEffect(() => {
    localStorage.setItem('meridian_vocalize_alerts', JSON.stringify(alertVocalizerEnabled));
  }, [alertVocalizerEnabled]);

  const [selectedVoice, setSelectedVoice] = useState<string>(() => {
    try {
      const saved = localStorage.getItem('meridian_tts_voice');
      return saved || 'M1';
    } catch {
      return 'M1';
    }
  });

  const selectedVoiceRef = useRef(selectedVoice);
  useEffect(() => {
    selectedVoiceRef.current = selectedVoice;
  }, [selectedVoice]);

  useEffect(() => {
    localStorage.setItem('meridian_tts_voice', selectedVoice);
  }, [selectedVoice]);

  // ── WhatsApp Link QR States ────────────────────────────────────────────────
  const [showWhatsAppQR, setShowWhatsAppQR] = useState<boolean>(false);
  const [qrTimestamp, setQrTimestamp] = useState<number>(Date.now());

  // Refs for audio playback and voice barge-in (VAD)
  const activeAudioRef = useRef<HTMLAudioElement | null>(null);
  const activeMicStreamRef = useRef<MediaStream | null>(null);
  const bargeInCheckIntervalRef = useRef<any>(null);



  // ── Multimodal Vision States ──────────────────────────────────────────────
  const [capturedImage, setCapturedImage] = useState<string | null>(null);
  const [capturedOCR, setCapturedOCR] = useState<string>('');
  const [isCapturingScreen, setIsCapturingScreen] = useState<boolean>(false);

  const handleCaptureScreen = async () => {
    setIsCapturingScreen(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/api/vision/screenshot', { method: 'POST' });
      if (response.ok) {
        const data = await response.json();
        if (data.status === 'success') {
          setCapturedImage(data.image);
          setCapturedOCR(data.ocr_text || '');
        }
      }
    } catch (e) {
      console.error("Failed to capture screen:", e);
    } finally {
      setIsCapturingScreen(false);
    }
  };

  useEffect(() => {
    let interval: any = null;
    if (showWhatsAppQR) {
      setQrTimestamp(Date.now());
      interval = setInterval(() => {
        setQrTimestamp(Date.now());
      }, 5000);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [showWhatsAppQR]);

  const handleInterrupt = async () => {
    console.log("Barging in: Interrupting speech playback and backend generation...");
    if (activeAudioRef.current) {
      activeAudioRef.current.pause();
      activeAudioRef.current = null;
    }
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    try {
      await fetch('http://127.0.0.1:8000/api/voice/interrupt', { method: 'POST' });
    } catch (e) {
      console.error("Failed to notify backend of voice interrupt:", e);
    }
  };

  const startMicBargeInMonitoring = async () => {
    stopMicBargeInMonitoring();
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      activeMicStreamRef.current = stream;
      
      const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
      const source = audioContext.createMediaStreamSource(stream);
      const analyser = audioContext.createAnalyser();
      analyser.fftSize = 512;
      source.connect(analyser);
      
      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);
      let consecutiveSpikes = 0;
      
      const checkVolume = () => {
        if (!activeMicStreamRef.current) return;
        analyser.getByteFrequencyData(dataArray);
        let sum = 0;
        for (let i = 0; i < bufferLength; i++) {
          sum += dataArray[i];
        }
        const average = sum / bufferLength;
        const normalizedVolume = average / 255;
        
        if (normalizedVolume > 0.12) {
          consecutiveSpikes++;
          if (consecutiveSpikes >= 3) {
            console.log("Mic audio spike detected, triggering barge-in interruption.");
            handleInterrupt();
            stopMicBargeInMonitoring();
            return;
          }
        } else {
          consecutiveSpikes = Math.max(0, consecutiveSpikes - 1);
        }
        bargeInCheckIntervalRef.current = requestAnimationFrame(checkVolume);
      };
      bargeInCheckIntervalRef.current = requestAnimationFrame(checkVolume);
    } catch (err) {
      console.warn("Could not access microphone for barge-in monitoring:", err);
    }
  };

  const stopMicBargeInMonitoring = () => {
    if (bargeInCheckIntervalRef.current) {
      cancelAnimationFrame(bargeInCheckIntervalRef.current);
      bargeInCheckIntervalRef.current = null;
    }
    if (activeMicStreamRef.current) {
      activeMicStreamRef.current.getTracks().forEach(track => track.stop());
      activeMicStreamRef.current = null;
    }
  };

  const playAlertTTS = async (text: string) => {
    try {
      const cleanText = text.replace(/<[^>]*>/g, '').trim();
      const response = await fetch('http://127.0.0.1:8000/api/tts', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: cleanText, voice: selectedVoice, lang: 'na' })
      });
      if (response.ok) {
        const blob = await response.blob();
        const url = URL.createObjectURL(blob);
        const audio = new Audio(url);
        await audio.play();
      }
    } catch (e) {
      console.error("Alert vocalizer TTS failed:", e);
    }
  };

  const triggerHealProposer = async (filePath: string, errorMessage: string, nudgeId: string) => {
    setIsFetchingHeal(true);
    setShowDiffModal(true);
    setDiffData({
      filePath,
      errorMessage,
      original: '',
      proposed: '',
      nudgeId
    });
    setCredentialSecret(null);

    // Equip construction hat for healing diagnostics
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('mascot-wardrobe-changed', { item: 'construction_hat' }).catch(console.error);
    }

    try {
      const res = await fetch('http://127.0.0.1:8000/api/watcher/propose-heal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_path: filePath, error_message: errorMessage })
      });
      if (res.ok) {
        const data = await res.json();
        setInitialProposed(data.proposed);
        setDiffData({
          filePath: data.file_path,
          errorMessage,
          original: data.original,
          proposed: data.proposed,
          nudgeId
        });
        
        if (errorMessage === 'secret_leak') {
          // Parse key to propose environment migration
          const match = data.original.match(/\b(api_key|client_secret|db_password|aws_secret|token|private_key)\b\s*=\s*['"]([^'"]+)['"]/i);
          if (match) {
            const keyName = match[1].toUpperCase();
            const keyValue = match[2];
            setCredentialSecret(`${keyName}=${keyValue}`);
          }
        }
      }
    } catch (e) {
      console.error("Failed to fetch heal proposal:", e);
    } finally {
      setIsFetchingHeal(false);
    }
  };

  const handleApplyHeal = async () => {
    if (!diffData) return;
    try {
      const response = await fetch('http://127.0.0.1:8000/api/watcher/apply-heal', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          file_path: diffData.filePath,
          proposed_code: diffData.proposed,
          credential_secret: credentialSecret,
          checkpoint_id: diffData.nudgeId
        })
      });
      if (response.ok) {
        const successMsg: Message = {
          id: 'heal-success-' + Date.now(),
          sender: 'assistant',
          text: `Self-healing successfully applied to: ${diffData.filePath}`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };
        setMessages(prev => [...prev, successMsg]);
        if (diffData.filePath.endsWith("sandbox_temp.py")) {
          setSandboxCode(diffData.proposed);
        }
        setShowDiffModal(false);
        setDiffData(null);
        setCredentialSecret(null);

        // Reset wardrobe back to default
        const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
        if (isTauri) {
          emit('mascot-wardrobe-changed', { item: 'default' }).catch(console.error);
        }
      } else {
        console.error("Failed to apply heal:", await response.text());
      }
    } catch (e) {
      console.error("Failed to apply heal:", e);
    }
  };

  const handleRollbackToCheckpoint = async (checkpointId: string) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/history/rollback', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ checkpoint_id: checkpointId })
      });
      if (response.ok) {
        const rollbackMsg: Message = {
          id: 'rollback-success-' + Date.now(),
          sender: 'assistant',
          text: `Workspace successfully rolled back to checkpoint: ${checkpointId}`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
        };
        setMessages(prev => [...prev, rollbackMsg]);
        alert(`Workspace successfully rolled back to step: ${checkpointId}`);
      } else {
        const errMsg = await response.text();
        console.error("Rollback failed:", errMsg);
        alert(`Rollback failed: ${errMsg}`);
      }
    } catch (e) {
      console.error("Rollback failed:", e);
      alert(`Rollback error: ${e}`);
    }
  };

  const triggerVoiceCommandRef = useRef<() => void>();

  // Subscribe to backend proactive stream
  useEffect(() => {
    if (!backendConnected) return;
    const es = new EventSource('http://127.0.0.1:8000/api/proactive/stream');
    es.addEventListener('nudge', (e: MessageEvent) => {
      try {
        const nudge: ProactiveNudge = JSON.parse(e.data);
        
        if (nudge.type === "game_mode_changed") {
          const enabled = nudge.message === "enabled";
          setGameMode(enabled);
          const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
          if (isTauri) {
            invoke('toggle_game_mode', { enabled }).catch(console.error);
            if (enabled) {
              setMascotEnabled(false);
            }
          }
          return;
        }

        if (nudge.action === "start_voice_command") {
          triggerVoiceCommandRef.current?.();
          return;
        }

        setNudges(prev => [...prev.slice(-4), nudge]); // keep max 5

        if (alertVocalizerEnabled && nudge.message) {
          playAlertTTS(nudge.message);
        }

        // Auto-dismiss after 12 seconds
        setTimeout(() => {
          setNudges(prev => prev.filter(n => n.id !== nudge.id));
        }, 12000);
      } catch (err) {
        console.error('Failed to parse proactive nudge:', err);
      }
    });
    return () => es.close();
  }, [backendConnected, alertVocalizerEnabled, selectedVoice]);

  const dismissNudge = (id: string) => setNudges(prev => prev.filter(n => n.id !== id));

  const fetchClipboard = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/clipboard/history?limit=15');
      if (res.ok) {
        const data = await res.json();
        if (data.history) setClipboardHistory(data.history);
      }
    } catch (err) {}
  };

  const fetchDevStats = async () => {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/developer/stats');
      if (res.ok) {
        const data = await res.json();
        setDevStats(data);
      }
    } catch (err) {}
  };

  useEffect(() => {
    if (backendConnected) {
      fetchClipboard();
      fetchDevStats();
      const interval = setInterval(() => {
        if (sidebarTab === 'clipboard') fetchClipboard();
        if (sidebarTab === 'productivity') fetchDevStats();
      }, 4000);
      return () => clearInterval(interval);
    }
  }, [backendConnected, sidebarTab]);

  const initializeNodePositions = (nodes: any[]) => {
    const width = 500;
    const height = 400;
    return nodes.map((node, i) => {
      const angle = (i / nodes.length) * 2 * Math.PI;
      const radius = 120 + Math.random() * 30;
      return {
        ...node,
        x: width / 2 + Math.cos(angle) * radius,
        y: height / 2 + Math.sin(angle) * radius
      };
    });
  };

  const fetchCodeGraph = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/codebase/graph');
      if (response.ok) {
        const data = await response.json();
        const positionedNodes = initializeNodePositions(data.nodes || []);
        setCodeGraph({ nodes: positionedNodes, links: data.links || [] });
      }
    } catch (e) {
      console.error("Failed to fetch code graph:", e);
    }
  };

  useEffect(() => {
    if (sidebarTab === 'codemap' && backendConnected) {
      fetchCodeGraph();
    }
  }, [sidebarTab, backendConnected]);

  const handleGraphNodeDrag = (e: React.MouseEvent<SVGSVGElement>) => {
    if (!draggedNodeId) return;
    const rect = e.currentTarget.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;
    setCodeGraph(prev => ({
      ...prev,
      nodes: prev.nodes.map(n => n.id === draggedNodeId ? { ...n, x, y } : n)
    }));
  };

  const handleGraphNodeDragEnd = () => {
    setDraggedNodeId(null);
  };

  const handleRunLobbyDebate = async () => {
    if (!lobbyPrompt.trim()) return;
    setIsLobbyRunning(true);
    setLobbyDebate([]);
    setLobbyProposedCode('');
    
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('mascot-state-changed', { state: 'diagnostic' }).catch(console.error);
    }
    
    try {
      const response = await fetch('http://127.0.0.1:8000/api/lobby/debate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: lobbyPrompt })
      });
      if (response.ok) {
        const data = await response.json();
        if (data.status === 'success') {
          setLobbyDebate(data.debate || []);
          setLobbyProposedCode(data.proposed_code || '');
          if (isTauri) {
            emit('mascot-state-changed', { state: 'happy' }).catch(console.error);
          }
        }
      }
    } catch (e) {
      console.error("Lobby debate failed:", e);
    } finally {
      setIsLobbyRunning(false);
    }
  };

  const handleRunSandbox = async () => {
    setSandboxStatus('auditing');
    setSandboxOutput('');
    setSandboxAuditorReasoning('');
    setSandboxSyntaxErr(null);

    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('mascot-state-changed', { state: 'diagnostic' }).catch(console.error);
    }

    try {
      await new Promise(r => setTimeout(r, 800));
      setSandboxStatus('executing');

      const res = await fetch('http://127.0.0.1:8000/api/sandbox/run', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code: sandboxCode })
      });
      
      if (res.ok) {
        const data = await res.json();
        if (data.status === 'success') {
          setSandboxStatus('success');
          setSandboxOutput(data.output);
          setSandboxAuditorReasoning(data.auditor_reasoning);
          playUISound('success');
          if (isTauri) {
            emit('mascot-state-changed', { state: 'happy' }).catch(console.error);
          }
        } else if (data.status === 'blocked') {
          setSandboxStatus('blocked');
          setSandboxOutput(data.message);
          playUISound('error');
          if (isTauri) {
            emit('mascot-state-changed', { state: 'disapproving' }).catch(console.error);
          }
        } else if (data.status === 'syntax_error') {
          setSandboxStatus('syntax_error');
          setSandboxOutput(data.message);
          setSandboxSyntaxErr(data);
          playUISound('error');
          if (isTauri) {
            emit('mascot-state-changed', { state: 'tired' }).catch(console.error);
          }
        } else {
          setSandboxStatus('failed');
          setSandboxOutput(data.message || 'Execution error');
          playUISound('error');
          if (isTauri) {
            emit('mascot-state-changed', { state: 'tired' }).catch(console.error);
          }
        }
      } else {
        setSandboxStatus('failed');
        setSandboxOutput(`API status error: ${res.statusText}`);
        playUISound('error');
      }
    } catch (err: any) {
      setSandboxStatus('failed');
      setSandboxOutput(`Communication error: ${err.message}`);
      playUISound('error');
    }
  };

  const handleHealSandboxCode = async () => {
    if (!sandboxSyntaxErr || !sandboxSyntaxErr.file_path) return;
    triggerHealProposer(sandboxSyntaxErr.file_path, sandboxSyntaxErr.message, 'sandbox');
  };

  const handleNudgeAction = (nudge: ProactiveNudge) => {
    dismissNudge(nudge.id);

    if (nudge.action === "run_repair" && nudge.patch) {
      handleSendCommand(nudge.patch.proposed);
      return;
    }

    if (nudge.action === "show_diff" && nudge.patch) {
      setDiffData({
        filePath: nudge.patch.file_path,
        errorMessage: nudge.patch.error_message,
        original: nudge.patch.original,
        proposed: nudge.patch.proposed,
        nudgeId: nudge.id
      });
      setInitialProposed(nudge.patch.proposed);
      setShowDiffModal(true);
      return;
    }

    if (nudge.type === 'secret_leak') {
      const targetFile = nudge.action_hint?.replace("Secure key in .env: ", "") || "";
      triggerHealProposer(targetFile, 'secret_leak', nudge.id);
    } 
    else if (nudge.type === 'save_to_heal') {
      const target = nudge.action_hint?.replace("Fix syntax: ", "").split(":")[0] || "";
      triggerHealProposer(target, 'save_to_heal', nudge.id);
    } 
    else if (nudge.type === 'git_copilot') {
      const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
      if (isTauri) {
        emit('mascot-wardrobe-changed', { item: 'detective_hat' }).catch(console.error);
      }
      handleSendCommand("Draft a structured git commit message for the changes in the workspace.");
    } 
    else if (nudge.type === 'focus_distraction') {
      const alertMsg: Message = {
        id: 'focus-reset-' + Date.now(),
        sender: 'assistant',
        text: "Focus guard reset. Let's get back to coding! I've cleared the distraction alert.",
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, alertMsg]);
    } 
    else if (nudge.type === 'network_adapter') {
      const isOffline = nudge.title.toLowerCase().includes("offline");
      setModelSettings(prev => {
        const nextSettings: ModelSettings = {
          ...prev,
          modelSource: isOffline ? 'local' : 'api'
        };
        localStorage.setItem('meridian_model_settings', JSON.stringify(nextSettings));
        return nextSettings;
      });
      const networkMsg: Message = {
        id: 'network-switch-' + Date.now(),
        sender: 'assistant',
        text: isOffline 
          ? "Switched LLM provider to local offline fallback models."
          : "Restored cloud LLM provider settings.",
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      };
      setMessages(prev => [...prev, networkMsg]);
    } 
    else if (nudge.type === 'battery_saver') {
      try {
        fetch('http://127.0.0.1:8000/api/system/power-save', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ active: true })
        }).then(res => {
          if (res.ok) {
            const powerMsg: Message = {
              id: 'power-save-success-' + Date.now(),
              sender: 'assistant',
              text: "Power-Saving Mode activated. Workspace has paused heavy tasks and switched to local Qwen 1.5B fallback model.",
              timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
            };
            setMessages(prev => [...prev, powerMsg]);
            setModelSettings(prev => ({
              ...prev,
              brainModel: 'qwen2.5-coder:1.5b-instruct-q8_0'
            }));
          }
        });
      } catch (e) {
        console.error("Failed to activate power-saving mode:", e);
      }
    }
    else if (nudge.action_hint) {
      handleSendCommand(nudge.action_hint);
    }
  };

  // Pomodoro countdown effect
  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (pomodoroActive && pomodoroTime > 0 && !showBreakOverlay) {
      interval = setInterval(() => {
        setPomodoroTime(prev => prev - 1);
      }, 1000);
    } else if (pomodoroActive && pomodoroTime === 0 && !showBreakOverlay) {
      setShowBreakOverlay(true);
      setBreakTimer(20);
      
      // Increment pomodoro count on backend
      fetch('http://127.0.0.1:8000/api/profile/pomodoro/increment', { method: 'POST' })
        .then(() => fetchDevStats())
        .catch(console.error);
        
      const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
      if (isTauri) {
        emit('mascot-state-changed', { state: 'crown' }).catch(console.error);
        emit('mascot-wardrobe-changed', { item: 'crown' }).catch(console.error);
      }
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [pomodoroActive, pomodoroTime, showBreakOverlay]);

  // Break overlay countdown effect
  useEffect(() => {
    let interval: NodeJS.Timeout | null = null;
    if (showBreakOverlay && breakTimer > 0) {
      interval = setInterval(() => {
        setBreakTimer(prev => prev - 1);
      }, 1000);
    } else if (showBreakOverlay && breakTimer === 0) {
      setShowBreakOverlay(false);
      setPomodoroTime(25 * 60);
      const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
      if (isTauri) {
        emit('mascot-state-changed', { state: 'default' }).catch(console.error);
      }
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [showBreakOverlay, breakTimer]);

  useEffect(() => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      if (nudges.length > 0) {
        const latestNudge = nudges[nudges.length - 1];
        if (latestNudge.mascot_state) {
          emit('mascot-state-changed', { state: latestNudge.mascot_state }).catch(console.error);
        }
      } else {
        emit('mascot-state-changed', { state: 'default' }).catch(console.error);
      }
    }
  }, [nudges]);

  useEffect(() => {
    let eventSource: EventSource | null = null;
    if (backendConnected) {
      eventSource = new EventSource('http://127.0.0.1:8000/api/swarm/stream');
      eventSource.onmessage = (e) => {
        try {
          const message = JSON.parse(e.data);
          setSwarmThoughts(prev => [
            ...prev,
            {
              agent: message.agent,
              thought: message.thought,
              timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
            }
          ].slice(-50));
        } catch (err) {
          console.error("Failed to parse swarm thought:", err);
        }
      };
    }
    return () => {
      if (eventSource) {
        eventSource.close();
      }
    };
  }, [backendConnected]);

  const [modelSettings, setModelSettings] = useState<ModelSettings>(() => {
    try {
      const saved = localStorage.getItem('meridian_model_settings');
      if (saved) {
        const parsed = JSON.parse(saved);
        return {
          modelSource: parsed.modelSource || 'local',
          apiProvider: parsed.apiProvider || 'gemini',
          selectedModel: parsed.selectedModel || 'gemini-3.5-flash',
          brainModel: parsed.brainModel || LOCAL_BRAIN_MODELS[0],
          ocrModel: parsed.ocrModel || LOCAL_OCR_MODELS[0]
        };
      }
    } catch (e) {
      console.error("Failed to load model settings from localStorage", e);
    }
    return {
      modelSource: 'local',
      apiProvider: 'gemini',
      selectedModel: 'gemini-3.5-flash',
      brainModel: LOCAL_BRAIN_MODELS[0],
      ocrModel: LOCAL_OCR_MODELS[0]
    };
  });

  const [settingsOpen, setSettingsOpen] = useState<'header' | 'ribbon' | null>(null);

  const settingsRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (settingsOpen && settingsRef.current && !settingsRef.current.contains(event.target as Node)) {
        const headerToggle = document.getElementById('settings-dropdown-toggle');
        const ribbonToggle = document.getElementById('settings-ribbon-toggle');
        if (headerToggle && headerToggle.contains(event.target as Node)) {
          return;
        }
        if (ribbonToggle && ribbonToggle.contains(event.target as Node)) {
          return;
        }
        setSettingsOpen(null);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [settingsOpen]);
  const [mascotEnabled, setMascotEnabled] = useState<boolean>(() => {
    try {
      const saved = localStorage.getItem('meridian_mascot_enabled');
      return saved ? JSON.parse(saved) : false;
    } catch {
      return false;
    }
  });

  useEffect(() => {
    localStorage.setItem('meridian_mascot_enabled', JSON.stringify(mascotEnabled));
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      invoke('set_mascot_visible', { visible: mascotEnabled }).catch(err => {
        console.error("Failed to set mascot visible:", err);
      });
    }
  }, [mascotEnabled]);

  const [gameMode, setGameMode] = useState<boolean>(false);

  useEffect(() => {
    if (backendConnected) {
      fetch('http://127.0.0.1:8000/api/game-mode')
        .then(res => res.json())
        .then(data => {
          if (data && typeof data.game_mode === 'boolean') {
            setGameMode(data.game_mode);
            const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
            if (isTauri) {
              invoke('toggle_game_mode', { enabled: data.game_mode }).catch(console.error);
            }
          }
        })
        .catch(console.error);
    }
  }, [backendConnected]);

  const handleToggleGameMode = async (enabled: boolean) => {
    setGameMode(enabled);
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      try {
        await invoke('toggle_game_mode', { enabled });
        if (enabled) {
          setMascotEnabled(false);
        }
      } catch (err) {
        console.error("Tauri toggle_game_mode failed:", err);
      }
    }
    try {
      await fetch('http://127.0.0.1:8000/api/game-mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ game_mode: enabled })
      });
    } catch (err) {
      console.error("FastAPI set_game_mode failed:", err);
    }
  };

  useEffect(() => {
    let unlistenMascotHide: Promise<any> | undefined;
    let unlistenMascotShow: Promise<any> | undefined;
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenMascotHide = listen('hide-mascot', () => {
        setMascotEnabled(false);
      });
      unlistenMascotShow = listen('show-mascot', () => {
        setMascotEnabled(true);
      });
    }
    return () => {
      if (unlistenMascotHide) {
        unlistenMascotHide.then(fn => {
          if (typeof fn === 'function') fn();
        });
      }
      if (unlistenMascotShow) {
        unlistenMascotShow.then(fn => {
          if (typeof fn === 'function') fn();
        });
      }
    };
  }, []);

  useEffect(() => {
    let unlistenTrayToggle: Promise<any> | undefined;
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenTrayToggle = listen('tray-toggle-game-mode', () => {
        setGameMode(prev => {
          const next = !prev;
          invoke('toggle_game_mode', { enabled: next }).catch(console.error);
          if (next) {
            setMascotEnabled(false);
          }
          fetch('http://127.0.0.1:8000/api/game-mode', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ game_mode: next })
          }).catch(console.error);
          return next;
        });
      });
    }
    return () => {
      if (unlistenTrayToggle) {
        unlistenTrayToggle.then(fn => {
          if (typeof fn === 'function') fn();
        });
      }
    };
  }, []);

  useEffect(() => {
    let unlistenMascotDrop: Promise<any> | undefined;
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenMascotDrop = listen<{ paths: string[] }>('file-dropped-on-mascot', (event) => {
        const filePaths = event.payload.paths;
        if (filePaths && filePaths.length > 0) {
          handleSendCommand(`Ingest and analyze these files: ${filePaths.join(', ')}`);
        }
      });
    }
    return () => {
      if (unlistenMascotDrop) {
        unlistenMascotDrop.then(fn => {
          if (typeof fn === 'function') fn();
        });
      }
    };
  }, []);

  useEffect(() => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('ai-state-changed', { isThinking: isRunning }).catch(err => {
        console.error("Failed to emit ai-state-changed:", err);
      });

      const latestThought = thoughts.length > 0 ? thoughts[thoughts.length - 1] : null;
      emit('agent-status-update', {
        isRunning,
        latestThought,
        thoughts: thoughts.slice(-5)
      }).catch(err => {
        console.error("Failed to emit agent-status-update:", err);
      });
    }
  }, [isRunning, thoughts]);

  useEffect(() => {
    let unlistenCancel: Promise<any> | undefined;
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenCancel = listen('cancel-agent-execution', () => {
        handleStopExecution();
      });
    }
    return () => {
      if (unlistenCancel) {
        unlistenCancel.then(fn => {
          if (typeof fn === 'function') fn();
        });
      }
    };
  }, [abortController]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.altKey && e.key.toLowerCase() === 'm') {
        e.preventDefault();
        setMascotEnabled(prev => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const [fallbackNotice, setFallbackNotice] = useState<string | null>(null);
  const [currentView, setCurrentView] = useState<'landing' | 'app'>(() => {
    try {
      const saved = localStorage.getItem('meridian_model_settings');
      if (saved) {
        const parsed = JSON.parse(saved);
        if (parsed.modelSource === 'api') {
          return 'app';
        }
      }
    } catch (e) {}
    return 'landing';
  });

  const [voiceOutputEnabled, setVoiceOutputEnabled] = useState<boolean>(() => {
    try {
      const saved = localStorage.getItem('meridian_voice_output_enabled');
      return saved ? JSON.parse(saved) : false;
    } catch {
      return false;
    }
  });

  const [isRestartingBackend, setIsRestartingBackend] = useState(false);

  const handleRestartBackend = async () => {
    setIsRestartingBackend(true);
    try {
      await invoke('trigger_backend_restart');
      setTimeout(() => {
        setIsRestartingBackend(false);
      }, 3000);
    } catch (err) {
      console.error('Failed to restart backend:', err);
      setIsRestartingBackend(false);
    }
  };

  useEffect(() => {
    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.getVoices();
    }
  }, []);

  const localVisionModels = Array.from(new Set([...localOllamaModels, ...LOCAL_OCR_MODELS]));

  useEffect(() => {
    localStorage.setItem('meridian_model_settings', JSON.stringify(modelSettings));
  }, [modelSettings]);

  useEffect(() => {
    localStorage.setItem('meridian_voice_output_enabled', JSON.stringify(voiceOutputEnabled));
  }, [voiceOutputEnabled]);

  useEffect(() => {
    const fetchOllamaModels = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/ollama-models');
        if (res.ok) {
          const data = await res.json();
          if (data.models && data.models.length > 0) {
            setLocalOllamaModels(data.models);
            
            const savedRaw = localStorage.getItem('meridian_model_settings');
            if (savedRaw) {
              const saved = JSON.parse(savedRaw);
              if (saved.modelSource === 'local') {
                if (data.models.includes(saved.brainModel)) {
                  setCurrentView('app');
                } else {
                  setCurrentView('landing');
                }
              }
            }

            setModelSettings(prev => {
              if (!data.models.includes(prev.brainModel)) {
                const matched = data.models.find((m: string) => m.toLowerCase() === prev.brainModel.toLowerCase())
                  || data.models.find((m: string) => m.toLowerCase().includes(prev.brainModel.toLowerCase()))
                  || data.models[0];
                return { ...prev, brainModel: matched };
              }
              return prev;
            });
          }
        }
      } catch (err) {
        console.error("Failed to fetch Ollama models:", err);
      }
    };
    fetchOllamaModels();
  }, [backendConnected]);

  useEffect(() => {
    const fetchHistory = async () => {
      if (!backendConnected) return;
      try {
        const res = await fetch('http://127.0.0.1:8000/api/chat/history');
        if (res.ok) {
          const data = await res.json();
          if (data.history && data.history.length > 0) {
            const formatted = data.history.map((msg: any) => {
              let timestampStr = "";
              try {
                if (typeof msg.timestamp === 'number') {
                  const date = new Date(msg.timestamp * 1000);
                  timestampStr = date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                } else {
                  timestampStr = msg.timestamp || "";
                }
              } catch (e) {
                timestampStr = "";
              }
              return {
                id: msg.id || ('hist-' + Math.random()),
                sender: msg.sender,
                text: msg.text,
                timestamp: timestampStr
              };
            });
            setMessages([
              {
                id: 'welcome-msg',
                sender: 'assistant',
                text: "Hello! I am Meridian, your intelligent workspace companion. Let know if you would like to analyze layouts, organize documents, inspect system configurations, or run tests.",
                timestamp: formatted[0] ? formatted[0].timestamp : new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
              },
              ...formatted
            ]);
          }
        }
      } catch (err) {
        console.error("Failed to fetch chat history:", err);
      }
    };
    fetchHistory();
  }, [backendConnected]);

  const [telemetry, setTelemetry] = useState<SystemResource>({
    cpuUsage: 14,
    ramUsage: 49,
    cpuHistory: Array(24).fill(14),
    ramHistory: Array(24).fill(49)
  });

  const [isRecording, setIsRecording] = useState(false);
  const [micVisualizerWaves, setMicVisualizerWaves] = useState<number[]>(Array(16).fill(2));
  const micIntervalRef = useRef<NodeJS.Timeout | null>(null);

  const chatScrollRef = useRef<HTMLDivElement>(null);
  const thoughtScrollRef = useRef<HTMLDivElement>(null);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const [sidebarWidth, setSidebarWidth] = useState(340);
  const isResizingRef = useRef(false);
  const [isResizing, setIsResizing] = useState(false);

  const startResizing = (e: React.MouseEvent) => {
    isResizingRef.current = true;
    setIsResizing(true);
    e.preventDefault();
  };

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      if (!isResizingRef.current) return;
      // Draggable divider is on the right side of the main console, resizing the right sidebar
      const newWidth = Math.max(260, Math.min(window.innerWidth - e.clientX, Math.floor(window.innerWidth * 0.65)));
      setSidebarWidth(newWidth);
    };

    const handleMouseUp = () => {
      if (isResizingRef.current) {
        isResizingRef.current = false;
        setIsResizing(false);
        document.body.style.cursor = '';
        document.body.style.userSelect = '';
      }
    };

    window.addEventListener('mousemove', handleMouseMove);
    window.addEventListener('mouseup', handleMouseUp);

    return () => {
      window.removeEventListener('mousemove', handleMouseMove);
      window.removeEventListener('mouseup', handleMouseUp);
    };
  }, []);

  useEffect(() => {
    if (isResizing) {
      document.body.style.cursor = 'col-resize';
      document.body.style.userSelect = 'none';
    }
  }, [isResizing]);

  useEffect(() => {
    const fetchUsage = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/system-usage');
        if (res.ok) {
          const data = await res.json();
          setBackendConnected(true);
          setTelemetry(prev => {
            const nextCpuHistory = [...prev.cpuHistory.slice(1), data.cpu];
            const nextRamHistory = [...prev.ramHistory.slice(1), data.ram];
            return {
              cpuUsage: data.cpu,
              ramUsage: data.ram,
              cpuHistory: nextCpuHistory,
              ramHistory: nextRamHistory
            };
          });
          return;
        }
      } catch (err) {
        // Fall back to simulation below
      }

      setBackendConnected(false);
      setTelemetry(prev => {
        const val = Math.max(10, Math.min(95, Math.round(prev.cpuUsage + (Math.random() * 10 - 5))));
        const ram = Math.max(45, Math.min(88, Math.round(prev.ramUsage + (Math.random() * 2 - 1))));
        return {
          cpuUsage: val,
          ramUsage: ram,
          cpuHistory: [...prev.cpuHistory.slice(1), val],
          ramHistory: [...prev.ramHistory.slice(1), ram]
        };
      });
    };

    fetchUsage();
    const interval = setInterval(fetchUsage, 2000);
    return () => clearInterval(interval);
  }, []);

  // Auto-scroll chat window when new messages are added, avoiding snapping if the user has scrolled up
  useEffect(() => {
    const el = chatScrollRef.current;
    if (!el) return;
    const isAtBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 150;
    if (isAtBottom || (messages.length > 0 && messages[messages.length - 1].sender === 'user')) {
      el.scrollTop = el.scrollHeight;
    }
  }, [messages, sidebarWidth]);

  // Maintain bottom scroll positioning on window resize
  useEffect(() => {
    const handleResize = () => {
      const el = chatScrollRef.current;
      if (!el) return;
      const isAtBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 150;
      if (isAtBottom) {
        el.scrollTop = el.scrollHeight;
      }
    };
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  useEffect(() => {
    if (thoughtScrollRef.current) {
      thoughtScrollRef.current.scrollTop = thoughtScrollRef.current.scrollHeight;
    }
  }, [thoughts]);

  // Auto-resize textarea when text, sidebar width, or window size changes
  useEffect(() => {
    const adjustHeight = () => {
      if (textareaRef.current) {
        textareaRef.current.style.height = 'auto';
        textareaRef.current.style.height = `${Math.min(textareaRef.current.scrollHeight, 180)}px`;
      }
    };
    adjustHeight();
    window.addEventListener('resize', adjustHeight);
    return () => window.removeEventListener('resize', adjustHeight);
  }, [inputText, sidebarWidth]);

  useEffect(() => {
    if (isRecording) {
      micIntervalRef.current = setInterval(() => {
        setMicVisualizerWaves(Array(16).fill(0).map(() => Math.floor(Math.random() * 20) + 3));
      }, 90);
    } else {
      if (micIntervalRef.current) clearInterval(micIntervalRef.current);
      setMicVisualizerWaves(Array(16).fill(2));
    }
    return () => {
      if (micIntervalRef.current) clearInterval(micIntervalRef.current);
    };
  }, [isRecording]);

  const syncMascotMouthWithAudio = (audio: HTMLAudioElement) => {
    try {
      const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
      const audioContext = new AudioContextClass();
      audio.crossOrigin = "anonymous";
      const source = audioContext.createMediaElementSource(audio);
      const analyser = audioContext.createAnalyser();
      analyser.fftSize = 64;
      source.connect(analyser);
      analyser.connect(audioContext.destination);
      const bufferLength = analyser.frequencyBinCount;
      const dataArray = new Uint8Array(bufferLength);
      let syncInterval: any = null;
      
      const updateSpeechMouth = () => {
        if (audio.paused || audio.ended) {
          if (syncInterval) cancelAnimationFrame(syncInterval);
          emit('mascot-amplitude-changed', { amplitude: 0 }).catch(() => {});
          return;
        }
        analyser.getByteFrequencyData(dataArray);
        let sum = 0;
        for (let i = 0; i < bufferLength; i++) {
          sum += dataArray[i];
        }
        const average = sum / bufferLength;
        const normalized = average / 255;
        emit('mascot-amplitude-changed', { amplitude: normalized }).catch(() => {});
        syncInterval = requestAnimationFrame(updateSpeechMouth);
      };
      
      audio.addEventListener('play', () => {
        syncInterval = requestAnimationFrame(updateSpeechMouth);
      });
    } catch (e) {
      console.warn("Falling back to simulated speech mouth sync:", e);
      let syncInterval: any = null;
      let phase = 0;
      const simulateMouth = () => {
        if (audio.paused || audio.ended) {
          if (syncInterval) clearInterval(syncInterval);
          emit('mascot-amplitude-changed', { amplitude: 0 }).catch(() => {});
          return;
        }
        phase += 0.35;
        const amp = 0.2 + Math.abs(Math.sin(phase)) * 0.5 + Math.random() * 0.15;
        emit('mascot-amplitude-changed', { amplitude: amp }).catch(() => {});
      };
      
      audio.addEventListener('play', () => {
        syncInterval = setInterval(simulateMouth, 60);
      });
      const clearSim = () => {
        if (syncInterval) {
          clearInterval(syncInterval);
          syncInterval = null;
        }
        emit('mascot-amplitude-changed', { amplitude: 0 }).catch(() => {});
      };
      audio.addEventListener('pause', clearSim);
      audio.addEventListener('ended', clearSim);
    }
  };

  const speakResponse = async (text: string, lang: string = 'na') => {
    const cleanText = text.replace(/<[^>]*>/g, '').trim(); // strip XML/HTML tags
    if (!cleanText) return;

    try {
      const response = await fetch('http://127.0.0.1:8000/api/tts', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
          text: cleanText, 
          voice: selectedVoiceRef.current,
          lang: lang 
        })
      });
      if (response.ok) {
        const blob = await response.blob();
        const audioUrl = URL.createObjectURL(blob);
        const audio = new Audio(audioUrl);
        activeAudioRef.current = audio;
        
        syncMascotMouthWithAudio(audio);
        
        audio.onplay = () => {
          startMicBargeInMonitoring();
        };
        audio.onended = () => {
          stopMicBargeInMonitoring();
          URL.revokeObjectURL(audioUrl);
          if (activeAudioRef.current === audio) {
            activeAudioRef.current = null;
          }
        };
        audio.onerror = () => {
          stopMicBargeInMonitoring();
          URL.revokeObjectURL(audioUrl);
          if (activeAudioRef.current === audio) {
            activeAudioRef.current = null;
          }
        };
        
        audio.play().catch(e => {
          console.error("Audio playback error:", e);
          stopMicBargeInMonitoring();
          URL.revokeObjectURL(audioUrl);
          if (activeAudioRef.current === audio) {
            activeAudioRef.current = null;
          }
        });

      } else {
        console.warn("Backend TTS failed, falling back to browser SpeechSynthesis");
        throw new Error("TTS status error");
      }
    } catch (err) {
      window.speechSynthesis.cancel();
      const utterance = new SpeechSynthesisUtterance(cleanText);
      if (lang && lang !== 'na') {
        utterance.lang = lang;
      }
      try {
        const voices = window.speechSynthesis.getVoices();
        const isFemale = selectedVoiceRef.current.startsWith('F');
        let matchedVoice = null;
        if (isFemale) {
          matchedVoice = voices.find(v => /zira|hazel|susan|heera|mary|karen|female|girl/i.test(v.name));
        } else {
          matchedVoice = voices.find(v => /david|george|mark|ravi|male|boy/i.test(v.name));
        }
        if (matchedVoice) {
          utterance.voice = matchedVoice;
        }
      } catch (e) {
        console.warn("Failed to set browser fallback voice:", e);
      }
      
      let synthesisInterval: any = null;
      let phase = 0;
      utterance.onstart = () => {
        startMicBargeInMonitoring();
        synthesisInterval = setInterval(() => {
          phase += 0.35;
          const amp = 0.2 + Math.abs(Math.sin(phase)) * 0.5 + Math.random() * 0.15;
          emit('mascot-amplitude-changed', { amplitude: amp }).catch(() => {});
        }, 65);
      };
      
      const stopSynthesisMascotSync = () => {
        stopMicBargeInMonitoring();
        if (synthesisInterval) {
          clearInterval(synthesisInterval);
          synthesisInterval = null;
        }
        emit('mascot-amplitude-changed', { amplitude: 0 }).catch(() => {});
      };
      
      utterance.onend = stopSynthesisMascotSync;
      utterance.onerror = stopSynthesisMascotSync;
      
      window.speechSynthesis.speak(utterance);
    }
  };

  const handleSendCommand = async (textToSend?: string) => {
    let prompt = (textToSend || inputText).trim();
    if (!prompt) return;

    if (capturedImage && capturedOCR) {
      prompt += `\n\n[Foreground Screen Capture Attached]\nOCR text extracted from screen:\n${capturedOCR}`;
      setCapturedImage(null);
      setCapturedOCR('');
    }

    setFallbackNotice(null);
    const controller = new AbortController();
    setAbortController(controller);

    if (!textToSend) {
      setInputText('');
    }

    const userMsgId = 'user-' + Date.now();
    const userMsg: Message = {
      id: userMsgId,
      sender: 'user',
      text: prompt,
      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
    };

    setMessages(prev => [...prev, userMsg]);
    setIsRunning(true);

    const assistantMsgId = 'assistant-' + Date.now();
    const brainLabel = modelSettings.modelSource === 'local' ? modelSettings.brainModel : modelSettings.selectedModel;

    const delay = (ms: number) => new Promise((resolve, reject) => {
      const onAbort = () => {
        clearTimeout(timeout);
        reject(new DOMException("Aborted", "AbortError"));
      };
      const timeout = setTimeout(() => {
        controller.signal.removeEventListener('abort', onAbort);
        resolve(null);
      }, ms);
      controller.signal.addEventListener('abort', onAbort);
    });

    try {
      const response = await fetch('http://127.0.0.1:8000/api/chat/stream', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          prompt,
          modelSettings
        }),
        signal: controller.signal
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.statusText}`);
      }

      const reader = response.body?.getReader();
      if (!reader) {
        throw new Error("Response body is not readable");
      }

      const decoder = new TextDecoder("utf-8");
      let buffer = "";
      let hasCreatedAssistantMessage = false;
      let accumulatedText = "";

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        buffer = buffer.replace(/\r\n/g, '\n');

        let boundary = buffer.indexOf('\n\n');
        while (boundary !== -1) {
          const chunk = buffer.slice(0, boundary);
          buffer = buffer.slice(boundary + 2);

          if (chunk.trim()) {
            const lines = chunk.split('\n');
            let event = "";
            const dataParts: string[] = [];
            for (const line of lines) {
              if (line.startsWith("event: ")) {
                event = line.slice(7).trim();
              } else if (line.startsWith("event:")) {
                event = line.slice(6).trim();
              } else if (line.startsWith("data: ")) {
                dataParts.push(line.slice(6));
              } else if (line.startsWith("data:")) {
                dataParts.push(line.slice(5));
              }
            }
            const data = dataParts.join('\n');

            if (event === "thought" && data) {
              try {
                const thoughtData = JSON.parse(data);
                
                const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                if (isTauri) {
                  if (thoughtData.mascot_state) {
                    emit('mascot-state-changed', { state: thoughtData.mascot_state }).catch(console.error);
                  }
                  if (thoughtData.mascot_wardrobe) {
                    emit('mascot-wardrobe-changed', { item: thoughtData.mascot_wardrobe }).catch(console.error);
                  }
                  
                  const desktopTools = ["gui_click", "gui_double_click", "gui_drag", "gui_type", "gui_hotkey", "gui_scroll"];
                  if (thoughtData.type === "exec" && thoughtData.status === "running" && desktopTools.includes(thoughtData.tool)) {
                    emit('automation-state-changed', { active: true, tool: thoughtData.tool }).catch(console.error);
                  } else if (thoughtData.status === "completed" || thoughtData.status === "failed") {
                    emit('automation-state-changed', { active: false }).catch(console.error);
                  }
                }

                const targetId = thoughtData.id || ('thought-step-' + Date.now() + '-' + Math.random());
                
                setThoughts(prev => {
                  const exists = prev.some(t => t.id === targetId);
                  if (exists) {
                    return prev.map(t => {
                      if (t.id === targetId) {
                        return {
                          ...t,
                          type: thoughtData.type || t.type,
                          text: thoughtData.append ? (t.text + (thoughtData.text || '')) : (thoughtData.text !== undefined ? thoughtData.text : t.text),
                          tool: thoughtData.tool !== undefined ? thoughtData.tool : t.tool,
                          command: thoughtData.command !== undefined ? thoughtData.command : t.command,
                          status: thoughtData.status || t.status
                        };
                      }
                      return t;
                    });
                  } else {
                    const newStep: ThoughtStep = {
                      id: targetId,
                      type: thoughtData.type || 'info',
                      text: thoughtData.text || '',
                      tool: thoughtData.tool,
                      command: thoughtData.command,
                      timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
                      status: thoughtData.status || 'completed'
                    };
                    const updatedPrev = prev.map(t => t.status === 'running' ? { ...t, status: 'completed' as const } : t);
                    return [...updatedPrev, newStep];
                  }
                });
              } catch (e) {
                console.error("Failed to parse thought JSON:", e);
              }
            } else if (event === "text") {
              accumulatedText += data;
              const displayText = getStreamingChatText(accumulatedText);
              if (!hasCreatedAssistantMessage) {
                hasCreatedAssistantMessage = true;
                setMessages(prev => [
                  ...prev,
                  {
                    id: assistantMsgId,
                    sender: 'assistant',
                    text: displayText,
                    timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
                  }
                ]);
              } else {
                setMessages(prev => prev.map(msg => 
                  msg.id === assistantMsgId ? { ...msg, text: displayText } : msg
                ));
              }
            } else if (event === "confirmation" && data) {
              try {
                const confData = JSON.parse(data);
                setPendingConfirmation(confData);
              } catch (e) {
                console.error("Failed to parse confirmation JSON:", e);
              }
            }
          }
          boundary = buffer.indexOf('\n\n');
        }
      }

      if (buffer.trim()) {
        const lines = buffer.split('\n');
        let event = "";
        const dataParts: string[] = [];
        for (const line of lines) {
          if (line.startsWith("event: ")) {
            event = line.slice(7).trim();
          } else if (line.startsWith("event:")) {
            event = line.slice(6).trim();
          } {
            if (line.startsWith("data: ")) {
              dataParts.push(line.slice(6));
            } else if (line.startsWith("data:")) {
              dataParts.push(line.slice(5));
            }
          }
        }
        const data = dataParts.join('\n');
        if (event === "thought" && data) {
          try {
            const thoughtData = JSON.parse(data);
            
            const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
            if (isTauri) {
              if (thoughtData.mascot_state) {
                emit('mascot-state-changed', { state: thoughtData.mascot_state }).catch(console.error);
              }
              if (thoughtData.mascot_wardrobe) {
                emit('mascot-wardrobe-changed', { item: thoughtData.mascot_wardrobe }).catch(console.error);
              }
            }

            const targetId = thoughtData.id || ('thought-step-' + Date.now() + '-' + Math.random());
            setThoughts(prev => {
              const exists = prev.some(t => t.id === targetId);
              if (exists) {
                return prev.map(t => {
                  if (t.id === targetId) {
                    return {
                      ...t,
                      type: thoughtData.type || t.type,
                      text: thoughtData.append ? (t.text + (thoughtData.text || '')) : (thoughtData.text !== undefined ? thoughtData.text : t.text),
                      tool: thoughtData.tool !== undefined ? thoughtData.tool : t.tool,
                      command: thoughtData.command !== undefined ? thoughtData.command : t.command,
                      status: thoughtData.status || t.status
                    };
                  }
                  return t;
                });
              } else {
                const newStep: ThoughtStep = {
                  id: targetId,
                  type: thoughtData.type || 'info',
                  text: thoughtData.text || '',
                  tool: thoughtData.tool,
                  command: thoughtData.command,
                  timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
                  status: thoughtData.status || 'completed'
                };
                const updatedPrev = prev.map(t => t.status === 'running' ? { ...t, status: 'completed' as const } : t);
                return [...updatedPrev, newStep];
              }
            });
          } catch (e) {
            console.error("Failed to parse thought JSON:", e);
          }
        } else if (event === "text" && data) {
          accumulatedText += data;
          const displayText = getStreamingChatText(accumulatedText);
          if (!hasCreatedAssistantMessage) {
            setMessages(prev => [
              ...prev,
              {
                id: assistantMsgId,
                sender: 'assistant',
                text: displayText,
                timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
              }
            ]);
          } else {
            setMessages(prev => prev.map(msg => 
              msg.id === assistantMsgId ? { ...msg, text: displayText } : msg
            ));
          }
        } else if (event === "confirmation" && data) {
          try {
            const confData = JSON.parse(data);
            setPendingConfirmation(confData);
          } catch (e) {
            console.error("Failed to parse confirmation JSON:", e);
          }
        }
      }

      if (voiceOutputEnabled && accumulatedText) {
        const finalSpeech = getStreamingSpeechText(accumulatedText);
        const finalLang = getFinalLangCode(accumulatedText);
        speakResponse(finalSpeech, finalLang);
      }
      playUISound('success');

    } catch (err: any) {
      if (err.name === 'AbortError' || (err instanceof DOMException && err.name === 'AbortError')) {
        const abortThought: ThoughtStep = {
          id: 'abort-' + Date.now(),
          type: 'warning',
          text: 'Execution cancelled by user.',
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
          status: 'failed'
        };
        setThoughts(prev => [...prev, abortThought]);
        setMessages(prev => [
          ...prev, 
          {
            id: 'err-' + Date.now(),
            sender: 'assistant',
            text: "Request cancelled.",
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
          }
        ]);
      } else {
        console.warn("Backend streaming failed, falling back to simulator:", err);
        playUISound('error');
        const fallbackRes = getSimulatedResponse(prompt, brainLabel, modelSettings.ocrModel);
        
        const fallbackWarningThought: ThoughtStep = {
          id: 'fallback-warning-' + Date.now(),
          type: 'warning',
          text: `Host communication interrupt: ${err.message || 'Check connection settings'}. Swapping to simulation core.`,
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
          status: 'completed'
        };
        setThoughts(prev => [...prev, fallbackWarningThought]);

        for (const step of fallbackRes.steps) {
          if (controller.signal.aborted) throw new DOMException("Aborted", "AbortError");
          setThoughts(prev => [...prev, {
            ...step,
            id: 'thought-step-' + Date.now() + '-' + Math.random(),
            timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
          }]);
          await delay(15);
        }

        const words = fallbackRes.text.split(" ");
        let currentSimText = "";
        for (let i = 0; i < words.length; i++) {
          if (controller.signal.aborted) throw new DOMException("Aborted", "AbortError");
          const space = i > 0 ? " " : "";
          currentSimText += space + words[i];

          if (i === 0) {
            setMessages(prev => [
              ...prev,
              {
                id: assistantMsgId,
                sender: 'assistant',
                text: currentSimText,
                timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
              }
            ]);
          } else {
            setMessages(prev => prev.map(msg => 
              msg.id === assistantMsgId ? { ...msg, text: currentSimText } : msg
            ));
          }
          await delay(15);
        }

        if (voiceOutputEnabled && fallbackRes.text) {
          speakResponse(fallbackRes.text);
        }
      }
    } finally {
      setIsRunning(false);
      setAbortController(null);
    }
  };

  const handleConfirmResponse = async (id: string, approved: boolean) => {
    try {
      await fetch('http://127.0.0.1:8000/api/chat/confirm', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ id, approved })
      });
    } catch (err) {
      console.error("Failed to send confirmation:", err);
    }
    setPendingConfirmation(null);
  };

  const handleStopExecution = () => {
    if (abortController) {
      abortController.abort();
    }
    setIsRunning(false);
  };

  const toggleRecording = async () => {
    if (isRecording) {
      setIsRecording(false);
      return;
    }

    setIsRecording(true);
    try {
      const response = await fetch('http://127.0.0.1:8000/api/voice/record', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      setIsRecording(false);
      
      if (response.ok) {
        const data = await response.json();
        const transcribedText = data.text || "";
        if (transcribedText.trim()) {
          setInputText(transcribedText);
          return;
        }
      }
      throw new Error("Empty transcription or status error");
    } catch (err) {
      console.warn("Real mic recording failed or offline. Falling back to simulation.", err);
      const speechOptions = [
        "Check Screen layout and verify active window coordinates",
        "Organize PDF receipts under download directories recursively",
        "Show process list to find CPU and RAM load data",
        "Verify local network socket response diagnostics and parameters"
      ];
      const chosen = speechOptions[Math.floor(Math.random() * speechOptions.length)];
      
      setInputText(chosen);
    }
  };

  const triggerVoiceCommand = async () => {
    if (isRecording || isRunning) return;
    setIsRecording(true);
    
    try {
      const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
      const oscillator = audioContext.createOscillator();
      const gainNode = audioContext.createGain();
      oscillator.connect(gainNode);
      gainNode.connect(audioContext.destination);
      oscillator.type = 'sine';
      oscillator.frequency.setValueAtTime(600, audioContext.currentTime);
      gainNode.gain.setValueAtTime(0.05, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.001, audioContext.currentTime + 0.15);
      oscillator.start();
      oscillator.stop(audioContext.currentTime + 0.15);
    } catch (e) {
      console.warn("Failed to play start beep:", e);
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/api/voice/record', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        }
      });
      setIsRecording(false);
      
      if (response.ok) {
        const data = await response.json();
        const transcribedText = data.text || "";
        if (transcribedText.trim()) {
          await handleSendCommand(transcribedText);
        }
      }
    } catch (err) {
      console.error("Wake word voice capture failed:", err);
      setIsRecording(false);
    }
  };

  triggerVoiceCommandRef.current = triggerVoiceCommand;

  const handleClearHistory = async () => {
    try {
      await fetch('http://127.0.0.1:8000/api/chat/clear', { method: 'POST' });
    } catch (err) {
      console.error("Failed to clear chat history on backend:", err);
    }
    setMessages([
      {
        id: 'welcome-msg-purged',
        sender: 'assistant',
        text: "Registers purged safely. Daemon listener online.",
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
      }
    ]);
    setThoughts([
      {
        id: 'purge-thought',
        type: 'status',
        text: 'User cleared live tracing buffer stack.',
        timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
        status: 'completed'
      }
    ]);
  };

  const handleApplyPreset = (presetText: string) => {
    setInputText(presetText);
  };

  const handleMinimize = () => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      getCurrentWindow().minimize().catch(err => console.error("Minimize error:", err));
    }
  };

  const handleMaximize = () => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      getCurrentWindow().toggleMaximize().catch(err => console.error("Maximize error:", err));
    }
  };

  const handleClose = () => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      invoke('close_application').catch(err => console.error("Close application error:", err));
    }
  };

  // ── Offline docs search action ─────────────────────────────────────────────
  const handleSearchDocs = async (e?: React.FormEvent) => {
    if (e) e.preventDefault();
    if (!docsQuery.trim()) return;
    setIsSearchingDocs(true);
    try {
      const res = await fetch(`http://127.0.0.1:8000/api/docs/search?query=${encodeURIComponent(docsQuery)}`);
      if (res.ok) {
        const data = await res.json();
        if (data.status === 'success') {
          setDocsResults(data.results || []);
        }
      }
    } catch (err) {
      console.error("Failed to search offline documents:", err);
    } finally {
      setIsSearchingDocs(false);
    }
  };

  // ── HTML5 Drag and Drop File Ingestion ─────────────────────────────────────
  const handleHtmlFileDrop = async (e: React.DragEvent<HTMLDivElement>) => {
    e.preventDefault();
    setIsDragging(false);
    
    const files = Array.from(e.dataTransfer.files) as File[];
    if (files.length === 0) return;

    setIngestStatus('ingesting');
    setIngestMessage('');
    playUISound('click');

    try {
      for (const file of files) {
        const text = await new Promise<string>((resolve, reject) => {
          const reader = new FileReader();
          reader.onload = (evt) => resolve(evt.target?.result as string || '');
          reader.onerror = (evt) => reject(new Error('Failed to read file'));
          reader.readAsText(file);
        });

        const res = await fetch('http://127.0.0.1:8000/api/rag/ingest', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            source: file.name,
            text: text,
            metadata: { size: file.size, lastModified: file.lastModified }
          })
        });

        if (!res.ok) {
          const errData = await res.json();
          throw new Error(errData.detail || `Ingestion failed: ${res.statusText}`);
        }
      }

      setIngestStatus('success');
      setIngestMessage(`Successfully ingested ${files.length} file(s) into Turbovec RAG.`);
      playUISound('success');
    } catch (err: any) {
      setIngestStatus('error');
      setIngestMessage(err.message || 'Error ingesting files.');
      playUISound('error');
    }
  };

  const isTauriEnv = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;



  if (currentView === 'landing') {
    return (
      <div className={`flex flex-col min-h-screen bg-main-theme text-white font-sans antialiased selection:bg-theme-accent/30 selection:text-theme-accent overflow-y-auto justify-center ${theme !== 'default' ? 'theme-' + theme : ''}`}>
        <div className="flex-1 flex flex-col justify-between bg-main-theme relative min-h-[600px] py-12 px-6">
          <div className="absolute inset-0 bg-[radial-gradient(#1e1e1e_1.5px,transparent_1.5px)] [background-size:24px_24px] opacity-25 pointer-events-none"></div>
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[450px] h-[450px] bg-theme-accent/5 blur-[100px] rounded-full pointer-events-none"></div>

          <div className="max-w-md w-full mx-auto flex flex-col items-center text-center space-y-6 relative z-10 py-6">
            <div className="relative group">
              <div className="absolute inset-x-0 -inset-y-2 bg-theme-accent/10 rounded-full blur-2xl transition-all duration-300"></div>
              <img 
                src="/logo.png" 
                alt="Meridian Logo" 
                referrerPolicy="no-referrer" 
                className="w-20 h-20 sm:w-24 sm:h-24 object-contain relative z-10 transition-transform duration-500 hover:scale-105" 
                id="landing-logo"
              />
            </div>

            <div className="space-y-1">
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white font-display">
                Meridian
              </h1>
              <p className="text-xs text-theme-dim font-medium tracking-wide">
                Intelligent Workspace Assistant
              </p>
            </div>

            <div className="w-full bg-panel-theme/80 border border-theme rounded-2xl p-5 space-y-4 text-left shadow-xl">
              <div className="space-y-1.5">
                <label className="block text-[10px] font-semibold text-theme-dim uppercase tracking-wider">
                  Engine Source
                </label>
                <div className="grid grid-cols-2 gap-1.5 p-1 bg-main-theme border border-theme rounded-xl">
                  <button
                    onClick={() => setModelSettings(prev => ({ ...prev, modelSource: 'local' }))}
                    className={`py-1.5 text-xs font-bold font-mono rounded-lg transition-all cursor-pointer ${
                      modelSettings.modelSource === 'local'
                        ? 'bg-theme-accent text-black'
                        : 'text-theme-dim hover:text-theme-main'
                    }`}
                  >
                    Local Cluster
                  </button>
                  <button
                    onClick={() => setModelSettings(prev => ({ ...prev, modelSource: 'api' }))}
                    className={`py-1.5 text-xs font-bold font-mono rounded-lg transition-all cursor-pointer ${
                      modelSettings.modelSource === 'api'
                        ? 'bg-theme-accent text-black'
                        : 'text-theme-dim hover:text-theme-main'
                    }`}
                  >
                    API Gateway
                  </button>
                </div>
              </div>

              {modelSettings.modelSource === 'api' ? (
                <div className="space-y-4">
                  <div className="space-y-1.5">
                    <label className="block text-[10px] font-semibold text-theme-dim uppercase tracking-wider">
                      API Provider
                    </label>
                    <div className="relative">
                      <select
                        value={modelSettings.apiProvider || 'gemini'}
                        onChange={(e) => {
                          const val = e.target.value;
                          const available = PROVIDER_MODELS[val] || [];
                          setModelSettings(prev => ({
                            ...prev,
                            apiProvider: val,
                            selectedModel: available[0] || ''
                          }));
                        }}
                        className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main focus:text-theme-main rounded-xl px-3 py-2.5 text-xs font-sans tracking-wide appearance-none focus:outline-none focus:ring-1 focus:ring-theme-accent/40 cursor-pointer transition-all"
                      >
                        {API_PROVIDERS.map(p => (
                          <option key={p.id} value={p.id} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{p.name}</option>
                        ))}
                      </select>
                      <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-theme-dim">
                        <ChevronDown className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </div>

                  <div className="space-y-1.5">
                    <label className="block text-[10px] font-semibold text-theme-dim uppercase tracking-wider">
                      Cloud Core AI Model
                    </label>
                    <div className="relative">
                      <select
                        value={modelSettings.selectedModel}
                        onChange={(e) => setModelSettings(prev => ({ ...prev, selectedModel: e.target.value }))}
                        className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main focus:text-theme-main rounded-xl px-3 py-2.5 text-xs font-sans tracking-wide appearance-none focus:outline-none focus:ring-1 focus:ring-theme-accent/40 cursor-pointer transition-all"
                      >
                        {(PROVIDER_MODELS[modelSettings.apiProvider || 'gemini'] || []).map(m => (
                          <option key={m} value={m} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{m}</option>
                        ))}
                      </select>
                      <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-theme-dim">
                        <ChevronDown className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="space-y-4">
                  <div className="space-y-1.5">
                    <label className="block text-[10px] font-semibold text-theme-dim uppercase tracking-wider">
                      Brain Core AI Model
                    </label>
                    <div className="relative">
                      <select
                        value={modelSettings.brainModel}
                        onChange={(e) => setModelSettings(prev => ({ ...prev, brainModel: e.target.value }))}
                        className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main focus:text-theme-main rounded-xl px-3 py-2.5 text-xs font-sans tracking-wide appearance-none focus:outline-none focus:ring-1 focus:ring-theme-accent/40 cursor-pointer transition-all"
                      >
                        {localOllamaModels.map((model) => (
                          <option key={model} value={model} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>
                            {model}
                          </option>
                        ))}
                      </select>
                      <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-theme-dim">
                        <ChevronDown className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </div>

                  <div className="space-y-1.5">
                    <label className="block text-[10px] font-semibold text-theme-dim uppercase tracking-wider">
                      Vision Key Perception Core
                    </label>
                    <div className="relative">
                      <select
                        value={modelSettings.ocrModel}
                        onChange={(e) => setModelSettings(prev => ({ ...prev, ocrModel: e.target.value }))}
                        className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main focus:text-theme-main rounded-xl px-3 py-2.5 text-xs font-sans tracking-wide appearance-none focus:outline-none focus:ring-1 focus:ring-theme-accent/40 cursor-pointer transition-all"
                      >
                        {localVisionModels.map((model) => (
                          <option key={model} value={model} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>
                            {model}
                          </option>
                        ))}
                      </select>
                      <div className="pointer-events-none absolute inset-y-0 right-0 flex items-center px-3 text-theme-dim">
                        <ChevronDown className="w-3.5 h-3.5" />
                      </div>
                    </div>
                  </div>
                </div>
              )}
            </div>

            <button
              onClick={() => setCurrentView('app')}
              className="w-full py-3.5 bg-white hover:bg-theme-accent hover:border-theme-accent text-black rounded-xl text-xs font-semibold uppercase tracking-wider transition-all duration-200 cursor-pointer shadow-lg hover:shadow-theme-glow"
              id="launch-app-btn"
            >
              Enter Workspace Console
            </button>
          </div>

          <footer className="text-center text-[9px] text-theme-dim font-medium tracking-wide relative z-10 select-none py-2">
            © {new Date().getFullYear()} Meridian Labs. All rights reserved.
          </footer>
        </div>
      </div>
    );
  }

  const renderSettingsDropdownContent = () => {
    return (
      <div className="space-y-4">
        <div className="flex items-center justify-between pb-3 mb-4 border-b border-theme select-none">
          <span className="text-xs font-semibold flex items-center gap-2 text-theme-main">
            <Settings2 className="w-4 h-4 text-theme-accent" />
            Engine Settings
          </span>
          <span className="text-[10px] font-mono font-bold text-black bg-theme-accent px-3 py-0.5 rounded-full">
            {modelSettings.modelSource.toUpperCase()}
          </span>
        </div>

        {/* Source Toggle */}
        <div className="mb-4">
          <label className="block text-[10px] font-mono uppercase tracking-widest text-theme-dim mb-2 font-bold select-none">Engine Source</label>
          <div className="grid grid-cols-2 gap-1.5 p-1 bg-main-theme border border-theme rounded-xl">
            <button
              onMouseEnter={() => playUISound('hover')}
              onClick={() => {
                playUISound('click');
                setModelSettings(prev => ({ ...prev, modelSource: 'local' }));
              }}
              className={`py-1.5 text-xs font-bold font-mono rounded-lg transition-all cursor-pointer ${
                modelSettings.modelSource === 'local' ? 'bg-theme-accent text-black font-bold shadow-theme-glow' : 'text-theme-dim hover:text-theme-main'
              }`}
            >
              Local Cluster
            </button>
            <button
              onMouseEnter={() => playUISound('hover')}
              onClick={() => {
                playUISound('click');
                setModelSettings(prev => ({ ...prev, modelSource: 'api' }));
              }}
              className={`py-1.5 text-xs font-bold font-mono rounded-lg transition-all cursor-pointer ${
                modelSettings.modelSource === 'api' ? 'bg-theme-accent text-black font-bold shadow-theme-glow' : 'text-theme-dim hover:text-theme-main'
              }`}
            >
              API Gateway
            </button>
          </div>
        </div>

        {modelSettings.modelSource === 'api' ? (
          <div className="space-y-3.5 mb-4">
            <div>
              <label htmlFor="api-provider" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
                API Provider
              </label>
              <div className="relative">
                <select
                  id="api-provider"
                  value={modelSettings.apiProvider || 'gemini'}
                  onMouseEnter={() => playUISound('hover')}
                  onChange={(e) => {
                    playUISound('click');
                    const val = e.target.value;
                    const available = PROVIDER_MODELS[val] || [];
                    setModelSettings(prev => ({
                      ...prev,
                      apiProvider: val,
                      selectedModel: available[0] || ''
                    }));
                  }}
                  className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent cursor-pointer font-bold font-mono appearance-none transition-all duration-150"
                >
                  {API_PROVIDERS.map(p => (
                    <option key={p.id} value={p.id} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{p.name}</option>
                  ))}
                </select>
                <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
              </div>
            </div>

            <div>
              <label htmlFor="primary-api-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
                Cloud Core AI Model
              </label>
              <div className="relative">
                <select
                  id="primary-api-model"
                  value={modelSettings.selectedModel}
                  onMouseEnter={() => playUISound('hover')}
                  onChange={(e) => {
                    playUISound('click');
                    setModelSettings(prev => ({ ...prev, selectedModel: e.target.value }));
                  }}
                  className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent cursor-pointer font-bold font-mono appearance-none transition-all duration-150"
                >
                  {(PROVIDER_MODELS[modelSettings.apiProvider || 'gemini'] || []).map(m => (
                    <option key={m} value={m} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{m}</option>
                  ))}
                </select>
                <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
              </div>
            </div>
          </div>
        ) : (
          <div className="space-y-3.5 mb-4">
            <div>
              <label htmlFor="local-brain-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
                Local Brain Model
              </label>
              <div className="relative">
                <select
                  id="local-brain-model"
                  value={modelSettings.brainModel}
                  onMouseEnter={() => playUISound('hover')}
                  onChange={(e) => {
                    playUISound('click');
                    setModelSettings(prev => ({ ...prev, brainModel: e.target.value }));
                  }}
                  className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold appearance-none transition-all duration-150"
                >
                  {localOllamaModels.map(m => (
                    <option key={m} value={m} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{m}</option>
                  ))}
                </select>
                <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
              </div>
            </div>
            <div>
              <label htmlFor="local-ocr-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
                OCR Vision Engine
              </label>
              <div className="relative">
                <select
                  id="local-ocr-model"
                  value={modelSettings.ocrModel}
                  onMouseEnter={() => playUISound('hover')}
                  onChange={(e) => {
                    playUISound('click');
                    setModelSettings(prev => ({ ...prev, ocrModel: e.target.value }));
                  }}
                  className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold appearance-none transition-all duration-150"
                >
                  {localVisionModels.map(m => (
                    <option key={m} value={m} className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>{m}</option>
                  ))}
                </select>
                <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
              </div>
            </div>
          </div>
        )}

        {/* Voice Output Switch */}
        <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme border-b border-theme font-mono">
          <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">Voice Output (TTS)</span>
          <button 
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              setVoiceOutputEnabled(prev => !prev);
            }}
            className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${voiceOutputEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
          >
            <div className={`w-4 h-4 rounded-full bg-white transition-transform ${voiceOutputEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
          </button>
        </div>

        {voiceOutputEnabled && (
          <div className="mb-4 animate-fade-in">
            <label htmlFor="voice-selector" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
              Voice Style
            </label>
            <div className="relative">
              <select
                id="voice-selector"
                value={selectedVoice}
                onMouseEnter={() => playUISound('hover')}
                onChange={(e) => {
                  playUISound('click');
                  setSelectedVoice(e.target.value);
                }}
                className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold appearance-none transition-all duration-150"
              >
                <optgroup label="Male Voices" className="bg-zinc-950 text-zinc-400 font-bold" style={{ backgroundColor: 'var(--bg-main)', color: 'var(--text-dim)' }}>
                  <option value="M1" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>M1 - Authority / JARVIS</option>
                  <option value="M2" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>M2 - Natural / Technical</option>
                  <option value="M3" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>M3 - Deep / Command</option>
                  <option value="M4" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>M4 - Warm / Friendly</option>
                  <option value="M5" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>M5 - Crisp / Professional</option>
                </optgroup>
                <optgroup label="Female Voices" className="bg-zinc-950 text-zinc-400 font-bold" style={{ backgroundColor: 'var(--bg-main)', color: 'var(--text-dim)' }}>
                  <option value="F1" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>F1 - Clear / Assistant</option>
                  <option value="F2" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>F2 - Soft / Conversational</option>
                  <option value="F3" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>F3 - Energetic / Lively</option>
                  <option value="F4" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>F4 - Warm / Supportive</option>
                  <option value="F5" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>F5 - Crisp / Informative</option>
                </optgroup>
              </select>
              <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
            </div>
          </div>
        )}

        {/* Game Mode Switch */}
        <div className="flex flex-col gap-1 py-2.5 mb-2.5 border-t border-theme font-mono font-bold">
          <div className="flex items-center justify-between">
            <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">🎮 Game Mode</span>
            <button 
              onMouseEnter={() => playUISound('hover')}
              onClick={() => {
                playUISound('click');
                handleToggleGameMode(!gameMode);
              }}
              className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${gameMode ? 'bg-theme-accent animate-pulse' : 'bg-zinc-800'}`}
            >
              <div className={`w-4 h-4 rounded-full bg-white transition-transform ${gameMode ? 'translate-x-5' : 'translate-x-0'}`} />
            </button>
          </div>
          <p className="text-[9px] font-normal text-zinc-500 font-sans mt-0.5 leading-snug">
            Disables global hotkeys (Alt+M / Alt+Shift+M), hides mascot companion, and suppresses background notifications/nudges so you can play games.
          </p>
        </div>

        {/* Mascot Companion Switch */}
        <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme font-mono font-bold">
          <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">Mascot Companion</span>
          <button 
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              setMascotEnabled(prev => !prev);
            }}
            className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${mascotEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
          >
            <div className={`w-4 h-4 rounded-full bg-white transition-transform ${mascotEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
          </button>
        </div>

        {/* Pomodoro Focus Timer Switch */}
        <div className="flex flex-col gap-2 py-2.5 mb-2.5 border-t border-theme font-mono font-bold">
          <div className="flex items-center justify-between">
            <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">Pomodoro Focus</span>
            <button
              onMouseEnter={() => playUISound('hover')}
              onClick={() => {
                playUISound('click');
                setPomodoroActive(prev => !prev);
                if (!pomodoroActive) {
                  setPomodoroTime(25 * 60);
                }
              }}
              className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${pomodoroActive ? 'bg-theme-accent' : 'bg-zinc-800'}`}
            >
              <div className={`w-4 h-4 rounded-full bg-white transition-transform ${pomodoroActive ? 'translate-x-5' : 'translate-x-0'}`} />
            </button>
          </div>
          {pomodoroActive && (
            <div className="flex items-center justify-between text-[11px] text-zinc-400 font-mono mt-1 select-none">
              <span>Time Remaining:</span>
              <span className="font-bold text-theme-accent animate-pulse">
                {Math.floor(pomodoroTime / 60)}:{(pomodoroTime % 60).toString().padStart(2, '0')}
              </span>
            </div>
          )}
        </div>

        {/* Vocalize Alerts Switch */}
        <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme font-mono font-bold">
          <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">Vocalize Alerts</span>
          <button 
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              setAlertVocalizerEnabled(prev => !prev);
            }}
            className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${alertVocalizerEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
          >
            <div className={`w-4 h-4 rounded-full bg-white transition-transform ${alertVocalizerEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
          </button>
        </div>

        {/* UI Sound Effects Switch */}
        <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme font-mono font-bold">
          <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold select-none">UI Sound Effects</span>
          <button 
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              setUiSoundEnabled(prev => {
                const newVal = !prev;
                if (newVal) {
                  try {
                    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
                    if (AudioContextClass) {
                      const ctx = new AudioContextClass();
                      const osc = ctx.createOscillator();
                      const gain = ctx.createGain();
                      osc.frequency.setValueAtTime(800, ctx.currentTime);
                      gain.gain.setValueAtTime(0.04, ctx.currentTime);
                      gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.04);
                      osc.connect(gain);
                      gain.connect(ctx.destination);
                      osc.start();
                      osc.stop(ctx.currentTime + 0.04);
                    }
                  } catch (e) {}
                }
                return newVal;
              });
            }}
            className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${uiSoundEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
          >
            <div className={`w-4 h-4 rounded-full bg-white transition-transform ${uiSoundEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
          </button>
        </div>

        {/* WhatsApp Bridge Config Link */}
        <div className="mb-4 pt-2.5 border-t border-theme">
          <button
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              setShowWhatsAppQR(true);
            }}
            className="w-full bg-zinc-900 hover:bg-emerald-950/30 border border-zinc-800 hover:border-emerald-900/40 text-zinc-400 hover:text-emerald-400 font-bold py-2 rounded-xl text-xs text-center transition-all cursor-pointer uppercase tracking-wider flex items-center justify-center gap-2"
          >
            <Share2 className="w-3.5 h-3.5" />
            <span>Link WhatsApp Device</span>
          </button>
        </div>

        {/* Mascot Closet Selector */}
        <div className="mb-4 pt-2.5 border-t border-theme">
          <label htmlFor="mascot-wardrobe-selector" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
            🕶️ Mascot Closet
          </label>
          <div className="relative">
            <select
              id="mascot-wardrobe-selector"
              value={mascotWardrobe}
              onMouseEnter={() => playUISound('hover')}
              onChange={(e) => {
                playUISound('click');
                setMascotWardrobe(e.target.value);
              }}
              className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold appearance-none transition-all duration-150"
            >
              <option value="auto" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Auto-React Outfit</option>
              <option value="none" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>No Accessories</option>
              <option value="glasses" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Cyberpunk Glasses</option>
              <option value="construction_hat" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Diagnostics Hat</option>
              <option value="detective_hat" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Detective Hat</option>
              <option value="crown" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Royal Crown</option>
              <option value="dev_hoodie" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Developer Hoodie</option>
              <option value="cyberpunk_visor" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Neon Visor</option>
            </select>
            <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
          </div>
        </div>

        {/* Theme Switcher Selector */}
        <div className="mb-4">
          <label htmlFor="theme-selector" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold select-none">
            Visual Theme
          </label>
          <div className="relative">
            <select
              id="theme-selector"
              value={theme}
              onMouseEnter={() => playUISound('hover')}
              onChange={(e) => {
                playUISound('click');
                setTheme(e.target.value as any);
              }}
              className="w-full bg-main-theme border border-theme hover:border-theme-accent/50 text-theme-main rounded-xl py-2 pl-3 pr-8 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold appearance-none transition-all duration-150"
            >
              <option value="default" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Standard Orange</option>
              <option value="cyberpunk" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Cyberpunk Neo</option>
              <option value="amber" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Amber CRT</option>
              <option value="slate" className="bg-panel-theme text-theme-main" style={{ backgroundColor: 'var(--bg-panel)', color: 'var(--text-main)' }}>Midnight Slate</option>
            </select>
            <ChevronDown className="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-theme-dim" />
          </div>
        </div>

        <div className="pt-2.5 flex flex-col gap-2">
          <button
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              if (isTauriEnv) {
                handleRestartBackend();
              } else {
                alert("Backend restart is only available in the Desktop App.");
              }
            }}
            disabled={isRestartingBackend}
            className="w-full bg-zinc-900 hover:bg-red-950/30 border border-zinc-800 hover:border-red-900/40 text-zinc-400 hover:text-red-400 font-bold py-2 rounded-xl text-xs text-center transition-all cursor-pointer uppercase tracking-wider flex items-center justify-center gap-2 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {isRestartingBackend ? (
              <Loader2 className="w-3.5 h-3.5 animate-spin text-red-400" />
            ) : (
              <RefreshCw className="w-3.5 h-3.5" />
            )}
            {isRestartingBackend ? 'Restarting...' : 'Restart API Backend'}
          </button>
          <button
            onMouseEnter={() => playUISound('hover')}
            onClick={() => {
              playUISound('click');
              setSettingsOpen(null);
            }}
            className="w-full bg-white hover:bg-theme-accent hover:border-theme-accent border border-white text-black font-bold py-2 rounded-xl text-xs text-center transition-all cursor-pointer uppercase tracking-wider"
          >
            Apply Configs
          </button>
        </div>
      </div>
    );
  };

  return (
    <>
      <BackgroundCanvas theme={theme} />
      {isAutomating && (
        <div className="fixed bottom-4 right-4 bg-amber-500/10 border border-amber-500/50 rounded-lg px-4 py-2 shadow-[0_0_15px_rgba(245,158,11,0.3)] animate-pulse pointer-events-none z-50 flex items-center gap-2">
          <Activity className="h-4 w-4 text-amber-500 animate-spin" strokeWidth={2.5} />
          <span className="text-xs font-mono font-bold text-amber-400 uppercase tracking-wider">
            Automation Safeguard: {automatingTool} Active
          </span>
        </div>
      )}
      
      <div className={`flex flex-col h-screen overflow-hidden bg-main-theme text-white font-sans antialiased ${theme !== 'default' ? 'theme-' + theme : ''}`}>
        
        {/* HEADER BAR - Draggable Titlebar region */}
        <header data-tauri-drag-region className="flex items-center justify-between px-6 py-4 border-b border-theme bg-panel-theme-65 relative z-20 select-none cursor-default min-h-[72px]">
          <div data-tauri-drag-region className="flex items-center gap-3 shrink-0">
            <div className="flex items-center justify-center w-8 h-8">
              <img 
                src="/logo.png" 
                alt="Meridian Logo" 
                referrerPolicy="no-referrer" 
                className="w-8 h-8 object-contain" 
              />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-sm font-semibold tracking-tight text-white font-display">
                  Meridian
                </span>
                {backendConnected ? (
                  <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[9px] font-medium bg-emerald-500/10 text-emerald-400">
                    <span className="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span>
                    Connected
                  </span>
                ) : (
                  <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[9px] font-medium bg-rose-500/10 text-rose-400 animate-pulse">
                    <span className="w-1.5 h-1.5 rounded-full bg-rose-500"></span>
                    Backend Offline
                  </span>
                )}
                {!isTauriEnv && (
                  <span className="inline-flex items-center gap-1 px-2.5 py-0.5 rounded-full text-[9px] font-medium bg-amber-500/10 text-amber-400 border border-amber-500/20">
                    Browser Fallback
                  </span>
                )}
              </div>
              <p className="text-[10px] text-zinc-400 font-medium font-sans">Workspace Console</p>
            </div>
          </div>

          {/* TELEMETRY METRICS IN HEADER */}
          <div className="hidden sm:flex items-center gap-3 text-[11px] text-theme-dim mx-4">
            <div className="flex items-center gap-2.5 px-3 py-1 rounded-lg bg-panel-theme-40 border border-theme-40">
              <Cpu className="w-3.5 h-3.5 text-theme-dim shrink-0" />
              <span className="text-theme-dim font-semibold text-[10px] tracking-wide uppercase">CPU</span>
              <div className="w-14 h-1 bg-main-theme-50 rounded-full overflow-hidden shrink-0">
                <motion.div 
                  className="h-full bg-theme-accent"
                  initial={{ width: 0 }}
                  animate={{ width: `${telemetry.cpuUsage}%` }}
                  transition={{ type: "spring", stiffness: 70, damping: 14 }}
                />
              </div>
              <span className="font-mono text-theme-main font-bold text-[10px] min-w-[28px] text-right">
                {telemetry.cpuUsage}%
              </span>
            </div>

            <div className="flex items-center gap-2.5 px-3 py-1 rounded-lg bg-panel-theme-40 border border-theme-40">
              <Database className="w-3.5 h-3.5 text-theme-dim shrink-0" />
              <span className="text-theme-dim font-semibold text-[10px] tracking-wide uppercase">RAM</span>
              <div className="w-14 h-1 bg-main-theme-50 rounded-full overflow-hidden shrink-0">
                <motion.div 
                  className="h-full bg-theme-accent"
                  initial={{ width: 0 }}
                  animate={{ width: `${telemetry.ramUsage}%` }}
                  transition={{ type: "spring", stiffness: 70, damping: 14 }}
                />
              </div>
              <span className="font-mono text-theme-main font-bold text-[10px] min-w-[28px] text-right">
                {telemetry.ramUsage}%
              </span>
            </div>
          </div>

          {/* MODEL OPTIONS TRIGGER AND WINDOW CONTROLS */}
          <div className="flex items-center gap-2 relative shrink-0">
            <button
              onClick={() => {
                const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                if (isTauri) {
                  setMascotEnabled(prev => !prev);
                } else {
                  alert("Dynamic Island is only available in Desktop mode.");
                }
              }}
              title="Toggle Dynamic Island (Alt+Shift+M)"
              className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg border border-theme bg-panel-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40 text-xs font-medium tracking-wide transition-all cursor-pointer"
            >
              <Minimize2 className="w-3.5 h-3.5" />
              <span className="hidden md:inline">Dynamic Island</span>
            </button>

            <div className="relative">
              <button 
                id="settings-dropdown-toggle"
                onMouseEnter={() => playUISound('hover')}
                onClick={() => {
                  playUISound('click');
                  setSettingsOpen(prev => prev === 'header' ? null : 'header');
                }}
                className={`flex items-center gap-2 px-3 tracking-wide py-1.5 rounded-lg border text-xs font-semibold transition-all duration-150 cursor-pointer ${
                  settingsOpen === 'header'
                    ? 'bg-white border-white text-black' 
                    : 'bg-panel-theme border-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40'
                }`}
              >
                <Settings className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Configuration</span>
              </button>

              {/* CONFIGURATION DROPDOWN PANEL */}
              {settingsOpen === 'header' && (
                <div ref={settingsRef} className="absolute right-0 mt-3 w-80 bg-panel-theme border border-theme rounded-2xl p-5 z-40 text-left shadow-2xl shadow-theme-glow max-h-[80vh] overflow-y-auto scrollbar-thin">
                  {renderSettingsDropdownContent()}
                </div>
              )}
            </div>

            {/* Custom Titlebar Control Buttons */}
            <div className="flex items-center gap-1.5 border-l border-zinc-850 pl-2.5 ml-1">
              <button 
                onMouseEnter={() => playUISound('hover')}
                onClick={() => {
                  playUISound('click');
                  handleMinimize();
                }}
                title="Minimize Window"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-panel-theme hover:border-theme-accent/50 text-theme-dim hover:text-theme-main cursor-pointer transition-all"
              >
                <Minus className="w-3 h-3" />
              </button>
              <button 
                onMouseEnter={() => playUISound('hover')}
                onClick={() => {
                  playUISound('click');
                  handleMaximize();
                }}
                title="Maximize Window"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-panel-theme hover:border-theme-accent/50 text-theme-dim hover:text-theme-main cursor-pointer transition-all"
              >
                <Maximize2 className="w-3 h-3" />
              </button>
              <button 
                onMouseEnter={() => playUISound('hover')}
                onClick={() => {
                  playUISound('click');
                  handleClose();
                }}
                title="Close Application"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-red-950/25 hover:border-red-900 hover:text-red-500 text-theme-dim cursor-pointer transition-all"
              >
                <X className="w-3 h-3" />
              </button>
            </div>
          </div>
        </header>

        {/* WORKSPACE CONTENT GRID - Three Column Command Center */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* COLUMN 1: LEFT NAVIGATION STRIP (VERTICAL ICON RIBBON) */}
          <aside className="w-16 border-r border-theme bg-panel-theme flex flex-col items-center py-5 justify-between select-none shrink-0 z-20">
            <div className="flex flex-col gap-4.5 w-full items-center">
              {[
                { id: 'timeline', label: 'Timeline Hub', icon: Clock },
                { id: 'codemap', label: 'Code Map Network', icon: Link },
                { id: 'lobby', label: 'Swarm Debate Arena', icon: MessageSquare },
                { id: 'productivity', label: 'Productivity & Metrics', icon: Trophy },
                { id: 'docs', label: 'Local Search RAG', icon: BookOpen },
                { id: 'closet', label: 'Mascot Closet', icon: Shirt },
                { id: 'sandbox', label: 'Python Editor Sandbox', icon: Code },
                { id: 'jobs', label: 'Background Runs Scheduler', icon: Briefcase },
                { id: 'clipboard', label: 'Smart Clipboard history', icon: Clipboard }
              ].map(tab => {
                const isActive = sidebarTab === tab.id;
                const IconComponent = tab.icon;
                return (
                  <button
                    key={tab.id}
                    onMouseEnter={() => playUISound('hover')}
                    onClick={() => {
                      playUISound('click');
                      setSidebarTab(tab.id as any);
                    }}
                    title={tab.label}
                    className={`group relative p-3 rounded-xl transition-all cursor-pointer border ${
                      isActive
                        ? 'text-theme-accent bg-theme-accent-10 border-theme-accent-30 shadow-theme-glow'
                        : 'text-theme-dim hover:text-theme-main hover:bg-main-theme-40 border-transparent'
                    }`}
                  >
                    <IconComponent className="w-5 h-5 transition-transform group-hover:scale-110" />
                    {isActive && (
                      <div className="absolute left-0 top-1/4 bottom-1/4 w-[3px] bg-theme-accent rounded-r" />
                    )}
                  </button>
                );
              })}
            </div>

            <div className="flex flex-col items-center gap-4">
            <div className="flex flex-col items-center gap-4 relative">
              <button
                id="settings-ribbon-toggle"
                onMouseEnter={() => playUISound('hover')}
                onClick={() => {
                  playUISound('click');
                  setSettingsOpen(prev => prev === 'ribbon' ? null : 'ribbon');
                }}
                title="Configuration & Styles"
                className={`p-3 rounded-xl transition-all cursor-pointer border ${
                  settingsOpen === 'ribbon'
                    ? 'text-theme-accent bg-theme-accent-10 border-theme-accent-30'
                    : 'text-theme-dim hover:text-theme-main hover:bg-main-theme-40 border-transparent'
                }`}
              >
                <Settings className="w-5 h-5" />
              </button>
              {settingsOpen === 'ribbon' && (
                <div ref={settingsRef} className="absolute left-[72px] bottom-0 w-80 bg-panel-theme border border-theme rounded-2xl p-5 z-40 text-left shadow-2xl shadow-theme-glow max-h-[80vh] overflow-y-auto scrollbar-thin">
                  {renderSettingsDropdownContent()}
                </div>
              )}
            </div>
            </div>
          </aside>

          {/* COLUMN 2: CENTRAL CONSOLE VIEWPORT (DASHBOARD VIEWS) */}
          <div className="flex-1 flex flex-col min-w-0 bg-main-theme-20 overflow-hidden relative">
            <div className="flex items-center justify-between px-6 py-4 border-b border-theme bg-panel-theme-40 shrink-0 select-none">
              <div className="flex items-center gap-2.5">
                <span className="text-xs font-mono text-theme-accent uppercase font-bold tracking-widest">
                  {sidebarTab === 'timeline' && 'Timeline & Rollback Hub'}
                  {sidebarTab === 'codemap' && 'Codebase Dependency Map'}
                  {sidebarTab === 'lobby' && 'Multi-Agent Debate Lobby'}
                  {sidebarTab === 'productivity' && 'Telemetry & Achievements'}
                  {sidebarTab === 'docs' && 'Offline Document RAG Search'}
                  {sidebarTab === 'closet' && 'Mascot Closet Wardrobe'}
                  {sidebarTab === 'sandbox' && 'Python Execution Sandbox'}
                  {sidebarTab === 'jobs' && 'Background Jobs Scheduler'}
                  {sidebarTab === 'clipboard' && 'Smart Clipboard History'}
                </span>
              </div>
            </div>

            <div className="flex-1 overflow-y-auto min-h-0 relative">
              
              {/* TIMELINE HUB */}
              {sidebarTab === 'timeline' && (
                <div ref={thoughtScrollRef} className="flex-1 overflow-y-auto p-6 space-y-4 animate-fade-in max-h-full">
                  <div className="relative border-l border-zinc-800/80 ml-3.5 pl-6 space-y-6">
                    {thoughts.map((step, idx) => {
                      const isRunning = step.status === 'running';
                      const isFailed = step.status === 'failed';
                      
                      return (
                        <div key={step.id} className="relative group animate-fade-in">
                          <div className={`absolute -left-[32px] top-1.5 w-3 h-3 rounded-full border-2 transition-all ${
                            isRunning ? 'bg-theme-accent border-theme-accent animate-ping' :
                            isFailed ? 'bg-rose-500 border-rose-500' : 'bg-emerald-500 border-emerald-500'
                          }`} />
                          
                          <div className={`absolute -left-[32px] top-1.5 w-3 h-3 rounded-full border-2 ${
                            isRunning ? 'bg-theme-accent border-theme-accent' :
                            isFailed ? 'bg-rose-500 border-rose-500' : 'bg-emerald-500 border-emerald-500'
                          }`} />

                          <div className={`p-4 bg-main-theme-30 border border-theme rounded-2xl space-y-2 hover:border-theme-accent transition-all ${isFailed ? 'border-rose-950/40 bg-rose-950/5' : ''}`}>
                            <div className="flex items-center justify-between text-[9px] text-theme-dim font-mono">
                              <span className="uppercase font-bold tracking-wide text-theme-accent">Step {idx + 1}: {step.type}</span>
                              <span>{step.timestamp}</span>
                            </div>
                            
                            <p className="text-xs text-theme-main leading-relaxed font-sans break-words whitespace-pre-wrap select-text">{step.text}</p>
                            
                            {step.tool && (
                              <div className="flex items-center gap-1.5 mt-2 bg-main-theme-60 border border-theme-50 px-2.5 py-1 rounded-lg text-[10px] font-mono text-theme-dim">
                                <span className="w-1.5 h-1.5 rounded-full bg-theme-accent"></span>
                                <span>Service: <strong className="text-theme-main">{step.tool}</strong></span>
                              </div>
                            )}
                            
                            {step.command && (
                              <div className={`mt-1.5 text-[9px] font-mono p-3 rounded-xl border break-words whitespace-pre-wrap ${isFailed ? 'text-rose-400 bg-rose-950/20 border-rose-900/20' : 'text-theme-main bg-main-theme-60 border-theme'}`}>
                                <code>{step.command}</code>
                              </div>
                            )}
                            
                            {step.status === 'completed' && (
                              <div className="flex justify-end mt-2">
                                <button
                                  onClick={() => handleRollbackToCheckpoint(step.id)}
                                  className="px-3 py-1 bg-zinc-900 hover:bg-zinc-800 text-zinc-350 hover:text-white border border-zinc-800 rounded-lg text-[10px] font-semibold transition-all cursor-pointer flex items-center gap-1.5"
                                >
                                  <span>⏪ Rollback Workspace</span>
                                </button>
                              </div>
                            )}
                          </div>
                        </div>
                      );
                    })}
                    {thoughts.length === 0 && (
                      <div className="text-center py-10 text-zinc-500 text-xs font-sans">
                        No execution logs captured yet.
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* BACKGROUND JOBS */}
              {sidebarTab === 'jobs' && (
                <div className="flex-1 overflow-y-auto p-6 space-y-4 animate-fade-in">
                  {backgroundRuns.map((run) => {
                    const runTime = new Date(run.timestamp * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
                    const isExpanded = !!expandedRunIds[run.id];
                    const isSuccess = run.status === 'success';
                    const isRunning = run.status === 'running';

                    return (
                      <div 
                        key={run.id} 
                        className="p-4 bg-main-theme-30 border border-theme hover:border-theme-accent/50 rounded-2xl transition-all duration-200 space-y-3 shadow-md animate-fade-in"
                      >
                        <div className="flex items-center justify-between">
                          <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-[9px] font-bold uppercase tracking-wider ${
                            isSuccess ? 'bg-emerald-500/10 text-emerald-400' :
                            isRunning ? 'bg-amber-500/10 text-amber-400 animate-pulse' : 'bg-rose-500/10 text-rose-400'
                          }`}>
                            {run.status}
                          </span>
                          <span className="text-[10px] text-theme-dim font-mono">{runTime}</span>
                        </div>

                        <div>
                          <h4 className="text-xs font-bold text-white leading-relaxed font-sans">{run.goal}</h4>
                        </div>

                        {run.log && (
                          <div className="space-y-1.5">
                            <button
                              onClick={() => setExpandedRunIds(prev => ({ ...prev, [run.id]: !isExpanded }))}
                              className="text-[10px] font-semibold text-theme-accent hover:underline flex items-center gap-1 cursor-pointer transition-all"
                            >
                              <span>{isExpanded ? 'Hide Logs' : 'View Logs'}</span>
                              <ChevronDown className={`w-3 h-3 transition-transform duration-200 ${isExpanded ? 'rotate-180' : ''}`} />
                            </button>

                            {isExpanded && (
                              <pre className="p-3.5 bg-black/40 border border-theme rounded-xl text-[10px] font-mono text-theme-main select-all overflow-x-auto whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">
                                {run.log}
                              </pre>
                            )}
                          </div>
                        )}
                      </div>
                    );
                  })}
                  {backgroundRuns.length === 0 && (
                    <div className="text-center py-10 text-zinc-500 text-xs font-sans">
                      No background scheduler jobs recorded yet.
                    </div>
                  )}
                </div>
              )}

              {/* SMART CLIPBOARD */}
              {sidebarTab === 'clipboard' && (
                <div className="flex-1 overflow-y-auto p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="flex items-center gap-2 bg-main-theme-40 border border-theme p-2.5 rounded-xl shrink-0">
                    <input
                      type="text"
                      placeholder="Search clipboard segments..."
                      value={clipboardSearch}
                      onChange={(e) => setClipboardSearch(e.target.value)}
                      className="w-full bg-transparent border-none text-xs text-white placeholder-zinc-500 focus:outline-none focus:ring-0"
                    />
                  </div>
                  <div className="flex-1 overflow-y-auto space-y-3.5 pr-1">
                    {clipboardHistory
                      .filter(c => c.text.toLowerCase().includes(clipboardSearch.toLowerCase()))
                      .map((item, idx) => (
                        <div key={idx} className="p-4 bg-main-theme-30 border border-theme rounded-2xl space-y-3 hover:border-theme-accent/50 transition-all">
                          <div className="flex items-center justify-between text-[9px] text-theme-dim font-mono">
                            <span>SEGMENT #{clipboardHistory.length - idx}</span>
                            <span>{new Date(item.timestamp * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</span>
                          </div>
                          <pre className="p-3 bg-black/40 border border-theme rounded-xl text-[10px] font-mono text-zinc-350 select-all overflow-x-auto whitespace-pre-wrap max-h-36">
                            {item.text}
                          </pre>
                          <div className="flex items-center gap-2 flex-wrap">
                            <button
                              onClick={() => { navigator.clipboard.writeText(item.text); }}
                              className="px-3 py-1 bg-main-theme border border-theme hover:border-theme-accent-30 text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold transition-all cursor-pointer"
                            >
                              Copy Text
                            </button>
                            <button
                              onClick={() => { handleSendCommand(`Refactor this code: \n\n\`\`\`python\n${item.text}\n\`\`\``); }}
                              className="px-3 py-1 bg-main-theme border border-theme hover:border-theme-accent-30 text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold transition-all cursor-pointer flex items-center gap-1.5"
                            >
                              <Sparkles className="w-3 h-3 text-theme-accent" />
                              <span>Refactor</span>
                            </button>
                            <button
                              onClick={() => { handleSendCommand(`Explain this code and outline key logic details: \n\n\`\`\`python\n${item.text}\n\`\`\``); }}
                              className="px-3 py-1 bg-main-theme border border-theme hover:border-theme-accent-30 text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold transition-all cursor-pointer flex items-center gap-1.5"
                            >
                              <Terminal className="w-3 h-3 text-theme-accent" />
                              <span>Explain</span>
                            </button>
                            <button
                              onClick={() => { handleSendCommand(`Generate comprehensive unit tests for this code block: \n\n\`\`\`python\n${item.text}\n\`\`\``); }}
                              className="px-3 py-1 bg-main-theme border border-theme hover:border-theme-accent-30 text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold transition-all cursor-pointer flex items-center gap-1.5"
                            >
                              <CheckCircle2 className="w-3 h-3 text-theme-accent" />
                              <span>Tests</span>
                            </button>
                          </div>
                        </div>
                      ))}
                    {clipboardHistory.length === 0 && (
                      <div className="text-center py-10 text-zinc-500 text-xs font-sans">
                        No clipboard segments indexed in database yet.
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* TELEMETRY & PRODUCTIVITY */}
              {sidebarTab === 'productivity' && (
                <div className="flex-1 overflow-y-auto p-6 space-y-5 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="grid grid-cols-2 gap-4 shrink-0">
                    <div className="p-4 rounded-2xl text-center space-y-1.5 glass-card border border-theme accent-glow-hover">
                      <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider block font-bold">Tasks Executed</span>
                      <span className="text-2xl font-extrabold text-white font-mono tracking-tight drop-shadow-[0_0_8px_rgba(255,255,255,0.2)]">{devStats.total_tasks}</span>
                    </div>
                    <div className="p-4 rounded-2xl text-center space-y-1.5 glass-card border border-theme accent-glow-hover">
                      <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider block font-bold">Success Rate</span>
                      <span className="text-2xl font-extrabold text-theme-accent font-mono tracking-tight drop-shadow-[0_0_10px_var(--accent-glow)]">
                        {devStats.total_tasks > 0 ? `${Math.round((devStats.success_tasks / devStats.total_tasks) * 100)}%` : '100%'}
                      </span>
                    </div>
                    <div className="p-4 rounded-2xl text-center space-y-1.5 glass-card border border-theme accent-glow-hover">
                      <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider block font-bold">Security Audits</span>
                      <span className="text-2xl font-extrabold text-theme-accent font-mono tracking-tight drop-shadow-[0_0_10px_var(--accent-glow)]">{devStats.security_audits}</span>
                    </div>
                    <div className="p-4 rounded-2xl text-center space-y-1.5 glass-card border border-theme accent-glow-hover">
                      <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider block font-bold">Focus Pomodoros</span>
                      <span className="text-2xl font-extrabold text-amber-400 font-mono tracking-tight flex items-center justify-center gap-1.5 drop-shadow-[0_0_10px_rgba(245,158,11,0.25)]">
                        <Crown className="w-5 h-5 text-amber-500 fill-amber-500/20 animate-bounce" />
                        <span>{devStats.pomodoros}</span>
                      </span>
                    </div>
                  </div>

                  {/* Telemetry charts */}
                  <div className="grid grid-cols-2 gap-4 flex-grow min-h-0">
                    <div className="rounded-2xl p-4 flex flex-col min-h-0 glass-card">
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider font-bold">CPU Usage History</span>
                        <span className="text-[11px] font-mono text-white font-extrabold drop-shadow-[0_0_5px_rgba(255,255,255,0.25)]">{telemetry.cpuUsage}%</span>
                      </div>
                      <div className="flex-grow min-h-[90px] relative border-b border-l border-zinc-800/80 bg-black/25 rounded-bl">
                        <svg className="w-full h-full animate-fade-in" viewBox="0 0 100 40" preserveAspectRatio="none">
                          <defs>
                            <linearGradient id="cpuGrad" x1="0" y1="0" x2="0" y2="1">
                              <stop offset="0%" stopColor="var(--accent)" stopOpacity="0.35"/>
                              <stop offset="100%" stopColor="var(--accent)" stopOpacity="0.0"/>
                            </linearGradient>
                            <filter id="glow-chart">
                              <feGaussianBlur stdDeviation="1" result="blur" />
                              <feComposite in="SourceGraphic" in2="blur" operator="over" />
                            </filter>
                          </defs>
                          <g stroke="rgba(255,255,255,0.04)" strokeWidth="0.5">
                            <line x1="0" y1="10" x2="100" y2="10" /><line x1="0" y1="20" x2="100" y2="20" /><line x1="0" y1="30" x2="100" y2="30" />
                            <line x1="25" y1="0" x2="25" y2="40" /><line x1="50" y1="0" x2="50" y2="40" /><line x1="75" y1="0" x2="75" y2="40" />
                          </g>
                          <path
                            d={`M 0 40 L ${telemetry.cpuHistory.map((val, idx) => `${(idx / (telemetry.cpuHistory.length - 1)) * 100} ${40 - (val / 100) * 40}`).join(' L ')} L 100 40 Z`}
                            fill="url(#cpuGrad)"
                          />
                          <path
                            d={`M ${telemetry.cpuHistory.map((val, idx) => `${(idx / (telemetry.cpuHistory.length - 1)) * 100} ${40 - (val / 100) * 40}`).join(' L ')}`}
                            fill="none"
                            stroke="var(--accent)"
                            strokeWidth="1.8"
                            strokeLinecap="round"
                            filter="url(#glow-chart)"
                          />
                        </svg>
                      </div>
                    </div>

                    <div className="rounded-2xl p-4 flex flex-col min-h-0 glass-card">
                      <div className="flex items-center justify-between mb-2">
                        <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider font-bold">RAM Load History</span>
                        <span className="text-[11px] font-mono text-[#14b8a6] font-extrabold drop-shadow-[0_0_5px_rgba(20,184,166,0.25)]">{telemetry.ramUsage}%</span>
                      </div>
                      <div className="flex-grow min-h-[90px] relative border-b border-l border-zinc-800/80 bg-black/25 rounded-bl">
                        <svg className="w-full h-full animate-fade-in" viewBox="0 0 100 40" preserveAspectRatio="none">
                          <defs>
                            <linearGradient id="ramGrad" x1="0" y1="0" x2="0" y2="1">
                              <stop offset="0%" stopColor="#14b8a6" stopOpacity="0.3"/>
                              <stop offset="100%" stopColor="#14b8a6" stopOpacity="0.0"/>
                            </linearGradient>
                          </defs>
                          <g stroke="rgba(255,255,255,0.04)" strokeWidth="0.5">
                            <line x1="0" y1="10" x2="100" y2="10" /><line x1="0" y1="20" x2="100" y2="20" /><line x1="0" y1="30" x2="100" y2="30" />
                            <line x1="25" y1="0" x2="25" y2="40" /><line x1="50" y1="0" x2="50" y2="40" /><line x1="75" y1="0" x2="75" y2="40" />
                          </g>
                          <path
                            d={`M 0 40 L ${telemetry.ramHistory.map((val, idx) => `${(idx / (telemetry.ramHistory.length - 1)) * 100} ${40 - (val / 100) * 40}`).join(' L ')} L 100 40 Z`}
                            fill="url(#ramGrad)"
                          />
                          <path
                            d={`M ${telemetry.ramHistory.map((val, idx) => `${(idx / (telemetry.ramHistory.length - 1)) * 100} ${40 - (val / 100) * 40}`).join(' L ')}`}
                            fill="none"
                            stroke="#14b8a6"
                            strokeWidth="1.8"
                            strokeLinecap="round"
                            filter="url(#glow-chart)"
                          />
                        </svg>
                      </div>
                    </div>
                  </div>

                  {/* Achievements Grid */}
                  <div className="p-4 flex flex-col min-h-0 shrink-0 space-y-2 glass-card rounded-2xl">
                    <span className="text-[9px] font-mono text-theme-dim uppercase tracking-wider font-bold">
                      🏆 Developer Achievements
                    </span>
                    <div className="grid grid-cols-2 gap-3">
                      {[
                        {
                          id: 'bug_hunter',
                          title: 'Bug Hunter',
                          description: 'Heal a file error',
                          icon: '🐛',
                          unlocked: (devStats.successful_heals || 0) >= 1,
                          progress: `${devStats.successful_heals || 0}/1`
                        },
                        {
                          id: 'deep_focus',
                          title: 'Deep Focus',
                          description: 'Complete a Pomodoro',
                          icon: '⏱️',
                          unlocked: (devStats.pomodoros || 0) >= 1,
                          progress: `${devStats.pomodoros || 0}/1`
                        },
                        {
                          id: 'fortress',
                          title: 'Fortress',
                          description: '2+ security audits',
                          icon: '🛡️',
                          unlocked: (devStats.security_audits || 0) >= 2,
                          progress: `${devStats.security_audits || 0}/2`
                        },
                        {
                          id: 'git_master',
                          title: 'Git Master',
                          description: '5+ workspace commits',
                          icon: '🌿',
                          unlocked: (devStats.git_commits || 0) >= 5,
                          progress: `${devStats.git_commits || 0}/5`
                        }
                      ].map(ach => (
                        <div 
                          key={ach.id} 
                          className={`p-3 border rounded-xl flex items-center gap-2.5 transition-all relative overflow-hidden accent-glow-hover ${
                            ach.unlocked 
                              ? 'glass-card-accent border-purple-500/40 text-purple-300 shadow-[0_0_10px_rgba(168,85,247,0.15)]' 
                              : 'bg-black/20 border-zinc-800/80 opacity-50 grayscale'
                          }`}
                        >
                          <div className="text-xl relative shrink-0">
                            {ach.icon}
                            {!ach.unlocked && (
                              <div className="absolute inset-0 bg-black/60 flex items-center justify-center rounded-md text-[10px]">
                                🔒
                              </div>
                            )}
                          </div>
                          <div className="flex-grow min-w-0">
                            <h4 className={`text-[10px] font-bold truncate ${ach.unlocked ? 'text-purple-300' : 'text-zinc-400'}`}>
                              {ach.title}
                            </h4>
                            <p className="text-[8px] text-zinc-500 truncate leading-tight">
                              {ach.description}
                            </p>
                            <span className="text-[8px] font-mono text-zinc-650 block mt-0.5">
                              Progress: {ach.progress}
                            </span>
                          </div>
                          {ach.unlocked && (
                            <div className="absolute right-1 top-1 w-1.5 h-1.5 rounded-full bg-purple-400 animate-ping" />
                          )}
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              )}

              {/* OFFLINE SEARCH */}
              {sidebarTab === 'docs' && (
                <div className="p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <form onSubmit={handleSearchDocs} className="flex gap-2 bg-main-theme-40 border border-theme p-2.5 rounded-xl shrink-0">
                    <BookOpen className="w-5 h-5 text-theme-dim self-center ml-2" />
                    <input
                      type="text"
                      placeholder="Search offline RAG documentation library..."
                      value={docsQuery}
                      onChange={(e) => setDocsQuery(e.target.value)}
                      onMouseEnter={() => playUISound('hover')}
                      className="flex-1 bg-transparent border-none text-xs text-white placeholder-zinc-500 focus:outline-none focus:ring-0 font-sans"
                    />
                    <button
                      type="submit"
                      disabled={isSearchingDocs}
                      onMouseEnter={() => playUISound('hover')}
                      className="px-4 py-1.5 bg-white text-black font-bold rounded-lg text-xs hover:bg-theme-accent transition-all cursor-pointer flex items-center gap-1"
                    >
                      {isSearchingDocs ? <Loader2 className="w-3 h-3 animate-spin text-black" /> : <BookOpen className="w-3 h-3" />}
                      <span>Search</span>
                    </button>
                  </form>

                  <div className="flex-grow overflow-y-auto space-y-3.5 pr-1 flex flex-col min-h-0">
                    <div className="flex-grow space-y-3.5 min-h-[150px]">
                      {docsResults.length > 0 ? (
                        docsResults.map((result, idx) => (
                          <div key={idx} className="p-4 bg-main-theme-30 border border-theme rounded-2xl space-y-2 hover:border-theme-accent/50 transition-all select-text">
                            <div className="flex items-center justify-between text-xs font-mono">
                              <span className="text-theme-accent font-bold">📄 {result.title || result.file_path || 'Document'}</span>
                              {result.score !== undefined && (
                                <span className="text-emerald-400 font-bold">{Math.round(result.score * 100)}% match</span>
                              )}
                            </div>
                            <p className="text-xs text-theme-dim font-sans leading-relaxed select-text italic">
                              "... {result.content || result.snippet} ..."
                            </p>
                            <div className="flex justify-end">
                              <button
                                onMouseEnter={() => playUISound('hover')}
                                onClick={() => {
                                  playUISound('click');
                                  const prompt = `Analyze document "${result.title || result.file_path}": "${result.content || result.snippet}". Please explain: `;
                                  setInputText(prompt);
                                }}
                                className="px-2.5 py-1 bg-main-theme border border-theme hover:border-theme-accent-30 text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold transition-all cursor-pointer"
                              >
                                Use Context
                              </button>
                            </div>
                          </div>
                        ))
                      ) : docsQuery ? (
                        <div className="text-center py-10 text-zinc-500 text-xs font-sans select-none">
                          No matching documents found.
                        </div>
                      ) : (
                        <div className="flex-grow flex flex-col items-center justify-center text-center p-6 text-theme-dim h-full select-none">
                          <span className="text-4xl mb-3">📚</span>
                          <p className="text-xs font-semibold leading-relaxed">Local Documentation Search (RAG)</p>
                          <p className="text-[11px] max-w-xs mt-1 leading-normal text-zinc-500">
                            Search through your workspace's local documentation libraries. Results are retrieved from our local vector database offline.
                          </p>
                        </div>
                      )}
                    </div>

                    {/* Drag and Drop ingestion zone */}
                    <div
                      onDragOver={(e) => {
                        e.preventDefault();
                        setIsDragging(true);
                      }}
                      onDragLeave={() => setIsDragging(false)}
                      onDrop={handleHtmlFileDrop}
                      className={`shrink-0 border-2 border-dashed rounded-2xl p-6 text-center transition-all mt-4 ${
                        isDragging
                          ? 'border-theme-accent bg-theme-accent-10/20 shadow-theme-glow'
                          : 'border-theme bg-panel-theme-40 hover:border-theme-accent/40'
                      }`}
                    >
                      <div className="flex flex-col items-center justify-center space-y-2 select-none">
                        <span className="text-2xl animate-bounce">📥</span>
                        <p className="text-xs font-semibold text-theme-main">
                          Drag and drop documentation files here
                        </p>
                        <p className="text-[10px] text-theme-dim">
                          Supports text documents (FileReader ingestion for browser, Tauri native paths ingestion)
                        </p>
                      </div>

                      {ingestStatus !== 'idle' && (
                        <div className="mt-4 p-3.5 rounded-xl border flex items-center justify-center gap-2 text-xs font-medium bg-main-theme-30">
                          {ingestStatus === 'ingesting' && (
                            <div className="flex items-center gap-2 text-amber-400">
                              <Loader2 className="w-3.5 h-3.5 animate-spin" />
                              <span>Ingesting files into local RAG DB...</span>
                            </div>
                          )}
                          {ingestStatus === 'success' && (
                            <div className="flex items-center gap-2 text-teal-400">
                              <CheckCircle2 className="w-3.5 h-3.5" />
                              <span>{ingestMessage}</span>
                            </div>
                          )}
                          {ingestStatus === 'error' && (
                            <div className="flex items-center gap-2 text-rose-400">
                              <AlertCircle className="w-3.5 h-3.5" />
                              <span>{ingestMessage}</span>
                            </div>
                          )}
                        </div>
                      )}
                    </div>

                  </div>
                </div>
              )}

              {/* MASCOT CLOSET */}
              {sidebarTab === 'closet' && (
                <div className="p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="shrink-0 flex flex-col space-y-1 bg-black/40 border border-theme rounded-2xl p-4">
                    <span className="text-xs font-bold text-white font-display">🕶️ Wardrobe Customization</span>
                    <p className="text-[11px] text-theme-dim leading-relaxed">
                      Dress up Meridian's animated companion character. By default, Auto-React allows Meridian to automatically change outfits based on active tasks (diagnostic helmet when healing, crown when focused, detective hat when scanning logs).
                    </p>
                  </div>

                  <div className="flex-grow overflow-y-auto pr-1">
                    <div className="grid grid-cols-2 gap-4">
                      {[
                        { id: 'auto', name: 'Auto-React Outfit', emoji: '🤖', desc: 'Reacts to agent status' },
                        { id: 'none', name: 'Standard Outfit', emoji: '⚙️', desc: 'No special accessories' },
                        { id: 'glasses', name: 'Cyberpunk Glasses', emoji: '🕶️', desc: 'Cool neon shades' },
                        { id: 'construction_hat', name: 'Diagnostics Helmet', emoji: '🪖', desc: 'Equipped during codebase healing' },
                        { id: 'detective_hat', name: 'Detective Fedora', emoji: '🕵️', desc: 'Equipped during system audits' },
                        { id: 'crown', name: 'Royal Crown', emoji: '👑', desc: 'Equipped when focus metric is hit' },
                        { id: 'dev_hoodie', name: 'Developer Hoodie', emoji: '🧥', desc: 'Comfortable slate grey hoodie' },
                        { id: 'cyberpunk_visor', name: 'Neon Cyber Goggles', emoji: '🽿', desc: 'Futuristic visor overlays' }
                      ].map(item => {
                        const isEquipped = mascotWardrobe === item.id;
                        return (
                          <button
                            key={item.id}
                            onClick={() => {
                              setMascotWardrobe(item.id);
                              localStorage.setItem('meridian_mascot_wardrobe', item.id);
                              const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                              if (isTauri) {
                                emit('mascot-wardrobe-changed', { item: item.id }).catch(console.error);
                              }
                            }}
                            className={`p-3.5 border rounded-2xl text-left transition-all relative overflow-hidden flex flex-col justify-between h-28 cursor-pointer ${
                              isEquipped
                                ? 'glass-card-accent border-theme-accent shadow-theme-glow text-theme-main'
                                : 'bg-main-theme-30 border-theme text-theme-dim hover:border-theme-accent-30'
                            }`}
                          >
                            <div className="flex items-center justify-between w-full">
                              <span className="text-2xl">{item.emoji}</span>
                              {isEquipped && (
                                <span className="text-[9px] font-mono font-bold text-black bg-theme-accent px-2 py-0.5 rounded-full uppercase">
                                  Equipped
                                </span>
                              )}
                            </div>
                            <div>
                              <h4 className="text-xs font-bold text-white">{item.name}</h4>
                              <p className="text-[10px] text-zinc-500 leading-tight mt-0.5 truncate">{item.desc}</p>
                            </div>
                          </button>
                        );
                      })}
                    </div>
                  </div>
                </div>
              )}

              {/* PYTHON SCRIPT SANDBOX */}
              {sidebarTab === 'sandbox' && (
                <div className="flex-1 overflow-y-auto p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="flex-grow flex flex-col min-h-[160px] border border-theme rounded-2xl overflow-hidden bg-black/40">
                    <div className="px-4 py-2.5 border-b border-theme bg-main-theme/50 flex items-center justify-between shrink-0 select-none">
                      <span className="text-[10px] font-mono text-theme-dim font-bold uppercase tracking-wider">
                        Python Script Editor
                      </span>
                      <span className="text-[9px] text-theme-accent italic font-semibold">Isolated Sandbox</span>
                    </div>
                    <textarea
                      value={sandboxCode}
                      onChange={(e) => setSandboxCode(e.target.value)}
                      className="flex-1 p-4 bg-transparent text-theme-main font-mono text-xs focus:outline-none resize-none overflow-y-auto scrollbar-thin border-none"
                      disabled={sandboxStatus === 'auditing' || sandboxStatus === 'executing'}
                    />
                  </div>

                  <div className="flex items-center justify-between shrink-0 select-none">
                    <span className="text-[10px] font-mono text-theme-dim uppercase tracking-wider font-bold">
                      Runner Status: 
                      <span className={`ml-1.5 font-bold ${
                        sandboxStatus === 'success' ? 'text-teal-400' :
                        sandboxStatus === 'blocked' ? 'text-red-400' :
                        sandboxStatus === 'syntax_error' ? 'text-amber-500 animate-pulse' :
                        sandboxStatus === 'auditing' || sandboxStatus === 'executing' ? 'text-amber-400 animate-pulse' : 'text-zinc-500'
                      }`}>
                        {sandboxStatus.toUpperCase()}
                      </span>
                    </span>

                    <div className="flex gap-2">
                      {sandboxStatus === 'syntax_error' && (
                        <button
                          onClick={handleHealSandboxCode}
                          className="px-3.5 py-1.5 bg-amber-500 hover:shadow-[0_0_15px_rgba(245,158,11,0.35)] text-black rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5"
                        >
                          <Sparkles className="w-3.5 h-3.5 fill-black" />
                          <span>Auto-Heal Code</span>
                        </button>
                      )}
                      <button
                        onClick={handleRunSandbox}
                        disabled={sandboxStatus === 'auditing' || sandboxStatus === 'executing'}
                        className="px-4.5 py-1.5 bg-white hover:bg-theme-accent hover:border-theme-accent disabled:opacity-40 text-black rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center gap-1.5"
                      >
                        {sandboxStatus === 'auditing' || sandboxStatus === 'executing' ? (
                          <Loader2 className="w-3.5 h-3.5 animate-spin text-black" />
                        ) : (
                          <Terminal className="w-3.5 h-3.5" />
                        )}
                        <span>Execute</span>
                      </button>
                    </div>
                  </div>

                  {sandboxAuditorReasoning && (
                    <div className="p-3.5 bg-panel-theme border border-theme rounded-xl space-y-1 shrink-0 select-text">
                      <span className="text-[9px] font-bold text-theme-accent uppercase font-mono block">Security Audit Reasoning:</span>
                      <p className="text-[11px] text-theme-main font-sans leading-relaxed">{sandboxAuditorReasoning}</p>
                    </div>
                  )}

                  <div className="flex-grow flex flex-col min-h-[140px] border border-theme rounded-xl overflow-hidden bg-black/50">
                    <div className="px-4 py-2 border-b border-theme bg-main-theme/30 flex items-center justify-between shrink-0 select-none">
                      <span className="text-[9px] font-mono text-zinc-500 uppercase tracking-wider font-bold">
                        Sandbox Output / STDERR
                      </span>
                      <button
                        onClick={() => setSandboxOutput('')}
                        className="text-[9px] text-zinc-500 hover:text-zinc-355 cursor-pointer"
                      >
                        Clear Log
                      </button>
                    </div>
                    <pre className="flex-grow p-3.5 text-[10px] font-mono text-zinc-300 select-all overflow-x-auto whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">
                      {sandboxOutput || (
                        <span className="text-zinc-600 italic">Execute code to see output logs here...</span>
                      )}
                    </pre>
                  </div>
                </div>
              )}

              {/* SWARM DEBATE ARENA */}
              {sidebarTab === 'lobby' && (
                <div className="flex-1 overflow-y-auto p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="shrink-0 flex flex-col space-y-2.5 border border-theme rounded-2xl p-4 bg-black/40">
                    <span className="text-[10px] font-mono text-theme-dim font-bold uppercase tracking-wider block">
                      💬 Multi-Agent Debate Prompt
                    </span>
                    <textarea
                      value={lobbyPrompt}
                      onChange={(e) => setLobbyPrompt(e.target.value)}
                      placeholder="Describe the code you want to build or bug to fix... (e.g. Write a thread-safe cache in Python)"
                      className="w-full p-3 bg-transparent text-theme-main font-sans text-xs focus:outline-none border border-theme rounded-xl resize-none min-h-[60px]"
                      disabled={isLobbyRunning}
                    />
                    <button
                      onClick={handleRunLobbyDebate}
                      disabled={isLobbyRunning || !lobbyPrompt.trim()}
                      className="w-full py-2 bg-white hover:bg-theme-accent disabled:opacity-40 text-black rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5"
                    >
                      {isLobbyRunning ? (
                        <>
                          <Loader2 className="w-3.5 h-3.5 animate-spin text-black" />
                          <span>Agents Debating...</span>
                        </>
                      ) : (
                        <>
                          <Sparkles className="w-3.5 h-3.5" />
                          <span>Debate & Generate Fix</span>
                        </>
                      )}
                    </button>
                  </div>

                  <div className="flex-grow flex flex-col space-y-3.5 overflow-y-auto pr-1">
                    {lobbyDebate.length === 0 && !isLobbyRunning && (
                      <div className="flex-grow flex flex-col items-center justify-center text-center p-6 text-theme-dim h-full">
                        <span className="text-3xl mb-2">🤝</span>
                        <p className="text-xs font-semibold leading-relaxed">The Multi-Agent Sandbox is idle.</p>
                        <p className="text-[11px] max-w-xs mt-1 leading-normal text-zinc-500">
                          Enter a prompt above. Three specialized local LLM agents (Coder, QA, and Auditor) will debate design decisions, review security risks, and produce optimized code.
                        </p>
                      </div>
                    )}

                    {isLobbyRunning && lobbyDebate.length === 0 && (
                      <div className="flex-grow flex flex-col items-center justify-center p-6 text-theme-dim h-full">
                        <Loader2 className="w-8 h-8 animate-spin text-theme-accent mb-2" />
                        <p className="text-xs font-bold animate-pulse text-theme-main">Coder, QA, and Auditor are debating...</p>
                        <p className="text-[10px] mt-1 text-zinc-500">This may take 15-30 seconds using offline local models.</p>
                      </div>
                    )}

                    {lobbyDebate.map((d, index) => (
                      <div 
                        key={index} 
                        className={`p-4 border rounded-2xl flex flex-col space-y-1.5 ${
                          d.agent.includes("QA") ? 'bg-emerald-500/5 border-emerald-500/20' :
                          d.agent.includes("Auditor") ? 'bg-amber-500/5 border-amber-500/20' :
                          d.agent.includes("Final") ? 'bg-purple-500/5 border-purple-500/20' : 'bg-blue-500/5 border-blue-500/20'
                        }`}
                      >
                        <div className="flex items-center gap-1.5 select-none">
                          <span className="text-sm">{d.avatar}</span>
                          <span className={`text-[10px] font-bold tracking-wide uppercase ${
                            d.agent.includes("QA") ? 'text-emerald-400' :
                            d.agent.includes("Auditor") ? 'text-amber-400' :
                            d.agent.includes("Final") ? 'text-purple-400' : 'text-blue-400'
                          }`}>
                            {d.agent}
                          </span>
                        </div>
                        <p className="text-[11px] text-zinc-300 font-sans leading-relaxed whitespace-pre-wrap select-text">
                          {d.message}
                        </p>
                      </div>
                    ))}

                    {lobbyProposedCode && (
                      <div className="mt-4 space-y-3">
                        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                          {/* LEFT PANEL: Target Specifications / Input Prompt */}
                          <div className="flex flex-col border border-theme rounded-2xl overflow-hidden bg-black/55">
                            <div className="px-4 py-2 border-b border-theme bg-rose-500/10 flex items-center justify-between select-none">
                              <span className="text-[9px] font-mono text-rose-300 font-bold uppercase tracking-wider">
                                Target Specifications / Requirements
                              </span>
                              <button
                                onMouseEnter={() => playUISound('hover')}
                                onClick={() => {
                                  playUISound('click');
                                  navigator.clipboard.writeText(lobbyPrompt);
                                }}
                                className="text-[9px] text-zinc-400 hover:text-white cursor-pointer bg-zinc-800 px-2 py-0.5 border border-zinc-700 rounded"
                              >
                                Copy Specs
                              </button>
                            </div>
                            <div className="p-3 bg-black/40 overflow-y-auto max-h-[300px] scrollbar-thin">
                              {renderDiffLines(lobbyPrompt, 'red')}
                            </div>
                          </div>

                          {/* RIGHT PANEL: Optimized Solution Code */}
                          <div className="flex flex-col border border-theme rounded-2xl overflow-hidden bg-black/55">
                            <div className="px-4 py-2 border-b border-theme bg-emerald-500/10 flex items-center justify-between select-none">
                              <span className="text-[9px] font-mono text-emerald-350 font-bold uppercase tracking-wider">
                                Optimized Agent Solution Code
                              </span>
                              <div className="flex items-center gap-2">
                                <button
                                  onMouseEnter={() => playUISound('hover')}
                                  onClick={() => {
                                    playUISound('click');
                                    setSandboxCode(lobbyProposedCode);
                                    setSidebarTab('sandbox');
                                  }}
                                  className="text-[9px] text-theme-accent hover:text-white font-bold cursor-pointer bg-theme-accent/10 px-2 py-0.5 border border-theme-accent/20 rounded"
                                >
                                  Apply to Sandbox
                                </button>
                                <button
                                  onMouseEnter={() => playUISound('hover')}
                                  onClick={() => {
                                    playUISound('click');
                                    navigator.clipboard.writeText(lobbyProposedCode);
                                  }}
                                  className="text-[9px] text-zinc-400 hover:text-white cursor-pointer bg-zinc-800 px-2 py-0.5 border border-zinc-700 rounded"
                                >
                                  Copy Code
                                </button>
                              </div>
                            </div>
                            <div className="p-3 bg-black/40 overflow-y-auto max-h-[300px] scrollbar-thin">
                              {renderDiffLines(lobbyProposedCode, 'green')}
                            </div>
                          </div>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* CODEBASE GRAPH */}
              {sidebarTab === 'codemap' && (
                <div className="p-6 space-y-4 animate-fade-in flex flex-col h-full min-h-0">
                  <div className="shrink-0 flex flex-col space-y-1.5 rounded-2xl p-4 glass-card">
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] font-mono text-theme-dim font-bold uppercase tracking-wider block">
                        🕸️ Codebase Graph
                      </span>
                      <button
                        onMouseEnter={() => playUISound('hover')}
                        onClick={() => {
                          playUISound('click');
                          fetchCodeGraph();
                        }}
                        className="text-[9px] text-theme-accent hover:text-white font-bold cursor-pointer bg-theme-accent/10 px-2.5 py-0.5 border border-theme-accent/20 rounded-lg accent-glow-hover"
                      >
                        Refresh Graph
                      </button>
                    </div>
                    <p className="text-[10px] text-theme-dim leading-relaxed">
                      Interactive map of codebase files and dependencies. Drag nodes to reposition. Click a node to view details or trigger heals.
                    </p>
                  </div>

                  {/* Filters and Search Bar */}
                  <div className="shrink-0 flex flex-wrap items-center justify-between gap-3 bg-panel-theme border border-theme p-3 rounded-2xl">
                    {/* Extension Filter Buttons */}
                    <div className="flex items-center gap-1.5">
                      <span className="text-[9px] font-mono text-theme-dim uppercase font-bold mr-1">Filter:</span>
                      {[
                        { id: 'all', label: 'All Files' },
                        { id: 'py', label: '.py' },
                        { id: 'ts', label: '.ts / .tsx' },
                        { id: 'js', label: '.js / .jsx' }
                      ].map(f => (
                        <button
                          key={f.id}
                          onMouseEnter={() => playUISound('hover')}
                          onClick={() => {
                            playUISound('click');
                            setCodeMapFilter(f.id as any);
                          }}
                          className={`px-2.5 py-1 text-[10px] font-bold font-mono rounded-lg border transition-all cursor-pointer ${
                            codeMapFilter === f.id
                              ? 'bg-theme-accent text-black border-theme-accent shadow-theme-glow'
                              : 'bg-main-theme-30 text-theme-dim border-theme hover:text-theme-main hover:border-theme-accent/40'
                          }`}
                        >
                          {f.label}
                        </button>
                      ))}
                    </div>

                    {/* Search Input Box */}
                    <div className="relative flex items-center w-full sm:w-64">
                      <Search className="absolute left-2.5 w-3.5 h-3.5 text-zinc-500 pointer-events-none" />
                      <input
                        type="text"
                        value={codeMapSearch}
                        onChange={(e) => setCodeMapSearch(e.target.value)}
                        placeholder="Search file node..."
                        onMouseEnter={() => playUISound('hover')}
                        className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-1.5 pl-8 pr-3.5 text-xs focus:outline-none focus:border-theme-accent font-mono placeholder-zinc-650"
                      />
                      {codeMapSearch && (
                        <button
                          onClick={() => setCodeMapSearch('')}
                          className="absolute right-2.5 text-zinc-550 hover:text-white"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      )}
                    </div>
                  </div>

                  {/* SVG Code Map Network Graph */}
                  <div className="flex-grow rounded-2xl overflow-hidden relative min-h-[300px] flex flex-col glass-card">
                    {codeGraph.nodes.length === 0 ? (
                      <div className="flex-1 flex flex-col items-center justify-center text-center p-6 text-theme-dim">
                        <span className="text-3xl mb-2">🕸️</span>
                        <p className="text-xs font-semibold leading-relaxed">No files found or graph is empty.</p>
                      </div>
                    ) : (
                      <svg
                        className="w-full h-full min-h-[300px] select-none"
                        onMouseMove={handleGraphNodeDrag}
                        onMouseUp={handleGraphNodeDragEnd}
                        onMouseLeave={handleGraphNodeDragEnd}
                      >
                        <defs>
                          <marker
                            id="arrow"
                            viewBox="0 0 10 10"
                            refX="18"
                            refY="5"
                            markerWidth="6"
                            markerHeight="6"
                            orient="auto-start-reverse"
                          >
                            <path d="M 0 0 L 10 5 L 0 10 z" fill="var(--accent)" opacity="0.6" />
                          </marker>
                          <filter id="node-glow" x="-50%" y="-50%" width="200%" height="200%">
                            <feGaussianBlur stdDeviation="3" result="blur" />
                            <feComposite in="SourceGraphic" in2="blur" operator="over" />
                          </filter>
                        </defs>

                        {/* Links */}
                        {codeGraph.links.map((link, idx) => {
                          const sourceNode = codeGraph.nodes.find(n => n.id === link.source);
                          const targetNode = codeGraph.nodes.find(n => n.id === link.target);
                          if (!sourceNode || !targetNode) return null;

                          // Filter out links whose endpoints are filtered out
                          const isSourceMatch = codeMapFilter === 'all' || 
                            (codeMapFilter === 'py' && sourceNode.type === 'py') ||
                            (codeMapFilter === 'ts' && (sourceNode.type === 'ts' || sourceNode.type === 'tsx')) ||
                            (codeMapFilter === 'js' && (sourceNode.type === 'js' || sourceNode.type === 'jsx'));
                          const isTargetMatch = codeMapFilter === 'all' || 
                            (codeMapFilter === 'py' && targetNode.type === 'py') ||
                            (codeMapFilter === 'ts' && (targetNode.type === 'ts' || targetNode.type === 'tsx')) ||
                            (codeMapFilter === 'js' && (targetNode.type === 'js' || targetNode.type === 'jsx'));

                          if (!isSourceMatch || !isTargetMatch) return null;

                          // Search dimming
                          let opacity = 0.6;
                          if (codeMapSearch.trim()) {
                            const query = codeMapSearch.toLowerCase();
                            const sourceLabelMatch = sourceNode.label.toLowerCase().includes(query) || sourceNode.id.toLowerCase().includes(query);
                            const targetLabelMatch = targetNode.label.toLowerCase().includes(query) || targetNode.id.toLowerCase().includes(query);
                            if (!sourceLabelMatch || !targetLabelMatch) {
                              opacity = 0.15;
                            }
                          }

                          return (
                            <line
                              key={`link-${idx}`}
                              x1={sourceNode.x || 250}
                              y1={sourceNode.y || 200}
                              x2={targetNode.x || 250}
                              y2={targetNode.y || 200}
                              stroke="color-mix(in srgb, var(--accent) 35%, transparent)"
                              strokeWidth="1.5"
                              opacity={opacity}
                              className="graph-flow-link"
                              markerEnd="url(#arrow)"
                            />
                          );
                        })}

                        {/* Nodes */}
                        {codeGraph.nodes.map((node) => {
                          // Filter extension
                          const isMatchFilter = codeMapFilter === 'all' || 
                            (codeMapFilter === 'py' && node.type === 'py') ||
                            (codeMapFilter === 'ts' && (node.type === 'ts' || node.type === 'tsx')) ||
                            (codeMapFilter === 'js' && (node.type === 'js' || node.type === 'jsx'));

                          if (!isMatchFilter) return null;

                          const isSelected = selectedNode && selectedNode.id === node.id;
                          const isError = node.status === 'error';
                          
                          let nodeColor = '#3b82f6'; // blue for py
                          if (node.type === 'tsx') nodeColor = '#a855f7'; // purple
                          if (node.type === 'ts') nodeColor = '#6366f1'; // indigo
                          if (node.type === 'js' || node.type === 'jsx') nodeColor = '#eab308'; // yellow
                          
                          // Search highlight / dimming
                          let opacity = 1;
                          let highlightNode = false;
                          if (codeMapSearch.trim()) {
                            const query = codeMapSearch.toLowerCase();
                            const isLabelMatch = node.label.toLowerCase().includes(query) || node.id.toLowerCase().includes(query);
                            if (!isLabelMatch) {
                              opacity = 0.25;
                            } else {
                              highlightNode = true;
                            }
                          }

                          return (
                            <g
                              key={node.id}
                              transform={`translate(${node.x || 250}, ${node.y || 200})`}
                              className="cursor-pointer group"
                              opacity={opacity}
                              onMouseDown={() => setDraggedNodeId(node.id)}
                              onClick={() => {
                                playUISound('click');
                                setSelectedNode(node);
                              }}
                            >
                              <circle
                                r={isSelected ? 10 : (highlightNode ? 11 : 8)}
                                fill={nodeColor}
                                stroke={isError ? '#ef4444' : (isSelected ? '#ffffff' : (highlightNode ? 'var(--accent)' : 'transparent'))}
                                strokeWidth={isSelected || highlightNode ? "2.5" : "2"}
                                filter={isError || highlightNode ? 'url(#node-glow)' : ''}
                                className={`transition-all duration-150 hover:scale-125 ${highlightNode ? 'animate-pulse' : ''}`}
                              />
                              {isError && (
                                <circle
                                  r="4"
                                  fill="#ef4444"
                                  cx="6"
                                  cy="-6"
                                />
                              )}
                              <text
                                y="20"
                                textAnchor="middle"
                                fill={isSelected || highlightNode ? '#ffffff' : '#a1a1aa'}
                                className="text-[9px] font-mono select-none pointer-events-none font-bold"
                              >
                                {node.label}
                              </text>
                            </g>
                          );
                        })}
                      </svg>
                    )}
                  </div>

                  {/* DETAILS & AUTO-HEAL FOOTER */}
                  {selectedNode && (
                    <div className="shrink-0 flex flex-col space-y-2 rounded-2xl p-4 animate-fade-in font-sans glass-card-accent">
                      <div className="flex items-center justify-between border-b border-theme pb-2 select-none">
                        <span className="text-[10px] font-mono text-purple-300 font-bold uppercase tracking-wider">
                          📄 File Info
                        </span>
                        <button
                          onClick={() => setSelectedNode(null)}
                          className="text-[9px] text-zinc-400 hover:text-white"
                        >
                          Close Details
                        </button>
                      </div>

                      <div className="space-y-1 select-text">
                        <p className="text-[11px] font-mono text-zinc-200 break-all">
                          <span className="text-theme-dim font-bold">Path:</span> {selectedNode.id}
                        </p>
                        <p className="text-[11px] text-zinc-200">
                          <span className="text-theme-dim font-bold">Type:</span> {selectedNode.type.toUpperCase()}
                        </p>
                        <p className="text-[11px] text-zinc-200">
                          <span className="text-theme-dim font-bold">Status:</span>{' '}
                          <span className={selectedNode.status === 'error' ? 'text-red-400 font-bold' : 'text-teal-400'}>
                            {selectedNode.status === 'error' ? 'COMPILE ERROR' : 'HEALTHY'}
                          </span>
                        </p>
                      </div>

                      {selectedNode.status === 'error' && (
                        <div className="mt-2.5 p-3 bg-red-500/5 border border-red-500/20 rounded-xl flex flex-col space-y-2 select-text">
                          <span className="text-[9px] font-mono text-red-400 font-bold uppercase tracking-wider select-none">
                            ⚠️ Diagnostic Message:
                          </span>
                          <p className="text-[10px] font-mono text-zinc-300 leading-normal whitespace-pre-wrap select-text">
                            {selectedNode.error_message}
                          </p>
                          <button
                            onClick={() => triggerHealProposer(selectedNode.id, selectedNode.error_message, 'codemap_heal')}
                            className="w-full py-1.5 bg-red-500 hover:bg-red-600 hover:shadow-[0_0_15px_rgba(239,68,68,0.35)] text-white rounded-lg text-xs font-bold transition-all cursor-pointer flex items-center justify-center gap-1.5"
                          >
                            <Sparkles className="w-3.5 h-3.5" />
                            <span>Run Auto-Heal Fix</span>
                          </button>
                        </div>
                      )}
                    </div>
                  )}
                </div>
              )}

            </div>

            {/* Central console bottom status strip */}
            <div className="px-6 py-3 border-t border-theme bg-panel-theme text-[10px] text-theme-dim font-sans flex items-center gap-2 select-none shrink-0">
              <Activity className="w-3.5 h-3.5 text-emerald-500 animate-pulse" />
              <span>Verified Local Workspace Sandbox Environment Active</span>
            </div>
          </div>

          {/* COLUMN RESIZING DIVIDER */}
          <div 
            onMouseDown={startResizing}
            className={`w-[3px] hover:bg-theme-accent/50 transition-colors z-20 shrink-0 select-none relative ${
              isResizing ? 'bg-theme-accent' : 'bg-zinc-900/60'
            }`}
          >
            <div className="absolute inset-y-0 -left-1.5 -right-1.5 cursor-col-resize z-30" />
          </div>

          {/* COLUMN 3: RIGHT SIDEBAR CONSOLE (COMMAND INTERFACE & CHAT) */}
          <aside 
            className="border-l border-theme bg-panel-theme flex flex-col overflow-hidden relative shrink-0"
            style={{ width: `${sidebarWidth}px` }}
          >
            {/* Right sidebar header with Mascot character and audio waveform */}
            <div className="flex items-center justify-between px-4 py-3 border-b border-theme bg-panel-theme-40 shrink-0 min-h-[64px] select-none">
              <div className="flex items-center gap-2.5 min-w-0">
                <MascotCharacter 
                  state={mascotState} 
                  accentColor={theme === 'default' ? '#ea580c' : theme === 'cyberpunk' ? '#ff007f' : theme === 'amber' ? '#ffb000' : '#14b8a6'} 
                  wardrobe={mascotWardrobe === 'auto' ? (mascotState === 'crown' ? 'crown' : mascotState === 'diagnostic' ? 'construction_hat' : mascotState === 'disapproving' ? 'detective_hat' : 'none') : mascotWardrobe} 
                  speechAmplitude={speechAmplitude} 
                />
                <div className="flex flex-col min-w-0">
                  <span className="text-[10px] font-bold text-white tracking-wide leading-tight">Meridian</span>
                  <span className="text-[8px] text-zinc-500 uppercase font-bold tracking-wider">
                    {isRunning ? 'Thinking...' : 'Connected'}
                  </span>
                </div>
              </div>

              {/* real-time voice amplitude visualizer waveform SVG */}
              <div className="flex-1 flex justify-end">
                {isRecording ? (
                  <div className="flex items-end gap-[2.5px] h-5 px-2">
                    {micVisualizerWaves.map((height, idx) => (
                      <div 
                        key={idx} 
                        className="w-[2.5px] bg-emerald-500 rounded-full transition-all duration-75"
                        style={{ height: `${height * 0.8}px` }}
                      />
                    ))}
                  </div>
                ) : speechAmplitude > 0 ? (
                  <div className="flex items-center h-6 px-2 justify-center overflow-hidden">
                    <svg className="w-20 h-5 overflow-visible text-theme-accent" viewBox="0 0 100 24" fill="none">
                      <motion.path
                        d="M0 12 Q25 2, 50 12 T100 12"
                        stroke="currentColor"
                        strokeWidth="2.2"
                        animate={{
                          d: [
                            `M0 12 Q25 ${12 - speechAmplitude * 15}, 50 12 T100 12`,
                            `M0 12 Q25 ${12 + speechAmplitude * 15}, 50 12 T100 12`,
                            `M0 12 Q25 ${12 - speechAmplitude * 15}, 50 12 T100 12`
                          ]
                        }}
                        transition={{ duration: 0.8, repeat: Infinity, ease: "easeInOut" }}
                      />
                    </svg>
                  </div>
                ) : (
                  <div className="flex items-center h-6 px-2 justify-center overflow-hidden">
                    <svg className="w-20 h-5 overflow-visible text-teal-500/20" viewBox="0 0 100 24" fill="none">
                      <motion.path
                        d="M0 12 H100"
                        stroke="currentColor"
                        strokeWidth="1.2"
                        animate={{
                          strokeDashoffset: [0, -20]
                        }}
                        strokeDasharray="4 4"
                        transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                      />
                    </svg>
                  </div>
                )}
              </div>
            </div>

            {/* Chat Box bubbles scrollable viewport */}
            <div 
              ref={chatScrollRef}
              className="flex-1 overflow-y-auto px-4 py-4 space-y-4 bg-main-theme-30 select-text"
            >
              {messages.map((msg) => {
                const isAssistant = msg.sender === 'assistant';
                return (
                  <div key={msg.id} className={`flex ${isAssistant ? 'justify-start' : 'justify-end'} animate-fade-in`}>
                    <div className={`max-w-[90%] flex flex-col ${isAssistant ? 'items-start' : 'items-end'}`}>
                      
                      <div className="flex items-center gap-1.5 mb-1 px-1 text-[9px] text-theme-dim font-semibold tracking-wide select-none">
                        <span>{isAssistant ? 'Meridian' : 'User'}</span>
                        <span>•</span>
                        <span className="text-theme-dim font-medium">{msg.timestamp}</span>
                      </div>

                      <div className={`rounded-xl px-4 py-2.5 text-xs leading-relaxed border transition-all ${
                        isAssistant
                          ? 'glass-card border-l-4 border-l-theme-accent text-theme-main font-sans rounded-tl-none shadow-md'
                          : 'bg-main-theme-50 border-theme-60 border-r-4 border-r-zinc-650 text-theme-main font-medium rounded-tr-none shadow-md'
                      }`}>
                        {isAssistant ? (
                          <div 
                            className="markdown-body select-text"
                            dangerouslySetInnerHTML={{ __html: marked.parse(msg.text) as string }}
                          />
                        ) : (
                          <div className="break-words space-y-2 select-text tracking-wide whitespace-pre-wrap">
                            {msg.text}
                          </div>
                        )}
                      </div>
                    </div>
                  </div>
                );
              })}

              {isRunning && (
                <div className="flex justify-start animate-pulse">
                  <div className="flex flex-col items-start max-w-[85%]">
                    <div className="flex items-center gap-2 mb-1.5 px-1 text-[9px] text-zinc-400 font-medium tracking-wide">
                      <span>Meridian is processing...</span>
                    </div>
                    <div className="bg-zinc-950 border border-zinc-900 rounded-xl px-3 py-2 text-zinc-400 flex items-center gap-2.5">
                      <Loader2 className="w-3.5 h-3.5 animate-spin" />
                      <span className="font-sans text-xs font-semibold">Generating...</span>
                    </div>
                  </div>
                </div>
              )}
            </div>

            {/* Input Console Bottom Panel */}
            <div className="p-4 bg-panel-theme border-t border-theme shrink-0">
              
              {/* Confirmation Overlay */}
              {pendingConfirmation && (
                <div className="mb-4 p-4.5 bg-panel-theme border border-theme-accent rounded-2xl relative z-20 shadow-2xl animate-fade-in shadow-theme-glow">
                  <div className="flex items-start gap-2.5">
                    <div className="w-7 h-7 rounded-lg bg-theme-accent-10 border border-theme-accent-30 flex items-center justify-center text-theme-accent shrink-0">
                      <AlertCircle className="w-4 h-4 animate-bounce" />
                    </div>
                    <div className="space-y-1.5 flex-1 min-w-0">
                      <h4 className="text-[10px] font-bold text-white uppercase tracking-wider font-mono">
                        Authorization Required (Tier {pendingConfirmation.tier})
                      </h4>
                      <p className="text-xs text-theme-main leading-relaxed font-sans select-text">
                        Run <code className="bg-main-theme px-1 py-0.5 rounded font-mono text-theme-accent">{pendingConfirmation.tool}</code> with:
                      </p>
                      <pre className="mt-1.5 p-2.5 bg-main-theme border border-theme rounded-xl text-[9px] font-mono text-theme-main select-all overflow-x-auto leading-normal">
                        {JSON.stringify(pendingConfirmation.args, null, 2)}
                      </pre>
                    </div>
                  </div>
                  <div className="mt-3.5 flex items-center justify-end gap-2.5">
                    <button
                      onClick={() => handleConfirmResponse(pendingConfirmation.id, false)}
                      className="px-3.5 py-1.5 bg-main-theme hover:bg-main-theme-80 border border-theme text-theme-dim hover:text-theme-main rounded-lg text-[10px] font-semibold tracking-wider transition-all uppercase cursor-pointer"
                    >
                      Reject
                    </button>
                    <button
                      onClick={() => handleConfirmResponse(pendingConfirmation.id, true)}
                      className="px-4 py-1.5 bg-theme-accent hover:bg-theme-accent text-black rounded-lg text-[10px] font-semibold tracking-wider transition-all uppercase cursor-pointer"
                    >
                      Approve
                    </button>
                  </div>
                </div>
              )}

              {/* Simulated Recording/Voice Connected status */}
              {isRecording && (
                <div className="absolute top-0 left-0 right-0 -translate-y-full px-4 py-2 bg-panel-theme border-t border-b border-theme flex items-center justify-between text-xs text-theme-main select-none">
                  <div className="flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span className="font-sans text-[9px] text-theme-dim font-bold uppercase tracking-wider">Voice Connected</span>
                  </div>
                  <div className="flex items-end gap-1 h-3.5">
                    {micVisualizerWaves.map((height, idx) => (
                      <div 
                        key={idx} 
                        className="w-[2px] bg-theme-accent rounded-full transition-all duration-75"
                        style={{ height: `${height * 0.6}px` }}
                      />
                    ))}
                  </div>
                </div>
              )}

              {/* Screen Capture Preview thumbnail */}
              {capturedImage && (
                <div className="mb-3 p-2.5 bg-zinc-950/60 border border-theme rounded-xl flex items-center justify-between gap-3 animate-fade-in">
                  <div className="flex items-center gap-2.5 min-w-0">
                    <div className="w-10 h-10 rounded-lg border border-theme overflow-hidden shrink-0 relative bg-black/45">
                      <img src={capturedImage} alt="Screen capture preview" className="w-full h-full object-cover" />
                    </div>
                    <div className="min-w-0">
                      <p className="text-[10px] font-bold text-theme-main font-mono uppercase tracking-wider">Screen Attached</p>
                      <p className="text-[9px] text-theme-dim truncate leading-normal">
                        {capturedOCR ? `OCR: "${capturedOCR.substring(0, 40)}..."` : 'No OCR text detected.'}
                      </p>
                    </div>
                  </div>
                  <button
                    onClick={() => {
                      setCapturedImage(null);
                      setCapturedOCR('');
                    }}
                    className="p-1 rounded-lg border border-theme hover:border-rose-900/40 text-theme-dim hover:text-rose-400 transition-colors cursor-pointer"
                  >
                    <X className="w-3 h-3" />
                  </button>
                </div>
              )}

              {/* Main input text field and buttons */}
              <div className="relative flex items-stretch gap-2 bg-panel-theme border border-theme rounded-xl p-2 focus-within:border-theme-accent focus-within:shadow-[0_0_12px_var(--accent-glow)] transition-all">
                <textarea
                  ref={textareaRef}
                  id="task-input-field"
                  rows={1}
                  value={inputText}
                  onChange={(e) => setInputText(e.target.value)}
                  onKeyDown={(e) => {
                    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                    if (isTauri && e.key !== 'Enter') {
                      emit('user-typing', {}).catch(() => {});
                    }
                    if (e.key === 'Enter' && !e.shiftKey) {
                      e.preventDefault();
                      handleSendCommand();
                    }
                  }}
                  disabled={isRunning}
                  placeholder="Enter a workspace task..."
                  className="flex-1 bg-transparent text-white placeholder-zinc-500 border-none px-2.5 font-sans text-xs focus:outline-none focus:ring-0 disabled:opacity-50 resize-none py-1.5 min-h-[24px] max-h-[180px] overflow-y-auto leading-relaxed"
                />

                <div className="flex items-center gap-1.5 self-center">
                  <button
                    id="mic-recording-btn"
                    onClick={toggleRecording}
                    disabled={isRunning}
                    title="Translate speech to command"
                    className={`p-2 border rounded-lg transition-all cursor-pointer ${
                      isRecording 
                        ? 'bg-theme-accent-10 text-theme-accent border-theme-accent-30 shadow-theme-glow' 
                        : 'bg-panel-theme border-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40 disabled:opacity-30'
                    }`}
                  >
                    {isRecording ? <MicOff className="w-3.5 h-3.5" /> : <Mic className="w-3.5 h-3.5" />}
                  </button>

                  <button
                    id="capture-screen-btn"
                    onClick={handleCaptureScreen}
                    disabled={isRunning || isCapturingScreen}
                    title="Capture active workspace screen"
                    className="p-2 border rounded-lg transition-all cursor-pointer bg-panel-theme border-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40 disabled:opacity-30 flex items-center justify-center"
                  >
                    {isCapturingScreen ? (
                      <Loader2 className="w-3.5 h-3.5 animate-spin text-theme-accent" />
                    ) : (
                      <Activity className="w-3.5 h-3.5" />
                    )}
                  </button>

                  {isRunning ? (
                    <button
                      id="stop-execution-btn"
                      onClick={handleStopExecution}
                      title="Halt model workspace execution process"
                      className="flex items-center gap-1 px-3 py-1.5 bg-theme-accent hover:bg-theme-accent text-black border border-transparent rounded-lg text-[10px] font-bold tracking-normal transition-all cursor-pointer uppercase"
                    >
                      <Square className="w-2.5 h-2.5 fill-black" />
                      <span>Halt</span>
                    </button>
                  ) : (
                    <button
                      id="send-command-btn"
                      onClick={() => handleSendCommand()}
                      disabled={!inputText.trim()}
                      className="flex items-center gap-1 px-3 py-1.5 bg-white disabled:bg-main-theme border border-transparent disabled:border-transparent text-black disabled:text-theme-dim rounded-lg text-[10px] font-bold tracking-normal transition-all uppercase cursor-pointer accent-glow-hover hover:shadow-[0_0_10px_var(--accent-glow)]"
                    >
                      <span>Send</span>
                      <Send className="w-2.5 h-2.5" />
                    </button>
                  )}
                </div>
              </div>

              <div className="flex justify-between items-center mt-3 px-1 text-[10px] text-theme-dim font-medium select-none">
                <span className="flex items-center gap-1 leading-none">
                  <CornerDownLeft className="w-3 h-3 text-theme-accent" />
                  Press Enter to submit
                </span>
                <span>Sandbox Secured</span>
              </div>

              {!backendConnected && (
                <div className="mt-3 flex items-center justify-center gap-2 p-2.5 rounded-xl border border-rose-950/40 bg-rose-950/10 text-rose-450 text-[10px] font-sans tracking-wide select-none">
                  <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                  <span><strong>Warning:</strong> FastAPI Backend is offline. Run <code className="bg-rose-950/30 px-1 py-0.5 rounded border border-rose-900/30 font-mono text-[9px] select-all">start_meridian.bat</code> option 3.</span>
                </div>
              )}
            </div>
          </aside>

        </div>
      </div>

      {/* ── PROACTIVE NUDGES TOAST STACK ──────────────────────────────────────── */}
      <div
        id="proactive-nudge-stack"
        style={{
          position: 'fixed',
          bottom: '24px',
          right: '24px',
          zIndex: 9999,
          display: 'flex',
          flexDirection: 'column',
          gap: '10px',
          alignItems: 'flex-end',
          pointerEvents: 'none'
        }}
      >
        {nudges.map((nudge) => (
          <motion.div
            key={nudge.id}
            id={`nudge-${nudge.id}`}
            initial={{ opacity: 0, x: 60, scale: 0.92 }}
            animate={{ opacity: 1, x: 0, scale: 1 }}
            exit={{ opacity: 0, x: 60, scale: 0.9 }}
            transition={{ type: 'spring', stiffness: 320, damping: 28 }}
            style={{
              pointerEvents: 'all',
              width: '320px',
              background: 'linear-gradient(135deg, rgba(15,15,20,0.97) 0%, rgba(22,22,32,0.97) 100%)',
              border: '1px solid rgba(255,255,255,0.09)',
              borderRadius: '14px',
              boxShadow: '0 8px 32px rgba(0,0,0,0.55), 0 0 0 1px rgba(99,102,241,0.12)',
              overflow: 'hidden',
              backdropFilter: 'blur(20px)'
            }}
          >
            <div style={{
              height: '2px',
              background: nudge.type === 'system_health' ? 'linear-gradient(90deg,#ef4444,#f97316)' :
                nudge.type === 'clipboard_error' ? 'linear-gradient(90deg,#ef4444,#ec4899)' :
                nudge.type === 'idle_nudge' ? 'linear-gradient(90deg,#6366f1,#8b5cf6)' :
                nudge.type === 'followup' ? 'linear-gradient(90deg,#10b981,#06b6d4)' : 'linear-gradient(90deg,#6366f1,#a78bfa)'
            }} />

            <div style={{ padding: '12px 14px 10px' }}>
              <div style={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: '8px', marginBottom: '6px' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '7px', flex: 1, minWidth: 0 }}>
                  <span style={{ fontSize: '16px', flexShrink: 0 }}>{nudge.icon}</span>
                  <span style={{ fontSize: '12px', fontWeight: 700, color: '#e2e8f0', letterSpacing: '0.01em', lineHeight: 1.3 }}>
                    {nudge.title}
                  </span>
                </div>
                <button
                  id={`nudge-dismiss-${nudge.id}`}
                  onClick={() => dismissNudge(nudge.id)}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    cursor: 'pointer',
                    color: '#64748b',
                    padding: '2px',
                    lineHeight: 1,
                    flexShrink: 0
                  }}
                >
                  <X style={{ width: '13px', height: '13px' }} />
                </button>
              </div>

              <p style={{ fontSize: '11.5px', color: '#94a3b8', margin: '0 0 10px', lineHeight: 1.5 }}>
                {nudge.message}
              </p>

              {nudge.type === 'terminal_heal' && nudge.patch && (
                <div style={{
                  marginTop: '8px',
                  marginBottom: '10px',
                  padding: '8px 10px',
                  background: 'rgba(239,68,68,0.06)',
                  border: '1px solid rgba(239,68,68,0.2)',
                  borderRadius: '8px',
                  fontSize: '10.5px',
                  display: 'flex',
                  flexDirection: 'column',
                  gap: '4px'
                }}>
                  <div style={{ color: '#ef4444', fontWeight: 600 }}>Failed Command:</div>
                  <div style={{ fontFamily: 'monospace', color: '#fca5a5', background: 'rgba(0,0,0,0.3)', padding: '4px 6px', borderRadius: '4px', overflowX: 'auto' }}>
                    {nudge.patch.original}
                  </div>
                  {nudge.patch.error_message && (
                    <>
                      <div style={{ color: '#ef4444', fontWeight: 600, marginTop: '2px' }}>Error Details:</div>
                      <div style={{ fontFamily: 'monospace', color: '#cbd5e1', background: 'rgba(0,0,0,0.3)', padding: '4px 6px', borderRadius: '4px', maxHeight: '60px', overflowY: 'auto' }}>
                        {nudge.patch.error_message}
                      </div>
                    </>
                  )}
                  <div style={{ color: '#10b981', fontWeight: 600, marginTop: '2px' }}>Suggested Fix:</div>
                  <div style={{ fontFamily: 'monospace', color: '#a7f3d0', background: 'rgba(0,0,0,0.3)', padding: '4px 6px', borderRadius: '4px', overflowX: 'auto' }}>
                    {nudge.patch.proposed}
                  </div>
                </div>
              )}

              {nudge.type !== 'terminal_heal' && nudge.patch && (
                <div style={{
                  marginTop: '8px',
                  marginBottom: '10px',
                  padding: '8px 10px',
                  background: 'rgba(0,0,0,0.45)',
                  border: '1px solid rgba(239,68,68,0.25)',
                  borderRadius: '8px',
                  fontSize: '10px',
                  color: '#f43f5e',
                  fontFamily: 'monospace',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  whiteSpace: 'nowrap'
                }}>
                  Target: {nudge.patch.file_path.split(/[\\/]/).pop()}
                </div>
              )}

              {nudge.action_hint && (
                <button
                  id={`nudge-action-${nudge.id}`}
                  onClick={() => handleNudgeAction(nudge)}
                  style={{
                    width: '100%',
                    background: 'rgba(99,102,241,0.12)',
                    border: '1px solid rgba(99,102,241,0.25)',
                    borderRadius: '7px',
                    padding: '6px 10px',
                    cursor: 'pointer',
                    color: '#a5b4fc',
                    fontSize: '11px',
                    fontWeight: 600,
                    textAlign: 'left',
                    display: 'flex',
                    alignItems: 'center',
                    gap: '6px',
                    transition: 'background 0.15s'
                  }}
                  onMouseEnter={e => (e.currentTarget.style.background = 'rgba(99,102,241,0.22)')}
                  onMouseLeave={e => (e.currentTarget.style.background = 'rgba(99,102,241,0.12)')}
                >
                  <Sparkles style={{ width: '11px', height: '11px', flexShrink: 0 }} />
                  <span style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                    {nudge.action_hint}
                  </span>
                </button>
              )}

              <div style={{ fontSize: '10px', color: '#334155', marginTop: '8px', textAlign: 'right' }}>
                {nudge.timestamp}
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {/* ── 20-20-20 EYE BREAK OVERLAY ────────────────────────────────────── */}
      <AnimatePresence>
        {showBreakOverlay && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[10000] flex flex-col items-center justify-center bg-black/80 backdrop-blur-2xl text-white font-sans overflow-hidden"
          >
            <div className="flex flex-col items-center max-w-md text-center px-6">
              <motion.div
                animate={{ scale: [1, 1.18, 1], borderColor: ['rgba(234,88,12,0.4)', 'rgba(99,102,241,0.6)', 'rgba(234,88,12,0.4)'] }}
                transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                className="w-48 h-48 rounded-full border-4 flex items-center justify-center shadow-[0_0_50px_rgba(99,102,241,0.25)] bg-zinc-950/60 backdrop-blur-md relative"
              >
                <motion.div
                  animate={{ scale: [0.85, 1.05, 0.85], opacity: [0.7, 0.95, 0.7] }}
                  transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
                  className="absolute inset-2 rounded-full bg-gradient-to-tr from-theme-accent/10 to-indigo-500/10 border border-theme-accent/20"
                />
                
                <div className="z-10 text-center">
                  <span className="text-5xl font-extrabold text-theme-accent font-mono tracking-tight">{breakTimer}</span>
                  <span className="block text-[9px] text-zinc-400 font-mono tracking-widest mt-1">SECONDS</span>
                </div>
              </motion.div>

              <h2 className="text-2xl font-bold mt-8 mb-3 tracking-tight text-white flex items-center gap-2">
                <Sparkles className="w-5 h-5 text-theme-accent animate-pulse" />
                20-20-20 Eye Break
              </h2>
              
              <div className="space-y-3 select-none">
                <p className="text-sm text-zinc-300 leading-relaxed">
                  Focus on something <span className="text-theme-accent font-bold">20 feet away</span> for <span className="text-theme-accent font-bold">20 seconds</span> to reduce digital eye strain.
                </p>
                <div className="py-2 px-4 rounded-xl bg-zinc-900/40 border border-zinc-800/50 inline-block">
                  <span className="text-xs text-zinc-400 font-mono">
                    Mascot Status: <span className="text-theme-accent font-bold animate-pulse">Resting...</span>
                  </span>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* ── INTERACTIVE SELF-HEALING DIFF MODAL ───────────────────────────── */}
      <AnimatePresence>
        {showDiffModal && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/70 backdrop-blur-md p-4"
          >
            <motion.div
              initial={{ scale: 0.95, y: 15 }}
              animate={{ scale: 1, y: 0 }}
              exit={{ scale: 0.95, y: 15 }}
              transition={{ type: 'spring', damping: 25, stiffness: 250 }}
              className="bg-panel-theme border border-theme rounded-2xl shadow-2xl shadow-theme-glow w-[92vw] max-w-5xl h-[82vh] flex flex-col overflow-hidden text-left"
            >
              <div className="flex items-center justify-between px-5 py-4 border-b border-theme bg-main-theme/40 select-none">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="w-2.5 h-2.5 rounded-full bg-theme-accent animate-pulse" />
                  <div className="min-w-0">
                    <h3 className="text-xs font-semibold text-theme-main truncate font-mono">
                      {diffData?.filePath || 'Healing Target'}
                    </h3>
                    <p className="text-[10px] text-theme-dim mt-0.5">
                      Diagnostic Auto-Heal: {diffData?.errorMessage === 'secret_leak' ? 'Secure Credential Migration' : 'Syntax Error Rectification'}
                    </p>
                  </div>
                </div>
                <button
                  onClick={() => {
                    setShowDiffModal(false);
                    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                    if (isTauri) {
                      emit('mascot-wardrobe-changed', { item: 'default' }).catch(console.error);
                    }
                  }}
                  className="p-1 rounded-lg border border-theme hover:border-theme-accent-40 text-theme-dim hover:text-theme-main transition-colors cursor-pointer"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              <div className="flex-1 overflow-hidden flex flex-col p-5 bg-main-theme/10">
                {isFetchingHeal ? (
                  <div className="flex-1 flex flex-col items-center justify-center gap-4 text-center select-none">
                    <Loader2 className="w-8 h-8 text-theme-accent animate-spin" />
                    <div>
                      <p className="text-xs font-semibold text-theme-main font-mono">Analyzing codebase diagnostics...</p>
                      <p className="text-[10px] text-theme-dim mt-1">Generating optimal refactoring suggestions via local LLM</p>
                    </div>
                  </div>
                ) : (
                  <div className="flex-1 flex flex-col gap-4 min-h-0">
                    {diffData?.errorMessage === 'secret_leak' && (
                      <div className="p-3.5 rounded-xl border border-amber-500/20 bg-amber-500/5 flex flex-col gap-2">
                        <span className="text-[10px] font-mono text-amber-400 font-bold uppercase tracking-wide">
                          Security Alert: Credential Leak Detected
                        </span>
                        <p className="text-xs text-zinc-300">
                          We found an exposed credential in the codebase. We propose to move it to your local environment file and load it dynamically using standard `os.environ`.
                        </p>
                        <div className="flex items-center gap-3 mt-1">
                          <label className="text-[10px] font-mono text-theme-accent uppercase font-bold tracking-wider">
                            Environment Entry:
                          </label>
                          <input
                            type="text"
                            value={credentialSecret || ''}
                            onChange={(e) => setCredentialSecret(e.target.value)}
                            placeholder="KEY=value"
                            className="flex-1 max-w-md bg-main-theme border border-theme text-theme-main rounded-lg py-1 px-2.5 text-xs font-mono focus:outline-none focus:border-theme-accent"
                          />
                        </div>
                      </div>
                    )}

                    <div className="flex-1 grid grid-cols-2 gap-4 min-h-0">
                      <div className="flex flex-col border border-theme rounded-xl overflow-hidden bg-main-theme/30">
                        <div className="px-3.5 py-2 border-b border-theme bg-main-theme/50 flex items-center justify-between select-none">
                          <span className="text-[10px] font-mono text-rose-400 font-bold uppercase tracking-wider">
                            Original Code
                          </span>
                        </div>
                        <textarea
                          readOnly
                          value={diffData?.original || ''}
                          className="flex-1 p-3.5 bg-black/40 text-rose-300 font-mono text-xs focus:outline-none resize-none overflow-y-auto scrollbar-thin border-none"
                        />
                      </div>

                      <div className="flex flex-col border border-theme rounded-xl overflow-hidden bg-main-theme/30">
                        <div className="px-3.5 py-2 border-b border-theme bg-main-theme/50 flex items-center justify-between select-none">
                          <span className="text-[10px] font-mono text-emerald-400 font-bold uppercase tracking-wider">
                            Proposed Healing {diffData?.proposed ? `(${diffData.proposed.split('\n').length} lines)` : ''}
                          </span>
                          <span className="text-[9px] text-theme-dim italic">Editable</span>
                        </div>
                        <textarea
                          value={diffData?.proposed || ''}
                          onChange={(e) => {
                            const val = e.target.value;
                            setDiffData(prev => prev ? { ...prev, proposed: val } : null);
                          }}
                          className="flex-1 p-3.5 bg-black/40 text-emerald-300 font-mono text-xs focus:outline-none focus:ring-1 focus:ring-theme-accent/30 resize-none overflow-y-auto scrollbar-thin border-none"
                        />
                      </div>
                    </div>
                  </div>
                )}
              </div>

              <div className="px-5 py-4 border-t border-theme bg-main-theme/40 flex justify-end items-center gap-3 select-none">
                <button
                  onClick={() => {
                    setShowDiffModal(false);
                    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
                    if (isTauri) {
                      emit('mascot-wardrobe-changed', { item: 'default' }).catch(console.error);
                    }
                  }}
                  className="px-4 py-2 border border-theme hover:border-theme-accent-40 rounded-xl text-xs font-semibold text-theme-dim hover:text-theme-main transition-colors cursor-pointer"
                >
                  Discard Fix
                </button>
                {initialProposed && (
                  <button
                    onClick={() => setDiffData(prev => prev ? { ...prev, proposed: initialProposed } : null)}
                    className="px-4 py-2 border border-theme hover:border-theme-accent-40 rounded-xl text-xs font-semibold text-theme-dim hover:text-theme-main transition-colors cursor-pointer"
                  >
                    Revert Proposal
                  </button>
                )}
                <button
                  onClick={handleApplyHeal}
                  disabled={isFetchingHeal || !diffData?.proposed}
                  className="flex items-center gap-1.5 px-4.5 py-2 bg-theme-accent hover:shadow-[0_0_20px_rgba(234,88,12,0.3)] disabled:opacity-40 text-black font-semibold rounded-xl text-xs tracking-wide transition-all cursor-pointer"
                >
                  <Sparkles className="w-3.5 h-3.5 fill-black" />
                  <span>Approve & Apply Heal</span>
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* ── WHATSAPP DEVICE LINKING QR MODAL ────────────────────────────── */}
      <AnimatePresence>
        {showWhatsAppQR && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/60 backdrop-blur-sm"
          >
            <motion.div
              initial={{ scale: 0.95, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              exit={{ scale: 0.95, opacity: 0 }}
              className="bg-panel-theme border border-theme rounded-2xl shadow-2xl shadow-theme-glow w-[92vw] max-w-md p-6 flex flex-col text-left"
            >
              <div className="flex items-center justify-between border-b border-theme pb-3 mb-4 select-none">
                <h3 className="text-xs font-semibold text-theme-main font-mono uppercase tracking-wider">
                  WhatsApp Device Linking
                </h3>
                <button
                  onClick={() => setShowWhatsAppQR(false)}
                  className="p-1 rounded-lg border border-theme hover:border-theme-accent-40 text-theme-dim hover:text-theme-main transition-colors cursor-pointer"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              </div>
              
              <div className="flex flex-col items-center gap-4 py-4">
                <p className="text-xs text-theme-dim text-center select-none">
                  Scan the QR code below using WhatsApp on your phone to link your account.
                </p>
                
                <div className="w-64 h-64 bg-zinc-950/40 border border-theme rounded-xl flex items-center justify-center overflow-hidden p-4 relative">
                  <img
                    src={`http://127.0.0.1:8000/api/whatsapp/qr?t=${qrTimestamp}`}
                    alt="WhatsApp QR Code"
                    className="max-w-full max-h-full object-contain"
                    onError={(e) => {
                      e.currentTarget.style.display = 'none';
                      const parent = e.currentTarget.parentElement;
                      if (parent) {
                        const loader = parent.querySelector('.qr-loading');
                        if (loader) (loader as HTMLElement).style.display = 'flex';
                      }
                    }}
                    onLoad={(e) => {
                      e.currentTarget.style.display = 'block';
                      const parent = e.currentTarget.parentElement;
                      if (parent) {
                        const loader = parent.querySelector('.qr-loading');
                        if (loader) (loader as HTMLElement).style.display = 'none';
                      }
                    }}
                  />
                  <div className="qr-loading absolute inset-0 flex flex-col items-center justify-center gap-2 text-theme-dim select-none">
                    <Loader2 className="w-8 h-8 animate-spin text-theme-accent" />
                    <span className="text-[10px] font-mono">Waiting for session...</span>
                  </div>
                </div>
                
                <div className="text-[10px] text-theme-dim text-center italic mt-2 font-mono select-all">
                  WHATSAPP_AUTHORIZED_CONTACT must be set.
                </div>
              </div>
              
              <div className="flex justify-end gap-3 mt-4 border-t border-theme pt-3 select-none">
                <button
                  onClick={() => setShowWhatsAppQR(false)}
                  className="px-4 py-2 border border-theme hover:border-theme-accent-40 rounded-xl text-xs font-semibold text-theme-dim hover:text-theme-main transition-colors cursor-pointer"
                >
                  Close
                </button>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </>
  );
}
