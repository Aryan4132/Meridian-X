import React from 'react';
import { Check } from 'lucide-react';
import GlowCard from '../../components/ui/GlowCard';

export interface ThemeOption {
  id: string;
  label: string;
  icon: string;
  sub: string;
  font: string;
  mode: string;
  swatches: string[];
}

export interface MascotTabProps {
  theme: string;
  setTheme: (t: string) => void;
  themeFilter: 'all' | 'dark' | 'light';
  setThemeFilter: (f: 'all' | 'dark' | 'light') => void;
  islandPosition: string;
  setIslandPosition: (pos: any) => void;
  ttsVoice: string;
  handleVoiceChange: (v: string) => void;
  ttsVolume: number;
  handleVolumeChange: (v: number) => void;
  audioFxEnabled: boolean;
  handleAudioFxChange: (v: boolean) => void;
  themes: readonly ThemeOption[];
}

export default function MascotTab({
  theme,
  setTheme,
  themeFilter,
  setThemeFilter,
  islandPosition,
  setIslandPosition,
  ttsVoice,
  handleVoiceChange,
  ttsVolume,
  handleVolumeChange,
  audioFxEnabled,
  handleAudioFxChange,
  themes,
}: MascotTabProps) {
  return (
    <>
      {/* Theme & Design Styles Selector */}
      <GlowCard className="glass" style={{ padding: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 10 }}>
          <div className="section-label" style={{ margin: 0 }}>Design Styles & Themes</div>
          <span style={{ fontSize: 10, fontFamily: 'JetBrains Mono', color: 'var(--accent)', background: 'var(--accent-muted)', padding: '2px 8px', borderRadius: 4 }}>
            15 STYLES AVAILABLE
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
              {tab === 'all' ? 'All (15)' : tab === 'dark' ? '🌙 Dark (11)' : '☀️ Light (4)'}
            </button>
          ))}
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(240px, 1fr))', gap: 10, maxHeight: 420, overflowY: 'auto', paddingRight: 2 }}>
          {themes.filter(t => themeFilter === 'all' || (themeFilter === 'dark' ? t.mode === 'Dark' : t.mode === 'Light')).map(t => {
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
                <div style={{ display: 'flex', gap: 3, flexShrink: 0, padding: 3, background: t.swatches[0], borderRadius: 'var(--radius-sm)', border: '1px solid var(--border-subtle)' }}>
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
                      background: 'var(--accent-muted)',
                      color: 'var(--accent)',
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
                    <Check size={12} color="var(--bg-void)" strokeWidth={3} />
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
  );
}
