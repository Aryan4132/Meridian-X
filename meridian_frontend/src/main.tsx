// Global error reporting to backend daemon for WebView2 debugging
if (typeof window !== 'undefined') {
  // Disable right-click context menu for standard native desktop feel
  document.addEventListener('contextmenu', e => e.preventDefault());

  const sendDebugLog = (message: string, level = 'error') => {
    fetch('http://localhost:4132/api/debug/log', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message, level }),
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
      document.body.classList.add('mascot-body');
    } else {
      setWindowType('main');
      document.body.classList.remove('mascot-body');
    }
  }, []);

  const onBootComplete = () => {
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
