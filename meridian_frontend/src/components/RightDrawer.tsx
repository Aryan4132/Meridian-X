import React from 'react';
import { ChevronRight } from 'lucide-react';
import { useApp, TabId } from '../AppContext';
import ProgressArc from './ui/ProgressArc';
import DataBadge from './ui/DataBadge';

interface DrawerContentProps {
  title: string;
  children: React.ReactNode;
}

// Exported so views can inject live thought content
export interface DrawerThoughtsFeed {
  thoughts: string[];
  streaming: boolean;
}

function DrawerSection({ title, children }: DrawerContentProps) {
  return (
    <div style={{ marginBottom: 20 }}>
      <div className="section-label">{title}</div>
      {children}
    </div>
  );
}

function HardwarePanel({ usage }: { usage: { cpu: number; ram: number } }) {
  return (
    <div style={{ display: 'flex', gap: 16, justifyContent: 'center', paddingTop: 8 }}>
      <div style={{ textAlign: 'center' }}>
        <ProgressArc value={usage.cpu} size={90} strokeWidth={6} label="CPU" color="var(--accent)" />
      </div>
      <div style={{ textAlign: 'center' }}>
        <ProgressArc
          value={usage.ram} size={90} strokeWidth={6} label="RAM"
          color={usage.ram > 85 ? 'var(--danger)' : 'var(--accent-2)'}
        />
      </div>
    </div>
  );
}

const DRAWER_TITLES: Record<TabId, string> = {
  timeline:     'ReAct Thoughts',
  jobs:         'Recent Runs',
  clipboard:    'Clipboard Stats',
  productivity: 'Hardware Vitals',
  lobby:        'Agent Legend',
  settings:     'Hardware Vitals',
};

export default function RightDrawer({
  thoughtsFeed,
  recentRuns,
}: {
  thoughtsFeed?: DrawerThoughtsFeed;
  recentRuns?: { id: string | number; status: string; goal: string }[];
}) {
  const { rightDrawerOpen, setRightDrawerOpen, activeTab, systemUsage } = useApp();
  const title = DRAWER_TITLES[activeTab];

  return (
    <>
      <div
        style={{
          width: rightDrawerOpen ? 'var(--drawer-width)' : 0,
          opacity: rightDrawerOpen ? 1 : 0,
          transition: 'width 0.22s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.22s cubic-bezier(0.16, 1, 0.3, 1)',
          background: 'var(--bg-void)',
          borderLeft: rightDrawerOpen ? '1px solid var(--border-subtle)' : 'none',
          overflow: 'hidden',
          flexShrink: 0,
          display: 'flex',
          flexDirection: 'column',
          height: '100%',
        }}
      >
        <div style={{ width: 'var(--drawer-width)', padding: '16px 16px 0', display: 'flex', flexDirection: 'column', height: '100%' }}>
          {/* Header */}
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 16 }}>
            <span style={{ fontSize: 11, fontWeight: 600, color: 'var(--text-dim)', textTransform: 'uppercase', letterSpacing: '0.08em', fontFamily: "'JetBrains Mono', monospace" }}>
              {title}
            </span>
            <button
              onClick={() => setRightDrawerOpen(false)}
              style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--text-dim)', padding: 4, borderRadius: 'var(--radius-sm)', display: 'flex' }}
              title="Collapse"
            >
              <ChevronRight size={14} />
            </button>
          </div>

          {/* Content */}
          <div style={{ flex: 1, overflowY: 'auto', paddingBottom: 16 }}>

            {/* TIMELINE: Live ReAct thoughts */}
            {activeTab === 'timeline' && (
              <div>
                {thoughtsFeed?.streaming && (
                  <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginBottom: 8 }}>
                    <span style={{ width: 6, height: 6, borderRadius: '50%', background: 'var(--accent)', display: 'inline-block', animation: 'pulse-glow-kf 1s ease-in-out infinite' }} />
                    <span style={{ fontSize: 10, color: 'var(--accent)', fontFamily: "'JetBrains Mono', monospace" }}>Streaming...</span>
                  </div>
                )}
                {(thoughtsFeed?.thoughts ?? []).length === 0 ? (
                  <p style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>
                    No thoughts yet. Send a message to start.
                  </p>
                ) : (
                  <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    {thoughtsFeed!.thoughts.map((t, i) => (
                      <div key={i} style={{
                        fontSize: 11,
                        color: 'var(--text-main)',
                        fontFamily: "'JetBrains Mono', monospace",
                        background: 'var(--bg-surface)',
                        padding: '6px 8px',
                        borderRadius: 'var(--radius-sm)',
                        borderLeft: '2px solid var(--accent-dim)',
                        lineHeight: 1.5,
                      }}>
                        <span style={{ color: 'var(--text-dim)', marginRight: 6 }}>{(i + 1).toString().padStart(2, '0')}.</span>
                        {t}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}

            {/* JOBS: Recent run previews */}
            {activeTab === 'jobs' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                {(recentRuns ?? []).slice(0, 5).map((r) => (
                  <div key={r.id} style={{
                    padding: '8px 10px',
                    background: 'var(--bg-surface)',
                    borderRadius: 'var(--radius-sm)',
                    borderLeft: `2px solid ${r.status === 'success' ? 'var(--success)' : 'var(--danger)'}`,
                  }}>
                    <div style={{ fontSize: 10, fontFamily: "'JetBrains Mono', monospace", color: r.status === 'success' ? 'var(--success)' : 'var(--danger)', marginBottom: 3 }}>
                      #{r.id} · {r.status}
                    </div>
                    <div style={{ fontSize: 11, color: 'var(--text-main)', lineHeight: 1.4, overflow: 'hidden', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical' }}>
                      {r.goal}
                    </div>
                  </div>
                ))}
                {(recentRuns ?? []).length === 0 && (
                  <p style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace" }}>No runs yet.</p>
                )}
              </div>
            )}

            {/* CLIPBOARD: Stats */}
            {activeTab === 'clipboard' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div className="glass" style={{ padding: '10px 12px' }}>
                  <div style={{ fontSize: 10, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", marginBottom: 4 }}>POLLING INTERVAL</div>
                  <div style={{ fontSize: 16, fontWeight: 700, color: 'var(--accent)' }}>1.5s</div>
                </div>
                <p style={{ fontSize: 11, color: 'var(--text-dim)', fontFamily: "'JetBrains Mono', monospace", lineHeight: 1.5 }}>
                  Clipboard is monitored continuously. Click "Analyze" on any item to route it through the ReAct agent.
                </p>
              </div>
            )}

            {/* PRODUCTIVITY / SETTINGS: Hardware arcs */}
            {(activeTab === 'productivity' || activeTab === 'settings') && (
              <HardwarePanel usage={systemUsage} />
            )}

            {/* LOBBY: Agent legend */}
            {activeTab === 'lobby' && (
              <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                {[
                  { role: 'CODER', color: 'var(--success)', desc: 'Proposes implementation' },
                  { role: 'AUDITOR', color: 'var(--warning)', desc: 'Validates security + safety' },
                  { role: 'QA', color: '#60A5FA', desc: 'Runs syntax + logic checks' },
                ].map(({ role, color, desc }) => (
                  <div key={role} style={{ display: 'flex', gap: 10, alignItems: 'flex-start' }}>
                    <span style={{ fontFamily: "'JetBrains Mono', monospace", fontSize: 10, fontWeight: 700, color, paddingTop: 2, minWidth: 54 }}>{role}</span>
                    <span style={{ fontSize: 11, color: 'var(--text-dim)', lineHeight: 1.4 }}>{desc}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Open toggle when drawer is closed */}
      {!rightDrawerOpen && (
        <button
          onClick={() => setRightDrawerOpen(true)}
          title={title}
          style={{
            position: 'absolute',
            right: 0,
            top: '50%',
            transform: 'translateY(-50%)',
            background: 'var(--bg-void)',
            border: '1px solid var(--border-subtle)',
            borderRight: 'none',
            borderRadius: '6px 0 0 6px',
            padding: '8px 4px',
            cursor: 'pointer',
            color: 'var(--text-dim)',
            display: 'flex',
            zIndex: 10,
            transition: 'opacity 0.15s ease',
          }}
        >
          <ChevronRight size={12} style={{ transform: 'rotate(180deg)' }} />
        </button>
      )}
    </>
  );
}
