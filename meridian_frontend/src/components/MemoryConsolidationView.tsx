import React, { useState, useEffect } from 'react';
import { Database, Brain, Sparkles, FileText, Tag, CheckCircle, RefreshCw } from 'lucide-react';
import { API_BASE_URL } from '../config';

interface MemoryNode {
  id: string;
  category: string;
  content: string;
  confidence: number;
  tags: string[];
}

interface ConsolidationStatus {
  total_consolidation_runs: number;
  total_nodes_extracted: number;
  total_messages_processed: number;
  latest_summary: string;
}

export const MemoryConsolidationView: React.FC = () => {
  const [status, setStatus] = useState<ConsolidationStatus | null>(null);
  const [sampleMessages, setSampleMessages] = useState<string>(
    'User: I prefer dark theme for UI dashboards.\nAssistant: Settings saved.\nUser: We decided to use Q4_K_M quantization for speed.'
  );
  const [extractedNodes, setExtractedNodes] = useState<MemoryNode[]>([]);
  const [summary, setSummary] = useState<string>('');
  const [loading, setLoading] = useState<boolean>(false);

  useEffect(() => {
    fetchStatus();
  }, []);

  const fetchStatus = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/memory/consolidation-status`);
      if (res.ok) {
        const data = await res.json();
        setStatus(data);
      }
    } catch (e) {
      console.error(e);
    }
  };

  const handleConsolidate = async () => {
    setLoading(true);
    const parsedMessages = sampleMessages.split('\n').filter(Boolean).map(line => {
      const parts = line.split(':');
      return {
        role: parts[0]?.toLowerCase().includes('user') ? 'user' : 'assistant',
        content: parts.slice(1).join(':').trim() || line
      };
    });

    try {
      const res = await fetch(`${API_BASE_URL}/api/memory/consolidate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ session_id: 'active_session', messages: parsedMessages })
      });

      if (res.ok) {
        const data = await res.json();
        setSummary(data.summary);
        setExtractedNodes(data.extracted_nodes || []);
        fetchStatus();
      }
    } catch (e) {
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-6 text-[var(--text-bright)]">
      {/* Header */}
      <div className="flex items-center justify-between p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl backdrop-blur-md">
        <div className="flex items-center gap-3">
          <div className="p-2.5 bg-[var(--accent-muted)] border border-[var(--border-active)] rounded-lg">
            <Brain className="w-6 h-6 text-[var(--accent-2)]" />
          </div>
          <div>
            <h2 className="text-lg font-bold text-[var(--text-bright)]">Conversation Summarization & Memory Consolidation</h2>
            <p className="text-xs text-[var(--text-dim)]">Extract semantic user facts, decisions, and consolidate long-term memory nodes</p>
          </div>
        </div>
        <button
          onClick={fetchStatus}
          className="flex items-center gap-2 px-3 py-1.5 text-xs bg-[var(--bg-surface)] hover:bg-[var(--bg-hover)] text-[var(--text-main)] border border-[var(--border-subtle)] rounded-lg transition"
        >
          <RefreshCw className="w-3.5 h-3.5" /> Refresh Status
        </button>
      </div>

      {/* Metrics Row */}
      {status && (
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div className="p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl">
            <span className="text-xs text-[var(--text-dim)] block">Total Runs</span>
            <span className="text-xl font-bold font-mono text-[var(--accent)]">{status.total_consolidation_runs}</span>
          </div>
          <div className="p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl">
            <span className="text-xs text-[var(--text-dim)] block">Extracted Memory Nodes</span>
            <span className="text-xl font-bold font-mono text-[var(--accent-2)]">{status.total_nodes_extracted}</span>
          </div>
          <div className="p-4 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl">
            <span className="text-xs text-[var(--text-dim)] block">Messages Processed</span>
            <span className="text-xl font-bold font-mono text-[var(--success)]">{status.total_messages_processed}</span>
          </div>
        </div>
      )}

      {/* Interactive Consolidation Test Panel */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Input */}
        <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--accent-2)]">
            <FileText className="w-4 h-4" /> Conversation Input
          </h3>
          <textarea
            rows={8}
            value={sampleMessages}
            onChange={(e) => setSampleMessages(e.target.value)}
            className="w-full bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg p-3 text-xs font-mono text-[var(--text-main)] outline-none focus:border-[var(--accent)]"
          />
          <button
            onClick={handleConsolidate}
            disabled={loading}
            className="w-full py-2.5 bg-[var(--accent)] hover:bg-[var(--accent-dim)] text-[var(--bg-void)] text-xs font-semibold rounded-lg shadow-lg transition flex items-center justify-center gap-2"
          >
            <Sparkles className="w-4 h-4" />
            {loading ? 'Consolidating Memory Nodes...' : 'Summarize & Consolidate Memory'}
          </button>
        </div>

        {/* Results */}
        <div className="p-5 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-xl space-y-4">
          <h3 className="text-sm font-semibold flex items-center gap-2 text-[var(--success)]">
            <Database className="w-4 h-4" /> Extracted Memory Graph Nodes
          </h3>

          {summary && (
            <div className="p-3 bg-[var(--bg-surface)] border border-[var(--border-active)] rounded-lg text-xs space-y-1">
              <span className="font-semibold text-[var(--accent-2)]">Generated Summary:</span>
              <p className="text-[var(--text-main)]">{summary}</p>
            </div>
          )}

          {extractedNodes.length === 0 ? (
            <div className="p-6 text-center text-xs text-[var(--text-ghost)] border border-dashed border-[var(--border-subtle)] rounded-xl">
              No memory nodes extracted yet. Click Summarize & Consolidate above.
            </div>
          ) : (
            <div className="space-y-2 max-h-72 overflow-y-auto pr-1">
              {extractedNodes.map((node) => (
                <div key={node.id} className="p-3 bg-[var(--bg-panel)] border border-[var(--border-subtle)] rounded-lg space-y-1">
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-mono text-[var(--accent)] capitalize">{node.category}</span>
                    <span className="text-[10px] text-[var(--text-dim)]">Confidence: {(node.confidence * 100).toFixed(0)}%</span>
                  </div>
                  <p className="text-xs text-[var(--text-main)]">{node.content}</p>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
