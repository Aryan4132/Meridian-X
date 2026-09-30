import React, { useState, useEffect } from 'react';
import { Camera, Mic, Eye, Sparkles, Shield, RefreshCw } from 'lucide-react';

export const PerceptionHUD: React.FC = () => {
  const [cameraActive, setCameraActive] = useState(true);
  const [micActive, setMicActive] = useState(true);
  const [gazeActive, setGazeActive] = useState(false);
  const [gestureActive, setGestureActive] = useState(true);
  const [recentAlert, setRecentAlert] = useState<string | null>("Room presence sentinel active");

  return (
    <div className="flex items-center gap-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-full px-3 py-1.5 backdrop-blur-md shadow-lg text-xs font-mono text-[var(--text-dim)]">
      <div className="flex items-center gap-1.5">
        <button
          onClick={() => setCameraActive(!cameraActive)}
          className={`p-1 rounded-full transition-colors ${
            cameraActive ? 'bg-[color-mix(in_srgb,var(--success)_15%,transparent)] text-[var(--success)]' : 'bg-[color-mix(in_srgb,var(--danger)_15%,transparent)] text-[var(--danger)]'
          }`}
          title={cameraActive ? "Camera Sentinel Active (Click to Mute)" : "Camera Muted"}
        >
          <Camera className="w-3.5 h-3.5" />
        </button>
        <button
          onClick={() => setMicActive(!micActive)}
          className={`p-1 rounded-full transition-colors ${
            micActive ? 'bg-[color-mix(in_srgb,var(--success)_15%,transparent)] text-[var(--success)]' : 'bg-[color-mix(in_srgb,var(--danger)_15%,transparent)] text-[var(--danger)]'
          }`}
          title={micActive ? "Microphone Sentinel Active (Click to Mute)" : "Microphone Muted"}
        >
          <Mic className="w-3.5 h-3.5" />
        </button>
      </div>

      <div className="h-3 w-px bg-[var(--border-subtle)]" />

      <div className="flex items-center gap-2">
        <button
          onClick={() => setGazeActive(!gazeActive)}
          className={`flex items-center gap-1 px-2 py-0.5 rounded-full transition-all ${
            gazeActive ? 'bg-[var(--accent-muted)] text-[var(--accent-2)] border border-[var(--border-active)]' : 'bg-[var(--bg-surface)] text-[var(--text-ghost)]'
          }`}
        >
          <Eye className="w-3 h-3" />
          <span>Gaze</span>
        </button>

        <button
          onClick={() => setGestureActive(!gestureActive)}
          className={`flex items-center gap-1 px-2 py-0.5 rounded-full transition-all ${
            gestureActive ? 'bg-[var(--accent-muted)] text-[var(--accent)] border border-[var(--border-active)]' : 'bg-[var(--bg-surface)] text-[var(--text-ghost)]'
          }`}
        >
          <Sparkles className="w-3 h-3" />
          <span>Gesture</span>
        </button>
      </div>

      {recentAlert && (
        <div className="flex items-center gap-1.5 text-[10px] text-[var(--text-dim)] border-l border-[var(--border-subtle)] pl-2">
          <Shield className="w-3 h-3 text-[var(--accent)] animate-pulse" />
          <span className="truncate max-w-[140px]">{recentAlert}</span>
        </div>
      )}
    </div>
  );
};
