import React, { useState, useEffect } from 'react';
import { 
  Network, Code2, ShieldAlert, Compass, MousePointerClick, 
  Activity, Sparkles, Check, RefreshCw, Send, AlertTriangle, ArrowRight 
} from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';
import HoloButton from '../../components/ui/HoloButton';
import { API_BASE_URL } from '../../config';

interface TaskRouteConfig {
  provider: string;
  model: string;
  source: 'cloud' | 'local';
}

type TaskRoutesMap = Record<string, TaskRouteConfig>;

const DEFAULT_ROUTES: TaskRoutesMap = {
  ENGINEER:   { provider: 'deepseek',  model: 'deepseek-coder',             source: 'cloud' },
  REVIEWER:   { provider: 'anthropic', model: 'claude-3-5-sonnet-20241022', source: 'cloud' },
  RESEARCHER: { provider: 'gemini',    model: 'gemini-2.0-flash',           source: 'cloud' },
  OPERATOR:   { provider: 'openai',    model: 'gpt-4o',                     source: 'cloud' },
  ANALYST:    { provider: 'ollama',    model: 'qwen2.5-coder:7b',           source: 'local' },
  PROACTIVE:  { provider: 'ollama',    model: 'llama3.2:latest',            source: 'local' },
};

const MODE_METADATA: Record<string, { label: string; desc: string; icon: React.ComponentType<any>; color: string }> = {
  ENGINEER:   { label: 'Engineer Mode',   desc: 'Code generation, refactoring, debugging, syntax tests', icon: Code2,             color: '#7C3AED' },
  REVIEWER:   { label: 'Reviewer Mode',   desc: 'Security auditing, linting, code reviews, smell checks', icon: ShieldAlert,       color: '#CC785C' },
  RESEARCHER: { label: 'Researcher Mode', desc: 'Web search, paper summaries, documentation analysis',    icon: Compass,           color: '#4285F4' },
  OPERATOR:   { label: 'Operator Mode',   desc: 'Browser navigation, clicks, keystrokes, GUI automation', icon: MousePointerClick, color: '#00D97E' },
  ANALYST:    { label: 'Analyst Mode',    desc: 'System health, memory, CPU, database queries & logs',    icon: Activity,          color: '#F55036' },
  PROACTIVE:  { label: 'Proactive Mode',  desc: 'Background initiative, habit memory, next step nudges',  icon: Sparkles,          color: '#E8A020' },
};

const PROVIDER_OPTIONS = [
  { id: 'ollama',     label: 'Ollama (Local)',   source: 'local', defaultModel: 'qwen2.5-coder:7b' },
  { id: 'deepseek',   label: 'DeepSeek',         source: 'cloud', defaultModel: 'deepseek-coder' },
  { id: 'anthropic',  label: 'Anthropic Claude', source: 'cloud', defaultModel: 'claude-3-5-sonnet-20241022' },
  { id: 'gemini',     label: 'Google Gemini',    source: 'cloud', defaultModel: 'gemini-2.0-flash' },
  { id: 'openai',     label: 'OpenAI',           source: 'cloud', defaultModel: 'gpt-4o' },
  { id: 'groq',       label: 'Groq',             source: 'cloud', defaultModel: 'llama-3.3-70b-versatile' },
  { id: 'openrouter', label: 'OpenRouter',       source: 'cloud', defaultModel: 'anthropic/claude-3.5-sonnet' },
  { id: 'mistral',    label: 'Mistral',          source: 'cloud', defaultModel: 'codestral-latest' },
  { id: 'custom',     label: 'Custom API',       source: 'cloud', defaultModel: 'custom-model' },
];

const PRESET_MODELS: Record<string, string[]> = {
  ollama: ['qwen2.5-coder:7b', 'llama3.2:latest', 'deepseek-r1:8b', 'mistral:latest'],
  deepseek: ['deepseek-coder', 'deepseek-chat', 'deepseek-reasoner'],
  anthropic: ['claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022', 'claude-3-opus-20240229'],
  gemini: ['gemini-2.0-flash', 'gemini-1.5-pro', 'gemini-1.5-flash'],
  openai: ['gpt-4o', 'gpt-4o-mini', 'o3-mini', 'gpt-4-turbo'],
  groq: ['llama-3.3-70b-versatile', 'llama-3.1-8b-instant', 'mixtral-8x7b-32768'],
  openrouter: ['anthropic/claude-3.5-sonnet', 'openai/gpt-4o', 'deepseek/deepseek-r1'],
  mistral: ['codestral-latest', 'mistral-large-latest', 'pixtral-12b-2409'],
  custom: ['custom-model'],
};

export default function MultiModeTab() {
  const [enabled, setEnabled] = useState(false);
  const [routes, setRoutes] = useState<TaskRoutesMap>(DEFAULT_ROUTES);
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);
  
  // Simulator state
  const [testPrompt, setTestPrompt] = useState('Build a fast FastAPI endpoint and write unit tests for it');
  const [isSimulating, setIsSimulating] = useState(false);
  const [simResult, setSimResult] = useState<{
    classified_mode: string;
    target_model: string;
    target_provider: string;
    target_source: string;
    is_fallback: boolean;
  } | null>(null);

  useEffect(() => {
    fetch(`${API_BASE_URL}/api/settings/task-routes`)
      .then(res => res.json())
      .then(data => {
        if (data && data.status === 'success') {
          setEnabled(Boolean(data.enabled));
          if (data.routes && Object.keys(data.routes).length > 0) {
            setRoutes(prev => ({ ...prev, ...data.routes }));
          }
        }
      })
      .catch(err => console.warn('[MultiModeTab] Failed to load routes:', err));
  }, []);

  const handleToggleEnabled = async () => {
    const nextState = !enabled;
    setEnabled(nextState);
    try {
      await fetch(`${API_BASE_URL}/api/settings/task-routes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled: nextState, routes })
      });
    } catch (err) {
      console.error('[MultiModeTab] Failed to toggle enabled state:', err);
    }
  };

  const handleRouteChange = (mode: string, field: keyof TaskRouteConfig, value: string) => {
    setRoutes(prev => {
      const current = prev[mode] || { provider: 'ollama', model: '', source: 'local' };
      const updated = { ...current, [field]: value };
      if (field === 'provider') {
        const provDef = PROVIDER_OPTIONS.find(p => p.id === value);
        if (provDef) {
          updated.source = provDef.source as 'cloud' | 'local';
          if (!PRESET_MODELS[value]?.includes(updated.model)) {
            updated.model = provDef.defaultModel;
          }
        }
      }
      return { ...prev, [mode]: updated };
    });
  };

  const handleSaveAll = async () => {
    setIsSaving(true);
    setSaveSuccess(false);
    try {
      const res = await fetch(`${API_BASE_URL}/api/settings/task-routes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled, routes })
      });
      if (res.ok) {
        setSaveSuccess(true);
        setTimeout(() => setSaveSuccess(false), 2500);
      }
    } catch (err) {
      console.error('[MultiModeTab] Save error:', err);
    } finally {
      setIsSaving(false);
    }
  };

  const handleResetDefaults = () => {
    setRoutes(DEFAULT_ROUTES);
  };

  const handleSimulateRoute = async () => {
    if (!testPrompt.trim()) return;
    setIsSimulating(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/settings/task-routes/test`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: testPrompt })
      });
      if (res.ok) {
        const data = await res.json();
        setSimResult(data);
      }
    } catch (err) {
      console.error('[MultiModeTab] Simulation error:', err);
    } finally {
      setIsSimulating(false);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
      {/* Master Toggle Banner */}
      <GlowCard className="glass" style={{ padding: 18 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: 12 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ 
              width: 42, height: 42, borderRadius: 10, 
              background: enabled ? 'rgba(124, 58, 237, 0.2)' : 'var(--bg-surface)', 
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              border: enabled ? '1px solid #7C3AED' : '1px solid var(--border-subtle)',
              color: enabled ? '#A78BFA' : 'var(--text-dim)'
            }}>
              <Network size={22} />
            </div>
            <div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                <span style={{ fontSize: 14, fontWeight: 700, color: 'var(--text-bright)' }}>
                  Multi-Mode Dynamic Task Routing
                </span>
                <span style={{ 
                  fontSize: 10, fontWeight: 700, padding: '2px 8px', borderRadius: 12,
                  background: enabled ? 'rgba(52, 211, 153, 0.15)' : 'rgba(255, 255, 255, 0.05)',
                  color: enabled ? 'var(--success)' : 'var(--text-dim)',
                  border: enabled ? '1px solid var(--success)' : '1px solid var(--border-subtle)'
                }}>
                  {enabled ? 'ROUTING ACTIVE' : 'DISABLED (GLOBAL MODEL)'}
                </span>
              </div>
              <p style={{ fontSize: 11, color: 'var(--text-dim)', marginTop: 4, maxWidth: 640, lineHeight: 1.4 }}>
                When active, Meridian analyzes incoming user intent and dispatches each cognitive sub-task 
                to your dedicated model & provider (e.g., DeepSeek/Claude for coding, Gemini for research, local Ollama for health diagnostics).
              </p>
            </div>
          </div>

          <button
            type="button"
            onClick={handleToggleEnabled}
            style={{
              padding: '8px 18px',
              fontSize: 11,
              fontFamily: 'JetBrains Mono',
              fontWeight: 700,
              borderRadius: 'var(--radius-sm)',
              border: enabled ? '1px solid var(--success)' : '1px solid var(--border-subtle)',
              background: enabled ? 'rgba(52, 211, 153, 0.15)' : 'var(--bg-panel)',
              color: enabled ? 'var(--success)' : 'var(--text-main)',
              cursor: 'pointer',
              transition: 'all 0.2s ease',
              display: 'flex',
              alignItems: 'center',
              gap: 6
            }}
          >
            {enabled ? <Check size={14} /> : null}
            {enabled ? 'ENABLED' : 'ENABLE MULTI-MODE'}
          </button>
        </div>
      </GlowCard>

      {/* Per-Mode Configuration Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))', gap: 14 }}>
        {Object.entries(MODE_METADATA).map(([modeKey, meta]) => {
          const route = routes[modeKey] || DEFAULT_ROUTES[modeKey] || { provider: 'ollama', model: '', source: 'local' };
          const IconComponent = meta.icon;
          const providerModels = PRESET_MODELS[route.provider] || [];

          return (
            <GlowCard 
              key={modeKey} 
              className="glass" 
              style={{ 
                padding: 16, 
                opacity: enabled ? 1 : 0.75,
                transition: 'opacity 0.2s ease',
                display: 'flex',
                flexDirection: 'column',
                gap: 12,
                borderLeft: `3px solid ${meta.color}`
              }}
            >
              {/* Card Header */}
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                  <div style={{ 
                    padding: 6, borderRadius: 6, 
                    background: `${meta.color}20`, 
                    color: meta.color 
                  }}>
                    <IconComponent size={16} />
                  </div>
                  <div>
                    <div style={{ fontSize: 13, fontWeight: 700, color: 'var(--text-bright)' }}>
                      {meta.label}
                    </div>
                    <div style={{ fontSize: 10, color: 'var(--text-dim)' }}>
                      {meta.desc}
                    </div>
                  </div>
                </div>

                <span style={{
                  fontSize: 9, fontWeight: 700, textTransform: 'uppercase',
                  padding: '2px 6px', borderRadius: 4,
                  background: route.source === 'local' ? 'rgba(0, 217, 126, 0.1)' : 'rgba(66, 133, 244, 0.1)',
                  color: route.source === 'local' ? '#00D97E' : '#4285F4',
                  border: `1px solid ${route.source === 'local' ? 'rgba(0, 217, 126, 0.3)' : 'rgba(66, 133, 244, 0.3)'}`
                }}>
                  {route.source}
                </span>
              </div>

              {/* Provider & Model Pickers */}
              <div style={{ display: 'grid', gridTemplateColumns: '1fr 1.4fr', gap: 8, marginTop: 4 }}>
                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', display: 'block', marginBottom: 4 }}>
                    Provider
                  </label>
                  <select
                    value={route.provider}
                    disabled={!enabled}
                    onChange={(e) => handleRouteChange(modeKey, 'provider', e.target.value)}
                    style={{
                      width: '100%',
                      padding: '6px 8px',
                      fontSize: 11,
                      background: 'var(--bg-panel)',
                      color: 'var(--text-bright)',
                      border: '1px solid var(--border-subtle)',
                      borderRadius: 'var(--radius-sm)',
                      outline: 'none',
                      cursor: enabled ? 'pointer' : 'not-allowed'
                    }}
                  >
                    {PROVIDER_OPTIONS.map(opt => (
                      <option key={opt.id} value={opt.id}>
                        {opt.label}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label style={{ fontSize: 10, color: 'var(--text-dim)', display: 'block', marginBottom: 4 }}>
                    Model
                  </label>
                  {providerModels.length > 0 ? (
                    <select
                      value={route.model}
                      disabled={!enabled}
                      onChange={(e) => handleRouteChange(modeKey, 'model', e.target.value)}
                      style={{
                        width: '100%',
                        padding: '6px 8px',
                        fontSize: 11,
                        background: 'var(--bg-panel)',
                        color: 'var(--text-bright)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        outline: 'none',
                        cursor: enabled ? 'pointer' : 'not-allowed',
                        fontFamily: 'JetBrains Mono'
                      }}
                    >
                      {providerModels.map(m => (
                        <option key={m} value={m}>{m}</option>
                      ))}
                    </select>
                  ) : (
                    <input
                      type="text"
                      value={route.model}
                      disabled={!enabled}
                      onChange={(e) => handleRouteChange(modeKey, 'model', e.target.value)}
                      placeholder="Model identifier..."
                      style={{
                        width: '100%',
                        padding: '6px 8px',
                        fontSize: 11,
                        background: 'var(--bg-panel)',
                        color: 'var(--text-bright)',
                        border: '1px solid var(--border-subtle)',
                        borderRadius: 'var(--radius-sm)',
                        outline: 'none',
                        fontFamily: 'JetBrains Mono'
                      }}
                    />
                  )}
                </div>
              </div>
            </GlowCard>
          );
        })}
      </div>

      {/* Real-Time Routing Simulator */}
      <GlowCard className="glass" style={{ padding: 18 }}>
        <div className="section-label" style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 8 }}>
          <Sparkles size={14} color="var(--accent)" />
          Interactive Intent Route Simulator
        </div>
        <p style={{ fontSize: 11, color: 'var(--text-dim)', marginBottom: 12 }}>
          Test how any prompt will be classified and routed in real time against your configuration:
        </p>

        <div style={{ display: 'flex', gap: 8 }}>
          <input
            type="text"
            value={testPrompt}
            onChange={(e) => setTestPrompt(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleSimulateRoute()}
            placeholder="Type a sample user command..."
            style={{
              flex: 1,
              padding: '8px 12px',
              fontSize: 12,
              background: 'var(--bg-panel)',
              color: 'var(--text-bright)',
              border: '1px solid var(--border-subtle)',
              borderRadius: 'var(--radius-sm)',
              outline: 'none'
            }}
          />
          <HoloButton
            onClick={handleSimulateRoute}
            disabled={isSimulating || !testPrompt.trim()}
            loading={isSimulating}
            size="sm"
          >
            <Send size={13} />
            Test Route
          </HoloButton>
        </div>

        {simResult && (
          <div style={{ 
            marginTop: 12, padding: 12, 
            background: 'var(--bg-surface)', 
            borderRadius: 'var(--radius-sm)', 
            border: '1px solid var(--border-subtle)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            flexWrap: 'wrap',
            gap: 10
          }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <div style={{
                padding: '4px 8px', borderRadius: 6,
                background: 'rgba(124, 58, 237, 0.2)',
                color: '#A78BFA',
                fontWeight: 700,
                fontSize: 11
              }}>
                {simResult.classified_mode}
              </div>
              <ArrowRight size={14} color="var(--text-dim)" />
              <div style={{ fontSize: 12, color: 'var(--text-bright)', fontFamily: 'JetBrains Mono' }}>
                {simResult.target_provider.toUpperCase()} &middot; {simResult.target_model}
              </div>
              <span style={{
                fontSize: 9, padding: '2px 6px', borderRadius: 4,
                background: simResult.target_source === 'local' ? 'rgba(0, 217, 126, 0.1)' : 'rgba(66, 133, 244, 0.1)',
                color: simResult.target_source === 'local' ? '#00D97E' : '#4285F4'
              }}>
                {simResult.target_source}
              </span>
            </div>

            {simResult.is_fallback && (
              <div style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 11, color: 'var(--warning)' }}>
                <AlertTriangle size={13} />
                <span>Default fallback (multi-mode disabled or missing cloud key)</span>
              </div>
            )}
          </div>
        )}
      </GlowCard>

      {/* Save & Reset Actions */}
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'flex-end', gap: 10, marginTop: 4 }}>
        <button
          type="button"
          onClick={handleResetDefaults}
          style={{
            padding: '8px 14px',
            fontSize: 11,
            background: 'transparent',
            color: 'var(--text-dim)',
            border: '1px solid var(--border-subtle)',
            borderRadius: 'var(--radius-sm)',
            cursor: 'pointer'
          }}
        >
          Reset to Defaults
        </button>

        <HoloButton
          onClick={handleSaveAll}
          disabled={isSaving}
          loading={isSaving}
          size="sm"
        >
          {saveSuccess ? <Check size={14} /> : null}
          {saveSuccess ? 'Saved!' : 'Save Multi-Mode Routes'}
        </HoloButton>
      </div>
    </div>
  );
}
