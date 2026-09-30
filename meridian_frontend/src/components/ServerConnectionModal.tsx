import React, { useState, useEffect } from 'react';
import { getApiBaseUrl, getApiKey, hashPasswordSHA256 } from '../config';

interface Props {
  isOpen: boolean;
  onClose: () => void;
}

export const ServerConnectionModal: React.FC<Props> = ({ isOpen, onClose }) => {
  const [serverUrl, setServerUrl] = useState('');
  const [password, setPassword] = useState('');
  const [statusMsg, setStatusMsg] = useState<{ text: string; isError: boolean } | null>(null);
  const [isTesting, setIsTesting] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setServerUrl(localStorage.getItem('MERIDIAN_REMOTE_BACKEND_URL') || getApiBaseUrl());
      setPassword(localStorage.getItem('MERIDIAN_REMOTE_API_KEY') || getApiKey());
      setStatusMsg(null);
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const getEffectiveAuthKey = async (rawInput: string): Promise<string> => {
    const trimmed = rawInput.trim();
    if (!trimmed) return '';
    // If it looks like a 64-char hex string (already hashed or raw 32-byte key), use as is.
    if (/^[a-fA-F0-9]{64}$/.test(trimmed)) {
      return trimmed;
    }
    // Otherwise compute SHA-256 hash of custom user password
    return await hashPasswordSHA256(trimmed);
  };

  const handleTestConnection = async () => {
    setIsTesting(true);
    setStatusMsg(null);
    const targetUrl = serverUrl.trim().replace(/\/+$/, '');
    try {
      const headers: Record<string, string> = {};
      const keyOrHash = await getEffectiveAuthKey(password);
      if (keyOrHash) {
        headers['X-API-Key'] = keyOrHash;
      }
      const res = await fetch(`${targetUrl}/api/health`, { headers });
      if (res.ok) {
        setStatusMsg({ text: '✅ Connected successfully with encrypted key!', isError: false });
      } else {
        setStatusMsg({ text: `⚠️ Server returned status ${res.status}`, isError: true });
      }
    } catch (err: any) {
      setStatusMsg({ text: `❌ Connection failed: ${err.message || 'Network error'}`, isError: true });
    } finally {
      setIsTesting(false);
    }
  };

  const handleSave = async () => {
    if (serverUrl.trim()) {
      localStorage.setItem('MERIDIAN_REMOTE_BACKEND_URL', serverUrl.trim());
    } else {
      localStorage.removeItem('MERIDIAN_REMOTE_BACKEND_URL');
    }

    if (password.trim()) {
      const keyOrHash = await getEffectiveAuthKey(password);
      localStorage.setItem('MERIDIAN_REMOTE_API_KEY', keyOrHash);
    } else {
      localStorage.removeItem('MERIDIAN_REMOTE_API_KEY');
    }

    window.location.reload();
  };

  const handleResetLocal = () => {
    localStorage.removeItem('MERIDIAN_REMOTE_BACKEND_URL');
    localStorage.removeItem('MERIDIAN_REMOTE_API_KEY');
    window.location.reload();
  };

  const inputStyle: React.CSSProperties = {
    width: '100%',
    background: 'var(--bg-panel)',
    border: '1px solid var(--border-subtle)',
    borderRadius: 12,
    padding: '8px 12px',
    fontSize: 14,
    color: 'var(--text-main)',
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4" style={{ background: 'color-mix(in srgb, var(--bg-void) 70%, transparent)' }}>
      <div className="rounded-2xl max-w-md w-full p-6 shadow-2xl space-y-5" style={{ background: 'var(--bg-float)', border: '1px solid var(--border-subtle)', color: 'var(--text-bright)' }}>
        <div className="flex items-center justify-between pb-3" style={{ borderBottom: '1px solid var(--border-subtle)' }}>
          <div className="flex items-center gap-2">
            <span className="text-xl">🌐</span>
            <h3 className="font-semibold text-lg" style={{ fontFamily: 'var(--font-heading)' }}>Backend Server Settings</h3>
          </div>
          <button
            onClick={onClose}
            className="transition-colors"
            style={{ color: 'var(--text-dim)' }}
          >
            ✕
          </button>
        </div>

        <p className="text-xs leading-relaxed" style={{ color: 'var(--text-dim)' }}>
          Connect to local machine or a remote hosted Meridian-X server.
        </p>

        <div className="space-y-4">
          <div>
            <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-main)' }}>Server URL</label>
            <input
              type="text"
              value={serverUrl}
              onChange={(e) => setServerUrl(e.target.value)}
              placeholder="http://127.0.0.1:4132 or https://my-server.com"
              style={inputStyle}
            />
          </div>

          <div>
            <label className="block text-xs font-medium mb-1" style={{ color: 'var(--text-main)' }}>Connection Password / API Key (SHA-256 Encrypted)</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="Enter custom password or secret key"
              style={inputStyle}
            />
          </div>
        </div>

        {statusMsg && (
          <div
            className="p-3 rounded-xl text-xs font-medium"
            style={statusMsg.isError
              ? { background: 'color-mix(in srgb, var(--danger) 12%, transparent)', border: '1px solid var(--danger)', color: 'var(--danger)' }
              : { background: 'color-mix(in srgb, var(--success) 12%, transparent)', border: '1px solid var(--success)', color: 'var(--success)' }}
          >
            {statusMsg.text}
          </div>
        )}

        <div className="flex items-center gap-2 pt-2">
          <button
            onClick={handleTestConnection}
            disabled={isTesting}
            className="flex-1 py-2 px-3 text-xs rounded-xl font-medium transition-colors disabled:opacity-50"
            style={{ background: 'var(--bg-surface)', color: 'var(--text-main)', border: '1px solid var(--border-subtle)' }}
          >
            {isTesting ? 'Testing...' : 'Test Connection'}
          </button>
          <button
            onClick={handleSave}
            className="flex-1 py-2 px-3 text-xs rounded-xl font-medium transition-colors"
            style={{ background: 'var(--accent)', color: 'var(--bg-void)' }}
          >
            Save & Connect
          </button>
        </div>

        <button
          onClick={handleResetLocal}
          className="w-full text-center text-xs underline pt-1"
          style={{ color: 'var(--text-ghost)' }}
        >
          Reset to Default Local Backend
        </button>
      </div>
    </div>
  );
};
