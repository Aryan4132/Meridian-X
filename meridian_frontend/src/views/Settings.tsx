import React, { useState, useEffect } from 'react';
import { invoke } from '@tauri-apps/api/core';
import { motion, AnimatePresence } from 'motion/react';
import { RefreshCw, Check, Eye, EyeOff, Save, Plus, Trash2, Cpu, Sparkles, Mic, ShieldCheck, DollarSign, Plug, FolderOpen, Search, Download, Loader2 } from 'lucide-react';
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

          {/* Category: Spend & Air-Gap */}
          {activeCategory === 'spend' && (
            <>
              {/* Cloud Spend & Token Meter */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <span>Cloud Spend & Token Meter</span>
                  {spendStats.budget_exceeded && (
                    <span style={{ fontSize: 10, background: 'color-mix(in srgb, var(--danger) 15%, transparent)', color: 'var(--danger)', padding: '2px 8px', borderRadius: 'var(--radius-sm)', fontWeight: 700 }}>
                      BUDGET EXCEEDED — LOCAL FALLBACK ACTIVE
                    </span>
                  )}
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 16, marginTop: 12 }}>
                  {/* Progress Bar */}
                  <div>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: 12, marginBottom: 6, color: 'var(--text-main)', fontWeight: 600 }}>
                      <span>30-Day LLM Spend: ${spendStats.monthly_cost_usd?.toFixed(4)} USD</span>
                      <span>Cap: ${spendStats.budget_cap_usd?.toFixed(2)} USD</span>
                    </div>
                    <div style={{ width: '100%', height: 8, background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', overflow: 'hidden', border: '1px solid var(--border-subtle)' }}>
                      <div
                        style={{
                          height: '100%',
                          width: `${Math.min(100, ((spendStats.monthly_cost_usd || 0) / (spendStats.budget_cap_usd || 1)) * 100)}%`,
                          background: spendStats.budget_exceeded ? 'var(--danger)' : 'var(--accent)',
                          transition: 'width 0.3s ease'
                        }}
                      />
                    </div>
                  </div>

                  {/* Budget Cap Setter */}
                  <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                    <label style={{ fontSize: 11, color: 'var(--text-dim)', minWidth: 120 }}>Monthly Cap (USD):</label>
                    <input
                      type="number"
                      step="0.5"
                      value={newBudgetCap}
                      onChange={e => setNewBudgetCap(e.target.value)}
                      style={{ width: 100, padding: '6px 10px', borderRadius: 'var(--radius-sm)', background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', fontSize: 12 }}
                    />
                    <button
                      type="button"
                      onClick={handleUpdateBudgetCap}
                      style={{ padding: '6px 14px', borderRadius: 'var(--radius-sm)', background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', fontWeight: 600, fontSize: 12, cursor: 'pointer' }}
                    >
                      Update Cap
                    </button>
                  </div>

                  {/* Budget Enable/Disable Toggle */}
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', paddingTop: 8, borderTop: '1px solid var(--border-subtle)' }}>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-main)' }}>Enforce Spend Budget Cap</div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Automatically fall back to local model when cap is reached.</div>
                    </div>
                    <button
                      type="button"
                      onClick={async () => {
                        try {
                          const res = await fetch(`${API_BASE_URL}/api/spend/budget`, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ enabled: !spendStats.budget_enabled })
                          });
                          if (res.ok) fetchSpendAndAirgap();
                        } catch { /* noop */ }
                      }}
                      style={{
                        padding: '6px 14px', borderRadius: 16, border: 'none',
                        background: spendStats.budget_enabled !== false ? 'var(--success)' : 'var(--bg-surface)',
                        color: spendStats.budget_enabled !== false ? 'var(--bg-void)' : 'var(--text-dim)',
                        fontWeight: 700, fontSize: 11, cursor: 'pointer'
                      }}
                    >
                      {spendStats.budget_enabled !== false ? 'ENFORCING' : 'DISABLED'}
                    </button>
                  </div>
                </div>
              </GlowCard>

              {/* Mobile Manual Pairing */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">Mobile App Pairing</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 10, marginTop: 10 }}>
                  <div style={{ fontSize: 11, color: 'var(--text-dim)' }}>
                    Enter the desktop host, port and pairing secret from the Meridian-X mobile app, then verify.
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: 8 }}>
                    <div>
                      <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Desktop Host</label>
                      <input type="text" value={pairHost} onChange={e => setPairHost(e.target.value)} placeholder="127.0.0.1" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                    </div>
                    <div>
                      <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Port</label>
                      <input type="text" value={pairPort} onChange={e => setPairPort(e.target.value)} placeholder="4133" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                    </div>
                  </div>
                  <div>
                    <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Pairing Secret</label>
                    <input type="password" value={pairSecret} onChange={e => setPairSecret(e.target.value)} placeholder="paste pairing secret" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                  </div>
                  {pairStatus && (
                    <div style={{ fontSize: 11, color: pairStatus.isError ? 'var(--danger)' : 'var(--success)' }}>{pairStatus.text}</div>
                  )}
                  <HoloButton type="button" variant="primary" size="sm" onClick={handleVerifyPairing} loading={isVerifyingPair} disabled={!pairSecret.trim()}>
                    Verify Pairing
                  </HoloButton>
                </div>
              </GlowCard>

              {/* Local-Only Air-Gap Control */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">Local-Only Air-Gap Mode (OPS-04)</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 14, marginTop: 12 }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div>
                      <div style={{ fontSize: 13, fontWeight: 600, color: 'var(--text-main)' }}>Hard Network Air-Gap</div>
                      <div style={{ fontSize: 11, color: 'var(--text-dim)', marginTop: 2 }}>Blocks all non-loopback outbound cloud and remote API requests.</div>
                    </div>

                    <button
                      type="button"
                      onClick={() => handleToggleAirgap(!airgapStatus.airgap_active)}
                      style={{
                        padding: '8px 18px', borderRadius: 20, border: 'none',
                        background: airgapStatus.airgap_active ? 'var(--success)' : 'var(--bg-surface)',
                        color: airgapStatus.airgap_active ? 'var(--bg-void)' : 'var(--text-dim)',
                        fontWeight: 700, fontSize: 12, cursor: 'pointer', transition: 'all 0.2s ease'
                      }}
                    >
                      {airgapStatus.airgap_active ? 'ENABLED (AIR-GAPPED)' : 'DISABLED'}
                    </button>
                  </div>

                  {airgapStatus.airgap_active && (
                    <div style={{ padding: 12, borderRadius: 'var(--radius-sm)', background: 'color-mix(in srgb, var(--success) 8%, transparent)', border: '1px solid var(--success)', display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                        <span style={{ fontSize: 11, fontWeight: 700, color: 'var(--success)' }}>PROOF BADGE: {airgapStatus.proof_badge}</span>
                        <span style={{ fontSize: 10, color: 'var(--text-dim)' }}>Verified: {airgapStatus.verified_at}</span>
                      </div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'monospace', wordBreak: 'break-all' }}>
                        Sig: {airgapStatus.signature}
                      </div>
                    </div>
                  )}
                </div>
              </GlowCard>
            </>
          )}

          {/* Category: System Guard */}
          {activeCategory === 'guard' && (
            <>
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">System Guard & PC Execution Security</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 16, marginTop: 12 }}>
                  <div style={{ padding: 12, borderRadius: 8, background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)' }}>
                    <div style={{ fontSize: 13, fontWeight: 700, color: '#f87171', marginBottom: 4 }}>
                      Unrestricted PC Access Mode (Level 0)
                    </div>
                    <div style={{ fontSize: 11, color: 'var(--text-dim)' }}>
                      Grants Meridian-X full automated execution rights across the PC. Bypasses confirmation gates for system commands, process management, and file operations.
                    </div>
                  </div>

                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 600, color: 'var(--text-main)' }}>Level 1 Security (Human Confirmation Gates)</div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>Require confirmation before running destructive OS actions.</div>
                    </div>
                    <button
                      type="button"
                      onClick={async () => {
                        try {
                          const res = await fetch(`${API_BASE_URL}/api/mode/security_guard`, {
                            method: 'POST',
                            headers: { 'Content-Type': 'application/json' },
                            body: JSON.stringify({ level: 0 })
                          });
                          if (res.ok) alert('Unrestricted PC Access Mode Enabled.');
                        } catch { /* noop */ }
                      }}
                      style={{ padding: '6px 14px', borderRadius: 16, border: 'none', background: 'var(--danger)', color: '#fff', fontWeight: 700, fontSize: 11, cursor: 'pointer' }}
                    >
                      Bypass / Enable Level 0 Mode
                    </button>
                  </div>
                </div>
              </GlowCard>
            </>
          )}

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
          )}

          {/* Category: Integrations */}
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
                      <span style={{ fontSize: 9, background: 'var(--bg-surface)', padding: '2px 6px', borderRadius: 'var(--radius-sm)', textTransform: 'uppercase' }}>{updateInfo.update_type}</span>
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

              {/* Security Guard Level 0/1 */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">🛡️ System Guard & Execution Rights</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
                    <button
                      type="button"
                      onClick={() => handleToggleSecurityGuard(1)}
                      style={{
                        padding: 12,
                        textAlign: 'left',
                        borderRadius: 'var(--radius-sm)',
                        border: securityGuardLevel === 1 ? '1.5px solid var(--accent)' : '1px solid var(--border-subtle)',
                        background: securityGuardLevel === 1 ? 'var(--bg-surface)' : 'var(--bg-panel)',
                        cursor: 'pointer'
                      }}
                    >
                      <div style={{ fontSize: 12, fontWeight: 700, color: securityGuardLevel === 1 ? 'var(--accent)' : 'var(--text-bright)' }}>
                        Level 1: Standard Guard
                      </div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 4 }}>
                        Requires confirmation prompt before running OS shell commands or mutating files.
                      </div>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleToggleSecurityGuard(0)}
                      style={{
                        padding: 12,
                        textAlign: 'left',
                        borderRadius: 'var(--radius-sm)',
                        border: securityGuardLevel === 0 ? '1.5px solid var(--danger)' : '1px solid var(--border-subtle)',
                        background: securityGuardLevel === 0 ? 'rgba(239, 68, 68, 0.12)' : 'var(--bg-panel)',
                        cursor: 'pointer'
                      }}
                    >
                      <div style={{ fontSize: 12, fontWeight: 700, color: securityGuardLevel === 0 ? 'var(--danger)' : 'var(--text-bright)' }}>
                        Level 0: Unrestricted PC Access Mode
                      </div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 4 }}>
                        Bypasses approval gates. Allows Meridian-X full unrestricted OS execution without confirmation prompts.
                      </div>
                    </button>
                  </div>
                </div>
              </GlowCard>

              {/* Continuous Autonomous Loop Mode */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">🔄 Autonomous Continuous Loop Mode</div>
                <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                  <div>
                    <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Continuous Autonomous ReAct Loop</div>
                    <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                      Auto-continues multi-turn tool execution without requiring manual "continue" prompts.
                    </div>
                  </div>
                  <button
                    type="button"
                    onClick={() => handleToggleAutonomous(!autonomousMode)}
                    style={{
                      padding: '6px 14px',
                      fontSize: 11,
                      fontFamily: 'JetBrains Mono',
                      fontWeight: 600,
                      borderRadius: 'var(--radius-sm)',
                      border: autonomousMode ? '1px solid var(--accent-2)' : '1px solid var(--border-subtle)',
                      background: autonomousMode ? 'rgba(52, 211, 153, 0.15)' : 'var(--bg-panel)',
                      color: autonomousMode ? 'var(--accent-2)' : 'var(--text-dim)',
                      cursor: 'pointer'
                    }}
                  >
                    {autonomousMode ? '⚡ ENABLED (AUTO)' : '⏸️ MANUAL STEP'}
                  </button>
                </div>
              </GlowCard>

              {/* Mobile Manual Pairing */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">📱 Desktop-to-Mobile App Pairing</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
                    Pair Meridian Mobile companion app to sync backend control, voice triggers, and agent status. Enter details manually and verify.
                  </div>
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr 100px', gap: 8 }}>
                    <div>
                      <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Desktop Host</label>
                      <input type="text" value={pairHost} onChange={e => setPairHost(e.target.value)} placeholder="127.0.0.1" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                    </div>
                    <div>
                      <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Port</label>
                      <input type="text" value={pairPort} onChange={e => setPairPort(e.target.value)} placeholder="4133" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                    </div>
                  </div>
                  <div>
                    <label style={{ fontSize: 9, color: 'var(--text-dim)', display: 'block', marginBottom: 3 }}>Pairing Secret</label>
                    <input type="password" value={pairSecret} onChange={e => setPairSecret(e.target.value)} placeholder="paste pairing secret" className="input-base" style={{ height: 32, fontSize: 11, fontFamily: 'JetBrains Mono' }} />
                  </div>
                  {pairStatus && (
                    <div style={{ fontSize: 11, color: pairStatus.isError ? 'var(--danger)' : 'var(--success)' }}>{pairStatus.text}</div>
                  )}
                  <div>
                    <HoloButton type="button" variant="primary" size="sm" onClick={handleVerifyPairing} loading={isVerifyingPair} disabled={!pairSecret.trim()}>
                      Verify Pairing
                    </HoloButton>
                  </div>
                </div>
              </GlowCard>
            </>
          )}

          {/* Category: Spend & Air-Gap */}
          {activeCategory === 'spend' && (
            <>
              {/* Air-Gap Mode */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">🔒 Air-Gap Mode & Network Isolation</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Local-Only Air-Gap Isolation</div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                        Hard-blocks all cloud AI providers, remote Ollama servers, and external network calls. Forces 100% local model inference.
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={() => handleToggleAirgap(!airgapStatus.airgap_active)}
                      style={{
                        padding: '6px 14px',
                        fontSize: 11,
                        fontFamily: 'JetBrains Mono',
                        fontWeight: 600,
                        borderRadius: 'var(--radius-sm)',
                        border: airgapStatus.airgap_active ? '1px solid var(--success)' : '1px solid var(--border-subtle)',
                        background: airgapStatus.airgap_active ? 'rgba(52, 211, 153, 0.15)' : 'var(--bg-panel)',
                        color: airgapStatus.airgap_active ? 'var(--success)' : 'var(--text-main)',
                        cursor: 'pointer'
                      }}
                    >
                      {airgapStatus.airgap_active ? '🔒 AIR-GAP ACTIVE' : '🌐 CLOUD ALLOWED'}
                    </button>
                  </div>
                  {airgapStatus.proof_badge && (
                    <div style={{ fontSize: 10, color: 'var(--accent)', fontFamily: 'JetBrains Mono', background: 'var(--accent-muted)', padding: '6px 10px', borderRadius: 'var(--radius-sm)' }}>
                      Proof Badge: {airgapStatus.proof_badge}
                    </div>
                  )}
                </div>
              </GlowCard>

              {/* Monthly Spend Budget Cap & Toggle */}
              <GlowCard className="glass" style={{ padding: 16 }}>
                <div className="section-label">💰 Monthly LLM Spend Budget & Cap Controls</div>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                  
                  {/* Enable / Disable Budget Enforcement Toggle */}
                  <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div>
                      <div style={{ fontSize: 12, fontWeight: 700, color: 'var(--text-bright)' }}>Enforce Spend Budget Cap</div>
                      <div style={{ fontSize: 10, color: 'var(--text-dim)', marginTop: 2 }}>
                        Automatically block API calls when monthly spend exceeds your cap threshold.
                      </div>
                    </div>
                    <button
                      type="button"
                      onClick={() => handleToggleBudgetEnabled(!budgetEnabled)}
                      style={{
                        padding: '6px 14px',
                        fontSize: 11,
                        fontFamily: 'JetBrains Mono',
                        fontWeight: 600,
                        borderRadius: 'var(--radius-sm)',
                        border: budgetEnabled ? '1px solid var(--accent)' : '1px solid var(--border-subtle)',
                        background: budgetEnabled ? 'var(--accent-muted)' : 'var(--bg-panel)',
                        color: budgetEnabled ? 'var(--accent)' : 'var(--text-dim)',
                        cursor: 'pointer'
                      }}
                    >
                      {budgetEnabled ? 'ON (ENFORCED)' : 'OFF (DISABLED)'}
                    </button>
                  </div>

                  {/* Budget Limit Input */}
                  <div style={{ display: 'grid', gridTemplateColumns: '1fr auto', gap: 10, alignItems: 'end' }}>
                    <div>
                      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4, textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                        Monthly Spend Cap ($ USD)
                      </label>
                      <input
                        type="number"
                        step="0.50"
                        min="1.00"
                        value={newBudgetCap}
                        onChange={e => setNewBudgetCap(e.target.value)}
                        className="input-base"
                        style={{ fontFamily: 'JetBrains Mono' }}
                      />
                    </div>
                    <HoloButton type="button" variant="primary" size="sm" onClick={handleUpdateBudgetCap}>
                      Save Cap
                    </HoloButton>
                  </div>

                  {/* Current Monthly Cost Stats Meter */}
                  <div style={{ padding: '12px', background: 'var(--bg-surface)', borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                      <span style={{ fontSize: 11, color: 'var(--text-main)', fontFamily: 'JetBrains Mono' }}>Current Month Spend</span>
                      <span style={{ fontSize: 13, fontWeight: 700, color: spendStats.budget_exceeded ? 'var(--danger)' : 'var(--accent)', fontFamily: 'JetBrains Mono' }}>
                        ${Number(spendStats.monthly_cost_usd || 0).toFixed(4)} / ${Number(spendStats.budget_cap_usd || 10).toFixed(2)}
                      </span>
                    </div>
                    <div style={{ width: '100%', height: 6, background: 'var(--bg-panel)', borderRadius: 3, overflow: 'hidden' }}>
                      <div
                        style={{
                          width: `${Math.min(100, ((spendStats.monthly_cost_usd || 0) / (spendStats.budget_cap_usd || 10)) * 100)}%`,
                          height: '100%',
                          background: spendStats.budget_exceeded ? 'var(--danger)' : 'var(--accent)',
                          transition: 'width 0.3s ease'
                        }}
                      />
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
