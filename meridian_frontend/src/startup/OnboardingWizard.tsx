import React, { useState, useEffect } from 'react';
import { API_BASE_URL } from '../config';

interface ModelOption {
  id: string;
  name: string;
  tier: string;
  size: string;
  min_ram: string;
  description: string;
}

interface HardwareSpecs {
  cpu_cores: number;
  ram_gb: number;
  gpu: { has_gpu: boolean; vram_gb: number; name: string };
  hardware_tier: string;
  recommended_model: string;
  recommended_label: string;
  description: string;
  options: ModelOption[];
}

interface OllamaStatus {
  installed: boolean;
  running: boolean;
  base_url: string;
  models: string[];
  detected_port: string | null;
}

export const OnboardingWizard: React.FC<{ onComplete: () => void }> = ({ onComplete }) => {
  const [step, setStep] = useState<1 | 2 | 3>(1);
  const [specs, setSpecs] = useState<HardwareSpecs | null>(null);
  const [ollamaStatus, setOllamaStatus] = useState<OllamaStatus | null>(null);
  const [selectedModel, setSelectedModel] = useState<string>('llama3.2:3b');
  const [downloading, setDownloading] = useState(false);
  const [progress, setProgress] = useState<{ status: string; percentage: number }>({
    status: 'Ready',
    percentage: 0,
  });
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchHardwareSpecs();
    fetchOllamaStatus();
  }, []);

  const fetchHardwareSpecs = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/onboarding/hardware-spec`);
      if (res.ok) {
        const data: HardwareSpecs = await res.json();
        setSpecs(data);
        if (data.recommended_model) {
          setSelectedModel(data.recommended_model);
        }
      }
    } catch (e) {
      console.error('Failed to fetch hardware specs:', e);
    }
  };

  const fetchOllamaStatus = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/onboarding/ollama-status`);
      if (res.ok) {
        const data: OllamaStatus = await res.json();
        setOllamaStatus(data);
      }
    } catch (e) {
      console.error('Failed to fetch Ollama status:', e);
    }
  };

  const handleStartPullModel = async () => {
    setDownloading(true);
    setError(null);
    setProgress({ status: 'Starting download...', percentage: 0 });

    try {
      const response = await fetch(`${API_BASE_URL}/api/onboarding/models/pull`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model_name: selectedModel }),
      });

      if (!response.ok || !response.body) {
        throw new Error('Failed to initiate model pull');
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('data:')) {
            try {
              const jsonStr = line.slice(5).trim();
              if (jsonStr) {
                const chunk = JSON.parse(jsonStr);
                if (chunk.status === 'error') {
                  throw new Error(chunk.message || 'Download error');
                }
                setProgress({
                  status: chunk.status || 'Downloading...',
                  percentage: chunk.percentage || 0,
                });

                if (chunk.done || chunk.percentage === 100) {
                  setDownloading(false);
                  finishOnboarding();
                  return;
                }
              }
            } catch (err) {
              console.warn('Parsing SSE error:', err);
            }
          }
        }
      }
      setDownloading(false);
      finishOnboarding();
    } catch (err: any) {
      setError(err.message || 'Model download failed. Check network connection.');
      setDownloading(false);
    }
  };

  const finishOnboarding = () => {
    localStorage.setItem('MERIDIAN_ONBOARDED', 'true');
    localStorage.setItem('MERIDIAN_MODEL', selectedModel);
    onComplete();
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950/90 backdrop-blur-md p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-3xl max-w-xl w-full p-8 text-white shadow-2xl space-y-6">
        {/* Header */}
        <div className="text-center space-y-2">
          <div className="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-indigo-600/20 text-indigo-400 text-3xl mb-2">
            🚀
          </div>
          <h2 className="text-2xl font-bold tracking-tight">Welcome to Meridian-X</h2>
          <p className="text-slate-400 text-sm">Let's set up your offline AI brain in 30 seconds</p>
        </div>

        {/* Hardware Status Banner */}
        {specs && (
          <div className="bg-slate-950 border border-slate-800 rounded-2xl p-4 flex items-center justify-between text-xs">
            <div className="space-y-1">
              <span className="text-slate-400 font-medium">Detected Hardware:</span>
              <div className="font-semibold text-slate-200">
                {specs.ram_gb} GB RAM • {specs.cpu_cores} CPU Cores {specs.gpu.has_gpu && `• ${specs.gpu.name}`}
              </div>
            </div>
            <span className="px-3 py-1 bg-indigo-950 border border-indigo-700 text-indigo-300 rounded-full font-medium">
              {specs.hardware_tier.toUpperCase()} TIER
            </span>
          </div>
        )}

        {/* Existing Ollama Status Alert */}
        {ollamaStatus?.running && ollamaStatus.models.length > 0 && (
          <div className="bg-emerald-950/50 border border-emerald-800 rounded-2xl p-4 text-xs text-emerald-300 space-y-2">
            <div className="font-semibold flex items-center gap-2">
              <span>✅</span> Local AI Engine Detected ({ollamaStatus.models.length} model(s) ready)
            </div>
            <div className="text-slate-300">
              Installed: {ollamaStatus.models.join(', ')}
            </div>
            <button
              onClick={finishOnboarding}
              className="mt-2 text-xs font-semibold underline hover:text-white"
            >
              Use pre-installed local models and skip download →
            </button>
          </div>
        )}

        {/* Model Selector Cards */}
        <div className="space-y-3">
          <label className="text-xs font-medium text-slate-300">Choose AI Model Size:</label>
          <div className="grid grid-cols-1 gap-2 max-h-56 overflow-y-auto pr-1">
            {specs?.options.map((opt) => (
              <div
                key={opt.id}
                onClick={() => setSelectedModel(opt.id)}
                className={`p-3.5 rounded-xl border transition-all cursor-pointer flex items-center justify-between ${
                  selectedModel === opt.id
                    ? 'border-indigo-500 bg-indigo-950/30'
                    : 'border-slate-800 bg-slate-950/50 hover:border-slate-700'
                }`}
              >
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-sm text-white">{opt.name}</span>
                    <span className="text-[10px] px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 font-medium">
                      {opt.tier}
                    </span>
                    {specs.recommended_model === opt.id && (
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-amber-950 border border-amber-700 text-amber-300 font-medium">
                        Best for your PC
                      </span>
                    )}
                  </div>
                  <p className="text-xs text-slate-400 mt-1">{opt.description}</p>
                </div>
                <div className="text-xs text-slate-400 font-mono text-right pl-3">
                  {opt.size}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Progress Bar when downloading */}
        {downloading && (
          <div className="space-y-2 bg-slate-950 p-4 rounded-2xl border border-slate-800">
            <div className="flex justify-between text-xs text-slate-300 font-medium">
              <span>{progress.status}</span>
              <span>{progress.percentage}%</span>
            </div>
            <div className="w-full bg-slate-800 rounded-full h-2.5 overflow-hidden">
              <div
                className="bg-indigo-500 h-2.5 rounded-full transition-all duration-300"
                style={{ width: `${progress.percentage}%` }}
              ></div>
            </div>
          </div>
        )}

        {/* Error message */}
        {error && (
          <div className="text-xs text-rose-400 bg-rose-950/50 border border-rose-800 p-3 rounded-xl">
            {error}
          </div>
        )}

        {/* Footer Actions */}
        <div className="flex items-center justify-between pt-2">
          <button
            onClick={finishOnboarding}
            className="text-xs text-slate-500 hover:text-slate-400"
          >
            Skip for now (Use Cloud/API key)
          </button>
          <button
            onClick={handleStartPullModel}
            disabled={downloading}
            className="py-3 px-6 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-xl transition-all shadow-lg disabled:opacity-50"
          >
            {downloading ? 'Setting Up...' : 'Download & Get Started'}
          </button>
        </div>
      </div>
    </div>
  );
};
