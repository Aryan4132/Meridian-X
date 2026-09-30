import React, { useState, useEffect } from 'react';
import { Cpu, Download, HardDrive, Trash2, CheckCircle2, Layers, AlertCircle, RefreshCw, Zap } from 'lucide-react';
import { useToast } from './ui/ToastContext';

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
  const [activeModel, setActiveModel] = useState<string>('llama3:8b-instruct-q4_K_M');
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
      const res = await fetch('/api/models/local');
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
      const res = await fetch('/api/models/quantization-options');
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
      const res = await fetch('/api/models/estimate-resources', {
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
      const res = await fetch('/api/models/local/active', {
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
      const res = await fetch(`/api/models/local/${encodeURIComponent(modelName)}`, {
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
      const res = await fetch('/api/models/local/pull', {
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
    <div className="space-y-6 text-slate-100">
      {/* Header */}
      <div className="flex items-center justify-between p-4 bg-slate-900/80 border border-slate-800 rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-cyan-500/10 border border-cyan-500/30 rounded-lg">
            <Cpu className="w-6 h-6 text-cyan-400" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-slate-100">Local Model & Quantization Manager</h2>
            <p className="text-xs text-slate-400">Deploy, profile, and switch quantized local LLMs (Ollama / GGUF)</p>
          </div>
        </div>
        <button
          onClick={fetchModels}
          disabled={loading}
          className="flex items-center gap-2 px-3 py-1.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg transition"
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
          <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-cyan-400">
              <Download className="w-4 h-4" /> Pull New Model with Quantization
            </h3>
            <div className="flex flex-col sm:flex-row gap-3">
              <input
                type="text"
                placeholder="Model Tag (e.g. llama3:8b, mistral:7b, qwen2.5:7b)"
                value={pullModelName}
                onChange={(e) => setPullModelName(e.target.value)}
                className="flex-1 bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs focus:border-cyan-500 outline-none"
              />
              <select
                value={selectedQuant}
                onChange={(e) => setSelectedQuant(e.target.value)}
                className="bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs focus:border-cyan-500 outline-none text-slate-300"
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
                className="px-4 py-2 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-white font-medium text-xs rounded-lg shadow-lg shadow-cyan-500/20 transition disabled:opacity-50"
              >
                Pull Model
              </button>
            </div>

            {pullProgress && (
              <div className="space-y-1.5 pt-2">
                <div className="flex justify-between text-xs text-slate-300">
                  <span>{pullProgress.status}</span>
                  <span className="font-mono">{pullProgress.percentage}%</span>
                </div>
                <div className="w-full bg-slate-950 rounded-full h-2 overflow-hidden border border-slate-800">
                  <div
                    className="bg-gradient-to-r from-cyan-400 to-blue-500 h-full transition-all duration-300"
                    style={{ width: `${pullProgress.percentage}%` }}
                  />
                </div>
              </div>
            )}
          </div>

          {/* Installed Models List */}
          <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-slate-200">
              <HardDrive className="w-4 h-4 text-emerald-400" /> Installed Models
            </h3>

            {models.length === 0 ? (
              <div className="p-6 text-center text-xs text-slate-500 border border-dashed border-slate-800 rounded-xl">
                No local models detected. Make sure Ollama or local LLM server is running.
              </div>
            ) : (
              <div className="space-y-3">
                {models.map((m) => (
                  <div
                    key={m.name}
                    className={`flex items-center justify-between p-3.5 rounded-xl border transition ${
                      m.active
                        ? 'bg-cyan-950/30 border-cyan-500/50 shadow-md shadow-cyan-500/10'
                        : 'bg-slate-950/40 border-slate-800 hover:border-slate-700'
                    }`}
                  >
                    <div className="space-y-1">
                      <div className="flex items-center gap-2">
                        <span className="font-mono font-semibold text-xs text-slate-100">{m.name}</span>
                        {m.active && (
                          <span className="inline-flex items-center gap-1 px-2 py-0.5 text-[10px] font-semibold bg-emerald-500/10 border border-emerald-500/30 text-emerald-400 rounded-full">
                            <CheckCircle2 className="w-3 h-3" /> Active
                          </span>
                        )}
                        <span className="px-2 py-0.5 text-[10px] font-mono bg-slate-800 border border-slate-700 text-cyan-400 rounded">
                          {m.quantization || 'Q4_K_M'}
                        </span>
                      </div>
                      <div className="flex items-center gap-3 text-[11px] text-slate-400">
                        <span>Disk: {m.size_gb} GB</span>
                        <span>Params: {m.parameter_size}</span>
                      </div>
                    </div>

                    <div className="flex items-center gap-2">
                      {!m.active && (
                        <button
                          onClick={() => handleSetActive(m.name, m.quantization)}
                          className="px-3 py-1 text-xs bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg transition"
                        >
                          Set Active
                        </button>
                      )}
                      <button
                        onClick={() => handleDelete(m.name)}
                        className="p-1.5 text-slate-500 hover:text-rose-400 rounded-lg hover:bg-rose-500/10 transition"
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
          <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl backdrop-blur-md space-y-4">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-amber-400">
              <Zap className="w-4 h-4" /> VRAM / RAM Radial Footprint Gauge
            </h3>

            {/* SVG Ring Meter */}
            <div className="flex items-center justify-center py-2 relative">
              <svg className="w-32 h-32 transform -rotate-90" viewBox="0 0 100 100">
                <circle cx="50" cy="50" r="40" stroke="currentColor" strokeWidth="8" className="text-slate-800" fill="transparent" />
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
                <span className="text-lg font-bold font-mono text-cyan-400">{estimateResult?.estimated_vram_gb} GB</span>
                <span className="text-[10px] text-slate-400 font-mono">VRAM ({vramPercent}%)</span>
              </div>
            </div>

            <div className="space-y-3">
              <div>
                <label className="text-[11px] text-slate-400 block mb-1">Parameter Count (Billions)</label>
                <input
                  type="number"
                  value={estimateParams}
                  onChange={(e) => setEstimateParams(parseFloat(e.target.value) || 0)}
                  className="w-full bg-slate-950 border border-slate-800 rounded-lg px-3 py-2 text-xs text-slate-100 outline-none"
                />
              </div>
              <button
                onClick={calculateEstimate}
                className="w-full py-1.5 bg-slate-800 hover:bg-slate-700 border border-slate-700 text-slate-200 rounded-lg text-xs font-medium transition"
              >
                Estimate Hardware Footprint
              </button>
              {estimateResult && (
                <div className="p-3 bg-slate-950/80 border border-slate-800 rounded-lg text-xs space-y-1">
                  <div className="flex justify-between text-slate-300">
                    <span>Est. VRAM Required:</span>
                    <span className="font-mono text-cyan-400 font-bold">{estimateResult.estimated_vram_gb} GB</span>
                  </div>
                  <div className="flex justify-between text-slate-300">
                    <span>Est. System RAM:</span>
                    <span className="font-mono text-emerald-400 font-bold">{estimateResult.estimated_ram_gb} GB</span>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* Quantization Profiles Reference */}
          <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl backdrop-blur-md space-y-3">
            <h3 className="text-sm font-semibold flex items-center gap-2 text-purple-400">
              <Layers className="w-4 h-4" /> Quantization Presets
            </h3>
            <div className="space-y-2.5 max-h-80 overflow-y-auto pr-1">
              {presets.map((p) => (
                <div key={p.name} className="p-3 bg-slate-950/50 border border-slate-800/80 rounded-lg space-y-1">
                  <div className="flex items-center justify-between">
                    <span className="font-mono font-bold text-xs text-slate-200">{p.name}</span>
                    <span className="text-[10px] px-2 py-0.5 bg-purple-500/10 border border-purple-500/30 text-purple-300 rounded-full">
                      {p.bits_per_weight} bpw
                    </span>
                  </div>
                  <p className="text-[11px] text-slate-400">{p.description}</p>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
