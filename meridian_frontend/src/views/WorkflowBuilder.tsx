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

  const openExternalUrl = async (url: string) => {
    try {
      await fetch(`${API_BASE_URL}/api/utils/open-url`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ url })
      });
    } catch {
      window.open(url, '_blank');
    }
  };

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
        await openExternalUrl(data.auth_url);
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
    <div className="p-6 max-w-7xl mx-auto space-y-6 text-[var(--text-main)]">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-[var(--border-subtle)] pb-4">
        <div>
          <h1 className="text-2xl font-bold text-[var(--text-bright)]" style={{ fontFamily: 'var(--font-heading)' }}>
            Meridian-X Workflow Automation Engine
          </h1>
          <p className="text-sm text-[var(--text-dim)] mt-1">
            Visual DAG pipeline runner & AI-powered workflow generator with OAuth service integration.
          </p>
        </div>
      </div>

      {/* OAuth Connected Services Toolbar */}
      <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-4 space-y-3">
        <h2 className="text-xs font-bold uppercase tracking-wider text-[var(--text-dim)]">OAuth Services Sign-In & Status</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
          {[
            { id: 'google', name: 'Google Workspace', icon: '🌐' },
            { id: 'github', name: 'GitHub', icon: '🐙' },
            { id: 'cloudflare', name: 'Cloudflare', icon: '⚡' },
            { id: 'custom_oidc', name: 'Custom OIDC', icon: '🔑' }
          ].map(provider => {
            const isConnected = oauthConnections[provider.id]?.connected;
            return (
              <div key={provider.id} className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] p-3 rounded-lg flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <span className="text-base">{provider.icon}</span>
                  <div>
                    <div className="text-xs font-bold text-[var(--text-main)]">{provider.name}</div>
                    <div className="text-[10px] text-[var(--text-dim)]">{isConnected ? '✓ Connected' : 'Not Connected'}</div>
                  </div>
                </div>
                {isConnected ? (
                  <button
                    onClick={() => handleOAuthDisconnect(provider.id)}
                    className="px-2.5 py-1 text-xs font-semibold rounded bg-[color-mix(in_srgb,var(--danger)_15%,transparent)] hover:bg-[color-mix(in_srgb,var(--danger)_25%,transparent)] text-[var(--danger)] border border-[var(--danger)] transition"
                  >
                    Disconnect
                  </button>
                ) : (
                  <button
                    onClick={() => handleOpenOAuthModal(provider)}
                    className="px-2.5 py-1 text-xs font-semibold rounded bg-[var(--accent)] text-[var(--bg-void)] transition"
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
        <div className="fixed inset-0 z-50 bg-[var(--bg-void)] backdrop-blur-md flex items-center justify-center p-4">
          <div className="bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded-2xl p-6 max-w-md w-full space-y-4 shadow-2xl">
            <div className="flex items-center justify-between border-b border-[var(--border-subtle)] pb-3">
              <h3 className="text-lg font-bold text-[var(--text-bright)] flex items-center gap-2">
                <span>{activeModalProvider.icon}</span>
                <span>Sign In to {activeModalProvider.name}</span>
              </h3>
              <button
                onClick={() => setActiveModalProvider(null)}
                className="text-[var(--text-dim)] hover:text-[var(--text-bright)] text-lg font-bold"
              >
                ✕
              </button>
            </div>

            <div className="space-y-3">
              {/* Special Gmail App Password Option for Google */}
              {activeModalProvider.id === 'google' ? (
                <div className="bg-[var(--bg-surface)] border border-[var(--success)] p-3.5 rounded-xl space-y-2">
                  <div className="flex items-center justify-between">
                    <label className="text-xs font-bold text-[var(--success)] uppercase block">⭐ Option 1: Gmail App Password (Zero Verification!)</label>
                    <button
                      onClick={() => openExternalUrl('https://myaccount.google.com/apppasswords')}
                      className="text-[10px] font-semibold text-[var(--success)] hover:text-[var(--text-bright)] bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] px-2 py-0.5 rounded border border-[var(--success)] transition cursor-pointer"
                    >
                      Generate App Password ↗
                    </button>
                  </div>
                  <div className="text-[11px] text-[var(--text-main)] space-y-1 bg-[var(--bg-void)] p-2 rounded border border-[var(--border-subtle)]">
                    <div className="font-semibold text-[var(--success)]">💡 3-Step Setup Guide:</div>
                    <div>1. Click <b>Generate App Password ↗</b> button above.</div>
                    <div>2. Type <i>Meridian-X</i> as app name and click <b>Create</b>.</div>
                    <div>3. Copy the 16-character code and paste below!</div>
                  </div>
                  <input
                    type="email"
                    placeholder="your_email@gmail.com"
                    value={gmailEmailInput}
                    onChange={(e) => setGmailEmailInput(e.target.value)}
                    className="w-full px-3 py-1.5 bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded text-xs text-[var(--text-bright)] focus:outline-none focus:border-[var(--success)]"
                  />
                  <input
                    type="password"
                    placeholder="16-character App Password (e.g. abcd efgh ijkl mnop)"
                    value={gmailAppPassInput}
                    onChange={(e) => setGmailAppPassInput(e.target.value)}
                    className="w-full px-3 py-1.5 bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded text-xs text-[var(--text-bright)] focus:outline-none focus:border-[var(--success)]"
                  />
                  <button
                    onClick={handleSaveGmailAppPassword}
                    disabled={!gmailEmailInput.trim() || !gmailAppPassInput.trim() || isConnecting}
                    className="w-full py-2 bg-[var(--success)] text-[var(--bg-void)] font-medium text-xs rounded-lg transition disabled:opacity-50"
                  >
                    {isConnecting ? 'Saving...' : 'Connect Gmail via App Password'}
                  </button>
                </div>
              ) : null}

              {/* Personal Access Token / API Key Option */}
              <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] p-3.5 rounded-xl space-y-2">
                <div className="flex items-center justify-between">
                  <label className="text-xs font-bold text-[var(--accent)] uppercase block">
                    {activeModalProvider.id === 'google' ? 'Option 2: Personal Access Token / API Key' : 'Option 1: Personal Access Token / API Key'}
                  </label>
                  {activeModalProvider.id === 'github' && (
                    <button
                      onClick={() => openExternalUrl('https://github.com/settings/tokens')}
                      className="text-[10px] font-semibold text-[var(--accent)] hover:text-[var(--text-bright)] bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] px-2 py-0.5 rounded border border-[var(--accent)] transition cursor-pointer"
                    >
                      Generate GitHub Token ↗
                    </button>
                  )}
                  {activeModalProvider.id === 'cloudflare' && (
                    <button
                      onClick={() => openExternalUrl('https://dash.cloudflare.com/profile/api-tokens')}
                      className="text-[10px] font-semibold text-[var(--accent)] hover:text-[var(--text-bright)] bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] px-2 py-0.5 rounded border border-[var(--accent)] transition cursor-pointer"
                    >
                      Generate Cloudflare Token ↗
                    </button>
                  )}
                </div>

                {activeModalProvider.id === 'github' && (
                  <div className="text-[11px] text-[var(--text-main)] space-y-1 bg-[var(--bg-void)] p-2 rounded border border-[var(--border-subtle)]">
                    <div className="font-semibold text-[var(--accent)]">💡 2-Step GitHub Setup Guide:</div>
                    <div>1. Click <b>Generate GitHub Token ↗</b> above (select <i>repo</i> & <i>workflow</i>).</div>
                    <div>2. Paste your token (starts with <code>ghp_</code>) below!</div>
                  </div>
                )}

                <input
                  type="password"
                  placeholder={`Paste ${activeModalProvider.name} Token / Key...`}
                  value={manualTokenInput}
                  onChange={(e) => setManualTokenInput(e.target.value)}
                  className="w-full px-3 py-2 bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded-lg text-xs text-[var(--text-bright)] focus:outline-none focus:border-[var(--accent)]"
                />
                <button
                  onClick={handleSaveManualToken}
                  disabled={!manualTokenInput.trim() || isConnecting}
                  className="w-full py-2 bg-[var(--accent)] hover:bg-[var(--accent-dim)] disabled:opacity-50 text-[var(--bg-void)] font-medium text-xs rounded-lg transition"
                >
                  {isConnecting ? 'Saving...' : 'Connect with Token'}
                </button>
              </div>

              {/* Standard OAuth Browser Popup Option */}
              <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] p-3.5 rounded-xl space-y-2">
                <label className="text-xs font-bold text-[var(--accent)] uppercase block">Option A: Browser OAuth 2.0 Popup</label>
                <p className="text-[11px] text-[var(--text-dim)]">Launches floating authorization popup window for {activeModalProvider.name}.</p>
                <button
                  onClick={handleOpenBrowserLogin}
                  disabled={isConnecting}
                  className="w-full py-2 bg-[var(--accent)] text-[var(--bg-void)] font-medium text-xs rounded-lg transition"
                >
                  🚀 Open Browser Login Popup
                </button>
              </div>

              {/* Developer Client ID Setup Accordion */}
              <div className="border-t border-[var(--border-subtle)] pt-2">
                <button
                  onClick={() => setShowDevConfig(!showDevConfig)}
                  className="text-xs text-[var(--accent)] hover:text-[var(--accent)] font-semibold flex items-center gap-1"
                >
                  <span>{showDevConfig ? '▼' : '▶'}</span>
                  <span>⚡ Developer Settings: Configure Client ID</span>
                </button>

                {showDevConfig && (
                  <div className="mt-2 p-3 bg-[var(--bg-surface)] border border-[var(--border-active)] rounded-xl space-y-2">
                    <label className="text-[10px] uppercase font-bold text-[var(--accent)] block">OAuth Client ID</label>
                    <input
                      type="text"
                      placeholder={`e.g. 123456.apps.googleusercontent.com`}
                      value={clientIdInput}
                      onChange={(e) => setClientIdInput(e.target.value)}
                      className="w-full px-3 py-1.5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded text-xs text-[var(--text-bright)] focus:outline-none focus:border-[var(--accent)]"
                    />
                    <button
                      onClick={handleSaveClientId}
                      disabled={!clientIdInput.trim()}
                      className="w-full py-1.5 bg-[var(--accent)] hover:bg-[var(--accent-dim)] disabled:opacity-50 text-[var(--bg-void)] font-medium text-xs rounded transition"
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
                className="px-4 py-1.5 text-xs text-[var(--text-dim)] hover:text-[var(--text-main)]"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* AI Prompt Natural Language Workflow Generator Bar */}
      <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-4 flex flex-col sm:flex-row gap-3 items-center">
        <div className="flex-1 w-full">
          <label className="text-xs font-bold text-[var(--accent)] uppercase tracking-wider block mb-1">
            ✨ Ask Chatbot to Build Workflow Automatically
          </label>
          <input
            type="text"
            placeholder="e.g. 'check cloudflare domain myapp.com every hour and send alert email via gmail'"
            value={aiPrompt}
            onChange={(e) => setAiPrompt(e.target.value)}
            onKeyDown={(e) => e.key === 'Enter' && handleCreateAiWorkflow()}
            className="w-full px-3.5 py-2 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg text-sm text-[var(--text-bright)] focus:outline-none focus:border-[var(--accent)]"
          />
        </div>
        <button
          onClick={handleCreateAiWorkflow}
          disabled={isGenerating}
          className="w-full sm:w-auto px-5 py-2 bg-[var(--accent)] hover:bg-[var(--accent-dim)] text-[var(--bg-void)] font-medium text-sm rounded-lg transition flex items-center justify-center gap-2"
        >
          {isGenerating ? 'Generating...' : '✨ Generate Workflow'}
        </button>
      </div>

      {/* Workflow Builder Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left List */}
        <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-4 space-y-3">
          <h2 className="text-sm font-bold text-[var(--text-main)] border-b border-[var(--border-subtle)] pb-2">Active Workflows</h2>
          {workflows.length === 0 ? (
            <p className="text-xs text-[var(--text-ghost)] py-6 text-center">No workflows created. Use AI prompt above to create your first flow!</p>
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
                    ? 'border-[var(--accent)] bg-[var(--accent-muted)]'
                    : 'border-[var(--border-subtle)] bg-[var(--bg-panel)] hover:border-[var(--border-subtle)]'
                }`}
              >
                <div>
                  <h3 className="font-semibold text-sm text-[var(--text-bright)]">{wf.name}</h3>
                  <span className="text-xs text-[var(--text-dim)]">{wf.nodes.length} Nodes • Runs: {wf.execution_count || 0}</span>
                </div>
                <div className="flex items-center gap-2">
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleExecuteWorkflow(wf.id);
                    }}
                    disabled={isExecuting}
                    className="p-1.5 bg-[var(--accent-muted)] hover:bg-[var(--accent-muted)] text-[var(--accent)] rounded text-xs font-semibold"
                  >
                    ▶ Run
                  </button>
                  <button
                    onClick={(e) => {
                      e.stopPropagation();
                      handleDeleteWorkflow(wf.id);
                    }}
                    className="p-1.5 bg-[color-mix(in_srgb,var(--danger)_15%,transparent)] hover:bg-[color-mix(in_srgb,var(--danger)_25%,transparent)] text-[var(--danger)] rounded text-xs"
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
            <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-5 space-y-5">
              <div className="flex items-center justify-between border-b border-[var(--border-subtle)] pb-3">
                <h2 className="text-lg font-bold text-[var(--text-bright)] flex items-center gap-2">
                  <span>{selectedWorkflow.name}</span>
                  <span className="text-xs px-2 py-0.5 bg-[var(--accent-muted)] text-[var(--accent)] rounded-full font-mono">
                    {selectedWorkflow.id}
                  </span>
                </h2>
                <div className="flex gap-2">
                  <button
                    onClick={() => handleAddActionNode('action_cloudflare', 'Check Cloudflare')}
                    className="px-2.5 py-1 bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-xs font-semibold text-[var(--accent)] rounded border border-[var(--border-subtle)]"
                  >
                    + Cloudflare Node
                  </button>
                  <button
                    onClick={() => handleAddActionNode('action_gmail', 'Send Gmail')}
                    className="px-2.5 py-1 bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-xs font-semibold text-[var(--accent)] rounded border border-[var(--border-subtle)]"
                  >
                    + Gmail Node
                  </button>
                </div>
              </div>

              {/* Node Visual Flow Diagram */}
              <div className="space-y-2">
                <span className="text-xs font-bold text-[var(--text-dim)] uppercase tracking-wider">Interactive Node Flow (Click Node to Edit Parameters)</span>
                <div className="flex flex-wrap items-center gap-3 bg-[var(--bg-panel)] p-5 rounded-xl border border-[var(--border-subtle)]">
                  {selectedWorkflow.nodes.map((node, idx) => (
                    <React.Fragment key={node.id}>
                      <div
                        onClick={() => setSelectedNode(node)}
                        className={`px-4 py-3 rounded-xl border cursor-pointer transition flex flex-col gap-1 min-w-[150px] ${
                          selectedNode?.id === node.id
                            ? 'border-[var(--accent)] bg-[var(--accent-muted)] shadow-[0_0_15px_var(--accent-muted)]'
                            : 'border-[var(--border-subtle)] bg-[var(--bg-surface)] hover:border-[var(--border-active)]'
                        }`}
                      >
                        <span className="text-[10px] font-mono text-[var(--accent)] uppercase tracking-wider">{node.type}</span>
                        <span className="text-sm font-bold text-[var(--text-bright)]">{node.name}</span>
                        <span className="text-[10px] text-[var(--text-dim)] font-mono">ID: {node.id}</span>
                      </div>
                      {idx < selectedWorkflow.nodes.length - 1 && (
                        <span className="text-[var(--text-ghost)] font-bold text-xl">➔</span>
                      )}
                    </React.Fragment>
                  ))}
                </div>
              </div>

              {/* Selected Node Parameter Inspector */}
              {selectedNode && (
                <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-4 space-y-3">
                  <h3 className="text-xs font-bold text-[var(--accent)] uppercase tracking-wider border-b border-[var(--border-subtle)] pb-2">
                    Node Inspector Parameters — {selectedNode.name} ({selectedNode.id})
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    {Object.entries(selectedNode.parameters).map(([paramKey, paramVal]) => (
                      <div key={paramKey}>
                        <label className="text-[10px] font-mono uppercase text-[var(--text-dim)] block mb-1">{paramKey}</label>
                        <input
                          type="text"
                          value={String(paramVal)}
                          onChange={(e) => handleUpdateNodeParameter(paramKey, e.target.value)}
                          className="w-full px-3 py-1.5 bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded text-xs text-[var(--text-main)] focus:outline-none focus:border-[var(--accent)]"
                        />
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Execution Logs Output */}
              {executionLogs.length > 0 && (
                <div className="space-y-2 border-t border-[var(--border-subtle)] pt-4">
                  <h3 className="text-xs font-bold text-[var(--accent)] uppercase tracking-wider">Execution Pipeline Output Logs</h3>
                  <div className="bg-[var(--bg-void)] p-4 rounded-xl font-mono text-xs text-[var(--text-main)] space-y-3 max-h-64 overflow-y-auto border border-[var(--border-subtle)]">
                    {executionLogs.map((log, i) => (
                      <div key={i} className="border-b border-[var(--border-subtle)] pb-2">
                        <div className="flex items-center gap-2">
                          <span className="text-[var(--accent)]">[{log.type}]</span>
                          <span className="text-[var(--text-bright)] font-bold">{log.name}</span>
                          <span className="text-[var(--accent)] font-bold uppercase text-[10px]">{log.status}</span>
                        </div>
                        <pre className="text-[var(--text-dim)] mt-1.5 whitespace-pre-wrap">{JSON.stringify(log.output, null, 2)}</pre>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl p-12 text-center text-[var(--text-ghost)]">
              Select or generate a workflow to view and edit interactive node pipeline graphs.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default WorkflowBuilder;
