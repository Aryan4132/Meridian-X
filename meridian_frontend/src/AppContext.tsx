import React, { createContext, useContext, useState, useEffect } from 'react';
import { SystemUsage } from './types';
import { invoke } from '@tauri-apps/api/core';
import { listen } from '@tauri-apps/api/event';

export type TabId = 'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'lobby' | 'settings';
export type IslandPosition = 'top-center' | 'top-right' | 'bottom-right' | 'top-left' | 'bottom-left' | 'bottom-center';

interface AppContextValue {
  activeTab: TabId;
  setActiveTab: (tab: TabId) => void;
  theme: string;
  setTheme: (theme: string) => void;
  islandPosition: IslandPosition;
  setIslandPosition: (pos: IslandPosition) => void;
  backendAlive: boolean;
  modelName: string;
  setModelName: (model: string) => void;
  rightDrawerOpen: boolean;
  setRightDrawerOpen: (v: boolean) => void;
  systemUsage: SystemUsage;
  gameMode: boolean;
  setGameMode: (enabled: boolean) => void;
}

const AppCtx = createContext<AppContextValue | null>(null);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [activeTab, setActiveTab] = useState<TabId>('timeline');
  const [theme, _setTheme] = useState(() => localStorage.getItem('theme') || 'frost');
  const [islandPosition, _setIslandPosition] = useState<IslandPosition>(
    () => (localStorage.getItem('ISLAND_POSITION') as IslandPosition) || 'bottom-right'
  );
  const [backendAlive, setBackendAlive] = useState(false);
  const [modelName, setModelName] = useState(() => {
    const m = localStorage.getItem('MERIDIAN_MODEL') || '';
    return m || 'qwen2.5-coder:7b';
  });
  const [rightDrawerOpen, setRightDrawerOpen] = useState(true);
  const [systemUsage, setSystemUsage] = useState<SystemUsage>({ cpu: 0, ram: 0 });
  const [gameMode, _setGameMode] = useState(() => localStorage.getItem('GAME_MODE') === 'true');

  const setGameMode = async (enabled: boolean) => {
    _setGameMode(enabled);
    localStorage.setItem('GAME_MODE', enabled ? 'true' : 'false');
    
    // Sync to Tauri (Rust)
    if ((window as any).__TAURI_INTERNALS__) {
      try {
        await invoke('toggle_game_mode', { enabled });
      } catch (e) {
        console.error("Failed to toggle game mode in Tauri:", e);
      }
    }

    // Sync to Python Backend
    try {
      await fetch('http://localhost:4132/api/game-mode', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ enabled }),
      });
    } catch (e) {
      console.error("Failed to toggle game mode on backend:", e);
    }
  };

  const setTheme = (t: string) => {
    _setTheme(t);
    localStorage.setItem('theme', t);
    document.documentElement.className = t === 'void' ? '' : `theme-${t}`;
  };

  // Apply theme on mount
  useEffect(() => {
    const t = localStorage.getItem('theme') || 'void';
    document.documentElement.className = t === 'void' ? '' : `theme-${t}`;
  }, []);

  // Update model name when localStorage changes
  useEffect(() => {
    const update = () => {
      const m = localStorage.getItem('MERIDIAN_MODEL');
      if (m) setModelName(m);
    };
    window.addEventListener('storage', update);
    return () => window.removeEventListener('storage', update);
  }, []);

  // Poll backend health + usage
  useEffect(() => {
    const poll = async () => {
      try {
        const res = await fetch('http://localhost:4132/api/system-usage').catch(() => null);
        if (res?.ok) {
          const data = await res.json();
          setBackendAlive(true);
          setSystemUsage({ cpu: data.cpu || 0, ram: data.ram || 0 });
        } else {
          setBackendAlive(false);
        }
      } catch {
        setBackendAlive(false);
      }
    };
    poll();
    const t = setInterval(poll, 5000);
    return () => clearInterval(t);
  }, []);

  // Sync initial game mode to Tauri and Python Backend on mount
  useEffect(() => {
    const initialMode = localStorage.getItem('GAME_MODE') === 'true';
    if ((window as any).__TAURI_INTERNALS__) {
      invoke('toggle_game_mode', { enabled: initialMode }).catch(err =>
        console.error("Failed to sync initial game mode in Tauri:", err)
      );
    }

    // Sync to Python Backend
    fetch('http://localhost:4132/api/game-mode', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ enabled: initialMode }),
    }).catch(err =>
      console.error("Failed to sync initial game mode on backend:", err)
    );
  }, []);

  // Listen to system tray menu events
  useEffect(() => {
    let unlisten: any;
    if ((window as any).__TAURI_INTERNALS__) {
      listen('tray-toggle-game-mode', () => {
        const current = localStorage.getItem('GAME_MODE') === 'true';
        setGameMode(!current);
      }).then(u => {
        unlisten = u;
      }).catch(err => console.error("Failed to setup tray listener:", err));
    }
    return () => {
      if (unlisten) unlisten();
    };
  }, []);

  // Listen to proactive nudge stream for game mode auto-detection
  const [reconnectKey, setReconnectKey] = useState(0);
  useEffect(() => {
    if (!backendAlive) return;

    const eventSource = new EventSource('http://localhost:4132/api/proactive/stream');

    eventSource.addEventListener('nudge', (e) => {
      try {
        const nudge = JSON.parse(e.data);
        if (nudge.type === 'game_mode_changed') {
          const enabled = nudge.message === 'enabled';
          _setGameMode(enabled);
          localStorage.setItem('GAME_MODE', enabled ? 'true' : 'false');
          // Sync to Tauri (Rust)
          if ((window as any).__TAURI_INTERNALS__) {
            invoke('toggle_game_mode', { enabled }).catch(err =>
              console.error("Failed to toggle game mode in Tauri from auto-nudge:", err)
            );
          }
        }
      } catch (err) {
        console.error("Failed to parse proactive nudge:", err);
      }
    });

    eventSource.onerror = () => {
      console.warn("EventSource disconnected, scheduling reconnect...");
      eventSource.close();
      setTimeout(() => {
        setReconnectKey(prev => prev + 1);
      }, 3000);
    };

    return () => {
      eventSource.close();
    };
  }, [backendAlive, reconnectKey]);

  const setIslandPosition = (pos: IslandPosition) => {
    _setIslandPosition(pos);
    localStorage.setItem('ISLAND_POSITION', pos);
    window.dispatchEvent(new Event('meridian-island-position-changed'));
  };

  return (
    <AppCtx.Provider value={{
      activeTab, setActiveTab,
      theme, setTheme,
      islandPosition, setIslandPosition,
      backendAlive,
      modelName,
      setModelName,
      rightDrawerOpen, setRightDrawerOpen,
      systemUsage,
      gameMode, setGameMode,
    }}>
      {children}
    </AppCtx.Provider>
  );
}

export function useApp() {
  const ctx = useContext(AppCtx);
  if (!ctx) throw new Error('useApp must be used inside AppProvider');
  return ctx;
}
