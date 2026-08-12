import React, { useState, useEffect } from 'react';
import { API_BASE_URL } from '../config';

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
  const [selectedNode, setSelectedNode] = useState<WorkflowNode | null>(null);
  const [aiPrompt, setAiPrompt] = useState('');
  const [isGenerating, setIsGenerating] = useState(false);
  const [executionLogs, setExecutionLogs] = useState<any[]>([]);
  const [isExecuting, setIsExecuting] = useState(false);
  const [oauthConnections, setOauthConnections] = useState<Record<string, { connected: boolean; updated_at: number | null }>>({});

  // Interactive OAuth Modal state
  const [activeModalProvider, setActiveModalProvider] = useState<{ id: string; name: string; icon: string } | null>(null);
  const [manualTokenInput, setManualTokenInput] = useState('');
  const [gmailEmailInput, setGmailEmailInput] = useState('');
  const [gmailAppPassInput, setGmailAppPassInput] = useState('');
  const [clientIdInput, setClientIdInput] = useState('');
  const [isConnecting, setIsConnecting] = useState(false);
  const [showDevConfig, setShowDevConfig] = useState(false);

  const fetchWorkflows = async () => {
    try {
      const resp = await fetch(`${API_BASE_URL}/api/workflows/list`);
      const data = await resp.json();
      setWorkflows(data.workflows || []);
    } catch (e) {
      console.error('Failed to load workflows:', e);
    }
  };

  const fetchOAuthStatus = async () => {
    try {
      const resp = await fetch(`${API_BASE_URL}/api/auth/oauth/status`);
      const data = await resp.json();
      setOauthConnections(data.connections || {});
    } catch (e) {
      console.error('Failed to fetch OAuth connections:', e);
    }
  };

  useEffect(() => {
    fetchWorkflows();
    fetchOAuthStatus();
  }, []);

  const handleOpenOAuthModal = (provider: { id: string; name: string; icon: string }) => {
    setActiveModalProvider(provider);
    setManualTokenInput('');
    setGmailEmailInput('');
    setGmailAppPassInput('');
    setClientIdInput('');
    setShowDevConfig(false);
  };

  const handleOAuthDisconnect = async (providerId: string) => {
    try {
      await fetch(`${API_BASE_URL}/api/auth/oauth/disconnect/${providerId}`, { method: 'DELETE' });
      fetchOAuthStatus();
    } catch (e) {
      console.error('OAuth disconnect failed:', e);
    }
  };

  const handleSaveGmailAppPassword = async () => {
    if (!gmailEmailInput.trim() || !gmailAppPassInput.trim()) return;
    setIsConnecting(true);
    try {
      await fetch(`${API_BASE_URL}/api/auth/google/app-password`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: gmailEmailInput.trim(), app_password: gmailAppPassInput.trim() })
      });
      await fetchOAuthStatus();
      setActiveModalProvider(null);
    } catch (e) {
      console.error('Gmail app password save failed:', e);
    } finally {
      setIsConnecting(false);
    }
  };

  const handleOpenBrowserLogin = async () => {
    if (!activeModalProvider) return;
    setIsConnecting(true);

    try {
      const resp = await fetch(`${API_BASE_URL}/api/auth/oauth/authorize`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ provider: activeModalProvider.id, redirect_uri: window.location.origin + '/oauth/callback' })
      });
      const data = await resp.json();

      if (data.auth_url) {
        window.open(
          data.auth_url,
          '_blank',
          'width=600,height=700,resizable=yes,scrollbars=yes,status=no,location=no,toolbar=no,menubar=no'
        );
      }
    } catch (e) {
      console.error('OAuth popup launch failed:', e);
    } finally {
      setIsConnecting(false);
    }
  };

  const handleSaveClientId = async () => {
    if (!activeModalProvider || !clientIdInput.trim()) return;
    try {
      await fetch(`${API_BASE_URL}/api/auth/oauth/config`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ provider: activeModalProvider.id, client_id: clientIdInput.trim() })
      });
      alert(`OAuth Client ID for ${activeModalProvider.name} saved successfully!`);
      setShowDevConfig(false);
    } catch (e) {
      console.error('Failed to save Client ID:', e);
    }
  };

  const handleSaveManualToken = async () => {
    if (!activeModalProvider || !manualTokenInput.trim()) return;
    setIsConnecting(true);
    try {
      await fetch(`${API_BASE_URL}/api/auth/oauth/callback`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          state: 'manual_state',
          code: manualTokenInput.trim(),
          provider: activeModalProvider.id,
          redirect_uri: window.location.origin + '/oauth/callback'
        })
      });
      await fetchOAuthStatus();
      setActiveModalProvider(null);
    } catch (e) {
      console.error('Manual token submission failed:', e);
    } finally {
      setIsConnecting(false);
    }
  };

  const handleCreateAiWorkflow = async () => {
    if (!aiPrompt.trim()) return;
    setIsGenerating(true);
    try {
      const resp = await fetch(`${API_BASE_URL}/api/workflows/ai-create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ goal: aiPrompt })
      });
      const data = await resp.json();
      if (data.workflow) {
        setSelectedWorkflow(data.workflow);
        setAiPrompt('');
        fetchWorkflows();
      }
    } catch (e) {
      console.error('AI Workflow creation failed:', e);
    } finally {
      setIsGenerating(false);
    }
  };

  const handleExecuteWorkflow = async (id: string) => {
    setIsExecuting(true);
    try {
      const resp = await fetch(`${API_BASE_URL}/api/workflows/${id}/execute`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({})
      });
      const data = await resp.json();
      setExecutionLogs(data.data?.logs || []);
    } catch (e) {
      console.error('Execution failed:', e);
    } finally {
      setIsExecuting(false);
    }
  };

  const handleDeleteWorkflow = async (id: string) => {
    try {
      await fetch(`${API_BASE_URL}/api/workflows/${id}`, { method: 'DELETE' });
      if (selectedWorkflow?.id === id) setSelectedWorkflow(null);
      fetchWorkflows();
    } catch (e) {
      console.error('Failed to delete workflow:', e);
    }
  };

  const handleAddActionNode = async (type: string, name: string) => {
    if (!selectedWorkflow) return;
    const newNodeId = `node_${selectedWorkflow.nodes.length + 1}`;
    const newNode: WorkflowNode = {
      id: newNodeId,
      type,
      name,
      parameters: type === 'action_cloudflare' ? { domain: 'example.com' } : type === 'action_gmail' ? { to: 'admin@example.com', subject: 'Alert' } : {}
    };
    const lastNodeId = selectedWorkflow.nodes[selectedWorkflow.nodes.length - 1]?.id || 'node_1';
    const updatedNodes = [...selectedWorkflow.nodes, newNode];
    const updatedEdges = [...selectedWorkflow.edges, { from: lastNodeId, to: newNodeId }];

    try {
      const resp = await fetch(`${API_BASE_URL}/api/workflows/create`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: selectedWorkflow.name,
          nodes: updatedNodes,
          edges: updatedEdges,
          active: true
        })
      });
      const data = await resp.json();
      if (data.workflow) {
        setSelectedWorkflow(data.workflow);
        fetchWorkflows();
      }
    } catch (e) {
      console.error('Failed to add node:', e);
    }
  };

  const handleUpdateNodeParameter = (key: string, val: string) => {
    if (!selectedWorkflow || !selectedNode) return;
    const updatedNodes = selectedWorkflow.nodes.map(n => {
      if (n.id === selectedNode.id) {
        return { ...n, parameters: { ...n.parameters, [key]: val } };
      }
      return n;
    });
    setSelectedWorkflow({ ...selectedWorkflow, nodes: updatedNodes });
    setSelectedNode({ ...selectedNode, parameters: { ...selectedNode.parameters, [key]: val } });
  };

  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6 text-slate-200">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-slate-800 pb-4">
        <div>
          <h1 className="text-2xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-cyan-400 via-teal-300 to-indigo-400">
            Meridian-X Workflow Automation Engine
          </h1>
          <p className="text-sm text-slate-400 mt-1">
            Visual DAG pipeline runner & AI-powered workflow generator with OAuth service integration.
          </p>
        </div>
      </div>

      {/* OAuth Connected Services Toolbar */}
      <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 space-y-3">
        <h2 className="text-xs font-bold uppercase tracking-wider text-slate-400">OAuth Services Sign-In & Status</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {[
            { id: 'google', name: 'Google Workspace', icon: '🌐' },
            { id: 'github', name: 'GitHub', icon: '🐙' },
            { id: 'cloudflare', name: 'Cloudflare', icon: '⚡' },
            { id: 'custom_oidc', name: 'Custom OIDC', icon: '🔑' }
          ].map(provider => {
            const isConnected = oauthConnections[provider.id]?.connected;
            return (
              <div key={provider.id} className="bg-slate-950/60 border border-slate-800 p-3 rounded-lg flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="text-base">{provider.icon}</span>
                  <div>
                    <div className="text-xs font-bold text-slate-200">{provider.name}</div>
                    <div className="text-[10px] text-slate-400">{isConnected ? '✓ Connected' : 'Not Connected'}</div>
                  </div>
                </div>
                {isConnected ? (
                  <button
                    onClick={() => handleOAuthDisconnect(provider.id)}
                    className="px-2.5 py-1 text-xs font-semibold rounded bg-rose-600/20 hover:bg-rose-600/40 text-rose-400 border border-rose-500/30 transition"
                  >
                    Disconnect
                  </button>
                ) : (
                  <button
                    onClick={() => handleOpenOAuthModal(provider)}
                    className="px-2.5 py-1 text-xs font-semibold rounded bg-cyan-600 hover:bg-cyan-500 text-white transition"
                  >
                    Sign In
                  </button>
                )}
              </div>
            );
          })}
        </div>
      </div>

      {/* Interactive OAuth Sign In Modal */}
      {activeModalProvider && (
        <div className="fixed inset-0 z-50 bg-black/75 backdrop-blur-md flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-700 rounded-2xl p-6 max-w-md w-full space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-slate-800 pb-3">
              <h3 className="text-lg font-bold text-white flex items-center gap-2">
                <span>{activeModalProvider.icon}</span>
                <span>Sign In to {activeModalProvider.name}</span>
              </h3>
              <button
                onClick={() => setActiveModalProvider(null)}
                className="text-slate-400 hover:text-white text-lg font-bold"
              >
                ✕
              </button>
            </div>

            <div className="space-y-3">
              {/* Special Gmail App Password Option for Google */}
              {activeModalProvider.id === 'google' ? (
                <div className="bg-emerald-950/40 border border-emerald-500/40 p-3.5 rounded-xl space-y-2">
                  <div className="flex items-center justify-between">
                    <label className="text-xs font-bold text-emerald-300 uppercase block">⭐ Option 1: Gmail App Password (Zero Verification!)</label>
                    <a
                      href="https://myaccount.google.com/apppasswords"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-[10px] font-semibold text-emerald-400 hover:underline bg-emerald-900/60 px-2 py-0.5 rounded border border-emerald-500/30"
                    >
                      Generate App Password ↗
                    </a>
                  </div>
                  <div className="text-[11px] text-slate-300 space-y-1 bg-black/30 p-2 rounded border border-emerald-900/50">
                    <div className="font-semibold text-emerald-400">💡 3-Step Setup Guide:</div>
                    <div>1. Click <b>Generate App Password ↗</b> button above.</div>
                    <div>2. Type <i>Meridian-X</i> as app name and click <b>Create</b>.</div>
                    <div>3. Copy the 16-character code and paste below!</div>
                  </div>
                  <input
                    type="email"
                    placeholder="your_email@gmail.com"
                    value={gmailEmailInput}
                    onChange={(e) => setGmailEmailInput(e.target.value)}
                    className="w-full px-3 py-1.5 bg-slate-900 border border-slate-700 rounded text-xs text-slate-100 focus:outline-none focus:border-emerald-500"
                  />
                  <input
                    type="password"
                    placeholder="16-character App Password (e.g. abcd efgh ijkl mnop)"
                    value={gmailAppPassInput}
                    onChange={(e) => setGmailAppPassInput(e.target.value)}
                    className="w-full px-3 py-1.5 bg-slate-900 border border-slate-700 rounded text-xs text-slate-100 focus:outline-none focus:border-emerald-500"
                  />
                  <button
                    onClick={handleSaveGmailAppPassword}
                    disabled={!gmailEmailInput.trim() || !gmailAppPassInput.trim() || isConnecting}
                    className="w-full py-2 bg-emerald-600 hover:bg-emerald-500 disabled:opacity-50 text-white font-medium text-xs rounded-lg transition"
                  >
                    {isConnecting ? 'Saving...' : 'Connect Gmail via App Password'}
                  </button>
                </div>
              ) : null}

              {/* Personal Access Token / API Key Option */}
              <div className="bg-slate-950 border border-slate-800 p-3.5 rounded-xl space-y-2">
                <div className="flex items-center justify-between">
                  <label className="text-xs font-bold text-teal-400 uppercase block">
                    {activeModalProvider.id === 'google' ? 'Option 2: Personal Access Token / API Key' : 'Option 1: Personal Access Token / API Key'}
                  </label>
                  {activeModalProvider.id === 'github' && (
                    <a
                      href="https://github.com/settings/tokens"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-[10px] font-semibold text-teal-400 hover:underline bg-teal-900/60 px-2 py-0.5 rounded border border-teal-500/30"
                    >
                      Generate GitHub Token ↗
                    </a>
                  )}
                  {activeModalProvider.id === 'cloudflare' && (
                    <a
                      href="https://dash.cloudflare.com/profile/api-tokens"
                      target="_blank"
                      rel="noopener noreferrer"
                      className="text-[10px] font-semibold text-teal-400 hover:underline bg-teal-900/60 px-2 py-0.5 rounded border border-teal-500/30"
                    >
                      Generate Cloudflare Token ↗
                    </a>
                  )}
                </div>

                {activeModalProvider.id === 'github' && (
                  <div className="text-[11px] text-slate-300 space-y-1 bg-black/30 p-2 rounded border border-slate-800">
                    <div className="font-semibold text-teal-400">💡 2-Step GitHub Setup Guide:</div>
                    <div>1. Click <b>Generate GitHub Token ↗</b> above (select <i>repo</i> & <i>workflow</i>).</div>
                    <div>2. Paste your token (starts with <code>ghp_</code>) below!</div>
                  </div>
                )}

                <input
                  type="password"
                  placeholder={`Paste ${activeModalProvider.name} Token / Key...`}
                  value={manualTokenInput}
                  onChange={(e) => setManualTokenInput(e.target.value)}
                  className="w-full px-3 py-2 bg-slate-900 border border-slate-700 rounded-lg text-xs text-slate-100 focus:outline-none focus:border-teal-500"
                />
                <button
                  onClick={handleSaveManualToken}
                  disabled={!manualTokenInput.trim() || isConnecting}
                  className="w-full py-2 bg-teal-600 hover:bg-teal-500 disabled:opacity-50 text-white font-medium text-xs rounded-lg transition"
                >
                  {isConnecting ? 'Saving...' : 'Connect with Token'}
                </button>
              </div>

              {/* Standard OAuth Browser Popup Option */}
              <div className="bg-slate-950 border border-slate-800 p-3.5 rounded-xl space-y-2">
                <label className="text-xs font-bold text-cyan-400 uppercase block">Option A: Browser OAuth 2.0 Popup</label>
                <p className="text-[11px] text-slate-400">Launches floating authorization popup window for {activeModalProvider.name}.</p>
                <button
                  onClick={handleOpenBrowserLogin}
                  disabled={isConnecting}
                  className="w-full py-2 bg-gradient-to-r from-cyan-600 to-teal-600 hover:from-cyan-500 hover:to-teal-500 text-white font-medium text-xs rounded-lg transition"
                >
                  🚀 Open Browser Login Popup
                </button>
              </div>

              {/* Developer Client ID Setup Accordion */}
              <div className="border-t border-slate-800 pt-2">
                <button
                  onClick={() => setShowDevConfig(!showDevConfig)}
                  className="text-xs text-indigo-400 hover:text-indigo-300 font-semibold flex items-center gap-1"
                >
                  <span>{showDevConfig ? '▼' : '▶'}</span>
                  <span>⚡ Developer Settings: Configure Client ID</span>
                </button>

                {showDevConfig && (
                  <div className="mt-2 p-3 bg-indigo-950/30 border border-indigo-500/30 rounded-xl space-y-2">
                    <label className="text-[10px] uppercase font-bold text-indigo-300 block">OAuth Client ID</label>
                    <input
                      type="text"
                      placeholder={`e.g. 123456.apps.googleusercontent.com`}
                      value={clientIdInput}
                      onChange={(e) => setClientIdInput(e.target.value)}
                      className="w-full px-3 py-1.5 bg-slate-950 border border-slate-700 rounded text-xs text-slate-100 focus:outline-none focus:border-indigo-500"
                    />
                    <button
                      onClick={handleSaveClientId}
                      disabled={!clientIdInput.trim()}
                      className="w-full py-1.5 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white font-medium text-xs rounded transition"
                    >
                      Save Client ID to Vault
                    </button>
                  </div>
                )}
              </div>
            </div>

            <div className="flex justify-end pt-2">
              <button
                onClick={() => setActiveModalProvider(null)}
                className="px-4 py-1.5 text-xs text-slate-400 hover:text-slate-200"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* AI Prompt Natural Language Workflow Generator Bar */}
      <div className="bg-gradient-to-r from-indigo-950/40 via-slate-900 to-teal-950/40 border border-indigo-500/30 rounded-xl p-4 flex flex-col sm:flex-row gap-3 items-center">
        <div className="flex-1 w-full">
          <label className="text-xs font-bold text-indigo-300 uppercase tracking-wider block mb-1">
            ✨ Ask Chatbot to Build Workflow Automatically
          </label>
          <input
            type="text"
            placeholder="e.g. 'check cloudflare domain myapp.com every hour and send alert email via gmail'"
            value={aiPrompt}
            onChange={(e) => setAiPrompt(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleCreateAiWorkflow()}
            className="w-full px-3.5 py-2 bg-slate-950 border border-slate-700 rounded-lg text-sm text-slate-100 focus:outline-none focus:border-indigo-500"
          />
        </div>
        <button
          onClick={handleCreateAiWorkflow}
          disabled={isGenerating}
          className="w-full sm:w-auto px-5 py-2 bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-sm rounded-lg transition flex items-center justify-center gap-2"
        >
          {isGenerating ? 'Generating...' : '✨ Generate Workflow'}
        </button>
      </div>

      {/* Workflow Builder Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left List */}
        <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-4 space-y-3">
          <h2 className="text-sm font-bold text-slate-300 border-b border-slate-800 pb-2">Active Workflows</h2>
          {workflows.length === 0 ? (
            <p className="text-xs text-slate-500 py-6 text-center">No workflows created. Use AI prompt above to create your first flow!</p>
          ) : (
            workflows.map((wf) => (
              <div
                key={wf.id}
                onClick={() => {
                  setSelectedWorkflow(wf);
                  setSelectedNode(null);
                }}
                className={`p-3 rounded-lg border cursor-pointer transition flex items-center justify-between ${
                  selectedWorkflow?.id === wf.id
                    ? 'border-cyan-500 bg-cyan-950/30'
                    : 'border-slate-800 bg-slate-950/40 hover:border-slate-700'
                }`}
              >
                <div>
                  <h3 className="font-semibold text-sm text-slate-100">{wf.name}</h3>
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
                    className="p-1.5 bg-rose-600/20 hover:bg-rose-600/40 text-rose-400 rounded text-xs"
                  >
                    🗑
                  </button>
                </div>
              </div>
            ))
          )}
        </div>

        {/* Center Node Visual Graph & Editor */}
        <div className="lg:col-span-2 space-y-4">
          {selectedWorkflow ? (
            <div className="bg-slate-900/80 border border-slate-800 rounded-xl p-5 space-y-5">
              <div className="flex items-center justify-between border-b border-slate-800 pb-3">
                <h2 className="text-lg font-bold text-white flex items-center gap-2">
                  <span>{selectedWorkflow.name}</span>
                  <span className="text-xs px-2 py-0.5 bg-cyan-500/20 text-cyan-400 rounded-full font-mono">
                    {selectedWorkflow.id}
                  </span>
                </h2>
                <div className="flex gap-2">
                  <button
                    onClick={() => handleAddActionNode('action_cloudflare', 'Check Cloudflare')}
                    className="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-cyan-300 rounded border border-slate-700"
                  >
                    + Cloudflare Node
                  </button>
                  <button
                    onClick={() => handleAddActionNode('action_gmail', 'Send Gmail')}
                    className="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-teal-300 rounded border border-slate-700"
                  >
                    + Gmail Node
                  </button>
                </div>
              </div>

              {/* Node Visual Flow Diagram */}
              <div className="space-y-2">
                <span className="text-xs font-bold text-slate-400 uppercase tracking-wider">Interactive Node Flow (Click Node to Edit Parameters)</span>
                <div className="flex flex-wrap items-center gap-3 bg-slate-950 p-5 rounded-xl border border-slate-800">
                  {selectedWorkflow.nodes.map((node, idx) => (
                    <React.Fragment key={node.id}>
                      <div
                        onClick={() => setSelectedNode(node)}
                        className={`px-4 py-3 rounded-xl border cursor-pointer transition flex flex-col gap-1 min-w-[150px] ${
                          selectedNode?.id === node.id
                            ? 'border-cyan-400 bg-cyan-950/60 shadow-[0_0_15px_rgba(0,240,255,0.3)]'
                            : 'border-slate-700 bg-slate-900 hover:border-slate-600'
                        }`}
                      >
                        <span className="text-[10px] font-mono text-cyan-400 uppercase tracking-wider">{node.type}</span>
                        <span className="text-sm font-bold text-slate-100">{node.name}</span>
                        <span className="text-[10px] text-slate-400 font-mono">ID: {node.id}</span>
                      </div>
                      {idx < selectedWorkflow.nodes.length - 1 && (
                        <span className="text-slate-500 font-bold text-xl">➔</span>
                      )}
                    </React.Fragment>
                  ))}
                </div>
              </div>

              {/* Selected Node Parameter Inspector */}
              {selectedNode && (
                <div className="bg-slate-950 border border-slate-800 rounded-xl p-4 space-y-3">
                  <h3 className="text-xs font-bold text-cyan-300 uppercase tracking-wider border-b border-slate-800 pb-2">
                    Node Inspector Parameters — {selectedNode.name} ({selectedNode.id})
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {Object.entries(selectedNode.parameters).map(([paramKey, paramVal]) => (
                      <div key={paramKey}>
                        <label className="text-[10px] font-mono uppercase text-slate-400 block mb-1">{paramKey}</label>
                        <input
                          type="text"
                          value={String(paramVal)}
                          onChange={(e) => handleUpdateNodeParameter(paramKey, e.target.value)}
                          className="w-full px-3 py-1.5 bg-slate-900 border border-slate-700 rounded text-xs text-slate-200 focus:outline-none focus:border-cyan-500"
                        />
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Execution Logs Output */}
              {executionLogs.length > 0 && (
                <div className="space-y-2 border-t border-slate-800 pt-4">
                  <h3 className="text-xs font-bold text-teal-400 uppercase tracking-wider">Execution Pipeline Output Logs</h3>
                  <div className="bg-black/80 p-4 rounded-xl font-mono text-xs text-slate-300 space-y-3 max-h-64 overflow-y-auto border border-slate-800">
                    {executionLogs.map((log, i) => (
                      <div key={i} className="border-b border-slate-800/80 pb-2">
                        <div className="flex items-center gap-2">
                          <span className="text-cyan-400">[{log.type}]</span>
                          <span className="text-white font-bold">{log.name}</span>
                          <span className="text-teal-400 font-bold uppercase text-[10px]">{log.status}</span>
                        </div>
                        <pre className="text-slate-400 mt-1.5 whitespace-pre-wrap">{JSON.stringify(log.output, null, 2)}</pre>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="bg-slate-900/40 border border-slate-800/80 rounded-xl p-12 text-center text-slate-500">
              Select or generate a workflow to view and edit interactive node pipeline graphs.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default WorkflowBuilder;
