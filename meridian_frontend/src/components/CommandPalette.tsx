import React, { useState, useEffect } from 'react';
import { Search, Command, Mic, Shield, Terminal, Zap, X, FileCode, GitBranch, BookOpen, Cpu, Brain, Activity, Wrench } from 'lucide-react';

interface CommandPaletteProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectAction?: (actionId: string) => void;
}

export const CommandPalette: React.FC<CommandPaletteProps> = ({ isOpen, onClose, onSelectAction }) => {
  const [query, setQuery] = useState('');
  const [selectedIndex, setSelectedIndex] = useState(0);

  const actions = [
    { id: 'local_model_mgr', label: 'Local LLM & Quantization Manager (Q4_K_M / Q8_0)', icon: Cpu, category: 'Local AI' },
    { id: 'memory_consolidate', label: 'Summarize & Consolidate Conversation Memory Graph', icon: Brain, category: 'Memory' },
    { id: 'dev_automation', label: 'Run Developer Automation (Git, Pytest, Format)', icon: Wrench, category: 'Dev Tools' },
    { id: 'agent_stream', label: 'Real-Time Agent Status & Activity Stream', icon: Activity, category: 'Telemetry' },
    { id: 'voice_toggle', label: 'Toggle Voice Assistant', icon: Mic, category: 'Audio' },
    { id: 'vault_keys', label: 'Open Secret Vault Settings', icon: Shield, category: 'Security' },
    { id: 'run_swarm', label: 'Run Multi-Agent Swarm Audit', icon: Zap, category: 'AI Tools' },
    { id: 'open_terminal', label: 'Open Shell Diagnostics', icon: Terminal, category: 'System' },
    { id: 'codegraph_search', label: 'Search Codebase AST Symbols & Impact', icon: FileCode, category: 'CodeGraph' },
    { id: 'papercoder_gen', label: 'Generate Codebase from arXiv Paper / PDF (PaperCoder)', icon: BookOpen, category: 'PaperCoder' },
    { id: 'neural_rag_intent', label: 'Query Subconscious Intent Knowledge Graph', icon: GitBranch, category: 'Neural RAG' },
  ];

  const filteredActions = actions.filter((a) =>
    a.label.toLowerCase().includes(query.toLowerCase()) ||
    a.category.toLowerCase().includes(query.toLowerCase())
  );

  useEffect(() => {
    setSelectedIndex(0);
  }, [query]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (!isOpen) return;

      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        onClose();
      } else if (e.key === 'Escape') {
        onClose();
      } else if (e.key === 'ArrowDown') {
        e.preventDefault();
        setSelectedIndex((prev) => (prev + 1) % Math.max(1, filteredActions.length));
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        setSelectedIndex((prev) => (prev - 1 + filteredActions.length) % Math.max(1, filteredActions.length));
      } else if (e.key === 'Enter') {
        e.preventDefault();
        if (filteredActions[selectedIndex]) {
          onSelectAction?.(filteredActions[selectedIndex].id);
          onClose();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose, filteredActions, selectedIndex, onSelectAction]);

  const renderHighlightedText = (text: string, search: string) => {
    if (!search.trim()) return text;
    const regex = new RegExp(`(${search.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    const parts = text.split(regex);
    return parts.map((part, i) =>
      regex.test(part) ? (
        <mark
          key={i}
          className="font-bold px-0.5 rounded border"
          style={{ background: 'var(--accent-muted)', color: 'var(--accent)', borderColor: 'var(--border-active)' }}
        >
          {part}
        </mark>
      ) : (
        part
      )
    );
  };

  if (!isOpen) return null;

  const kbdStyle: React.CSSProperties = {
    padding: '2px 6px',
    background: 'var(--bg-surface)',
    borderRadius: 4,
    border: '1px solid var(--border-subtle)',
    fontSize: 10,
  };

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 backdrop-blur-md animate-fade-in" style={{ background: 'color-mix(in srgb, var(--bg-void) 70%, transparent)' }}>
      <div
        className="w-full max-w-xl rounded-2xl shadow-2xl overflow-hidden backdrop-blur-xl"
        style={{ background: 'var(--bg-float)', border: '1px solid var(--border-active)' }}
      >
        {/* Search Header */}
        <div className="flex items-center px-4 py-3.5" style={{ borderBottom: '1px solid var(--border-subtle)', background: 'var(--bg-panel)' }}>
          <Search className="w-5 h-5 mr-3 animate-pulse" style={{ color: 'var(--accent)' }} />
          <input
            type="text"
            className="w-full bg-transparent outline-none text-sm font-medium"
            style={{ color: 'var(--text-bright)' }}
            placeholder="Search commands (Press ↑/↓ to navigate, Enter to select)..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            autoFocus
          />
          <button onClick={onClose} className="p-1 transition" style={{ color: 'var(--text-dim)' }}>
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Action Items List */}
        <div className="max-h-80 overflow-y-auto p-2 space-y-1">
          {filteredActions.length === 0 ? (
            <div className="p-6 text-center text-xs" style={{ color: 'var(--text-ghost)', fontFamily: 'var(--font-main)' }}>
              No matching commands found.
            </div>
          ) : (
            filteredActions.map((action, idx) => {
              const Icon = action.icon;
              const isSelected = idx === selectedIndex;
              return (
                <button
                  key={action.id}
                  onClick={() => {
                    onSelectAction?.(action.id);
                    onClose();
                  }}
                  onMouseEnter={() => setSelectedIndex(idx)}
                  className="w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-left transition-all"
                  style={isSelected
                    ? { background: 'var(--accent-muted)', border: '1px solid var(--border-active)', color: 'var(--text-bright)' }
                    : { border: '1px solid transparent', color: 'var(--text-main)' }}
                >
                  <div className="flex items-center space-x-3">
                    <div
                      className="p-2 rounded-lg transition"
                      style={isSelected
                        ? { background: 'var(--accent-muted)', color: 'var(--accent)' }
                        : { background: 'var(--bg-surface)', color: 'var(--text-dim)' }}
                    >
                      <Icon className="w-4 h-4" />
                    </div>
                    <span className="text-sm font-medium" style={{ color: isSelected ? 'var(--text-bright)' : 'var(--text-main)' }}>
                      {renderHighlightedText(action.label, query)}
                    </span>
                  </div>
                  <span
                    className="text-xs px-2.5 py-0.5 rounded-full text-[10px] border"
                    style={{
                      fontFamily: 'var(--font-main)',
                      background: isSelected ? 'var(--accent-muted)' : 'var(--bg-surface)',
                      color: isSelected ? 'var(--accent)' : 'var(--text-dim)',
                      borderColor: isSelected ? 'var(--border-active)' : 'var(--border-subtle)',
                    }}
                  >
                    {renderHighlightedText(action.category, query)}
                  </span>
                </button>
              );
            })
          )}
        </div>

        {/* Keyboard Hints Footer */}
        <div
          className="px-4 py-2 flex items-center justify-between text-[11px]"
          style={{ background: 'var(--bg-panel)', borderTop: '1px solid var(--border-subtle)', color: 'var(--text-dim)', fontFamily: 'var(--font-main)' }}
        >
          <div className="flex items-center gap-3">
            <span><kbd style={kbdStyle}>↑</kbd> <kbd style={kbdStyle}>↓</kbd> Navigate</span>
            <span><kbd style={kbdStyle}>↵</kbd> Select</span>
          </div>
          <span><kbd style={kbdStyle}>Esc</kbd> Close</span>
        </div>
      </div>
    </div>
  );
};
