import React, { useState, useEffect } from 'react';
import { Activity, Radio, Cpu, Terminal, CheckCircle2, AlertTriangle, ShieldAlert } from 'lucide-react';

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
      const res = await fetch('/api/agent/status');
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
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    const wsUrl = `${protocol}//${window.location.host}/ws/agent-status`;

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
        return { color: 'bg-purple-500/10 text-purple-400 border-purple-500/30', label: 'Thinking...' };
      case 'executing_tool':
        return { color: 'bg-cyan-500/10 text-cyan-400 border-cyan-500/30', label: 'Executing Tool' };
      case 'verifying':
        return { color: 'bg-amber-500/10 text-amber-400 border-amber-500/30', label: 'Verifying Logic' };
      case 'completed':
        return { color: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30', label: 'Task Completed' };
      case 'error':
        return { color: 'bg-rose-500/10 text-rose-400 border-rose-500/30', label: 'Execution Error' };
      default:
        return { color: 'bg-slate-800 text-slate-400 border-slate-700', label: 'Idle' };
    }
  };

  const badge = getStatusBadge();

  return (
    <div className="space-y-6 text-slate-100">
      {/* Header Badge */}
      <div className="flex items-center justify-between p-4 bg-slate-900/80 border border-slate-800 rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-cyan-500/10 border border-cyan-500/30 rounded-lg">
            <Activity className="w-6 h-6 text-cyan-400" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-slate-100">Real-Time Agent Status & Activity Stream</h2>
            <p className="text-xs text-slate-400">Live agent execution state telemetry, subagent events, and activity logs</p>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <span className={`inline-flex items-center gap-1.5 px-3 py-1 text-xs font-semibold rounded-full border ${badge.color}`}>
            <span className="w-2 h-2 rounded-full bg-current animate-ping" />
            {badge.label}
          </span>
          <span className={`inline-flex items-center gap-1 px-2.5 py-0.5 text-[11px] font-mono rounded-full border ${
            connected ? 'bg-emerald-500/10 text-emerald-400 border-emerald-500/30' : 'bg-rose-500/10 text-rose-400 border-rose-500/30'
          }`}>
            <Radio className="w-3 h-3" />
            {connected ? 'WS Live' : 'WS Disconnected'}
          </span>
        </div>
      </div>

      {/* Task Snapshot */}
      {currentTask && (
        <div className="p-4 bg-slate-900/60 border border-cyan-500/30 rounded-xl text-xs space-y-1">
          <span className="text-cyan-400 font-semibold">Active Agent Task:</span>
          <p className="text-slate-200 font-mono">{currentTask}</p>
        </div>
      )}

      {/* Activity Event Feed */}
      <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl space-y-4">
        <h3 className="text-sm font-semibold flex items-center gap-2 text-slate-200">
          <Terminal className="w-4 h-4 text-cyan-400" /> Activity Stream Feed
        </h3>

        {events.length === 0 ? (
          <div className="p-6 text-center text-xs text-slate-500 border border-dashed border-slate-800 rounded-xl">
            No activity events recorded yet.
          </div>
        ) : (
          <div className="space-y-2 max-h-96 overflow-y-auto pr-1">
            {events.map((evt) => (
              <div key={evt.event_id} className="p-3 bg-slate-950/70 border border-slate-800/80 rounded-xl space-y-1.5 text-xs">
                <div className="flex items-center justify-between">
                  <div className="flex items-center gap-2">
                    <span className="font-mono text-[10px] px-2 py-0.5 bg-slate-800 text-cyan-400 rounded">
                      {evt.status}
                    </span>
                    {evt.active_tool && (
                      <span className="font-mono text-[10px] px-2 py-0.5 bg-purple-500/10 text-purple-300 border border-purple-500/30 rounded">
                        tool: {evt.active_tool}
                      </span>
                    )}
                  </div>
                  <span className="text-[10px] font-mono text-slate-500">
                    {new Date(evt.timestamp * 1000).toLocaleTimeString()}
                  </span>
                </div>
                <p className="text-slate-300 font-sans">{evt.message}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};
