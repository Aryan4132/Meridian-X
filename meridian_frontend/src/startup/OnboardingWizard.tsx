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
  const [selectedModel, setSelectedModel] = useState<string>('');
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
    <div className="fixed inset-0 z-50 flex items-center justify-center backdrop-blur-md p-4" style={{ background: 'color-mix(in srgb, var(--bg-void) 90%, transparent)' }}>
      <div className="rounded-3xl max-w-xl w-full p-8 shadow-2xl space-y-6" style={{ background: 'var(--bg-float)', border: '1px solid var(--border-subtle)', color: 'var(--text-bright)' }}>
        {/* Header */}
        <div className="text-center space-y-2">
          <div
            className="inline-flex items-center justify-center w-14 h-14 rounded-2xl text-3xl mb-2"
            style={{ background: 'var(--accent-muted)', color: 'var(--accent)' }}
          >
            🚀
          </div>
          <h2 className="text-2xl font-bold tracking-tight" style={{ fontFamily: 'var(--font-heading)' }}>Welcome to Meridian-X</h2>
          <p className="text-sm" style={{ color: 'var(--text-dim)' }}>Let's set up your offline AI brain in 30 seconds</p>
        </div>

        {/* Hardware Status Banner */}
        {specs && (
          <div className="rounded-2xl p-4 flex items-center justify-between text-xs" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)' }}>
            <div className="space-y-1">
              <span className="font-medium" style={{ color: 'var(--text-dim)' }}>Detected Hardware:</span>
              <div className="font-semibold" style={{ color: 'var(--text-main)' }}>
                {specs.ram_gb} GB RAM • {specs.cpu_cores} CPU Cores {specs.gpu.has_gpu && `• ${specs.gpu.name}`}
              </div>
            </div>
            <span className="px-3 py-1 rounded-full font-medium" style={{ background: 'var(--accent-muted)', border: '1px solid var(--border-active)', color: 'var(--accent)' }}>
              {specs.hardware_tier.toUpperCase()} TIER
            </span>
          </div>
        )}

        {/* Existing Ollama Status Alert */}
        {ollamaStatus?.running && ollamaStatus.models.length > 0 && (
          <div className="rounded-2xl p-4 text-xs space-y-2" style={{ background: 'color-mix(in srgb, var(--success) 10%, transparent)', border: '1px solid var(--success)', color: 'var(--success)' }}>
            <div className="font-semibold flex items-center gap-2">
              <span>✅</span> Local AI Engine Detected ({ollamaStatus.models.length} model(s) ready)
            </div>
            <div style={{ color: 'var(--text-main)' }}>
              Installed: {ollamaStatus.models.join(', ')}
            </div>
            <button
              onClick={finishOnboarding}
              className="mt-2 text-xs font-semibold underline"
            >
              Use pre-installed local models and skip download →
            </button>
          </div>
        )}

        {/* Model Selector Cards */}
        <div className="space-y-3">
          <label className="text-xs font-medium" style={{ color: 'var(--text-main)' }}>Choose AI Model Size:</label>
          <div className="grid grid-cols-1 gap-2 max-h-56 overflow-y-auto pr-1">
            {specs?.options.map((opt) => (
              <div
                key={opt.id}
                onClick={() => setSelectedModel(opt.id)}
                className="p-3.5 rounded-xl transition-all cursor-pointer flex items-center justify-between"
                style={selectedModel === opt.id
                  ? { border: '1px solid var(--accent)', background: 'var(--accent-muted)' }
                  : { border: '1px solid var(--border-subtle)', background: 'var(--bg-panel)' }}
              >
                <div>
                  <div className="flex items-center gap-2">
                    <span className="font-semibold text-sm" style={{ color: 'var(--text-bright)' }}>{opt.name}</span>
                    <span className="text-[10px] px-2 py-0.5 rounded-full font-medium" style={{ background: 'var(--bg-surface)', color: 'var(--text-main)' }}>
                      {opt.tier}
                    </span>
                    {specs.recommended_model === opt.id && (
                      <span className="text-[10px] px-2 py-0.5 rounded-full font-medium" style={{ background: 'var(--accent-muted)', border: '1px solid var(--border-active)', color: 'var(--accent)' }}>
                        Best for your PC
                      </span>
                    )}
                  </div>
                  <p className="text-xs mt-1" style={{ color: 'var(--text-dim)' }}>{opt.description}</p>
                </div>
                <div className="text-xs text-right pl-3" style={{ color: 'var(--text-dim)', fontFamily: 'var(--font-main)' }}>
                  {opt.size}
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Progress Bar when downloading */}
        {downloading && (
          <div className="space-y-2 p-4 rounded-2xl" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)' }}>
            <div className="flex justify-between text-xs font-medium" style={{ color: 'var(--text-main)' }}>
              <span>{progress.status}</span>
              <span>{progress.percentage}%</span>
            </div>
            <div className="w-full rounded-full h-2.5 overflow-hidden" style={{ background: 'var(--bg-surface)' }}>
              <div
                className="h-2.5 rounded-full transition-all duration-300"
                style={{ width: `${progress.percentage}%`, background: 'var(--accent)' }}
              ></div>
            </div>
          </div>
        )}

        {/* Error message */}
        {error && (
          <div className="text-xs p-3 rounded-xl" style={{ color: 'var(--danger)', background: 'color-mix(in srgb, var(--danger) 10%, transparent)', border: '1px solid var(--danger)' }}>
            {error}
          </div>
        )}

        {/* Footer Actions */}
        <div className="flex items-center justify-between pt-2">
          <button
            onClick={finishOnboarding}
            className="text-xs"
            style={{ color: 'var(--text-ghost)' }}
          >
            Skip for now (Use Cloud/API key)
          </button>
          <button
            onClick={handleStartPullModel}
            disabled={downloading}
            className="py-3 px-6 font-semibold text-sm rounded-xl transition-all shadow-lg disabled:opacity-50"
            style={{ background: 'var(--accent)', color: 'var(--bg-void)' }}
          >
            {downloading ? 'Setting Up...' : 'Download & Get Started'}
          </button>
        </div>
      </div>
    </div>
  );
};
