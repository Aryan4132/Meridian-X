import React, { useState, useEffect } from 'react';
import { Camera, Mic, Eye, Sparkles, Shield, RefreshCw } from 'lucide-react';

export const PerceptionHUD: React.FC = () => {
  const [cameraActive, setCameraActive] = useState(true);
  const [micActive, setMicActive] = useState(true);
  const [gazeActive, setGazeActive] = useState(false);
  const [gestureActive, setGestureActive] = useState(true);
  const [recentAlert, setRecentAlert] = useState<string | null>("Room presence sentinel active");

  return (
    <div className="flex items-center gap-3 bg-zinc-900/80 border border-zinc-800 rounded-full px-3 py-1.5 backdrop-blur-md shadow-lg text-xs font-mono text-zinc-300">
      <div className="flex items-center gap-1.5">
        <button
          onClick={() => setCameraActive(!cameraActive)}
          className={`p-1 rounded-full transition-colors ${
            cameraActive ? 'bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30' : 'bg-red-500/20 text-red-400 hover:bg-red-500/30'
          }`}
          title={cameraActive ? "Camera Sentinel Active (Click to Mute)" : "Camera Muted"}
        >
          <Camera className="w-3.5 h-3.5" />
        </button>
        <button
          onClick={() => setMicActive(!micActive)}
          className={`p-1 rounded-full transition-colors ${
            micActive ? 'bg-emerald-500/20 text-emerald-400 hover:bg-emerald-500/30' : 'bg-red-500/20 text-red-400 hover:bg-red-500/30'
          }`}
          title={micActive ? "Microphone Sentinel Active (Click to Mute)" : "Microphone Muted"}
        >
          <Mic className="w-3.5 h-3.5" />
        </button>
      </div>

      <div className="h-3 w-px bg-zinc-800" />

      <div className="flex items-center gap-2">
        <button
          onClick={() => setGazeActive(!gazeActive)}
          className={`flex items-center gap-1 px-2 py-0.5 rounded-full transition-all ${
            gazeActive ? 'bg-indigo-500/20 text-indigo-300 border border-indigo-500/30' : 'bg-zinc-800 text-zinc-500'
          }`}
        >
          <Eye className="w-3 h-3" />
          <span>Gaze</span>
        </button>

        <button
          onClick={() => setGestureActive(!gestureActive)}
          className={`flex items-center gap-1 px-2 py-0.5 rounded-full transition-all ${
            gestureActive ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30' : 'bg-zinc-800 text-zinc-500'
          }`}
        >
          <Sparkles className="w-3 h-3" />
          <span>Gesture</span>
        </button>
      </div>

      {recentAlert && (
        <div className="flex items-center gap-1.5 text-[10px] text-zinc-400 border-l border-zinc-800 pl-2">
          <Shield className="w-3 h-3 text-cyan-400 animate-pulse" />
          <span className="truncate max-w-[140px]">{recentAlert}</span>
        </div>
      )}
    </div>
  );
};
