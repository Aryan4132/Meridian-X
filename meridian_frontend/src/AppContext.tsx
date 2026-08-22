import React, { createContext, useContext, useState, useEffect } from 'react';
import { SystemUsage } from './types';
import { API_BASE_URL } from './config';
import { invoke } from '@tauri-apps/api/core';
import { listen, emit } from '@tauri-apps/api/event';


export type TabId = 'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'lobby' | 'workflows' | 'settings';

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
  const [gameMode, _setGameMode] = useState(false);

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
      await fetch(`${API_BASE_URL}/api/game-mode`, {
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
    document.documentElement.setAttribute('data-theme', t);
    document.documentElement.className = `theme-${t}`;
    window.dispatchEvent(new Event('meridian-theme-changed'));
    if ((window as any).__TAURI_INTERNALS__) {
      emit('meridian-theme-changed', { theme: t }).catch(() => {});
    }
  };

  // Apply theme on mount
  useEffect(() => {
    const t = localStorage.getItem('theme') || 'cyberslate';
    document.documentElement.setAttribute('data-theme', t);
    document.documentElement.className = `theme-${t}`;
  }, []);

  // Update model name when localStorage or model changes
  useEffect(() => {
    const update = () => {
      const m = localStorage.getItem('MERIDIAN_MODEL');
      if (m) setModelName(m);
    };
    window.addEventListener('storage', update);
    window.addEventListener('meridian-model-changed', update);
    return () => {
      window.removeEventListener('storage', update);
      window.removeEventListener('meridian-model-changed', update);
    };
  }, []);

  // Poll backend health + usage
  useEffect(() => {
    const poll = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/system-usage`).catch(() => null);
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

  // Sync initial game mode (off by default) to Tauri and Python Backend on mount
  useEffect(() => {
    const initialMode = false;
    localStorage.setItem('GAME_MODE', 'false');
    if ((window as any).__TAURI_INTERNALS__) {
      invoke('toggle_game_mode', { enabled: initialMode }).catch(err =>
        console.error("Failed to sync initial game mode in Tauri:", err)
      );
    }

    // Sync to Python Backend
    fetch(`${API_BASE_URL}/api/game-mode`, {
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

    const eventSource = new EventSource(`${API_BASE_URL}/api/proactive/stream`);

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

    // FIX: track the reconnect timer so it is cancelled on unmount (no ghost
    // reconnect after teardown) and use exponential backoff instead of a
    // fixed 3s hammer while the backend is down.
    let reconnectTimer: ReturnType<typeof setTimeout> | null = null;
    let backoffMs = 3000;
    eventSource.onerror = () => {
      console.warn("EventSource disconnected, scheduling reconnect...");
      eventSource.close();
      if (reconnectTimer) clearTimeout(reconnectTimer);
      reconnectTimer = setTimeout(() => {
        setReconnectKey(prev => prev + 1);
      }, backoffMs);
      backoffMs = Math.min(backoffMs * 2, 30000);
    };

    return () => {
      if (reconnectTimer) clearTimeout(reconnectTimer);
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
