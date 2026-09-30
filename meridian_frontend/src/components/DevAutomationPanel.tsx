import React, { useState, useEffect } from 'react';
import { Terminal, GitBranch, Play, CheckCircle2, XCircle, Clock, Code, Wrench, RefreshCw } from 'lucide-react';
import { API_BASE_URL } from '../config';

interface GitStatus {
  is_git_repo: boolean;
  branch: string;
  modified_count: number;
  untracked_count: number;
  modified_files: { status: string; file: string }[];
}

export const DevAutomationPanel: React.FC = () => {
  const [gitStatus, setGitStatus] = useState<GitStatus | null>(null);
  const [runningAction, setRunningAction] = useState<string | null>(null);
  const [actionOutput, setActionOutput] = useState<{ title: string; success: boolean; stdout: string; stderr: string; duration: number } | null>(null);

  useEffect(() => {
    fetchGitStatus();
  }, []);

  const fetchGitStatus = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/automation/git/status`);
      if (res.ok) {
        const data = await res.json();
        setGitStatus(data);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleFormatCode = async () => {
    setRunningAction('Formatting Code...');
    try {
      const res = await fetch(`${API_BASE_URL}/api/automation/code/format`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ formatter: 'auto' })
      });
      if (res.ok) {
        const data = await res.json();
        setActionOutput({
          title: 'Code Formatting',
          success: data.success,
          stdout: data.stdout,
          stderr: data.stderr,
          duration: data.duration_seconds || 0
        });
      }
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAction(null);
    }
  };

  const handleRunTests = async () => {
    setRunningAction('Running Tests...');
    try {
      const res = await fetch(`${API_BASE_URL}/api/automation/test/run`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ grep_filter: 'test_new_features' })
      });
      if (res.ok) {
        const data = await res.json();
        setActionOutput({
          title: 'Pytest Suite Run',
          success: data.success,
          stdout: data.stdout,
          stderr: data.stderr,
          duration: data.duration_seconds || 0
        });
      }
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAction(null);
    }
  };

  const handleBuildProject = async () => {
    setRunningAction('Building Project...');
    try {
      const res = await fetch(`${API_BASE_URL}/api/automation/build/project`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ target: 'backend' })
      });
      if (res.ok) {
        const data = await res.json();
        setActionOutput({
          title: 'Project Build',
          success: data.success,
          stdout: JSON.stringify(data.details, null, 2),
          stderr: '',
          duration: 0
        });
      }
    } catch (e) {
      console.error(e);
    } finally {
      setRunningAction(null);
    }
  };

  return (
    <div className="space-y-6 text-[var(--text-bright)]">
      {/* Header */}
      <div className="flex items-center justify-between p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-[color-mix(in_srgb,var(--success)_12%,transparent)] border border-[var(--success)] rounded-lg">
            <Wrench className="w-6 h-6 text-[var(--success)]" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-[var(--text-bright)]">Developer Automation Endpoints</h2>
            <p className="text-xs text-[var(--text-dim)]">One-click automation for git status, formatting, testing, and building</p>
          </div>
        </div>
        <button
          onClick={fetchGitStatus}
          className="flex items-center gap-2 px-3 py-1.5 text-xs bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-[var(--text-main)] border border-[var(--border-subtle)] rounded-lg transition"
        >
          <RefreshCw className="w-3.5 h-3.5" /> Refresh Git
        </button>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Git Status Card */}
        <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--accent)]">
            <GitBranch className="w-4 h-4" /> Git Repository Status
          </h3>
          {gitStatus ? (
            <div className="space-y-3">
              <div className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg text-xs space-y-1">
                <div className="flex justify-between">
                  <span className="text-[var(--text-dim)]">Branch:</span>
                  <span className="font-mono text-[var(--accent)] font-bold">{gitStatus.branch}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-[var(--text-dim)]">Modified Files:</span>
                  <span className="font-mono text-[var(--warning)] font-bold">{gitStatus.modified_count}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-[var(--text-dim)]">Untracked Files:</span>
                  <span className="font-mono text-[var(--text-dim)] font-bold">{gitStatus.untracked_count}</span>
                </div>
              </div>

              {gitStatus.modified_files.length > 0 && (
                <div className="space-y-1">
                  <span className="text-[11px] text-[var(--text-dim)] font-medium">Changed files:</span>
                  <div className="max-h-40 overflow-y-auto space-y-1">
                    {gitStatus.modified_files.map((f, idx) => (
                      <div key={idx} className="text-[11px] font-mono p-1.5 bg-[var(--bg-panel)] rounded border border-[var(--border-subtle)] flex items-center justify-between">
                        <span className="text-[var(--text-main)] truncate max-w-[180px]">{f.file}</span>
                        <span className="text-[10px] px-1.5 bg-[var(--bg-surface)] text-[var(--accent)] rounded">{f.status}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <span className="text-xs text-[var(--text-ghost)]">Loading git status...</span>
          )}
        </div>

        {/* Task Trigger Buttons */}
        <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--success)]">
            <Play className="w-4 h-4" /> Quick Automation Tasks
          </h3>
          <div className="space-y-3">
            <button
              onClick={handleFormatCode}
              disabled={!!runningAction}
              className="w-full p-3 bg-[var(--bg-panel)] hover:bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded-xl text-xs flex items-center justify-between text-[var(--text-main)] transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Code className="w-4 h-4 text-[var(--accent)]" /> Format Codebase
              </span>
              <span className="text-[10px] text-[var(--text-dim)]">Black / Prettier</span>
            </button>

            <button
              onClick={handleRunTests}
              disabled={!!runningAction}
              className="w-full p-3 bg-[var(--bg-panel)] hover:bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded-xl text-xs flex items-center justify-between text-[var(--text-main)] transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Terminal className="w-4 h-4 text-[var(--success)]" /> Run Pytest Suite
              </span>
              <span className="text-[10px] text-[var(--text-dim)]">Pytest</span>
            </button>

            <button
              onClick={handleBuildProject}
              disabled={!!runningAction}
              className="w-full p-3 bg-[var(--bg-panel)] hover:bg-[var(--bg-surface)] border border-[var(--border-subtle)] rounded-xl text-xs flex items-center justify-between text-[var(--text-main)] transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Wrench className="w-4 h-4 text-[var(--accent-2)]" /> Verify Project Build
              </span>
              <span className="text-[10px] text-[var(--text-dim)]">Backend / Frontend</span>
            </button>

            {runningAction && (
              <div className="p-3 bg-[color-mix(in_srgb,var(--success)_12%,transparent)] border border-[var(--success)] rounded-lg text-xs text-[var(--success)] flex items-center gap-2 animate-pulse">
                <RefreshCw className="w-3.5 h-3.5 animate-spin" />
                {runningAction}
              </div>
            )}
          </div>
        </div>

        {/* Task Output Console */}
        <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--accent-2)]">
            <Terminal className="w-4 h-4" /> Execution Console
          </h3>

          {actionOutput ? (
            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-[var(--text-main)]">{actionOutput.title}</span>
                <span className={`inline-flex items-center gap-1 font-mono text-[10px] px-2 py-0.5 rounded-full ${
                  actionOutput.success ? 'bg-[color-mix(in_srgb,var(--success)_12%,transparent)] text-[var(--success)] border border-[var(--success)]' : 'bg-[color-mix(in_srgb,var(--danger)_12%,transparent)] text-[var(--danger)] border border-[var(--danger)]'
                }`}>
                  {actionOutput.success ? <CheckCircle2 className="w-3 h-3" /> : <XCircle className="w-3 h-3" />}
                  {actionOutput.success ? 'Success' : 'Failed'}
                </span>
              </div>
              <pre className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg text-[11px] font-mono text-[var(--text-main)] max-h-56 overflow-y-auto whitespace-pre-wrap">
                {actionOutput.stdout || actionOutput.stderr || 'Command executed cleanly.'}
              </pre>
            </div>
          ) : (
            <div className="p-6 text-center text-xs text-[var(--text-ghost)] border border-dashed border-[var(--border-subtle)] rounded-xl">
              No task output available. Trigger a quick automation task above.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
