import React from 'react';
import { Eye, EyeOff, FolderOpen, Plus, Trash2 } from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';

export interface VoiceTabProps {
  voiceResponseEnabled: boolean;
  handleToggleVoiceResponse: () => void;
  duplexActive: boolean;
  handleToggleDuplex: () => void;
  continuousActive: boolean;
  continuousRemaining: number;
  handleTriggerContinuousWindow: () => void;
  biometricsCount: number;
  handleResetBiometrics: () => void;
  sttModelSize: string;
  setSttModelSize: (v: string) => void;
  wakewordThreshold: number;
  setWakewordThreshold: (v: number) => void;
  wakewordModel: string;
  setWakewordModel: (v: string) => void;
  fileInputRef: React.RefObject<HTMLInputElement | null>;
  handleFileInputChange: (e: React.ChangeEvent<HTMLInputElement>) => void;
  handleBrowseOnnxFile: () => void;
  vaultKeys: any[];
  keysUnlocked: boolean;
  showVaultSecrets: boolean;
  setShowVaultSecrets: (v: boolean | ((prev: boolean) => boolean)) => void;
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
}

export default function VoiceTab({
  voiceResponseEnabled,
  handleToggleVoiceResponse,
  duplexActive,
  handleToggleDuplex,
  continuousActive,
  continuousRemaining,
  handleTriggerContinuousWindow,
  biometricsCount,
  handleResetBiometrics,
  sttModelSize,
  setSttModelSize,
  wakewordThreshold,
  setWakewordThreshold,
  wakewordModel,
  setWakewordModel,
  fileInputRef,
  handleFileInputChange,
  handleBrowseOnnxFile,
  vaultKeys,
  keysUnlocked,
  showVaultSecrets,
  setShowVaultSecrets,
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
}: VoiceTabProps) {
  return (
    <>
      {/* Day 5 — Real-Time Voice Duplex & Biometrics Control Center */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Real-Time Voice Controls & Biometrics (AST-15, AST-08, JARVIS-03)</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>

          {/* Voice Output Response Toggle */}
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 6 }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Voice Assistant Speech Output</span>
              <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: voiceResponseEnabled ? 'rgba(52, 211, 153, 0.15)' : 'rgba(239, 68, 68, 0.15)', color: voiceResponseEnabled ? 'var(--success)' : 'var(--danger)' }}>
                {voiceResponseEnabled ? 'ENABLED' : 'MUTED'}
              </span>
            </div>
            <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
              Toggles synthesized voice responses. Turn OFF to keep responses text-only.
            </div>
            <button
              type="button"
              onClick={handleToggleVoiceResponse}
              className="btn-secondary"
              style={{ fontSize: 11, marginTop: 4, cursor: 'pointer', border: voiceResponseEnabled ? '1px solid var(--danger)' : '1px solid var(--success)', color: voiceResponseEnabled ? 'var(--danger)' : 'var(--success)' }}
            >
              {voiceResponseEnabled ? '🔇 Mute Voice Output' : '🔊 Enable Voice Output'}
            </button>
          </div>

          {/* Full-Duplex Real-Time Voice Streaming */}
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 6 }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Full-Duplex Voice Engine</span>
              <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: duplexActive ? 'color-mix(in srgb, var(--success) 15%, transparent)' : 'var(--bg-surface)', color: duplexActive ? 'var(--success)' : 'var(--text-dim)' }}>
                {duplexActive ? 'ACTIVE (50ms VAD)' : 'IDLE'}
              </span>
            </div>
            <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
              Sub-100ms VAD barge-in speech interruption mid-sentence.
            </div>
            <button
              type="button"
              onClick={handleToggleDuplex}
              className="btn-secondary"
              style={{ fontSize: 11, marginTop: 4, cursor: 'pointer' }}
            >
              {duplexActive ? 'Stop Duplex Session' : '🎙️ Start Duplex Session'}
            </button>
          </div>

          {/* Continuous Conversation Window */}
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 6 }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Continuous Listening Window</span>
              <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: continuousActive ? 'var(--accent-muted)' : 'var(--bg-surface)', color: continuousActive ? 'var(--accent)' : 'var(--text-dim)' }}>
                {continuousActive ? `LISTENING (${continuousRemaining}s)` : 'OFF'}
              </span>
            </div>
            <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
              10-second active follow-up listening window without wake word.
            </div>
            <button
              type="button"
              onClick={handleTriggerContinuousWindow}
              className="btn-secondary"
              style={{ fontSize: 11, marginTop: 4, cursor: 'pointer' }}
            >
              ⚡ Trigger 10s Continuous Window
            </button>
          </div>

          {/* Voice Biometric Identity Verification */}
          <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 6 }}>
            <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)', display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <span>Voice Biometrics & Identity</span>
              <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: biometricsCount > 0 ? 'color-mix(in srgb, var(--success) 15%, transparent)' : 'var(--bg-surface)', color: biometricsCount > 0 ? 'var(--success)' : 'var(--text-dim)' }}>
                {biometricsCount > 0 ? `${biometricsCount} ENROLLED` : 'NO VOICEPRINTS'}
              </span>
            </div>
            <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
              128-dim acoustic vector verification blocking background voices.
            </div>
            <button
              type="button"
              onClick={handleResetBiometrics}
              className="btn-secondary"
              style={{ fontSize: 11, marginTop: 4, cursor: 'pointer' }}
            >
              🗑️ Reset Enrolled Voiceprints
            </button>
          </div>

        </div>
      </GlowCard>

      {/* Voice & Wake Word Advanced Config */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div className="section-label">Voice & Wake Word Settings</div>
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>STT Whisper Model</label>
            <select value={sttModelSize} onChange={e => setSttModelSize(e.target.value)} className="select-base">
              <option value="base">base (Fastest)</option>
              <option value="small">small</option>
              <option value="medium">medium</option>
              <option value="large-v3">large-v3</option>
              <option value="turbo">turbo (Accurate)</option>
            </select>
          </div>
          <div>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Wake Word Score Threshold</label>
            <input type="number" min="0.1" max="1.0" step="0.05" value={wakewordThreshold} onChange={e => setWakewordThreshold(parseFloat(e.target.value))} className="input-base" />
          </div>
          <div style={{ gridColumn: 'span 2' }}>
            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Wake Word ONNX Model (Path / Filename)</label>
            <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
              <input
                type="text"
                value={wakewordModel}
                onChange={e => setWakewordModel(e.target.value)}
                className="input-base"
                placeholder="hey_meridian.onnx or C:/path/to/model.onnx"
                style={{ fontFamily: "'JetBrains Mono', monospace", flex: 1 }}
              />
              <input
                type="file"
                ref={fileInputRef}
                onChange={handleFileInputChange}
                accept=".onnx"
                style={{ display: 'none' }}
              />
              <HoloButton
                type="button"
                variant="ghost"
                size="sm"
                onClick={handleBrowseOnnxFile}
                title="Browse local disk for .onnx model"
                className="flex-shrink-0"
              >
                <FolderOpen size={14} />
                Browse
              </HoloButton>
            </div>
            <span style={{ fontSize: 9, color: 'var(--text-dim)', marginTop: 4, display: 'block' }}>
              Select a custom OpenWakeWord ONNX file or keep empty for default.
            </span>
          </div>
        </div>
      </GlowCard>

      {/* Dynamic API Keys & Custom Voice/Model Credentials */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
          <div className="section-label" style={{ margin: 0 }}>Custom Secret Keys & Custom Providers (AES-256 Vault)</div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
            <span style={{ fontSize: 10, fontFamily: 'JetBrains Mono', color: 'var(--accent)' }}>
              {vaultKeys.length} REGISTERED
            </span>
            <button
              type="button"
              onClick={() => setShowVaultSecrets(v => !v)}
              style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 2 }}
              title={showVaultSecrets ? 'Mask secrets' : 'Reveal secrets'}
            >
              {showVaultSecrets ? <EyeOff size={14} /> : <Eye size={14} />}
            </button>
          </div>
        </div>

        {/* Existing Vault Keys List */}
        {vaultKeys.length > 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: 6, marginBottom: 16 }}>
            {vaultKeys.map(k => (
              <div key={k.env_var} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '8px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                    <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{k.name}</span>
                    <span style={{ fontSize: 9, padding: '2px 6px', background: 'var(--accent-muted)', color: 'var(--accent)', borderRadius: 'var(--radius-sm)', fontFamily: 'JetBrains Mono' }}>
                      {k.category || 'Audio & Voice'}
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
            No custom API keys registered in encrypted vault yet. Add ElevenLabs, Deepgram, Whisper Cloud or any custom tool key below.
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
              <input type="text" value={vkName} onChange={e => setVkName(e.target.value)} placeholder="e.g. ElevenLabs / Deepgram" className="input-base" style={{ height: 32, fontSize: 11 }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Env Var Name</label>
              <input type="text" value={vkEnvVar} onChange={e => setVkEnvVar(e.target.value.toUpperCase())} placeholder="e.g. ELEVENLABS_API_KEY" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 8 }}>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>API Key / Secret Token</label>
              <input type="password" value={vkSecret} onChange={e => setVkSecret(e.target.value)} placeholder="xi-... / dg-..." className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
            </div>
            <div>
              <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Category</label>
              <select value={vkCategory} onChange={e => setVkCategory(e.target.value)} className="select-base" style={{ height: 32, fontSize: 11 }}>
                <option value="Audio & Voice">Audio & Voice</option>
                <option value="LLM Provider">LLM Provider</option>
                <option value="Search & Web">Search & Web</option>
                <option value="Vision & Media">Vision & Media</option>
                <option value="Vector DB">Vector DB</option>
                <option value="Custom Tool">Custom Tool</option>
              </select>
            </div>
          </div>

          <div>
            <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Base URL / Custom Endpoint (Optional)</label>
            <input type="text" value={vkBaseUrl} onChange={e => setVkBaseUrl(e.target.value)} placeholder="e.g. https://api.elevenlabs.io/v1 (Optional)" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
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
