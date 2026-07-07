// Global error reporting to backend daemon for WebView2 debugging
if (typeof window !== 'undefined') {
  // Disable right-click context menu for standard native desktop feel
  document.addEventListener('contextmenu', e => e.preventDefault());

  const sanitizeMessage = (msg: string): string => {
    return msg
      .replace(/(sk-[a-zA-Z0-9]{20,})/g, 'sk-***[REDACTED]***')
      .replace(/(AIzaSy[a-zA-Z0-9_-]{33})/g, 'AIzaSy***[REDACTED]***')
      .replace(/(xoxb-[a-zA-Z0-9-]{10,})/g, 'xoxb-***[REDACTED]***')
      .replace(/(ghp_[a-zA-Z0-9]{36,})/g, 'ghp_***[REDACTED]***')
      .replace(/(?:key|token|auth|pass|password|secret)(?:\s*[:=]\s*["']?)([a-zA-Z0-9_-]{12,})/gi, (match, p1) => {
        return match.replace(p1, '***[REDACTED]***');
      });
  };

  const sendDebugLog = (message: string, level = 'error') => {
    const cleanMessage = sanitizeMessage(message);
    fetch('http://localhost:4132/api/debug/log', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: cleanMessage, level }),
    }).catch(() => {});
  };

  const originalConsoleError = console.error;
  console.error = (...args: any[]) => {
    sendDebugLog(args.map(a => typeof a === 'object' ? JSON.stringify(a) : String(a)).join(' '), 'error');
    originalConsoleError.apply(console, args);
  };

  const originalConsoleWarn = console.warn;
  console.warn = (...args: any[]) => {
    sendDebugLog(args.map(a => typeof a === 'object' ? JSON.stringify(a) : String(a)).join(' '), 'warning');
    originalConsoleWarn.apply(console, args);
  };

  window.onerror = (message, source, lineno, colno, error) => {
    sendDebugLog(`Uncaught Exception: ${message} at ${source}:${lineno}:${colno} - Error: ${error?.stack || error}`, 'error');
    return false;
  };

  window.onunhandledrejection = (event) => {
    sendDebugLog(`Unhandled Promise Rejection: ${event.reason?.stack || event.reason}`, 'error');
  };
}

import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import Mascot from './Mascot';
import BootSequence from './startup/BootSequence';
import SetupWizard from './startup/SetupWizard';
import Shell from './components/Shell';
import { AppProvider } from './AppContext';
import './index.css';

type AppStage = 'boot' | 'setup' | 'shell';

function MainRouter() {
  const [windowType, setWindowType] = useState<'main' | 'mascot'>('main');
  const [stage, setStage] = useState<AppStage>('boot');

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (params.get('window') === 'mascot') {
      setWindowType('mascot');
      document.documentElement.classList.add('mascot-html');
      document.body.classList.add('mascot-body');
    } else {
      setWindowType('main');
      document.documentElement.classList.remove('mascot-html');
      document.body.classList.remove('mascot-body');
    }
  }, []);

  const onBootComplete = async () => {
    try {
      const res = await fetch('http://localhost:4132/api/profile/all');
      if (res.ok) {
        const profile = await res.json();
        if (profile && (profile.first_run_completed === true || profile.meridian_model)) {
          // Sync backend profile to localStorage
          localStorage.setItem('firstRunCompleted', 'true');
          const keyMap: Record<string, string> = {
            tavily_key: 'TAVILY_API_KEY',
            discord_token: 'DISCORD_BOT_TOKEN',
            telegram_token: 'TELEGRAM_BOT_TOKEN',
            telegram_chat_id: 'TELEGRAM_CHAT_ID',
            meridian_provider: 'MERIDIAN_PROVIDER',
            meridian_model: 'MERIDIAN_MODEL',
            meridian_vision_model: 'MERIDIAN_VISION_MODEL',
            ollama_host: 'OLLAMA_HOST',
            openai_key: 'OPENAI_API_KEY',
            anthropic_key: 'ANTHROPIC_API_KEY',
            gemini_key: 'GEMINI_API_KEY',
            deepseek_key: 'DEEPSEEK_API_KEY',
          };
          for (const [backendKey, localKey] of Object.entries(keyMap)) {
            if (profile[backendKey] !== undefined && profile[backendKey] !== null) {
              localStorage.setItem(localKey, String(profile[backendKey]));
            }
          }
          setStage('shell');
          return;
        }
      }
    } catch (e) {
      console.error('Failed to sync profile from backend:', e);
    }

    const firstRunDone = localStorage.getItem('firstRunCompleted') === 'true';
    setStage(firstRunDone ? 'shell' : 'setup');
  };

  const onSetupComplete = () => {
    setStage('shell');
  };

  if (windowType === 'mascot') return <Mascot />;

  return (
    <AppProvider>
      {stage === 'boot'  && <BootSequence onComplete={onBootComplete} />}
      {stage === 'setup' && <SetupWizard onComplete={onSetupComplete} />}
      {stage === 'shell' && <Shell />}
    </AppProvider>
  );
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MainRouter />
  </React.StrictMode>
);
