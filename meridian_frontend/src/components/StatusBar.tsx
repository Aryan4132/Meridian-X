import React, { useState } from 'react';
import { QrCode, Shield, Cpu, Activity } from 'lucide-react';
import MobilePairingModal from './mobile/MobilePairingModal';
import { useApp } from '../AppContext';
import { API_BASE_URL } from '../config';

export default function StatusBar() {
  const { backendAlive, modelName, systemUsage } = useApp();
  const [airgapActive, setAirgapActive] = React.useState(false);
  const [pairingModalOpen, setPairingModalOpen] = useState(false);
  const shortModel = modelName.split(':')[0] + (modelName.includes(':') ? ':' + modelName.split(':')[1]?.slice(0, 6) : '');

  React.useEffect(() => {
    const checkAirgap = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/mode/airgap`);
        if (res.ok) {
          const data = await res.json();
          setAirgapActive(!!data.airgap_active);
        }
      } catch { /* noop */ }
    };
    checkAirgap();
    const interval = setInterval(checkAirgap, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <>
      <footer
        style={{
          height: 'var(--statusbar-height, 32px)',
          background: 'color-mix(in srgb, var(--bg-void) 94%, transparent)',
          backdropFilter: 'blur(16px)',
          WebkitBackdropFilter: 'blur(16px)',
          borderTop: '1px solid var(--border-subtle)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0 16px',
          flexShrink: 0,
          zIndex: 10,
          userSelect: 'none',
        }}
      >
        {/* Left: Engine connection status */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 6,
            padding: '2px 8px',
            borderRadius: 9999,
            background: backendAlive ? 'rgba(52, 211, 153, 0.08)' : 'rgba(248, 113, 113, 0.08)',
            border: `1px solid ${backendAlive ? 'rgba(52, 211, 153, 0.25)' : 'rgba(248, 113, 113, 0.25)'}`,
          }}>
            <span style={{
              width: 6,
              height: 6,
              borderRadius: '50%',
              background: backendAlive ? 'var(--success, #34d399)' : 'var(--danger, #f87171)',
              boxShadow: backendAlive ? '0 0 8px var(--success, #34d399)' : 'none',
              display: 'inline-block',
            }} />
            <span style={{
              fontSize: 10,
              fontWeight: 600,
              color: backendAlive ? 'var(--success, #34d399)' : 'var(--danger, #f87171)',
              fontFamily: "'JetBrains Mono', monospace",
              letterSpacing: '0.02em',
            }}>
              {backendAlive ? 'ENGINE ONLINE' : 'ENGINE OFFLINE'}
            </span>
          </div>
        </div>

        {/* Center: Brand badge & Airgap verification */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
            <svg width="12" height="12" viewBox="0 0 32 32" fill="none">
              <polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="var(--accent)" strokeWidth="2.5" />
              <circle cx="16" cy="16" r="3.5" fill="var(--accent)" />
            </svg>
            <span style={{
              fontSize: 10,
              color: 'var(--text-bright)',
              fontFamily: "var(--font-heading, 'Outfit', sans-serif)",
              letterSpacing: '0.08em',
              fontWeight: 700
            }}>
              MERIDIAN-X
            </span>
          </div>

          {airgapActive && (
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: 4,
              fontSize: 9,
              fontWeight: 700,
              padding: '2px 7px',
              borderRadius: 'var(--radius-sm, 6px)',
              background: 'color-mix(in srgb, var(--success) 14%, transparent)',
              color: 'var(--success)',
              border: '1px solid var(--success)',
              fontFamily: 'var(--font-mono, monospace)',
              letterSpacing: '0.05em'
            }}>
              <Shield size={10} />
              AIR-GAP VERIFIED
            </span>
          )}
        </div>

        {/* Right: Active model, hardware gauges, mobile link */}
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{
            fontSize: 10,
            color: 'var(--text-dim)',
            fontFamily: "'JetBrains Mono', monospace",
            background: 'rgba(255, 255, 255, 0.03)',
            padding: '2px 7px',
            borderRadius: 4,
            border: '1px solid var(--border-subtle)',
          }}>
            {shortModel}
          </span>

          {/* Mini CPU meter */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 10, fontFamily: "'JetBrains Mono', monospace" }}>
            <span style={{ color: 'var(--text-dim)' }}>CPU</span>
            <div style={{ width: 36, height: 4, background: 'rgba(255, 255, 255, 0.08)', borderRadius: 2, overflow: 'hidden' }}>
              <div style={{
                width: `${Math.min(100, systemUsage.cpu)}%`,
                height: '100%',
                background: systemUsage.cpu > 80 ? 'var(--danger)' : systemUsage.cpu > 60 ? 'var(--warning)' : 'var(--accent)',
                transition: 'width 0.4s ease',
              }} />
            </div>
            <span style={{ color: systemUsage.cpu > 80 ? 'var(--danger)' : 'var(--text-dim)', minWidth: 24 }}>
              {systemUsage.cpu}%
            </span>
          </div>

          {/* Mini RAM meter */}
          <div style={{ display: 'flex', alignItems: 'center', gap: 4, fontSize: 10, fontFamily: "'JetBrains Mono', monospace" }}>
            <span style={{ color: 'var(--text-dim)' }}>RAM</span>
            <div style={{ width: 36, height: 4, background: 'rgba(255, 255, 255, 0.08)', borderRadius: 2, overflow: 'hidden' }}>
              <div style={{
                width: `${Math.min(100, systemUsage.ram)}%`,
                height: '100%',
                background: systemUsage.ram > 85 ? 'var(--danger)' : 'var(--accent-2)',
                transition: 'width 0.4s ease',
              }} />
            </div>
            <span style={{ color: systemUsage.ram > 85 ? 'var(--danger)' : 'var(--text-dim)', minWidth: 24 }}>
              {systemUsage.ram}%
            </span>
          </div>

          {/* Mobile Link trigger button */}
          <button
            onClick={() => setPairingModalOpen(true)}
            style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: 5,
              padding: '3px 9px',
              borderRadius: 6,
              background: 'color-mix(in srgb, var(--accent, #00f0ff) 12%, rgba(20, 24, 35, 0.7))',
              border: '1px solid color-mix(in srgb, var(--accent, #00f0ff) 30%, transparent)',
              color: 'var(--accent, #00f0ff)',
              fontSize: 10,
              fontWeight: 600,
              cursor: 'pointer',
              fontFamily: "'JetBrains Mono', monospace",
              transition: 'all 0.15s ease',
            }}
            onMouseEnter={e => {
              e.currentTarget.style.background = 'color-mix(in srgb, var(--accent, #00f0ff) 22%, rgba(20, 24, 35, 0.85))';
              e.currentTarget.style.boxShadow = '0 0 10px color-mix(in srgb, var(--accent, #00f0ff) 25%, transparent)';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.background = 'color-mix(in srgb, var(--accent, #00f0ff) 12%, rgba(20, 24, 35, 0.7))';
              e.currentTarget.style.boxShadow = 'none';
            }}
            title="Pair Mobile Companion (LAN / QR Code)"
          >
            <QrCode size={11} />
            <span>Mobile Link</span>
          </button>
        </div>
      </footer>

      <MobilePairingModal
        isOpen={pairingModalOpen}
        onClose={() => setPairingModalOpen(false)}
      />
    </>
  );
}
