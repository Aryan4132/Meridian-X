import React, { useState } from 'react';
import { Gamepad2, Eye, Zap, ShieldAlert } from 'lucide-react';

export const GameOverlay: React.FC = () => {
  const [isActive, setIsActive] = useState<boolean>(true);
  const [lastTip, setLastTip] = useState<string>('Enemy objective spawning in 15 seconds. Recommend rotating top lane.');

  return (
    <div className="p-6 bg-slate-900 text-slate-100 min-h-screen space-y-6">
      <div className="flex items-center space-x-3 border-b border-slate-800 pb-4">
        <Gamepad2 className="w-8 h-8 text-purple-400" />
        <div>
          <h1 className="text-2xl font-bold">Real-Time AI Game Coach (GAM-01)</h1>
          <p className="text-sm text-slate-400">Live OCR & Vision State Tactical Voice Tips (Alt+Space)</p>
        </div>
      </div>

      <div className="bg-slate-800/60 p-5 rounded-xl border border-slate-700 space-y-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2 text-purple-400">
            <Eye className="w-5 h-5" />
            <h2 className="font-semibold text-lg">Screen Vision State Parser</h2>
          </div>
          <button
            onClick={() => setIsActive(!isActive)}
            className={`px-4 py-1.5 rounded-lg text-sm font-medium transition ${
              isActive ? 'bg-purple-600 hover:bg-purple-500' : 'bg-slate-700 hover:bg-slate-600'
            }`}
          >
            {isActive ? 'Overlay Active' : 'Overlay Paused'}
          </button>
        </div>

        <div className="bg-slate-950 p-4 rounded-lg border border-purple-500/20 space-y-2">
          <div className="flex items-center space-x-2 text-amber-400 text-xs font-semibold uppercase tracking-wider">
            <Zap className="w-4 h-4" />
            <span>Latest Strategic Tactical Tip</span>
          </div>
          <p className="text-slate-200 text-sm font-medium">{lastTip}</p>
        </div>
      </div>
    </div>
  );
};

export default GameOverlay;
