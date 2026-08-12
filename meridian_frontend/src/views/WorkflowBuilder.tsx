import React, { useState, useEffect } from 'react';
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:4132';

interface WorkflowNode {
  id: string;
  type: string;
  name: string;
  parameters: Record<string, any>;
}

interface WorkflowEdge {
  from: string;
  to: string;
}

interface Workflow {
  id: string;
  name: string;
  active: boolean;
  nodes: WorkflowNode[];
  edges: WorkflowEdge[];
  execution_count?: number;
  last_executed?: number;
}

export const WorkflowBuilder: React.FC = () => {
  const [workflows, setWorkflows] = useState<Workflow[]>([]);
  const [selectedWorkflow, setSelectedWorkflow] = useState<Workflow | null>(null);
  const [newWorkflowName, setNewWorkflowName] = useState('');
  const [executionLogs, setExecutionLogs] = useState<any[]>([]);
  const [isExecuting, setIsExecuting] = useState(false);

  const fetchWorkflows = async () => {
    try {
      const resp = await axios.get(`${API_BASE_URL}/api/workflows/list`);
      setWorkflows(resp.data.workflows || []);
    } catch (e) {
      console.error('Failed to load workflows:', e);
    }
  };

  useEffect(() => {
    fetchWorkflows();
  }, []);

  const handleCreateSampleWorkflow = async () => {
    if (!newWorkflowName.trim()) return;
    const sampleNodes: WorkflowNode[] = [
      { id: 'node_1', type: 'trigger_webhook', name: 'Incoming Webhook', parameters: {} },
      { id: 'node_2', type: 'action_cloudflare', name: 'Check Domain Status', parameters: { domain: 'example.com' } },
      { id: 'node_3', type: 'action_gmail', name: 'Send Executive Briefing', parameters: { to: 'user@example.com', subject: 'Cloudflare Status', body: 'Domain is active.' } }
    ];
    const sampleEdges: WorkflowEdge[] = [
      { from: 'node_1', to: 'node_2' },
      { from: 'node_2', to: 'node_3' }
    ];

    try {
      await axios.post(`${API_BASE_URL}/api/workflows/create`, {
        name: newWorkflowName,
        nodes: sampleNodes,
        edges: sampleEdges,
        active: true
      });
      setNewWorkflowName('');
      fetchWorkflows();
    } catch (e) {
      console.error('Failed to create workflow:', e);
    }
  };

  const handleExecuteWorkflow = async (id: string) => {
    setIsExecuting(true);
    try {
      const resp = await axios.post(`${API_BASE_URL}/api/workflows/${id}/execute`, {});
      setExecutionLogs(resp.data.data?.logs || []);
    } catch (e) {
      console.error('Execution failed:', e);
    } finally {
      setIsExecuting(false);
    }
  };

  const handleDeleteWorkflow = async (id: string) => {
    try {
      await axios.delete(`${API_BASE_URL}/api/workflows/${id}`);
      if (selectedWorkflow?.id === id) setSelectedWorkflow(null);
      fetchWorkflows();
    } catch (e) {
      console.error('Failed to delete workflow:', e);
    }
  };

  return (
    <div className="p-6 max-w-6xl mx-auto space-y-6 text-slate-200">
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-teal-300">
            n8n Workflow Automation Engine
          </h1>
          <p className="text-sm text-slate-400 mt-1">
            Build event-driven node pipelines connecting Google Workspace, GitHub, Cloudflare, and LLM actions.
          </p>
        </div>
        <div className="flex gap-2">
          <input
            type="text"
            placeholder="New Workflow Name..."
            value={newWorkflowName}
            onChange={(e) => setNewWorkflowName(e.target.value)}
            className="px-3 py-1.5 bg-slate-900 border border-slate-700 rounded-lg text-sm focus:outline-none focus:border-blue-500"
          />
          <button
            onClick={handleCreateSampleWorkflow}
            className="px-4 py-1.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-sm font-medium transition"
          >
            + Create Workflow
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        {/* Workflow List */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 space-y-3">
          <h2 className="text-lg font-semibold text-slate-300 border-b border-slate-800 pb-2">Active Workflows</h2>
          {workflows.length === 0 ? (
            <p className="text-sm text-slate-500 py-4 text-center">No workflows configured.</p>
          ) : (
            workflows.map((wf) => (
              <div
                key={wf.id}
                onClick={() => setSelectedWorkflow(wf)}
                className={`p-3 rounded-lg border cursor-pointer transition flex items-center justify-between ${
                  selectedWorkflow?.id === wf.id
                    ? 'border-blue-500 bg-blue-950/30'
                    : 'border-slate-800 bg-slate-950/40 hover:border-slate-700'
                }`}
              >
                <div>
                  <h3 className="font-medium text-sm text-white">{wf.name}</h3>
                  <span className="text-xs text-slate-400">{wf.nodes.length} Nodes • Runs: {wf.execution_count || 0}</span>
                </div>
                <div className="flex items-center gap-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleExecuteWorkflow(wf.id);
                    }}
                    disabled={isExecuting}
                    className="p-1.5 bg-teal-600/30 hover:bg-teal-600/50 text-teal-300 rounded text-xs font-semibold"
                  >
                    ▶ Run
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDeleteWorkflow(wf.id);
                    }}
                    className="p-1.5 bg-red-600/20 hover:bg-red-600/40 text-red-400 rounded text-xs"
                  >
                    🗑
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Node Graph & Logs Detail */}
        <div className="md:col-span-2 space-y-4">
          {selectedWorkflow ? (
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-4">
              <h2 className="text-lg font-bold text-white flex items-center gap-2">
                <span>{selectedWorkflow.name}</span>
                <span className="text-xs px-2 py-0.5 bg-teal-500/20 text-teal-400 rounded-full font-mono">
                  {selectedWorkflow.id}
                </span>
              </h2>

              <div className="space-y-3">
                <h3 className="text-sm font-semibold text-slate-400">Node Pipeline Graph</h3>
                <div className="flex flex-wrap items-center gap-3 bg-slate-950 p-4 rounded-xl border border-slate-800">
                  {selectedWorkflow.nodes.map((node, idx) => (
                    <React.Fragment key={node.id}>
                      <div className="bg-slate-900 border border-slate-700 px-4 py-3 rounded-lg flex flex-col gap-1 min-w-[140px]">
                        <span className="text-xs font-mono text-blue-400 uppercase">{node.type}</span>
                        <span className="text-sm font-bold text-slate-200">{node.name}</span>
                      </div>
                      {idx < selectedWorkflow.nodes.length - 1 && (
                        <span className="text-slate-500 font-bold text-lg">➔</span>
                      )}
                    </React.Fragment>
                  ))}
                </div>
              </div>

              {/* Execution Logs */}
              {executionLogs.length > 0 && (
                <div className="space-y-2 border-t border-slate-800 pt-4">
                  <h3 className="text-sm font-semibold text-teal-400">Execution Output Logs</h3>
                  <div className="bg-black/70 p-3 rounded-lg font-mono text-xs text-slate-300 space-y-2 max-h-60 overflow-y-auto">
                    {executionLogs.map((log, i) => (
                      <div key={i} className="border-b border-slate-800/60 pb-1">
                        <span className="text-blue-400">[{log.type}]</span> <span className="text-white font-bold">{log.name}</span>: <span className="text-teal-300">{log.status}</span>
                        <pre className="text-slate-400 mt-1 whitespace-pre-wrap">{JSON.stringify(log.output, null, 2)}</pre>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="bg-slate-900/40 border border-slate-800/80 rounded-xl p-12 text-center text-slate-500">
              Select or create a workflow to view node pipeline graph and execution logs.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default WorkflowBuilder;
