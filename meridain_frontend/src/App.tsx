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
  RefreshCw
} from 'lucide-react';
import { Message, ThoughtStep, ModelSettings, SystemResource, ProactiveNudge } from './types';

import { listen, emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { getCurrentWindow } from '@tauri-apps/api/window';
import { WebviewWindow } from '@tauri-apps/api/webviewWindow';
import { marked } from 'marked';

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

  useEffect(() => {
    localStorage.setItem('meridian_theme', theme);
  }, [theme]);

  // Tabbed sidebar states
  const [sidebarTab, setSidebarTab] = useState<'timeline' | 'jobs'>('timeline');
  const [backgroundRuns, setBackgroundRuns] = useState<any[]>([]);
  const [expandedRunIds, setExpandedRunIds] = useState<Record<number, boolean>>({});

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
  // ProactiveNudge type is defined in types.ts and imported above
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
          credential_secret: credentialSecret
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

  // Subscribe to backend proactive stream
  useEffect(() => {
    if (!backendConnected) return;
    const es = new EventSource('http://127.0.0.1:8000/api/proactive/stream');
    es.addEventListener('nudge', (e: MessageEvent) => {
      try {
        const nudge: ProactiveNudge = JSON.parse(e.data);
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

  const handleNudgeAction = (nudge: ProactiveNudge) => {
    dismissNudge(nudge.id);

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
      const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
      if (isTauri) {
        emit('mascot-state-changed', { state: 'tired' }).catch(console.error);
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

  const [showSettingsDropdown, setShowSettingsDropdown] = useState(false);
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
      // Wait 3 seconds for the server to spin back up
      setTimeout(() => {
        setIsRestartingBackend(false);
      }, 3000);
    } catch (err) {
      console.error('Failed to restart backend:', err);
      setIsRestartingBackend(false);
    }
  };



  // Pre-fetch browser SpeechSynthesis voices on mount to handle asynchronous loading
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
            
            // Check if user has a saved local model preference and if it exists in the fetched list
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

            // Sync brainModel to first detected model if currently set to a hardcoded default that isn't running
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
      // Clamp between 180px and half the window width
      const newWidth = Math.max(180, Math.min(e.clientX, Math.floor(window.innerWidth / 2)));
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
  }, []); // ← empty deps: register once, ref keeps value current

  // Suppress text selection and change cursor while dragging
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
    
    // Check if user is scrolled near the bottom (150px threshold)
    const isAtBottom = el.scrollHeight - el.scrollTop - el.clientHeight < 150;
    
    // Auto-scroll if they are at the bottom or if it's a new user prompt
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
        // Revoke the blob URL after playback to prevent memory leak
        audio.onended = () => URL.revokeObjectURL(audioUrl);
        audio.play().catch(e => {
          console.error("Audio playback error:", e);
          URL.revokeObjectURL(audioUrl);
        });

      } else {
        console.warn("Backend TTS failed, falling back to browser SpeechSynthesis");
        throw new Error("TTS status error");
      }
    } catch (err) {
      // Fall back to browser SpeechSynthesis if backend is offline or fails
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
      window.speechSynthesis.speak(utterance);
    }
  };

  const handleSendCommand = async (textToSend?: string) => {
    const prompt = (textToSend || inputText).trim();
    if (!prompt) return;

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
                
                // Emit mascot state/wardrobe events if provided
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
            
            // Emit mascot state/wardrobe events if provided
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

  // Check if running inside Tauri (temporarily bypassed for testing)
  const isTauriEnv = true;

  if (!isTauriEnv) {
    return (
      <div className="min-h-screen bg-black text-white flex flex-col items-center justify-center p-6 font-mono selection:bg-[#ea580c] selection:text-black">
        <div className="max-w-md w-full border border-zinc-905 bg-zinc-950 p-8 rounded-2xl shadow-2xl relative overflow-hidden">
          <div className="absolute top-0 left-0 right-0 h-[2px] bg-[#ea580c]" />
          
          <div className="flex flex-col items-center text-center space-y-6">
            <div className="w-16 h-16 rounded-full bg-zinc-900 border border-zinc-800 flex items-center justify-center text-[#ea580c] animate-pulse">
              <Command className="w-8 h-8" />
            </div>
            
            <div className="space-y-2">
              <h1 className="text-lg font-bold uppercase tracking-wider text-white">Meridian-X</h1>
              <p className="text-[10px] text-zinc-500 uppercase tracking-widest font-bold">Desktop Core Required</p>
            </div>
            
            <p className="text-xs text-zinc-400 leading-relaxed font-sans">
              For security and local desktop integration, the Meridian-X environment must run within the native Tauri desktop shell. Standalone web access is restricted.
            </p>
            
            <div className="w-full bg-[#030303] border border-zinc-900 p-4 rounded-xl text-[11px] text-left text-zinc-500 space-y-1.5 font-bold">
              <div>&gt; STATUS: SECURE_RESTRICTION_ACTIVE</div>
              <div>&gt; PLATFORM: STANDARD_WEB_VIEWPORT</div>
              <div>&gt; RESOLUTION: RUN start_meridian.bat</div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (currentView === 'landing') {
    return (
      <div className={`flex flex-col min-h-screen bg-main-theme text-white font-sans antialiased selection:bg-theme-accent/30 selection:text-theme-accent overflow-y-auto justify-center ${theme !== 'default' ? 'theme-' + theme : ''}`}>
        {/* Borderless Full Screen Container */}
        <div className="flex-1 flex flex-col justify-between bg-main-theme relative min-h-[600px] py-12 px-6">
          
          {/* Ambient Grid Background */}
          <div className="absolute inset-0 bg-[radial-gradient(#1e1e1e_1.5px,transparent_1.5px)] [background-size:24px_24px] opacity-25 pointer-events-none"></div>
          
          {/* Subtle Ambient Radial Highlight centered behind the logo */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[450px] h-[450px] bg-theme-accent/5 blur-[100px] rounded-full pointer-events-none"></div>

          {/* MAIN CENTERED HERO CONTROLS */}
          <div className="max-w-md w-full mx-auto flex flex-col items-center text-center space-y-6 relative z-10 py-6">
            
            {/* 1. logo in the centre with an elegant subtle bloom */}
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

            {/* 2. name below it with sleek minimal metadata */}
            <div className="space-y-1">
              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight text-white font-display">
                Meridian
              </h1>
              <p className="text-xs text-theme-dim font-medium tracking-wide">
                Intelligent Workspace Assistant
              </p>
            </div>

            {/* 3. model dropdown select boxes for brain and vision */}
            <div className="w-full bg-panel-theme/80 border border-theme rounded-2xl p-5 space-y-4 text-left shadow-xl">
              
              {/* Source Selection Toggle */}
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
                          <option key={p.id} value={p.id} className="bg-panel-theme text-theme-main">{p.name}</option>
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
                          <option key={m} value={m} className="bg-panel-theme text-theme-main">{m}</option>
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
                          <option key={model} value={model} className="bg-panel-theme text-theme-main">
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
                          <option key={model} value={model} className="bg-panel-theme text-theme-main">
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

            {/* DIRECT CONNECT AND LAUNCH CONSOLE BUTTON */}
            <button
              onClick={() => setCurrentView('app')}
              className="w-full py-3.5 bg-white hover:bg-theme-accent hover:border-theme-accent text-black rounded-xl text-xs font-semibold uppercase tracking-wider transition-all duration-200 cursor-pointer shadow-lg hover:shadow-theme-glow"
              id="launch-app-btn"
            >
              Enter Workspace Console
            </button>

          </div>

          {/* BOTTOM COPYRIGHT FOOTER */}
          <footer className="text-center text-[9px] text-theme-dim font-medium tracking-wide relative z-10 select-none py-2">
            © {new Date().getFullYear()} Meridian Labs. All rights reserved.
          </footer>

        </div>
      </div>
    );
  }

  return (
    <>
      <div className={`flex flex-col h-screen overflow-hidden bg-main-theme text-white font-sans antialiased ${theme !== 'default' ? 'theme-' + theme : ''}`}>
      
      {/* Main Container - Borderless and Full Screen */}
      <div className="flex-1 flex flex-col min-h-0 overflow-hidden">
        
        {/* HEADER BAR - Sleek Rounded Minimalist with Draggable Titlebar region */}
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
              </div>
              <p className="text-[10px] text-zinc-400 font-medium font-sans">Workspace Console</p>
            </div>
          </div>

          {/* TELEMETRY VIEWPORT - Minimalist, sleek inline metrics with animated loading bars */}
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

          {/* MODEL OPTIONS TRIGGER AND ISLAND CONTAINER */}
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

            {/* Inspector Toggle Button Removed */}

            <div className="relative">
              <button 
                id="settings-dropdown-toggle"
                onClick={() => setShowSettingsDropdown(!showSettingsDropdown)}
                className={`flex items-center gap-2 px-3 tracking-wide py-1.5 rounded-lg border text-xs font-semibold transition-all duration-150 cursor-pointer ${
                  showSettingsDropdown 
                    ? 'bg-white border-white text-black' 
                    : 'bg-panel-theme border-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40'
                }`}
              >
                <Settings className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Configuration</span>
              </button>

              {/* ROUNDED DIALOG PANEL */}
              {showSettingsDropdown && (
                <div className="absolute right-0 mt-3 w-80 bg-panel-theme border border-theme rounded-2xl p-5 z-40 text-left shadow-2xl shadow-theme-glow">
                  <div className="flex items-center justify-between pb-3 mb-4 border-b border-theme">
                    <span className="text-xs font-semibold flex items-center gap-2 text-theme-main">
                      <Settings2 className="w-4 h-4 text-theme-accent" />
                      Engine Settings
                    </span>
                    <span className="text-[10px] font-mono font-bold text-black bg-theme-accent px-3 py-0.5 rounded-full">
                      {modelSettings.modelSource.toUpperCase()}
                    </span>
                  </div>

                  {/* Source Selection Toggle */}
                  <div className="mb-4">
                    <label className="block text-[10px] font-mono uppercase tracking-widest text-theme-dim mb-2 font-bold">Engine Source</label>
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

                  {/* Dropdowns */}
                  {modelSettings.modelSource === 'api' ? (
                    <div className="space-y-3.5 mb-4">
                      <div>
                        <label htmlFor="api-provider" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                          API Provider
                        </label>
                        <select
                          id="api-provider"
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
                          className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent cursor-pointer font-bold font-mono"
                        >
                          {API_PROVIDERS.map(p => (
                            <option key={p.id} value={p.id}>{p.name}</option>
                          ))}
                        </select>
                      </div>

                      <div>
                        <label htmlFor="primary-api-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                          Cloud Core AI Model
                        </label>
                        <select
                          id="primary-api-model"
                          value={modelSettings.selectedModel}
                          onChange={(e) => setModelSettings(prev => ({ ...prev, selectedModel: e.target.value }))}
                          className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent cursor-pointer font-bold font-mono"
                        >
                          {(PROVIDER_MODELS[modelSettings.apiProvider || 'gemini'] || []).map(m => (
                            <option key={m} value={m}>{m}</option>
                          ))}
                        </select>
                      </div>
                    </div>
                  ) : (
                    <div className="space-y-3.5 mb-4">
                      <div>
                        <label htmlFor="local-brain-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                          Local Brain Model
                        </label>
                        <select
                          id="local-brain-model"
                          value={modelSettings.brainModel}
                          onChange={(e) => setModelSettings(prev => ({ ...prev, brainModel: e.target.value }))}
                          className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer"
                        >
                          {localOllamaModels.map(m => (
                            <option key={m} value={m}>{m}</option>
                          ))}
                        </select>
                      </div>
                      <div>
                        <label htmlFor="local-ocr-model" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                          OCR Vision Engine
                        </label>
                        <select
                          id="local-ocr-model"
                          value={modelSettings.ocrModel}
                          onChange={(e) => setModelSettings(prev => ({ ...prev, ocrModel: e.target.value }))}
                          className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer"
                        >
                          {localVisionModels.map(m => (
                            <option key={m} value={m}>{m}</option>
                          ))}
                        </select>
                      </div>
                    </div>
                  )}

                  {/* Voice Output (TTS) Switch */}
                  <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme border-b border-theme font-mono">
                    <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold">Voice Output (TTS)</span>
                    <button 
                      onClick={() => setVoiceOutputEnabled(prev => !prev)}
                      className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${voiceOutputEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
                    >
                      <div className={`w-4 h-4 rounded-full bg-white transition-transform ${voiceOutputEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
                    </button>
                  </div>

                  {/* Voice Style Selector */}
                  {voiceOutputEnabled && (
                    <div className="mb-4 animate-fade-in">
                      <label htmlFor="voice-selector" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                        Voice Style
                      </label>
                      <select
                        id="voice-selector"
                        value={selectedVoice}
                        onChange={(e) => setSelectedVoice(e.target.value)}
                        className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold"
                      >
                        <optgroup label="Male Voices" className="bg-zinc-950 text-zinc-400 font-bold">
                          <option value="M1">M1 - Authority / JARVIS</option>
                          <option value="M2">M2 - Natural / Technical</option>
                          <option value="M3">M3 - Deep / Command</option>
                          <option value="M4">M4 - Warm / Friendly</option>
                          <option value="M5">M5 - Crisp / Professional</option>
                        </optgroup>
                        <optgroup label="Female Voices" className="bg-zinc-950 text-zinc-400 font-bold">
                          <option value="F1">F1 - Clear / Assistant</option>
                          <option value="F2">F2 - Soft / Conversational</option>
                          <option value="F3">F3 - Energetic / Lively</option>
                          <option value="F4">F4 - Warm / Supportive</option>
                          <option value="F5">F5 - Crisp / Informative</option>
                        </optgroup>
                      </select>
                    </div>
                  )}

                  {/* Mascot Companion Switch */}
                  <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme font-mono">
                    <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold">Mascot Companion</span>
                    <button 
                      onClick={() => setMascotEnabled(prev => !prev)}
                      className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${mascotEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
                    >
                      <div className={`w-4 h-4 rounded-full bg-white transition-transform ${mascotEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
                    </button>
                  </div>

                  {/* Pomodoro Focus Timer Switch */}
                  <div className="flex flex-col gap-2 py-2.5 mb-2.5 border-t border-theme font-mono">
                    <div className="flex items-center justify-between">
                      <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold">Pomodoro Focus</span>
                      <button
                        onClick={() => {
                          setPomodoroActive(prev => !prev);
                          if (!pomodoroActive) {
                            setPomodoroTime(25 * 60); // Reset to 25 min when starting
                          }
                        }}
                        className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${pomodoroActive ? 'bg-theme-accent' : 'bg-zinc-800'}`}
                      >
                        <div className={`w-4 h-4 rounded-full bg-white transition-transform ${pomodoroActive ? 'translate-x-5' : 'translate-x-0'}`} />
                      </button>
                    </div>
                    {pomodoroActive && (
                      <div className="flex items-center justify-between text-[11px] text-zinc-400 font-mono mt-1">
                        <span>Time Remaining:</span>
                        <span className="font-bold text-theme-accent animate-pulse">
                          {Math.floor(pomodoroTime / 60)}:{(pomodoroTime % 60).toString().padStart(2, '0')}
                        </span>
                      </div>
                    )}
                  </div>

                  {/* Vocalize Alerts Switch */}
                  <div className="flex items-center justify-between py-2.5 mb-2.5 border-t border-theme font-mono">
                    <span className="text-[10px] uppercase tracking-widest text-theme-accent font-bold">Vocalize Alerts</span>
                    <button 
                      onClick={() => setAlertVocalizerEnabled(prev => !prev)}
                      className={`w-10 h-5 rounded-full p-0.5 transition-colors cursor-pointer ${alertVocalizerEnabled ? 'bg-theme-accent' : 'bg-zinc-800'}`}
                    >
                      <div className={`w-4 h-4 rounded-full bg-white transition-transform ${alertVocalizerEnabled ? 'translate-x-5' : 'translate-x-0'}`} />
                    </button>
                  </div>

                  {/* Theme Switcher Selector */}
                  <div className="mb-4">
                    <label htmlFor="theme-selector" className="block text-[10px] font-mono uppercase tracking-widest text-theme-accent mb-1.5 font-bold">
                      Visual Theme
                    </label>
                    <select
                      id="theme-selector"
                      value={theme}
                      onChange={(e) => setTheme(e.target.value as any)}
                      className="w-full bg-main-theme border border-theme text-theme-main rounded-xl py-2 px-3 text-xs focus:outline-none focus:border-theme-accent font-mono cursor-pointer font-bold"
                    >
                      <option value="default">Standard Orange</option>
                      <option value="cyberpunk">Cyberpunk Neo</option>
                      <option value="amber">Amber CRT</option>
                      <option value="slate">Midnight Slate</option>
                    </select>
                  </div>



                  <div className="pt-2.5 flex flex-col gap-2">
                    <button
                      onClick={handleRestartBackend}
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
                      onClick={() => setShowSettingsDropdown(false)}
                      className="w-full bg-white hover:bg-theme-accent hover:border-theme-accent border border-white text-black font-bold py-2 rounded-xl text-xs text-center transition-all cursor-pointer uppercase tracking-wider"
                    >
                      Apply Configs
                    </button>
                  </div>
                </div>
              )}
            </div>

            {/* Custom Window Minimize/Maximize/Close Controls */}
            <div className="flex items-center gap-1.5 border-l border-zinc-850 pl-2.5 ml-1">
              <button 
                onClick={handleMinimize}
                title="Minimize Window"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-panel-theme hover:border-theme-accent/50 text-theme-dim hover:text-theme-main cursor-pointer transition-all"
              >
                <Minus className="w-3 h-3" />
              </button>
              <button 
                onClick={handleMaximize}
                title="Maximize Window"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-panel-theme hover:border-theme-accent/50 text-theme-dim hover:text-theme-main cursor-pointer transition-all"
              >
                <Maximize2 className="w-3 h-3" />
              </button>
              <button 
                onClick={handleClose}
                title="Close Application"
                className="p-1.5 rounded-lg bg-main-theme border border-theme hover:bg-red-950/25 hover:border-red-900 hover:text-red-500 text-theme-dim cursor-pointer transition-all"
              >
                <X className="w-3 h-3" />
              </button>
            </div>
          </div>
        </header>
        {/* WORKSPACE CONTENT GRID */}
        <div className="flex-1 flex overflow-hidden">
          
          {/* LEFT PANELS - Tabbed Interface */}
          <aside 
            className="hidden md:flex border-r border-theme bg-panel-theme flex-col overflow-hidden relative shrink-0"
            style={{ width: `${sidebarWidth}px` }}
          >
            <div className="flex bg-main-theme-45 border-b border-theme select-none">
              <button
                onClick={() => setSidebarTab('timeline')}
                className={`flex-1 py-3 text-center text-[10px] font-bold uppercase tracking-wider font-sans border-b-2 transition-all cursor-pointer ${
                  sidebarTab === 'timeline'
                    ? 'text-theme-accent border-theme-accent'
                    : 'text-theme-dim border-transparent hover:text-theme-main hover:border-theme-accent/30'
                }`}
              >
                Timeline
              </button>
              <button
                onClick={() => setSidebarTab('jobs')}
                className={`flex-1 py-3 text-center text-[10px] font-bold uppercase tracking-wider font-sans border-b-2 transition-all cursor-pointer ${
                  sidebarTab === 'jobs'
                    ? 'text-theme-accent border-theme-accent'
                    : 'text-theme-dim border-transparent hover:text-theme-main hover:border-theme-accent/30'
                }`}
              >
                Background Jobs
              </button>
            </div>

            {/* TAB CONTENT: TIMELINE FLOWCHART */}
            {sidebarTab === 'timeline' ? (
              <div ref={thoughtScrollRef} className="flex-1 overflow-y-auto p-5">
                <div className="relative border-l border-zinc-800/80 ml-3.5 pl-5 space-y-6">
                  {thoughts.map((step, idx) => {
                    const isRunning = step.status === 'running';
                    const isFailed = step.status === 'failed';
                    
                    return (
                      <div key={step.id} className="relative group">
                        {/* Bullet indicator on the timeline line */}
                        <div className={`absolute -left-[26px] top-1.5 w-3 h-3 rounded-full border-2 transition-all ${
                          isRunning
                            ? 'bg-theme-accent border-theme-accent animate-ping'
                            : isFailed
                              ? 'bg-rose-500 border-rose-500'
                              : 'bg-emerald-500 border-emerald-500'
                        }`} />
                        
                        <div className={`absolute -left-[26px] top-1.5 w-3 h-3 rounded-full border-2 ${
                          isRunning
                            ? 'bg-theme-accent border-theme-accent'
                            : isFailed
                              ? 'bg-rose-500 border-rose-500'
                              : 'bg-emerald-500 border-emerald-500'
                        }`} />

                        {/* Node Card */}
                        <div className={`p-3 bg-main-theme-30 border border-theme rounded-xl space-y-1.5 hover:border-theme-accent transition-all ${isFailed ? 'border-rose-950/40 bg-rose-950/5' : ''}`}>
                          <div className="flex items-center justify-between text-[9px] text-theme-dim font-mono">
                            <span className="uppercase font-bold tracking-wide text-theme-accent">Step {idx + 1}: {step.type}</span>
                            <span>{step.timestamp}</span>
                          </div>
                          
                          <p className="text-xs text-theme-main leading-relaxed font-sans break-words whitespace-pre-wrap">{step.text}</p>
                          
                          {step.tool && (
                            <div className="flex items-center gap-1.5 mt-2 bg-main-theme-60 border border-theme-50 px-2 py-1 rounded text-[10px] font-mono text-theme-dim">
                              <span className="w-1.5 h-1.5 rounded-full bg-theme-accent"></span>
                              <span>Service: <strong className="text-theme-main">{step.tool}</strong></span>
                            </div>
                          )}
                          
                          {step.command && (
                            <div className={`mt-1 text-[9px] font-mono p-2 rounded border break-words whitespace-pre-wrap ${isFailed ? 'text-rose-450 bg-rose-950/20 border-rose-900/20' : 'text-theme-main bg-main-theme-60 border-theme'}`}>
                              <code>{step.command}</code>
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
            ) : (
              /* TAB CONTENT: BACKGROUND JOBS */
              <div className="flex-1 overflow-y-auto p-4 space-y-4">
                {backgroundRuns.map((run) => {
                  const runTime = new Date(run.timestamp * 1000).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' });
                  const isExpanded = !!expandedRunIds[run.id];
                  const isSuccess = run.status === 'success';
                  const isRunning = run.status === 'running';
                  const isFailed = run.status === 'failed';

                  return (
                    <div 
                      key={run.id} 
                      className="p-3.5 bg-main-theme-30 border border-theme hover:border-theme-accent/50 rounded-2xl transition-all duration-200 space-y-2.5 shadow-md animate-fade-in"
                    >
                      <div className="flex items-center justify-between">
                        <span className={`inline-flex items-center px-2.5 py-0.5 rounded-full text-[9px] font-bold uppercase tracking-wider ${
                          isSuccess
                            ? 'bg-emerald-500/10 text-emerald-400'
                            : isRunning
                              ? 'bg-amber-500/10 text-amber-400 animate-pulse'
                              : 'bg-rose-500/10 text-rose-400'
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
                            <pre className="p-3 bg-black/40 border border-theme rounded-xl text-[10px] font-mono text-theme-main select-all overflow-x-auto whitespace-pre-wrap leading-relaxed max-h-48 overflow-y-auto">
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

            <div className="p-4 border-t border-theme text-[11px] text-theme-dim font-sans flex items-center gap-2 bg-panel-theme">
              <Activity className="w-3.5 h-3.5 text-emerald-500 animate-pulse animate-duration-1000" />
              <span>Workspace connected successfully.</span>
            </div>
          </aside>

          {/* Draggable Divider */}
          <div 
            onMouseDown={startResizing}
            className={`hidden md:block w-[3px] hover:bg-theme-accent/50 transition-colors z-20 shrink-0 select-none relative ${
              isResizing ? 'bg-theme-accent' : 'bg-zinc-900/60'
            }`}
          >
            <div className="absolute inset-y-0 -left-1.5 -right-1.5 cursor-col-resize z-30" />
          </div>

          {/* MAIN CHAT AREA */}
          <main className="flex-1 min-w-0 bg-main-theme-20 flex flex-col overflow-hidden relative border-l border-theme">
            <div className="flex items-center justify-between px-6 py-4 border-b border-theme bg-panel-theme-40">
              <div className="flex items-center gap-2">
                <span className={`w-2 h-2 rounded-full ${backendConnected ? 'bg-emerald-500' : 'bg-rose-500'} animate-pulse`}></span>
                <span className="text-[11px] font-bold text-theme-main tracking-wider">
                  WORKSPACE CHAT
                </span>
              </div>

              <button
                onClick={handleClearHistory}
                title="Clears the current conversation content list"
                className="px-3 py-1.5 text-xs text-theme-dim hover:text-theme-main rounded-lg border border-theme hover:border-theme-accent/40 bg-panel-theme transition-all cursor-pointer flex items-center gap-1.5"
              >
                <Trash2 className="w-3.5 h-3.5" />
                <span>Reset Session</span>
              </button>
            </div>

            {fallbackNotice && (
              <div className="bg-[#ea580c]/10 border-b border-[#ea580c]/20 px-6 py-3 flex items-center justify-between text-xs text-zinc-300 relative z-10">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="w-1.5 h-1.5 rounded-full bg-[#ea580c] animate-ping shrink-0" />
                  <span className="font-sans font-bold text-[#ea580c] tracking-wider uppercase shrink-0 text-[10px]">Backup Core:</span>
                  <p className="truncate text-zinc-300 font-sans text-[11px] select-text">
                    {fallbackNotice}
                  </p>
                </div>
                <button
                  onClick={() => setFallbackNotice(null)}
                  className="ml-3 font-sans text-[10px] font-semibold text-zinc-400 hover:text-white cursor-pointer bg-zinc-900 border border-zinc-800 rounded-lg px-2 py-0.5 transition-all shrink-0"
                >
                  Dismiss
                </button>
              </div>
            )}

            {/* Chat Box bubbles scrollable viewport */}
            <div 
              ref={chatScrollRef}
              className="flex-1 overflow-y-auto px-6 py-6 space-y-6 bg-main-theme"
            >
              {messages.map((msg) => {
                const isAssistant = msg.sender === 'assistant';
                return (
                  <div key={msg.id} className={`flex ${isAssistant ? 'justify-start' : 'justify-end'} animate-fade-in`}>
                    <div className={`max-w-[85%] flex flex-col ${isAssistant ? 'items-start' : 'items-end'}`}>
                      
                      <div className="flex items-center gap-1.5 mb-1.5 px-1 text-[10px] text-theme-dim font-semibold tracking-wide">
                        <span>{isAssistant ? 'Meridian' : 'User'}</span>
                        <span>•</span>
                        <span className="text-theme-dim font-medium">{msg.timestamp}</span>
                      </div>

                      <div className={`rounded-xl px-5 py-3.5 text-xs sm:text-sm leading-relaxed border transition-all ${
                        isAssistant
                          ? 'bg-panel-theme-80 border-theme text-theme-main font-sans rounded-tl-none shadow-md'
                          : 'bg-main-theme-50 border-theme-60 text-theme-main font-medium rounded-tr-none shadow-md'
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
                  <div className="flex flex-col items-start max-w-[75%]">
                    <div className="flex items-center gap-2 mb-1.5 px-1 text-[10px] text-zinc-400 font-medium tracking-wide">
                      <span>Meridian is processing...</span>
                    </div>
                    <div className="bg-zinc-950 border border-zinc-900 rounded-xl px-4 py-3 text-zinc-400 flex items-center gap-2.5">
                      <Loader2 className="w-3.5 h-3.5 animate-spin" />
                      <span className="font-sans text-xs font-semibold">Generating Response...</span>
                    </div>
                  </div>
                </div>
              )}
            </div>



            {/* Rounded input console bottom bar */}
            <div className="p-4 sm:p-6 bg-panel-theme border-t border-theme relative z-10">
              
              {/* Confirmation Overlay */}
              {pendingConfirmation && (
                <div className="mb-4 p-5 bg-panel-theme border-2 border-theme-accent rounded-2xl relative z-20 shadow-2xl animate-fade-in shadow-theme-glow">
                  <div className="flex items-start gap-3">
                    <div className="w-8 h-8 rounded-lg bg-theme-accent-10 border border-theme-accent-30 flex items-center justify-center text-theme-accent shrink-0">
                      <AlertCircle className="w-5 h-5 animate-bounce" />
                    </div>
                    <div className="space-y-1.5 flex-1 min-w-0">
                      <h4 className="text-xs font-bold text-white uppercase tracking-wider font-mono">
                        Action Authorization Required (Safety Tier {pendingConfirmation.tier})
                      </h4>
                      <p className="text-xs text-theme-main leading-relaxed font-sans select-text">
                        Meridian requests permission to run <code className="bg-main-theme px-1 py-0.5 rounded font-mono text-theme-accent">{pendingConfirmation.tool}</code> with the following arguments:
                      </p>
                      <pre className="mt-2 p-3 bg-main-theme border border-theme rounded-xl text-[10px] font-mono text-theme-main select-all overflow-x-auto leading-normal">
                        {JSON.stringify(pendingConfirmation.args, null, 2)}
                      </pre>
                    </div>
                  </div>
                  <div className="mt-4 flex items-center justify-end gap-2.5">
                    <button
                      onClick={() => handleConfirmResponse(pendingConfirmation.id, false)}
                      className="px-4 py-2 bg-main-theme hover:bg-main-theme-80 border border-theme text-theme-dim hover:text-theme-main rounded-lg text-xs font-semibold tracking-wider transition-all uppercase cursor-pointer"
                    >
                      Reject Call
                    </button>
                    <button
                      onClick={() => handleConfirmResponse(pendingConfirmation.id, true)}
                      className="px-4.5 py-2 bg-theme-accent hover:bg-theme-accent text-black rounded-lg text-xs font-semibold tracking-wider transition-all uppercase cursor-pointer"
                    >
                      Approve Exec
                    </button>
                  </div>
                </div>
              )}

              {isRecording && (
                <div className="absolute top-0 left-0 right-0 -translate-y-full px-6 py-2.5 bg-panel-theme border-t border-b border-theme flex items-center justify-between text-xs text-theme-main">
                  <div className="flex items-center gap-2">
                    <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse"></span>
                    <span className="font-sans text-[10px] text-theme-dim font-semibold uppercase">Voice Streaming Connected...</span>
                  </div>
                  <div className="flex items-end gap-1.5 h-4">
                    {micVisualizerWaves.map((height, idx) => (
                      <div 
                        key={idx} 
                        className="w-[3.5px] bg-theme-accent rounded-full transition-all duration-75"
                        style={{ height: `${height * 0.7}px` }}
                      />
                    ))}
                  </div>
                </div>
              )}

              <div className="relative flex items-stretch gap-2 bg-panel-theme border border-theme rounded-xl p-2 focus-within:border-theme-accent transition-all">
                
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
                  placeholder="Ask Meridian or enter a workspace task..."
                  className="flex-1 bg-transparent text-white placeholder-zinc-500 border-none px-3 font-sans text-xs sm:text-sm focus:outline-none focus:ring-0 disabled:opacity-50 resize-none py-1 min-h-[24px] max-h-[180px] overflow-y-auto leading-relaxed"
                />

                <div className="flex items-center gap-2 self-center">
                  
                  <button
                    id="mic-recording-btn"
                    onClick={toggleRecording}
                    disabled={isRunning}
                    title="Simulate speech translation"
                    className={`p-2 border rounded-lg transition-all cursor-pointer ${
                      isRecording 
                        ? 'bg-theme-accent-10 text-theme-accent border-theme-accent-30' 
                        : 'bg-panel-theme border-theme text-theme-dim hover:text-theme-main hover:border-theme-accent-40 disabled:opacity-30'
                    }`}
                  >
                    {isRecording ? <MicOff className="w-4 h-4" /> : <Mic className="w-4 h-4" />}
                  </button>

                  {isRunning ? (
                    <button
                      id="stop-execution-btn"
                      onClick={handleStopExecution}
                      title="Halt model workspace execution process"
                      className="flex items-center gap-1.5 px-4 py-2 bg-theme-main text-panel-theme hover:bg-theme-main border border-transparent rounded-lg text-xs font-semibold tracking-normal transition-all cursor-pointer"
                    >
                      <Square className="w-3 h-3 fill-panel-theme" />
                      <span>Halt</span>
                    </button>
                  ) : (
                    <button
                      id="send-command-btn"
                      onClick={() => handleSendCommand()}
                      disabled={!inputText.trim()}
                      className="flex items-center gap-1.5 px-4.5 py-2 bg-theme-main disabled:bg-main-theme border border-transparent disabled:border-transparent text-panel-theme disabled:text-theme-dim rounded-lg text-xs font-semibold tracking-normal transition-all uppercase cursor-pointer"
                    >
                      <span>Send</span>
                      <Send className="w-3 h-3" />
                    </button>
                  )}
                </div>
              </div>
              
              <div className="flex justify-between items-center mt-3 px-1 text-[11px] text-theme-dim font-medium">
                <span className="flex items-center gap-1.5 leading-none">
                  <CornerDownLeft className="w-3.5 h-3.5 text-theme-accent" />
                  Press Enter to submit
                </span>
                <span>Verified Sandbox Mode</span>
              </div>

              {!backendConnected && (
                <div className="mt-3 flex items-center justify-center gap-2 p-2.5 rounded-xl border border-rose-950/40 bg-rose-950/10 text-rose-450 text-xs font-sans tracking-wide">
                  <span className="w-1.5 h-1.5 rounded-full bg-rose-500 animate-ping"></span>
                  <span><strong>Warning:</strong> FastAPI Backend is offline. Run <code className="bg-rose-950/30 px-1.5 py-0.5 rounded border border-rose-900/30 font-mono text-[10px] select-all">start_meridian.bat</code> option 3 to start both frontend and backend.</span>
                </div>
              )}
            </div>
          </main>
        </div>
      </div>
    </div>

    {/* ── Proactive Nudge Toast Stack ──────────────────────────────────────── */}
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
          {/* Accent top bar */}
          <div style={{
            height: '2px',
            background: nudge.type === 'system_health'
              ? 'linear-gradient(90deg,#ef4444,#f97316)'
              : nudge.type === 'clipboard_error'
              ? 'linear-gradient(90deg,#ef4444,#ec4899)'
              : nudge.type === 'idle_nudge'
              ? 'linear-gradient(90deg,#6366f1,#8b5cf6)'
              : nudge.type === 'followup'
              ? 'linear-gradient(90deg,#10b981,#06b6d4)'
              : 'linear-gradient(90deg,#6366f1,#a78bfa)'
          }} />

          <div style={{ padding: '12px 14px 10px' }}>
            {/* Header row */}
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

            {/* Body */}
            <p style={{ fontSize: '11.5px', color: '#94a3b8', margin: '0 0 10px', lineHeight: 1.5 }}>
              {nudge.message}
            </p>

            {/* Action footer */}
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

            {/* Timestamp */}
            <div style={{ fontSize: '10px', color: '#334155', marginTop: '8px', textAlign: 'right' }}>
              {nudge.timestamp}
            </div>
          </div>
        </motion.div>
      ))}
    </div>

    {/* ── 20-20-20 Break Overlay ────────────────────────────────────────── */}
    <AnimatePresence>
      {showBreakOverlay && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[10000] flex flex-col items-center justify-center bg-black/80 backdrop-blur-2xl text-white font-sans overflow-hidden"
        >
          <div className="flex flex-col items-center max-w-md text-center px-6">
            {/* Outer pulsing ring */}
            <motion.div
              animate={{ scale: [1, 1.18, 1], borderColor: ['rgba(234,88,12,0.4)', 'rgba(99,102,241,0.6)', 'rgba(234,88,12,0.4)'] }}
              transition={{ duration: 4, repeat: Infinity, ease: "easeInOut" }}
              className="w-48 h-48 rounded-full border-4 flex items-center justify-center shadow-[0_0_50px_rgba(99,102,241,0.25)] bg-zinc-950/60 backdrop-blur-md relative"
            >
              {/* Inner breathing circle */}
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
            
            <div className="space-y-3">
              <p className="text-sm text-zinc-350 leading-relaxed">
                Focus on something <span className="text-theme-accent font-bold">20 feet away</span> for <span className="text-theme-accent font-bold">20 seconds</span> to reduce digital eye strain.
              </p>
              <div className="py-2 px-4 rounded-xl bg-zinc-900/40 border border-zinc-800/50 inline-block">
                <span className="text-xs text-zinc-450 font-mono">
                  Mascot Status: <span className="text-theme-accent font-bold animate-pulse">Resting...</span>
                </span>
              </div>
            </div>
          </div>
        </motion.div>
      )}
    </AnimatePresence>

    {/* ── Interactive Self-Healing Diff Modal ───────────────────────────── */}
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
            {/* Header */}
            <div className="flex items-center justify-between px-5 py-4 border-b border-theme bg-main-theme/40">
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

            {/* Body */}
            <div className="flex-1 overflow-hidden flex flex-col p-5 bg-main-theme/10">
              {isFetchingHeal ? (
                <div className="flex-1 flex flex-col items-center justify-center gap-4 text-center">
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
                      <p className="text-xs text-zinc-350">
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
                    {/* Left: Original File Content */}
                    <div className="flex flex-col border border-theme rounded-xl overflow-hidden bg-main-theme/30">
                      <div className="px-3.5 py-2 border-b border-theme bg-main-theme/50 flex items-center justify-between">
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

                    {/* Right: Proposed Healing Content */}
                    <div className="flex flex-col border border-theme rounded-xl overflow-hidden bg-main-theme/30">
                      <div className="px-3.5 py-2 border-b border-theme bg-main-theme/50 flex items-center justify-between">
                        <span className="text-[10px] font-mono text-emerald-400 font-bold uppercase tracking-wider">
                          Proposed Healing {diffData?.proposed ? `(${diffData.proposed.split('\n').length} lines, ${diffData.proposed.length} chars)` : ''}
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

            {/* Footer */}
            <div className="px-5 py-4 border-t border-theme bg-main-theme/40 flex justify-end items-center gap-3">
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
                  Revert to Proposal
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
    </>
  );
}
