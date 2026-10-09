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

            {/* Brain model */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Brain Model
              </label>
              {availableBrainModels.length > 0 ? (
                <select value={brainModel} onChange={e => setBrainModel(e.target.value)} className="select-base">
                  {availableBrainModels.map(m => <option key={m} value={m}>{m}</option>)}
                </select>
              ) : (
                <input type="text" value={brainModel} onChange={e => setBrainModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              )}
            </div>

            {/* Vision model */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Vision Model (Ollama)
              </label>
              {availableOllamaModels.length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                  <select value={visionModel} onChange={e => setVisionModel(e.target.value)} className="select-base">
                    {filterVisionModels(availableOllamaModels).map(m => <option key={m} value={m}>{m}</option>)}
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
                    Show all models (disable vision filtering)
                  </label>
                </div>
              ) : (
                <input type="text" value={visionModel} onChange={e => setVisionModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              )}
            </div>

            {/* Auditor model */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Auditor & Local Fallback Model (Ollama)
              </label>
              {availableOllamaModels.length > 0 ? (
                <select value={auditorModel} onChange={e => setAuditorModel(e.target.value)} className="select-base">
                  {availableOllamaModels.map(m => <option key={m} value={m}>{m}</option>)}
                </select>
              ) : (
                <input type="text" value={auditorModel} onChange={e => setAuditorModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              )}
            </div>

            {/* Embedding Model */}
            <div>
              <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                Embedding Model (Ollama Vector RAG)
              </label>
              {availableOllamaModels.length > 0 ? (
                <select value={embeddingModel} onChange={e => setEmbeddingModel(e.target.value)} className="select-base">
                  {availableOllamaModels.map(m => <option key={m} value={m}>{m}</option>)}
                </select>
              ) : (
                <input type="text" value={embeddingModel} onChange={e => setEmbeddingModel(e.target.value)} placeholder="e.g. nomic-embed-text" className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              )}
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
