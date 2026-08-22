import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import Mascot from './Mascot';
import BootSequence from './startup/BootSequence';
import SetupWizard from './startup/SetupWizard';
import Shell from './components/Shell';
import { AppProvider } from './AppContext';
import './index.css';
import { API_BASE_URL } from './config';

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
    fetch(`${API_BASE_URL}/api/debug/log`, {
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

import { OnboardingWizard } from './startup/OnboardingWizard';
import { BackendSetup } from './startup/BackendSetup';
import { invoke } from '@tauri-apps/api/core';

type AppStage = 'download' | 'boot' | 'onboarding' | 'setup' | 'shell';

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

      // Check if backend binary exists in production Tauri environment
      if (typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ && !(import.meta as any).env?.DEV) {
        invoke<boolean>('check_backend_installed')
          .then((installed) => {
            if (!installed) {
              setStage('download');
            }
          })
          .catch((e) => console.warn('Could not check backend status:', e));
      }
    }
  }, []);

  const onDownloadComplete = () => {
    setStage('boot');
  };

  const onBootComplete = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/profile/all`);
      if (res.ok) {
        const profile = await res.json();
        if (profile && (profile.first_run_completed === true || profile.meridian_model)) {
          localStorage.setItem('firstRunCompleted', 'true');
          setStage('shell');
          return;
        }
      }
    } catch (e) {
      console.error('Failed to sync profile from backend:', e);
    }

    const onboarded = localStorage.getItem('MERIDIAN_ONBOARDED') === 'true';
    if (!onboarded) {
      setStage('onboarding');
    } else {
      const firstRunDone = localStorage.getItem('firstRunCompleted') === 'true';
      setStage(firstRunDone ? 'shell' : 'setup');
    }
  };

  const onOnboardingComplete = () => {
    const firstRunDone = localStorage.getItem('firstRunCompleted') === 'true';
    setStage(firstRunDone ? 'shell' : 'setup');
  };

  const onSetupComplete = () => {
    setStage('shell');
  };

  if (windowType === 'mascot') return <Mascot />;

  return (
    <AppProvider>
      {stage === 'download'   && <BackendSetup onComplete={onDownloadComplete} />}
      {stage === 'boot'       && <BootSequence onComplete={onBootComplete} />}
      {stage === 'onboarding' && <OnboardingWizard onComplete={onOnboardingComplete} />}
      {stage === 'setup'      && <SetupWizard onComplete={onSetupComplete} />}
      {stage === 'shell'      && <Shell />}
    </AppProvider>
  );
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <MainRouter />
  </React.StrictMode>
);
