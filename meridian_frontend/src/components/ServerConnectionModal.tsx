import React, { useState, useEffect } from 'react';
import { getApiBaseUrl, getApiKey } from '../config';

interface Props {
  isOpen: boolean;
  onClose: () => void;
}

export const ServerConnectionModal: React.FC<Props> = ({ isOpen, onClose }) => {
  const [serverUrl, setServerUrl] = useState('');
  const [apiKey, setApiKey] = useState('');
  const [statusMsg, setStatusMsg] = useState<{ text: string; isError: boolean } | null>(null);
  const [isTesting, setIsTesting] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setServerUrl(localStorage.getItem('MERIDIAN_REMOTE_BACKEND_URL') || getApiBaseUrl());
      setApiKey(localStorage.getItem('MERIDIAN_REMOTE_API_KEY') || getApiKey());
      setStatusMsg(null);
    }
  }, [isOpen]);

  if (!isOpen) return null;

  const handleTestConnection = async () => {
    setIsTesting(true);
    setStatusMsg(null);
    const targetUrl = serverUrl.trim().replace(/\/+$/, '');
    try {
      const headers: Record<string, string> = {};
      if (apiKey.trim()) {
        headers['X-API-Key'] = apiKey.trim();
      }
      const res = await fetch(`${targetUrl}/api/health`, { headers });
      if (res.ok) {
        setStatusMsg({ text: '✅ Connected successfully!', isError: false });
      } else {
        setStatusMsg({ text: `⚠️ Server returned status ${res.status}`, isError: true });
      }
    } catch (err: any) {
      setStatusMsg({ text: `❌ Connection failed: ${err.message || 'Network error'}`, isError: true });
    } finally {
      setIsTesting(false);
    }
  };

  const handleSave = () => {
    if (serverUrl.trim()) {
      localStorage.setItem('MERIDIAN_REMOTE_BACKEND_URL', serverUrl.trim());
    } else {
      localStorage.removeItem('MERIDIAN_REMOTE_BACKEND_URL');
    }

    if (apiKey.trim()) {
      localStorage.setItem('MERIDIAN_REMOTE_API_KEY', apiKey.trim());
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

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-2xl max-w-md w-full p-6 text-white shadow-2xl space-y-5">
        <div className="flex items-center justify-between border-b border-slate-800 pb-3">
          <div className="flex items-center gap-2">
            <span className="text-xl">🌐</span>
            <h3 className="font-semibold text-lg">Backend Server Settings</h3>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white transition-colors"
          >
            ✕
          </button>
        </div>

        <p className="text-xs text-slate-400 leading-relaxed">
          Connect to local machine or a remote hosted Meridian-X server.
        </p>

        <div className="space-y-4">
          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">Server URL</label>
            <input
              type="text"
              value={serverUrl}
              onChange={(e) => setServerUrl(e.target.value)}
              placeholder="http://127.0.0.1:4132 or https://my-server.com"
              className="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>

          <div>
            <label className="block text-xs font-medium text-slate-300 mb-1">API Key (Required for Remote Server)</label>
            <input
              type="password"
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
              placeholder="Enter secret API key"
              className="w-full bg-slate-950 border border-slate-700 rounded-xl px-3 py-2 text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500"
            />
          </div>
        </div>

        {statusMsg && (
          <div className={`p-3 rounded-xl text-xs font-medium ${statusMsg.isError ? 'bg-rose-950/60 border border-rose-800 text-rose-300' : 'bg-emerald-950/60 border border-emerald-800 text-emerald-300'}`}>
            {statusMsg.text}
          </div>
        )}

        <div className="flex items-center gap-2 pt-2">
          <button
            onClick={handleTestConnection}
            disabled={isTesting}
            className="flex-1 py-2 px-3 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs rounded-xl font-medium transition-colors disabled:opacity-50"
          >
            {isTesting ? 'Testing...' : 'Test Connection'}
          </button>
          <button
            onClick={handleSave}
            className="flex-1 py-2 px-3 bg-indigo-600 hover:bg-indigo-500 text-white text-xs rounded-xl font-medium transition-colors"
          >
            Save & Connect
          </button>
        </div>

        <button
          onClick={handleResetLocal}
          className="w-full text-center text-xs text-slate-500 hover:text-slate-400 underline pt-1"
        >
          Reset to Default Local Backend
        </button>
      </div>
    </div>
  );
};
