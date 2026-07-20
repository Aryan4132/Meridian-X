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
  deepseek:  ['deepseek-v4-pro', 'deepseek-v4-flash', 'deepseek-chat', 'deepseek-coder'],
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
  const { theme, setTheme, systemUsage, setModelName, gameMode, setGameMode } = useApp();
  const [provider, setProvider]             = useState(() => localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama');
  const [ollamaHost, setOllamaHost]         = useState(() => localStorage.getItem('OLLAMA_HOST') || 'http://localhost:11434');
  const [brainModel, setBrainModel]         = useState(() => localStorage.getItem('MERIDIAN_MODEL') || 'qwen2.5-coder:7b-instruct-q4_K_M');
  const [visionModel, setVisionModel]       = useState(() => localStorage.getItem('MERIDIAN_VISION_MODEL') || 'moondream:1.8b');
  const [availableBrainModels, setAvailableBrainModels] = useState<string[]>([]);
  const [availableOllamaModels, setAvailableOllamaModels] = useState<string[]>([]);
  const [showAllVisionModels, setShowAllVisionModels] = useState(() => localStorage.getItem('meridian_show_all_vision_models') === 'true');
  const [openaiKey, setOpenaiKey]           = useState(() => localStorage.getItem('OPENAI_API_KEY') || '');
  const [anthropicKey, setAnthropicKey]     = useState(() => localStorage.getItem('ANTHROPIC_API_KEY') || '');
  const [geminiKey, setGeminiKey]           = useState(() => localStorage.getItem('GEMINI_API_KEY') || '');
  const [deepseekKey, setDeepseekKey]       = useState(() => localStorage.getItem('DEEPSEEK_API_KEY') || '');
  const [tavilyKey, setTavilyKey]           = useState(() => localStorage.getItem('TAVILY_API_KEY') || '');
  const [discordToken, setDiscordToken]     = useState(() => localStorage.getItem('DISCORD_BOT_TOKEN') || '');
  const [telegramToken, setTelegramToken]   = useState(() => localStorage.getItem('TELEGRAM_BOT_TOKEN') || '');
  const [telegramChatId, setTelegramChatId] = useState(() => localStorage.getItem('TELEGRAM_CHAT_ID') || '');
  const [saveStatus, setSaveStatus]         = useState<'idle' | 'saving' | 'saved' | 'fail'>('idle');

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

  // Additional dynamic settings state variables
  const [auditorModel, setAuditorModel] = useState(() => localStorage.getItem('meridian_auditor_model') || 'qwen2.5-coder:1.5b-instruct-q8_0');
  const [wakewordThreshold, setWakewordThreshold] = useState(() => parseFloat(localStorage.getItem('wakeword_threshold') || '0.6'));
  const [wakewordModel, setWakewordModel] = useState(() => localStorage.getItem('wakeword_model_filename') || 'hey_meridian.onnx');
  const [wakewordPhrase, setWakewordPhrase] = useState(() => localStorage.getItem('wakeword_phrase') || 'Hey Meridian');
  const [sttModelSize, setSttModelSize] = useState(() => localStorage.getItem('stt_model_size') || 'base');
  const [sttSilenceTimeout, setSttSilenceTimeout] = useState(() => parseFloat(localStorage.getItem('stt_silence_timeout') || '1.0'));
  const [sttVadThreshold, setSttVadThreshold] = useState(() => parseFloat(localStorage.getItem('stt_vad_threshold') || '300.0'));
  const [sttMaxDuration, setSttMaxDuration] = useState(() => parseFloat(localStorage.getItem('stt_max_duration') || '8.0'));
  const [browserWidth, setBrowserWidth] = useState(() => parseInt(localStorage.getItem('browser_viewport_width') || '1280'));
  const [browserHeight, setBrowserHeight] = useState(() => parseInt(localStorage.getItem('browser_viewport_height') || '800'));
  const [cpuWarn, setCpuWarn] = useState(() => parseFloat(localStorage.getItem('cpu_warn_threshold') || '85.0'));
  const [ramWarn, setRamWarn] = useState(() => parseFloat(localStorage.getItem('ram_warn_threshold') || '88.0'));
  const [diskWarn, setDiskWarn] = useState(() => parseFloat(localStorage.getItem('disk_warn_threshold') || '90.0'));
  const [distractions, setDistractions] = useState(() => localStorage.getItem('distraction_sites') || 'facebook.com, instagram.com, youtube.com, twitter.com, reddit.com');
  const [workspaceConfig, setWorkspaceConfig] = useState<any>({});
  const [workspaceModel, setWorkspaceModel] = useState('');
  const [workspaceDirectives, setWorkspaceDirectives] = useState('');

  const [smtpServer, setSmtpServer] = useState(() => localStorage.getItem('SMTP_SERVER') || 'smtp.gmail.com');
  const [smtpPort, setSmtpPort]     = useState(() => parseInt(localStorage.getItem('SMTP_PORT') || '587'));
  const [smtpEmail, setSmtpEmail]   = useState(() => localStorage.getItem('SMTP_EMAIL') || '');
  const [smtpPassword, setSmtpPassword] = useState(() => localStorage.getItem('SMTP_PASSWORD') || '');
  const [imapServer, setImapServer] = useState(() => localStorage.getItem('IMAP_SERVER') || 'imap.gmail.com');
  const [mongodbUri, setMongodbUri] = useState(() => localStorage.getItem('MONGODB_URI') || 'mongodb://localhost:27017/meridian_kg');
  const [logLevel, setLogLevel]     = useState(() => localStorage.getItem('MERIDIAN_LOG_LEVEL') || 'INFO');

  // Fetch profile configurations on mount to hydrate local storage & states
  useEffect(() => {
    fetch('http://localhost:4132/api/profile/all')
      .then(r => r.json())
      .then(data => {
        if (data) {
          if (data.meridian_provider) { setProvider(data.meridian_provider); localStorage.setItem('MERIDIAN_PROVIDER', data.meridian_provider); }
          if (data.ollama_host) { setOllamaHost(data.ollama_host); localStorage.setItem('OLLAMA_HOST', data.ollama_host); }
          if (data.meridian_model) { setBrainModel(data.meridian_model); localStorage.setItem('MERIDIAN_MODEL', data.meridian_model); setModelName(data.meridian_model); }
          if (data.meridian_vision_model) { setVisionModel(data.meridian_vision_model); localStorage.setItem('MERIDIAN_VISION_MODEL', data.meridian_vision_model); }
          if (data.openai_key) { setOpenaiKey(data.openai_key); localStorage.setItem('OPENAI_API_KEY', data.openai_key); }
          if (data.anthropic_key) { setAnthropicKey(data.anthropic_key); localStorage.setItem('ANTHROPIC_API_KEY', data.anthropic_key); }
          if (data.gemini_key) { setGeminiKey(data.gemini_key); localStorage.setItem('GEMINI_API_KEY', data.gemini_key); }
          if (data.deepseek_key) { setDeepseekKey(data.deepseek_key); localStorage.setItem('DEEPSEEK_API_KEY', data.deepseek_key); }
          if (data.tavily_key) { setTavilyKey(data.tavily_key); localStorage.setItem('TAVILY_API_KEY', data.tavily_key); }
          if (data.discord_token) { setDiscordToken(data.discord_token); localStorage.setItem('DISCORD_BOT_TOKEN', data.discord_token); }
          if (data.telegram_token) { setTelegramToken(data.telegram_token); localStorage.setItem('TELEGRAM_BOT_TOKEN', data.telegram_token); }
          if (data.telegram_chat_id) { setTelegramChatId(data.telegram_chat_id); localStorage.setItem('TELEGRAM_CHAT_ID', data.telegram_chat_id); }
          
          if (data.meridian_auditor_model) { setAuditorModel(data.meridian_auditor_model); localStorage.setItem('meridian_auditor_model', data.meridian_auditor_model); }
          if (data.meridian_voice) { setTtsVoice(data.meridian_voice); localStorage.setItem('meridian_tts_voice', data.meridian_voice); }
          if (data.wakeword_threshold) { setWakewordThreshold(data.wakeword_threshold); localStorage.setItem('wakeword_threshold', String(data.wakeword_threshold)); }
          if (data.wakeword_model_filename) { setWakewordModel(data.wakeword_model_filename); localStorage.setItem('wakeword_model_filename', data.wakeword_model_filename); }
          if (data.wakeword_phrase) { setWakewordPhrase(data.wakeword_phrase); localStorage.setItem('wakeword_phrase', data.wakeword_phrase); }
          if (data.stt_model_size) { setSttModelSize(data.stt_model_size); localStorage.setItem('stt_model_size', data.stt_model_size); }
          if (data.stt_silence_timeout) { setSttSilenceTimeout(data.stt_silence_timeout); localStorage.setItem('stt_silence_timeout', String(data.stt_silence_timeout)); }
          if (data.stt_vad_threshold) { setSttVadThreshold(data.stt_vad_threshold); localStorage.setItem('stt_vad_threshold', String(data.stt_vad_threshold)); }
          if (data.stt_max_duration) { setSttMaxDuration(data.stt_max_duration); localStorage.setItem('stt_max_duration', String(data.stt_max_duration)); }
          if (data.browser_viewport_width) { setBrowserWidth(data.browser_viewport_width); localStorage.setItem('browser_viewport_width', String(data.browser_viewport_width)); }
          if (data.browser_viewport_height) { setBrowserHeight(data.browser_viewport_height); localStorage.setItem('browser_viewport_height', String(data.browser_viewport_height)); }
          if (data.cpu_warn_threshold) { setCpuWarn(data.cpu_warn_threshold); localStorage.setItem('cpu_warn_threshold', String(data.cpu_warn_threshold)); }
          if (data.ram_warn_threshold) { setRamWarn(data.ram_warn_threshold); localStorage.setItem('ram_warn_threshold', String(data.ram_warn_threshold)); }
          if (data.disk_warn_threshold) { setDiskWarn(data.disk_warn_threshold); localStorage.setItem('disk_warn_threshold', String(data.disk_warn_threshold)); }
            if (data.distraction_sites) {
              const listStr = Array.isArray(data.distraction_sites) ? data.distraction_sites.join(', ') : data.distraction_sites;
              setDistractions(listStr);
              localStorage.setItem('distraction_sites', listStr);
            }
            if (data.smtp_server) { setSmtpServer(data.smtp_server); localStorage.setItem('SMTP_SERVER', data.smtp_server); }
            if (data.smtp_port) { setSmtpPort(data.smtp_port); localStorage.setItem('SMTP_PORT', String(data.smtp_port)); }
            if (data.smtp_email) { setSmtpEmail(data.smtp_email); localStorage.setItem('SMTP_EMAIL', data.smtp_email); }
            if (data.smtp_password) { setSmtpPassword(data.smtp_password); localStorage.setItem('SMTP_PASSWORD', data.smtp_password); }
            if (data.imap_server) { setImapServer(data.imap_server); localStorage.setItem('IMAP_SERVER', data.imap_server); }
            if (data.mongodb_uri) { setMongodbUri(data.mongodb_uri); localStorage.setItem('MONGODB_URI', data.mongodb_uri); }
            if (data.meridian_log_level) { setLogLevel(data.meridian_log_level); localStorage.setItem('MERIDIAN_LOG_LEVEL', data.meridian_log_level); }
          }
        })
        .catch(() => {});
    }, []);

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

  // Query startup status and workspace config on mount
  useEffect(() => {
    fetch('http://localhost:4132/api/system/startup')
      .then(r => r.json())
      .then(data => { if (typeof data.enabled === 'boolean') setStartupEnabled(data.enabled); })
      .catch(() => {});
      
    fetch('http://localhost:4132/api/workspace/config')
      .then(r => r.json())
      .then(data => {
        if (data.status === 'success' && data.config) {
          setWorkspaceConfig(data.config);
          setWorkspaceModel(data.config.brain_model || '');
          setWorkspaceDirectives(data.config.custom_directives || '');
        }
      })
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

  // Fetch Ollama models for Vision and Auditor
  useEffect(() => {
    fetch(`http://localhost:4132/api/provider-models?provider=ollama&host=${encodeURIComponent(ollamaHost)}`).catch(() => null)
      .then(r => r?.json())
      .then(d => {
        if (d?.models) {
          setAvailableOllamaModels(d.models.map((m: any) => m.name || m));
        }
      })
      .catch(() => {});
  }, [ollamaHost]);

  // Fetch Brain models based on selected provider and key
  useEffect(() => {
    let key = '';
    if (provider === 'openai') key = openaiKey;
    else if (provider === 'anthropic') key = anthropicKey;
    else if (provider === 'gemini') key = geminiKey;
    else if (provider === 'deepseek') key = deepseekKey;

    const url = `http://localhost:4132/api/provider-models?provider=${provider}&host=${encodeURIComponent(ollamaHost)}&api_key=${encodeURIComponent(key)}`;
    fetch(url).catch(() => null)
      .then(r => r?.json())
      .then(d => {
        if (d?.models) {
          setAvailableBrainModels(d.models.map((m: any) => m.name || m));
        }
      })
      .catch(() => {});
  }, [provider, ollamaHost, openaiKey, anthropicKey, geminiKey, deepseekKey]);

  // Set default models when provider changes to prevent model mismatch
  useEffect(() => {
    if (provider !== 'ollama') {
      const models = PROVIDER_MODELS[provider] || [];
      if (models.length > 0 && !models.includes(brainModel)) {
        setBrainModel(models[0]);
      }
    }
  }, [provider]);

  // Adjust selected brain model if availableBrainModels are loaded and current model is invalid
  useEffect(() => {
    if (availableBrainModels.length > 0 && !availableBrainModels.includes(brainModel)) {
      const otherProviderModels = Object.values(PROVIDER_MODELS).flat();
      if (otherProviderModels.includes(brainModel) || provider === 'ollama') {
        setBrainModel(availableBrainModels[0]);
      }
    }
  }, [availableBrainModels]);

  const filterVisionModels = (models: string[]) => {
    if (showAllVisionModels) return models;
    const filtered = models.filter(m => {
      const name = m.toLowerCase();
      return (
        name.includes('vision') ||
        name.includes('ocr') ||
        name.includes('moondream') ||
        name.includes('llava') ||
        name.includes('minicpm') ||
        name.includes('paligemma') ||
        name.includes('bakllava') ||
        name.includes('vl') ||
        name.endsWith('-v') ||
        name.includes('-v-') ||
        name.includes('-v1') ||
        name.includes('-v2') ||
        name.includes('-v3') ||
        name.includes('-v4')
      );
    });
    return filtered.length > 0 ? filtered : models;
  };

  const handleGameMode = async (checked: boolean) => {
    setGameMode(checked);
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
      GAME_MODE: gameMode ? 'true' : 'false',
      meridian_auditor_model: auditorModel,
      meridian_tts_voice: ttsVoice,
      wakeword_threshold: String(wakewordThreshold),
      wakeword_model_filename: wakewordModel,
      wakeword_phrase: wakewordPhrase,
      stt_model_size: sttModelSize,
      stt_silence_timeout: String(sttSilenceTimeout),
      stt_vad_threshold: String(sttVadThreshold),
      stt_max_duration: String(sttMaxDuration),
      browser_viewport_width: String(browserWidth),
      browser_viewport_height: String(browserHeight),
      cpu_warn_threshold: String(cpuWarn),
      ram_warn_threshold: String(ramWarn),
      disk_warn_threshold: String(diskWarn),
      distraction_sites: distractions,
      SMTP_SERVER: smtpServer,
      SMTP_PORT: String(smtpPort),
      SMTP_EMAIL: smtpEmail,
      SMTP_PASSWORD: smtpPassword,
      IMAP_SERVER: imapServer,
      MONGODB_URI: mongodbUri,
      MERIDIAN_LOG_LEVEL: logLevel,
    };
    Object.entries(entries).forEach(([k, v]) => localStorage.setItem(k, v));

    // Parse distraction sites list
    const parsedDistractions = distractions
      .split(',')
      .map(s => s.trim())
      .filter(s => s.length > 0);

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
          meridian_auditor_model: auditorModel,
          meridian_voice: ttsVoice,
          wakeword_threshold: wakewordThreshold,
          wakeword_model_filename: wakewordModel,
          wakeword_phrase: wakewordPhrase,
          stt_model_size: sttModelSize,
          stt_silence_timeout: sttSilenceTimeout,
          stt_vad_threshold: sttVadThreshold,
          stt_max_duration: sttMaxDuration,
          browser_viewport_width: browserWidth,
          browser_viewport_height: browserHeight,
          cpu_warn_threshold: cpuWarn,
          ram_warn_threshold: ramWarn,
          disk_warn_threshold: diskWarn,
          distraction_sites: parsedDistractions,
          smtp_server: smtpServer,
          smtp_port: smtpPort,
          smtp_email: smtpEmail,
          smtp_password: smtpPassword,
          imap_server: imapServer,
          mongodb_uri: mongodbUri,
          meridian_log_level: logLevel,
        }),
      });
      if (res.ok) {
        try {
          await fetch('http://localhost:4132/api/workspace/config', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              config: {
                ...workspaceConfig,
                brain_model: workspaceModel || undefined,
                custom_directives: workspaceDirectives || undefined
              }
            })
          });
        } catch { /* noop */ }
        setModelName(brainModel);
        setSaveStatus('saved');
      } else {
        setSaveStatus('fail');
      }
    } catch {
      setSaveStatus('fail');
    }
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
            </div>
          </GlowCard>

          {/* Email Configuration */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Email Configuration (SMTP & IMAP)</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Email Address</label>
                  <input type="email" value={smtpEmail} onChange={e => setSmtpEmail(e.target.value)} placeholder="your_email@gmail.com" className="input-base" />
                </div>
                <PasswordInput label="SMTP App-Specific Password" value={smtpPassword} onChange={setSmtpPassword} placeholder="16-character app password" />
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: '2fr 1fr 2fr', gap: 8 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Server</label>
                  <input type="text" value={smtpServer} onChange={e => setSmtpServer(e.target.value)} placeholder="smtp.gmail.com" className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>SMTP Port</label>
                  <input type="number" value={smtpPort} onChange={e => setSmtpPort(parseInt(e.target.value) || 587)} placeholder="587" className="input-base" />
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>IMAP Server</label>
                  <input type="text" value={imapServer} onChange={e => setImapServer(e.target.value)} placeholder="imap.gmail.com" className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
                </div>
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
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Wake Word ONNX Filename</label>
                <input type="text" value={wakewordModel} onChange={e => setWakewordModel(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Wake Word Phrase Text</label>
                <input type="text" value={wakewordPhrase} onChange={e => setWakewordPhrase(e.target.value)} className="input-base" />
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>VAD Silence Timeout (sec)</label>
                <input type="number" min="0.2" max="5.0" step="0.1" value={sttSilenceTimeout} onChange={e => setSttSilenceTimeout(parseFloat(e.target.value))} className="input-base" />
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>VAD Amplitude Threshold</label>
                <input type="number" min="50" max="2000" step="50" value={sttVadThreshold} onChange={e => setSttVadThreshold(parseFloat(e.target.value))} className="input-base" />
              </div>
              <div style={{ gridColumn: 'span 2' }}>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Max STT Recording Duration (sec)</label>
                <input type="number" min="2.0" max="60.0" step="1.0" value={sttMaxDuration} onChange={e => setSttMaxDuration(parseFloat(e.target.value))} className="input-base" />
              </div>
            </div>
          </GlowCard>

          {/* Proactive Guard Config */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Proactive Monitoring & System Guard</div>
            <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>CPU Warn (%)</label>
                  <input type="number" min="10" max="95" value={cpuWarn} onChange={e => setCpuWarn(parseFloat(e.target.value))} className="input-base" />
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>RAM Warn (%)</label>
                  <input type="number" min="10" max="95" value={ramWarn} onChange={e => setRamWarn(parseFloat(e.target.value))} className="input-base" />
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Disk Warn (%)</label>
                  <input type="number" min="10" max="95" value={diskWarn} onChange={e => setDiskWarn(parseFloat(e.target.value))} className="input-base" />
                </div>
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Distraction Websites Blocklist (comma-separated)</label>
                <input type="text" value={distractions} onChange={e => setDistractions(e.target.value)} className="input-base" />
              </div>
            </div>
          </GlowCard>

          {/* Browser Tool Config */}
          <GlowCard className="glass" style={{ padding: 16 }}>
            <div className="section-label">Web Browser Tool Settings</div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12 }}>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Viewport Width (px)</label>
                <input type="number" min="320" max="3840" value={browserWidth} onChange={e => setBrowserWidth(parseInt(e.target.value))} className="input-base" />
              </div>
              <div>
                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Viewport Height (px)</label>
                <input type="number" min="240" max="2160" value={browserHeight} onChange={e => setBrowserHeight(parseInt(e.target.value))} className="input-base" />
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
                  {Object.entries(mcpServers).map(([name, srv]: [string, any]) => (
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

              {/* Log Level & MongoDB URI */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: 8, borderTop: '1px solid var(--border-subtle)', paddingTop: 10 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>Log Level</label>
                  <select value={logLevel} onChange={e => setLogLevel(e.target.value)} className="select-base" style={{ height: 32, fontSize: 11 }}>
                    <option value="DEBUG">DEBUG</option>
                    <option value="INFO">INFO</option>
                    <option value="WARNING">WARNING</option>
                    <option value="ERROR">ERROR</option>
                    <option value="CRITICAL">CRITICAL</option>
                  </select>
                </div>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>MongoDB URI</label>
                  <input type="text" value={mongodbUri} onChange={e => setMongodbUri(e.target.value)} placeholder="mongodb://localhost:27017/meridian_kg" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: "'JetBrains Mono', monospace" }} />
                </div>
              </div>
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
