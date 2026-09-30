import React, { useState, useEffect } from "react";
import { Server, QrCode, X, Check, RefreshCw, AlertCircle, Wifi } from "lucide-react";

interface ServerConnectionModalProps {
  isOpen: boolean;
  onClose: () => void;
  currentBackendUrl: string;
  currentAuthToken: string;
  onSaveConfig: (url: string, token: string) => void;
  onOpenQRScanner: () => void;
}

export const ServerConnectionModal: React.FC<ServerConnectionModalProps> = ({
  isOpen,
  onClose,
  currentBackendUrl,
  currentAuthToken,
  onSaveConfig,
  onOpenQRScanner,
}) => {
  const [urlInput, setUrlInput] = useState(currentBackendUrl);
  const [tokenInput, setTokenInput] = useState(currentAuthToken);
  const [isTesting, setIsTesting] = useState(false);
  const [testResult, setTestResult] = useState<{ success: boolean; message: string; pingMs?: number } | null>(null);

  useEffect(() => {
    if (isOpen) {
      setUrlInput(currentBackendUrl || "http://192.168.1.100:4132");
      setTokenInput(currentAuthToken || "");
      setTestResult(null);
    }
  }, [isOpen, currentBackendUrl, currentAuthToken]);

  if (!isOpen) return null;

  const sanitizeUrl = (raw: string): string => {
    let clean = raw.trim();
    if (!clean.startsWith("http://") && !clean.startsWith("https://")) {
      clean = `http://${clean}`;
    }
    if (!clean.includes(":", 7) && !clean.startsWith("https://")) {
      clean = `${clean}:4132`;
    }
    return clean;
  };

  const handleTestConnection = async () => {
    const targetUrl = sanitizeUrl(urlInput);
    setIsTesting(true);
    setTestResult(null);
    const start = Date.now();

    try {
      const res = await fetch(`${targetUrl}/api/health`, {
        headers: tokenInput ? { Authorization: `Bearer ${tokenInput}` } : {},
      });
      const latency = Date.now() - start;

      if (res.ok) {
        setTestResult({
          success: true,
          message: `Connected successfully! Responded in ${latency}ms.`,
          pingMs: latency,
        });
      } else {
        setTestResult({
          success: false,
          message: `Server reachable but returned HTTP ${res.status} ${res.statusText}`,
        });
      }
    } catch (err: any) {
      setTestResult({
        success: false,
        message: `Connection failed: ${err.message || "Unable to reach server"}. Check IP & Wi-Fi.`,
      });
    } finally {
      setIsTesting(false);
    }
  };

  const handleSave = () => {
    const targetUrl = sanitizeUrl(urlInput);
    onSaveConfig(targetUrl, tokenInput);
    onClose();
  };

  const presets = [
    { label: "Emulator (10.0.2.2:4132)", url: "http://10.0.2.2:4132" },
    { label: "Local PC (4132)", url: "http://192.168.1.100:4132" },
    { label: "Cloudflare Tunnel", url: "https://meridian-x.trycloudflare.com" },
  ];

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-md z-[100] flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-[#0D1322] border border-cyan-500/30 rounded-3xl p-5 shadow-2xl shadow-cyan-950/80 space-y-4 animate-in fade-in zoom-in-95 duration-200">
        <div className="flex items-center justify-between pb-3 border-b border-white/10">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-cyan-500/10 border border-cyan-500/30 text-cyan-400">
              <Server className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-white tracking-wide">Server Pairing Settings</h3>
              <p className="text-[11px] text-slate-400">Connect mobile app to Meridian-X backend engine</p>
            </div>
          </div>
          <button
            onClick={onClose}
            className="p-1.5 rounded-xl bg-white/5 hover:bg-white/10 text-slate-400 hover:text-white transition-all"
          >
            <X className="w-4 h-4" />
          </button>
        </div>

        <div className="space-y-3">
          <div>
            <label className="block text-[11px] font-semibold uppercase tracking-wider text-slate-300 mb-1.5">
              Backend Endpoint URL
            </label>
            <input
              type="text"
              value={urlInput}
              onChange={(e) => setUrlInput(e.target.value)}
              placeholder="http://192.168.1.X:4132"
              className="w-full px-3.5 py-2.5 rounded-xl bg-white/5 border border-white/10 text-xs text-white placeholder-slate-500 font-mono focus:outline-none focus:border-cyan-500"
            />
          </div>

          <div>
            <label className="block text-[11px] font-semibold uppercase tracking-wider text-slate-300 mb-1.5">
              Bearer Auth Token (Optional)
            </label>
            <input
              type="password"
              value={tokenInput}
              onChange={(e) => setTokenInput(e.target.value)}
              placeholder="jwt_token_or_secret"
              className="w-full px-3.5 py-2.5 rounded-xl bg-white/5 border border-white/10 text-xs text-white placeholder-slate-500 font-mono focus:outline-none focus:border-cyan-500"
            />
          </div>

          <div>
            <span className="block text-[10px] uppercase font-semibold text-slate-400 mb-1.5">Quick Presets</span>
            <div className="flex flex-wrap gap-1.5">
              {presets.map((p, idx) => (
                <button
                  key={idx}
                  onClick={() => setUrlInput(p.url)}
                  className="px-2.5 py-1 rounded-lg bg-white/5 border border-white/10 hover:border-cyan-500/40 text-[10px] text-slate-300 hover:text-white transition-all font-mono"
                >
                  {p.label}
                </button>
              ))}
            </div>
          </div>

          {testResult && (
            <div
              className={`p-3 rounded-xl border text-xs flex items-start gap-2 ${
                testResult.success
                  ? "bg-emerald-500/10 border-emerald-500/30 text-emerald-300"
                  : "bg-rose-500/10 border-rose-500/30 text-rose-300"
              }`}
            >
              {testResult.success ? (
                <Check className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
              ) : (
                <AlertCircle className="w-4 h-4 text-rose-400 shrink-0 mt-0.5" />
              )}
              <span className="leading-snug">{testResult.message}</span>
            </div>
          )}
        </div>

        <div className="pt-2 flex items-center justify-between gap-2 border-t border-white/10">
          <button
            onClick={onOpenQRScanner}
            className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-white/5 border border-white/10 text-slate-300 hover:text-white text-xs font-medium transition-all"
          >
            <QrCode className="w-4 h-4 text-purple-400" />
            <span>Scan QR</span>
          </button>

          <div className="flex items-center gap-2">
            <button
              onClick={handleTestConnection}
              disabled={isTesting}
              className="flex items-center gap-1.5 px-3 py-2 rounded-xl bg-cyan-500/20 border border-cyan-500/40 text-cyan-300 hover:bg-cyan-500/30 text-xs font-medium transition-all"
            >
              {isTesting ? <RefreshCw className="w-3.5 h-3.5 animate-spin" /> : <Wifi className="w-3.5 h-3.5" />}
              <span>Test</span>
            </button>

            <button
              onClick={handleSave}
              className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 text-white font-medium text-xs shadow-lg shadow-cyan-500/20 active:scale-95 transition-all"
            >
              <Check className="w-4 h-4" />
              <span>Save & Connect</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
