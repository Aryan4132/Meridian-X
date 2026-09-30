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
        <mark key={i} className="bg-cyan-500/30 text-cyan-200 font-bold px-0.5 rounded border border-cyan-500/40">
          {part}
        </mark>
      ) : (
        part
      )
    );
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 bg-black/70 backdrop-blur-md animate-fade-in">
      <div className="w-full max-w-xl bg-slate-900/90 border border-cyan-500/40 rounded-2xl shadow-2xl shadow-cyan-500/20 overflow-hidden backdrop-blur-xl">
        {/* Search Header */}
        <div className="flex items-center px-4 py-3.5 border-b border-slate-800/80 bg-slate-950/40">
          <Search className="w-5 h-5 text-cyan-400 mr-3 animate-pulse" />
          <input
            type="text"
            className="w-full bg-transparent text-slate-100 placeholder-slate-500 outline-none text-sm font-medium"
            placeholder="Search commands (Press ↑/↓ to navigate, Enter to select)..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            autoFocus
          />
          <button onClick={onClose} className="p-1 text-slate-400 hover:text-slate-200 transition">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Action Items List */}
        <div className="max-h-80 overflow-y-auto p-2 space-y-1">
          {filteredActions.length === 0 ? (
            <div className="p-6 text-center text-xs text-slate-500 font-mono">
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
                  className={`w-full flex items-center justify-between px-3.5 py-2.5 rounded-xl text-left transition-all ${
                    isSelected
                      ? 'bg-gradient-to-r from-cyan-500/20 to-blue-500/10 border border-cyan-500/40 shadow-lg shadow-cyan-500/10 text-white'
                      : 'hover:bg-slate-800/50 text-slate-300 border border-transparent'
                  }`}
                >
                  <div className="flex items-center space-x-3">
                    <div className={`p-2 rounded-lg transition ${
                      isSelected ? 'bg-cyan-500/30 text-cyan-300' : 'bg-slate-800 text-slate-400'
                    }`}>
                      <Icon className="w-4 h-4" />
                    </div>
                    <span className={`text-sm font-medium ${isSelected ? 'text-cyan-200' : 'text-slate-200'}`}>
                      {renderHighlightedText(action.label, query)}
                    </span>
                  </div>
                  <span className={`text-xs px-2.5 py-0.5 rounded-full font-mono text-[10px] border ${
                    isSelected ? 'bg-cyan-500/20 text-cyan-300 border-cyan-500/40' : 'bg-slate-800 text-slate-500 border-slate-700/60'
                  }`}>
                    {renderHighlightedText(action.category, query)}
                  </span>
                </button>
              );
            })
          )}
        </div>

        {/* Keyboard Hints Footer */}
        <div className="px-4 py-2 bg-slate-950/60 border-t border-slate-800/80 flex items-center justify-between text-[11px] text-slate-400 font-mono">
          <div className="flex items-center gap-3">
            <span><kbd className="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px]">↑</kbd> <kbd className="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px]">↓</kbd> Navigate</span>
            <span><kbd className="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px]">↵</kbd> Select</span>
          </div>
          <span><kbd className="px-1.5 py-0.5 bg-slate-800 rounded border border-slate-700 text-[10px]">Esc</kbd> Close</span>
        </div>
      </div>
    </div>
  );
};
