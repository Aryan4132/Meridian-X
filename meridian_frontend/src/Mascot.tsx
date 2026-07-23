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

const THEME_COLORS: Record<string, { accent: string; bg: string; border: string }> = {
  void:          { accent: '#00E5FF', bg: '#0A0D17', border: 'rgba(0, 229, 255, 0.15)' },
  frost:         { accent: '#60A5FA', bg: '#050A14', border: 'rgba(96, 165, 250, 0.15)' },
  'tokyo-storm': { accent: '#7AA2F7', bg: '#131421', border: 'rgba(122, 162, 247, 0.15)' },
  abyss:         { accent: '#00A896', bg: '#00212B', border: 'rgba(0, 168, 150, 0.15)' },
  carbon:        { accent: '#E2E8F0', bg: '#0E0E10', border: 'rgba(226, 232, 240, 0.15)' },
  noir:          { accent: '#38BDF8', bg: '#000000', border: 'rgba(56, 189, 248, 0.15)' },
};

type HudState = 'idle' | 'working' | 'success' | 'error';

interface MascotCharacterProps {
  state: string;
  accentColor: string;
  speechAmplitude?: number;
}

export function MascotCharacter({ state, accentColor, speechAmplitude = 0 }: MascotCharacterProps) {
  // Body float animation
  const floatVariants = {
    default: {
      y: [0, -2.5, 0],
      transition: { duration: 3, repeat: Infinity, ease: "easeInOut" }
    },
    happy: {
      y: [0, -4.5, 0],
      scaleY: [1, 0.94, 1.06, 1],
      transition: { duration: 1.4, repeat: Infinity, ease: "easeInOut" }
    },
    sleeping: {
      y: [0, -1.2, 0],
      scaleY: [1, 0.96, 1],
      transition: { duration: 4.5, repeat: Infinity, ease: "easeInOut" }
    },
    tired: {
      y: [1, 2.5, 1],
      rotate: [0.3, -0.3, 0.3],
      transition: { duration: 4.2, repeat: Infinity, ease: "easeInOut" }
    },
    diagnostic: {
      y: [0, -1.8, 0],
      rotate: [0, 3, -3, 0],
      transition: { duration: 3.2, repeat: Infinity, ease: "easeInOut" }
    },
    disapproving: {
      x: [0, -0.8, 0.8, -0.8, 0.8, 0],
      transition: { duration: 0.6, repeat: Infinity, ease: "linear" }
    },
    typing: {
      y: [0, -1.5, 0],
      rotate: [0, -2, 2, 0],
      transition: { duration: 0.75, repeat: Infinity, ease: "easeInOut" }
    }
  };

  const currentVariant = floatVariants[state as keyof typeof floatVariants] ? state : 'default';

  // Determine state-specific coloring
  const stateColor = 
    state === 'sleeping' ? '#818cf8' : 
    state === 'tired' ? '#22d3ee' : 
    state === 'disapproving' ? '#f43f5e' : 
    state === 'diagnostic' ? '#f59e0b' : 
    state === 'typing' ? '#10b981' : 
    state === 'happy' ? '#3b82f6' : 
    accentColor;

  // Sizing central core based on speech amplitude
  const coreRadius = Math.min(8.0, 4.5 + speechAmplitude * 6.5);

  return (
    <div className="relative w-8 h-8 flex-shrink-0 flex items-center justify-center">
      {/* State-specific background glow */}
      <span className={`absolute w-7 h-7 rounded-full opacity-30 blur-[8px] transition-colors duration-500 ${
        state === 'sleeping' ? 'bg-indigo-500' :
        state === 'tired' ? 'bg-cyan-500' :
        state === 'disapproving' ? 'bg-rose-500' :
        state === 'diagnostic' ? 'bg-amber-500' : 
        state === 'typing' ? 'bg-emerald-400' : 'bg-cyan-400'
      }`} />

      <motion.div
        variants={floatVariants}
        animate={currentVariant}
        className="w-full h-full flex items-center justify-center relative z-10"
      >
        <svg viewBox="0 0 32 32" className="w-full h-full overflow-visible" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <radialGradient id="core-glow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stopColor={stateColor} />
              <stop offset="40%" stopColor={stateColor} stopOpacity="0.6" />
              <stop offset="100%" stopColor={stateColor} stopOpacity="0" />
            </radialGradient>
            <linearGradient id="yellow-hat" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%" stopColor="#fbbf24" />
              <stop offset="100%" stopColor="#d97706" />
            </linearGradient>
            <filter id="glow-visor-filter" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="1" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Inner ring (Motion) */}
          <motion.ellipse 
            cx="16" 
            cy="16" 
            rx="8.5" 
            ry="3.5" 
            stroke={stateColor} 
            strokeWidth={state === 'diagnostic' ? 1.5 : 1} 
            strokeDasharray={state === 'diagnostic' ? "2 2" : undefined}
            fill="none" 
            animate={{ rotate: [45, 45 + 360] }}
            transition={{
              duration: state === 'sleeping' ? 22 : state === 'tired' ? 15 : state === 'typing' ? 1.4 : state === 'diagnostic' ? 2.5 : 6,
              repeat: Infinity,
              ease: "linear"
            }}
            style={{ transformOrigin: '16px 16px' }}
          />

          {/* Middle ring (Motion) */}
          <motion.ellipse 
            cx="16" 
            cy="16" 
            rx="11.5" 
            ry="4.5" 
            stroke={stateColor} 
            strokeWidth={state === 'diagnostic' ? 1.5 : 1} 
            strokeDasharray={state === 'diagnostic' ? "3 1.5" : undefined}
            fill="none" 
            animate={{ rotate: [-45, -45 - 360] }}
            transition={{
              duration: state === 'sleeping' ? 18 : state === 'tired' ? 12 : state === 'typing' ? 1.1 : state === 'diagnostic' ? 2.0 : 5,
              repeat: Infinity,
              ease: "linear"
            }}
            style={{ transformOrigin: '16px 16px' }}
          />

          {/* Outer ring (Motion) */}
          {state === 'diagnostic' ? (
            <motion.polygon 
              points="16,2.5 27.5,9.2 27.5,22.8 16,29.5 4.5,22.8 4.5,9.2"
              stroke={stateColor} 
              strokeWidth="1.5"
              strokeDasharray="4 2"
              fill="none"
              animate={{ rotate: [0, 360] }}
              transition={{
                duration: state === 'diagnostic' ? 3.5 : 8,
                repeat: Infinity,
                ease: "linear"
              }}
              style={{ transformOrigin: '16px 16px' }}
            />
          ) : (
            <motion.ellipse 
              cx="16" 
              cy="16" 
              rx="14.5" 
              ry="5.5" 
              stroke={stateColor} 
              strokeWidth={state === 'typing' ? 1.5 : 1} 
              fill="none" 
              animate={{ rotate: [15, 15 + 360] }}
              transition={{
                duration: state === 'sleeping' ? 14 : state === 'tired' ? 10 : state === 'typing' ? 0.8 : 4,
                repeat: Infinity,
                ease: "linear"
              }}
              style={{ transformOrigin: '16px 16px' }}
            />
          )}

          {/* Core Glow (Motion) */}
          <motion.circle 
            cx="16" 
            cy="16" 
            r={coreRadius + 2.5} 
            fill="url(#core-glow)" 
            className="pointer-events-none" 
            animate={state === 'diagnostic' ? { scale: [0.92, 1.1, 0.92], opacity: [0.4, 0.75, 0.4] } : { scale: [0.95, 1.05, 0.95], opacity: [0.35, 0.5, 0.35] }}
            transition={{ duration: state === 'diagnostic' ? 0.8 : 2.5, repeat: Infinity, ease: "easeInOut" }}
            style={{ transformOrigin: '16px 16px' }}
          />

          {/* Actual Core (Motion) */}
          <motion.circle 
            cx="16" 
            cy="16" 
            r={coreRadius} 
            fill={stateColor} 
            stroke="#0f172a" 
            strokeWidth="1" 
            animate={state === 'diagnostic' ? { scale: [1, 1.12, 1] } : { scale: [1, 1.06, 1] }}
            transition={{ duration: state === 'diagnostic' ? 0.8 : 1.8, repeat: Infinity, ease: "easeInOut" }}
            style={{ transformOrigin: '16px 16px' }}
          />

        </svg>
      </motion.div>

      {/* Floating particles */}
      {state === 'sleeping' && (
        <div className="absolute inset-0 pointer-events-none">
          {[[9, 0], [12, 0.8], [15, 1.6]].map(([yShift, delay]) => (
            <motion.span
              key={delay}
              className="absolute text-[8px] font-bold text-indigo-400 select-none"
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

const playSoundEffect = (state: string) => {
  if (localStorage.getItem('meridian_mascot_audio_fx') === 'false') return;

  try {
    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
    if (!AudioContextClass) return;

    const volume = parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5');
    const ctx = new AudioContextClass();
    
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

const API_BASE_URL = 'http://127.0.0.1:4132';

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
  const [theme, setTheme] = useState<string>('void');
  const [voiceState, setVoiceState] = useState<'idle' | 'listening' | 'transcribing' | 'thinking' | 'speaking'>('idle');
  const [voiceText, setVoiceText] = useState<string>('');
  const [isAutomating, setIsAutomating] = useState(false);
  const [automatingTool, setAutomatingTool] = useState('');
  
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);
  const successTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const typingTimeoutRef = useRef<NodeJS.Timeout | null>(null);
  const lastEventTimestampRef = useRef<number>(0);
  const appWindow = getCurrentWindow();
  const colors = THEME_COLORS[theme] || THEME_COLORS.void;

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
        if (event.payload?.sender !== 'mascot' && audioRef.current) {
          audioRef.current.pause();
          audioRef.current = null;
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
        const saved = localStorage.getItem('theme') || 'void';
        if (THEME_COLORS[saved]) setTheme(saved);
        document.body.className = `theme-${saved} mascot-body`;
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
        await invoke('set_mascot_visible', { visible: false });
      } catch (err) {
        console.error("Failed triggering main visibility:", err);
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
    if (voiceState !== 'idle') {
      if (abortControllerRef.current) {
        abortControllerRef.current.abort();
        abortControllerRef.current = null;
      }
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current = null;
      }
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

    try {
      const recRes = await fetch(`${API_BASE_URL}/api/voice/record`, { method: 'POST', signal: controller.signal });
      if (!recRes.ok) throw new Error("Voice recording failed");

      setVoiceState('transcribing');
      const recData = await recRes.json();
      const transcription = recData.text || '';
      if (!transcription.trim() || transcription.startsWith("Error:") || transcription.startsWith("Recording and transcription failed")) {
        throw new Error("No clear voice command detected.");
      }

      setVoiceText(transcription);
      setVoiceLogs(prev => [...prev.slice(-3), transcription]);
      setVoiceState('thinking');

      const provider = localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama';
      const brainModel = localStorage.getItem('MERIDIAN_MODEL') || '';
      const modelSource = provider === 'ollama' ? 'local' : 'api';
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
      const audioQueue: string[] = [];
      let isPlayingAudio = false;
      let readerDone = false;
      let accumulatedText = "";
      let textBuffer = "";

      const playNextAudio = async () => {
        if (audioQueue.length === 0) {
          if (readerDone) {
            setVoiceState('idle');
            setVoiceText('');
          }
          return;
        }

        isPlayingAudio = true;
        setVoiceState('speaking');

        const nextUrl = audioQueue.shift()!;
        const audio = new Audio(nextUrl);
        audio.volume = parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5');
        audioRef.current = audio;

        audio.onended = () => {
          URL.revokeObjectURL(nextUrl);
          isPlayingAudio = false;
          playNextAudio();
        };
        audio.onerror = () => {
          URL.revokeObjectURL(nextUrl);
          isPlayingAudio = false;
          playNextAudio();
        };

        try {
          await audio.play();
        } catch {
          isPlayingAudio = false;
          playNextAudio();
        }
      };

      const fetchTTSForSentence = async (sentence: string) => {
        const cleanText = sentence.replace(/<[^>]*>/g, '').trim();
        if (!cleanText) return;
        try {
          const voice = localStorage.getItem('meridian_tts_voice') || 'M1';
          const ttsRes = await fetch(`${API_BASE_URL}/api/tts`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: cleanText, voice, lang: 'na' }),
            signal: controller.signal,
          });
          if (ttsRes.ok) {
            const blob = await ttsRes.blob();
            const url = URL.createObjectURL(blob);
            audioQueue.push(url);
            if (!isPlayingAudio) playNextAudio();
          }
        } catch { /* noop */ }
      };

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
              accumulatedText += data;
              textBuffer += data;
              setVoiceText(accumulatedText);

              const sentenceMatch = textBuffer.match(/^([^.!?\n]*[.!?\n])\s*(.*)$/s);
              if (sentenceMatch) {
                const sentence = sentenceMatch[1].trim();
                textBuffer = sentenceMatch[2];
                if (sentence) fetchTTSForSentence(sentence);
              }
            }
          }
          boundary = buffer.indexOf('\n\n');
        }
      }

      if (textBuffer.trim()) await fetchTTSForSentence(textBuffer.trim());
      if (audioQueue.length === 0 && !isPlayingAudio) {
        setVoiceState('idle');
        setVoiceText('');
      }
    } catch (err: any) {
      if (err.name === 'AbortError') return;
      setVoiceState('idle');
      setVoiceText(`Command input error`);
      setTimeout(() => setVoiceText(''), 3000);
    } finally {
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
          <span className="text-[8px] font-bold text-amber-500 uppercase tracking-widest bg-zinc-950/95 px-1.5 py-0.5 rounded border border-zinc-800">
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
            <MascotCharacter state={hudState === 'working' ? 'diagnostic' : mascotState} accentColor={colors.accent} speechAmplitude={speechAmplitude} />
            <span className="text-[10px] font-bold text-zinc-300 tracking-wider uppercase truncate" data-tauri-drag-region>
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
                <MascotCharacter state={hudState === 'working' ? 'diagnostic' : mascotState} accentColor={colors.accent} speechAmplitude={speechAmplitude} />

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
                    <span className="text-[8px] uppercase font-bold tracking-wider text-zinc-500" data-tauri-drag-region>
                      {voiceState !== 'idle' ? 'Voice Chat' : hudState === 'working' ? 'Agent Active' : hudState === 'success' ? 'Task Completed' : hudState === 'error' ? 'Task Alert' : 'System State'}
                    </span>
                    <span className="text-[10px] font-semibold text-zinc-100 truncate pr-2" data-tauri-drag-region>
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
                  className="w-6 h-6 rounded-full bg-zinc-950/60 border border-zinc-800 hover:border-zinc-700 hover:bg-zinc-900 text-zinc-400 hover:text-zinc-100 flex items-center justify-center transition-all duration-200 cursor-pointer"
                >
                  <LogIn className="w-3 h-3" />
                </button>


                {hudState === 'working' ? (
                  <button
                    onClick={handleCancelTask}
                    title="Cancel Task"
                    className="w-6 h-6 rounded-full bg-rose-950/40 hover:bg-rose-900/50 border border-rose-800/40 hover:border-rose-700 text-rose-400 hover:text-rose-300 flex items-center justify-center transition-all duration-200 cursor-pointer"
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
                      'bg-zinc-950/60 border-zinc-800 hover:border-zinc-700 hover:bg-zinc-900'
                    }`}
                  >
                    {voiceState === 'listening' ? (
                      <MicOff className="w-3 h-3 text-red-400 animate-pulse" />
                    ) : voiceState === 'speaking' ? (
                      <Volume2 className="w-3 h-3 text-teal-400 animate-pulse" />
                    ) : voiceState === 'transcribing' || voiceState === 'thinking' ? (
                      <Loader2 className="w-3 h-3 text-amber-400 animate-spin" />
                    ) : (
                      <Mic className="w-3 h-3 text-zinc-400 hover:text-zinc-100" />
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
                  className="flex-1 mt-1.5 border-t border-zinc-900 pt-1.5 flex flex-col justify-between overflow-hidden"
                >
                  {hudState === 'working' && (
                    <div className="flex-1 flex flex-col min-h-0">
                      <span className="text-[8px] font-bold text-zinc-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                        <Loader2 className="w-2.5 h-2.5 animate-spin text-amber-500" />
                        <span>Live Step Ticker</span>
                      </span>
                      <div className="flex-1 overflow-y-auto max-h-[50px] font-mono text-[9px] text-zinc-400 space-y-1 pr-1 select-text scrollbar-thin">
                        {recentThoughts.length === 0 ? (
                          <div className="text-zinc-600 italic">Initializing agent...</div>
                        ) : (
                          recentThoughts.map((thought, idx) => {
                            const isStr = typeof thought === 'string';
                            const text = isStr ? thought : (thought?.text || '');
                            const tool = isStr ? null : thought?.tool;
                            const id = isStr ? idx : (thought?.id || idx);
                            return (
                              <div key={id} className="flex gap-1.5 items-start leading-tight">
                                <span className="text-amber-500 flex-shrink-0">❯</span>
                                <div className="flex-1 truncate">
                                  {tool && <span className="text-zinc-500 font-bold mr-1">[{tool}]</span>}
                                  <span className="text-zinc-300">{text}</span>
                                </div>
                              </div>
                            );
                          })
                        )}
                      </div>
                    </div>
                  )}

                  <div className="flex-1 flex flex-col min-h-0 border-t border-zinc-900 pt-1 mt-1">
                    <span className="text-[8px] font-bold text-zinc-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                      <Mic className="w-2.5 h-2.5 text-cyan-400" />
                      <span>Voice Command History</span>
                    </span>
                    <div className="max-h-[40px] overflow-y-auto font-mono text-[9px] text-zinc-450 space-y-1 pr-1 select-text scrollbar-thin">
                      {voiceLogs.length === 0 ? (
                        <div className="text-zinc-700 italic">No voice sessions.</div>
                      ) : (
                        voiceLogs.map((logStr, idx) => (
                          <div key={idx} className="flex gap-1.5 items-start leading-tight">
                            <span className="text-zinc-500">{idx + 1}.</span>
                            <span className="text-zinc-300">{logStr}</span>
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
