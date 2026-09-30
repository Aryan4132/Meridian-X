import React, { useState, useEffect, useRef } from 'react';
import { getCurrentWindow, LogicalSize, LogicalPosition, currentMonitor } from '@tauri-apps/api/window';
import { listen, emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { motion, AnimatePresence } from 'motion/react';
import { 
  LogIn, 
  EyeOff, 
  Loader2,
  Mic,
  MicOff,
  Volume2,
  VolumeX,
  Crown,
  X,
  Play
} from 'lucide-react';
import { Mascot3DCharacter } from './Mascot3DCharacter';
import { API_BASE_URL } from './config';
import { applyThemeToDocument, resolveTheme, DEFAULT_THEME } from './AppContext';
import { streamingAudio } from './services/streamingAudioPlayer';


// Mirrors the canonical index.css themes (+ legacy aliases). Unknown IDs
// fall back to DEFAULT_THEME so the mascot never renders unstyled.
const THEME_COLORS: Record<string, { accent: string; bg: string; border: string }> = {
  tokyonight:   { accent: '#7aa2f7', bg: '#1a1b26', border: 'rgba(122, 162, 247, 0.25)' },
  oled:         { accent: '#38bdf8', bg: '#000000', border: 'rgba(56, 189, 248, 0.30)' },
  'vscode-dark':{ accent: '#007acc', bg: '#1e1e1e', border: 'rgba(0, 122, 204, 0.35)' },
  cyberslate:   { accent: '#E8A020', bg: '#141920', border: 'rgba(232, 160, 32, 0.20)' },
  artdeco:      { accent: '#D4AF37', bg: '#0A0A0A', border: 'rgba(212, 175, 55, 0.25)' },
  neobrutalism: { accent: '#FFDE59', bg: '#FFFDF5', border: '#000000' },
  cyberpunk:    { accent: '#FF0055', bg: '#070614', border: 'rgba(255, 0, 85, 0.30)' },
  retro:        { accent: '#FF71CE', bg: '#0A0414', border: 'rgba(255, 113, 206, 0.25)' },
  ink:          { accent: '#818CF8', bg: '#111113', border: 'rgba(129, 140, 248, 0.25)' },
  nordic:       { accent: '#38BDF8', bg: '#0B0F17', border: 'rgba(56, 189, 248, 0.25)' },
  maximalism:   { accent: '#FF007A', bg: '#0D021A', border: 'rgba(255, 0, 122, 0.30)' },
  paper:        { accent: '#D95338', bg: '#F4F2EC', border: 'rgba(217, 83, 56, 0.25)' },
  sakura:       { accent: '#E85D75', bg: '#FFF5F7', border: 'rgba(232, 93, 117, 0.25)' },
  solaris:      { accent: '#2563EB', bg: '#F4F6FB', border: 'rgba(37, 99, 235, 0.25)' },
  chronos:      { accent: '#4CC9F0', bg: '#0F0F1A', border: 'rgba(76, 201, 240, 0.20)' },
  // Legacy aliases (old stored values) resolve to cyberslate styling.
  slate:        { accent: '#E8A020', bg: '#141920', border: 'rgba(232, 160, 32, 0.18)' },
  void:         { accent: '#E8A020', bg: '#141920', border: 'rgba(232, 160, 32, 0.18)' },
};

const LIGHT_THEMES = ['neobrutalism', 'paper', 'sakura', 'solaris'];

export function mascotThemeMode(theme: string): 'dark' | 'light' {
  return LIGHT_THEMES.includes(theme) ? 'light' : 'dark';
}






type HudState = 'idle' | 'working' | 'success' | 'error';

interface MascotCharacterProps {
  state: string;
  accentColor: string;
  speechAmplitude?: number;
  themeMode?: 'dark' | 'light';
}

export function MascotCharacter({ state, accentColor, speechAmplitude = 0, themeMode = 'dark' }: MascotCharacterProps) {
  // Core orb state colors: Blue = idle/happy/default, Yellow = working/diagnostic, Red = failed/disapproving, Green = success/typing
  const stateColor = 
    state === 'disapproving' || state === 'error' || state === 'failed' ? '#F43F5E' : 
    state === 'working' || state === 'diagnostic' ? '#F59E0B' : 
    state === 'success' || state === 'typing' ? '#10B981' : 
    '#3B82F6';

  return (
    <div className="relative w-8 h-8 flex-shrink-0 flex items-center justify-center">
      {/* State-specific background glow */}
      <span className={`absolute w-7 h-7 rounded-full opacity-35 blur-[8px] transition-colors duration-500 ${
        state === 'sleeping' ? 'bg-[var(--accent-2)]' :
        state === 'tired' ? 'bg-[var(--accent)]' :
        state === 'disapproving' ? 'bg-[var(--danger)]' :
        state === 'diagnostic' ? 'bg-[var(--warning)]' :
        state === 'typing' ? 'bg-[var(--success)]' : 'bg-[var(--accent)]'
      }`} />

      <div className="w-full h-full flex items-center justify-center relative z-10">
        <Mascot3DCharacter
          state={state}
          accentColor={stateColor}
          speechAmplitude={speechAmplitude}
          themeMode={themeMode}
          size={32}
        />
      </div>

      {/* Floating sleep Zzz particles */}
      {state === 'sleeping' && (
        <div className="absolute inset-0 pointer-events-none">
          {[[9, 0], [12, 0.8], [15, 1.6]].map(([yShift, delay]) => (
            <motion.span
              key={delay}
              className="absolute text-[8px] font-bold text-[var(--accent-2)] select-none"
              initial={{ x: 10, y: -2, opacity: 0, scale: 0.5 }}
              animate={{ x: [10, 14, 18], y: [-2, -yShift, -yShift - 8], opacity: [0, 1, 0], scale: [0.5, 1, 0.8] }}
              transition={{ duration: 2.8, repeat: Infinity, delay }}
            >
              z
            </motion.span>
          ))}
        </div>
      )}
    </div>
  );
}


// FIX: reuse ONE shared AudioContext — creating a new context per state
// change leaks them (browsers cap ~6 concurrent contexts, after which UI
// sound effects silently stop playing).
let sharedAudioCtx: AudioContext | null = null;
const getSharedAudioContext = (): AudioContext | null => {
  const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
  if (!AudioContextClass) return null;
  if (!sharedAudioCtx || sharedAudioCtx.state === 'closed') {
    try {
      sharedAudioCtx = new AudioContextClass();
    } catch {
      return null;
    }
  }
  if (sharedAudioCtx.state === 'suspended') {
    sharedAudioCtx.resume().catch(() => {});
  }
  return sharedAudioCtx;
};

const playSoundEffect = (state: string) => {
  if (localStorage.getItem('meridian_mascot_audio_fx') === 'false') return;

  try {
    const ctx = getSharedAudioContext();
    if (!ctx) return;

    const volume = parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5');
    
    if (state === 'happy' || state === 'default') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(520, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(780, ctx.currentTime + 0.15);
      gain.gain.setValueAtTime(0.1 * volume, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.005 * volume, ctx.currentTime + 0.15);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.15);
    } else if (state === 'sleeping') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(260, ctx.currentTime);
      osc.frequency.linearRampToValueAtTime(130, ctx.currentTime + 0.6);
      gain.gain.setValueAtTime(0.06 * volume, ctx.currentTime);
      gain.gain.linearRampToValueAtTime(0.005 * volume, ctx.currentTime + 0.6);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.6);
    } else if (state === 'diagnostic') {
      const now = ctx.currentTime;
      [now, now + 0.08].forEach(time => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(950, time);
        gain.gain.setValueAtTime(0.06 * volume, time);
        gain.gain.exponentialRampToValueAtTime(0.005 * volume, time + 0.03);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(time);
        osc.stop(time + 0.03);
      });
    } else if (state === 'disapproving') {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(170, ctx.currentTime);
      gain.gain.setValueAtTime(0.08 * volume, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.005 * volume, ctx.currentTime + 0.4);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.4);
    }
  } catch (err) {
    console.error("Web Audio synthesis error:", err);
  }
};

export default function Mascot({ mascotState: propMascotState }: { mascotState?: string }) {
  const [mascotState, setMascotState] = useState<string>('default');
  const [speechAmplitude, setSpeechAmplitude] = useState<number>(0);
  const [audioEnabled, setAudioEnabled] = useState<boolean>(() => localStorage.getItem('meridian_mascot_audio_fx') !== 'false');
  const [voiceLogs, setVoiceLogs] = useState<string[]>([]);
  const [hudState, setHudState] = useState<HudState>('idle');
  const [isRunning, setIsRunning] = useState(false);
  const [latestThought, setLatestThought] = useState<any | null>(null);
  const [recentThoughts, setRecentThoughts] = useState<any[]>([]);
  const [isExpanded, setIsExpanded] = useState(false);
  const [theme, setTheme] = useState<string>(DEFAULT_THEME);
  const [voiceState, setVoiceState] = useState<'idle' | 'listening' | 'transcribing' | 'thinking' | 'speaking'>('idle');
  const [voiceText, setVoiceText] = useState<string>('');
  const [isAutomating, setIsAutomating] = useState(false);
  const [automatingTool, setAutomatingTool] = useState('');
  
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);
  const successTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const typingTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const lastEventTimestampRef = useRef<number>(0);
  const generationIdRef = useRef<number>(0);
  const appWindow = getCurrentWindow();
  const colors = THEME_COLORS[resolveTheme(theme)] || THEME_COLORS[DEFAULT_THEME];

  const hoverTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const handleMouseEnter = () => {
    if (hoverTimeoutRef.current) {
      clearTimeout(hoverTimeoutRef.current);
      hoverTimeoutRef.current = null;
    }
    setIsExpanded(true);
  };

  const handleMouseLeave = () => {
    if (hoverTimeoutRef.current) {
      clearTimeout(hoverTimeoutRef.current);
    }
    hoverTimeoutRef.current = setTimeout(() => {
      setIsExpanded(false);
      hoverTimeoutRef.current = null;
    }, 280);
  };

  useEffect(() => {
    return () => {
      if (hoverTimeoutRef.current) clearTimeout(hoverTimeoutRef.current);
    };
  }, []);

  useEffect(() => {
    if (propMascotState) setMascotState(propMascotState);
  }, [propMascotState]);

  // Sync theme to Mascot window (preserves non-theme <html> classes)
  useEffect(() => {
    const applyCurrentTheme = () => {
      applyThemeToDocument(localStorage.getItem('theme'));
    };
    applyCurrentTheme();

    window.addEventListener('meridian-theme-changed', applyCurrentTheme);
    window.addEventListener('storage', applyCurrentTheme);

    let unlistenTheme: any;
    if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__) {
      listen('meridian-theme-changed', (event: any) => {
        applyThemeToDocument(event.payload?.theme || localStorage.getItem('theme'));
      }).then(u => { unlistenTheme = u; });
    }

    return () => {
      window.removeEventListener('meridian-theme-changed', applyCurrentTheme);
      window.removeEventListener('storage', applyCurrentTheme);
      if (unlistenTheme) unlistenTheme();
    };
  }, []);

  useEffect(() => {
    const handleContextMenu = (e: MouseEvent) => e.preventDefault();
    document.addEventListener('contextmenu', handleContextMenu);
    return () => document.removeEventListener('contextmenu', handleContextMenu);
  }, []);

  useEffect(() => {
    playSoundEffect(mascotState);
  }, [mascotState]);

  const handleVoiceChatRef = useRef<any>(null);
  useEffect(() => {
    handleVoiceChatRef.current = handleVoiceChat;
  }, [voiceState, voiceText]);

  // Synchronize events from main Tauri app
  useEffect(() => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      const unlistenState = listen('mascot-state-changed', (event: any) => {
        setMascotState(event.payload?.state || event.payload?.mascot_state || 'default');
      });
      const unlistenAmplitude = listen('mascot-amplitude-changed', (event: any) => {
        setSpeechAmplitude(event.payload?.amplitude || 0);
      });
      const unlistenStopSpeech = listen('stop-all-speech', (event: any) => {
        if (event.payload?.sender !== 'mascot') {
          generationIdRef.current++;
          if (audioRef.current) {
            audioRef.current.pause();
            audioRef.current.src = '';
            audioRef.current = null;
          }
          setVoiceState('idle');
          setVoiceText('');
        }
      });
      const unlistenUserTyping = listen('user-typing', () => {
        setMascotState('typing');
        if (typingTimeoutRef.current) clearTimeout(typingTimeoutRef.current);
        typingTimeoutRef.current = setTimeout(() => setMascotState('default'), 1200);
      });
      const unlistenAutomation = listen('automation-state-changed', (event: any) => {
        setIsAutomating(!!event.payload?.active);
        setAutomatingTool(event.payload?.tool || '');
      });
      const unlistenGlobalPtt = listen('global-push-to-talk', () => {
        handleVoiceChatRef.current?.();
      });

      return () => {
        unlistenState.then(fn => fn());
        unlistenAmplitude.then(fn => fn());
        unlistenStopSpeech.then(fn => fn());
        unlistenUserTyping.then(fn => fn());
        unlistenAutomation.then(fn => fn());
        unlistenGlobalPtt.then(fn => fn());
      };
    }
  }, []);

  // Listen to browser-wide DOM custom events for mascot reactivity (e.g. from SSE proactive nudges)
  useEffect(() => {
    const handleMascotCustomEvent = (event: any) => {
      const targetState = event.detail?.state || event.detail?.mascot_state;
      if (targetState) {
        setMascotState(targetState);
      }
    };
    const handleStartVoice = () => {
      handleVoiceChatRef.current?.();
    };

    if (typeof window !== 'undefined') {
      window.addEventListener('meridian:mascot-state-changed', handleMascotCustomEvent);
      window.addEventListener('meridian:start-voice-chat', handleStartVoice);
      return () => {
        window.removeEventListener('meridian:mascot-state-changed', handleMascotCustomEvent);
        window.removeEventListener('meridian:start-voice-chat', handleStartVoice);
      };
    }
  }, []);

  // Window size logic (Dynamic Island bounds)
  let targetWidth = 180;
  let targetHeight = 36;

  const isWorking = hudState === 'working';
  const isVoiceActive = voiceState !== 'idle';
  const isSuccessOrError = hudState === 'success' || hudState === 'error';
  const isCompactIdle = hudState === 'idle' && voiceState === 'idle' && !isExpanded;

  // Add +16px buffer to window size to accommodate p-3 (12px) transparent padding without clipping shadows
  if (isWorking) {
    targetWidth = 340 + 16;
    targetHeight = isExpanded ? 220 + 16 : 60 + 16;
  } else if (isVoiceActive || isSuccessOrError) {
    targetWidth = 340 + 16;
    targetHeight = 60 + 16;
  } else {
    targetWidth = isExpanded ? 340 + 16 : 180 + 16;
    targetHeight = isExpanded ? 60 + 16 : 36 + 16;
  }

  const resizeAndCenter = async (width: number, height: number) => {
    if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined) {
      try {
        await appWindow.setResizable(true);
        const monitor = await currentMonitor();
        if (monitor) {
          const scaleFactor = monitor.scaleFactor;
          const monitorWidth = monitor.size.width / scaleFactor;
          const monitorHeight = monitor.size.height / scaleFactor;
          const monitorX = monitor.position.x / scaleFactor;
          const monitorY = monitor.position.y / scaleFactor;

          const positionSetting = localStorage.getItem('ISLAND_POSITION') || 'bottom-right';

          let x = monitorX + monitorWidth - width - 16;
          let y = monitorY + monitorHeight - height - 60;

          if (positionSetting === 'top-center') {
            x = monitorX + (monitorWidth - width) / 2;
            y = monitorY + 16;
          } else if (positionSetting === 'bottom-center') {
            x = monitorX + (monitorWidth - width) / 2;
            y = monitorY + monitorHeight - height - 60;
          } else if (positionSetting === 'top-right') {
            x = monitorX + monitorWidth - width - 16;
            y = monitorY + 16;
          } else if (positionSetting === 'top-left') {
            x = monitorX + 16;
            y = monitorY + 16;
          } else if (positionSetting === 'bottom-left') {
            x = monitorX + 16;
            y = monitorY + monitorHeight - height - 60;
          }

          await appWindow.setSize(new LogicalSize(width, height));
          await appWindow.setPosition(new LogicalPosition(x, y));
        } else {
          await appWindow.setSize(new LogicalSize(width, height));
        }
        await appWindow.setResizable(false);
      } catch (err) {
        console.error("Failed resizing Tauri window:", err);
      }
    }
  };

  useEffect(() => {
    resizeAndCenter(targetWidth, targetHeight);
  }, [targetWidth, targetHeight]);

  useEffect(() => {
    const handlePosChange = () => resizeAndCenter(targetWidth, targetHeight);
    window.addEventListener('meridian-island-position-changed', handlePosChange);
    return () => window.removeEventListener('meridian-island-position-changed', handlePosChange);
  }, [targetWidth, targetHeight]);

  // Sync theme
  useEffect(() => {
    const updateTheme = () => {
      try {
        const saved = resolveTheme(localStorage.getItem('theme'));
        setTheme(saved);
        applyThemeToDocument(saved);
        document.body.classList.add('mascot-body');
      } catch (e) {
        console.error("Theme reading error:", e);
      }
    };
    updateTheme();
    const interval = setInterval(updateTheme, 2000);
    return () => clearInterval(interval);
  }, []);

  // Listen to status updates
  useEffect(() => {
    let unlistenStatus: Promise<any> | undefined;
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenStatus = listen('agent-status-update', (event: any) => {
        const payload = event.payload;
        const eventTimestamp = payload.timestamp || 0;
        if (eventTimestamp && eventTimestamp < lastEventTimestampRef.current) {
          console.warn("[Mascot] Ignored out-of-order agent-status-update event");
          return;
        }
        if (eventTimestamp) {
          lastEventTimestampRef.current = eventTimestamp;
        }

        setIsRunning(payload.isRunning);
        if (payload.latestThought) setLatestThought(payload.latestThought);
        if (payload.thoughts) setRecentThoughts(payload.thoughts);

        if (payload.isRunning) {
          if (successTimeoutRef.current) clearTimeout(successTimeoutRef.current);
          setHudState('working');
        } else {
          const lastType = payload.latestThought?.type;
          const lastStatus = payload.latestThought?.status;
          if (lastType === 'warning' || lastType === 'error' || lastStatus === 'failed') {
            setHudState('error');
          } else {
            setHudState('success');
            successTimeoutRef.current = setTimeout(() => setHudState('idle'), 4000);
          }
        }
      });
    }
    return () => {
      if (unlistenStatus) unlistenStatus.then(fn => fn());
      if (successTimeoutRef.current) clearTimeout(successTimeoutRef.current);
    };
  }, []);

  const handleOpenDashboard = async () => {
    if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined) {
      try {
        await invoke('show_main_window');
      } catch (err) {
        console.error("Failed triggering main visibility:", err);
        try {
          await invoke('set_mascot_visible', { visible: false });
        } catch (e) {}
      }
    }
  };

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.altKey && e.key.toLowerCase() === 'm') {
        e.preventDefault();
        handleOpenDashboard();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  // Voice recording & query processing
  async function handleVoiceChat() {
    handleVoiceChatRef.current = handleVoiceChat;
    const currentGen = ++generationIdRef.current;

    if (abortControllerRef.current) {
      abortControllerRef.current.abort();
      abortControllerRef.current = null;
    }
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.src = '';
      audioRef.current = null;
    }

    if (voiceState !== 'idle') {
      setVoiceState('idle');
      setVoiceText('');
      return;
    }

    setVoiceState('listening');
    setVoiceText('');

    if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined) {
      emit('stop-all-speech', { sender: 'mascot' }).catch(() => {});
    }

    const controller = new AbortController();
    abortControllerRef.current = controller;

    let unsubAudio: (() => void) | null = null;

    try {
      let transcription = '';
      const SpeechRecognition = typeof window !== 'undefined' && ((window as any).SpeechRecognition || (window as any).webkitSpeechRecognition);
      const useWebSpeech = SpeechRecognition && localStorage.getItem('meridian_stt_engine') !== 'backend';

      if (useWebSpeech) {
        try {
          transcription = await new Promise<string>((resolve, reject) => {
            const recognition = new SpeechRecognition();
            recognition.continuous = false;
            recognition.interimResults = true;
            recognition.lang = localStorage.getItem('meridian_stt_lang') || 'en-US';

            let interimTranscript = '';
            controller.signal.addEventListener('abort', () => {
              try { recognition.abort(); } catch {}
              reject(new DOMException('Aborted', 'AbortError'));
            });

            recognition.onresult = (event: any) => {
              let textAccum = '';
              for (let i = 0; i < event.results.length; ++i) {
                textAccum += event.results[i][0].transcript;
              }
              interimTranscript = textAccum.trim();
              if (interimTranscript) setVoiceText(interimTranscript);
            };

            recognition.onerror = (e: any) => {
              if (e.error === 'no-speech') resolve('');
              else reject(new Error(e.error));
            };

            recognition.onend = () => {
              resolve(interimTranscript);
            };

            recognition.start();
          });
        } catch (err: any) {
          if (err.name === 'AbortError') return;
        }
      }

      if (!transcription.trim()) {
        const recRes = await fetch(`${API_BASE_URL}/api/voice/record`, { method: 'POST', signal: controller.signal });
        if (!recRes.ok) throw new Error("Voice recording failed");

        setVoiceState('transcribing');
        const recData = await recRes.json();
        transcription = recData.text || '';
      }

      if (!transcription.trim() || transcription.startsWith("Error:") || transcription.startsWith("Recording and transcription failed") || transcription === "No audio captured.") {
        throw new Error("No clear voice command detected.");
      }

      setVoiceText(transcription);
      setVoiceLogs(prev => [...prev.slice(-3), transcription]);
      setVoiceState('thinking');

      const provider = localStorage.getItem('MERIDIAN_PROVIDER') || localStorage.getItem('meridian_provider') || 'ollama';
      const brainModel = localStorage.getItem('MERIDIAN_MODEL') || localStorage.getItem('meridian_model') || '';
      const configuredSource = localStorage.getItem('meridian_model_source') || localStorage.getItem('MERIDIAN_MODEL_SOURCE');
      const modelSource = configuredSource || (provider === 'ollama' ? 'local' : 'cloud');

      const openaiKey = localStorage.getItem('OPENAI_API_KEY') || '';
      const anthropicKey = localStorage.getItem('ANTHROPIC_API_KEY') || '';
      const geminiKey = localStorage.getItem('GEMINI_API_KEY') || '';
      const deepseekKey = localStorage.getItem('DEEPSEEK_API_KEY') || '';

      // Chat stream request
      const chatRes = await fetch(`${API_BASE_URL}/api/chat/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: transcription,
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
      if (!chatRes.ok) throw new Error("Chat process failed");

      const reader = chatRes.body?.getReader();
      if (!reader) throw new Error("Non-readable stream returned");

      const decoder = new TextDecoder("utf-8");
      let buffer = "";
      let readerDone = false;
      let accumulatedText = "";
      streamingAudio.resetSession();
      unsubAudio = streamingAudio.subscribeState(s => {
        if (s === 'speaking') {
          setVoiceState('speaking');
        } else if (s === 'idle' && readerDone) {
          setVoiceState('idle');
          setVoiceText('');
        }
      });

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          readerDone = true;
          break;
        }
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
              if (line.startsWith("event: ")) event = line.slice(7).trim();
              else if (line.startsWith("data: ")) dataParts.push(line.slice(6));
            }
            const data = dataParts.join('\n');

            if (event === "text" && data) {
              const trimmed = data.trim();
              if (trimmed.startsWith('{')) {
                try {
                  const parsed = JSON.parse(trimmed);
                  const finalMsg = parsed.speech || parsed.chat || "";
                  if (finalMsg) {
                    accumulatedText = finalMsg;
                    setVoiceText(accumulatedText);
                    streamingAudio.dispatchImmediateText(finalMsg, currentGen);
                    continue;
                  }
                } catch { /* not valid JSON, proceed normally */ }
              }

              accumulatedText += data;
              setVoiceText(accumulatedText);
              streamingAudio.feedText(data, currentGen);
            }
          }
          boundary = buffer.indexOf('\n\n');
        }
      }

      readerDone = true;
      streamingAudio.flush(currentGen);
    } catch (err: any) {
      if (err.name === 'AbortError') return;
      setVoiceState('idle');
      setVoiceText(`Command input error`);
      setTimeout(() => setVoiceText(''), 3000);
    } finally {
      unsubAudio?.();
      abortControllerRef.current = null;
    }
  }

  const handleCancelTask = () => {
    emit('cancel-agent-execution', {});
    setHudState('idle');
    setIsRunning(false);
  };

  // Determine state-specific glow/styling on the island
  const getIslandBorder = () => {
    if (voiceState === 'listening') return '1px solid var(--danger)';
    if (voiceState === 'transcribing' || voiceState === 'thinking' || hudState === 'working') return '1px solid var(--warning)';
    if (voiceState === 'speaking' || hudState === 'success') return '1px solid var(--success)';
    if (hudState === 'error') return '1px solid var(--danger)';
    return `1px solid ${colors.accent}20`;
  };

  const getIslandShadow = () => {
    // Soften and tighten shadows so they fit inside transparent boundaries and don't create sharp clipping borders
    if (voiceState === 'listening') return '0 4px 10px rgba(239, 68, 68, 0.25)';
    if (voiceState === 'transcribing' || voiceState === 'thinking' || hudState === 'working') return '0 4px 10px rgba(245, 158, 11, 0.25)';
    if (voiceState === 'speaking' || hudState === 'success') return '0 4px 10px rgba(16, 185, 129, 0.25)';
    if (hudState === 'error') return '0 4px 10px rgba(239, 68, 68, 0.25)';
    return '0 4px 12px rgba(0, 0, 0, 0.35)';
  };


  const displayStatusText = voiceState === 'listening'
    ? 'Listening...'
    : voiceState === 'transcribing'
    ? 'Transcribing...'
    : voiceState === 'thinking'
    ? 'Thinking...'
    : voiceState === 'speaking'
    ? (voiceText || 'Speaking...')
    : voiceText
    ? voiceText
    : hudState === 'working'
    ? (latestThought?.tool ? `Using ${latestThought.tool}...` : latestThought?.text || 'Executing task...')
    : hudState === 'success'
    ? 'Goal achieved!'
    : hudState === 'error'
    ? 'Task failed'
    : 'System Standby';

  return (
    <div 
      className="w-screen h-screen relative select-none bg-transparent flex flex-col justify-start p-3 font-sans"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      {isAutomating && (
        <div className="absolute top-1.5 right-12 z-50 pointer-events-none">
          <span className="text-[8px] font-bold text-[var(--warning)] uppercase tracking-widest bg-[var(--bg-panel)] px-1.5 py-0.5 rounded border border-[var(--border-subtle)]">
            AUTO: {automatingTool}
          </span>
        </div>
      )}

      <motion.div
        layout
        className={`w-full h-full border flex flex-col transition-all duration-300 relative ${isCompactIdle ? 'p-1' : 'p-2'}`}
        style={{
          border: getIslandBorder(),
          backgroundColor: 'var(--bg-panel)',
          boxShadow: getIslandShadow(),
          borderRadius: isCompactIdle ? '9999px' : 'var(--radius-md)'
        }}
      >
        {isCompactIdle ? (
          /* Sleek Minimal Dynamic Island Pill */
          <div 
            data-tauri-drag-region 
            className="flex items-center justify-center gap-2 w-full h-full cursor-grab active:cursor-grabbing px-3"
          >
            <MascotCharacter state={mascotState} accentColor={colors.accent} speechAmplitude={speechAmplitude} themeMode={mascotThemeMode(theme)} />
            <span className="text-[10px] font-bold text-[var(--text-main)] tracking-wider uppercase truncate" data-tauri-drag-region>
              MERIDIAN
            </span>
          </div>
        ) : (
          /* Full HUD / Expanded Panel View */
          <>
            {/* Core Pill Layout (Header) */}
            <div 
              data-tauri-drag-region 
              className="flex items-center justify-between w-full h-8 cursor-grab active:cursor-grabbing"
            >
              <div className="flex items-center gap-2 flex-1 min-w-0" data-tauri-drag-region>
                <MascotCharacter state={hudState === 'working' ? 'diagnostic' : mascotState} accentColor={colors.accent} speechAmplitude={speechAmplitude} themeMode={mascotThemeMode(theme)} />


                {voiceState === 'listening' || voiceState === 'speaking' ? (
                  <div className="flex items-center gap-1.5 h-6 px-1 flex-1 justify-center overflow-hidden">
                    <svg className="w-24 h-6 overflow-visible" viewBox="0 0 100 24" fill="none" style={{ color: colors.accent }}>
                      <motion.path
                        d="M0 12 Q25 2, 50 12 T100 12"
                        stroke="currentColor"
                        strokeWidth="1.5"
                        animate={{ d: ["M0 12 Q25 2, 50 12 T100 12", "M0 12 Q25 22, 50 12 T100 12", "M0 12 Q25 2, 50 12 T100 12"] }}
                        transition={{ duration: 1.2, repeat: Infinity, ease: "easeInOut" }}
                      />
                      <motion.path
                        d="M0 12 Q25 22, 50 12 T100 12"
                        stroke="currentColor"
                        strokeWidth="1"
                        opacity="0.4"
                        animate={{ d: ["M0 12 Q25 22, 50 12 T100 12", "M0 12 Q25 2, 50 12 T100 12", "M0 12 Q25 22, 50 12 T100 12"] }}
                        transition={{ duration: 0.9, repeat: Infinity, ease: "easeInOut" }}
                      />
                    </svg>
                  </div>
                ) : (
                  <div className="flex flex-col flex-1 min-w-0" data-tauri-drag-region>
                    <span className="text-[8px] uppercase font-bold tracking-wider text-[var(--text-ghost)]" data-tauri-drag-region>
                      {voiceState !== 'idle' ? 'Voice Chat' : hudState === 'working' ? 'Agent Active' : hudState === 'success' ? 'Task Completed' : hudState === 'error' ? 'Task Alert' : 'System State'}
                    </span>
                    <span className="text-[10px] font-semibold text-[var(--text-bright)] truncate pr-2" data-tauri-drag-region>
                      {displayStatusText}
                    </span>
                  </div>
                )}
              </div>

              {/* Actions */}
              <div className="flex items-center gap-1.5 flex-shrink-0 z-20">
                <button
                  onClick={handleOpenDashboard}
                  title="Open Dashboard"
                  className="w-6 h-6 rounded-full bg-[var(--bg-panel)] border border-[var(--border-subtle)] hover:border-[var(--border-active)] hover:bg-[var(--bg-hover)] text-[var(--text-dim)] hover:text-[var(--text-bright)] flex items-center justify-center transition-all duration-200 cursor-pointer"
                >
                  <LogIn className="w-3 h-3" />
                </button>


                {hudState === 'working' ? (
                  <button
                    onClick={handleCancelTask}
                    title="Cancel Task"
                    className="w-6 h-6 rounded-full bg-[color-mix(in_srgb,var(--danger)_12%,transparent)] border border-[var(--danger)] text-[var(--danger)] flex items-center justify-center transition-all duration-200 cursor-pointer"
                  >
                    <X className="w-3 h-3" />
                  </button>
                ) : (
                  <button
                    onClick={handleVoiceChat}
                    title={
                      voiceState === 'listening' ? 'Stop Listening' :
                      voiceState === 'speaking' ? 'Stop Speaking' : 'Voice Chat'
                    }
                    className={`w-6 h-6 rounded-full border flex items-center justify-center transition-all duration-200 cursor-pointer ${
                      voiceState === 'listening' ? 'bg-red-950/40 border-red-800/40 hover:bg-red-900/50 hover:border-red-700' :
                      voiceState === 'speaking' ? 'bg-teal-950/40 border-teal-800/40 hover:bg-teal-900/50 hover:border-teal-700' :
                      'bg-[var(--bg-panel)] border-[var(--border-subtle)] hover:border-[var(--border-active)] hover:bg-[var(--bg-hover)]'
                    }`}
                  >
                    {voiceState === 'listening' ? (
                      <MicOff className="w-3 h-3 text-red-400 animate-pulse" />
                    ) : voiceState === 'speaking' ? (
                      <Volume2 className="w-3 h-3 text-[var(--accent)] animate-pulse" />
                    ) : voiceState === 'transcribing' || voiceState === 'thinking' ? (
                      <Loader2 className="w-3 h-3 text-[var(--warning)] animate-spin" />
                    ) : (
                      <Mic className="w-3 h-3 text-[var(--text-dim)] hover:text-[var(--text-bright)]" />
                    )}
                  </button>
                )}
              </div>
            </div>


            {/* Step Tickers and History logs */}
            <AnimatePresence>
              {isExpanded && (
                <motion.div 
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: 'auto' }}
                  exit={{ opacity: 0, height: 0 }}
                  transition={{ duration: 0.2 }}
                  className="flex-1 mt-1.5 border-t border-[var(--border-subtle)] pt-1.5 flex flex-col justify-between overflow-hidden"
                >
                  {hudState === 'working' && (
                    <div className="flex-1 flex flex-col min-h-0">
                      <span className="text-[8px] font-bold text-[var(--text-ghost)] uppercase tracking-wide mb-1 flex items-center gap-1">
                        <Loader2 className="w-2.5 h-2.5 animate-spin text-[var(--warning)]" />
                        <span>Live Step Ticker</span>
                      </span>
                      <div className="flex-1 overflow-y-auto max-h-[50px] font-mono text-[9px] text-[var(--text-dim)] space-y-1 pr-1 select-text scrollbar-thin">
                        {recentThoughts.length === 0 ? (
                          <div className="text-[var(--text-ghost)] italic">Initializing agent...</div>
                        ) : (
                          recentThoughts.map((thought, idx) => {
                            const isStr = typeof thought === 'string';
                            const text = isStr ? thought : (thought?.text || '');
                            const tool = isStr ? null : thought?.tool;
                            const id = isStr ? idx : (thought?.id || idx);
                            return (
                              <div key={id} className="flex gap-1.5 items-start leading-tight">
                                <span className="text-[var(--warning)] flex-shrink-0">❯</span>
                                <div className="flex-1 truncate">
                                  {tool && <span className="text-[var(--text-ghost)] font-bold mr-1">[{tool}]</span>}
                                  <span className="text-[var(--text-main)]">{text}</span>
                                </div>
                              </div>
                            );
                          })
                        )}
                      </div>
                    </div>
                  )}

                  <div className="flex-1 flex flex-col min-h-0 border-t border-[var(--border-subtle)] pt-1 mt-1">
                    <span className="text-[8px] font-bold text-[var(--text-ghost)] uppercase tracking-wide mb-1 flex items-center gap-1">
                      <Mic className="w-2.5 h-2.5 text-[var(--accent)]" />
                      <span>Voice Command History</span>
                    </span>
                    <div className="max-h-[40px] overflow-y-auto font-mono text-[9px] text-[var(--text-dim)] space-y-1 pr-1 select-text scrollbar-thin">
                      {voiceLogs.length === 0 ? (
                        <div className="text-[var(--text-ghost)] italic">No voice sessions.</div>
                      ) : (
                        voiceLogs.map((logStr, idx) => (
                          <div key={idx} className="flex gap-1.5 items-start leading-tight">
                            <span className="text-[var(--text-ghost)]">{idx + 1}.</span>
                            <span className="text-[var(--text-main)]">{logStr}</span>
                          </div>
                        ))
                      )}
                    </div>
                  </div>
                </motion.div>
              )}
            </AnimatePresence>
          </>
        )}
      </motion.div>
    </div>
  );
}
