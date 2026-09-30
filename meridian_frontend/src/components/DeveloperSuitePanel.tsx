import React, { useState } from 'react';
import { Play, Sparkles, Terminal, ShieldAlert, Cpu, GitCommit, Search, Wand2, TestTube } from 'lucide-react';
import { API_BASE_URL } from '../config';

export default function DeveloperSuitePanel() {
  const [activeSubTab, setActiveSubTab] = useState<'orchestrator' | 'self_evolving' | 'explain' | 'experiment' | 'detective' | 'genie' | 'commit'>('orchestrator');
  const [loading, setLoading] = useState(false);
  const [output, setOutput] = useState<any>(null);

  // Form inputs
  const [preset, setPreset] = useState('coding');
  const [explainFile, setExplainFile] = useState('src/core/loop.py');
  const [explainLine, setExplainLine] = useState(1);
  const [expEndpoint, setExpEndpoint] = useState('/health');
  const [componentName, setComponentName] = useState('UserCard');
  const [updatedPackage, setUpdatedPackage] = useState('pydantic');

  const handleLaunchPreset = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/orchestrator/launch`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ preset })
      });
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  const handleExplainCode = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/explain/symbol`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ file_path: explainFile, line_number: Number(explainLine) })
      });
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  const handleRunExperiment = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/experiment/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ endpoint: expEndpoint, method: 'GET' })
      });
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  const handleDiagnoseBroke = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/detective/diagnose`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ updated_package: updatedPackage })
      });
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  const handleGenerateBoilerplate = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/boilerplate/generate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ component_name: componentName })
      });
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  const handleCommitWhisper = async () => {
    setLoading(true);
    try {
      const res = await fetch(`${API_BASE_URL}/api/commit-whisperer/inspect`);
      const data = await res.json();
      setOutput(data);
    } catch (e: any) {
      setOutput({ error: e.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="glass-card" style={{ padding: '20px', borderRadius: 'var(--radius-lg)', border: '1px solid var(--border-subtle)', background: 'var(--bg-panel)' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '16px' }}>
        <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
        <h2 style={{ fontSize: '18px', fontWeight: 700, color: 'var(--text-bright)', margin: 0, fontFamily: 'var(--font-heading)' }}>Proactive Developer Intelligence Suite</h2>
      </div>

      {/* Sub tabs navigation */}
      <div style={{ display: 'flex', flexWrap: 'wrap', gap: '8px', marginBottom: '20px' }}>
        <button
          onClick={() => { setActiveSubTab('orchestrator'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'orchestrator' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'orchestrator' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          ⚙️ Workspace Orchestration
        </button>
        <button
          onClick={() => { setActiveSubTab('explain'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'explain' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'explain' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          💡 Explain Like I'm Coding
        </button>
        <button
          onClick={() => { setActiveSubTab('experiment'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'experiment' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'experiment' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          🧪 One-Click Experiment
        </button>
        <button
          onClick={() => { setActiveSubTab('detective'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'detective' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'detective' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          🕵️‍♂️ 'What Just Broke?' Detective
        </button>
        <button
          onClick={() => { setActiveSubTab('genie'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'genie' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'genie' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          🧞‍♂️ Boilerplate Genie
        </button>
        <button
          onClick={() => { setActiveSubTab('commit'); setOutput(null); }}
          style={{ padding: '8px 14px', borderRadius: 'var(--radius-sm)', border: 'none', background: activeSubTab === 'commit' ? 'var(--accent)' : 'var(--bg-surface)', color: activeSubTab === 'commit' ? 'var(--bg-void)' : 'var(--text-bright)', fontWeight: 600, fontSize: '13px', cursor: 'pointer' }}
        >
          📜 Commit Whisperer
        </button>
      </div>

      {/* Main SubTab Contents */}
      <div style={{ background: 'var(--bg-void)', padding: '16px', borderRadius: 'var(--radius-md)', marginBottom: '16px', border: '1px solid var(--border-subtle)' }}>
        {activeSubTab === 'orchestrator' && (
          <div>
            <p style={{ color: 'var(--text-dim)', fontSize: '13px' }}>
              Simultaneously launches VS Code, MongoDB/Docker compose, documentation tabs, and Spotify Focus playlist.
            </p>
            <button onClick={handleLaunchPreset} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Launching Workspace...' : '🚀 Prepare Workspace for Coding'}
            </button>
          </div>
        )}

        {activeSubTab === 'explain' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <input value={explainFile} onChange={e => setExplainFile(e.target.value)} placeholder="File path" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }} />
            <input type="number" value={explainLine} onChange={e => setExplainLine(Number(e.target.value))} placeholder="Line number" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }} />
            <button onClick={handleExplainCode} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Analyzing Git History...' : '💡 Explain Code & Suggest Refactor'}
            </button>
          </div>
        )}

        {activeSubTab === 'experiment' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <input value={expEndpoint} onChange={e => setExpEndpoint(e.target.value)} placeholder="API Endpoint (e.g. /health)" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }} />
            <button onClick={handleRunExperiment} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Running Experiment...' : '🧪 Run Isolated API Experiment'}
            </button>
          </div>
        )}

        {activeSubTab === 'detective' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <input value={updatedPackage} onChange={e => setUpdatedPackage(e.target.value)} placeholder="Updated package name (e.g. pydantic)" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }} />
            <button onClick={handleDiagnoseBroke} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Tracing Signatures...' : '🕵️‍♂️ Diagnose What Just Broke'}
            </button>
          </div>
        )}

        {activeSubTab === 'genie' && (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
            <input value={componentName} onChange={e => setComponentName(e.target.value)} placeholder="Component Name (e.g. UserCard)" style={{ background: 'var(--bg-panel)', border: '1px solid var(--border-subtle)', color: 'var(--text-main)', padding: '8px 12px', borderRadius: 'var(--radius-sm)' }} />
            <button onClick={handleGenerateBoilerplate} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Extracting Patterns...' : '🧞‍♂️ Generate Component Stub & Skeleton'}
            </button>
          </div>
        )}

        {activeSubTab === 'commit' && (
          <div>
            <p style={{ color: 'var(--text-dim)', fontSize: '13px' }}>
              Verifies staged git status against semver rules and checks CHANGELOG updates before committing.
            </p>
            <button onClick={handleCommitWhisper} disabled={loading} style={{ background: 'var(--accent)', border: 'none', color: 'var(--bg-void)', padding: '10px 20px', borderRadius: 'var(--radius-sm)', fontWeight: 700, cursor: 'pointer' }}>
              {loading ? 'Inspecting Git Status...' : '📜 Inspect Staged Changes & Semver'}
            </button>
          </div>
        )}
      </div>

      {/* Results output area */}
      {output && (
        <div style={{ background: 'var(--bg-void)', borderRadius: 'var(--radius-sm)', padding: '12px', border: '1px solid var(--border-active)' }}>
          <div style={{ fontSize: '12px', color: 'var(--accent)', fontWeight: 700, marginBottom: '6px' }}>Result Output:</div>
          <pre style={{ color: 'var(--text-main)', fontSize: '12px', margin: 0, overflowX: 'auto', whiteSpace: 'pre-wrap' }}>
            {JSON.stringify(output, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}
