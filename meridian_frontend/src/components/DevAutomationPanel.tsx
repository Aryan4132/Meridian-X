import React, { useState, useEffect } from 'react';
import { Terminal, GitBranch, Play, CheckCircle2, XCircle, Clock, Code, Wrench, RefreshCw } from 'lucide-react';

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
      const res = await fetch('/api/automation/git/status');
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
      const res = await fetch('/api/automation/code/format', {
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
      const res = await fetch('/api/automation/test/run', {
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
      const res = await fetch('/api/automation/build/project', {
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
    <div className="space-y-6 text-slate-100">
      {/* Header */}
      <div className="flex items-center justify-between p-4 bg-slate-900/80 border border-slate-800 rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-emerald-500/10 border border-emerald-500/30 rounded-lg">
            <Wrench className="w-6 h-6 text-emerald-400" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-slate-100">Developer Automation Endpoints</h2>
            <p className="text-xs text-slate-400">One-click automation for git status, formatting, testing, and building</p>
          </div>
        </div>
        <button
          onClick={fetchGitStatus}
          className="flex items-center gap-2 px-3 py-1.5 text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 rounded-lg transition"
        >
          <RefreshCw className="w-3.5 h-3.5" /> Refresh Git
        </button>
      </div>

      {/* Main Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Git Status Card */}
        <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-cyan-400">
            <GitBranch className="w-4 h-4" /> Git Repository Status
          </h3>
          {gitStatus ? (
            <div className="space-y-3">
              <div className="p-3 bg-slate-950/80 border border-slate-800 rounded-lg text-xs space-y-1">
                <div className="flex justify-between">
                  <span className="text-slate-400">Branch:</span>
                  <span className="font-mono text-cyan-300 font-bold">{gitStatus.branch}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Modified Files:</span>
                  <span className="font-mono text-amber-400 font-bold">{gitStatus.modified_count}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Untracked Files:</span>
                  <span className="font-mono text-slate-400 font-bold">{gitStatus.untracked_count}</span>
                </div>
              </div>

              {gitStatus.modified_files.length > 0 && (
                <div className="space-y-1">
                  <span className="text-[11px] text-slate-400 font-medium">Changed files:</span>
                  <div className="max-h-40 overflow-y-auto space-y-1">
                    {gitStatus.modified_files.map((f, idx) => (
                      <div key={idx} className="text-[11px] font-mono p-1.5 bg-slate-950/40 rounded border border-slate-800/50 flex items-center justify-between">
                        <span className="text-slate-300 truncate max-w-[180px]">{f.file}</span>
                        <span className="text-[10px] px-1.5 bg-slate-800 text-cyan-400 rounded">{f.status}</span>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <span className="text-xs text-slate-500">Loading git status...</span>
          )}
        </div>

        {/* Task Trigger Buttons */}
        <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-emerald-400">
            <Play className="w-4 h-4" /> Quick Automation Tasks
          </h3>
          <div className="space-y-3">
            <button
              onClick={handleFormatCode}
              disabled={!!runningAction}
              className="w-full p-3 bg-slate-950/80 hover:bg-slate-800 border border-slate-800 rounded-xl text-xs flex items-center justify-between text-slate-200 transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Code className="w-4 h-4 text-cyan-400" /> Format Codebase
              </span>
              <span className="text-[10px] text-slate-400">Black / Prettier</span>
            </button>

            <button
              onClick={handleRunTests}
              disabled={!!runningAction}
              className="w-full p-3 bg-slate-950/80 hover:bg-slate-800 border border-slate-800 rounded-xl text-xs flex items-center justify-between text-slate-200 transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Terminal className="w-4 h-4 text-emerald-400" /> Run Pytest Suite
              </span>
              <span className="text-[10px] text-slate-400">Pytest</span>
            </button>

            <button
              onClick={handleBuildProject}
              disabled={!!runningAction}
              className="w-full p-3 bg-slate-950/80 hover:bg-slate-800 border border-slate-800 rounded-xl text-xs flex items-center justify-between text-slate-200 transition"
            >
              <span className="flex items-center gap-2 font-medium">
                <Wrench className="w-4 h-4 text-purple-400" /> Verify Project Build
              </span>
              <span className="text-[10px] text-slate-400">Backend / Frontend</span>
            </button>

            {runningAction && (
              <div className="p-3 bg-emerald-950/20 border border-emerald-500/30 rounded-lg text-xs text-emerald-300 flex items-center gap-2 animate-pulse">
                <RefreshCw className="w-3.5 h-3.5 animate-spin" />
                {runningAction}
              </div>
            )}
          </div>
        </div>

        {/* Task Output Console */}
        <div className="p-5 bg-slate-900/60 border border-slate-800 rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-purple-400">
            <Terminal className="w-4 h-4" /> Execution Console
          </h3>

          {actionOutput ? (
            <div className="space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-slate-200">{actionOutput.title}</span>
                <span className={`inline-flex items-center gap-1 font-mono text-[10px] px-2 py-0.5 rounded-full ${
                  actionOutput.success ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30' : 'bg-rose-500/10 text-rose-400 border border-rose-500/30'
                }`}>
                  {actionOutput.success ? <CheckCircle2 className="w-3 h-3" /> : <XCircle className="w-3 h-3" />}
                  {actionOutput.success ? 'Success' : 'Failed'}
                </span>
              </div>
              <pre className="p-3 bg-slate-950 border border-slate-800 rounded-lg text-[11px] font-mono text-slate-300 max-h-56 overflow-y-auto whitespace-pre-wrap">
                {actionOutput.stdout || actionOutput.stderr || 'Command executed cleanly.'}
              </pre>
            </div>
          ) : (
            <div className="p-6 text-center text-xs text-slate-500 border border-dashed border-slate-800 rounded-xl">
              No task output available. Trigger a quick automation task above.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
