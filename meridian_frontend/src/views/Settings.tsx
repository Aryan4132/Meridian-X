import React, { useState, useEffect } from 'react';
import { invoke } from '@tauri-apps/api/core';
import { Check, Save, Cpu, Sparkles, Mic, ShieldCheck, DollarSign, Plug } from 'lucide-react';
import { emit } from '@tauri-apps/api/event';
import { API_BASE_URL, getApiBaseUrl, getApiKey } from '../config';
import { SystemUsage } from '../types';
import { useApp } from '../AppContext';
import { useLowRamMode } from '../hooks/useMemoryOptimizer';
import ProgressArc from '../components/ui/ProgressArc';
import HoloButton from '../components/ui/HoloButton';
import GlowCard from '../components/ui/GlowCard';
import {
  hasKeyLockPassword, verifyKeyLockPassword, isKeyLockUnlocked,
  unlockKeyLockSession, lockKeyLockSession, setKeyLockPassword,
} from '../utils/keyLock';
import MascotTab from './settings/MascotTab';
import VoiceTab from './settings/VoiceTab';
import IntegrationsTab from './settings/IntegrationsTab';
import AiModelsTab from './settings/AiModelsTab';
import SystemGuardTab from './settings/SystemGuardTab';
import SpendAirGapTab from './settings/SpendAirGapTab';
import PasswordInput from './settings/PasswordInput';

const SETTINGS_TABS = [
  { id: 'models', label: 'AI Models', icon: Cpu },
  { id: 'mascot', label: 'Mascot & Style', icon: Sparkles },
  { id: 'voice', label: 'Voice & Audio', icon: Mic },
  { id: 'guard', label: 'System Guard', icon: ShieldCheck },
  { id: 'spend', label: 'Spend & Air-Gap', icon: DollarSign },
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
  deepseek: ['deepseek-chat', 'deepseek-reasoner', 'deepseek-coder'],
};

const THEMES = [
  { id: 'tokyonight',   label: 'Tokyo Night',         icon: '🌙', sub: 'Tokyo Midnight & Soft Pastel Ice',  font: "'Inter', sans-serif",        mode: 'Dark',  swatches: ['#1a1b26', '#7aa2f7', '#bb9af7'] },


  { id: 'oled',         label: 'Pure OLED Black',     icon: '⬛', sub: 'True #000000 & Electric Cyan Glow', font: "'Outfit', sans-serif",       mode: 'Dark',  swatches: ['#000000', '#38bdf8', '#a855f7'] },
  { id: 'vscode-dark',  label: 'VS Code Dark Pro',    icon: '💻', sub: 'IDE Dark Slate & Classic VS Blue', font: "'JetBrains Mono', monospace", mode: 'Dark', swatches: ['#1e1e1e', '#007acc', '#4ec9b0'] },
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
  { id: 'chronos',      label: 'Chronos',             icon: '⏳', sub: 'Premium Time-Inspired Deep Navy',   font: "'Outfit', sans-serif",       mode: 'Dark',  swatches: ['#0F0F1A', '#4CC9F0', '#F5A623'] },
];






function KeyLockModal({ open, mode, error, password, setPassword, onClose, onSubmit }: {
  open: boolean; mode: 'unlock' | 'set'; error: string; password: string;
  setPassword: (v: string) => void; onClose: () => void; onSubmit: () => void;
}) {
  if (!open) return null;
  return (
    <div
      style={{ position: 'fixed', inset: 0, zIndex: 9999, background: 'rgba(0,0,0,0.6)', display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20 }}
      onClick={onClose}
    >
      <div
        className="glass"
        style={{ width: '100%', maxWidth: 360, padding: 20, display: 'flex', flexDirection: 'column', gap: 12 }}
        onClick={e => e.stopPropagation()}
      >
        <div style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-bright)' }}>
          {mode === 'unlock' ? '🔒 Enter password to reveal keys' : '🔒 Set key-reveal password'}
        </div>
        <div style={{ fontSize: 11, color: 'var(--text-dim)', lineHeight: 1.5 }}>
          {mode === 'unlock'
            ? 'Keys stay masked until you unlock. The session auto-locks after 10 minutes.'
            : 'Choose a password. It will be required to reveal API keys and secrets.'}
        </div>
        <input
          type="password"
          value={password}
          onChange={e => setPassword(e.target.value)}
          onKeyDown={e => { if (e.key === 'Enter') onSubmit(); }}
          placeholder={mode === 'unlock' ? 'password' : 'min. 4 characters'}
          className="input-base"
          autoFocus
        />
        {error && <div style={{ fontSize: 11, color: 'var(--danger)' }}>{error}</div>}
        <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 8 }}>
          <HoloButton type="button" variant="ghost" size="sm" onClick={onClose}>Cancel</HoloButton>
          <HoloButton type="button" variant="primary" size="sm" onClick={onSubmit}>
            {mode === 'unlock' ? 'Unlock' : 'Set password'}
          </HoloButton>
        </div>
      </div>
    </div>
  );
}

export default function Settings() {
  const { theme, setTheme, islandPosition, setIslandPosition, systemUsage, setModelName, gameMode, setGameMode } = useApp();
  const { isLowRam, toggleLowRamMode } = useLowRamMode();
  const [activeCategory, setActiveCategory] = useState<'models' | 'mascot' | 'voice' | 'guard' | 'spend' | 'integrations'>('models');
  const [provider, setProvider] = useState(() => localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama');
  const [modelSource, setModelSource] = useState(() => localStorage.getItem('MERIDIAN_MODEL_SOURCE') || (provider === 'ollama' ? 'local' : 'api'));
  const [ollamaHost, setOllamaHost] = useState(() => localStorage.getItem('OLLAMA_HOST') || 'http://localhost:11434');
  const [brainModel, setBrainModel] = useState(() => localStorage.getItem('MERIDIAN_MODEL') || '');
  const [visionModel, setVisionModel] = useState(() => localStorage.getItem('MERIDIAN_VISION_MODEL') || '');
  const [embeddingModel, setEmbeddingModel] = useState(() => localStorage.getItem('EMBEDDING_MODEL') || localStorage.getItem('embedding_model') || '');
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

  // Day 9 Spend & Air-Gap state
  const [spendStats, setSpendStats] = useState<any>({ monthly_cost_usd: 0, budget_cap_usd: 10, budget_exceeded: false, by_provider: {} });
  const [newBudgetCap, setNewBudgetCap] = useState('10.00');
  const [airgapStatus, setAirgapStatus] = useState<any>({ airgap_active: false, proof_badge: '' });
  const [budgetEnabled, setBudgetEnabled] = useState<boolean>(true);
  const [autonomousMode, setAutonomousMode] = useState<boolean>(true);
  const [securityGuardLevel, setSecurityGuardLevel] = useState<number>(1);
  // Manual mobile pairing (host / port / secret + server-side verification).
  const [pairHost, setPairHost] = useState('127.0.0.1');
  const [pairPort, setPairPort] = useState('8009');
  const [pairSecret, setPairSecret] = useState('');
  const fetchPairingInfo = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/p2p/pairing-info`);
      if (res.ok) {
        const data = await res.json();
        if (data.host) setPairHost(data.host);
        if (data.port) setPairPort(String(data.port));
      }
    } catch { /* noop */ }
  };
  const [pairStatus, setPairStatus] = useState<{ text: string; isError: boolean } | null>(null);
  const [isVerifyingPair, setIsVerifyingPair] = useState(false);

  const fetchSpendAndAirgap = async () => {
    try {
      const resSpend = await fetch(`${API_BASE_URL}/api/spend/stats`);
      if (resSpend.ok) {
        const data = await resSpend.json();
        setSpendStats(data);
        if (data.budget_cap_usd) setNewBudgetCap(String(data.budget_cap_usd));
        if (typeof data.budget_enabled === 'boolean') setBudgetEnabled(data.budget_enabled);
      }
      const resAirgap = await fetch(`${API_BASE_URL}/api/mode/airgap`);
      if (resAirgap.ok) {
        const data = await resAirgap.json();
        setAirgapStatus(data);
      }
      const resGuard = await fetch(`${API_BASE_URL}/api/mode/security_guard`);
      if (resGuard.ok) {
        const data = await resGuard.json();
        if (typeof data.level === 'number') setSecurityGuardLevel(data.level);
      }
      const resAuto = await fetch(`${API_BASE_URL}/api/mode/autonomous`);
      if (resAuto.ok) {
        const data = await resAuto.json();
        if (typeof data.autonomous_mode === 'boolean') setAutonomousMode(data.autonomous_mode);
      }
    } catch { /* noop */ }
  };

  const handleUpdateBudgetCap = async () => {
    const val = parseFloat(newBudgetCap);
    if (isNaN(val) || val <= 0) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/spend/budget`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget_cap_usd: val, enabled: budgetEnabled })
      });
      if (res.ok) fetchSpendAndAirgap();
    } catch { /* noop */ }
  };

  const handleToggleBudgetEnabled = async (enabled: boolean) => {
    setBudgetEnabled(enabled);
    try {
      const res = await fetch(`${API_BASE_URL}/api/spend/budget`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ budget_cap_usd: parseFloat(newBudgetCap) || 10.0, enabled })
      });
      if (res.ok) fetchSpendAndAirgap();
    } catch { /* noop */ }
  };

  const handleToggleSecurityGuard = async (level: number) => {
    setSecurityGuardLevel(level);
    try {
      const res = await fetch(`${API_BASE_URL}/api/mode/security_guard`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ level })
      });
      if (res.ok) {
        const data = await res.json();
        if (typeof data.level === 'number') setSecurityGuardLevel(data.level);
      }
    } catch { /* noop */ }
  };

  const handleToggleAutonomous = async (enabled: boolean) => {
    setAutonomousMode(enabled);
    try {
      const res = await fetch(`${API_BASE_URL}/api/mode/autonomous`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled })
      });
      if (res.ok) {
        const data = await res.json();
        if (typeof data.autonomous_mode === 'boolean') setAutonomousMode(data.autonomous_mode);
      }
    } catch { /* noop */ }
  };

  const handleVerifyPairing = async () => {
    setIsVerifyingPair(true);
    setPairStatus(null);
    try {
      const res = await fetch(`${API_BASE_URL}/api/p2p/verify-pairing`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ secret: pairSecret }),
      });
      if (res.ok) {
        setPairStatus({ text: `✅ Paired with ${pairHost}:${pairPort} successfully!`, isError: false });
      } else {
        setPairStatus({ text: '❌ Invalid pairing secret.', isError: true });
      }
    } catch {
      setPairStatus({ text: '❌ Verification failed: network error.', isError: true });
    } finally {
      setIsVerifyingPair(false);
    }
  };

  const handleToggleAirgap = async (enabled: boolean) => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/mode/airgap`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled })
      });
      if (res.ok) {
        const data = await res.json();
        setAirgapStatus(data);
      }
    } catch { /* noop */ }
  };

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
    fetchSpendAndAirgap();
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

  const [auditorModel, setAuditorModel] = useState(() => localStorage.getItem('meridian_auditor_model') || '');
  const [contextTokenLimit, setContextTokenLimit] = useState(() => parseInt(localStorage.getItem('context_token_limit') || '8192'));
  const [wakewordThreshold, setWakewordThreshold] = useState(() => parseFloat(localStorage.getItem('wakeword_threshold') || '0.6'));
  const [wakewordModel, setWakewordModel] = useState(() => localStorage.getItem('wakeword_model_filename') || 'hey_meridian.onnx');
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
  // Key-reveal lock: password required to unmask any API key / secret.
  const [keysUnlocked, setKeysUnlocked] = useState(() => isKeyLockUnlocked());
  const [lockModalOpen, setLockModalOpen] = useState(false);
  const [lockModalMode, setLockModalMode] = useState<'unlock' | 'set'>(() => (hasKeyLockPassword() ? 'unlock' : 'set'));
  const [lockPasswordInput, setLockPasswordInput] = useState('');
  const [lockError, setLockError] = useState('');

  const requestUnlock = () => {
    setLockModalMode(hasKeyLockPassword() ? 'unlock' : 'set');
    setLockError('');
    setLockPasswordInput('');
    setLockModalOpen(true);
  };

  const submitLockModal = async () => {
    if (lockModalMode === 'unlock') {
      const ok = await verifyKeyLockPassword(lockPasswordInput);
      if (!ok) { setLockError('Incorrect password.'); return; }
      unlockKeyLockSession();
      setKeysUnlocked(true);
      setLockModalOpen(false);
      setLockPasswordInput('');
      fetchVaultKeys(true);
    } else {
      if (lockPasswordInput.length < 4) { setLockError('Password must be at least 4 characters.'); return; }
      await setKeyLockPassword(lockPasswordInput);
      unlockKeyLockSession();
      setKeysUnlocked(true);
      setLockModalOpen(false);
      setLockPasswordInput('');
      fetchVaultKeys(true);
    }
  };

  const lockKeys = () => {
    lockKeyLockSession();
    setKeysUnlocked(false);
    setShowVaultSecrets(false);
    fetchVaultKeys(false);
  };
  const [vkName, setVkName] = useState('');
  const [vkEnvVar, setVkEnvVar] = useState('');
  const [vkSecret, setVkSecret] = useState('');
  const [vkBaseUrl, setVkBaseUrl] = useState('');
  const [vkCategory, setVkCategory] = useState('LLM Provider');

  const fetchVaultKeys = async (showFull = showVaultSecrets) => {
    // Never pull plaintext secrets while the key lock is engaged.
    const effective = showFull && (keysUnlocked || isKeyLockUnlocked());
    try {
      const res = await fetch(`${API_BASE_URL}/api/vault/keys?include_secrets=${effective}`);
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
    fetchPairingInfo();
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
          const names = d.models.map((m: any) => m.name || m);
          setAvailableOllamaModels(Array.from(new Set(names)));
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
          const names = d.models.map((m: any) => m.name || m);
          setAvailableBrainModels(Array.from(new Set(names)));
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
        <h1 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: 'var(--font-heading)' }}>Settings</h1>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', margin: '2px 0 8px', fontFamily: "'JetBrains Mono', monospace" }}>Configuration · Models · Appearance · Guard</p>

        {/* Category Navigation Bar */}
        <div className="subtab-bar">
          {SETTINGS_TABS.map(t => {
            const Icon = t.icon;
            const active = activeCategory === t.id;
            return (
              <button
                key={t.id}
                type="button"
                onClick={() => setActiveCategory(t.id as any)}
                className={`subtab-btn ${active ? 'subtab-btn-active' : ''}`}
              >
                <Icon size={13} />
                {t.label}
              </button>
            );
          })}
        </div>
      </div>

      {/* Key-reveal lock banner */}
      <div style={{ flexShrink: 0, marginBottom: 12, padding: '8px 12px', borderRadius: 8, background: keysUnlocked ? 'rgba(0,217,126,0.08)' : 'rgba(232,160,32,0.08)', border: `1px solid ${keysUnlocked ? 'rgba(0,217,126,0.3)' : 'rgba(232,160,32,0.3)'}`, display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
        <span style={{ fontSize: 11, color: 'var(--text-main)' }}>
          {keysUnlocked ? '🔓 Keys unlocked — auto-locks after 10 minutes.' : '🔒 API keys are masked. A password is required to reveal them.'}
        </span>
        {keysUnlocked ? (
          <button type="button" onClick={lockKeys} style={{ fontSize: 11, fontWeight: 700, background: 'none', border: 'none', cursor: 'pointer', color: 'var(--accent)' }}>
            Lock now
          </button>
        ) : (
          <button type="button" onClick={requestUnlock} style={{ fontSize: 11, fontWeight: 700, background: 'none', border: 'none', cursor: 'pointer', color: 'var(--accent)' }}>
            {hasKeyLockPassword() ? 'Unlock' : 'Set password'}
          </button>
        )}
      </div>
      <KeyLockModal open={lockModalOpen} mode={lockModalMode} error={lockError} password={lockPasswordInput} setPassword={setLockPasswordInput} onClose={() => setLockModalOpen(false)} onSubmit={submitLockModal} />

      <form onSubmit={handleSave} style={{ flex: 1, overflowY: 'auto', display: 'grid', gridTemplateColumns: '1fr 260px', gap: 16 }}>
        {/* Left: config */}
        <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>

          {activeCategory === 'models' && (
            <AiModelsTab
              providers={PROVIDERS}
              provider={provider}
              setProvider={setProvider}
              ollamaHost={ollamaHost}
              setOllamaHost={setOllamaHost}
              customBaseUrl={customBaseUrl}
              setCustomBaseUrl={setCustomBaseUrl}
              customModel={customModel}
              setCustomModel={setCustomModel}
              customApiKey={customApiKey}
              setCustomApiKey={setCustomApiKey}
              keysUnlocked={keysUnlocked}
              requestUnlock={requestUnlock}
              apiKeyForProvider={apiKeyForProvider}
              modelSource={modelSource}
              setModelSource={setModelSource}
              brainModel={brainModel}
              setBrainModel={setBrainModel}
              availableBrainModels={availableBrainModels}
              visionModel={visionModel}
              setVisionModel={setVisionModel}
              availableOllamaModels={availableOllamaModels}
              filterVisionModels={filterVisionModels}
              showAllVisionModels={showAllVisionModels}
              setShowAllVisionModels={setShowAllVisionModels}
              auditorModel={auditorModel}
              setAuditorModel={setAuditorModel}
              embeddingModel={embeddingModel}
              setEmbeddingModel={setEmbeddingModel}
              contextTokenLimit={contextTokenLimit}
              setContextTokenLimit={setContextTokenLimit}
              workspaceModel={workspaceModel}
              setWorkspaceModel={setWorkspaceModel}
              workspaceDirectives={workspaceDirectives}
              setWorkspaceDirectives={setWorkspaceDirectives}
              vaultKeys={vaultKeys}
              showVaultSecrets={showVaultSecrets}
              setShowVaultSecrets={setShowVaultSecrets}
              fetchVaultKeys={fetchVaultKeys}
              handleDeleteVaultKey={handleDeleteVaultKey}
              vkName={vkName}
              setVkName={setVkName}
              vkEnvVar={vkEnvVar}
              setVkEnvVar={setVkEnvVar}
              vkSecret={vkSecret}
              setVkSecret={setVkSecret}
              vkCategory={vkCategory}
              setVkCategory={setVkCategory}
              vkBaseUrl={vkBaseUrl}
              setVkBaseUrl={setVkBaseUrl}
              handleAddVaultKey={handleAddVaultKey}
              isKeyLockUnlocked={isKeyLockUnlocked}
            />
          )}

          {activeCategory === 'mascot' && (
            <MascotTab
              theme={theme}
              setTheme={setTheme}
              themeFilter={themeFilter}
              setThemeFilter={setThemeFilter}
              islandPosition={islandPosition}
              setIslandPosition={setIslandPosition}
              ttsVoice={ttsVoice}
              handleVoiceChange={handleVoiceChange}
              ttsVolume={ttsVolume}
              handleVolumeChange={handleVolumeChange}
              audioFxEnabled={audioFxEnabled}
              handleAudioFxChange={handleAudioFxChange}
              themes={THEMES}
            />
          )}

          {activeCategory === 'voice' && (
            <VoiceTab
              voiceResponseEnabled={voiceResponseEnabled}
              handleToggleVoiceResponse={handleToggleVoiceResponse}
              duplexActive={duplexActive}
              handleToggleDuplex={handleToggleDuplex}
              continuousActive={continuousActive}
              continuousRemaining={continuousRemaining}
              handleTriggerContinuousWindow={handleTriggerContinuousWindow}
              biometricsCount={biometricsCount}
              handleResetBiometrics={handleResetBiometrics}
              sttModelSize={sttModelSize}
              setSttModelSize={setSttModelSize}
              wakewordThreshold={wakewordThreshold}
              setWakewordThreshold={setWakewordThreshold}
              wakewordModel={wakewordModel}
              setWakewordModel={setWakewordModel}
              fileInputRef={fileInputRef}
              handleFileInputChange={handleFileInputChange}
              handleBrowseOnnxFile={handleBrowseOnnxFile}
              vaultKeys={vaultKeys}
              keysUnlocked={keysUnlocked}
              showVaultSecrets={showVaultSecrets}
              setShowVaultSecrets={setShowVaultSecrets}
              handleDeleteVaultKey={handleDeleteVaultKey}
              vkName={vkName}
              setVkName={setVkName}
              vkEnvVar={vkEnvVar}
              setVkEnvVar={setVkEnvVar}
              vkSecret={vkSecret}
              setVkSecret={setVkSecret}
              vkCategory={vkCategory}
              setVkCategory={setVkCategory}
              vkBaseUrl={vkBaseUrl}
              setVkBaseUrl={setVkBaseUrl}
              handleAddVaultKey={handleAddVaultKey}
            />
          )}

          {activeCategory === 'guard' && (
            <SystemGuardTab
              checkSystemUpdate={checkSystemUpdate}
              isCheckingUpdate={isCheckingUpdate}
              updateInfo={updateInfo}
              handleTriggerUpdate={handleTriggerUpdate}
              isTriggeringUpdate={isTriggeringUpdate}
              updateMsg={updateMsg}
              cpuWarn={cpuWarn}
              setCpuWarn={setCpuWarn}
              ramWarn={ramWarn}
              setRamWarn={setRamWarn}
              diskWarn={diskWarn}
              setDiskWarn={setDiskWarn}
              distractions={distractions}
              setDistractions={setDistractions}
              isLowRam={isLowRam}
              toggleLowRamMode={toggleLowRamMode}
              browserWidth={browserWidth}
              setBrowserWidth={setBrowserWidth}
              browserHeight={browserHeight}
              setBrowserHeight={setBrowserHeight}
              mcpServers={mcpServers}
              handleRemoveMcpServer={handleRemoveMcpServer}
              newServerName={newServerName}
              setNewServerName={setNewServerName}
              newServerCommand={newServerCommand}
              setNewServerCommand={setNewServerCommand}
              newServerArgs={newServerArgs}
              setNewServerArgs={setNewServerArgs}
              newServerEnv={newServerEnv}
              setNewServerEnv={setNewServerEnv}
              handleAddMcpServer={handleAddMcpServer}
              startupEnabled={startupEnabled}
              handleToggleStartup={handleToggleStartup}
              gameMode={gameMode}
              handleGameMode={handleGameMode}
              logLevel={logLevel}
              setLogLevel={setLogLevel}
              mongodbUri={mongodbUri}
              setMongodbUri={setMongodbUri}
              securityGuardLevel={securityGuardLevel}
              handleToggleSecurityGuard={handleToggleSecurityGuard}
              autonomousMode={autonomousMode}
              handleToggleAutonomous={handleToggleAutonomous}
              pairHost={pairHost}
              setPairHost={setPairHost}
              pairPort={pairPort}
              setPairPort={setPairPort}
              pairSecret={pairSecret}
              setPairSecret={setPairSecret}
              pairStatus={pairStatus}
              handleVerifyPairing={handleVerifyPairing}
              isVerifyingPair={isVerifyingPair}
            />
          )}

          {activeCategory === 'spend' && (
            <SpendAirGapTab
              airgapStatus={airgapStatus}
              handleToggleAirgap={handleToggleAirgap}
              budgetEnabled={budgetEnabled}
              handleToggleBudgetEnabled={handleToggleBudgetEnabled}
              newBudgetCap={newBudgetCap}
              setNewBudgetCap={setNewBudgetCap}
              handleUpdateBudgetCap={handleUpdateBudgetCap}
              spendStats={spendStats}
            />
          )}

          {activeCategory === 'integrations' && (
            <IntegrationsTab
              backendUrl={backendUrl}
              setBackendUrl={setBackendUrl}
              backendApiKey={backendApiKey}
              setBackendApiKey={setBackendApiKey}
              backendStatusMsg={backendStatusMsg}
              isTestingBackend={isTestingBackend}
              handleTestBackendConnection={handleTestBackendConnection}
              handleSaveBackendConfig={handleSaveBackendConfig}
              handleResetBackendConfig={handleResetBackendConfig}
              tavilyKey={tavilyKey}
              setTavilyKey={setTavilyKey}
              discordToken={discordToken}
              setDiscordToken={setDiscordToken}
              telegramToken={telegramToken}
              setTelegramToken={setTelegramToken}
              telegramChatId={telegramChatId}
              setTelegramChatId={setTelegramChatId}
              vaultKeys={vaultKeys}
              showVaultSecrets={showVaultSecrets}
              setShowVaultSecrets={setShowVaultSecrets}
              fetchVaultKeys={fetchVaultKeys}
              handleDeleteVaultKey={handleDeleteVaultKey}
              vkName={vkName}
              setVkName={setVkName}
              vkEnvVar={vkEnvVar}
              setVkEnvVar={setVkEnvVar}
              vkSecret={vkSecret}
              setVkSecret={setVkSecret}
              vkCategory={vkCategory}
              setVkCategory={setVkCategory}
              vkBaseUrl={vkBaseUrl}
              setVkBaseUrl={setVkBaseUrl}
              handleAddVaultKey={handleAddVaultKey}
              smtpEmail={smtpEmail}
              setSmtpEmail={setSmtpEmail}
              smtpPassword={smtpPassword}
              setSmtpPassword={setSmtpPassword}
              smtpServer={smtpServer}
              setSmtpServer={setSmtpServer}
              smtpPort={smtpPort}
              setSmtpPort={setSmtpPort}
              imapServer={imapServer}
              setImapServer={setImapServer}
              mcpServers={mcpServers}
              handleDeleteCustomMcpServer={handleDeleteCustomMcpServer}
              newServerName={newServerName}
              setNewServerName={setNewServerName}
              newServerCommand={newServerCommand}
              setNewServerCommand={setNewServerCommand}
              newServerArgs={newServerArgs}
              setNewServerArgs={setNewServerArgs}
              newServerEnv={newServerEnv}
              setNewServerEnv={setNewServerEnv}
              handleAddCustomMcpServer={handleAddCustomMcpServer}
              mcpCatalog={mcpCatalog}
              handleInstallMcp={handleInstallMcp}
              keysUnlocked={keysUnlocked}
              requestUnlock={requestUnlock}
              isKeyLockUnlocked={isKeyLockUnlocked}
            />
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
                <span style={{ fontSize: 9, padding: '2px 6px', borderRadius: 4, fontFamily: 'JetBrains Mono', background: isLowRam ? 'color-mix(in srgb, var(--success) 15%, transparent)' : 'var(--bg-surface)', color: isLowRam ? 'var(--success)' : 'var(--text-dim)' }}>
                  {isLowRam ? 'ACTIVE' : 'DISABLED'}
                </span>
              </div>
              <div style={{ fontSize: 10, color: 'var(--text-dim)', lineHeight: 1.4 }}>
                Disables canvas background particles to optimize memory footprint.
              </div>
              <HoloButton type="button" variant={isLowRam ? "ghost" : "primary"} size="sm" onClick={() => toggleLowRamMode()}>
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
