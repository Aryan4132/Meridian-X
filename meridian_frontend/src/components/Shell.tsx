import React, { useState, useEffect, Suspense, lazy } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { useApp } from '../AppContext';
import NavRail from './NavRail';
import StatusBar from './StatusBar';
import RightDrawer from './RightDrawer';
import { CommandPalette } from './CommandPalette';
import { ToastProvider } from './ui/ToastContext';
import Timeline from '../views/Timeline';
import Jobs from '../views/Jobs';
import Clipboard from '../views/Clipboard';
import Productivity from '../views/Productivity';
// Heavy views load on demand so the initial bundle stays lean.
const SwarmDebate = lazy(() => import('../views/SwarmDebate'));
const WorkflowBuilder = lazy(() => import('../views/WorkflowBuilder'));
const MemoryEditor = lazy(() => import('../views/MemoryEditor'));
const Settings = lazy(() => import('../views/Settings'));

function ViewLoadingFallback() {
  return (
    <div style={{ padding: 32, color: 'var(--text-secondary)', fontSize: 14 }}>
      Loading view…
    </div>
  );
}

import AmbientParticles from './ui/AmbientParticles';
import ProactiveGuardBanner from './ProactiveGuardBanner';

export default function Shell() {
  const { activeTab, setActiveTab } = useApp();
  const [isPaletteOpen, setIsPaletteOpen] = useState(false);
  // Lifted state so RightDrawer can receive live thoughts from Timeline
  const [thoughtsFeed, setThoughtsFeed] = useState<{ thoughts: string[]; streaming: boolean }>({ thoughts: [], streaming: false });
  const [recentRuns, setRecentRuns] = useState<{ id: string | number; status: string; goal: string }[]>([]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        setIsPaletteOpen(prev => !prev);
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, []);

  const handleSelectAction = (actionId: string) => {
    switch (actionId) {
      case 'local_model_mgr':
      case 'memory_consolidate':
      case 'dev_automation':
      case 'agent_stream':
        setActiveTab('productivity');
        break;
      case 'run_swarm':
        setActiveTab('lobby');
        break;
      case 'codegraph_search':
      case 'papercoder_gen':
        setActiveTab('workflows');
        break;
      case 'vault_keys':
        setActiveTab('settings');
        break;
      default:
        break;
    }
  };

  return (
    <ToastProvider>
      <ProactiveGuardBanner />
      <div style={{

        display: 'flex',
        height: '100vh',
        width: '100vw',
        flexDirection: 'column',
        background: 'var(--bg-base)',
        position: 'relative',
        overflow: 'hidden',
      }}>
        {/* Ambient background */}
        <div className="void-bg" />
        <AmbientParticles />

        {/* Main row */}
        <div style={{ display: 'flex', flex: 1, overflow: 'hidden', position: 'relative' }}>
          <NavRail />

          {/* Content area */}
          <main style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', position: 'relative' }}>
            <div style={{ flex: 1, position: 'relative', width: '100%', height: '100%', overflow: 'hidden' }}>
              {[
                { id: 'timeline', component: <Timeline onThoughtsUpdate={setThoughtsFeed} /> },
                { id: 'jobs', component: <Jobs onRunsUpdate={setRecentRuns} isActive={activeTab === 'jobs'} /> },
                { id: 'clipboard', component: <Clipboard isActive={activeTab === 'clipboard'} /> },
                { id: 'productivity', component: <Productivity isActive={activeTab === 'productivity'} /> },
                { id: 'lobby', component: (<Suspense fallback={<ViewLoadingFallback />}><SwarmDebate /></Suspense>) },
                { id: 'workflows', component: (<Suspense fallback={<ViewLoadingFallback />}><WorkflowBuilder /></Suspense>) },
                { id: 'memory', component: (<Suspense fallback={<ViewLoadingFallback />}><MemoryEditor /></Suspense>) },
                { id: 'settings', component: (<Suspense fallback={<ViewLoadingFallback />}><Settings /></Suspense>) },
              ].map(({ id, component }) => {
                const isCurrent = activeTab === id;
                return (
                  <motion.div
                    key={id}
                    initial={false}
                    animate={{
                      opacity: isCurrent ? 1 : 0,
                      scale: isCurrent ? 1 : 0.99,
                      y: isCurrent ? 0 : 4,
                    }}
                    transition={{ duration: 0.22, ease: [0.16, 1, 0.3, 1] }}
                    style={{
                      position: 'absolute',
                      inset: 0,
                      display: 'flex',
                      flexDirection: 'column',
                      overflow: 'hidden',
                      pointerEvents: isCurrent ? 'auto' : 'none',
                      visibility: isCurrent ? 'visible' : 'hidden',
                      zIndex: isCurrent ? 1 : 0,
                    }}
                  >
                    {component}
                  </motion.div>
                );
              })}
            </div>

          </main>

          {/* Right drawer — Timeline & Jobs tabs only */}
          {(activeTab === 'timeline' || activeTab === 'jobs') && (
            <div style={{ position: 'relative', flexShrink: 0 }}>
              <RightDrawer thoughtsFeed={thoughtsFeed} recentRuns={recentRuns} />
            </div>
          )}
        </div>

        <StatusBar />
        <CommandPalette
          isOpen={isPaletteOpen}
          onClose={() => setIsPaletteOpen(false)}
          onSelectAction={handleSelectAction}
        />
      </div>
    </ToastProvider>
  );
}
