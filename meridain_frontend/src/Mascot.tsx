import React, { useState, useEffect, useRef } from 'react';
import { getCurrentWindow, LogicalSize, LogicalPosition, currentMonitor } from '@tauri-apps/api/window';
import { WebviewWindow } from '@tauri-apps/api/webviewWindow';
import { listen, emit } from '@tauri-apps/api/event';
import { invoke } from '@tauri-apps/api/core';
import { motion, AnimatePresence } from 'motion/react';
import { 
  X, 
  Terminal, 
  Settings2, 
  Play, 
  Square, 
  LogIn, 
  EyeOff, 
  Moon, 
  Sun,
  Loader2,
  CheckCircle2,
  AlertTriangle,
  Mic,
  MicOff,
  Volume2,
  VolumeX,
  Crown,
  Wrench
} from 'lucide-react';

const THEME_COLORS: Record<string, { accent: string; bg: string; border: string }> = {
  default: { accent: '#ea580c', bg: '#09090b', border: '#27272a' },
  cyberpunk: { accent: '#ff007f', bg: '#090214', border: '#ff007f' },
  amber: { accent: '#ffb000', bg: '#0f0a00', border: '#ffb000' },
  slate: { accent: '#14b8a6', bg: '#0b1329', border: '#14b8a6' },
  nordic: { accent: '#7dd3fc', bg: '#0e131f', border: '#242f46' },
  crimson_charcoal: { accent: '#fb7185', bg: '#121214', border: '#26262b' },
  forest: { accent: '#34d399', bg: '#0a0e12', border: '#1c2633' }
};

type HudState = 'idle' | 'working' | 'success' | 'error';

interface MascotCharacterProps {
  state: string;
  accentColor: string;
  wardrobe?: string;
  speechAmplitude?: number;
}

export function MascotCharacter({ state, accentColor, wardrobe = 'none', speechAmplitude = 0 }: MascotCharacterProps) {
  // Body animation variants
  const floatVariants = {
    default: {
      y: [0, -3, 0],
      transition: { duration: 3, repeat: Infinity, ease: "easeInOut" }
    },
    happy: {
      y: [0, -5, 0],
      scaleY: [1, 0.95, 1.05, 1],
      transition: { duration: 1.5, repeat: Infinity, ease: "easeInOut" }
    },
    sleeping: {
      y: [0, -1.5, 0],
      scaleY: [1, 0.95, 1],
      transition: { duration: 4, repeat: Infinity, ease: "easeInOut" }
    },
    tired: {
      y: [1, 3, 1],
      rotate: [0.5, -0.5, 0.5],
      transition: { duration: 4, repeat: Infinity, ease: "easeInOut" }
    },
    diagnostic: {
      y: [0, -2, 0],
      rotate: [0, 4, -4, 0],
      transition: { duration: 3.5, repeat: Infinity, ease: "easeInOut" }
    },
    disapproving: {
      x: [0, -1, 1, -1, 1, 0],
      y: [0, 0, 0, 0, 0, 0],
      transition: { duration: 0.5, repeat: Infinity, ease: "linear" }
    },
    typing: {
      y: [0, -2, 0],
      rotate: [0, -3, 3, 0],
      transition: { duration: 0.8, repeat: Infinity, ease: "easeInOut" }
    }
  };

  const currentVariant = floatVariants[state as keyof typeof floatVariants] ? state : 'default';

  return (
    <div className="relative w-6.5 h-6.5 flex-shrink-0 flex items-center justify-center">
      {/* State-specific background glow */}
      <span className={`absolute w-full h-full rounded-full opacity-35 blur-[5px] transition-colors duration-500 ${
        state === 'sleeping' ? 'bg-indigo-500' :
        state === 'tired' ? 'bg-cyan-500' :
        state === 'disapproving' ? 'bg-rose-500' :
        state === 'diagnostic' ? 'bg-amber-500' : 
        state === 'typing' ? 'bg-emerald-400' : 'bg-emerald-500'
      }`} />

      <motion.div
        variants={floatVariants}
        animate={currentVariant}
        className="w-full h-full flex items-center justify-center relative z-10"
      >
        <svg viewBox="0 0 32 32" className="w-full h-full overflow-visible" fill="none" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="body-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="#27272a" />
              <stop offset="50%" stopColor="#18181b" />
              <stop offset="100%" stopColor="#09090b" />
            </linearGradient>
            <linearGradient id="screen-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#09090b" />
              <stop offset="100%" stopColor="#030303" />
            </linearGradient>
            <linearGradient id="glare-grad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor="white" stopOpacity="0.15" />
              <stop offset="35%" stopColor="white" stopOpacity="0.04" />
              <stop offset="35.1%" stopColor="white" stopOpacity="0" />
              <stop offset="100%" stopColor="white" stopOpacity="0" />
            </linearGradient>
            <linearGradient id="yellow-hat-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#fbbf24" />
              <stop offset="100%" stopColor="#b45309" />
            </linearGradient>
            <linearGradient id="detective-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#5c2c16" />
              <stop offset="100%" stopColor="#1f0a00" />
            </linearGradient>
            <linearGradient id="crown-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#fde047" />
              <stop offset="100%" stopColor="#ca8a04" />
            </linearGradient>
            <linearGradient id="hoodie-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#52525b" />
              <stop offset="100%" stopColor="#27272a" />
            </linearGradient>
            <linearGradient id="visor-grad" x1="0%" y1="0%" x2="0%" y2="100%">
              <stop offset="0%" stopColor="#ec4899" />
              <stop offset="100%" stopColor="#9d174d" />
            </linearGradient>
            <filter id="glow-visor-filter" x="-20%" y="-20%" width="140%" height="140%">
              <feGaussianBlur stdDeviation="1.5" result="blur" />
              <feComposite in="SourceGraphic" in2="blur" operator="over" />
            </filter>
          </defs>

          {/* Outer Shield / Ears (Robot Body) with Gradient */}
          <rect x="3" y="5" width="26" height="20" rx="6" fill="url(#body-grad)" stroke={accentColor} strokeWidth="1.5" />
          
          {/* Inner Screen Visor with Depth */}
          <rect x="5" y="7" width="22" height="16" rx="4" fill="url(#screen-grad)" stroke={`${accentColor}40`} strokeWidth="1" />
          
          {/* Screen Glass Glare reflection overlay */}
          <rect x="5" y="7" width="22" height="16" rx="4" fill="url(#glare-grad)" pointerEvents="none" />

          {/* Eyes rendering based on state */}
          {state === 'sleeping' ? (
            <>
              <path d="M9 14 Q11 17 13 14" stroke="#818cf8" strokeWidth="1.8" strokeLinecap="round" fill="none" />
              <path d="M19 14 Q21 17 23 14" stroke="#818cf8" strokeWidth="1.8" strokeLinecap="round" fill="none" />
            </>
          ) : state === 'tired' ? (
            <>
              <path d="M9 13 H13 M9 15 H13" stroke="#22d3ee" strokeWidth="1.8" strokeLinecap="round" />
              <path d="M19 13 H23 M19 15 H23" stroke="#22d3ee" strokeWidth="1.8" strokeLinecap="round" />
            </>
          ) : state === 'diagnostic' && wardrobe !== 'glasses' ? (
            <>
              <rect x="7" y="11" width="18" height="6" rx="1.5" fill={`${accentColor}25`} stroke={accentColor} strokeWidth="1.5" filter="url(#glow-visor-filter)" />
              <line x1="8" y1="14" x2="24" y2="14" stroke={accentColor} strokeWidth="1" strokeDasharray="2 2" />
            </>
          ) : state === 'disapproving' ? (
            <>
              <path d="M8 11 L13 13" stroke="#f43f5e" strokeWidth="1.8" strokeLinecap="round" />
              <path d="M24 11 L19 13" stroke="#f43f5e" strokeWidth="1.8" strokeLinecap="round" />
              <circle cx="10.5" cy="15" r="1.5" fill="#f43f5e" />
              <circle cx="21.5" cy="15" r="1.5" fill="#f43f5e" />
            </>
          ) : state === 'typing' ? (
            <>
              {/* Squinting focused eyes */}
              <path d="M9 14 L13 14" stroke={accentColor} strokeWidth="2" strokeLinecap="round" />
              <path d="M19 14 L23 14" stroke={accentColor} strokeWidth="2" strokeLinecap="round" />
              {/* Cute smile mouth */}
              <path d="M14 17 Q16 19 18 17" stroke={accentColor} strokeWidth="1.5" strokeLinecap="round" fill="none" />
              {/* Small typing hands below screen */}
              <circle cx="12" cy="21" r="0.8" fill={accentColor} />
              <circle cx="15" cy="22" r="0.8" fill={accentColor} />
              <circle cx="17" cy="22" r="0.8" fill={accentColor} />
              <circle cx="20" cy="21" r="0.8" fill={accentColor} />
            </>
          ) : (
            <>
              <motion.circle
                cx="11"
                cy="15"
                r="2"
                fill={accentColor}
                animate={{ scaleY: [1, 1, 0.1, 1, 1] }}
                transition={{ duration: 4, repeat: Infinity, repeatDelay: 3 }}
                filter="url(#glow-visor-filter)"
              />
              <motion.circle
                cx="21"
                cy="15"
                r="2"
                fill={accentColor}
                animate={{ scaleY: [1, 1, 0.1, 1, 1] }}
                transition={{ duration: 4, repeat: Infinity, repeatDelay: 3 }}
                filter="url(#glow-visor-filter)"
              />
              <path d={`M14 18 Q16 ${20 + speechAmplitude * 6} 18 18`} stroke={accentColor} strokeWidth="1.2" strokeLinecap="round" fill="none" />
            </>
          )}

          {/* Wardrobe Sunglasses Overlay */}
          {wardrobe === 'glasses' && (
            <>
              <rect x="6" y="11" width="9" height="5" rx="1.5" fill="rgba(244, 63, 94, 0.45)" stroke="#f43f5e" strokeWidth="1.5" />
              <rect x="17" y="11" width="9" height="5" rx="1.5" fill="rgba(244, 63, 94, 0.45)" stroke="#f43f5e" strokeWidth="1.5" />
              <line x1="15" y1="13" x2="17" y2="13" stroke="#f43f5e" strokeWidth="1.5" />
              <line x1="4" y1="12" x2="6" y2="12.5" stroke="#f43f5e" strokeWidth="1.5" />
              <line x1="28" y1="12" x2="26" y2="12.5" stroke="#f43f5e" strokeWidth="1.5" />
            </>
          )}

          {/* Wardrobe Construction Hat Overlay */}
          {wardrobe === 'construction_hat' && (
            <>
              <path d="M8 7 C8 2 24 2 24 7 Z" fill="url(#yellow-hat-grad)" stroke="#92400e" strokeWidth="1" />
              <path d="M4 7 H28" stroke="#92400e" strokeWidth="1.5" strokeLinecap="round" />
              <rect x="14" y="3" width="4" height="4" fill="#d97706" rx="0.5" />
            </>
          )}

          {/* Wardrobe Detective Hat Overlay */}
          {wardrobe === 'detective_hat' && (
            <>
              <path d="M9 7 C9 2.5 13 2 16 3 C19 2 23 2.5 23 7 Z" fill="url(#detective-grad)" stroke="#270e00" strokeWidth="1" />
              <rect x="9.5" y="5.8" width="13" height="1.2" fill="#0f172a" />
              <path d="M5 7 C10 6 22 6 27 7" stroke="#270e00" strokeWidth="1.5" strokeLinecap="round" />
            </>
          )}

          {/* Wardrobe Crown Overlay */}
          {wardrobe === 'crown' && (
            <>
              {/* Crown base */}
              <path d="M8 8 L10 4 L13 7.5 L16 2.5 L19 7.5 L22 4 L24 8 Z" fill="url(#crown-grad)" stroke="#9a3412" strokeWidth="1" />
              {/* Little circles on tips */}
              <circle cx="10" cy="4" r="0.8" fill="#fbbf24" stroke="#9a3412" strokeWidth="0.5" />
              <circle cx="16" cy="2.5" r="0.8" fill="#fbbf24" stroke="#9a3412" strokeWidth="0.5" />
              <circle cx="22" cy="4" r="0.8" fill="#fbbf24" stroke="#9a3412" strokeWidth="0.5" />
            </>
          )}

          {/* Wardrobe Developer Hoodie Overlay */}
          {wardrobe === 'dev_hoodie' && (
            <>
              {/* Hoodie background cap */}
              <path d="M 2,11 C 2,3.5 30,3.5 30,11 L 30,22 C 30,22 28,24.5 26,24.5 C 24,24.5 22,22 22,22 L 10,22 C 10,22 8,24.5 6,24.5 C 4,24.5 2,22 2,22 Z" fill="url(#hoodie-grad)" stroke="#18181b" strokeWidth="1" />
              {/* Hoodie drawstrings */}
              <line x1="13" y1="23" x2="13" y2="28" stroke="#cbd5e1" strokeWidth="1.5" strokeLinecap="round" />
              <line x1="19" y1="23" x2="19" y2="28" stroke="#cbd5e1" strokeWidth="1.5" strokeLinecap="round" />
            </>
          )}

          {/* Wardrobe Cyberpunk Visor Overlay */}
          {wardrobe === 'cyberpunk_visor' && (
            <>
              <polygon points="4,10 28,8 28,17 4,19" fill="url(#visor-grad)" stroke="#f472b6" strokeWidth="1.5" opacity="0.85" filter="url(#glow-visor-filter)" />
              <line x1="4" y1="14" x2="28" y2="12" stroke="#38bdf8" strokeWidth="1.2" />
            </>
          )}

          {/* Core glow */}
          <circle cx="16" cy="3" r="1.5" fill={
            state === 'sleeping' ? '#818cf8' :
            state === 'tired' ? '#22d3ee' :
            state === 'disapproving' ? '#f43f5e' : accentColor
          } filter="url(#glow-visor-filter)" />
          <line x1="16" y1="4.5" x2="16" y2="6" stroke="#27272a" strokeWidth="1" />
        </svg>
      </motion.div>

      {/* Floating particles/elements outside the SVG container */}
      {state === 'sleeping' && (
        <div className="absolute inset-0 pointer-events-none">
          <motion.span
            className="absolute text-[8px] font-bold text-indigo-400 select-none"
            initial={{ x: 10, y: -2, opacity: 0, scale: 0.5 }}
            animate={{ x: [10, 15, 18], y: [-2, -12, -20], opacity: [0, 1, 0], scale: [0.5, 1, 0.8] }}
            transition={{ duration: 3, repeat: Infinity, delay: 0 }}
          >
            z
          </motion.span>
          <motion.span
            className="absolute text-[10px] font-bold text-indigo-300 select-none"
            initial={{ x: 12, y: -2, opacity: 0, scale: 0.5 }}
            animate={{ x: [12, 18, 22], y: [-2, -14, -24], opacity: [0, 1, 0], scale: [0.5, 1.2, 0.9] }}
            transition={{ duration: 3, repeat: Infinity, delay: 1 }}
          >
            Z
          </motion.span>
          <motion.span
            className="absolute text-[11px] font-bold text-indigo-200 select-none"
            initial={{ x: 14, y: -2, opacity: 0, scale: 0.5 }}
            animate={{ x: [14, 21, 26], y: [-2, -16, -28], opacity: [0, 1, 0], scale: [0.5, 1.4, 1.0] }}
            transition={{ duration: 3, repeat: Infinity, delay: 2 }}
          >
            Z
          </motion.span>
        </div>
      )}

      {state === 'tired' && (
        <div className="absolute inset-0 pointer-events-none">
          <motion.svg
            className="absolute text-cyan-400"
            style={{ top: '6px', right: '-4px', width: '6px', height: '8px' }}
            viewBox="0 0 8 10"
            fill="currentColor"
            initial={{ y: -2, opacity: 0, scale: 0.5 }}
            animate={{ y: [0, 5, 8], opacity: [0, 1, 0], scale: [0.5, 1, 0.8] }}
            transition={{ duration: 2.2, repeat: Infinity, ease: "easeIn" }}
          >
            <path d="M4 0 C2 3 0 5 0 7 C0 9 2 10 4 10 C6 10 8 9 8 7 C8 5 6 3 4 0 Z" />
          </motion.svg>
        </div>
      )}

      {state === 'disapproving' && (
        <div className="absolute inset-0 pointer-events-none">
          <motion.svg
            className="absolute text-zinc-600"
            style={{ left: '-6px', top: '6px', width: '6px', height: '6px' }}
            viewBox="0 0 8 8"
            fill="currentColor"
            animate={{ x: [0, -5], y: [0, -2], opacity: [0, 0.8, 0], scale: [0.6, 1.1, 0.7] }}
            transition={{ duration: 1.2, repeat: Infinity, delay: 0 }}
          >
            <circle cx="4" cy="4" r="3" />
          </motion.svg>
          <motion.svg
            className="absolute text-zinc-600"
            style={{ right: '-6px', top: '6px', width: '6px', height: '6px' }}
            viewBox="0 0 8 8"
            fill="currentColor"
            animate={{ x: [0, 5], y: [0, -2], opacity: [0, 0.8, 0], scale: [0.6, 1.1, 0.7] }}
            transition={{ duration: 1.2, repeat: Infinity, delay: 0.6 }}
          >
            <circle cx="4" cy="4" r="3" />
          </motion.svg>
        </div>
      )}
    </div>
  );
}

const playSoundEffect = (state: string) => {
  const isAudioEnabled = localStorage.getItem('meridian_mascot_audio_fx') !== 'false';
  if (!isAudioEnabled) return;

  try {
    const AudioContextClass = window.AudioContext || (window as any).webkitAudioContext;
    if (!AudioContextClass) return;

    const volumeStr = localStorage.getItem('meridian_ui_volume');
    const volume = volumeStr !== null ? parseFloat(volumeStr) : 0.5;

    const ctx = new AudioContextClass();
    
    if (state === 'happy' || state === 'default') {
      // Happy chirp: 520Hz -> 780Hz
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(520, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(780, ctx.currentTime + 0.15);
      gain.gain.setValueAtTime(0.12 * volume, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.005 * volume, ctx.currentTime + 0.15);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.15);
    } 
    else if (state === 'sleeping') {
      // Yawn: 300Hz -> 140Hz
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'triangle';
      osc.frequency.setValueAtTime(300, ctx.currentTime);
      osc.frequency.linearRampToValueAtTime(140, ctx.currentTime + 0.6);
      gain.gain.setValueAtTime(0.08 * volume, ctx.currentTime);
      gain.gain.linearRampToValueAtTime(0.005 * volume, ctx.currentTime + 0.6);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.6);
    } 
    else if (state === 'diagnostic') {
      // Diagnostic double click
      const now = ctx.currentTime;
      [now, now + 0.08].forEach(time => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(1000, time);
        gain.gain.setValueAtTime(0.08 * volume, time);
        gain.gain.exponentialRampToValueAtTime(0.005 * volume, time + 0.03);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(time);
        osc.stop(time + 0.03);
      });
    } 
    else if (state === 'disapproving') {
      // Buzz
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(180, ctx.currentTime);
      gain.gain.setValueAtTime(0.1 * volume, ctx.currentTime);
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
  const [activeWardrobe, setActiveWardrobe] = useState<string>(() => {
    return localStorage.getItem('meridian_mascot_wardrobe') || 'auto';
  });
  const [audioEnabled, setAudioEnabled] = useState<boolean>(() => {
    return localStorage.getItem('meridian_mascot_audio_fx') !== 'false';
  });
  const [showWardrobeMenu, setShowWardrobeMenu] = useState(false);
  const [voiceLogs, setVoiceLogs] = useState<string[]>([]);

  useEffect(() => {
    if (propMascotState) {
      setMascotState(propMascotState);
    }
  }, [propMascotState]);

  useEffect(() => {
    const handleContextMenu = (e: MouseEvent) => {
      e.preventDefault();
    };
    document.addEventListener('contextmenu', handleContextMenu);
    return () => {
      document.removeEventListener('contextmenu', handleContextMenu);
    };
  }, []);

  useEffect(() => {
    playSoundEffect(mascotState);
  }, [mascotState]);

  const handleVoiceChatRef = useRef<any>(null);
  useEffect(() => {
    handleVoiceChatRef.current = handleVoiceChat;
  }, [handleVoiceChat]);

  useEffect(() => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      const unlistenState = listen('mascot-state-changed', (event: any) => {
        const state = event.payload?.state || event.payload?.mascot_state || 'default';
        setMascotState(state);
      });
      const unlistenWardrobe = listen('mascot-wardrobe-changed', (event: any) => {
        const item = event.payload?.item || 'auto';
        setActiveWardrobe(item);
      });
      const unlistenAmplitude = listen('mascot-amplitude-changed', (event: any) => {
        setSpeechAmplitude(event.payload?.amplitude || 0);
      });
      const unlistenStopSpeech = listen('stop-all-speech', (event: any) => {
        if (event.payload?.sender !== 'mascot') {
          if (audioRef.current) {
            audioRef.current.pause();
            audioRef.current = null;
          }
        }
      });
      const unlistenUserTyping = listen('user-typing', () => {
        setMascotState('typing');
        if (typingTimeoutRef.current) {
          clearTimeout(typingTimeoutRef.current);
        }
        typingTimeoutRef.current = setTimeout(() => {
          setMascotState('default');
        }, 1200);
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
        unlistenWardrobe.then(fn => fn());
        unlistenAmplitude.then(fn => fn());
        unlistenStopSpeech.then(fn => fn());
        unlistenUserTyping.then(fn => fn());
        unlistenAutomation.then(fn => fn());
        unlistenGlobalPtt.then(fn => fn());
      };
    }
  }, []);

  const [hudState, setHudState] = useState<HudState>('idle');
  const [isRunning, setIsRunning] = useState(false);
  const [latestThought, setLatestThought] = useState<any | null>(null);
  const [recentThoughts, setRecentThoughts] = useState<any[]>([]);
  const [isExpanded, setIsExpanded] = useState(false);
  
  const [theme, setTheme] = useState<string>('default');

  const [voiceState, setVoiceState] = useState<'idle' | 'listening' | 'transcribing' | 'thinking' | 'speaking'>('idle');
  const [voiceText, setVoiceText] = useState<string>('');
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const abortControllerRef = useRef<AbortController | null>(null);

  const successTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const [isAutomating, setIsAutomating] = useState(false);
  const [automatingTool, setAutomatingTool] = useState('');
  const typingTimeoutRef = useRef<NodeJS.Timeout | null>(null);

  const appWindow = getCurrentWindow() as any;
  const colors = THEME_COLORS[theme] || THEME_COLORS.default;

  // Resolve actual accessory
  let equipped = activeWardrobe;
  if (activeWardrobe === 'auto') {
    if (mascotState === 'crown') {
      equipped = 'crown';
    } else if (mascotState === 'diagnostic' || mascotState === 'tired') {
      equipped = 'construction_hat';
    } else if (mascotState === 'disapproving') {
      equipped = 'detective_hat';
    } else if (mascotState === 'happy' || voiceState === 'listening' || voiceState === 'speaking') {
      equipped = 'glasses';
    } else {
      equipped = 'none';
    }
  }

  // Target dimensions based on states
  let targetWidth = 180;
  let targetHeight = 36;

  const isWorking = hudState === 'working';
  const isVoiceActive = voiceState !== 'idle';
  const isSuccessOrError = hudState === 'success' || hudState === 'error';
  const isCompactIdle = hudState === 'idle' && voiceState === 'idle' && !isExpanded;

  if (isWorking) {
    targetWidth = 340;
    targetHeight = isExpanded ? (showWardrobeMenu ? 320 : 260) : 64;
  } else if (isVoiceActive || isSuccessOrError) {
    targetWidth = 340;
    targetHeight = 64;
  } else {
    // Idle state: thin bar if hovered, pill if not
    targetWidth = isExpanded ? 340 : 180;
    targetHeight = isExpanded ? (showWardrobeMenu ? 150 : 64) : 36;
  }

  const resizeAndCenter = async (width: number, height: number) => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      try {
        await appWindow.setResizable(true);
        const monitor = await currentMonitor();
        if (monitor) {
          const scaleFactor = monitor.scaleFactor;
          const monitorWidth = monitor.size.width / scaleFactor;
          const monitorX = monitor.position.x / scaleFactor;
          
          // Center the window on the active monitor's top edge
          const x = monitorX + (monitorWidth - width) / 2;
          const y = 12; // 12px margin from the top edge
          
          await appWindow.setSize(new LogicalSize(width, height));
          await appWindow.setPosition(new LogicalPosition(x, y));
        } else {
          await appWindow.setSize(new LogicalSize(width, height));
        }
      } catch (err: any) {
        console.error("Failed to resize and center window:", err);
      }
    }
  };

  // Sync window size & position dynamically
  useEffect(() => {
    resizeAndCenter(targetWidth, targetHeight);
  }, [targetWidth, targetHeight]);

  // Sync theme from localStorage
  useEffect(() => {
    const updateTheme = () => {
      try {
        const saved = localStorage.getItem('meridian_theme');
        if (saved && THEME_COLORS[saved]) {
          setTheme(saved);
        }
      } catch (e) {
        console.error("Failed to read theme:", e);
      }
    };
    updateTheme();
    const interval = setInterval(updateTheme, 2000);
    return () => clearInterval(interval);
  }, []);

  // Listen to Tauri events for agent updates
  useEffect(() => {
    let unlistenStatus: Promise<any> | undefined;
    let unlistenAiState: Promise<any> | undefined;

    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      unlistenStatus = listen('agent-status-update', (event: any) => {
        const payload = event.payload;
        
        setIsRunning(payload.isRunning);
        if (payload.latestThought) {
          setLatestThought(payload.latestThought);
        }
        if (payload.thoughts) {
          setRecentThoughts(payload.thoughts);
        }

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
            successTimeoutRef.current = setTimeout(() => {
              setHudState('idle');
            }, 4000);
          }
        }
      });

      unlistenAiState = listen('ai-state-changed', (event: any) => {
        const isThinking = event.payload?.isThinking;
        if (isThinking) {
          setHudState('working');
          setIsRunning(true);
        }
      });
    }

    return () => {
      if (unlistenStatus) unlistenStatus.then(fn => fn());
      if (unlistenAiState) unlistenAiState.then(fn => fn());
      if (successTimeoutRef.current) clearTimeout(successTimeoutRef.current);
    };
  }, []);

  const handleOpenDashboard = async () => {
    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      try {
        await invoke('set_mascot_visible', { visible: false });
      } catch (err) {
        console.error("Failed to show main dashboard:", err);
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

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      if (audioRef.current) {
        audioRef.current.pause();
        audioRef.current = null;
      }
    };
  }, []);

  async function handleVoiceChat() {
    if (voiceState === 'listening' || voiceState === 'transcribing' || voiceState === 'thinking' || voiceState === 'speaking') {
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

    const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
    if (isTauri) {
      emit('stop-all-speech', { sender: 'mascot' }).catch(() => {});
    }

    const controller = new AbortController();
    abortControllerRef.current = controller;

    try {
      // 1. Record & Transcribe
      const recRes = await fetch(`${API_BASE_URL}/api/voice/record`, { method: 'POST', signal: controller.signal });
      if (!recRes.ok) throw new Error("Failed to record from microphone");
      
      setVoiceState('transcribing');
      const recData = await recRes.json();
      const transcription = recData.text || "";
      if (!transcription.trim() || transcription.startsWith("Error:") || transcription.startsWith("Recording and transcription failed")) {
        throw new Error(transcription || "No speech detected.");
      }

      setVoiceText(transcription);
      setVoiceLogs(prev => [...prev.slice(-4), transcription]);
      setVoiceState('thinking');

      // Load model settings from localStorage
      let modelSettings = {
        modelSource: 'local',
        apiProvider: 'gemini',
        selectedModel: 'gemini-3.5-flash',
        brainModel: 'Llama-3.1-Instruct-v3',
        ocrModel: 'Florence-2-large'
      };
      try {
        const saved = localStorage.getItem('meridian_model_settings');
        if (saved) modelSettings = JSON.parse(saved);
      } catch (e) {}

      // 2. Query Chat LLM in a streaming way
      const chatRes = await fetch(`${API_BASE_URL}/api/chat/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          prompt: transcription,
          modelSettings
        }),
        signal: controller.signal
      });
      if (!chatRes.ok) throw new Error("Chat completion failed");
      
      const reader = chatRes.body?.getReader();
      if (!reader) throw new Error("Response body is not readable");

      const decoder = new TextDecoder("utf-8");
      let buffer = "";
      
      // Queues and players for audio chunks
      const audioQueue: string[] = [];
      let isPlayingAudio = false;
      let readerDone = false;
      let accumulatedText = "";
      let textBuffer = "";

      const playNextAudio = async () => {
        if (audioQueue.length === 0) {
          if (!readerDone) {
            // Keep waiting for more incoming chunks
            return;
          }
          // Completed reading and playing all chunks
          setVoiceState('idle');
          setVoiceText('');
          return;
        }

        // Stop all speech cross-window
        const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
        if (isTauri) {
          emit('stop-all-speech', { sender: 'mascot' }).catch(() => {});
        }

        isPlayingAudio = true;
        setVoiceState('speaking');

        const nextUrl = audioQueue.shift()!;
        const audio = new Audio(nextUrl);
        const volumeStr = localStorage.getItem('meridian_ui_volume');
        audio.volume = volumeStr !== null ? parseFloat(volumeStr) : 0.5;
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
        } catch (e) {
          console.error("Audio playback error:", e);
          isPlayingAudio = false;
          playNextAudio();
        }
      };

      const fetchTTSForSentence = async (sentence: string) => {
        const cleanText = sentence.replace(/<[^>]*>/g, '').trim();
        if (!cleanText) return;

        try {
          const savedVoice = localStorage.getItem('meridian_tts_voice') || 'M1';
          const ttsRes = await fetch(`${API_BASE_URL}/api/tts`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              text: cleanText,
              voice: savedVoice,
              lang: 'na'
            }),
            signal: controller.signal
          });
          if (ttsRes.ok) {
            const blob = await ttsRes.blob();
            const url = URL.createObjectURL(blob);
            audioQueue.push(url);
            if (!isPlayingAudio) {
              playNextAudio();
            }
          }
        } catch (e) {
          console.warn("Failed to fetch TTS for chunk:", e);
        }
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

            if (event === "text" && data) {
              accumulatedText += data;
              textBuffer += data;
              setVoiceText(accumulatedText);

              // Check for punctuation boundary (. ! ? \n) to trigger chunk synthesis
              const sentenceMatch = textBuffer.match(/^([^.!?\n]*[.!?\n])\s*(.*)$/s);
              if (sentenceMatch) {
                const sentence = sentenceMatch[1].trim();
                textBuffer = sentenceMatch[2];
                if (sentence) {
                  fetchTTSForSentence(sentence);
                }
              }
            } else if (event === "thought" && data) {
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
              } catch (e) {}
            }
          }
          boundary = buffer.indexOf('\n\n');
        }
      }

      // Final remaining text in buffer
      if (textBuffer.trim()) {
        await fetchTTSForSentence(textBuffer.trim());
      }
      
      // If we finished reading but nothing ever played or got queued, reset state
      if (audioQueue.length === 0 && !isPlayingAudio) {
        setVoiceState('idle');
        setVoiceText('');
      }

    } catch (err: any) {
      if (err.name === 'AbortError') {
        console.log("Voice stream fetch aborted successfully.");
        return;
      }
      console.error("Voice I/O error:", err);
      setVoiceState('idle');
      setVoiceText(`Error: ${err?.message || String(err)}`);
      setTimeout(() => {
        setVoiceText('');
      }, 4000);
    } finally {
      abortControllerRef.current = null;
    }
  };

  const handleCancelTask = () => {
    emit('cancel-agent-execution', {});
    setHudState('idle');
    setIsRunning(false);
  };



  // Status Orb visuals
  let orbColor = 'bg-emerald-500';
  let orbShadow = 'shadow-[0_0_12px_rgba(16,185,129,0.6)]';
  let orbPulseClass = 'animate-pulse';

  if (voiceState === 'listening') {
    orbColor = 'bg-rose-500';
    orbShadow = 'shadow-[0_0_12px_rgba(244,63,94,0.6)]';
    orbPulseClass = 'animate-pulse';
  } else if (voiceState === 'transcribing' || voiceState === 'thinking') {
    orbColor = 'bg-amber-500';
    orbShadow = 'shadow-[0_0_12px_rgba(245,158,11,0.6)]';
    orbPulseClass = 'animate-pulse';
  } else if (voiceState === 'speaking') {
    orbColor = 'bg-teal-500';
    orbShadow = 'shadow-[0_0_12px_rgba(20,184,166,0.6)]';
    orbPulseClass = 'animate-ping';
  } else if (hudState === 'working') {
    orbColor = 'bg-amber-500';
    orbShadow = 'shadow-[0_0_12px_rgba(245,158,11,0.6)]';
    orbPulseClass = 'animate-ping';
  } else if (hudState === 'success') {
    orbColor = 'bg-teal-500';
    orbShadow = 'shadow-[0_0_12px_rgba(20,184,166,0.6)]';
    orbPulseClass = '';
  } else if (hudState === 'error') {
    orbColor = 'bg-rose-500';
    orbShadow = 'shadow-[0_0_12px_rgba(244,63,94,0.6)]';
    orbPulseClass = 'animate-pulse';
  }

  // Define display status text
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
    ? 'Goal achieved successfully!'
    : hudState === 'error'
    ? 'Task failed / interrupted'
    : 'System Standby — Online';

  return (
    <div 
      className="w-screen h-screen relative overflow-hidden select-none bg-transparent flex flex-col justify-start p-1.5 font-sans"
      onMouseEnter={() => setIsExpanded(true)}
      onMouseLeave={() => setIsExpanded(false)}
    >
      {isAutomating && (
        <div className="absolute inset-0 rounded-xl border border-amber-500/80 shadow-[0_0_15px_rgba(245,158,11,0.5)] animate-pulse pointer-events-none z-50 flex items-center justify-center bg-amber-500/5">
          <span className="text-[9px] font-bold text-amber-400 uppercase tracking-widest bg-black/90 px-1.5 py-0.5 rounded border border-amber-500/40">
            AUTO: {automatingTool}
          </span>
        </div>
      )}
      <motion.div
        layout
        className={`w-full h-full border flex flex-col transition-all duration-300 relative ${isCompactIdle ? 'p-1' : 'p-2.5'}`}
        style={{
          borderColor: colors.accent + '25',
          backgroundColor: colors.bg + 'd8',
          boxShadow: `0 8px 32px 0 rgba(0, 0, 0, 0.45)`,
          backdropFilter: 'blur(10px)',
          WebkitBackdropFilter: 'blur(10px)',
          borderRadius: isCompactIdle ? '9999px' : '22px'
        }}
      >
        {isCompactIdle ? (
          /* Sleek Minimal Dynamic Island Pill */
          <div 
            data-tauri-drag-region 
            className="flex items-center justify-center gap-2.5 w-full h-full cursor-grab active:cursor-grabbing px-3.5"
          >
            <MascotCharacter state={mascotState} accentColor={colors.accent} wardrobe={equipped} speechAmplitude={speechAmplitude} />
            <span className="text-[10px] font-bold text-zinc-300 tracking-widest uppercase truncate" data-tauri-drag-region>
              Meridian
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
              {/* Left: Mascot Character and text */}
              <div className="flex items-center gap-2.5 flex-1 min-w-0" data-tauri-drag-region>
                <MascotCharacter state={mascotState} accentColor={colors.accent} wardrobe={equipped} speechAmplitude={speechAmplitude} />

                {voiceState === 'listening' || voiceState === 'speaking' ? (
                  <div className="flex items-center gap-1.5 h-6 px-1 flex-1 justify-center overflow-hidden">
                    <svg className="w-24 h-6 overflow-visible text-theme-accent" viewBox="0 0 100 24" fill="none">
                      <motion.path
                        d="M0 12 Q25 2, 50 12 T100 12"
                        stroke="currentColor"
                        strokeWidth="1.5"
                        animate={{
                          d: [
                            "M0 12 Q25 2, 50 12 T100 12",
                            "M0 12 Q25 22, 50 12 T100 12",
                            "M0 12 Q25 2, 50 12 T100 12"
                          ]
                        }}
                        transition={{ duration: 1.5, repeat: Infinity, ease: "easeInOut" }}
                      />
                      <motion.path
                        d="M0 12 Q25 22, 50 12 T100 12"
                        stroke="currentColor"
                        strokeWidth="1"
                        opacity="0.5"
                        animate={{
                          d: [
                            "M0 12 Q25 22, 50 12 T100 12",
                            "M0 12 Q25 2, 50 12 T100 12",
                            "M0 12 Q25 22, 50 12 T100 12"
                          ]
                        }}
                        transition={{ duration: 1.2, repeat: Infinity, ease: "easeInOut" }}
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

              {/* Right: Actions */}
              <div className="flex items-center gap-1.5 flex-shrink-0 z-20">
                <button
                  onClick={handleOpenDashboard}
                  title="Open Dashboard"
                  className="w-6.5 h-6.5 rounded-full bg-zinc-900 border border-zinc-850 hover:border-zinc-700 hover:bg-zinc-800 text-zinc-400 hover:text-zinc-100 flex items-center justify-center transition-all duration-200 cursor-pointer"
                >
                  <LogIn className="w-3 h-3" />
                </button>

                {!isWorking && (
                  <button
                    onClick={() => setShowWardrobeMenu(prev => !prev)}
                    title="Mascot Customization"
                    className={`w-6.5 h-6.5 rounded-full border flex items-center justify-center transition-all duration-200 cursor-pointer ${
                      showWardrobeMenu
                        ? 'bg-amber-950/40 border-amber-800/40 text-amber-400'
                        : 'bg-zinc-900 border-zinc-850 hover:border-zinc-700 hover:bg-zinc-800 text-zinc-400 hover:text-zinc-100'
                    }`}
                  >
                    <Crown className="w-3 h-3" />
                  </button>
                )}

                {hudState === 'working' ? (
                  <button
                    onClick={handleCancelTask}
                    title="Cancel Task"
                    className="w-6.5 h-6.5 rounded-full bg-rose-950/40 hover:bg-rose-900/50 border border-rose-800/40 hover:border-rose-700 text-rose-400 hover:text-rose-300 flex items-center justify-center transition-all duration-200 cursor-pointer"
                  >
                    <X className="w-3 h-3" />
                  </button>
                ) : (
                  <button
                    onClick={handleVoiceChat}
                    title={
                      voiceState === 'listening' ? 'Stop Listening' :
                      voiceState === 'transcribing' ? 'Transcribing...' :
                      voiceState === 'thinking' ? 'Thinking...' :
                      voiceState === 'speaking' ? 'Stop Speaking' : 'Voice Chat'
                    }
                    className={`w-6.5 h-6.5 rounded-full border flex items-center justify-center transition-all duration-200 cursor-pointer ${
                      voiceState === 'listening' ? 'bg-red-950/40 border-red-800/40 hover:bg-red-900/50 hover:border-red-700' :
                      voiceState === 'speaking' ? 'bg-teal-950/40 border-teal-800/40 hover:bg-teal-900/50 hover:border-teal-700' :
                      voiceState !== 'idle' ? 'bg-amber-950/40 border-amber-800/40' :
                      'bg-zinc-900 border-zinc-850 hover:border-zinc-700 hover:bg-zinc-800'
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

            {/* Wardrobe & Audio Settings Panel */}
            {showWardrobeMenu && (
              <div className="mt-2 border-t border-zinc-850 pt-2 flex flex-col gap-2">
                <div className="flex items-center justify-between">
                  <span className="text-[9px] font-bold text-zinc-500 uppercase tracking-wide">Accessories</span>
                  <button 
                    onClick={() => {
                      const nextAudio = !audioEnabled;
                      setAudioEnabled(nextAudio);
                      localStorage.setItem('meridian_mascot_audio_fx', String(nextAudio));
                    }}
                    className="flex items-center gap-1 text-[9px] text-zinc-400 hover:text-zinc-100 bg-zinc-900 px-2 py-0.5 rounded border border-zinc-800 cursor-pointer"
                  >
                    {audioEnabled ? <Volume2 className="w-2.5 h-2.5 text-emerald-400" /> : <VolumeX className="w-2.5 h-2.5 text-zinc-500" />}
                    <span>Sound FX</span>
                  </button>
                </div>
                
                <div className="flex flex-wrap gap-1.5">
                  {[
                    { id: 'auto', name: 'Auto' },
                    { id: 'glasses', name: 'Glasses' },
                    { id: 'construction_hat', name: 'Helmet' },
                    { id: 'detective_hat', name: 'Fedora' },
                    { id: 'crown', name: 'Crown' },
                    { id: 'none', name: 'None' }
                  ].map(item => (
                    <button
                      key={item.id}
                      onClick={() => {
                        setActiveWardrobe(item.id);
                        localStorage.setItem('meridian_mascot_wardrobe', item.id);
                        emit('mascot-wardrobe-changed', { item: item.id }).catch(console.error);
                      }}
                      className={`text-[9px] px-2 py-1 rounded border font-semibold transition-all duration-150 cursor-pointer ${
                        activeWardrobe === item.id
                          ? 'bg-theme-accent/20 border-theme-accent text-theme-accent'
                          : 'bg-zinc-950 border-zinc-850 text-zinc-400 hover:border-zinc-750'
                      }`}
                      style={{
                        borderColor: activeWardrobe === item.id ? colors.accent : undefined,
                        color: activeWardrobe === item.id ? colors.accent : undefined
                      }}
                    >
                      {item.name}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Expanded Details Pane */}
            <AnimatePresence>
              {isExpanded && (
                <motion.div 
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: 'auto' }}
                  exit={{ opacity: 0, height: 0 }}
                  transition={{ duration: 0.2 }}
                  className="flex-1 mt-2.5 border-t border-zinc-800/50 pt-2 flex flex-col justify-between overflow-hidden"
                >
                  {/* Steps / Logs Panel */}
                  {hudState === 'working' && (
                    <div className="flex-1 flex flex-col min-h-0">
                      <span className="text-[8px] font-bold text-zinc-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                        <Loader2 className="w-2.5 h-2.5 animate-spin text-amber-500" />
                        <span>Live Step Ticker</span>
                      </span>
                      <div className="flex-1 overflow-y-auto max-h-[70px] font-mono text-[9px] text-zinc-400 space-y-1 pr-1 select-text scrollbar-thin">
                        {recentThoughts.length === 0 ? (
                          <div className="text-zinc-600 italic">Initializing local agent...</div>
                        ) : (
                          recentThoughts.map((thought, idx) => (
                            <div key={thought.id || idx} className="flex gap-1.5 items-start leading-tight">
                              <span className="text-amber-500 flex-shrink-0">❯</span>
                              <div className="flex-1 truncate">
                                {thought.tool && (
                                  <span className="text-zinc-500 font-bold mr-1">[{thought.tool}]</span>
                                )}
                                <span className="text-zinc-300">{thought.text}</span>
                              </div>
                            </div>
                          ))
                        )}
                      </div>
                    </div>
                  )}

                  {/* Voice Transcription History */}
                  <div className="flex-1 flex flex-col min-h-0 border-t border-zinc-900 pt-1.5 mt-1.5">
                    <span className="text-[8px] font-bold text-zinc-500 uppercase tracking-wide mb-1 flex items-center gap-1">
                      <Mic className="w-2.5 h-2.5 text-theme-accent" />
                      <span>Voice Command History</span>
                    </span>
                    <div className="max-h-[50px] overflow-y-auto font-mono text-[9px] text-zinc-400 space-y-1 pr-1 select-text scrollbar-thin">
                      {voiceLogs.length === 0 ? (
                        <div className="text-zinc-650 italic">No voice sessions recorded.</div>
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
