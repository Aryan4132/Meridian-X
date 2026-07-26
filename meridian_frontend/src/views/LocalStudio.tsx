import React, { useState } from 'react';
import { Palette, Sparkles, Image as ImageIcon, Download } from 'lucide-react';

export const LocalStudio: React.FC = () => {
  const [prompt, setPrompt] = useState<string>('Futuristic cyberpunk mascot icon with neon blue aura');
  const [isGenerating, setIsGenerating] = useState<boolean>(false);

  const handleGenerate = () => {
    setIsGenerating(true);
    setTimeout(() => setIsGenerating(false), 1500);
  };

  return (
    <div className="p-6 bg-slate-900 text-slate-100 min-h-screen space-y-6">
      <div className="flex items-center space-x-3 border-b border-slate-800 pb-4">
        <Palette className="w-8 h-8 text-pink-400" />
        <div>
          <h1 className="text-2xl font-bold">Local AI Visual Studio (CRT-01)</h1>
          <p className="text-sm text-slate-400">Local Graphic Assets, Icons & UI Mockup Generator</p>
        </div>
      </div>

      <div className="bg-slate-800/60 p-5 rounded-xl border border-slate-700 space-y-4">
        <div className="space-y-2">
          <label className="text-xs font-semibold text-slate-400 uppercase">Image Prompt</label>
          <div className="flex space-x-2">
            <input
              type="text"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              className="flex-1 bg-slate-950 px-4 py-2 rounded-lg border border-slate-800 text-sm focus:outline-none focus:border-pink-500"
            />
            <button
              onClick={handleGenerate}
              disabled={isGenerating}
              className="flex items-center space-x-2 px-5 py-2 bg-pink-600 hover:bg-pink-500 rounded-lg text-sm font-medium transition disabled:opacity-50"
            >
              <Sparkles className="w-4 h-4" />
              <span>{isGenerating ? 'Synthesizing...' : 'Generate Asset'}</span>
            </button>
          </div>
        </div>

        <div className="bg-slate-950 p-8 rounded-lg border border-slate-800 flex flex-col items-center justify-center space-y-3 min-h-[220px]">
          <ImageIcon className="w-12 h-12 text-slate-600" />
          <p className="text-sm text-slate-400">Local Diffusion Engine Ready (FLUX / ComfyUI)</p>
        </div>
      </div>
    </div>
  );
};

export default LocalStudio;
