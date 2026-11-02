import React, { useState } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import {
  MessageSquare, Zap, Clipboard, Timer, Bot, Settings2, Network, Brain,
  Eye, Minus, Square, X, Sparkles, Terminal
} from 'lucide-react';
import { useApp, TabId } from '../AppContext';
import { MascotCharacter } from '../Mascot';

import { getCurrentWindow } from '@tauri-apps/api/window';
import { invoke } from '@tauri-apps/api/core';

const NAV_ITEMS: { id: TabId; icon: React.ElementType; label: string; shortcut: string }[] = [
  { id: 'timeline',    icon: MessageSquare, label: 'Timeline Chat',       shortcut: '1' },
  { id: 'jobs',        icon: Zap,           label: 'Background Jobs',     shortcut: '2' },
  { id: 'clipboard',   icon: Clipboard,     label: 'Clipboard Hub',       shortcut: '3' },
  { id: 'productivity',icon: Timer,         label: 'Productivity HUD',    shortcut: '4' },
  { id: 'lobby',       icon: Bot,           label: 'Swarm Debate',        shortcut: '5' },
  { id: 'workflows',   icon: Network,       label: 'Workflow Canvas',     shortcut: '6' },
  { id: 'memory',      icon: Brain,         label: 'Memory Graph',        shortcut: '7' },
  { id: 'settings',    icon: Settings2,     label: 'Settings & Vitals',   shortcut: '8' },
];

export default function NavRail() {
  const { activeTab, setActiveTab, backendAlive } = useApp();
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
      if (window.confirm('Are you sure you want to close Meridian-X? This will stop all background processes.')) {
        try { invoke('close_application'); } catch { /* noop */ }
      }
    }
  };

  return (
    <motion.nav
      data-tauri-drag-region
      initial={false}
      animate={{ width: isExpanded ? 210 : 66 }}
      transition={{ duration: 0.22, ease: [0.16, 1, 0.3, 1] }}
      onMouseEnter={() => setIsExpanded(true)}
      onMouseLeave={() => setIsExpanded(false)}
      style={{
        background: 'color-mix(in srgb, var(--bg-void) 92%, transparent)',
        backdropFilter: 'blur(20px)',
        WebkitBackdropFilter: 'blur(20px)',
        borderRight: '1px solid var(--border-subtle)',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        padding: '14px 0 10px',
        flexShrink: 0,
        zIndex: 20,
        position: 'relative',
        boxShadow: '4px 0 24px rgba(0, 0, 0, 0.25)',
      }}
    >
      {/* Brand Mascot Logo */}
      <div 
        onClick={handleMascot}
        style={{
          marginBottom: 16,
          padding: '6px 8px',
          cursor: 'pointer',
          display: 'flex',
          alignItems: 'center',
          gap: 10,
          width: '100%',
          justifyContent: isExpanded ? 'flex-start' : 'center',
          paddingLeft: isExpanded ? 16 : 8,
          transition: 'all 0.2s ease',
        }} 
        title="Meridian-X Core Agent (Click to summon companion)"
      >
        <div style={{ position: 'relative' }}>
          <MascotCharacter state="default" accentColor="var(--accent)" />
          <span style={{
            position: 'absolute',
            bottom: -2,
            right: -2,
            width: 7,
            height: 7,
            borderRadius: '50%',
            background: backendAlive ? 'var(--success, #00ff88)' : 'var(--danger, #ff4b4b)',
            boxShadow: backendAlive ? '0 0 8px var(--success, #00ff88)' : 'none',
          }} />
        </div>
        {isExpanded && (
          <div style={{ display: 'flex', flexDirection: 'column' }}>
            <span style={{
              fontSize: 13,
              fontWeight: 800,
              fontFamily: "var(--font-heading, 'Outfit', sans-serif)",
              letterSpacing: '0.04em',
              color: 'var(--text-bright)',
            }}>
              MERIDIAN-X
            </span>
            <span style={{
              fontSize: 9,
              color: 'var(--accent)',
              fontFamily: "var(--font-mono, monospace)",
              letterSpacing: '0.06em',
            }}>
              AUTONOMOUS v0.1.7
            </span>
          </div>
        )}
      </div>

      {/* Navigation Items */}
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 4, width: '100%', padding: '0 8px' }}>
        {NAV_ITEMS.map(({ id, icon: Icon, label, shortcut }) => {
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
                padding: '9px 12px',
                borderRadius: 'var(--radius-md, 10px)',
                border: 'none',
                background: isActive 
                  ? 'color-mix(in srgb, var(--accent) 14%, rgba(255, 255, 255, 0.02))' 
                  : 'transparent',
                cursor: 'pointer',
                color: isActive ? 'var(--accent)' : 'var(--text-dim)',
                transition: 'all 0.18s cubic-bezier(0.16, 1, 0.3, 1)',
                gap: 12,
              }}
              onMouseEnter={e => {
                if (!isActive) {
                  (e.currentTarget as HTMLElement).style.color = 'var(--text-bright)';
                  (e.currentTarget as HTMLElement).style.background = 'rgba(255, 255, 255, 0.04)';
                }
              }}
              onMouseLeave={e => {
                if (!isActive) {
                  (e.currentTarget as HTMLElement).style.color = 'var(--text-dim)';
                  (e.currentTarget as HTMLElement).style.background = 'transparent';
                }
              }}
            >
              {isActive && (
                <div
                  style={{
                    position: 'absolute',
                    left: 0,
                    top: '18%',
                    bottom: '18%',
                    width: 3,
                    borderRadius: '0 4px 4px 0',
                    background: 'var(--accent)',
                    boxShadow: '0 0 12px var(--accent)',
                  }}
                />
              )}
              <Icon 
                size={18} 
                style={{ 
                  position: 'relative', 
                  zIndex: 1, 
                  flexShrink: 0,
                  filter: isActive ? 'drop-shadow(0 0 6px var(--accent-muted))' : 'none',
                }} 
              />
              {isExpanded && (
                <div style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  width: '100%',
                  position: 'relative',
                  zIndex: 1,
                  overflow: 'hidden',
                }}>
                  <span style={{
                    fontSize: 12,
                    fontWeight: isActive ? 600 : 500,
                    whiteSpace: 'nowrap',
                    fontFamily: "var(--font-main, sans-serif)",
                    letterSpacing: '-0.01em',
                    color: isActive ? 'var(--text-bright)' : 'var(--text-main)'
                  }}>
                    {label}
                  </span>
                  <span style={{
                    fontSize: 9,
                    fontFamily: "var(--font-mono, monospace)",
                    color: 'var(--text-dim)',
                    background: 'rgba(255, 255, 255, 0.06)',
                    padding: '1px 5px',
                    borderRadius: 4,
                  }}>
                    {shortcut}
                  </span>
                </div>
              )}
            </button>
          );
        })}
      </div>

      {/* Window Controls / Footer */}
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: 3,
        width: '100%',
        padding: '10px 8px 0',
        borderTop: '1px solid var(--border-subtle)',
      }}>
        {[
          { action: handleMascot, icon: Eye, label: 'Mascot Companion', danger: false },
          { action: handleMinimize, icon: Minus, label: 'Minimize Window', danger: false },
          { action: handleToggleMaximize, icon: Square, label: 'Toggle Maximize', danger: false },
          { action: handleClose, icon: X, label: 'Close to Tray', danger: true },
        ].map(({ action, icon: Icon, label, danger }) => (
          <button
            key={label}
            onClick={action}
            title={label}
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: isExpanded ? 'flex-start' : 'center',
              padding: '7px 10px',
              borderRadius: 'var(--radius-sm, 6px)',
              border: 'none',
              background: 'transparent',
              cursor: 'pointer',
              gap: 10,
              color: 'var(--text-dim)',
              transition: 'all 0.15s ease',
            }}
            onMouseEnter={e => {
              e.currentTarget.style.color = danger ? 'var(--danger)' : 'var(--text-bright)';
              e.currentTarget.style.background = danger ? 'rgba(248, 113, 113, 0.1)' : 'rgba(255, 255, 255, 0.04)';
            }}
            onMouseLeave={e => {
              e.currentTarget.style.color = 'var(--text-dim)';
              e.currentTarget.style.background = 'transparent';
            }}
          >
            <Icon size={danger ? 14 : 15} style={{ flexShrink: 0 }} />
            {isExpanded && (
              <span style={{ fontSize: 11, fontFamily: "var(--font-main, sans-serif)", whiteSpace: 'nowrap' }}>
                {label}
              </span>
            )}
          </button>
        ))}
      </div>
    </motion.nav>
  );
}
