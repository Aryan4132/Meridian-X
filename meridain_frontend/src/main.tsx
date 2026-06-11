import {StrictMode, useEffect, useState} from 'react';
import {createRoot} from 'react-dom/client';
import { getCurrentWindow } from '@tauri-apps/api/window';
import App from './App.tsx';
import Mascot from './Mascot.tsx';
import './index.css';

function Root() {
  const [windowLabel, setWindowLabel] = useState<string | null>(null);

  useEffect(() => {
    try {
      const isTauri = typeof window !== 'undefined' && (window as any).__TAURI_INTERNALS__ !== undefined;
      if (isTauri) {
        setWindowLabel(getCurrentWindow().label);
      } else {
        const params = new URLSearchParams(window.location.search);
        setWindowLabel(params.get('window') || 'main');
      }
    } catch (e) {
      console.error("Failed to detect Tauri window label:", e);
      setWindowLabel('main');
    }
  }, []);

  if (windowLabel === null) {
    return <div className="bg-transparent h-screen w-screen" />;
  }

  if (windowLabel === 'mascot') {
    return <Mascot />;
  }

  return <App />;
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Root />
  </StrictMode>,
);
