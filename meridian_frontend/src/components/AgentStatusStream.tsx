import React, { useState, useEffect } from 'react';
import { Activity, Radio, Cpu, Terminal, CheckCircle2, AlertTriangle, ShieldAlert } from 'lucide-react';
import { API_BASE_URL } from '../config';

interface AgentEvent {
  event_id: string;
  timestamp: number;
  status: string;
  current_task?: string;
  active_tool?: string;
  subagent?: string;
  message: string;
}

export const AgentStatusStream: React.FC = () => {
  const [status, setStatus] = useState<string>('idle');
  const [currentTask, setCurrentTask] = useState<string | null>(null);
  const [events, setEvents] = useState<AgentEvent[]>([]);
  const [connected, setConnected] = useState<boolean>(false);

  useEffect(() => {
    fetchSnapshot();
    connectWebSocket();
  }, []);

  const fetchSnapshot = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/agent/status`);
      if (res.ok) {
        const data = await res.json();
        setStatus(data.status || 'idle');
        setCurrentTask(data.current_task || null);
        setEvents(data.recent_events || []);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const connectWebSocket = () => {
    const wsUrl = API_BASE_URL.replace(/^https/, 'wss').replace(/^http/, 'ws') + '/ws/agent-status';

    const ws = new WebSocket(wsUrl);

    ws.onopen = () => {
      setConnected(true);
    };

    ws.onmessage = (e) => {
      try {
        const event: AgentEvent = JSON.parse(e.data);
        if (event.status) setStatus(event.status);
        if (event.current_task !== undefined) setCurrentTask(event.current_task);

        setEvents((prev) => [event, ...prev].slice(0, 50));
      } catch (err) {}
    };

    ws.onclose = () => {
      setConnected(false);
      setTimeout(connectWebSocket, 3000);
    };
  };

  const getStatusBadge = () => {
    switch (status) {
      case 'thinking':
        return { color: 'bg-[var(--accent-muted)] text-[var(--accent-2)] border-[var(--border-active)]', label: 'Thinking...' };
      case 'executing_tool':
        return { color: 'bg-[var(--accent-muted)] text-[var(--accent)] border-[var(--border-active)]', label: 'Executing Tool' };
      case 'verifying':
        return { color: 'bg-[color-mix(in_srgb,var(--warning)_12%,transparent)] text-[var(--warning)] border-[var(--warning)]', label: 'Verifying Logic' };
      case 'completed':
        return { color: 'bg-[color-mix(in_srgb,var(--success)_12%,transparent)] text-[var(--success)] border-[var(--success)]', label: 'Task Completed' };
      case 'error':
        return { color: 'bg-[color-mix(in_srgb,var(--danger)_12%,transparent)] text-[var(--danger)] border-[var(--danger)]', label: 'Execution Error' };
      default:
        return { color: 'bg-[var(--bg-surface)] text-[var(--text-dim)] border-[var(--border-subtle)]', label: 'Idle' };
    }
  };

  const badge = getStatusBadge();

  return (
    <div className="space-y-6 text-[var(--text-bright)]">
      {/* Header Badge */}
      <div className="flex items-center justify-between p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-[var(--accent-muted)] border border-[var(--border-active)] rounded-lg">
            <Activity className="w-6 h-6 text-[var(--accent)]" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-[var(--text-bright)]">Real-Time Agent Status & Activity Stream</h2>
            <p className="text-xs text-[var(--text-dim)]">Live agent execution state telemetry, subagent events, and activity logs</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <span className={`inline-flex items-center gap-1.5 px-3 py-1 text-xs font-semibold rounded-full border ${badge.color}`}>
            <span className="w-2 h-2 rounded-full bg-current animate-ping" />
            {badge.label}
          </span>
          <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 text-[11px] font-mono rounded-full border ${
            connected ? 'bg-[color-mix(in_srgb,var(--success)_12%,transparent)] text-[var(--success)] border-[var(--success)]' : 'bg-[color-mix(in_srgb,var(--danger)_12%,transparent)] text-[var(--danger)] border-[var(--danger)]'
          }`}>
            <Radio className="w-3 h-3" />
            {connected ? 'WS Live' : 'WS Disconnected'}
          </span>
        </div>
      </div>

      {/* Task Snapshot */}
      {currentTask && (
        <div className="p-4 bg-[var(--bg-panel)] border border-[var(--border-active)] rounded-xl text-xs space-y-1">
          <span className="text-[var(--accent)] font-semibold">Active Agent Task:</span>
          <p className="text-[var(--text-main)] font-mono">{currentTask}</p>
        </div>
      )}

      {/* Activity Event Feed */}
      <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
        <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--text-main)]">
          <Terminal className="w-4 h-4 text-[var(--accent)]" /> Activity Stream Feed
        </h3>

        {events.length === 0 ? (
          <div className="p-6 text-center text-xs text-[var(--text-ghost)] border border-dashed border-[var(--border-subtle)] rounded-xl">
            No activity events recorded yet.
          </div>
        ) : (
          <div className="space-y-2 max-h-96 overflow-y-auto pr-1">
            {events.map((evt) => (
              <div key={evt.event_id} className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-1.5 text-xs">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-[10px] px-2 py-0.5 bg-[var(--bg-surface)] text-[var(--accent)] rounded">
                      {evt.status}
                    </span>
                    {evt.active_tool && (
                      <span className="font-mono text-[10px] px-2 py-0.5 bg-[var(--accent-muted)] text-[var(--accent-2)] border border-[var(--border-active)] rounded">
                        tool: {evt.active_tool}
                      </span>
                    )}
                  </div>
                  <span className="text-[10px] font-mono text-[var(--text-ghost)]">
                    {new Date(evt.timestamp * 1000).toLocaleTimeString()}
                  </span>
                </div>
                <p className="text-[var(--text-main)] font-sans">{evt.message}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
