import React, { useState } from 'react';
import { useApp } from '../AppContext';
import NavRail from './NavRail';
import StatusBar from './StatusBar';
import RightDrawer from './RightDrawer';
import Timeline from '../views/Timeline';
import Jobs from '../views/Jobs';
import Clipboard from '../views/Clipboard';
import Productivity from '../views/Productivity';
import SwarmDebate from '../views/SwarmDebate';
import Settings from '../views/Settings';

export default function Shell() {
  const { activeTab } = useApp();
  // Lifted state so RightDrawer can receive live thoughts from Timeline
  const [thoughtsFeed, setThoughtsFeed] = useState<{ thoughts: string[]; streaming: boolean }>({ thoughts: [], streaming: false });
  const [recentRuns, setRecentRuns] = useState<{ id: string | number; status: string; goal: string }[]>([]);

  return (
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
              <Jobs onRunsUpdate={setRecentRuns} />
            </div>
            <div style={{ display: activeTab === 'clipboard' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
              <Clipboard />
            </div>
            <div style={{ display: activeTab === 'productivity' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
              <Productivity />
            </div>
            <div style={{ display: activeTab === 'lobby' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
              <SwarmDebate />
            </div>
            <div style={{ display: activeTab === 'settings' ? 'flex' : 'none', flex: 1, flexDirection: 'column', overflow: 'hidden' }}>
              <Settings />
            </div>
          </div>
        </main>

        {/* Right drawer */}
        <div style={{ position: 'relative', flexShrink: 0 }}>
          <RightDrawer thoughtsFeed={thoughtsFeed} recentRuns={recentRuns} />
        </div>
      </div>

      <StatusBar />
    </div>
  );
}
