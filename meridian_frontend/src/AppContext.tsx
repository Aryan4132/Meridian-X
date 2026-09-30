import React, { createContext, useContext, useState, useEffect } from 'react';
import { SystemUsage } from './types';
import { API_BASE_URL } from './config';
import { invoke } from '@tauri-apps/api/core';
import { listen, emit } from '@tauri-apps/api/event';

export type TabId = 'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'lobby' | 'workflows' | 'memory' | 'settings';

export type IslandPosition = 'top-center' | 'top-right' | 'bottom-right' | 'top-left' | 'bottom-left' | 'bottom-center';

interface AppContextValue {
  activeTab: TabId;
  setActiveTab: (tab: TabId) => void;
  theme: string;
  setTheme: (theme: string) => void;
  accentColor: string;
  setAccentColor: (color: string) => void;
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

// Single source of truth for themes. IDs must match the canonical
// [data-theme="x"] / .theme-x blocks in index.css and the Settings picker.
export const THEME_IDS = [
  'cyberslate', 'artdeco', 'neobrutalism', 'cyberpunk', 'retro', 'ink',
  'nordic', 'maximalism', 'paper', 'sakura', 'solaris', 'tokyonight',
  'oled', 'vscode-dark', 'chronos',
] as const;

export type ThemeId = (typeof THEME_IDS)[number];

export const DEFAULT_THEME: ThemeId = 'cyberslate';

export function resolveTheme(t: string | null | undefined): ThemeId {
  return (THEME_IDS as readonly string[]).includes(t || '') ? (t as ThemeId) : DEFAULT_THEME;
}

/** Applies theme without clobbering unrelated <html> classes (e.g. mascot-html). */
export function applyThemeToDocument(t: string): void {
  const theme = resolveTheme(t);
  document.documentElement.setAttribute('data-theme', theme);
  const cls = document.documentElement.classList;
  // Drop any previous theme-* class, preserve everything else.
  Array.from(cls).forEach(c => {
    if (c.startsWith('theme-')) cls.remove(c);
  });
  cls.add(`theme-${theme}`);
}

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [activeTab, setActiveTab] = useState<TabId>('timeline');
  const [theme, _setTheme] = useState(() => resolveTheme(localStorage.getItem('theme')));
  const [accentColor, _setAccentColor] = useState(() => localStorage.getItem('MERIDIAN_ACCENT_COLOR') || '#E8A020');
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

  const setAccentColor = (color: string) => {
    _setAccentColor(color);
    localStorage.setItem('MERIDIAN_ACCENT_COLOR', color);
    document.documentElement.style.setProperty('--accent', color);
  };

  const setGameMode = async (enabled: boolean) => {
    _setGameMode(enabled);
    localStorage.setItem('GAME_MODE', enabled ? 'true' : 'false');
    
    if ((window as any).__TAURI_INTERNALS__) {
      try {
        await invoke('toggle_game_mode', { enabled });
      } catch (e) {
        console.error("Failed to toggle game mode in Tauri:", e);
      }
    }

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
    const theme = resolveTheme(t);
    _setTheme(theme);
    localStorage.setItem('theme', theme);
    applyThemeToDocument(theme);
    window.dispatchEvent(new Event('meridian-theme-changed'));
    if ((window as any).__TAURI_INTERNALS__) {
      emit('meridian-theme-changed', { theme }).catch(() => {});
    }
  };

  const setIslandPosition = (pos: IslandPosition) => {
    _setIslandPosition(pos);
    localStorage.setItem('ISLAND_POSITION', pos);
  };

  useEffect(() => {
    applyThemeToDocument(localStorage.getItem('theme'));

    const color = localStorage.getItem('MERIDIAN_ACCENT_COLOR');
    if (color) {
      document.documentElement.style.setProperty('--accent', color);
    }
  }, []);

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

  useEffect(() => {
    let unlisten: (() => void) | undefined;
    if ((window as any).__TAURI_INTERNALS__) {
      listen<any>('meridian-model-changed', (event) => {
        if (event.payload?.model) {
          setModelName(event.payload.model);
        }
      }).then(un => { unlisten = un; }).catch(() => {});
    }
    return () => {
      if (unlisten) unlisten();
    };
  }, []);

  useEffect(() => {
    const checkBackend = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/health`);
        setBackendAlive(res.ok);
      } catch {
        setBackendAlive(false);
      }
    };
    checkBackend();
    const interval = setInterval(checkBackend, 4000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (!backendAlive) return;
    const fetchUsage = async () => {
      try {
        const res = await fetch(`${API_BASE_URL}/api/system-usage`);
        if (res.ok) {
          const data = await res.json();
          setSystemUsage({ cpu: data.cpu ?? 0, ram: data.ram ?? 0 });
        }
      } catch { /* noop */ }
    };
    fetchUsage();
    const interval = setInterval(fetchUsage, 3000);
    return () => clearInterval(interval);
  }, [backendAlive]);

  return (
    <AppCtx.Provider
      value={{
        activeTab,
        setActiveTab,
        theme,
        setTheme,
        accentColor,
        setAccentColor,
        islandPosition,
        setIslandPosition,
        backendAlive,
        modelName,
        setModelName,
        rightDrawerOpen,
        setRightDrawerOpen,
        systemUsage,
        gameMode,
        setGameMode,
      }}
    >
      {children}
    </AppCtx.Provider>
  );
}

export function useApp() {
  const ctx = useContext(AppCtx);
  if (!ctx) throw new Error('useApp must be used within AppProvider');
  return ctx;
}
