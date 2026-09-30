import React, { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { Search, Brain, Trash2, Edit3, Download, RefreshCw, Layers, Calendar, Sliders, Eye, EyeOff } from 'lucide-react';
import { API_BASE_URL } from '../config';

interface MemoryItem {
  id: string;
  type: string;
  category: string;
  key?: string;
  value?: any;
  entity_id?: string;
  state?: any;
  summary?: string;
  date?: string;
  timestamp?: number;
  created_at?: string;
  temporal_relevance?: number;
}

export default function MemoryEditor() {
  const [memories, setMemories] = useState<MemoryItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [categoryFilter, setCategoryFilter] = useState<string>('all');
  const [editingItem, setEditingItem] = useState<MemoryItem | null>(null);
  const [editValue, setEditValue] = useState<string>('');
  const [showKeys, setShowKeys] = useState(false);

  const fetchMemories = async () => {
    setLoading(true);
    try {
      let url = `${API_BASE_URL}/api/memory/list`;
      const params = new URLSearchParams();
      if (searchQuery) params.append('query', searchQuery);
      if (categoryFilter !== 'all') params.append('category', categoryFilter);
      if (params.toString()) url += `?${params.toString()}`;

      const res = await fetch(url);
      if (res.ok) {
        const data = await res.json();
        setMemories(data.memories || []);
      }
    } catch (e) {
      console.error('Failed fetching memories:', e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchMemories();
  }, [categoryFilter]);

  const handleSearchSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetchMemories();
  };

  const handleForgetEntity = async (entityId: string) => {
    if (!confirm(`Are you sure you want to forget and permanently delete memory for '${entityId}'?`)) return;
    try {
      const res = await fetch(`${API_BASE_URL}/api/memory/forget`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ entity_id: entityId }),
      });
      if (res.ok) {
        fetchMemories();
      }
    } catch (e) {
      console.error('Failed forgetting entity:', e);
    }
  };

  const handleSaveEdit = async () => {
    if (!editingItem) return;
    try {
      let parsedValue: any = editValue;
      try {
        parsedValue = JSON.parse(editValue);
      } catch {
        // Keep string if not valid JSON
      }

      const res = await fetch(`${API_BASE_URL}/api/memory/update`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: editingItem.id, new_value: parsedValue }),
      });
      if (res.ok) {
        setEditingItem(null);
        fetchMemories();
      }
    } catch (e) {
      console.error('Failed updating memory:', e);
    }
  };

  const handleExportJSON = async () => {
    try {
      const res = await fetch(`${API_BASE_URL}/api/memory/export`);
      if (res.ok) {
        const data = await res.json();
        const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `meridian_memory_export_${new Date().toISOString().split('T')[0]}.json`;
        a.click();
        URL.revokeObjectURL(url);
      }
    } catch (e) {
      console.error('Export failed:', e);
    }
  };

  return (
    <div style={{ flex: 1, padding: 24, display: 'flex', flexDirection: 'column', gap: 20, overflowY: 'auto' }}>
      {/* Top Header & Stats */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 16 }}>
        <div>
          <h1 style={{ fontSize: 24, fontWeight: 700, margin: 0, display: 'flex', alignItems: 'center', gap: 10, color: 'var(--text-main)' }}>
            <Brain style={{ color: 'var(--accent)' }} size={28} /> Memory Editor ("What do you remember?")
          </h1>
          <p style={{ margin: '4px 0 0', color: 'var(--text-dim)', fontSize: 14 }}>
            View, search, update, forget entities, or export Meridian-X memory graphs.
          </p>
        </div>

        <div style={{ display: 'flex', gap: 10 }}>
          <button
            onClick={() => setShowKeys(!showKeys)}
            style={{
              display: 'flex', alignItems: 'center', gap: 6, padding: '8px 14px', borderRadius: 8,
              background: 'rgba(255,255,255,0.06)', border: '1px solid var(--border-subtle)',
              color: 'var(--text-main)', cursor: 'pointer', fontSize: 13, fontWeight: 500
            }}
          >
            {showKeys ? <EyeOff size={14} /> : <Eye size={14} />} {showKeys ? 'Hide Values' : 'Show Values'}
          </button>

          <button
            onClick={fetchMemories}
            style={{
              display: 'flex', alignItems: 'center', gap: 6, padding: '8px 14px', borderRadius: 8,
              background: 'rgba(255,255,255,0.06)', border: '1px solid var(--border-subtle)',
              color: 'var(--text-main)', cursor: 'pointer', fontSize: 13, fontWeight: 500
            }}
          >
            <RefreshCw size={14} className={loading ? 'animate-spin' : ''} /> Refresh
          </button>

          <button
            onClick={handleExportJSON}
            style={{
              display: 'flex', alignItems: 'center', gap: 6, padding: '8px 14px', borderRadius: 8,
              background: 'var(--accent)', border: 'none', color: '#000', cursor: 'pointer',
              fontSize: 13, fontWeight: 600
            }}
          >
            <Download size={14} /> Export JSON
          </button>
        </div>
      </div>

      {/* Search & Category Filter Bar */}
      <div style={{ display: 'flex', gap: 12, flexWrap: 'wrap' }}>
        <form onSubmit={handleSearchSubmit} style={{ flex: 1, display: 'flex', position: 'relative', minWidth: 260 }}>
          <Search size={16} style={{ position: 'absolute', left: 12, top: 12, color: 'var(--text-dim)' }} />
          <input
            type="text"
            placeholder="Search facts, preferences, entity IDs, or journals..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{
              width: '100%', padding: '10px 12px 10px 36px', borderRadius: 8,
              background: 'rgba(0,0,0,0.3)', border: '1px solid var(--border-subtle)',
              color: 'var(--text-main)', fontSize: 13, outline: 'none'
            }}
          />
        </form>

        <div style={{ display: 'flex', gap: 6, background: 'rgba(0,0,0,0.3)', padding: 4, borderRadius: 8, border: '1px solid var(--border-subtle)' }}>
          {[
            { id: 'all', label: 'All', icon: Layers },
            { id: 'preference', label: 'Preferences', icon: Sliders },
            { id: 'temporal', label: 'Temporal Graph', icon: Brain },
            { id: 'journal', label: 'Journals', icon: Calendar },
          ].map(({ id, label, icon: Icon }) => (
            <button
              key={id}
              onClick={() => setCategoryFilter(id)}
              style={{
                display: 'flex', alignItems: 'center', gap: 6, padding: '6px 12px', borderRadius: 6,
                border: 'none', background: categoryFilter === id ? 'var(--accent)' : 'transparent',
                color: categoryFilter === id ? '#000' : 'var(--text-dim)',
                cursor: 'pointer', fontSize: 12, fontWeight: categoryFilter === id ? 600 : 400
              }}
            >
              <Icon size={13} /> {label}
            </button>
          ))}
        </div>
      </div>

      {/* Memory List */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
        {memories.length === 0 ? (
          <div style={{ padding: 40, textAlign: 'center', color: 'var(--text-dim)', background: 'rgba(255,255,255,0.02)', borderRadius: 12, border: '1px solid var(--border-subtle)' }}>
            No memory entries found matching search query or category filter.
          </div>
        ) : (
          memories.map((item) => (
            <motion.div
              key={item.id}
              initial={{ opacity: 0, y: 4 }}
              animate={{ opacity: 1, y: 0 }}
              style={{
                padding: 16, borderRadius: 10, background: 'rgba(255,255,255,0.03)',
                border: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between',
                alignItems: 'center', gap: 16
              }}
            >
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span
                    style={{
                      padding: '2px 8px', borderRadius: 4, fontSize: 10, fontWeight: 700, textTransform: 'uppercase',
                      background: item.category === 'preference' ? 'rgba(59, 130, 246, 0.2)' : item.category === 'temporal' ? 'rgba(168, 85, 247, 0.2)' : 'rgba(34, 197, 94, 0.2)',
                      color: item.category === 'preference' ? '#60a5fa' : item.category === 'temporal' ? '#c084fc' : '#4ade80',
                      border: `1px solid ${item.category === 'preference' ? '#3b82f640' : item.category === 'temporal' ? '#a855f740' : '#22c55e40'}`
                    }}
                  >
                    {item.type || item.category}
                  </span>

                  <span style={{ fontSize: 14, fontWeight: 600, color: 'var(--text-main)' }}>
                    {item.key || item.entity_id || item.date || item.id}
                  </span>

                  {item.temporal_relevance !== undefined && (
                    <span style={{ fontSize: 11, color: 'var(--text-dim)', background: 'rgba(255,255,255,0.05)', padding: '2px 6px', borderRadius: 4 }}>
                      Relevance: {(item.temporal_relevance * 100).toFixed(0)}%
                    </span>
                  )}
                </div>

                <div style={{ fontSize: 13, color: 'var(--text-dim)', wordBreak: 'break-word', fontFamily: 'monospace', letterSpacing: showKeys ? 'normal' : '2px' }}>
                  {showKeys
                    ? (item.summary || (typeof item.value === 'object' ? JSON.stringify(item.value) : String(item.value ?? JSON.stringify(item.state))))
                    : '••••••••••••••••'}
                </div>
              </div>

              <div style={{ display: 'flex', gap: 8 }}>
                <button
                  onClick={() => {
                    setEditingItem(item);
                    setEditValue(typeof item.value === 'object' ? JSON.stringify(item.value, null, 2) : String(item.value ?? JSON.stringify(item.state ?? '')));
                  }}
                  title="Edit Memory Value"
                  style={{
                    padding: 8, borderRadius: 6, border: '1px solid var(--border-subtle)',
                    background: 'rgba(255,255,255,0.05)', color: 'var(--text-main)', cursor: 'pointer'
                  }}
                >
                  <Edit3 size={14} />
                </button>

                <button
                  onClick={() => handleForgetEntity(item.key || item.entity_id || item.id)}
                  title="Forget Entity"
                  style={{
                    padding: 8, borderRadius: 6, border: '1px solid rgba(239, 68, 68, 0.3)',
                    background: 'rgba(239, 68, 68, 0.1)', color: '#ef4444', cursor: 'pointer'
                  }}
                >
                  <Trash2 size={14} />
                </button>
              </div>
            </motion.div>
          ))
        )}
      </div>

      {/* Edit Modal */}
      {editingItem && (
        <div style={{ position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', backdropFilter: 'blur(4px)', display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 100 }}>
          <div style={{ background: '#121318', border: '1px solid var(--border-subtle)', borderRadius: 12, padding: 24, width: 480, maxWidth: '90vw', display: 'flex', flexDirection: 'column', gap: 16 }}>
            <h3 style={{ margin: 0, fontSize: 16, color: 'var(--text-main)' }}>
              Edit Memory Value for '{editingItem.key || editingItem.id}'
            </h3>
            <textarea
              rows={6}
              value={editValue}
              onChange={(e) => setEditValue(e.target.value)}
              style={{
                width: '100%', padding: 12, borderRadius: 8, background: 'rgba(0,0,0,0.4)',
                border: '1px solid var(--border-subtle)', color: 'var(--text-main)', fontFamily: 'monospace', fontSize: 13
              }}
            />
            <div style={{ display: 'flex', justifyContent: 'flex-end', gap: 10 }}>
              <button
                onClick={() => setEditingItem(null)}
                style={{ padding: '8px 16px', borderRadius: 6, border: '1px solid var(--border-subtle)', background: 'transparent', color: 'var(--text-dim)', cursor: 'pointer' }}
              >
                Cancel
              </button>
              <button
                onClick={handleSaveEdit}
                style={{ padding: '8px 16px', borderRadius: 6, border: 'none', background: 'var(--accent)', color: '#000', fontWeight: 600, cursor: 'pointer' }}
              >
                Save Changes
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
