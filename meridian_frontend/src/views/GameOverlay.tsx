import React, { useState, useEffect } from 'react';
import { Mic, Activity, ShieldAlert, Cpu } from 'lucide-react';

export const GameOverlay: React.FC = () => {
  const [visible, setVisible] = useState(false);
  const [fps, setFps] = useState(120);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.altKey && e.code === 'Space') {
        e.preventDefault();
        setVisible((prev) => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  if (!visible) return null;

  return (
    <div className="fixed top-4 right-4 z-50 p-3 bg-slate-950/80 backdrop-blur-md border border-cyan-500/30 rounded-2xl shadow-xl shadow-cyan-500/10 text-xs text-slate-200 min-w-[220px] animate-pulse-slow">
      <div className="flex items-center justify-between border-b border-slate-800 pb-2 mb-2">
        <div className="flex items-center space-x-2">
          <div className="w-2 h-2 rounded-full bg-emerald-400 animate-ping" />
          <span className="font-bold tracking-wider text-cyan-400">GAME OVERLAY</span>
        </div>
        <span className="text-[10px] text-slate-500">Alt+Space</span>
      </div>

      <div className="space-y-1.5">
        <div className="flex items-center justify-between">
          <span className="flex items-center text-slate-400"><Cpu className="w-3 h-3 mr-1 text-cyan-400" /> CPU Load</span>
          <span className="font-mono text-emerald-400">18%</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="flex items-center text-slate-400"><Activity className="w-3 h-3 mr-1 text-purple-400" /> Frame Rate</span>
          <span className="font-mono text-cyan-400">{fps} FPS</span>
        </div>
        <div className="flex items-center justify-between">
          <span className="flex items-center text-slate-400"><Mic className="w-3 h-3 mr-1 text-emerald-400" /> Voice Hotkey</span>
          <span className="font-mono text-slate-300">Active</span>
        </div>
      </div>
    </div>
  );
};
