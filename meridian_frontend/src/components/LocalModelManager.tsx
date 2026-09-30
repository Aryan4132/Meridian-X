import React, { useState, useEffect } from 'react';
import { Cpu, Download, HardDrive, Trash2, CheckCircle2, Layers, AlertCircle, RefreshCw, Zap } from 'lucide-react';
import { useToast } from './ui/ToastContext';
import { API_BASE_URL } from '../config';

interface QuantPreset {
  name: string;
  description: string;
  bits_per_weight: number;
  quality_loss: string;
  speed_rating: string;
  recommended: boolean;
}

interface LocalModel {
  name: string;
  size_gb: number;
  quantization: string;
  parameter_size: string;
  modified_at: string;
  active: boolean;
}

export const LocalModelManager: React.FC = () => {
  const { showToast } = useToast();
  const [models, setModels] = useState<LocalModel[]>([]);
  const [presets, setPresets] = useState<QuantPreset[]>([]);
  const [activeModel, setActiveModel] = useState<string>(() => localStorage.getItem('MERIDIAN_MODEL') || localStorage.getItem('meridian_model') || '');
  const [loading, setLoading] = useState<boolean>(false);
  const [pullModelName, setPullModelName] = useState<string>('');
  const [selectedQuant, setSelectedQuant] = useState<string>('Q4_K_M');
  const [pullProgress, setPullProgress] = useState<{ status: string; percentage: number } | null>(null);

  // Resource Estimator State
  const [estimateParams, setEstimateParams] = useState<number>(8);
  const [estimateResult, setEstimateResult] = useState<{ estimated_vram_gb: number; estimated_ram_gb: number } | null>({
    estimated_vram_gb: 5.7,
    estimated_ram_gb: 7.13
  });

  useEffect(() => {
    fetchModels();
    fetchQuantOptions();
  }, []);

  const fetchModels = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/models/local`);
      if (res.ok) {
        const data = await res.json();
        setModels(data.models || []);
        if (data.active_model) setActiveModel(data.active_model);
      }
    } catch (e) {
      console.error('Failed to fetch local models:', e);
    } finally {
      setLoading(false);
    }
  };

  const fetchQuantOptions = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/models/quantization-options`);
      if (res.ok) {
        const data = await res.json();
        setPresets(data.presets || []);
      }
    } catch (e) {
      console.error('Failed to fetch quantization presets:', e);
    }
  };

  const calculateEstimate = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/models/estimate-resources`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ param_count_billion: estimateParams, quantization: selectedQuant })
      });
      if (res.ok) {
        const data = await res.json();
        setEstimateResult(data);
        showToast('Resource Footprint Calculated', `VRAM: ${data.estimated_vram_gb} GB, RAM: ${data.estimated_ram_gb} GB`, 'success');
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleSetActive = async (modelName: string, quant: string) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/models/local/active`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model_name: modelName, quantization: quant })
      });
      if (res.ok) {
        setActiveModel(modelName);
        showToast('Active Model Updated', `Switched to ${modelName}`, 'success');
        fetchModels();
      }
    } catch (e) {
      console.error('Failed to set active model:', e);
    }
  };

  const handleDelete = async (modelName: string) => {
    if (!confirm(`Are you sure you want to delete ${modelName}?`)) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/models/local/${encodeURIComponent(modelName)}`, {
        method: 'DELETE'
      });
      if (res.ok) {
        showToast('Model Deleted', `Deleted ${modelName}`, 'info');
        fetchModels();
      }
    } catch (e) {
      console.error('Failed to delete model:', e);
    }
  };

  const handlePullModel = async () => {
    if (!pullModelName.trim()) return;
    setPullProgress({ status: 'Initiating download...', percentage: 0 });

    try {
      const res = await fetch(`${API_BASE_URL}/api/models/local/pull`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ model_name: pullModelName, quantization: selectedQuant })
      });

      if (res.ok && res.body) {
        const reader = res.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
          const { value, done } = await reader.read();
          if (done) break;
          const chunkStr = decoder.decode(value);
          const lines = chunkStr.split('\n').filter(Boolean);
          for (const line of lines) {
            try {
              const data = JSON.parse(line);
              setPullProgress({ status: data.status, percentage: data.percentage || 0 });
              if (data.done) {
                setPullProgress(null);
                setPullModelName('');
                showToast('Model Pull Complete', `Pulled ${pullModelName}`, 'success');
                fetchModels();
              }
            } catch (err) {}
          }
        }
      }
    } catch (e) {
      console.error('Error pulling model:', e);
      setPullProgress(null);
    }
  };

  // SVG Radial Gauge Math (16GB max baseline)
  const maxVram = 16;
  const vramPercent = Math.min(100, Math.round(((estimateResult?.estimated_vram_gb || 5.7) / maxVram) * 100));
  const strokeDashoffset = 251.2 - (251.2 * vramPercent) / 100;

  return (
    <div className="space-y-6 text-[var(--text-bright)]">
      {/* Header */}
      <div className="flex items-center justify-between p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-[var(--accent-muted)] border border-[var(--border-active)] rounded-lg">
            <Cpu className="w-6 h-6 text-[var(--accent)]" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-[var(--text-bright)]">Local Model & Quantization Manager</h2>
            <p className="text-xs text-[var(--text-dim)]">Deploy, profile, and switch quantized local LLMs (Ollama / GGUF)</p>
          </div>
        </div>
        <button
          onClick={fetchModels}
          disabled={loading}
          className="flex items-center gap-2 px-3 py-1.5 text-xs bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-[var(--text-main)] border border-[var(--border-subtle)] rounded-lg transition"
        >
          <RefreshCw className={`w-3.5 h-3.5 ${loading ? 'animate-spin' : ''}`} />
          Refresh Models
        </button>
      </div>

      {/* Grid Content */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left Column: Installed Models & Pull */}
        <div className="lg:col-span-2 space-y-6">
          {/* Pull New Model Card */}
          <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--accent)]">
              <Download className="w-4 h-4" /> Pull New Model with Quantization
            </h3>
            <div className="flex flex-col sm:flex-row gap-3">
              <input
                type="text"
                placeholder="Model Tag (e.g. llama3:8b, mistral:7b, qwen2.5:7b)"
                value={pullModelName}
                onChange={(e) => setPullModelName(e.target.value)}
                className="flex-1 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg px-3 py-2 text-xs focus:border-[var(--accent)] outline-none"
              />
              <select
                value={selectedQuant}
                onChange={(e) => setSelectedQuant(e.target.value)}
                className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg px-3 py-2 text-xs focus:border-[var(--accent)] outline-none text-[var(--text-main)]"
              >
                {presets.map((p) => (
                  <option key={p.name} value={p.name}>
                    {p.name} ({p.bits_per_weight} bpw - {p.speed_rating})
                  </option>
                ))}
              </select>
              <button
                onClick={handlePullModel}
                disabled={!pullModelName.trim() || !!pullProgress}
                className="px-4 py-2 bg-[var(--accent)] hover:bg-[var(--accent-dim)] text-[var(--bg-void)] font-medium text-xs rounded-lg shadow-lg transition disabled:opacity-50"
              >
                Pull Model
              </button>
            </div>

            {pullProgress && (
              <div className="space-y-1.5 pt-2">
                <div className="flex justify-between text-xs text-[var(--text-main)]">
                  <span>{pullProgress.status}</span>
                  <span className="font-mono">{pullProgress.percentage}%</span>
                </div>
                <div className="w-full bg-[var(--bg-panel)] rounded-full h-2 overflow-hidden border border-[var(--border-subtle)]">
                  <div
                    className="bg-[var(--accent)] h-full transition-all duration-300"
                    style={{ width: `${pullProgress.percentage}%` }}
                  />
                </div>
              </div>
            )}
          </div>

          {/* Installed Models List */}
          <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--text-main)]">
              <HardDrive className="w-4 h-4 text-[var(--success)]" /> Installed Models
            </h3>

            {models.length === 0 ? (
              <div className="p-6 text-center text-xs text-[var(--text-ghost)] border border-dashed border-[var(--border-subtle)] rounded-xl">
                No local models detected. Make sure Ollama or local LLM server is running.
              </div>
            ) : (
              <div className="space-y-3">
                {models.map((m) => (
                  <div
                    key={m.name}
                    className={`flex items-center justify-between p-3.5 rounded-xl border transition ${
                      m.active
                        ? 'bg-[var(--accent-muted)] border-[var(--accent)] shadow-md'
                        : 'bg-[var(--bg-panel)] border-[var(--border-subtle)] hover:border-[var(--border-active)]'
                    }`}
                  >
                    <div className="space-y-1">
                      <div className="flex items-center gap-2">
                        <span className="font-mono font-semibold text-xs text-[var(--text-bright)]">{m.name}</span>
                        {m.active && (
                          <span className="inline-flex items-center gap-1 px-2 py-0.5 text-[10px] font-semibold bg-[color-mix(in_srgb,var(--success)_12%,transparent)] border border-[var(--success)] text-[var(--success)] rounded-full">
                            <CheckCircle2 className="w-3 h-3" /> Active
                          </span>
                        )}
                        <span className="px-2 py-0.5 text-[10px] font-mono bg-[var(--bg-surface)] border border-[var(--border-subtle)] text-[var(--accent)] rounded">
                          {m.quantization || 'Q4_K_M'}
                        </span>
                      </div>
                      <div className="flex items-center gap-3 text-[11px] text-[var(--text-dim)]">
                        <span>Disk: {m.size_gb} GB</span>
                        <span>Params: {m.parameter_size}</span>
                      </div>
                    </div>

                    <div className="flex items-center gap-2">
                      {!m.active && (
                        <button
                          onClick={() => handleSetActive(m.name, m.quantization)}
                          className="px-3 py-1 text-xs bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-[var(--text-main)] border border-[var(--border-subtle)] rounded-lg transition"
                        >
                          Set Active
                        </button>
                      )}
                      <button
                        onClick={() => handleDelete(m.name)}
                        className="p-1.5 text-[var(--text-ghost)] hover:text-[var(--danger)] rounded-lg hover:bg-[color-mix(in_srgb,var(--danger)_12%,transparent)] transition"
                      >
                        <Trash2 className="w-4 h-4" />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>

        {/* Right Column: Quantization Presets & VRAM Ring Meter */}
        <div className="space-y-6">
          {/* Animated SVG Radial Gauge VRAM / RAM Estimator */}
          <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--warning)]">
              <Zap className="w-4 h-4" /> VRAM / RAM Radial Footprint Gauge
            </h3>

            {/* SVG Ring Meter */}
            <div className="flex items-center justify-center py-2 relative">
              <svg className="w-32 h-32 transform -rotate-90" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="40" stroke="currentColor" strokeWidth="8" className="text-[var(--text-ghost)]" fill="transparent" />
                <circle
                  cx="50" cy="50" r="40"
                  stroke="url(#vramGradient)" strokeWidth="8" strokeDasharray="251.2"
                  strokeDashoffset={strokeDashoffset}
                  strokeLinecap="round" fill="transparent"
                  className="transition-all duration-700 ease-out"
                />
                <defs>
                  <linearGradient id="vramGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stopColor="#00F0FF" />
                    <stop offset="100%" stopColor="#3B82F6" />
                  </linearGradient>
                </defs>
              </svg>
              <div className="absolute flex flex-col items-center justify-center text-center">
                <span className="text-lg font-bold font-mono text-[var(--accent)]">{estimateResult?.estimated_vram_gb} GB</span>
                <span className="text-[10px] text-[var(--text-dim)] font-mono">VRAM ({vramPercent}%)</span>
              </div>
            </div>

            <div className="space-y-3">
              <div>
                <label className="text-[11px] text-[var(--text-dim)] block mb-1">Parameter Count (Billions)</label>
                <input
                  type="number"
                  value={estimateParams}
                  onChange={(e) => setEstimateParams(parseFloat(e.target.value) || 0)}
                  className="w-full bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg px-3 py-2 text-xs text-[var(--text-bright)] outline-none"
                />
              </div>
              <button
                onClick={calculateEstimate}
                className="w-full py-1.5 bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] border border-[var(--border-subtle)] text-[var(--text-main)] rounded-lg text-xs font-medium transition"
              >
                Estimate Hardware Footprint
              </button>
              {estimateResult && (
                <div className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg text-xs space-y-1">
                  <div className="flex justify-between text-[var(--text-main)]">
                    <span>Est. VRAM Required:</span>
                    <span className="font-mono text-[var(--accent)] font-bold">{estimateResult.estimated_vram_gb} GB</span>
                  </div>
                  <div className="flex justify-between text-[var(--text-main)]">
                    <span>Est. System RAM:</span>
                    <span className="font-mono text-[var(--success)] font-bold">{estimateResult.estimated_ram_gb} GB</span>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Quantization Profiles Reference */}
          <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md space-y-3">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--accent-2)]">
              <Layers className="w-4 h-4" /> Quantization Presets
            </h3>
            <div className="space-y-2.5 max-h-80 overflow-y-auto pr-1">
              {presets.map((p) => (
                <div key={p.name} className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-mono font-bold text-xs text-[var(--text-main)]">{p.name}</span>
                    <span className="text-[10px] px-2 py-0.5 bg-[var(--accent-muted)] border border-[var(--border-active)] text-[var(--accent-2)] rounded-full">
                      {p.bits_per_weight} bpw
                    </span>
                  </div>
                  <p className="text-[11px] text-[var(--text-dim)]">{p.description}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
