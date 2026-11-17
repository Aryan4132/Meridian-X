import React from 'react';
import { Eye, EyeOff, Plus, Trash2 } from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';
import PasswordInput from './PasswordInput';

export interface AiModelsTabProps {
  providers: readonly { id: string; label: string; sub: string; color: string }[];
  provider: string;
  setProvider: (p: string) => void;
  ollamaHost: string;
  setOllamaHost: (v: string) => void;
  customBaseUrl: string;
  setCustomBaseUrl: (v: string) => void;
  customModel: string;
  setCustomModel: (v: string) => void;
  customApiKey: string;
  setCustomApiKey: (v: string) => void;
  keysUnlocked: boolean;
  requestUnlock: () => void;
  apiKeyForProvider: () => [string, (v: string) => void, string] | null;
  modelSource: string;
  setModelSource: (v: string) => void;
  brainModel: string;
  setBrainModel: (v: string) => void;
  availableBrainModels: string[];
  visionModel: string;
  setVisionModel: (v: string) => void;
  availableOllamaModels: string[];
  filterVisionModels: (models: string[]) => string[];
  showAllVisionModels: boolean;
  setShowAllVisionModels: (v: boolean) => void;
  auditorModel: string;
  setAuditorModel: (v: string) => void;
  embeddingModel: string;
  setEmbeddingModel: (v: string) => void;
  contextTokenLimit: number;
  setContextTokenLimit: (v: number) => void;
  workspaceModel: string;
  setWorkspaceModel: (v: string) => void;
  workspaceDirectives: string;
  setWorkspaceDirectives: (v: string) => void;
  vaultKeys: any[];
  showVaultSecrets: boolean;
  setShowVaultSecrets: (v: boolean | ((prev: boolean) => boolean)) => void;
  fetchVaultKeys: (unmask?: boolean) => void;
  handleDeleteVaultKey: (k: string) => void;
  vkName: string;
  setVkName: (v: string) => void;
  vkEnvVar: string;
  setVkEnvVar: (v: string) => void;
  vkSecret: string;
  setVkSecret: (v: string) => void;
  vkCategory: string;
  setVkCategory: (v: string) => void;
  vkBaseUrl: string;
  setVkBaseUrl: (v: string) => void;
  handleAddVaultKey: () => void;
  isKeyLockUnlocked: () => boolean;
}

const CLOUD_VISION_PRESETS: Record<string, string[]> = {
  openai: ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo'],
  gemini: ['gemini-2.5-flash', 'gemini-1.5-flash', 'gemini-2.0-flash', 'gemini-2.5-pro'],
  anthropic: ['claude-3-7-sonnet-20250219', 'claude-3-5-sonnet-20241022'],
  groq: ['llama-3.2-11b-vision-preview', 'llama-3.2-90b-vision-preview'],
  mistral: ['pixtral-12b-2409', 'pixtral-large-latest'],
  openrouter: ['openai/gpt-4o', 'anthropic/claude-3.5-sonnet', 'google/gemini-flash-1.5'],
  deepseek: ['deepseek-chat', 'gpt-4o-mini', 'gemini-2.5-flash', 'claude-3-5-haiku-20241022'],
};
const FALLBACK_CLOUD_VISION = ['gpt-4o', 'gpt-4o-mini', 'gemini-2.5-flash', 'claude-3-5-sonnet-20241022', 'llama-3.2-11b-vision-preview'];

const CLOUD_AUDITOR_PRESETS: Record<string, string[]> = {
  deepseek: ['deepseek-chat', 'deepseek-reasoner'],
  openai: ['gpt-4o-mini', 'gpt-4o', 'o3-mini'],
  gemini: ['gemini-2.5-flash', 'gemini-2.0-flash', 'gemini-1.5-flash'],
  anthropic: ['claude-3-5-haiku-20241022', 'claude-3-5-sonnet-20241022'],
  groq: ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile'],
  mistral: ['mistral-small-latest', 'codestral-latest'],
  openrouter: ['deepseek/deepseek-r1', 'meta-llama/llama-3.3-70b-instruct'],
};
const FALLBACK_CLOUD_AUDITOR = ['deepseek-chat', 'gpt-4o-mini', 'gemini-2.5-flash', 'claude-3-5-haiku-20241022', 'llama-3.1-8b-instant'];

const CLOUD_EMBEDDING_PRESETS = [
  'text-embedding-3-small',
  'text-embedding-3-large',
  'fastembed-bge-small-en-v1.5',
  'bge-small-en-v1.5',
];

const DEFAULT_LOCAL_EMBEDDINGS = [
  'nomic-embed-text',
  'nomic-embed-text-v2-moe:latest',
  'bge-m3',
  'all-minilm',
];

const RECOMMENDED_SLM_PACK = [
  { tag: 'llama3.2:3b', name: 'Llama 3.2 3B', role: 'Brain / Fast Agent', size: '2.0 GB', vram: '4GB VRAM / 8GB RAM' },
  { tag: 'qwen2.5:3b', name: 'Qwen 2.5 3B', role: 'Brain / Code & Math', size: '1.9 GB', vram: '4GB VRAM / 8GB RAM' },
  { tag: 'granite4.1:3b', name: 'Granite 4.1 3B', role: 'Auditor & Safety Guard', size: '2.1 GB', vram: '4GB VRAM / 8GB RAM' },
  { tag: 'qwen2-vl:2b', name: 'Qwen 2-VL 2B', role: 'Local Vision & OCR', size: '1.5 GB', vram: '3GB VRAM / 6GB RAM' },
  { tag: 'nomic-embed-text', name: 'Nomic Embed Text', role: 'Vector Embeddings', size: '274 MB', vram: '512MB RAM' },
];

export default function AiModelsTab({
  providers,
  provider,
  setProvider,
  ollamaHost,
  setOllamaHost,
  customBaseUrl,
  setCustomBaseUrl,
  customModel,
  setCustomModel,
  customApiKey,
  setCustomApiKey,
  keysUnlocked,
  requestUnlock,
  apiKeyForProvider,
  modelSource,
  setModelSource,
  brainModel,
  setBrainModel,
  availableBrainModels,
  visionModel,
  setVisionModel,
  availableOllamaModels,
  filterVisionModels,
  showAllVisionModels,
  setShowAllVisionModels,
  auditorModel,
  setAuditorModel,
  embeddingModel,
  setEmbeddingModel,
  contextTokenLimit,
  setContextTokenLimit,
  workspaceModel,
  setWorkspaceModel,
  workspaceDirectives,
  setWorkspaceDirectives,
  vaultKeys,
  showVaultSecrets,
  setShowVaultSecrets,
  fetchVaultKeys,
  handleDeleteVaultKey,
  vkName,
  setVkName,
  vkEnvVar,
  setVkEnvVar,
  vkSecret,
  setVkSecret,
  vkCategory,
  setVkCategory,
  vkBaseUrl,
  setVkBaseUrl,
  handleAddVaultKey,
  isKeyLockUnlocked,
}: AiModelsTabProps) {
  const [pullingModel, setPullingModel] = React.useState<string | null>(null);
  const [pullStatus, setPullStatus] = React.useState<string>('');

  const handlePullRecommended = async (tag: string) => {
    setPullingModel(tag);
    setPullStatus(`Pulling ${tag} in background...`);
    try {
      const res = await fetch('/api/ollama/pull', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: tag }),
      });
      if (res.ok) {
        setPullStatus(`✓ ${tag} downloaded successfully!`);
        window.dispatchEvent(new Event('meridian-model-changed'));
      } else {
        setPullStatus(`✕ Could not pull ${tag}. Check Ollama daemon.`);
      }
    } catch {
      setPullStatus(`✕ Failed connecting to Ollama.`);
    } finally {
      setTimeout(() => {
        setPullingModel(null);
        setPullStatus('');
      }, 4000);
    }
  };

  return (
    <>
      {/* AI Config */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">AI Configuration</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          {/* Provider grid */}
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Intelligence Provider
            </label>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 6 }}>
              {providers.map(p => {
                const active = provider === p.id;
                return (
                  <button key={p.id} type="button" onClick={() => setProvider(p.id)} style={{
                    padding: '8px 4px', borderRadius: 'var(--radius-sm)',
                    border: active ? `1px solid ${p.color}` : '1px solid var(--border-subtle)',
                    background: active ? `${p.color}12` : 'var(--bg-surface)',
                    cursor: 'pointer', textAlign: 'center', transition: 'all 0.15s ease',
                  }}>
                    <div style={{ fontSize: 11, fontWeight: 600, color: active ? p.color : 'var(--text-main)', marginBottom: 2 }}>{p.label}</div>
                    <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>{p.sub}</div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Provider-specific */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
            {provider === 'ollama' ? (
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  Ollama Host URL
                </label>
                <input type="text" value={ollamaHost} onChange={e => setOllamaHost(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              </div>
            ) : provider === 'custom' ? (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Custom Endpoint Base URL (llama.cpp / vLLM / LocalAI / HuggingFace)
                  </label>
                  <input
                    type="text"
                    value={customBaseUrl}
                    onChange={e => setCustomBaseUrl(e.target.value)}
                    placeholder="http://localhost:8000/v1 or https://api-inference.huggingface.co/v1"
                    className="input-base"
                    style={{ fontFamily: "'JetBrains Mono', monospace" }}
                  />
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Custom Model ID / Name
                  </label>
                  <input
                    type="text"
                    value={customModel}
                    onChange={e => setCustomModel(e.target.value)}
                    placeholder="mistralai/Mistral-7B-Instruct-v0.1 or custom-model"
                    className="input-base"
                    style={{ fontFamily: "'JetBrains Mono', monospace" }}
                  />
                </div>
                <PasswordInput
                  label="Custom API Key / Token (Optional for Local Servers)"
                  value={customApiKey}
                  onChange={setCustomApiKey}
                  placeholder="hf_... or leave blank for local servers"
                  requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock}
                />
              </div>
            ) : (() => {
              const cfg = apiKeyForProvider();
              if (!cfg) return null;
              const [val, setter, ph] = cfg;
              return <PasswordInput label="API Key" value={val} onChange={setter} placeholder={ph} requireUnlock keysUnlocked={keysUnlocked} onRequestUnlock={requestUnlock} />;
            })()}

            {/* Model Execution Mode */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Model Execution Mode
              </label>
              <select value={modelSource} onChange={e => setModelSource(e.target.value)} className="select-base">
                <option value="local">Local Mode (Enables local multi-agent features & HTP)</option>
                <option value="api">Cloud/API Mode (Instant streaming, bypasses local task decomposition)</option>
              </select>
            </div>

            {/* Cloud Provider Quick Alignment Banner */}
            {provider !== 'ollama' && (
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                padding: '8px 12px',
                background: 'rgba(56, 189, 248, 0.06)',
                borderRadius: 8,
                border: '1px solid rgba(56, 189, 248, 0.18)',
                gap: 8,
              }}>
                <div style={{ fontSize: 11, color: 'var(--text-main)', display: 'flex', alignItems: 'center', gap: 6 }}>
                  <span style={{ color: 'var(--accent)' }}>⚡</span>
                  <span>Active Provider: <strong style={{ color: 'var(--accent)', textTransform: 'capitalize' }}>{provider}</strong></span>
                </div>
                <button
                  type="button"
                  onClick={() => {
                    const brain = (CLOUD_AUDITOR_PRESETS[provider] || [brainModel])[0] || brainModel;
                    const auditor = CLOUD_AUDITOR_PRESETS[provider]?.[0] || 'deepseek-chat';
                    const vision = CLOUD_VISION_PRESETS[provider]?.[0] || 'gpt-4o-mini';
                    const emb = provider === 'openai' ? 'text-embedding-3-small' : (embeddingModel || 'fastembed-bge-small-en-v1.5');
                    
                    if (brain) {
                      setBrainModel(brain);
                      localStorage.setItem('MERIDIAN_MODEL', brain);
                    }
                    setAuditorModel(auditor);
                    localStorage.setItem('meridian_auditor_model', auditor);
                    setVisionModel(vision);
                    localStorage.setItem('MERIDIAN_VISION_MODEL', vision);
                    setEmbeddingModel(emb);
                    localStorage.setItem('EMBEDDING_MODEL', emb);
                  }}
                  className="btn-ghost"
                  style={{
                    fontSize: 10,
                    padding: '3px 10px',
                    borderRadius: 4,
                    cursor: 'pointer',
                    color: 'var(--accent)',
                    border: '1px solid rgba(56, 189, 248, 0.3)',
                    background: 'rgba(56, 189, 248, 0.1)',
                    fontFamily: 'JetBrains Mono',
                  }}
                >
                  ⚡ Align All Models to {provider.toUpperCase()}
                </button>
              </div>
            )}

            {/* Brain model */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Brain Model
              </label>
              {availableBrainModels.length > 0 ? (
                <select value={brainModel} onChange={e => setBrainModel(e.target.value)} className="select-base">
                  {availableBrainModels.map(m => <option key={m} value={m}>{m}</option>)}
                  {brainModel && !availableBrainModels.includes(brainModel) && (
                    <option value={brainModel}>{brainModel}</option>
                  )}
                </select>
              ) : (
                <input type="text" value={brainModel} onChange={e => setBrainModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              )}
            </div>

            {/* Vision model */}
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  Vision Model
                </label>
                {provider !== 'ollama' && (
                  <span style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                    Cloud & Local Supported
                  </span>
                )}
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                <select
                  value={visionModel}
                  onChange={e => {
                    setVisionModel(e.target.value);
                    localStorage.setItem('MERIDIAN_VISION_MODEL', e.target.value);
                  }}
                  className="select-base"
                >
                  <optgroup label={`Cloud Vision (${provider.toUpperCase()})`}>
                    {(CLOUD_VISION_PRESETS[provider] || FALLBACK_CLOUD_VISION).map(m => (
                      <option key={`cloud-vision-${m}`} value={m}>{m}</option>
                    ))}
                  </optgroup>
                  <optgroup label="Local Ollama Vision Models">
                    {filterVisionModels(availableOllamaModels.length > 0 ? availableOllamaModels : ['qwen2-vl:2b', 'moondream2']).map(m => (
                      <option key={`local-vision-${m}`} value={m}>{m}</option>
                    ))}
                  </optgroup>
                  {visionModel &&
                    !(CLOUD_VISION_PRESETS[provider] || FALLBACK_CLOUD_VISION).includes(visionModel) &&
                    !availableOllamaModels.includes(visionModel) && (
                      <optgroup label="Custom / Active Model">
                        <option value={visionModel}>{visionModel}</option>
                      </optgroup>
                    )}
                </select>
                <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 10, color: 'var(--text-dim)', cursor: 'pointer', marginTop: 2 }}>
                  <input
                    type="checkbox"
                    checked={showAllVisionModels}
                    onChange={e => {
                      setShowAllVisionModels(e.target.checked);
                      localStorage.setItem('meridian_show_all_vision_models', String(e.target.checked));
                    }}
                  />
                  Show all Ollama models in vision list
                </label>
              </div>
            </div>

            {/* Auditor model */}
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  Auditor & Fallback Model
                </label>
                {provider !== 'ollama' && auditorModel !== (CLOUD_AUDITOR_PRESETS[provider]?.[0] || 'deepseek-chat') && (
                  <button
                    type="button"
                    onClick={() => {
                      const def = CLOUD_AUDITOR_PRESETS[provider]?.[0] || (availableBrainModels[0] || 'deepseek-chat');
                      setAuditorModel(def);
                      localStorage.setItem('meridian_auditor_model', def);
                    }}
                    style={{ fontSize: 9, color: 'var(--accent)', background: 'transparent', border: 'none', cursor: 'pointer', fontFamily: 'JetBrains Mono' }}
                  >
                    ⚡ Use {provider} Cloud Auditor
                  </button>
                )}
              </div>
              <select
                value={auditorModel}
                onChange={e => {
                  setAuditorModel(e.target.value);
                  localStorage.setItem('meridian_auditor_model', e.target.value);
                }}
                className="select-base"
              >
                <optgroup label={`Cloud / ${provider.toUpperCase()} Auditor Models`}>
                  {Array.from(new Set([
                    ...(availableBrainModels.length > 0 ? availableBrainModels : []),
                    ...(CLOUD_AUDITOR_PRESETS[provider] || FALLBACK_CLOUD_AUDITOR),
                  ])).map(m => (
                    <option key={`cloud-auditor-${m}`} value={m}>{m}</option>
                  ))}
                </optgroup>
                <optgroup label="Local Ollama Models">
                  {(availableOllamaModels.length > 0 ? availableOllamaModels : ['granite4.1:3b', 'qwen2.5:3b', 'llama3.2:3b']).map(m => (
                    <option key={`local-auditor-${m}`} value={m}>{m}</option>
                  ))}
                </optgroup>
                {auditorModel &&
                  !availableBrainModels.includes(auditorModel) &&
                  !(CLOUD_AUDITOR_PRESETS[provider] || FALLBACK_CLOUD_AUDITOR).includes(auditorModel) &&
                  !availableOllamaModels.includes(auditorModel) && (
                    <optgroup label="Custom / Active Model">
                      <option value={auditorModel}>{auditorModel}</option>
                    </optgroup>
                  )}
              </select>
            </div>

            {/* Embedding Model */}
            <div>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 }}>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  Embedding Model (Vector RAG)
                </label>
                {provider === 'openai' && embeddingModel !== 'text-embedding-3-small' && (
                  <button
                    type="button"
                    onClick={() => {
                      setEmbeddingModel('text-embedding-3-small');
                      localStorage.setItem('EMBEDDING_MODEL', 'text-embedding-3-small');
                    }}
                    style={{ fontSize: 9, color: 'var(--accent)', background: 'transparent', border: 'none', cursor: 'pointer', fontFamily: 'JetBrains Mono' }}
                  >
                    ⚡ Use OpenAI Embeddings
                  </button>
                )}
              </div>
              <select
                value={embeddingModel}
                onChange={e => {
                  setEmbeddingModel(e.target.value);
                  localStorage.setItem('EMBEDDING_MODEL', e.target.value);
                }}
                className="select-base"
              >
                <optgroup label="Cloud & In-Memory Embeddings">
                  {CLOUD_EMBEDDING_PRESETS.map(m => (
                    <option key={`cloud-emb-${m}`} value={m}>{m}</option>
                  ))}
                </optgroup>
                <optgroup label="Local Ollama Embeddings">
                  {Array.from(new Set([
                    ...availableOllamaModels.filter(m => m.toLowerCase().includes('embed') || m.toLowerCase().includes('nomic') || m.toLowerCase().includes('bge') || m.toLowerCase().includes('minilm')),
                    ...DEFAULT_LOCAL_EMBEDDINGS,
                    ...availableOllamaModels,
                  ])).map(m => (
                    <option key={`local-emb-${m}`} value={m}>{m}</option>
                  ))}
                </optgroup>
                {embeddingModel &&
                  !CLOUD_EMBEDDING_PRESETS.includes(embeddingModel) &&
                  !availableOllamaModels.includes(embeddingModel) &&
                  !DEFAULT_LOCAL_EMBEDDINGS.includes(embeddingModel) && (
                    <optgroup label="Custom / Active Model">
                      <option value={embeddingModel}>{embeddingModel}</option>
                    </optgroup>
                  )}
              </select>
            </div>

            {/* Token Context Limit */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Max Token Context Limit
              </label>
              <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                <select
                  value={[4096, 8192, 16384, 32768, 65536, 131072].includes(contextTokenLimit) ? contextTokenLimit : 'custom'}
                  onChange={e => {
                    if (e.target.value !== 'custom') {
                      const val = parseInt(e.target.value);
                      setContextTokenLimit(val);
                      localStorage.setItem('context_token_limit', String(val));
                    }
                  }}
                  className="select-base"
                  style={{ flex: 1 }}
                >
                  <option value="4096">4,096 tokens (4k)</option>
                  <option value="8192">8,192 tokens (8k - Default)</option>
                  <option value="16384">16,384 tokens (16k)</option>
                  <option value="32768">32,768 tokens (32k)</option>
                  <option value="65536">65,536 tokens (64k)</option>
                  <option value="131072">131,072 tokens (128k)</option>
                  <option value="custom">Custom Limit...</option>
                </select>
                <input
                  type="number"
                  min="1024"
                  max="1048576"
                  step="1024"
                  value={contextTokenLimit}
                  onChange={e => {
                    const val = parseInt(e.target.value) || 8192;
                    setContextTokenLimit(val);
                    localStorage.setItem('context_token_limit', String(val));
                  }}
                  className="input-base"
                  style={{ width: 110, fontFamily: "'JetBrains Mono', monospace" }}
                />
              </div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 4, fontFamily: "'JetBrains Mono', monospace" }}>
                Warning threshold triggers compression at 80% ({Math.round(contextTokenLimit * 0.8).toLocaleString()} tokens).
              </div>
            </div>
          </div>
        </div>
      </GlowCard>

      {/* Recommended Local SLM Models (1-Click Optimization Pack) */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 }}>
          <div>
            <div className="section-label" style={{ marginBottom: 2 }}>Curated Local SLM Models (Offline Optimized)</div>
            <div style={{ fontSize: 11, color: 'var(--text-dim)' }}>
              Lightweight models ($\le$3.2B) tuned for instant inference, low RAM footprint, and multi-format tool calling.
            </div>
          </div>
          {pullStatus && (
            <div style={{ fontSize: 11, color: pullStatus.startsWith('✓') ? '#10b981' : '#f59e0b', fontFamily: 'JetBrains Mono' }}>
              {pullStatus}
            </div>
          )}
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: 10 }}>
          {RECOMMENDED_SLM_PACK.map(model => {
            const isInstalled = availableOllamaModels.some(m => m.toLowerCase().startsWith(model.tag.toLowerCase()));
            const isPulling = pullingModel === model.tag;

            return (
              <div
                key={model.tag}
                style={{
                  padding: '10px 12px',
                  borderRadius: 8,
                  background: isInstalled ? 'rgba(56, 189, 248, 0.05)' : 'rgba(255, 255, 255, 0.02)',
                  border: isInstalled ? '1px solid rgba(56, 189, 248, 0.25)' : '1px solid rgba(255, 255, 255, 0.07)',
                  display: 'flex',
                  flexDirection: 'column',
                  justifyContent: 'space-between',
                  gap: 8,
                }}
              >
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <span style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-main)' }}>{model.name}</span>
                    <span
                      style={{
                        fontSize: 9,
                        padding: '1px 6px',
                        borderRadius: 4,
                        background: isInstalled ? 'rgba(16, 185, 129, 0.15)' : 'rgba(255, 255, 255, 0.05)',
                        color: isInstalled ? '#10b981' : 'var(--text-dim)',
                        fontFamily: 'JetBrains Mono',
                      }}
                    >
                      {isInstalled ? '✓ Ready' : model.size}
                    </span>
                  </div>
                  <div style={{ fontSize: 10, color: 'var(--accent)', marginTop: 2, fontFamily: 'JetBrains Mono' }}>
                    {model.role}
                  </div>
                  <div style={{ fontSize: 9, color: 'var(--text-dim)', marginTop: 4 }}>
                    RAM: {model.vram}
                  </div>
                </div>

                <div style={{ display: 'flex', gap: 6, marginTop: 4 }}>
                  {isInstalled ? (
                    <button
                      type="button"
                      onClick={() => {
                        if (model.role.includes('Vision')) {
                          setVisionModel(model.tag);
                          localStorage.setItem('MERIDIAN_VISION_MODEL', model.tag);
                        } else if (model.role.includes('Auditor')) {
                          setAuditorModel(model.tag);
                          localStorage.setItem('meridian_auditor_model', model.tag);
                        } else if (model.role.includes('Vector')) {
                          setEmbeddingModel(model.tag);
                          localStorage.setItem('EMBEDDING_MODEL', model.tag);
                        } else {
                          setBrainModel(model.tag);
                          localStorage.setItem('MERIDIAN_MODEL', model.tag);
                        }
                      }}
                      className="btn-ghost"
                      style={{ flex: 1, fontSize: 10, padding: '4px 8px', borderRadius: 4, cursor: 'pointer', color: 'var(--accent)' }}
                    >
                      Set Active
                    </button>
                  ) : (
                    <button
                      type="button"
                      disabled={isPulling}
                      onClick={() => handlePullRecommended(model.tag)}
                      className="btn-ghost"
                      style={{
                        flex: 1,
                        fontSize: 10,
                        padding: '4px 8px',
                        borderRadius: 4,
                        cursor: isPulling ? 'not-allowed' : 'pointer',
                        color: isPulling ? '#f59e0b' : 'var(--text-main)',
                        border: '1px solid rgba(255, 255, 255, 0.15)',
                      }}
                    >
                      {isPulling ? 'Pulling...' : '📥 1-Click Pull'}
                    </button>
                  )}
                </div>
              </div>
            );
          })}
        </div>
      </GlowCard>

      {/* Workspace Configuration override (.meridian.json) */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Workspace Override Configuration (.meridian.json)</div>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Workspace Brain Model Override
            </label>
            <input
              type="text"
              value={workspaceModel}
              onChange={e => setWorkspaceModel(e.target.value)}
              placeholder="e.g. qwen2.5-coder:7b (empty to use global default)"
              className="input-base"
              style={{ fontFamily: "'JetBrains Mono', monospace" }}
            />
          </div>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Workspace Custom Directives
            </label>
            <textarea
              value={workspaceDirectives}
              onChange={e => setWorkspaceDirectives(e.target.value)}
              placeholder="Enter system prompt instructions, custom agent constraints or rules specific to this workspace..."
              className="input-base"
              rows={4}
              style={{ resize: 'vertical', minHeight: 80 }}
            />
          </div>
        </div>
      </GlowCard>

      {/* Universal Encrypted Secret Vault inside AI Models tab */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
          <div className="section-label" style={{ margin: 0 }}>🔐 Universal API Key & Encrypted Secret Vault</div>
          <button
            type="button"
            onClick={() => {
              if (showVaultSecrets) { setShowVaultSecrets(false); fetchVaultKeys(false); }
              else if (keysUnlocked || isKeyLockUnlocked()) { setShowVaultSecrets(true); fetchVaultKeys(true); }
              else requestUnlock();
            }}
            style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--accent)', fontSize: 11, display: 'flex', alignItems: 'center', gap: 4, fontFamily: 'JetBrains Mono' }}
          >
            {showVaultSecrets ? <EyeOff size={12} /> : <Eye size={12} />}
            {showVaultSecrets ? 'Mask Keys' : 'Unmask Keys'}
          </button>
        </div>

        {/* List of active custom keys */}
        {vaultKeys.length > 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 8, marginBottom: 16 }}>
            {vaultKeys.map(k => (
              <div key={k.env_var} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{k.name}</span>
                    <span style={{ fontSize: 9, padding: '2px 6px', background: 'var(--accent-muted)', color: 'var(--accent)', borderRadius: 'var(--radius-sm)', fontFamily: 'JetBrains Mono' }}>
                      {k.category || 'LLM Provider'}
                    </span>
                    <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', fontWeight: 600 }}>
                      ${k.env_var}
                    </span>
                  </div>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                    Key: {(keysUnlocked && showVaultSecrets) ? k.api_key : '••••••••••••••••'} {k.base_url && `· Base: ${k.base_url}`}
                  </div>
                </div>
                <HoloButton type="button" variant="danger" size="sm" onClick={() => handleDeleteVaultKey(k.env_var)}>
                  <Trash2 size={12} />
                </HoloButton>
              </div>
            ))}
          </div>
        ) : (
          <div style={{ fontSize: 11, color: 'var(--text-dim)', padding: '10px 0', textAlign: 'center', border: '1px dashed var(--border-subtle)', borderRadius: 'var(--radius-sm)', marginBottom: 16 }}>
            No custom API keys registered in encrypted vault yet. Add Groq, OpenRouter, Mistral, SerpAPI or any custom tool key below.
          </div>
        )}

        {/* Add New Key Form */}
        <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
          <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
            + Add Dynamic API Key or Cloud Secret
          </label>

          <div style={{ display: 'grid', gridTemplateColumns: '1.2fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Service Name</label>
              <input type="text" value={vkName} onChange={e => setVkName(e.target.value)} placeholder="e.g. Groq Cloud / OpenRouter" className="input-base" style={{ height: 32, fontSize: 11 }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Env Var Name</label>
              <input type="text" value={vkEnvVar} onChange={e => setVkEnvVar(e.target.value.toUpperCase())} placeholder="e.g. GROQ_API_KEY" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>API Key / Secret Token</label>
              <input type="password" value={vkSecret} onChange={e => setVkSecret(e.target.value)} placeholder="gsk_... / sk-or-v1-..." className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Category</label>
              <select value={vkCategory} onChange={e => setVkCategory(e.target.value)} className="select-base" style={{ height: 32, fontSize: 11 }}>
                <option value="LLM Provider">LLM Provider</option>
                <option value="Search & Web">Search & Web</option>
                <option value="Audio & Voice">Audio & Voice</option>
                <option value="Vision & Media">Vision & Media</option>
                <option value="Vector DB">Vector DB</option>
                <option value="Custom Tool">Custom Tool</option>
              </select>
            </div>
          </div>

          <div>
            <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Base URL / Custom Endpoint (Optional)</label>
            <input type="text" value={vkBaseUrl} onChange={e => setVkBaseUrl(e.target.value)} placeholder="e.g. https://api.groq.com/openai/v1 (Optional)" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
          </div>

          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 4 }}>
            <HoloButton type="button" variant="primary" size="sm" onClick={handleAddVaultKey} disabled={!vkName.trim() || !vkEnvVar.trim() || !vkSecret.trim()}>
              <Plus size={12} /> Save Secret to Vault
            </HoloButton>
          </div>
        </div>
      </GlowCard>
    </>
  );
}
