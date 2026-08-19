import React, { useState, useEffect } from 'react';
import { Search, Command, Mic, Shield, Terminal, Zap, X, FileCode, GitBranch, BookOpen } from 'lucide-react';

interface CommandPaletteProps {
  isOpen: boolean;
  onClose: () => void;
  onSelectAction?: (actionId: string) => void;
}

export const CommandPalette: React.FC<CommandPaletteProps> = ({ isOpen, onClose, onSelectAction }) => {
  const [query, setQuery] = useState('');

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') {
        e.preventDefault();
        if (isOpen) onClose();
      }
      if (e.key === 'Escape' && isOpen) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, onClose]);

  if (!isOpen) return null;

  const actions = [
    { id: 'voice_toggle', label: 'Toggle Voice Assistant', icon: Mic, category: 'Audio' },
    { id: 'vault_keys', label: 'Open Secret Vault Settings', icon: Shield, category: 'Security' },
    { id: 'run_swarm', label: 'Run Multi-Agent Swarm Audit', icon: Zap, category: 'AI Tools' },
    { id: 'open_terminal', label: 'Open Shell Diagnostics', icon: Terminal, category: 'System' },
    { id: 'codegraph_search', label: 'Search Codebase AST Symbols & Impact', icon: FileCode, category: 'CodeGraph' },
    { id: 'papercoder_gen', label: 'Generate Codebase from arXiv Paper / PDF (PaperCoder)', icon: BookOpen, category: 'PaperCoder' },
    { id: 'neural_rag_intent', label: 'Query Subconscious Intent Knowledge Graph', icon: GitBranch, category: 'Neural RAG' },
  ];


  const filteredActions = actions.filter((a) =>
    a.label.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <div className="fixed inset-0 z-50 flex items-start justify-center pt-20 bg-black/60 backdrop-blur-sm animate-fade-in">
      <div className="w-full max-w-xl bg-slate-900 border border-cyan-500/30 rounded-2xl shadow-2xl shadow-cyan-500/10 overflow-hidden">
        {/* Search Header */}
        <div className="flex items-center px-4 py-3 border-b border-slate-800">
          <Search className="w-5 h-5 text-cyan-400 mr-3" />
          <input
            type="text"
            className="w-full bg-transparent text-slate-100 placeholder-slate-500 outline-none text-sm"
            placeholder="Type a command or search actions... (Cmd+K)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            autoFocus
          />
          <button onClick={onClose} className="p-1 text-slate-400 hover:text-slate-200">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Action Items List */}
        <div className="max-h-80 overflow-y-auto p-2">
          {filteredActions.map((action) => {
            const Icon = action.icon;
            return (
              <button
                key={action.id}
                onClick={() => {
                  onSelectAction?.(action.id);
                  onClose();
                }}
                className="w-full flex items-center justify-between px-3 py-2.5 rounded-xl hover:bg-cyan-500/10 hover:border hover:border-cyan-500/20 text-left group transition-all"
              >
                <div className="flex items-center space-x-3">
                  <div className="p-2 rounded-lg bg-slate-800 group-hover:bg-cyan-500/20 text-cyan-400">
                    <Icon className="w-4 h-4" />
                  </div>
                  <span className="text-sm font-medium text-slate-200 group-hover:text-white">
                    {action.label}
                  </span>
                </div>
                <span className="text-xs text-slate-500 px-2 py-0.5 rounded-md bg-slate-800">
                  {action.category}
                </span>
              </button>
            );
          })}
        </div>
      </div>
    </div>
  );
};
