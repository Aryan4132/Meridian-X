import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  MessageSquare, Zap, Clipboard, Timer, Bot, Settings2, Network, Brain,
  Eye, Minus, Square, X, ChevronRight, ChevronLeft
} from 'lucide-react';
import { useApp, TabId } from '../AppContext';
import { MascotCharacter } from '../Mascot';

import { getCurrentWindow } from '@tauri-apps/api/window';
import { invoke } from '@tauri-apps/api/core';

const NAV_ITEMS: { id: TabId; icon: React.ElementType; label: string }[] = [
  { id: 'timeline',    icon: MessageSquare, label: 'Timeline Logs' },
  { id: 'jobs',        icon: Zap,           label: 'Background Jobs' },
  { id: 'clipboard',   icon: Clipboard,     label: 'Clipboard History' },
  { id: 'productivity',icon: Timer,         label: 'Productivity HUD' },
  { id: 'lobby',       icon: Bot,           label: 'Swarm Debate' },
  { id: 'workflows',   icon: Network,       label: 'Workflow Automation' },
  { id: 'memory',      icon: Brain,         label: 'Memory Editor' },
  { id: 'settings',    icon: Settings2,     label: 'Settings & Hardware' },
];

export default function NavRail() {
  const { activeTab, setActiveTab } = useApp();
  const [isExpanded, setIsExpanded] = useState(false);

  const handleMascot = () => {
    if ((window as any).__TAURI_INTERNALS__) {
      try { invoke('set_mascot_visible', { visible: true }); } catch { /* noop */ }
    }
  };
  const handleMinimize = () => {
    if ((window as any).__TAURI_INTERNALS__) {
      try { getCurrentWindow().minimize(); } catch { /* noop */ }
    }
  };
  const handleToggleMaximize = () => {
    if ((window as any).__TAURI_INTERNALS__) {
      try { getCurrentWindow().toggleMaximize(); } catch { /* noop */ }
    }
  };
   const handleClose = () => {
     if ((window as any).__TAURI_INTERNALS__) {
       // Show confirmation dialog to prevent accidental closure
       if (window.confirm('Are you sure you want to close Meridian-X? This will stop all background processes.')) {
         try { invoke('close_application'); } catch { /* noop */ }
       }
     }
   };

  return (
    <motion.nav
      data-tauri-drag-region
      initial={false}
      animate={{ width: isExpanded ? 200 : 64 }}
      transition={{ duration: 0.25, ease: 'easeInOut' }}
      onMouseEnter={() => setIsExpanded(true)}
      onMouseLeave={() => setIsExpanded(false)}
      style={{
        background: 'var(--bg-void)',
        borderRight: '1px solid var(--border-subtle)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '12px 0',
        flexShrink: 0,
        zIndex: 20,
        position: 'relative',
        overflow: 'hidden',
      }}
    >
      {/* Mascot Logo */}
      <div 
        onClick={handleMascot}
        style={{ marginBottom: 16, padding: 4, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' }} 
        title="Meridian-X Mascot (Click to summon companion)"
      >
        <MascotCharacter state="default" accentColor="var(--accent)" />
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
                justifyContent: isExpanded ? 'flex-start' : 'center',
                padding: '10px 12px',
                borderRadius: 'var(--radius-sm)',
                border: 'none',
                background: 'transparent',
                cursor: 'pointer',
                color: isActive ? 'var(--accent)' : 'var(--text-dim)',
                transition: 'all 0.15s ease',
                gap: 12,
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
                    background: 'var(--accent-muted)',
                    borderLeft: '3px solid var(--accent)',
                    boxShadow: '0 0 16px var(--accent-muted)',
                  }}
                />
              )}
              <Icon size={18} style={{ position: 'relative', zIndex: 1, flexShrink: 0 }} />
              {isExpanded && (
                <span style={{
                  position: 'relative',
                  zIndex: 1,
                  fontSize: 12,
                  fontWeight: 600,
                  whiteSpace: 'nowrap',
                  fontFamily: "var(--font-main, sans-serif)",
                  letterSpacing: '-0.01em',
                  color: isActive ? 'var(--accent)' : 'var(--text-main)'
                }}>
                  {label}
                </span>
              )}
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
              display: 'flex', alignItems: 'center', justifyContent: isExpanded ? 'flex-start' : 'center',
              padding: 8, borderRadius: 'var(--radius-sm)', border: 'none',
              background: 'transparent', cursor: 'pointer', gap: 10,
              color: 'var(--text-dim)', transition: 'color 0.15s ease',
            }}
            onMouseEnter={e => (e.currentTarget.style.color = danger ? 'var(--danger)' : 'var(--text-main)')}
            onMouseLeave={e => (e.currentTarget.style.color = 'var(--text-dim)')}
          >
            <Icon size={danger ? 14 : 16} style={{ flexShrink: 0 }} />
            {isExpanded && (
              <span style={{ fontSize: 10, fontFamily: "'JetBrains Mono', monospace", whiteSpace: 'nowrap' }}>
                {label}
              </span>
            )}
          </button>
        ))}
      </div>
    </motion.nav>
  );
}
