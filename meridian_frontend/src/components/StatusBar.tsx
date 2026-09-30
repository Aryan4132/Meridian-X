import React from 'react';
import { useApp } from '../AppContext';
import { API_BASE_URL } from '../config';
import DataBadge from './ui/DataBadge';

export default function StatusBar() {
  const { backendAlive, modelName, systemUsage } = useApp();
  const [airgapActive, setAirgapActive] = React.useState(false);
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
    <div
      style={{
        height: 'var(--statusbar-height)',
        background: 'var(--bg-void)',
        borderTop: '1px solid var(--border-subtle)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        padding: '0 16px',
        flexShrink: 0,
        zIndex: 10,
      }}
    >
      {/* Left: daemon status */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <span style={{
          width: 6, height: 6, borderRadius: '50%',
          background: backendAlive ? 'var(--success)' : 'var(--danger)',
          boxShadow: backendAlive ? '0 0 6px var(--success)' : 'none',
          display: 'inline-block',
          animation: backendAlive ? 'pulse-glow-kf 2s ease-in-out infinite' : 'none',
        }} />
        <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
          {backendAlive ? 'Backend Online' : 'Backend Offline'}
        </span>
      </div>

      {/* Center: wordmark & airgap badge */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
          <svg width="12" height="12" viewBox="0 0 32 32" fill="none">
            <polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="var(--accent)" strokeWidth="2" />
            <circle cx="16" cy="16" r="3" fill="var(--accent)" />
          </svg>
          <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.12em', fontWeight: 600 }}>
            MERIDIAN-X
          </span>
        </div>

        {airgapActive && (
          <span style={{
            fontSize: 9, fontWeight: 700, padding: '1px 6px', borderRadius: 4,
            background: 'rgba(34, 197, 94, 0.15)', color: '#4ade80', border: '1px solid rgba(34, 197, 94, 0.3)',
            fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.05em'
          }}>
            AIR-GAP VERIFIED
          </span>
        )}
      </div>

      {/* Right: model + usage */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
          {shortModel}
        </span>
        <DataBadge label="CPU" value={`${systemUsage.cpu}%`} color={systemUsage.cpu > 80 ? 'danger' : systemUsage.cpu > 60 ? 'warning' : 'dim'} />
        <DataBadge label="RAM" value={`${systemUsage.ram}%`} color={systemUsage.ram > 85 ? 'danger' : 'dim'} />
      </div>
    </div>
  );
}
