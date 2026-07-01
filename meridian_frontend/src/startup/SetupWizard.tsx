import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { ArrowRight, Bot, RefreshCw, CheckCircle, ChevronDown, ChevronUp } from 'lucide-react';
import HoloButton from '../components/ui/HoloButton';

interface SetupWizardProps { onComplete: () => void; }

const PROVIDERS = [
  { id: 'ollama',    label: 'Ollama',    sub: 'Offline · Free',       color: '#00D97E' },
  { id: 'openai',   label: 'OpenAI',    sub: 'Cloud · API Key',       color: '#74AA9C' },
  { id: 'anthropic',label: 'Anthropic', sub: 'Cloud · API Key',       color: '#CC785C' },
  { id: 'gemini',   label: 'Gemini',    sub: 'Cloud · API Key',       color: '#4285F4' },
  { id: 'deepseek', label: 'DeepSeek',  sub: 'Cloud · API Key',       color: '#7C3AED' },
];

const PROVIDER_MODELS: Record<string, string[]> = {
  openai:    ['gpt-4o', 'gpt-4-turbo', 'gpt-3.5-turbo'],
  anthropic: ['claude-3-5-sonnet-20241022', 'claude-3-5-haiku-20241022', 'claude-3-opus-20240229'],
  gemini:    ['gemini-1.5-pro', 'gemini-1.5-flash', 'gemini-1.0-pro'],
  deepseek:  ['deepseek-chat', 'deepseek-coder'],
};

// Progress bar for steps
function StepBar({ step }: { step: number }) {
  return (
    <div style={{ display: 'flex', gap: 4, marginBottom: 28 }}>
      {[1, 2, 3, 4].map(s => (
        <div
          key={s}
          style={{
            height: 3,
            flex: 1,
            borderRadius: 99,
            background: s <= step ? 'var(--accent)' : 'var(--bg-surface)',
            boxShadow: s === step ? '0 0 8px var(--accent)' : 'none',
            transition: 'background 0.3s ease, box-shadow 0.3s ease',
          }}
        />
      ))}
    </div>
  );
}

export default function SetupWizard({ onComplete }: SetupWizardProps) {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);

  // Step 2 — integrations
  const [tavilyKey, setTavilyKey]           = useState(() => localStorage.getItem('TAVILY_API_KEY') || '');
  const [discordToken, setDiscordToken]     = useState(() => localStorage.getItem('DISCORD_BOT_TOKEN') || '');
  const [telegramToken, setTelegramToken]   = useState(() => localStorage.getItem('TELEGRAM_BOT_TOKEN') || '');
  const [telegramChatId, setTelegramChatId] = useState(() => localStorage.getItem('TELEGRAM_CHAT_ID') || '');
  const [whatsappPhone, setWhatsappPhone]   = useState(() => localStorage.getItem('WHATSAPP_PHONE') || '');
  const [openSection, setOpenSection]       = useState<string | null>(null);

  // Step 3 — model
  const [selectedProvider, setSelectedProvider] = useState(() => localStorage.getItem('MERIDIAN_PROVIDER') || 'ollama');
  const [selectedModel, setSelectedModel]       = useState(() => localStorage.getItem('MERIDIAN_MODEL') || '');
  const [ollamaHost, setOllamaHost]             = useState(() => localStorage.getItem('OLLAMA_HOST') || 'http://localhost:11434');
  const [ollamaStatus, setOllamaStatus]         = useState<'idle' | 'ok' | 'fail'>('idle');
  const [ollamaModels, setOllamaModels]         = useState<string[]>([]);
  const [openaiKey, setOpenaiKey]               = useState(() => localStorage.getItem('OPENAI_API_KEY') || '');
  const [anthropicKey, setAnthropicKey]         = useState(() => localStorage.getItem('ANTHROPIC_API_KEY') || '');
  const [geminiKey, setGeminiKey]               = useState(() => localStorage.getItem('GEMINI_API_KEY') || '');
  const [deepseekKey, setDeepseekKey]           = useState(() => localStorage.getItem('DEEPSEEK_API_KEY') || '');

  // Set default models when provider changes
  useEffect(() => {
    if (selectedProvider !== 'ollama') {
      const models = PROVIDER_MODELS[selectedProvider] || [];
      if (!models.includes(selectedModel)) setSelectedModel(models[0] || '');
    } else {
      testOllama();
    }
  }, [selectedProvider]);

  const testOllama = async () => {
    setLoading(true);
    setOllamaStatus('idle');
    setOllamaModels([]);
    try {
      const res = await fetch(`http://localhost:4132/api/ollama-models?host=${encodeURIComponent(ollamaHost)}`).catch(() => null);
      if (res?.ok) {
        const data = await res.json();
        const models = (data.models || []).map((m: any) => m.name || m);
        setOllamaModels(models);
        setOllamaStatus('ok');
        if (!models.includes(selectedModel)) {
          const pref = models.find((m: string) => m.includes('qwen2.5-coder'));
          setSelectedModel(pref || models[0] || '');
        }
      } else { setOllamaStatus('fail'); }
    } catch { setOllamaStatus('fail'); }
    finally { setLoading(false); }
  };

  const saveSettings = async () => {
    localStorage.setItem('TAVILY_API_KEY', tavilyKey);
    localStorage.setItem('DISCORD_BOT_TOKEN', discordToken);
    localStorage.setItem('TELEGRAM_BOT_TOKEN', telegramToken);
    localStorage.setItem('TELEGRAM_CHAT_ID', telegramChatId);
    localStorage.setItem('WHATSAPP_PHONE', whatsappPhone);
    localStorage.setItem('MERIDIAN_PROVIDER', selectedProvider);
    localStorage.setItem('MERIDIAN_MODEL', selectedModel);
    localStorage.setItem('OLLAMA_HOST', ollamaHost);
    localStorage.setItem('OPENAI_API_KEY', openaiKey);
    localStorage.setItem('ANTHROPIC_API_KEY', anthropicKey);
    localStorage.setItem('GEMINI_API_KEY', geminiKey);
    localStorage.setItem('DEEPSEEK_API_KEY', deepseekKey);
    localStorage.setItem('firstRunCompleted', 'true');
    try {
      await fetch('http://localhost:4132/api/profile/save', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          tavily_key: tavilyKey, discord_token: discordToken,
          telegram_token: telegramToken, telegram_chat_id: telegramChatId,
          whatsapp_phone: whatsappPhone, meridian_provider: selectedProvider,
          meridian_model: selectedModel, ollama_host: ollamaHost,
          openai_key: openaiKey, anthropic_key: anthropicKey,
          gemini_key: geminiKey, deepseek_key: deepseekKey,
        }),
      });
    } catch { /* saved locally */ }
  };

  const handleNext = () => {
    if (step === 3) { saveSettings(); }
    setStep(s => Math.min(s + 1, 4) as any);
  };

  // API key field helper
  const apiKeyForProvider = () => {
    const sets: Record<string, [string, (v: string) => void, string]> = {
      openai:    [openaiKey,    setOpenaiKey,    'sk-proj-...'],
      anthropic: [anthropicKey, setAnthropicKey, 'sk-ant-...'],
      gemini:    [geminiKey,    setGeminiKey,    'AIzaSy...'],
      deepseek:  [deepseekKey,  setDeepseekKey,  'sk-...'],
    };
    return sets[selectedProvider];
  };

  // Accordion for integrations
  const AccordionSection = ({ id, title, icon, children }: { id: string; title: string; icon: string; children: React.ReactNode }) => {
    const open = openSection === id;
    return (
      <div style={{ border: '1px solid var(--border-subtle)', borderRadius: 'var(--radius-sm)', overflow: 'hidden' }}>
        <button
          type="button"
          onClick={() => setOpenSection(open ? null : id)}
          style={{
            width: '100%', display: 'flex', alignItems: 'center', justifyContent: 'space-between',
            padding: '10px 14px', background: open ? 'var(--bg-surface)' : 'transparent',
            border: 'none', cursor: 'pointer', color: 'var(--text-main)', transition: 'background 0.15s ease',
          }}
        >
          <span style={{ fontSize: 13, fontWeight: 500 }}>{icon} {title}</span>
          {open ? <ChevronUp size={14} style={{ color: 'var(--text-dim)' }} /> : <ChevronDown size={14} style={{ color: 'var(--text-dim)' }} />}
        </button>
        <AnimatePresence initial={false}>
          {open && (
            <motion.div
              initial={{ height: 0 }}
              animate={{ height: 'auto' }}
              exit={{ height: 0 }}
              transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
              style={{ overflow: 'hidden' }}
            >
              <div style={{ padding: '12px 14px', borderTop: '1px solid var(--border-subtle)', display: 'flex', flexDirection: 'column', gap: 10 }}>
                {children}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    );
  };

  return (
    <div style={{
      minHeight: '100vh', display: 'flex', alignItems: 'center', justifyContent: 'center',
      background: 'var(--bg-base)', padding: 24, position: 'relative',
    }}>
      <div className="void-bg" />

      {/* Decorative hex (top-right) */}
      <div style={{ position: 'fixed', top: -40, right: -40, opacity: 0.15, pointerEvents: 'none' }}>
        <svg width="240" height="240" viewBox="0 0 240 240" fill="none">
          <polygon points="120,10 210,62 210,178 120,230 30,178 30,62" fill="none" stroke="var(--accent)" strokeWidth="1.5" />
          <polygon points="120,40 185,77 185,163 120,200 55,163 55,77" fill="none" stroke="var(--accent)" strokeWidth="1" strokeOpacity="0.5" />
          <circle cx="120" cy="120" r="20" fill="none" stroke="var(--accent)" strokeWidth="1" />
        </svg>
      </div>

      <div
        className="holo-border"
        style={{ width: '100%', maxWidth: 520, position: 'relative', zIndex: 1 }}
      >
        <div className="glass" style={{ padding: 32 }}>
          {/* Header */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 20 }}>
            <svg width="24" height="24" viewBox="0 0 32 32" fill="none" style={{ filter: 'drop-shadow(0 0 6px var(--accent))' }}>
              <polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="var(--accent)" strokeWidth="2" />
              <circle cx="16" cy="16" r="4" fill="var(--accent)" />
            </svg>
            <span style={{ fontSize: 16, fontWeight: 700, color: 'var(--text-bright)', fontFamily: "'Space Grotesk', sans-serif" }}>
              Meridian-X Setup
            </span>
          </div>

          <StepBar step={step} />

          {/* Step content */}
          <AnimatePresence mode="wait">
            <motion.div
              key={step}
              initial={{ opacity: 0, x: 16 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -16 }}
              transition={{ duration: 0.2, ease: [0.16, 1, 0.3, 1] }}
              style={{ minHeight: 300 }}
            >
              {/* ── Step 1: Welcome ── */}
              {step === 1 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 16 }}>
                  <h1 style={{ fontSize: 24, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>
                    Welcome to<br />
                    <span style={{ color: 'var(--accent)' }}>Meridian-X</span>
                  </h1>
                  <p style={{ fontSize: 13, color: 'var(--text-main)', lineHeight: 1.6, margin: 0 }}>
                    Your autonomous local intelligence layer. Built for developers who want an AI companion that works offline, respects privacy, and doesn't slow down your machine.
                  </p>
                  <div style={{ display: 'flex', gap: 10, marginTop: 4 }}>
                    {[
                      { icon: '🔒', label: 'Privacy-first' },
                      { icon: '📡', label: 'Offline-capable' },
                      { icon: '🧠', label: 'ReAct reasoning' },
                    ].map(({ icon, label }) => (
                      <div key={label} style={{
                        display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px',
                        background: 'var(--bg-surface)', border: '1px solid var(--border-subtle)',
                        borderRadius: 99, fontSize: 12, color: 'var(--text-main)',
                      }}>
                        <span>{icon}</span><span>{label}</span>
                      </div>
                    ))}
                  </div>
                  <div style={{
                    marginTop: 8, padding: '12px 14px', background: 'color-mix(in srgb, var(--accent) 6%, transparent)',
                    border: '1px solid color-mix(in srgb, var(--accent) 20%, transparent)', borderRadius: 'var(--radius-sm)',
                    fontSize: 12, color: 'var(--text-dim)', lineHeight: 1.5,
                  }}>
                    Choose between fully <strong style={{ color: 'var(--text-main)' }}>offline execution</strong> (local Ollama + ONNX voice) or <strong style={{ color: 'var(--text-main)' }}>cloud AI providers</strong> via API key. You can switch at any time.
                  </div>
                </div>
              )}

              {/* ── Step 2: Integrations ── */}
              {step === 2 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                  <div>
                    <h2 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: '0 0 4px', fontFamily: "'Space Grotesk', sans-serif" }}>Connect Your Services</h2>
                    <p style={{ fontSize: 12, color: 'var(--text-dim)', margin: 0 }}>All optional. Configure later in Settings.</p>
                  </div>

                  <AccordionSection id="search" title="Web Search" icon="🌐">
                    <div>
                      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>TAVILY API KEY</label>
                      <input type="password" placeholder="tvly-..." value={tavilyKey} onChange={e => setTavilyKey(e.target.value)} className="input-base" />
                    </div>
                  </AccordionSection>

                  <AccordionSection id="notifs" title="Notifications" icon="💬">
                    <div>
                      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>DISCORD BOT TOKEN</label>
                      <input type="password" placeholder="MT..." value={discordToken} onChange={e => setDiscordToken(e.target.value)} className="input-base" />
                    </div>
                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8 }}>
                      <div>
                        <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>TELEGRAM TOKEN</label>
                        <input type="password" placeholder="bot..." value={telegramToken} onChange={e => setTelegramToken(e.target.value)} className="input-base" />
                      </div>
                      <div>
                        <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>CHAT ID</label>
                        <input type="text" placeholder="123..." value={telegramChatId} onChange={e => setTelegramChatId(e.target.value)} className="input-base" />
                      </div>
                    </div>
                    <div>
                      <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>WHATSAPP PHONE (E.164)</label>
                      <input type="text" placeholder="+1234567890" value={whatsappPhone} onChange={e => setWhatsappPhone(e.target.value)} className="input-base" />
                    </div>
                  </AccordionSection>
                </div>
              )}

              {/* ── Step 3: Brain Model ── */}
              {step === 3 && (
                <div style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                  <div>
                    <h2 style={{ fontSize: 18, fontWeight: 700, color: 'var(--text-bright)', margin: '0 0 4px', fontFamily: "'Space Grotesk', sans-serif" }}>Intelligence Engine</h2>
                    <p style={{ fontSize: 12, color: 'var(--text-dim)', margin: 0 }}>Select your primary AI provider.</p>
                  </div>

                  {/* Provider card grid */}
                  <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 8 }}>
                    {PROVIDERS.map(p => {
                      const active = selectedProvider === p.id;
                      return (
                        <button
                          key={p.id}
                          type="button"
                          onClick={() => setSelectedProvider(p.id)}
                          style={{
                            padding: '10px 8px', borderRadius: 'var(--radius-sm)',
                            border: active ? `1px solid ${p.color}` : '1px solid var(--border-subtle)',
                            background: active ? `${p.color}12` : 'var(--bg-surface)',
                            cursor: 'pointer', textAlign: 'center', transition: 'all 0.15s ease',
                            boxShadow: active ? `0 0 12px ${p.color}20` : 'none',
                          }}
                        >
                          <div style={{ fontSize: 12, fontWeight: 600, color: active ? p.color : 'var(--text-main)', marginBottom: 2 }}>{p.label}</div>
                          <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>{p.sub}</div>
                        </button>
                      );
                    })}
                  </div>

                  {/* Provider-specific config */}
                  <AnimatePresence mode="wait">
                    <motion.div
                      key={selectedProvider}
                      initial={{ opacity: 0, height: 0 }}
                      animate={{ opacity: 1, height: 'auto' }}
                      exit={{ opacity: 0, height: 0 }}
                      transition={{ duration: 0.2 }}
                      style={{ overflow: 'hidden', display: 'flex', flexDirection: 'column', gap: 10 }}
                    >
                      {selectedProvider === 'ollama' ? (
                        <>
                          <div>
                            <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>OLLAMA HOST URL</label>
                            <div style={{ display: 'flex', gap: 8 }}>
                              <input type="text" value={ollamaHost} onChange={e => setOllamaHost(e.target.value)} className="input-base" style={{ fontFamily: "'JetBrains Mono', monospace" }} />
                              <HoloButton variant="ghost" size="sm" onClick={testOllama} loading={loading}>
                                <RefreshCw size={12} /> Test
                              </HoloButton>
                            </div>
                          </div>
                          <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ fontSize: 10, fontFamily: 'JetBrains Mono', color: 'var(--text-dim)' }}>STATUS:</span>
                            <span className={ollamaStatus === 'ok' ? 'badge badge-success' : ollamaStatus === 'fail' ? 'badge badge-danger' : 'badge badge-dim'}>
                              {ollamaStatus === 'ok' ? '● Connected' : ollamaStatus === 'fail' ? '✕ Offline' : '… Checking'}
                            </span>
                          </div>
                          {ollamaModels.length > 0 && (
                            <div>
                              <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', marginBottom: 6 }}>SELECT MODEL:</div>
                              <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                                {ollamaModels.map(m => (
                                  <button key={m} type="button" onClick={() => setSelectedModel(m)}
                                    className={selectedModel === m ? 'badge badge-accent' : 'badge badge-dim'}
                                    style={{ cursor: 'pointer', border: '1px solid' }}
                                  >{m}</button>
                                ))}
                              </div>
                            </div>
                          )}
                          {ollamaStatus === 'fail' && (
                            <div className="badge badge-danger" style={{ fontSize: 11, padding: '8px 10px', width: '100%', borderRadius: 'var(--radius-sm)', lineHeight: 1.5 }}>
                              Ollama not found. Make sure it's running, then click Test.
                            </div>
                          )}
                        </>
                      ) : (
                        (() => {
                          const cfg = apiKeyForProvider();
                          if (!cfg) return null;
                          const [val, setter, ph] = cfg;
                          return (
                            <>
                              <div>
                                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 4 }}>API KEY</label>
                                <input type="password" placeholder={ph} value={val} onChange={e => setter(e.target.value)} className="input-base" />
                              </div>
                              <div>
                                <label style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: 'JetBrains Mono', display: 'block', marginBottom: 6 }}>MODEL</label>
                                <div style={{ display: 'flex', flexWrap: 'wrap', gap: 6 }}>
                                  {(PROVIDER_MODELS[selectedProvider] || []).map(m => (
                                    <button key={m} type="button" onClick={() => setSelectedModel(m)}
                                      className={selectedModel === m ? 'badge badge-accent' : 'badge badge-dim'}
                                      style={{ cursor: 'pointer', border: '1px solid' }}
                                    >{m}</button>
                                  ))}
                                </div>
                              </div>
                            </>
                          );
                        })()
                      )}
                    </motion.div>
                  </AnimatePresence>
                </div>
              )}

              {/* ── Step 4: Complete ── */}
              {step === 4 && (
                <div style={{ textAlign: 'center', padding: '24px 0', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16 }}>
                  <motion.div
                    initial={{ scale: 0.5, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    transition={{ type: 'spring', stiffness: 300, damping: 20 }}
                    style={{ color: 'var(--success)', filter: 'drop-shadow(0 0 16px var(--success))' }}
                  >
                    <CheckCircle size={64} />
                  </motion.div>
                  <h2 style={{ fontSize: 22, fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: "'Space Grotesk', sans-serif" }}>Configuration Complete</h2>
                  <p style={{ fontSize: 13, color: 'var(--text-dim)', maxWidth: 320, lineHeight: 1.6, margin: 0 }}>
                    Settings saved and intelligence parameters registered. Meridian-X is ready.
                  </p>
                  <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap', justifyContent: 'center' }}>
                    {['Alt+M  Toggle Shell', 'Alt+V  Voice PTT', 'Alt+Shift+M  Mascot'].map(hint => (
                      <div key={hint} style={{
                        fontSize: 11, fontFamily: "'JetBrains Mono', monospace",
                        color: 'var(--accent)', padding: '4px 10px',
                        background: 'color-mix(in srgb, var(--accent) 8%, transparent)',
                        border: '1px solid color-mix(in srgb, var(--accent) 20%, transparent)',
                        borderRadius: 'var(--radius-sm)',
                      }}>{hint}</div>
                    ))}
                  </div>
                </div>
              )}
            </motion.div>
          </AnimatePresence>

          {/* Navigation footer */}
          <div style={{ display: 'flex', justifyContent: 'space-between', marginTop: 24, paddingTop: 20, borderTop: '1px solid var(--border-subtle)' }}>
            {step > 1 && step < 4 ? (
              <HoloButton variant="ghost" size="sm" onClick={() => setStep(s => (s - 1) as any)}>← Back</HoloButton>
            ) : <div />}

            {step < 4 ? (
              <HoloButton variant="primary" size="md" onClick={handleNext}>
                Continue <ArrowRight size={14} />
              </HoloButton>
            ) : (
              <HoloButton variant="primary" size="md" onClick={onComplete}>
                Launch Meridian-X <Bot size={14} />
              </HoloButton>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
