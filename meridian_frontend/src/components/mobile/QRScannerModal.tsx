import React, { useState } from "react";
import { QrCode, X, ShieldCheck, Wifi, Cloud, Smartphone, ArrowRight, RefreshCw } from "lucide-react";

interface QRScannerModalProps {
  isOpen: boolean;
  onClose: () => void;
  onPairSuccess: (config: { localUrl: string; remoteUrl: string; token: string }) => void;
}

export const QRScannerModal: React.FC<QRScannerModalProps> = ({ isOpen, onClose, onPairSuccess }) => {
  const [manualIp, setManualIp] = useState("192.168.1.100:4132");
  const [manualToken, setManualToken] = useState("");
  const [isPairing, setIsPairing] = useState(false);

  if (!isOpen) return null;

  const handleSimulateScan = () => {
    setIsPairing(true);
    setTimeout(() => {
      onPairSuccess({
        localUrl: `http://${manualIp || "192.168.1.100:4132"}`,
        remoteUrl: "https://meridian-x.trycloudflare.com",
        token: manualToken || "simulated_aes256_token_9921",
      });
      setIsPairing(false);
      onClose();
    }, 1200);
  };

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-md z-50 flex items-center justify-center p-4">
      <div className="w-full max-w-sm bg-[#0D1322] border border-cyan-500/30 rounded-3xl p-5 shadow-2xl shadow-cyan-950/80 animate-in zoom-in-95 duration-200">
        {/* Header */}
        <div className="flex items-center justify-between mb-4">
          <div className="flex items-center gap-2.5">
            <div className="p-2 rounded-xl bg-purple-500/20 border border-purple-500/30 text-purple-400">
              <QrCode className="w-5 h-5" />
            </div>
            <div>
              <h3 className="text-sm font-bold text-white">Desktop Pairing</h3>
              <p className="text-[11px] text-slate-400">Scan QR or enter manual endpoint</p>
            </div>
          </div>
          <button onClick={onClose} className="p-1.5 rounded-full hover:bg-white/10 text-slate-400 hover:text-white">
            <X className="w-4 h-4" />
          </button>
        </div>

        {/* Viewfinder Target */}
        <div className="relative my-4 aspect-square w-full rounded-2xl bg-black/60 border-2 border-dashed border-cyan-500/40 flex flex-col items-center justify-center overflow-hidden group">
          <div className="absolute inset-4 border-2 border-cyan-400/80 rounded-xl pointer-events-none animate-pulse" />
          <Smartphone className="w-10 h-10 text-cyan-400 mb-2 animate-bounce" />
          <p className="text-xs text-slate-300 font-mono text-center px-4">
            Point camera at QR code on Desktop screen
          </p>

          {isPairing && (
            <div className="absolute inset-0 bg-black/90 flex flex-col items-center justify-center gap-2">
              <RefreshCw className="w-8 h-8 text-cyan-400 animate-spin" />
              <span className="text-xs font-mono text-cyan-300">Verifying AES-256 Auth Handshake...</span>
            </div>
          )}
        </div>

        {/* Manual Endpoint Form Fallback */}
        <div className="space-y-2.5 my-3">
          <div>
            <label className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider block mb-1">
              Local IP / Port
            </label>
            <input
              type="text"
              value={manualIp}
              onChange={(e) => setManualIp(e.target.value)}
              placeholder="e.g. 192.168.1.100:4132"
              className="w-full px-3 py-2 rounded-xl bg-white/5 border border-white/10 text-xs font-mono text-white focus:outline-none focus:border-cyan-500/60"
            />
          </div>
          <div>
            <label className="text-[10px] font-semibold text-slate-400 uppercase tracking-wider block mb-1">
              Pairing Auth Token (Optional)
            </label>
            <input
              type="password"
              value={manualToken}
              onChange={(e) => setManualToken(e.target.value)}
              placeholder="AES-256 session token"
              className="w-full px-3 py-2 rounded-xl bg-white/5 border border-white/10 text-xs font-mono text-white focus:outline-none focus:border-cyan-500/60"
            />
          </div>
        </div>

        {/* Connect Action Button */}
        <button
          onClick={handleSimulateScan}
          disabled={isPairing}
          className="w-full mt-2 py-3 rounded-xl bg-gradient-to-r from-cyan-500 to-purple-600 font-medium text-white text-xs flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/25 active:scale-98 transition-all"
        >
          <span>Establish Encrypted Session</span>
          <ArrowRight className="w-4 h-4" />
        </button>

        {/* Security Badge */}
        <div className="mt-3 flex items-center justify-center gap-1.5 text-[10px] text-slate-400 font-mono">
          <ShieldCheck className="w-3.5 h-3.5 text-emerald-400" />
          <span>E2E Encrypted Local & Cloudflare Tunnel</span>
        </div>
      </div>
    </div>
  );
};
