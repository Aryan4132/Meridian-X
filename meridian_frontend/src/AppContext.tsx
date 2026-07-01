import React, { createContext, useContext, useState, useEffect } from 'react';
import { SystemUsage } from './types';

export type TabId = 'timeline' | 'jobs' | 'clipboard' | 'productivity' | 'lobby' | 'settings';

interface AppContextValue {
  activeTab: TabId;
  setActiveTab: (tab: TabId) => void;
  theme: string;
  setTheme: (theme: string) => void;
  backendAlive: boolean;
  modelName: string;
  rightDrawerOpen: boolean;
  setRightDrawerOpen: (v: boolean) => void;
  systemUsage: SystemUsage;
}

const AppCtx = createContext<AppContextValue | null>(null);

export function AppProvider({ children }: { children: React.ReactNode }) {
  const [activeTab, setActiveTab] = useState<TabId>('timeline');
  const [theme, _setTheme] = useState(() => localStorage.getItem('theme') || 'frost');
  const [backendAlive, setBackendAlive] = useState(false);
  const [modelName, setModelName] = useState(() => {
    const m = localStorage.getItem('MERIDIAN_MODEL') || '';
    return m || 'qwen2.5-coder:7b';
  });
  const [rightDrawerOpen, setRightDrawerOpen] = useState(true);
  const [systemUsage, setSystemUsage] = useState<SystemUsage>({ cpu: 0, ram: 0 });

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

  return (
    <AppCtx.Provider value={{
      activeTab, setActiveTab,
      theme, setTheme,
      backendAlive,
      modelName,
      rightDrawerOpen, setRightDrawerOpen,
      systemUsage,
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
