import React, { useState, useEffect } from 'react';
import { invoke } from '@tauri-apps/api/core';
import { motion, AnimatePresence } from 'motion/react';
import { RefreshCw, Check, Eye, EyeOff, Save, Plus, Trash2, Cpu, Sparkles, Mic, ShieldCheck, Plug, FolderOpen, Search, Download, Loader2 } from 'lucide-react';
import { emit } from '@tauri-apps/api/event';
import { API_BASE_URL, getApiBaseUrl, getApiKey } from '../config';
import { SystemUsage } from '../types';
import { useApp } from '../AppContext';
import { useLowRamMode } from '../hooks/useMemoryOptimizer';
import ProgressArc from '../components/ui/ProgressArc';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';

const SETTINGS_TABS = [
  { id: 'models', label: 'AI Models', icon: Cpu },
  { id: 'mascot', label: 'Mascot & Style', icon: Sparkles },
  { id: 'voice', label: 'Voice & Audio', icon: Mic },
  { id: 'guard', label: 'System Guard', icon: ShieldCheck },
  { id: 'integrations', label: 'Integrations', icon: Plug },
] as const;

const PROVIDERS = [
  { id: 'ollama', label: 'Ollama', sub: 'Local · Offline', color: '#00D97E' },
  { id: 'groq', label: 'Groq', sub: 'Ultra-Fast Cloud', color: '#F55036' },
  { id: 'openrouter', label: 'OpenRouter', sub: '100+ Cloud Models', color: '#6366F1' },
  { id: 'mistral', label: 'Mistral', sub: 'Cloud · API Key', color: '#FF7000' },
  { id: 'openai', label: 'OpenAI', sub: 'Cloud · API Key', color: '#74AA9C' },
  { id: 'anthropic', label: 'Anthropic', sub: 'Cloud · API Key', color: '#CC785C' },
  { id: 'gemini', label: 'Gemini', sub: 'Cloud · API Key', color: '#4285F4' },
  { id: 'deepseek', label: 'DeepSeek', sub: 'Cloud · API Key', color: '#7C3AED' },
  { id: 'custom', label: 'Custom Endpoint', sub: 'llama.cpp · vLLM · HF', color: '#E8A020' },
];

const PROVIDER_MODELS: Record<string, string[]> = {
  groq: ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant', 'mixtral-8x7b-32768', 'gemma2-9b-it'],
  openrouter: ['anthropic/claude-3.5-sonnet', 'openai/gpt-4o', 'meta-llama/llama-3.3-70b-instruct', 'deepseek/deepseek-r1'],
  mistral: ['mistral-large-latest', 'codestral-latest', 'pixtral-12b-2409', 'mistral-small-latest'],
  openai: ['gpt-4o', 'gpt-4o-mini', 'gpt-4-turbo', 'o3-mini'],
  anthropic: ['claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022', 'claude-3-opus-20240229'],
  gemini: ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-2.0-flash-exp'],
  deepseek: ['deepseek-chat', 'deepseek-reasoner', 'deepseek-coder'],
};

const THEMES = [
  { id: 'cyberslate',   label: 'Classic Cyber Slate', icon: '🪐', sub: 'Tactile Slate & Solar Amber',        font: "'IBM Plex Mono', monospace", mode: 'Dark',  swatches: ['#0A0C10', '#E8A020', '#1E232E'] },
  { id: 'artdeco',      label: 'Art Deco Luxury',     icon: '🏛️', sub: 'Obsidian Black & Metallic Gold',    font: "'Playfair Display', serif",  mode: 'Dark',  swatches: ['#050505', '#D4AF37', '#1E3D59'] },
  { id: 'neobrutalism', label: 'Neobrutalism',        icon: '⚡', sub: 'Light Cream & Stark Black Shadows', font: "'Space Grotesk', sans-serif",mode: 'Light', swatches: ['#FFFDF5', '#FFDE59', '#000000'] },
  { id: 'cyberpunk',    label: 'Cyberpunk Neon',      icon: '🌆', sub: 'Dark Void & Neon Magenta/Cyan',   font: "'Orbitron', sans-serif",     mode: 'Dark',  swatches: ['#030308', '#FF0055', '#00F0FF'] },
  { id: 'retro',        label: 'Retro Synthwave',     icon: '👾', sub: '80s CRT Terminal & Vaporwave',   font: "'VT323', monospace",         mode: 'Dark',  swatches: ['#0A0414', '#FF71CE', '#05FFA1'] },
  { id: 'ink',          label: 'Ink & Slate',          icon: '🖋️', sub: 'Warm Charcoal & Muted Indigo',   font: "'Inter', sans-serif",        mode: 'Dark',  swatches: ['#111113', '#818CF8', '#34D399'] },
  { id: 'nordic',       label: 'Nordic Frost',        icon: '❄️', sub: 'Midnight Slate & Sky Blue',      font: "'DM Sans', sans-serif",      mode: 'Dark',  swatches: ['#0B0F17', '#38BDF8', '#A7F3D0'] },
  { id: 'maximalism',   label: 'Maximalism',          icon: '🌈', sub: 'High-Energy Vibrant Magenta & Lime',font: "'Syne', sans-serif",        mode: 'Dark',  swatches: ['#0D021A', '#FF007A', '#76FF03'] },
  { id: 'paper',        label: 'Paper & Ink',         icon: '📜', sub: 'Warm Off-White Editorial Linen',    font: "'Lora', serif",              mode: 'Light', swatches: ['#F4F2EC', '#D95338', '#2D6A4F'] },
  { id: 'sakura',       label: 'Sakura Blossom',      icon: '🌸', sub: 'Soft Pastel Blush & Rose Quartz',   font: "'Outfit', sans-serif",       mode: 'Light', swatches: ['#FFF5F7', '#E85D75', '#6DB193'] },
  { id: 'solaris',      label: 'Solaris Light',       icon: '☀️', sub: 'Clean Solar White & Cobalt Blue',   font: "'DM Sans', sans-serif",      mode: 'Light', swatches: ['#F4F6FB', '#2563EB', '#059669'] },
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
  const { theme, setTheme, islandPosition, setIslandPosition, systemUsage, setModelName, gameMode, setGameMode } = useApp();
  const { isLowRam, toggleLowRamMode } = useLowRamMode();
  const [activeCategory, setActiveCategory] = useState<'models' | 'mascot' | 'voice' | 'guard' | 'integrations'>('models');
  const [provider, setProvider] = useState(() => localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama');
  const [modelSource, setModelSource] = useState(() => localStorage.getItem('MERIDIAN_MODEL_SOURCE') || (provider === 'ollama' ? 'local' : 'api'));
  const [ollamaHost, setOllamaHost] = useState(() => localStorage.getItem('OLLAMA_HOST') || 'http://localhost:11434');
  const [brainModel, setBrainModel] = useState(() => localStorage.getItem('MERIDIAN_MODEL') || 'for ex: model name');
  const [visionModel, setVisionModel] = useState(() => localStorage.getItem('MERIDIAN_VISION_MODEL') || 'for ex: model name');
  const [embeddingModel, setEmbeddingModel] = useState(() => localStorage.getItem('EMBEDDING_MODEL') || localStorage.getItem('embedding_model') || 'for ex: model name');
  const [availableBrainModels, setAvailableBrainModels] = useState<string[]>([]);
  const [availableOllamaModels, setAvailableOllamaModels] = useState<string[]>([]);
  const [showAllVisionModels, setShowAllVisionModels] = useState(() => localStorage.getItem('meridian_show_all_vision_models') === 'true');
  const [groqKey, setGroqKey] = useState(() => localStorage.getItem('GROQ_API_KEY') || '');
  const [openrouterKey, setOpenrouterKey] = useState(() => localStorage.getItem('OPENROUTER_API_KEY') || '');
  const [mistralKey, setMistralKey] = useState(() => localStorage.getItem('MISTRAL_API_KEY') || '');
  const [openaiKey, setOpenaiKey] = useState(() => localStorage.getItem('OPENAI_API_KEY') || '');
  const [anthropicKey, setAnthropicKey] = useState(() => localStorage.getItem('ANTHROPIC_API_KEY') || '');
  const [geminiKey, setGeminiKey] = useState(() => localStorage.getItem('GEMINI_API_KEY') || '');
  const [deepseekKey, setDeepseekKey] = useState(() => localStorage.getItem('DEEPSEEK_API_KEY') || '');
  const [customBaseUrl, setCustomBaseUrl] = useState(() => localStorage.getItem('CUSTOM_LLM_BASE_URL') || 'http://localhost:8000/v1');
  const [customApiKey, setCustomApiKey] = useState(() => localStorage.getItem('CUSTOM_LLM_API_KEY') || '');
  const [customModel, setCustomModel] = useState(() => localStorage.getItem('CUSTOM_LLM_MODEL') || 'custom-model');
  const [elevenlabsKey, setElevenlabsKey] = useState(() => localStorage.getItem('ELEVENLABS_API_KEY') || '');
  const [deepgramKey, setDeepgramKey] = useState(() => localStorage.getItem('DEEPGRAM_API_KEY') || '');
  const [tavilyKey, setTavilyKey] = useState(() => localStorage.getItem('TAVILY_API_KEY') || '');
  const [discordToken, setDiscordToken] = useState(() => localStorage.getItem('DISCORD_BOT_TOKEN') || '');
  const [telegramToken, setTelegramToken] = useState(() => localStorage.getItem('TELEGRAM_BOT_TOKEN') || '');
  const [telegramChatId, setTelegramChatId] = useState(() => localStorage.getItem('TELEGRAM_CHAT_ID') || '');
  const [saveStatus, setSaveStatus] = useState<'idle' | 'saving' | 'saved' | 'fail'>('idle');

  // Backend Integration state
  const [backendUrl, setBackendUrl] = useState(() => localStorage.getItem('MERIDIAN_REMOTE_BACKEND_URL') || getApiBaseUrl());
  const [backendApiKey, setBackendApiKey] = useState(() => localStorage.getItem('MERIDIAN_REMOTE_API_KEY') || getApiKey());
  const [backendStatusMsg, setBackendStatusMsg] = useState<{ text: string; isError: boolean } | null>(null);
  const [isTestingBackend, setIsTestingBackend] = useState(false);

  const [audioFxEnabled, setAudioFxEnabled] = useState(() => localStorage.getItem('meridian_mascot_audio_fx') !== 'false');
  const [ttsVoice, setTtsVoice] = useState(() => localStorage.getItem('meridian_tts_voice') || 'M1');
  const [ttsVolume, setTtsVolume] = useState(() => parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5'));
  const [startupEnabled, setStartupEnabled] = useState(false);
  const [themeFilter, setThemeFilter] = useState<'all' | 'dark' | 'light'>('all');

  // MCP state variables
  const [mcpServers, setMcpServers] = useState<Record<string, any>>({});
  const [mcpCatalog, setMcpCatalog] = useState<any[]>([
    { id: 'github-mcp', name: 'GitHub Integration', category: 'Developer Tools', description: 'Manage repositories, issues, PRs, and workflow runs via GitHub API.', command: 'npx -y @modelcontextprotocol/server-github', installed: false },
    { id: 'postgres-mcp', name: 'PostgreSQL Database Engine', category: 'Database', description: 'Inspect schemas, execute queries, and generate migrations for Postgres.', command: 'npx -y @modelcontextprotocol/server-postgres', installed: false },
    { id: 'slack-mcp', name: 'Slack Messenger', category: 'Communication', description: 'Send notifications, read channels, and manage Slack workspace communications.', command: 'npx -y @modelcontextprotocol/server-slack', installed: false },
    { id: 'linear-mcp', name: 'Linear Issue Tracker', category: 'Productivity', description: 'Sync issues, sprint backlogs, and project milestones with Linear.', command: 'npx -y @modelcontextprotocol/server-linear', installed: false },
  ]);
  const [newServerName, setNewServerName] = useState('');
  const [newServerCommand, setNewServerCommand] = useState('');
  const [newServerArgs, setNewServerArgs] = useState('');
  const [newServerEnv, setNewServerEnv] = useState('');

  // Day 5 Voice features state
  const [voiceResponseEnabled, setVoiceResponseState] = useState(true);
  const [duplexActive, setDuplexActive] = useState(false);
  const [continuousActive, setContinuousActive] = useState(false);
  const [continuousRemaining, setContinuousRemaining] = useState(0);
  const [biometricsCount, setBiometricsCount] = useState(0);

  const fetchVoiceStatus = async () => {
    try {
      const resResp = await fetch(`${API_BASE_URL}/api/voice/response/status`);
      if (resResp.ok) {
        const data = await resResp.json();
        if (typeof data.enabled === 'boolean') setVoiceResponseState(data.enabled);
      }
      const resDup = await fetch(`${API_BASE_URL}/api/voice/duplex/status`);
      if (resDup.ok) {
        const data = await resDup.json();
        if (data.duplex_state?.active) setDuplexActive(data.duplex_state.active);
      }
      const resWin = await fetch(`${API_BASE_URL}/api/voice/continuous-window/status`);
      if (resWin.ok) {
        const data = await resWin.json();
        setContinuousActive(data.active);
        setContinuousRemaining(data.remaining_seconds || 0);
      }
      const resBio = await fetch(`${API_BASE_URL}/api/voice/biometrics/status`);
      if (resBio.ok) {
        const data = await resBio.json();
        setBiometricsCount(data.biometrics?.enrolled_count || 0);
      }
    } catch { /* noop */ }
  };

  const handleToggleVoiceResponse = async () => {
    const nextState = !voiceResponseEnabled;
    setVoiceResponseState(nextState);
    try {
      await fetch(`${API_BASE_URL}/api/voice/response/toggle?enabled=${nextState}`, { method: 'POST' });
    } catch { }
  };

  const handleToggleDuplex = async () => {
    const endpoint = duplexActive ? 'stop' : 'start';
    try {
      const res = await fetch(`${API_BASE_URL}/api/voice/duplex/${endpoint}`, { method: 'POST' });
      if (res.ok) setDuplexActive(!duplexActive);
    } catch { }
  };

  const handleTriggerContinuousWindow = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/voice/continuous-window/start?duration=10.0`, { method: 'POST' });
      if (res.ok) {
        setContinuousActive(true);
        setContinuousRemaining(10.0);
      }
    } catch { }
  };

  const handleResetBiometrics = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/voice/biometrics/reset`, { method: 'DELETE' });
      if (res.ok) setBiometricsCount(0);
    } catch { }
  };

  const fetchCustomMcpServers = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/mcp/custom`);
      const data = await res.json();
      if (data.servers) {
        setMcpServers(data.servers);
      }
    } catch { }
  };

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/mcp/servers`)
      .then(res => res.json())
      .then(data => {
        if (data.servers && data.servers.length > 0) setMcpCatalog(data.servers);
      })
      .catch(() => { });
    fetchCustomMcpServers();
    fetchVoiceStatus();
  }, []);

  const handleInstallMcp = async (serverId: string) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/mcp/install`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ server_id: serverId })
      });
      if (res.ok) {
        setMcpCatalog(prev => prev.map(s => s.id === serverId ? { ...s, installed: true } : s));
        fetchCustomMcpServers();
      }
    } catch { }
  };

  const handleAddCustomMcpServer = async () => {
    if (!newServerName.trim() || !newServerCommand.trim()) return;
    try {
      const argsArray = newServerArgs
        .split(' ')
        .map(a => a.trim())
        .filter(a => a.length > 0);

      const envObj: Record<string, string> = {};
      newServerEnv.split(',').forEach(pair => {
        const [k, v] = pair.split('=');
        if (k && v) envObj[k.trim()] = v.trim();
      });

      const res = await fetch(`${API_BASE_URL}/api/mcp/custom`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: newServerName.trim(),
          command: newServerCommand.trim(),
          args: argsArray,
          env: envObj
        })
      });
      if (res.ok) {
        setNewServerName('');
        setNewServerCommand('');
        setNewServerArgs('');
        setNewServerEnv('');
        fetchCustomMcpServers();
      }
    } catch { }
  };

  const handleDeleteCustomMcpServer = async (serverName: string) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/mcp/custom/${encodeURIComponent(serverName)}`, {
        method: 'DELETE'
      });
      if (res.ok) {
        fetchCustomMcpServers();
      }
    } catch { }
  };

  const [auditorModel, setAuditorModel] = useState(() => localStorage.getItem('meridian_auditor_model') || 'for ex: model name');
  const [contextTokenLimit, setContextTokenLimit] = useState(() => parseInt(localStorage.getItem('context_token_limit') || '8192'));
  const [wakewordThreshold, setWakewordThreshold] = useState(() => parseFloat(localStorage.getItem('wakeword_threshold') || '0.6'));
  const [wakewordModel, setWakewordModel] = useState(() => localStorage.getItem('wakeword_model_filename') || 'hey_meridian.onnx');
  const [scannedOnnxModels, setScannedOnnxModels] = useState<Array<{ name: string; path: string; folder: string }>>([]);
  const [isScanningOnnx, setIsScanningOnnx] = useState(false);
  const fileInputRef = React.useRef<HTMLInputElement>(null);

  const [updateInfo, setUpdateInfo] = useState<any>(null);
  const [isCheckingUpdate, setIsCheckingUpdate] = useState(false);
  const [isTriggeringUpdate, setIsTriggeringUpdate] = useState(false);
  const [updateMsg, setUpdateMsg] = useState('');

  const checkSystemUpdate = async () => {
    setIsCheckingUpdate(true);
    setUpdateMsg('');
    try {
      const res = await fetch(`${API_BASE_URL}/api/system/check-update`);
      if (res.ok) {
        const data = await res.json();
        setUpdateInfo(data);
      }
    } catch (e) {
      console.error("Check update error:", e);
    } finally {
      setIsCheckingUpdate(false);
    }
  };

  const handleTriggerUpdate = async () => {
    setIsTriggeringUpdate(true);
    setUpdateMsg('');
    try {
      const res = await fetch(`${API_BASE_URL}/api/system/trigger-update`, { method: 'POST' });
      if (res.ok) {
        const data = await res.json();
        setUpdateMsg(data.message || 'Update triggered successfully.');
      }
    } catch (e) {
      setUpdateMsg(`Update failed: ${e}`);
    } finally {
      setIsTriggeringUpdate(false);
    }
  };

  useEffect(() => {
    checkSystemUpdate();
  }, []);

  const handleBrowseOnnxFile = async () => {
    // tauri-plugin-dialog is not installed; fall through to HTML file input
    // If the dialog plugin is added in the future, the invoke call can be re-enabled:
    //   const selected = await invoke<string | null>('dialog|open', { ... });
    fileInputRef.current?.click();
  };

  const handleFileInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file) {
      const fullPath = (file as any).path || file.name;
      setWakewordModel(fullPath);
    }
  };

  const fetchScannedOnnxModels = async () => {
    setIsScanningOnnx(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/voice/onnx-models`);
      if (res.ok) {
        const data = await res.json();
        if (data.models) setScannedOnnxModels(data.models);
      }
    } catch (e) {
      console.warn("Failed to scan ONNX models:", e);
    } finally {
      setIsScanningOnnx(false);
    }
  };
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
  const [smtpPort, setSmtpPort] = useState(() => parseInt(localStorage.getItem('SMTP_PORT') || '587'));
  const [smtpEmail, setSmtpEmail] = useState(() => localStorage.getItem('SMTP_EMAIL') || '');
  const [smtpPassword, setSmtpPassword] = useState(() => localStorage.getItem('SMTP_PASSWORD') || '');
  const [imapServer, setImapServer] = useState(() => localStorage.getItem('IMAP_SERVER') || 'imap.gmail.com');
  const [mongodbUri, setMongodbUri] = useState(() => localStorage.getItem('MONGODB_URI') || 'mongodb://localhost:27017/meridian_kg');
  const [logLevel, setLogLevel] = useState(() => localStorage.getItem('MERIDIAN_LOG_LEVEL') || 'INFO');

  // Dynamic Secret Vault Keys state
  const [vaultKeys, setVaultKeys] = useState<Array<{ name: string; env_var: string; api_key: string; base_url: string; category: string }>>([]);
  const [showVaultSecrets, setShowVaultSecrets] = useState(false);
  const [vkName, setVkName] = useState('');
  const [vkEnvVar, setVkEnvVar] = useState('');
  const [vkSecret, setVkSecret] = useState('');
  const [vkBaseUrl, setVkBaseUrl] = useState('');
  const [vkCategory, setVkCategory] = useState('LLM Provider');

  const fetchVaultKeys = async (showFull = showVaultSecrets) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/vault/keys?include_secrets=${showFull}`);
      if (res.ok) {
        const data = await res.json();
        if (data.keys) setVaultKeys(data.keys);
      }
    } catch (e) {
      console.warn("Failed to fetch vault keys:", e);
    }
  };

  const handleAddVaultKey = async () => {
    if (!vkName.trim() || !vkEnvVar.trim() || !vkSecret.trim()) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/vault/keys`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: vkName,
          env_var: vkEnvVar.toUpperCase(),
          api_key: vkSecret,
          base_url: vkBaseUrl,
          category: vkCategory
        })
      });
      if (res.ok) {
        setVkName('');
        setVkEnvVar('');
        setVkSecret('');
        setVkBaseUrl('');
        fetchVaultKeys();
      }
    } catch (e) {
      console.error("Failed to save vault key:", e);
    }
  };

  const handleDeleteVaultKey = async (env_var: string) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/vault/keys/${env_var}`, { method: 'DELETE' });
      if (res.ok) fetchVaultKeys();
    } catch (e) {
      console.error("Failed to delete vault key:", e);
    }
  };

  const handleTestBackendConnection = async () => {
    setIsTestingBackend(true);
    setBackendStatusMsg(null);
    const targetUrl = backendUrl.trim().replace(/\/+$/, '');
    try {
      const headers: Record<string, string> = {};
      if (backendApiKey.trim()) {
        headers['X-API-Key'] = backendApiKey.trim();
      }
      const res = await fetch(`${targetUrl}/api/health`, { headers });
      if (res.ok) {
        setBackendStatusMsg({ text: '✅ Connected successfully!', isError: false });
      } else {
        setBackendStatusMsg({ text: `⚠️ Server returned status ${res.status}`, isError: true });
      }
    } catch (err: any) {
      setBackendStatusMsg({ text: `❌ Connection failed: ${err.message || 'Network error'}`, isError: true });
    } finally {
      setIsTestingBackend(false);
    }
  };

  const handleSaveBackendConfig = () => {
    if (backendUrl.trim()) {
      localStorage.setItem('MERIDIAN_REMOTE_BACKEND_URL', backendUrl.trim());
    } else {
      localStorage.removeItem('MERIDIAN_REMOTE_BACKEND_URL');
    }

    if (backendApiKey.trim()) {
      localStorage.setItem('MERIDIAN_REMOTE_API_KEY', backendApiKey.trim());
    } else {
      localStorage.removeItem('MERIDIAN_REMOTE_API_KEY');
    }

    window.location.reload();
  };

  const handleResetBackendConfig = () => {
    localStorage.removeItem('MERIDIAN_REMOTE_BACKEND_URL');
    localStorage.removeItem('MERIDIAN_REMOTE_API_KEY');
    setBackendUrl(getApiBaseUrl());
    setBackendApiKey('');
    window.location.reload();
  };

  useEffect(() => {
    fetchVaultKeys();
  }, [showVaultSecrets]);

  // Fetch profile configurations on mount to hydrate local storage & states
  useEffect(() => {
    fetch(`${API_BASE_URL}/api/profile/all`)
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
      .catch(() => { });
  }, []);

  // Fetch MCP config on mount
  useEffect(() => {
    fetch(`${API_BASE_URL}/api/mcp/config`)
      .then(r => r.json())
      .then(data => {
        if (data && data.mcpServers) {
          setMcpServers(data.mcpServers);
        }
      })
      .catch(() => { });
  }, []);

  const saveMcpConfig = async (servers: Record<string, any>) => {
    try {
      await fetch(`${API_BASE_URL}/api/mcp/config`, {
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
    fetch(`${API_BASE_URL}/api/system/startup`)
      .then(r => r.json())
      .then(data => { if (typeof data.enabled === 'boolean') setStartupEnabled(data.enabled); })
      .catch(() => { });

    fetch(`${API_BASE_URL}/api/workspace/config`)
      .then(r => r.json())
      .then(data => {
        if (data.status === 'success' && data.config) {
          setWorkspaceConfig(data.config);
          setWorkspaceModel(data.config.brain_model || '');
          setWorkspaceDirectives(data.config.custom_directives || '');
        }
      })
      .catch(() => { });
  }, []);

  const handleToggleStartup = async (checked: boolean) => {
    setStartupEnabled(checked);
    try {
      await fetch(`${API_BASE_URL}/api/system/startup`, {
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
    fetch(`${API_BASE_URL}/api/provider-models?provider=ollama&host=${encodeURIComponent(ollamaHost)}`).catch(() => null)
      .then(r => r?.json())
      .then(d => {
        if (d?.models) {
          setAvailableOllamaModels(d.models.map((m: any) => m.name || m));
        }
      })
      .catch(() => { });
  }, [ollamaHost]);

  // Fetch Brain models based on selected provider and key
  useEffect(() => {
    let key = '';
    if (provider === 'openai') key = openaiKey;
    else if (provider === 'anthropic') key = anthropicKey;
    else if (provider === 'gemini') key = geminiKey;
    else if (provider === 'deepseek') key = deepseekKey;

    const url = `${API_BASE_URL}/api/provider-models?provider=${provider}&host=${encodeURIComponent(ollamaHost)}&api_key=${encodeURIComponent(key)}`;
    fetch(url).catch(() => null)
      .then(r => r?.json())
      .then(d => {
        if (d?.models) {
          setAvailableBrainModels(d.models.map((m: any) => m.name || m));
        }
      })
      .catch(() => { });
  }, [provider, ollamaHost, openaiKey, anthropicKey, geminiKey, deepseekKey]);

  // Set default models when provider changes to prevent model mismatch
  useEffect(() => {
    if (provider !== 'ollama') {
      const models = PROVIDER_MODELS[provider] || [];
      if (models.length > 0 && !models.includes(brainModel)) {
        setBrainModel(models[0]);
        localStorage.setItem('MERIDIAN_MODEL', models[0]);
        setModelName(models[0]);
        window.dispatchEvent(new Event('meridian-model-changed'));
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
      MERIDIAN_PROVIDER: provider, MERIDIAN_MODEL_SOURCE: modelSource, OLLAMA_HOST: ollamaHost,
      MERIDIAN_MODEL: brainModel, MERIDIAN_VISION_MODEL: visionModel,
      GROQ_API_KEY: groqKey, OPENROUTER_API_KEY: openrouterKey, MISTRAL_API_KEY: mistralKey,
      OPENAI_API_KEY: openaiKey, ANTHROPIC_API_KEY: anthropicKey,
      GEMINI_API_KEY: geminiKey, DEEPSEEK_API_KEY: deepseekKey,
      CUSTOM_LLM_BASE_URL: customBaseUrl, CUSTOM_LLM_API_KEY: customApiKey, CUSTOM_LLM_MODEL: customModel,
      ELEVENLABS_API_KEY: elevenlabsKey, DEEPGRAM_API_KEY: deepgramKey,
      TAVILY_API_KEY: tavilyKey, DISCORD_BOT_TOKEN: discordToken,
      TELEGRAM_BOT_TOKEN: telegramToken, TELEGRAM_CHAT_ID: telegramChatId,
      GAME_MODE: gameMode ? 'true' : 'false',
      meridian_auditor_model: auditorModel,
      EMBEDDING_MODEL: embeddingModel,
      embedding_model: embeddingModel,
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
      context_token_limit: String(contextTokenLimit),
    };
    Object.entries(entries).forEach(([k, v]) => localStorage.setItem(k, v));

    // Parse distraction sites list
    const parsedDistractions = distractions
      .split(',')
      .map(s => s.trim())
      .filter(s => s.length > 0);

    try {
      const res = await fetch(`${API_BASE_URL}/api/profile/save`, {
        method: 'POST', headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          meridian_provider: provider, meridian_model_source: modelSource, ollama_host: ollamaHost,
          meridian_model: brainModel, meridian_vision_model: visionModel,
          groq_key: groqKey, openrouter_key: openrouterKey, mistral_key: mistralKey,
          openai_key: openaiKey, anthropic_key: anthropicKey,
          gemini_key: geminiKey, deepseek_key: deepseekKey,
          custom_llm_base_url: customBaseUrl, custom_llm_api_key: customApiKey, custom_llm_model: customModel,
          tavily_key: tavilyKey, discord_token: discordToken,
          telegram_token: telegramToken, telegram_chat_id: telegramChatId,
          meridian_auditor_model: auditorModel,
          embedding_model: embeddingModel,
          context_token_limit: contextTokenLimit,
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
          await fetch(`${API_BASE_URL}/api/workspace/config`, {
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
        window.dispatchEvent(new Event('meridian-model-changed'));
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
      groq: [groqKey, setGroqKey, 'gsk_...'],
      openrouter: [openrouterKey, setOpenrouterKey, 'sk-or-v1-...'],
      mistral: [mistralKey, setMistralKey, 'sk-...'],
      openai: [openaiKey, setOpenaiKey, 'sk-proj-...'],
      anthropic: [anthropicKey, setAnthropicKey, 'sk-ant-...'],
      gemini: [geminiKey, setGeminiKey, 'AIzaSy...'],
      deepseek: [deepseekKey, setDeepseekKey, 'sk-...'],
    };
    return map[provider] ?? null;
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', height: '100%', padding: '20px 24px', overflow: 'hidden' }}>
      <div style={{ marginBottom: 16, flexShrink: 0 }}>
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Settings</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 8px', fontFamily: "'JetBrains Mono', monospace" }}>Configuration · Models · Appearance · Guard</p>

        {/* Category Navigation Bar */}
        <div style={{ display: 'flex', gap: 6, overflowX: 'auto', borderBottom: '1px solid var(--border-subtle)', paddingBottom: 8, marginTop: 12 }}>
          {SETTINGS_TABS.map(t => {
            const Icon = t.icon;
            const active = activeCategory === t.id;
            return (
              <button
                key={t.id}
                type="button"
                onClick={() => setActiveCategory(t.id as any)}
                style={{
                  display: 'flex', alignItems: 'center', gap: 6,
                  padding: '6px 12px', borderRadius: 'var(--radius-sm)',
                  border: active ? '1px solid var(--accent)' : '1px solid transparent',
                  background: active ? 'color-mix(in srgb, var(--accent) 12%, transparent)' : 'var(--bg-surface)',
                  color: active ? 'var(--accent)' : 'var(--text-dim)',
                  cursor: 'pointer', fontSize: 11, fontWeight: active ? 600 : 400,
                  transition: 'all 0.15s ease',
                  whiteSpace: 'nowrap',
                }}
              >
                <Icon size={13} />
                {t.label}
              </button>
            );
          })}
        </div>
      </div>

      <form onSubmit={handleSave} style={{ flex: 1, overflowY: 'auto', display: 'grid', gridTemplateColumns: '1fr 260px', gap: 16 }}>
        {/* Left: config */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>

          {/* Category 1: AI Models */}
          {activeCategory === 'models' && (
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
                        />
                      </div>
                    ) : (() => {
                      const cfg = apiKeyForProvider();
                      if (!cfg) return null;
                      const [val, setter, ph] = cfg;
                      return <PasswordInput label="API Key" value={val} onChange={setter} placeholder={ph} />;
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
                    onClick={() => setShowVaultSecrets(v => !v)}
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
                            <span style={{ fontSize: 9, padding: '2px 6px', background: 'rgba(96, 165, 250, 0.15)', color: '#60A5FA', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                              {k.category || 'LLM Provider'}
                            </span>
                            <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', fontWeight: 600 }}>
                              ${k.env_var}
                            </span>
                          </div>
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                            Key: {k.api_key} {k.base_url && `· Base: ${k.base_url}`}
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
          )}

          {/* Category: Integrations */}
          {activeCategory === 'integrations' && (
            <>
              {/* Frontend & Backend Server Integration */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
                  <div className="section-label" style={{ margin: 0 }}>🌐 Core Frontend & Backend Integration</div>
                  <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                    Active Endpoint: {API_BASE_URL}
                  </span>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  <div>
                    <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                      Backend Server URL
                    </label>
                    <input
                      type="text"
                      value={backendUrl}
                      onChange={(e) => setBackendUrl(e.target.value)}
                      placeholder="http://127.0.0.1:4132 or https://my-backend-server.com"
                      className="input-base"
                      style={{ width: '100%', fontSize: 12 }}
                    />
                  </div>

                  <PasswordInput
                    label="Backend API Key (Required for Remote/Protected Server)"
                    value={backendApiKey}
                    onChange={setBackendApiKey}
                    placeholder="Enter Meridian secret API key"
                  />

                  {backendStatusMsg && (
                    <div style={{
                      padding: '8px 12px',
                      borderRadius: 'var(--radius-sm)',
                      fontSize: 11,
                      fontFamily: 'JetBrains Mono',
                      background: backendStatusMsg.isError ? 'rgba(244, 63, 94, 0.15)' : 'rgba(16, 185, 129, 0.15)',
                      border: backendStatusMsg.isError ? '1px solid rgba(244, 63, 94, 0.4)' : '1px solid rgba(16, 185, 129, 0.4)',
                      color: backendStatusMsg.isError ? '#f87171' : '#34d399'
                    }}>
                      {backendStatusMsg.text}
                    </div>
                  )}

                  <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                    <HoloButton
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={handleTestBackendConnection}
                      disabled={isTestingBackend}
                    >
                      {isTestingBackend ? <Loader2 className="animate-spin" size={12} /> : <RefreshCw size={12} />}
                      {isTestingBackend ? 'Testing...' : 'Test Connection'}
                    </HoloButton>

                    <HoloButton
                      type="button"
                      variant="primary"
                      size="sm"
                      onClick={handleSaveBackendConfig}
                    >
                      <Save size={12} />
                      Save & Connect
                    </HoloButton>

                    <HoloButton
                      type="button"
                      variant="ghost"
                      size="sm"
                      onClick={handleResetBackendConfig}
                    >
                      Reset Defaults
                    </HoloButton>
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

              {/* Universal Encrypted Secret Vault */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
                  <div className="section-label" style={{ margin: 0 }}>🔐 Universal API Key & Secret Vault</div>
                  <button
                    type="button"
                    onClick={() => setShowVaultSecrets(v => !v)}
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
                            <span style={{ fontSize: 9, padding: '2px 6px', background: 'rgba(96, 165, 250, 0.15)', color: '#60A5FA', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                              {k.category || 'LLM Provider'}
                            </span>
                            <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', fontWeight: 600 }}>
                              ${k.env_var}
                            </span>
                          </div>
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                            Key: {k.api_key} {k.base_url && `· Base: ${k.base_url}`}
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

              {/* Model Context Protocol (MCP) Server Marketplace */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label" style={{ marginBottom: 10 }}>🔌 Model Context Protocol (MCP) Server Registry</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                  <div style={{ fontSize: 11, color: 'var(--text-dim)', lineHeight: '1.5' }}>
                    Manage connected Model Context Protocol (MCP) servers. Registered servers dynamically expose tools directly into the ReAct reasoning loop.
                  </div>

                  {/* Registered Custom Servers */}
                  {Object.keys(mcpServers).length > 0 ? (
                    <div>
                      <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
                        Active Connected MCP Servers ({Object.keys(mcpServers).length})
                      </label>
                      <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                        {Object.entries(mcpServers).map(([srvName, srvConfig]: [string, any]) => (
                          <div key={srvName} style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{srvName}</span>
                                <span style={{ fontSize: 9, padding: '2px 6px', background: 'rgba(0, 217, 126, 0.15)', color: '#00D97E', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                                  Active
                                </span>
                              </div>
                              <div style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono' }}>
                                {srvConfig.command} {srvConfig.args?.join(' ')}
                              </div>
                            </div>
                            <HoloButton type="button" variant="danger" size="sm" onClick={() => handleDeleteCustomMcpServer(srvName)}>
                              <Trash2 size={12} />
                            </HoloButton>
                          </div>
                        ))}
                      </div>
                    </div>
                  ) : null}

                  {/* Add Custom MCP Server Form */}
                  <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12, display: 'flex', flexDirection: 'column', gap: 10 }}>
                    <label style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', display: 'block', textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
                      + Enter / Register Custom MCP Server
                    </label>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                      <div>
                        <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Server Name</label>
                        <input type="text" value={newServerName} onChange={e => setNewServerName(e.target.value)} placeholder="e.g. Filesystem MCP / Git MCP" className="input-base" style={{ height: 32, fontSize: 11 }} />
                      </div>
                      <div>
                        <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Command Executable</label>
                        <input type="text" value={newServerCommand} onChange={e => setNewServerCommand(e.target.value)} placeholder="e.g. npx / uvx / node / python" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                      </div>
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: '1.5fr 1fr', gap: 8 }}>
                      <div>
                        <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Arguments (Space Separated)</label>
                        <input type="text" value={newServerArgs} onChange={e => setNewServerArgs(e.target.value)} placeholder="e.g. -y @modelcontextprotocol/server-filesystem C:/Projects" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                      </div>
                      <div>
                        <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Env Vars (KEY=VAL, ...)</label>
                        <input type="text" value={newServerEnv} onChange={e => setNewServerEnv(e.target.value)} placeholder="API_KEY=xxx, TOKEN=yyy" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                      </div>
                    </div>

                    <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: 2 }}>
                      <HoloButton type="button" variant="primary" size="sm" onClick={handleAddCustomMcpServer} disabled={!newServerName.trim() || !newServerCommand.trim()}>
                        <Plus size={12} /> Register MCP Server
                      </HoloButton>
                    </div>
                  </div>

                  {/* Catalog Servers */}
                  <div style={{ borderTop: '1px solid var(--border-subtle)', paddingTop: 12 }}>
                    <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 8, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                      1-Click Featured MCP Marketplace Catalog
                    </label>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                      {mcpCatalog.map(s => (
                        <div key={s.id} style={{ display: 'flex', flexDirection: 'column', justifyContent: 'space-between', padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', gap: 8 }}>
                          <div>
                            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 4 }}>
                              <span style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>{s.name}</span>
                              <span style={{ fontSize: 9, padding: '2px 6px', background: s.installed ? 'rgba(0, 217, 126, 0.15)' : 'rgba(96, 165, 250, 0.15)', color: s.installed ? '#00D97E' : '#60A5FA', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                                {s.installed ? 'Installed' : s.category}
                              </span>
                            </div>
                            <div style={{ fontSize: 10, color: 'var(--text-dim)', lineHeight: '1.4' }}>{s.description}</div>
                            <div style={{ fontSize: 9, color: 'var(--accent)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>{s.command}</div>
                          </div>
                          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                            <HoloButton
                              type="button"
                              variant={s.installed ? "ghost" : "primary"}
                              size="sm"
                              disabled={s.installed}
                              onClick={() => handleInstallMcp(s.id)}
                            >
                              {s.installed ? "Active" : "Install Server"}
                            </HoloButton>
                          </div>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>
              </GlowCard>
            </>
          )}

          {/* Category: Voice */}
          {activeCategory === 'voice' && (
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
                      <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: duplexActive ? 'rgba(52, 211, 153, 0.15)' : 'rgba(255,255,255,0.06)', color: duplexActive ? 'var(--success)' : 'var(--text-dim)' }}>
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
                      <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: continuousActive ? 'rgba(96, 165, 250, 0.15)' : 'rgba(255,255,255,0.06)', color: continuousActive ? '#60A5FA' : 'var(--text-dim)' }}>
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
                      <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: biometricsCount > 0 ? 'rgba(52, 211, 153, 0.15)' : 'rgba(255,255,255,0.06)', color: biometricsCount > 0 ? 'var(--success)' : 'var(--text-dim)' }}>
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
                        accept=".onnx"
                        style={{ display: 'none' }}
                        onChange={handleFileInputChange}
                      />
                      <button
                        type="button"
                        onClick={handleBrowseOnnxFile}
                        className="btn-secondary"
                        style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '8px 12px', fontSize: 11, cursor: 'pointer', whiteSpace: 'nowrap' }}
                        title="Browse folders for .onnx model"
                      >
                        <FolderOpen size={14} />
                        Browse...
                      </button>
                      <button
                        type="button"
                        onClick={fetchScannedOnnxModels}
                        disabled={isScanningOnnx}
                        className="btn-secondary"
                        style={{ display: 'flex', alignItems: 'center', gap: 6, padding: '8px 12px', fontSize: 11, cursor: 'pointer', whiteSpace: 'nowrap' }}
                        title="Scan system folders for .onnx models"
                      >
                        <Search size={14} />
                        {isScanningOnnx ? 'Scanning...' : 'Scan'}
                      </button>
                    </div>
                    {scannedOnnxModels.length > 0 && (
                      <div style={{ marginTop: 8, background: 'rgba(0,0,0,0.3)', borderRadius: 6, padding: 8, border: '1px solid rgba(255,255,255,0.08)' }}>
                        <div style={{ fontSize: 10, color: 'var(--text-dim)', marginBottom: 4, fontFamily: 'JetBrains Mono' }}>DETECTED ONNX MODELS:</div>
                        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                          {scannedOnnxModels.map((m, idx) => (
                            <button
                              key={idx}
                              type="button"
                              onClick={() => setWakewordModel(m.path || m.name)}
                              style={{
                                fontSize: 11,
                                fontFamily: "'JetBrains Mono', monospace",
                                background: wakewordModel === m.path || wakewordModel === m.name ? 'rgba(96, 165, 250, 0.2)' : 'rgba(255,255,255,0.05)',
                                border: wakewordModel === m.path || wakewordModel === m.name ? '1px solid var(--accent-primary, #60A5FA)' : '1px solid rgba(255,255,255,0.1)',
                                color: 'var(--text-main, #E2E8F0)',
                                borderRadius: 4,
                                padding: '4px 8px',
                                cursor: 'pointer'
                              }}
                              title={m.path}
                            >
                              {m.name}
                            </button>
                          ))}
                        </div>
                      </div>
                    )}
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

              {/* Voice & Audio Provider API Credentials */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">Cloud Voice & Speech Provider API Keys</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                  <PasswordInput label="ElevenLabs API Key (TTS High-Fidelity Voice)" value={elevenlabsKey} onChange={setElevenlabsKey} placeholder="xi-..." />
                  <PasswordInput label="Deepgram API Key (Real-Time Cloud STT)" value={deepgramKey} onChange={setDeepgramKey} placeholder="dg-..." />
                </div>
              </GlowCard>

              {/* Universal Encrypted Secret Vault inside Voice tab */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
                  <div className="section-label" style={{ margin: 0 }}>🔐 Universal API Key & Encrypted Secret Vault</div>
                  <button
                    type="button"
                    onClick={() => setShowVaultSecrets(v => !v)}
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
                            <span style={{ fontSize: 9, padding: '2px 6px', background: 'rgba(96, 165, 250, 0.15)', color: '#60A5FA', borderRadius: 4, fontFamily: 'JetBrains Mono' }}>
                              {k.category || 'Audio & Voice'}
                            </span>
                            <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', fontWeight: 600 }}>
                              ${k.env_var}
                            </span>
                          </div>
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                            Key: {k.api_key} {k.base_url && `· Base: ${k.base_url}`}
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
          )}

          {/* Category: Guard */}
          {activeCategory === 'guard' && (
            <>
              {/* System Version & Auto-Update Engine */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 12 }}>
                  <div className="section-label" style={{ margin: 0 }}>🪐 System Version & Auto-Update Engine</div>
                  <HoloButton type="button" variant="ghost" size="sm" onClick={checkSystemUpdate} disabled={isCheckingUpdate}>
                    {isCheckingUpdate ? <Loader2 size={12} className="animate-spin" /> : <RefreshCw size={12} />}
                    {isCheckingUpdate ? 'Checking GitHub...' : 'Check for Updates'}
                  </HoloButton>
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 12, marginBottom: 12 }}>
                  <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase' }}>Installed Version</div>
                    <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>
                      v{updateInfo?.current_version || '0.2.3'}
                    </div>
                  </div>
                  <div style={{ background: 'var(--bg-surface)', padding: 12, borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div style={{ fontSize: 9, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', textTransform: 'uppercase' }}>GitHub Latest Version</div>
                    <div style={{ fontSize: 16, fontWeight: 700, color: updateInfo?.update_available ? '#34D399' : 'var(--text-bright)', fontFamily: 'JetBrains Mono', marginTop: 4 }}>
                      v{updateInfo?.version_on_github || '0.2.3'}
                    </div>
                  </div>
                </div>

                {updateInfo?.update_available ? (
                  <div style={{ background: updateInfo.update_type === 'major' ? 'rgba(239, 68, 68, 0.12)' : 'rgba(16, 185, 129, 0.12)', border: updateInfo.update_type === 'major' ? '1px solid rgba(239, 68, 68, 0.3)' : '1px solid rgba(16, 185, 129, 0.3)', borderRadius: 'var(--radius-sm)', padding: 12 }}>
                    <div style={{ fontSize: 12, fontWeight: 700, color: updateInfo.update_type === 'major' ? '#F87171' : '#34D399', display: 'flex', alignItems: 'center', gap: 6 }}>
                      <span>✨ {updateInfo.update_type === 'major' ? 'Major Version Upgrade Available!' : updateInfo.auto_downloaded ? 'Patch Update Ready to Apply!' : 'Minor Update Ready!'}</span>
                      <span style={{ fontSize: 9, background: 'rgba(255,255,255,0.1)', padding: '2px 6px', borderRadius: 4, textTransform: 'uppercase' }}>{updateInfo.update_type}</span>
                    </div>
                    <div style={{ fontSize: 11, color: 'var(--text-main)', marginTop: 6, lineHeight: 1.4 }}>
                      {updateInfo.update_type === 'major'
                        ? 'A major release has breaking architectural changes. Click below to upgrade.'
                        : updateInfo.auto_downloaded
                          ? 'Patch assets were auto-downloaded in the background. Click below to pull final code and apply update.'
                          : 'A minor update is available. Click below to apply.'}
                    </div>
                    <div style={{ display: 'flex', gap: 8, marginTop: 10, alignItems: 'center' }}>
                      <HoloButton type="button" variant="primary" size="sm" onClick={handleTriggerUpdate} disabled={isTriggeringUpdate}>
                        {isTriggeringUpdate ? <Loader2 size={12} className="animate-spin" /> : <Download size={12} />}
                        {isTriggeringUpdate ? 'Updating...' : updateInfo.update_type === 'major' ? 'Upgrade to Major Version' : 'Apply Update & Pull Code'}
                      </HoloButton>
                      {updateInfo.release_url && (
                        <a href={updateInfo.release_url} target="_blank" rel="noreferrer" style={{ fontSize: 11, color: 'var(--accent)', textDecoration: 'none', fontFamily: 'JetBrains Mono' }}>
                          View Release Notes ↗
                        </a>
                      )}
                    </div>
                  </div>
                ) : (
                  <div style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono' }}>
                    ✅ Meridian-X is running the latest version.
                  </div>
                )}
                {updateMsg && (
                  <div style={{ marginTop: 8, fontSize: 11, color: '#34D399', fontFamily: 'JetBrains Mono' }}>
                    {updateMsg}
                  </div>
                )}
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

              {/* OPT-01 RAM & Performance Engine */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">⚡ RAM & Performance Engine (OPT-01)</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-bright)' }}>Low-RAM Performance Mode</div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>Strips blurs, backdrop filters, animations, and box shadows to maintain memory under 45MB RAM.</div>
                    </div>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer' }}>
                      <input
                        type="checkbox"
                        checked={isLowRam}
                        onChange={e => toggleLowRamMode(e.target.checked)}
                      />
                      <span style={{ fontSize: 11, fontFamily: 'JetBrains Mono', color: isLowRam ? 'var(--accent)' : 'var(--text-dim)' }}>
                        {isLowRam ? 'Enabled' : 'Disabled'}
                      </span>
                    </label>
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
            </>
          )}

          {/* Category: Mascot & Style */}
          {activeCategory === 'mascot' && (
            <>
              {/* Theme & Design Styles Selector */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
                  <div className="section-label" style={{ margin: 0 }}>Design Styles & Themes</div>
                  <span style={{ fontSize: 10, fontFamily: 'JetBrains Mono', color: 'var(--accent)', background: 'var(--accent-muted)', padding: '2px 8px', borderRadius: 4 }}>
                    11 STYLES AVAILABLE
                  </span>
                </div>

                {/* Filter Tabs */}
                <div style={{ display: 'flex', gap: 6, marginBottom: 12 }}>
                  {(['all', 'dark', 'light'] as const).map(tab => (
                    <button
                      key={tab}
                      type="button"
                      onClick={() => setThemeFilter(tab)}
                      style={{
                        flex: 1,
                        padding: '4px 8px',
                        fontSize: 10,
                        fontFamily: 'JetBrains Mono',
                        borderRadius: 4,
                        border: '1px solid var(--border-subtle)',
                        background: themeFilter === tab ? 'var(--accent-muted)' : 'transparent',
                        color: themeFilter === tab ? 'var(--accent)' : 'var(--text-dim)',
                        cursor: 'pointer',
                        textTransform: 'uppercase',
                        transition: 'all 0.15s ease',
                      }}
                    >
                      {tab === 'all' ? 'All (11)' : tab === 'dark' ? '🌙 Dark (7)' : '☀️ Light (4)'}
                    </button>
                  ))}
                </div>

                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: 10, maxHeight: 420, overflowY: 'auto', paddingRight: 2 }}>
                  {THEMES.filter(t => themeFilter === 'all' || (themeFilter === 'dark' ? t.mode === 'Dark' : t.mode === 'Light')).map(t => {
                    const isSelected = theme === t.id;
                    return (
                      <div
                        key={t.id}
                        onClick={() => setTheme(t.id)}
                        style={{
                          display: 'flex',
                          alignItems: 'center',
                          gap: 12,
                          padding: '10px 12px',
                          borderRadius: 'var(--radius-md)',
                          background: isSelected ? 'var(--bg-surface)' : 'var(--bg-panel)',
                          border: isSelected ? '1.5px solid var(--accent)' : '1px solid var(--border-subtle)',
                          boxShadow: isSelected ? '0 0 12px var(--accent-muted)' : 'none',
                          cursor: 'pointer',
                          transition: 'all 0.15s ease',
                          position: 'relative',
                          overflow: 'hidden',
                        }}
                      >
                        {/* Active accent bar */}
                        {isSelected && (
                          <div style={{ position: 'absolute', left: 0, top: 0, bottom: 0, width: 4, background: 'var(--accent)' }} />
                        )}

                        {/* Color Swatch Stack */}
                        <div style={{ display: 'flex', gap: 3, flexShrink: 0, padding: 3, background: t.swatches[0], borderRadius: 6, border: '1px solid rgba(255,255,255,0.1)' }}>
                          <div style={{ width: 8, height: 24, borderRadius: 3, background: t.swatches[0] }} />
                          <div style={{ width: 8, height: 24, borderRadius: 3, background: t.swatches[1] }} />
                          <div style={{ width: 8, height: 24, borderRadius: 3, background: t.swatches[2] }} />
                        </div>

                        {/* Info */}
                        <div style={{ flex: 1, minWidth: 0 }}>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                            <span style={{ fontSize: 13 }}>{t.icon}</span>
                            <span style={{
                              fontSize: 13,
                              fontWeight: 600,
                              fontFamily: t.font,
                              color: isSelected ? 'var(--text-bright)' : 'var(--text-main)',
                              whiteSpace: 'nowrap',
                              overflow: 'hidden',
                              textOverflow: 'ellipsis',
                            }}>
                              {t.label}
                            </span>
                            <span style={{
                              fontSize: 9,
                              fontFamily: 'JetBrains Mono',
                              padding: '1px 5px',
                              borderRadius: 3,
                              background: t.mode === 'Light' ? 'rgba(255, 222, 89, 0.2)' : 'rgba(255,255,255,0.06)',
                              color: t.mode === 'Light' ? '#FFDE59' : 'var(--text-dim)',
                              marginLeft: 'auto',
                            }}>
                              {t.mode}
                            </span>
                          </div>
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2, whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
                            {t.sub}
                          </div>
                        </div>

                        {/* Selected Checkmark */}
                        {isSelected && (
                          <div style={{
                            width: 20,
                            height: 20,
                            borderRadius: '50%',
                            background: 'var(--accent)',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            flexShrink: 0,
                          }}>
                            <Check size={12} color="#000" strokeWidth={3} />
                          </div>
                        )}
                      </div>
                    );
                  })}
                </div>
              </GlowCard>

              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">Mascot & Audio Customize</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>

                  {/* Dynamic Island Position */}
                  <div>
                    <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                      Dynamic Island Screen Position
                    </label>
                    <select
                      value={islandPosition}
                      onChange={e => setIslandPosition(e.target.value as any)}
                      className="select-base"
                    >
                      <option value="top-center">🍏 Top-Center (Apple Notch / Header)</option>
                      <option value="bottom-center">📱 Bottom-Center (Dock Style)</option>
                      <option value="top-right">↗️ Top-Right HUD</option>
                      <option value="bottom-right">📍 Bottom-Right Tray (Default)</option>
                      <option value="top-left">↖️ Top-Left Corner</option>
                      <option value="bottom-left">↙️ Bottom-Left Corner</option>
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
            </>
          )}

          {/* System Card inside Guard */}
          {activeCategory === 'guard' && (
            <>
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
            </>
          )}

          {/* Save Button */}
          <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
            <HoloButton type="submit" variant="primary" size="md" loading={saveStatus === 'saving'}>
              {saveStatus === 'saved' ? <><Check size={14} /> Saved!</> : saveStatus === 'fail' ? 'Save Failed' : <><Save size={14} /> Save Settings</>}
            </HoloButton>
          </div>
        </div>

        {/* Right: Hardware Vitals & Engine Monitor */}
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

          {/* Engine Health & Memory Optimizer Card */}
          <GlowCard className="glass" style={{ padding: 16, display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div className="section-label" style={{ margin: 0 }}>Memory & Engine Monitor</div>

            {/* Low RAM Mode Toggle */}
            <div style={{ padding: '10px 12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 8 }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <span style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-bright)' }}>Low RAM Optimizer</span>
                <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: isLowRam ? 'rgba(52, 211, 153, 0.15)' : 'rgba(255,255,255,0.06)', color: isLowRam ? 'var(--success)' : 'var(--text-dim)' }}>
                  {isLowRam ? 'ACTIVE' : 'DISABLED'}
                </span>
              </div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', lineHeight: 1.4 }}>
                Disables canvas background particles to optimize memory footprint.
              </div>
              <HoloButton type="button" variant={isLowRam ? "ghost" : "primary"} size="sm" onClick={toggleLowRamMode}>
                {isLowRam ? 'Disable Low-RAM Mode' : '⚡ Enable Low-RAM Mode'}
              </HoloButton>
            </div>

            {/* Subsystem Health Badges */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 6, paddingTop: 4 }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: 10, fontFamily: "'JetBrains Mono', monospace" }}>
                <span style={{ color: 'var(--text-dim)' }}>Backend Daemon</span>
                <span style={{ color: 'var(--success)', fontWeight: 600 }}>● Active (:4132)</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: 10, fontFamily: "'JetBrains Mono', monospace" }}>
                <span style={{ color: 'var(--text-dim)' }}>Vector DB Engine</span>
                <span style={{ color: 'var(--accent)', fontWeight: 600 }}>Turbovec Active</span>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', fontSize: 10, fontFamily: "'JetBrains Mono', monospace" }}>
                <span style={{ color: 'var(--text-dim)' }}>State Store</span>
                <span style={{ color: 'var(--accent-2)', fontWeight: 600 }}>SQLite WAL</span>
              </div>
            </div>
          </GlowCard>
        </div>
      </form>
    </div>
  );
}
