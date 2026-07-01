import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { RefreshCw, Check, Eye, EyeOff, Save, Plus, Trash2 } from 'lucide-react';
import { emit } from '@tauri-apps/api/event';
import { SystemUsage } from '../types';
import { useApp } from '../AppContext';
import ProgressArc from '../components/ui/ProgressArc';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';

const PROVIDERS = [
  { id: 'ollama',    label: 'Ollama',    sub: 'Offline · Free',  color: '#00D97E' },
  { id: 'openai',   label: 'OpenAI',    sub: 'Cloud · API Key', color: '#74AA9C' },
  { id: 'anthropic',label: 'Anthropic', sub: 'Cloud · API Key', color: '#CC785C' },
  { id: 'gemini',   label: 'Gemini',    sub: 'Cloud · API Key', color: '#4285F4' },
  { id: 'deepseek', label: 'DeepSeek',  sub: 'Cloud · API Key', color: '#7C3AED' },
];

const PROVIDER_MODELS: Record<string, string[]> = {
  openai:    ['gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo'],
  anthropic: ['claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022', 'claude-3-opus-20240229'],
  gemini:    ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro'],
  deepseek:  ['deepseek-chat', 'deepseek-coder'],
};

const THEMES = [
  { id: 'frost',       label: 'Frost',        color: '#60A5FA' },
  { id: 'tokyo-storm', label: 'Tokyo Storm',  color: '#7AA2F7' },
  { id: 'abyss',       label: 'Abyss',        color: '#00A896' },
  { id: 'carbon',      label: 'Carbon',       color: '#E2E8F0' },
  { id: 'noir',        label: 'Noir (OLED)',  color: '#38BDF8' },
];

function PasswordInput({ label, value, onChange, placeholder }: { label: string; value: string; onChange: (v: string) => void; placeholder: string }) {
  const [show, setShow] = useState(false);
  return (
    <div>
      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
        {label}
      </label>
      <div style={{ position: 'relative' }}>
        <input
          type={show ? 'text' : 'password'}
          value={value}
          onChange={e => onChange(e.target.value)}
          placeholder={placeholder}
          className="input-base"
          style={{ paddingRight: 36 }}
        />
        <button
          type="button"
          onClick={() => setShow(v => !v)}
          style={{
            position: 'absolute', right: 8, top: '50%', transform: 'translateY(-50%)',
            background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 2,
          }}
        >
          {show ? <EyeOff size={14} /> : <Eye size={14} />}
        </button>
      </div>
    </div>
  );
}

export default function Settings() {
  const { theme, setTheme, systemUsage } = useApp();
  const [provider, setProvider]             = useState(() => localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama');
  const [ollamaHost, setOllamaHost]         = useState(() => localStorage.getItem('OLLAMA_HOST') || 'http://localhost:11434');
  const [brainModel, setBrainModel]         = useState(() => localStorage.getItem('MERIDIAN_MODEL') || 'qwen2.5-coder:7b-instruct-q4_K_M');
  const [visionModel, setVisionModel]       = useState(() => localStorage.getItem('MERIDIAN_VISION_MODEL') || 'moondream:1.8b');
  const [availableModels, setAvailableModels] = useState<string[]>([]);
  const [openaiKey, setOpenaiKey]           = useState(() => localStorage.getItem('OPENAI_API_KEY') || '');
  const [anthropicKey, setAnthropicKey]     = useState(() => localStorage.getItem('ANTHROPIC_API_KEY') || '');
  const [geminiKey, setGeminiKey]           = useState(() => localStorage.getItem('GEMINI_API_KEY') || '');
  const [deepseekKey, setDeepseekKey]       = useState(() => localStorage.getItem('DEEPSEEK_API_KEY') || '');
  const [tavilyKey, setTavilyKey]           = useState(() => localStorage.getItem('TAVILY_API_KEY') || '');
  const [discordToken, setDiscordToken]     = useState(() => localStorage.getItem('DISCORD_BOT_TOKEN') || '');
  const [telegramToken, setTelegramToken]   = useState(() => localStorage.getItem('TELEGRAM_BOT_TOKEN') || '');
  const [telegramChatId, setTelegramChatId] = useState(() => localStorage.getItem('TELEGRAM_CHAT_ID') || '');
  const [whatsappPhone, setWhatsappPhone]   = useState(() => localStorage.getItem('WHATSAPP_PHONE') || '');
  const [gameMode, setGameMode]             = useState(() => localStorage.getItem('GAME_MODE') === 'true');
  const [saveStatus, setSaveStatus]         = useState<'idle' | 'saving' | 'saved' | 'fail'>('idle');

  const [mascotWardrobe, setMascotWardrobe] = useState(() => localStorage.getItem('meridian_mascot_wardrobe') || 'auto');
  const [audioFxEnabled, setAudioFxEnabled] = useState(() => localStorage.getItem('meridian_mascot_audio_fx') !== 'false');
  const [ttsVoice, setTtsVoice]             = useState(() => localStorage.getItem('meridian_tts_voice') || 'M1');
  const [ttsVolume, setTtsVolume]           = useState(() => parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5'));
  const [startupEnabled, setStartupEnabled] = useState(false);

  // MCP state variables
  const [mcpServers, setMcpServers] = useState<Record<string, any>>({});
  const [newServerName, setNewServerName] = useState('');
  const [newServerCommand, setNewServerCommand] = useState('');
  const [newServerArgs, setNewServerArgs] = useState('');
  const [newServerEnv, setNewServerEnv] = useState('');

  // Fetch MCP config on mount
  useEffect(() => {
    fetch('http://localhost:4132/api/mcp/config')
      .then(r => r.json())
      .then(data => {
        if (data && data.mcpServers) {
          setMcpServers(data.mcpServers);
        }
      })
      .catch(() => {});
  }, []);

  const saveMcpConfig = async (servers: Record<string, any>) => {
    try {
      await fetch('http://localhost:4132/api/mcp/config', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ mcpServers: servers })
      });
    } catch (e) {
      console.error("Failed to save MCP config:", e);
    }
  };

  const handleAddMcpServer = async () => {
    if (!newServerName.trim() || !newServerCommand.trim()) return;
    
    // Parse args
    const parsedArgs = newServerArgs
      .split(',')
      .map(s => s.trim())
      .filter(s => s.length > 0);
      
    // Parse env
    const parsedEnv: Record<string, string> = {};
    if (newServerEnv.trim()) {
      newServerEnv.split(',').forEach(kv => {
        const parts = kv.split('=');
        if (parts.length >= 2) {
          parsedEnv[parts[0].trim()] = parts.slice(1).join('=').trim();
        }
      });
    }
    
    const updatedServers = {
      ...mcpServers,
      [newServerName.trim()]: {
        command: newServerCommand.trim(),
        args: parsedArgs,
        env: parsedEnv
      }
    };
    
    setMcpServers(updatedServers);
    
    // Reset form
    setNewServerName('');
    setNewServerCommand('');
    setNewServerArgs('');
    setNewServerEnv('');
    
    await saveMcpConfig(updatedServers);
  };

  const handleRemoveMcpServer = async (name: string) => {
    const updated = { ...mcpServers };
    delete updated[name];
    setMcpServers(updated);
    await saveMcpConfig(updated);
  };

  // Query startup status on mount
  useEffect(() => {
    fetch('http://localhost:4132/api/system/startup')
      .then(r => r.json())
      .then(data => { if (typeof data.enabled === 'boolean') setStartupEnabled(data.enabled); })
      .catch(() => {});
  }, []);

  const handleToggleStartup = async (checked: boolean) => {
    setStartupEnabled(checked);
    try {
      await fetch('http://localhost:4132/api/system/startup', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled: checked })
      });
    } catch { /* noop */ }
  };

  const handleWardrobeChange = (val: string) => {
    setMascotWardrobe(val);
    localStorage.setItem('meridian_mascot_wardrobe', val);
    try {
      emit('mascot-wardrobe-changed', { item: val });
    } catch (e) {
      console.warn("Failed to emit wardrobe change:", e);
    }
  };

  const handleAudioFxChange = (enabled: boolean) => {
    setAudioFxEnabled(enabled);
    localStorage.setItem('meridian_mascot_audio_fx', String(enabled));
  };

  const handleVoiceChange = (val: string) => {
    setTtsVoice(val);
    localStorage.setItem('meridian_tts_voice', val);
  };

  const handleVolumeChange = (val: number) => {
    setTtsVolume(val);
    localStorage.setItem('meridian_ui_volume', String(val));
  };

  // Fetch models on provider change
  useEffect(() => {
    if (provider === 'ollama') {
      fetch(`http://localhost:4132/api/ollama-models?host=${encodeURIComponent(ollamaHost)}`).catch(() => null)
        .then(r => r?.json())
        .then(d => { if (d?.models) setAvailableModels(d.models.map((m: any) => m.name || m)); })
        .catch(() => {});
    } else {
      setAvailableModels(PROVIDER_MODELS[provider] || []);
    }
  }, [provider, ollamaHost]);

  const handleGameMode = async (checked: boolean) => {
    setGameMode(checked);
    localStorage.setItem('GAME_MODE', checked ? 'true' : 'false');
    if ((window as any).__TAURI_INTERNALS__) {
      try { await (window as any).__TAURI_INTERNALS__.invoke('toggle_game_mode', { enabled: checked }); } catch { /* noop */ }
    }
  };

  const handleSave = async (e: React.FormEvent) => {
    e.preventDefault();
    setSaveStatus('saving');
    const entries: Record<string, string> = {
      MERIDIAN_PROVIDER: provider, OLLAMA_HOST: ollamaHost,
      MERIDIAN_MODEL: brainModel, MERIDIAN_VISION_MODEL: visionModel,
      OPENAI_API_KEY: openaiKey, ANTHROPIC_API_KEY: anthropicKey,
      GEMINI_API_KEY: geminiKey, DEEPSEEK_API_KEY: deepseekKey,
      TAVILY_API_KEY: tavilyKey, DISCORD_BOT_TOKEN: discordToken,
      TELEGRAM_BOT_TOKEN: telegramToken, TELEGRAM_CHAT_ID: telegramChatId,
      WHATSAPP_PHONE: whatsappPhone, GAME_MODE: gameMode ? 'true' : 'false',
    };
    Object.entries(entries).forEach(([k, v]) => localStorage.setItem(k, v));

    try {
      const res = await fetch('http://localhost:4132/api/profile/save', {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          meridian_provider: provider, ollama_host: ollamaHost,
          meridian_model: brainModel, meridian_vision_model: visionModel,
          openai_key: openaiKey, anthropic_key: anthropicKey,
          gemini_key: geminiKey, deepseek_key: deepseekKey,
          tavily_key: tavilyKey, discord_token: discordToken,
          telegram_token: telegramToken, telegram_chat_id: telegramChatId,
          whatsapp_phone: whatsappPhone,
        }),
      });
      setSaveStatus(res.ok ? 'saved' : 'fail');
    } catch { setSaveStatus('saved'); /* saved locally */ }
    setTimeout(() => setSaveStatus('idle'), 2500);
  };

  const apiKeyForProvider = (): [string, (v: string) => void, string] | null => {
    const map: Record<string, [string, (v: string) => void, string]> = {
      openai:    [openaiKey,    setOpenaiKey,    'sk-proj-...'],
      anthropic: [anthropicKey, setAnthropicKey, 'sk-ant-...'],
      gemini:    [geminiKey,    setGeminiKey,    'AIzaSy...'],
      deepseek:  [deepseekKey,  setDeepseekKey,  'sk-...'],
    };
    return map[provider] ?? null;
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px', overflow: 'hidden' }}>
      <div style={{ marginBottom: 20, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Settings</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 0', fontFamily: "'JetBrains Mono', monospace" }}>Configuration · Model · Hardware</p>
      </div>

      <form onSubmit={handleSave} style={{ flex: 1, overflowY: 'auto', display: 'grid', gridTemplateColumns: '1fr 260px', gap: 16 }}>
        {/* Left: config */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>

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
                  {PROVIDERS.map(p => {
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
                ) : (() => {
                  const cfg = apiKeyForProvider();
                  if (!cfg) return null;
                  const [val, setter, ph] = cfg;
                  return <PasswordInput label="API Key" value={val} onChange={setter} placeholder={ph} />;
                })()}

                {/* Brain model */}
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Brain Model
                  </label>
                  {availableModels.length > 0 ? (
                    <select value={brainModel} onChange={e => setBrainModel(e.target.value)} className="select-base">
                      {availableModels.map(m => <option key={m} value={m}>{m}</option>)}
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
                  <input type="text" value={visionModel} onChange={e => setVisionModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
                </div>
              </div>
            </div>
          </GlowCard>

          {/* Integrations */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Integrations & Tokens</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <PasswordInput label="Tavily API Key (Web Search)" value={tavilyKey} onChange={setTavilyKey} placeholder="tvly-..." />
              <PasswordInput label="Discord Bot Token" value={discordToken} onChange={setDiscordToken} placeholder="MT..." />
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                <PasswordInput label="Telegram Bot Token" value={telegramToken} onChange={setTelegramToken} placeholder="bot..." />
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Chat ID</label>
                  <input type="text" value={telegramChatId} onChange={e => setTelegramChatId(e.target.value)} placeholder="123456789" className="input-base" />
                </div>
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  WhatsApp Phone (E.164)
                </label>
                <input type="text" value={whatsappPhone} onChange={e => setWhatsappPhone(e.target.value)} placeholder="+1234567890" className="input-base" />
              </div>
            </div>
          </GlowCard>

          {/* MCP Servers Manager */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">MCP Servers Manager</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              
              {/* Active Servers List */}
              {Object.keys(mcpServers).length > 0 ? (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Active Servers
                  </label>
                  {Object.entries(mcpServers).map(([name, srv]) => (
                    <div key={name} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                        <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--accent)' }}>
                          {name} <span style={{ fontSize: 9, color: 'var(--text-dim)', fontWeight: 400, fontFamily: 'JetBrains Mono' }}>({srv.command})</span>
                        </div>
                        {srv.args && srv.args.length > 0 && (
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', wordBreak: 'break-all' }}>
                            args: {srv.args.join(' ')}
                          </div>
                        )}
                        {srv.env && Object.keys(srv.env).length > 0 && (
                          <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                            env: {Object.entries(srv.env).map(([k, v]) => `${k}=${v}`).join(', ')}
                          </div>
                        )}
                      </div>
                      <HoloButton type="button" variant="danger" size="sm" onClick={() => handleRemoveMcpServer(name)}>
                        <Trash2 size={12} />
                      </HoloButton>
                    </div>
                  ))}
                </div>
              ) : (
                <div style={{ fontSize: 11, color: 'var(--text-dim)', padding: '12px 0', textAlign: 'center', border: '1px dashed var(--border-subtle)', borderRadius: 'var(--radius-sm)' }}>
                  No active MCP servers configured. Add one below to extend agent capabilities.
                </div>
              )}

              {/* Add New Server Form */}
              <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
                <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
                  Add Stdio MCP Server
                </label>
                
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                  <div>
                    <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Server ID Name</label>
                    <input type="text" value={newServerName} onChange={e => setNewServerName(e.target.value)} placeholder="e.g. sqlite" className="input-base" style={{ height: 32, fontSize: 11 }} />
                  </div>
                  <div>
                    <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Startup Command</label>
                    <input type="text" value={newServerCommand} onChange={e => setNewServerCommand(e.target.value)} placeholder="e.g. npx" className="input-base" style={{ height: 32, fontSize: 11 }} />
                  </div>
                </div>

                <div>
                  <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Arguments (comma-separated)</label>
                  <input type="text" value={newServerArgs} onChange={e => setNewServerArgs(e.target.value)} placeholder="e.g. -y, @modelcontextprotocol/server-sqlite, --db, test.db" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                </div>

                <div>
                  <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Environment Variables (comma-separated KEY=VAL)</label>
                  <input type="text" value={newServerEnv} onChange={e => setNewServerEnv(e.target.value)} placeholder="e.g. API_KEY=abc, DB_PATH=def" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                </div>

                <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 4 }}>
                  <HoloButton type="button" variant="primary" size="sm" onClick={handleAddMcpServer} disabled={!newServerName.trim() || !newServerCommand.trim()}>
                    <Plus size={12} /> Add Server
                  </HoloButton>
                </div>
              </div>

            </div>
          </GlowCard>

          {/* System */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">System</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              {/* Startup Toggle */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)' }}>
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 2 }}>Launch on Startup</div>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Automatically start Meridian-X when Windows boots.</div>
                </div>
                <input
                  type="checkbox"
                  checked={startupEnabled}
                  onChange={e => handleToggleStartup(e.target.checked)}
                  style={{ width: 16, height: 16, accentColor: 'var(--accent)', cursor: 'pointer' }}
                />
              </div>

              {/* Game Mode */}
              {((window as any).__TAURI_INTERNALS__) && (
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)' }}>
                  <div>
                    <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 2 }}>Desktop Game Mode</div>
                    <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Suspends Alt+M / Alt+V hotkeys during full-screen games.</div>
                  </div>
                  <input
                    type="checkbox"
                    checked={gameMode}
                    onChange={e => handleGameMode(e.target.checked)}
                    style={{ width: 16, height: 16, accentColor: 'var(--accent)', cursor: 'pointer' }}
                  />
                </div>
              )}
            </div>
          </GlowCard>

          {/* Save */}
          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <HoloButton type="submit" variant="primary" size="md" loading={saveStatus === 'saving'}>
              {saveStatus === 'saved' ? <><Check size={14} /> Saved!</> : saveStatus === 'fail' ? 'Save Failed' : <><Save size={14} /> Save Settings</>}
            </HoloButton>
          </div>
        </div>

        {/* Right: hardware + theme */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Hardware Vitals</div>
            <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16, paddingTop: 8 }}>
              <div style={{ textAlign: 'center' }}>
                <ProgressArc value={systemUsage.cpu} size={96} strokeWidth={7} label="CPU" color={systemUsage.cpu > 80 ? 'var(--danger)' : 'var(--accent)'} />
              </div>
              <div style={{ textAlign: 'center' }}>
                <ProgressArc value={systemUsage.ram} size={96} strokeWidth={7} label="RAM" color={systemUsage.ram > 85 ? 'var(--danger)' : 'var(--accent-2)'} />
              </div>
            </div>
          </GlowCard>

          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Theme</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
              {THEMES.map(t => (
                <label key={t.id} style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer', padding: '4px 2px' }}>
                  <input
                    type="radio"
                    name="theme"
                    checked={theme === t.id}
                    onChange={() => setTheme(t.id)}
                    style={{ accentColor: t.color }}
                  />
                  <span style={{ width: 10, height: 10, borderRadius: '50%', background: t.color, flexShrink: 0, boxShadow: theme === t.id ? `0 0 8px ${t.color}` : 'none' }} />
                  <span style={{ fontSize: 12, color: theme === t.id ? 'var(--text-bright)' : 'var(--text-main)', fontWeight: theme === t.id ? 600 : 400 }}>{t.label}</span>
                </label>
              ))}
            </div>
          </GlowCard>

          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Mascot & Audio Customize</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              {/* Wardrobe selection */}
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  Accessories (Wardrobe)
                </label>
                <select 
                  value={mascotWardrobe} 
                  onChange={e => handleWardrobeChange(e.target.value)} 
                  className="select-base"
                >
                  <option value="auto">Auto (Contextual)</option>
                  <option value="none">None</option>
                  <option value="glasses">Glasses</option>
                  <option value="construction_hat">Helmet</option>
                  <option value="detective_hat">Fedora</option>
                  <option value="crown">Crown</option>
                </select>
              </div>

              {/* TTS Voice Selection */}
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                  TTS Voice Engine (Speaker)
                </label>
                <select 
                  value={ttsVoice} 
                  onChange={e => handleVoiceChange(e.target.value)} 
                  className="select-base"
                >
                  <option value="M1">Male 1 (Coordinator)</option>
                  <option value="M2">Male 2 (Assistant)</option>
                  <option value="M3">Male 3 (Calm)</option>
                  <option value="M4">Male 4 (Warm)</option>
                  <option value="M5">Male 5 (Deep)</option>
                  <option value="F1">Female 1 (Soft)</option>
                  <option value="F2">Female 2 (Professional)</option>
                  <option value="F3">Female 3 (Expressive)</option>
                  <option value="F4">Female 4 (Bright)</option>
                  <option value="F5">Female 5 (Crisp)</option>
                </select>
              </div>

              {/* TTS Volume Slider */}
              <div>
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                    Speech Volume
                  </label>
                  <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono' }}>
                    {Math.round(ttsVolume * 100)}%
                  </span>
                </div>
                <input 
                  type="range" 
                  min="0" 
                  max="1" 
                  step="0.05"
                  value={ttsVolume} 
                  onChange={e => handleVolumeChange(parseFloat(e.target.value))} 
                  style={{ width: '100%', accentColor: 'var(--accent)', cursor: 'pointer' }}
                />
              </div>

              {/* Sound FX Toggle */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)' }}>
                <div>
                  <div style={{ fontSize: 11, fontWeight: 600, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 2 }}>Mascot Sound FX</div>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Enable ambient state-change audio.</div>
                </div>
                <input
                  type="checkbox"
                  checked={audioFxEnabled}
                  onChange={e => handleAudioFxChange(e.target.checked)}
                  style={{ width: 16, height: 16, accentColor: 'var(--accent)', cursor: 'pointer' }}
                />
              </div>
            </div>
          </GlowCard>
        </div>
      </form>
    </div>
  );
}
