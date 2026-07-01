import React from 'react';
import { useApp } from '../AppContext';
import DataBadge from './ui/DataBadge';

export default function StatusBar() {
  const { backendAlive, modelName, systemUsage } = useApp();
  const shortModel = modelName.split(':')[0] + (modelName.includes(':') ? ':' + modelName.split(':')[1]?.slice(0, 6) : '');

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

      {/* Center: wordmark */}
      <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
        <svg width="12" height="12" viewBox="0 0 32 32" fill="none">
          <polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="var(--accent)" strokeWidth="2" />
          <circle cx="16" cy="16" r="3" fill="var(--accent)" />
        </svg>
        <span style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", letterSpacing: '0.12em', fontWeight: 600 }}>
          MERIDIAN-X
        </span>
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
