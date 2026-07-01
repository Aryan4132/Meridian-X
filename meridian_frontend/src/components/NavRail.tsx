import React from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  MessageSquare, Zap, Clipboard, Timer, Bot, Settings2,
  Eye, Minus, Square, X
} from 'lucide-react';
import { useApp, TabId } from '../AppContext';

import { getCurrentWindow } from '@tauri-apps/api/window';
import { invoke } from '@tauri-apps/api/core';

const NAV_ITEMS: { id: TabId; icon: React.ElementType; label: string }[] = [
  { id: 'timeline',    icon: MessageSquare, label: 'Timeline Logs' },
  { id: 'jobs',        icon: Zap,           label: 'Background Jobs' },
  { id: 'clipboard',   icon: Clipboard,     label: 'Clipboard History' },
  { id: 'productivity',icon: Timer,         label: 'Productivity HUD' },
  { id: 'lobby',       icon: Bot,           label: 'Swarm Debate' },
  { id: 'settings',    icon: Settings2,     label: 'Settings & Hardware' },
];

function HexLogo() {
  return (
    <svg width="32" height="32" viewBox="0 0 32 32" fill="none" style={{ filter: 'drop-shadow(0 0 8px var(--accent))' }}>
      <polygon points="16,2 28,9 28,23 16,30 4,23 4,9" fill="none" stroke="var(--accent)" strokeWidth="1.5" />
      <polygon points="16,8 22,11.5 22,20.5 16,24 10,20.5 10,11.5" fill="color-mix(in srgb, var(--accent) 12%, transparent)" stroke="var(--accent)" strokeWidth="1" strokeOpacity="0.5" />
      <circle cx="16" cy="16" r="3" fill="var(--accent)" opacity="0.9" />
    </svg>
  );
}

export default function NavRail() {
  const { activeTab, setActiveTab } = useApp();

  const handleMascot = () => {
    try { invoke('set_mascot_visible', { visible: true }); } catch { /* noop */ }
  };
  const handleMinimize = () => {
    try { getCurrentWindow().minimize(); } catch { /* noop */ }
  };
  const handleToggleMaximize = () => {
    try { getCurrentWindow().toggleMaximize(); } catch { /* noop */ }
  };
  const handleClose = () => {
    try { invoke('close_application'); } catch { /* noop */ }
  };

  return (
    <nav
      data-tauri-drag-region
      style={{
        width: 'var(--nav-width)',
        background: 'var(--bg-void)',
        borderRight: '1px solid var(--border-subtle)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '12px 0',
        flexShrink: 0,
        zIndex: 20,
        position: 'relative',
      }}
    >
      {/* Logo */}
      <div data-tauri-drag-region style={{ marginBottom: 16, padding: 8, cursor: 'move' }} title="Meridian-X">
        <HexLogo />
      </div>

      {/* Nav items */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 2, width: '100%', padding: '0 8px' }}>
        {NAV_ITEMS.map(({ id, icon: Icon, label }) => {
          const isActive = activeTab === id;
          return (
            <button
              key={id}
              onClick={() => setActiveTab(id)}
              title={label}
              style={{
                position: 'relative',
                width: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '10px 0',
                borderRadius: 'var(--radius-sm)',
                border: 'none',
                background: 'transparent',
                cursor: 'pointer',
                color: isActive ? 'var(--accent)' : 'var(--text-dim)',
                transition: 'color 0.15s ease',
              }}
              onMouseEnter={e => { if (!isActive) (e.currentTarget as HTMLElement).style.color = 'var(--text-main)'; }}
              onMouseLeave={e => { if (!isActive) (e.currentTarget as HTMLElement).style.color = 'var(--text-dim)'; }}
            >
              {isActive && (
                <div
                  style={{
                    position: 'absolute',
                    inset: 0,
                    borderRadius: 'var(--radius-sm)',
                    background: 'color-mix(in srgb, var(--accent) 8%, transparent)',
                    borderLeft: '2px solid var(--accent)',
                  }}
                />
              )}
              <Icon size={18} style={{ position: 'relative', zIndex: 1 }} />
            </button>
          );
        })}
      </div>

      {/* Bottom controls */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 2, width: '100%', padding: '8px 8px 0', borderTop: '1px solid var(--border-subtle)', marginTop: 4 }}>
        {[
          { action: handleMascot, icon: Eye, label: 'Mascot view', danger: false },
          { action: handleMinimize,       icon: Minus,  label: 'Minimize', danger: false },
          { action: handleToggleMaximize, icon: Square, label: 'Maximize', danger: false },
          { action: handleClose,          icon: X,      label: 'Close to tray', danger: true },
        ].map(({ action, icon: Icon, label, danger }) => (
          <button
            key={label}
            onClick={action}
            title={label}
            style={{
              display: 'flex', alignItems: 'center', justifyContent: 'center',
              padding: 8, borderRadius: 'var(--radius-sm)', border: 'none',
              background: 'transparent', cursor: 'pointer',
              color: 'var(--text-dim)', transition: 'color 0.15s ease',
            }}
            onMouseEnter={e => (e.currentTarget.style.color = danger ? 'var(--danger)' : 'var(--text-main)')}
            onMouseLeave={e => (e.currentTarget.style.color = 'var(--text-dim)')}
          >
            <Icon size={danger ? 14 : 16} />
          </button>
        ))}
      </div>
    </nav>
  );
}
