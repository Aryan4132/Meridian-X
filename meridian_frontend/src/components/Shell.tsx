import React, { useState, useEffect } from 'react';
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
import SwarmDebate from '../views/SwarmDebate';
import WorkflowBuilder from '../views/WorkflowBuilder';
import MemoryEditor from '../views/MemoryEditor';
import Settings from '../views/Settings';

import AmbientParticles from './ui/AmbientParticles';

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
            <div style={{ flex: 1, display: 'flex', flexDirection: 'column', overflow: 'hidden', position: 'relative' }}>
              <div style={{ display: activeTab === 'timeline' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <Timeline onThoughtsUpdate={setThoughtsFeed} />
              </div>
              <div style={{ display: activeTab === 'jobs' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <Jobs onRunsUpdate={setRecentRuns} isActive={activeTab === 'jobs'} />
              </div>
              <div style={{ display: activeTab === 'clipboard' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <Clipboard isActive={activeTab === 'clipboard'} />
              </div>
              <div style={{ display: activeTab === 'productivity' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <Productivity isActive={activeTab === 'productivity'} />
              </div>
              <div style={{ display: activeTab === 'lobby' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <SwarmDebate />
              </div>
              <div style={{ display: activeTab === 'workflows' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <WorkflowBuilder />
              </div>
              <div style={{ display: activeTab === 'memory' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <MemoryEditor />
              </div>
              <div style={{ display: activeTab === 'settings' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
                <Settings />
              </div>
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
