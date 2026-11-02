import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { Smartphone, QrCode, Copy, Check, X, Wifi, ShieldCheck, RefreshCw } from 'lucide-react';
import { API_BASE_URL } from '../../config';

interface PairingInfo {
  lan_ip: string;
  port: number;
  ws_url: string;
  http_url: string;
  auth_token: string;
  pairing_uri: string;
  tailscale_ip?: string;
  all_endpoints: Array<{ type: string; ip: string; ws_url: string; http_url: string }>;
}

interface MobilePairingModalProps {
  isOpen: boolean;
  onClose: () => void;
}

export default function MobilePairingModal({ isOpen, onClose }: MobilePairingModalProps) {
  const [pairingInfo, setPairingInfo] = useState<PairingInfo | null>(null);
  const [loading, setLoading] = useState(false);
  const [copiedKey, setCopiedKey] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  const fetchPairingInfo = async () => {
    setLoading(true);
    setError(null);
    try {
      const res = await fetch(`${API_BASE_URL}/api/system/pairing-info`);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const data = await res.json();
      setPairingInfo(data);
    } catch (err: any) {
      setError(err?.message || 'Failed to resolve LAN IP pairing details');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (isOpen) {
      fetchPairingInfo();
    }
  }, [isOpen]);

  const handleCopy = (key: string, text: string) => {
    navigator.clipboard.writeText(text);
    setCopiedKey(key);
    setTimeout(() => setCopiedKey(null), 2000);
  };

  if (!isOpen) return null;

  return (
    <AnimatePresence>
      <div
        style={{
          position: 'fixed',
          inset: 0,
          background: 'rgba(0, 0, 0, 0.75)',
          backdropFilter: 'blur(8px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 1000,
          padding: 20,
        }}
        onClick={onClose}
      >
        <motion.div
          initial={{ opacity: 0, scale: 0.94, y: 12 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.94, y: 12 }}
          transition={{ duration: 0.2, ease: 'easeOut' }}
          onClick={(e) => e.stopPropagation()}
          style={{
            background: 'var(--bg-card, #12151c)',
            border: '1px solid var(--border-glow, rgba(0, 240, 255, 0.25))',
            borderRadius: 16,
            width: '100%',
            maxWidth: 520,
            boxShadow: '0 20px 50px rgba(0, 0, 0, 0.6), 0 0 30px rgba(0, 240, 255, 0.1)',
            overflow: 'hidden',
            display: 'flex',
            flexDirection: 'column',
          }}
        >
          {/* Header */}
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'space-between',
              padding: '16px 20px',
              borderBottom: '1px solid var(--border-subtle, rgba(255, 255, 255, 0.08))',
              background: 'rgba(255, 255, 255, 0.02)',
            }}
          >
            <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
              <div
                style={{
                  width: 34,
                  height: 34,
                  borderRadius: 8,
                  background: 'color-mix(in srgb, var(--accent, #00f0ff) 15%, transparent)',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  border: '1px solid var(--accent, #00f0ff)',
                }}
              >
                <Smartphone size={18} color="var(--accent, #00f0ff)" />
              </div>
              <div>
                <h3 style={{ margin: 0, fontSize: 15, fontWeight: 700, color: 'var(--text-main, #ffffff)' }}>
                  Mobile Companion Pairing
                </h3>
                <p style={{ margin: 0, fontSize: 11, color: 'var(--text-dim, #8892b0)' }}>
                  Link Android / iOS phone directly to desktop engine
                </p>
              </div>
            </div>
            <button
              onClick={onClose}
              style={{
                background: 'transparent',
                border: 'none',
                color: 'var(--text-dim, #8892b0)',
                cursor: 'pointer',
                padding: 4,
                borderRadius: 6,
              }}
            >
              <X size={18} />
            </button>
          </div>

          {/* Body */}
          <div style={{ padding: 20, display: 'flex', flexDirection: 'column', gap: 18 }}>
            {error ? (
              <div
                style={{
                  padding: 14,
                  borderRadius: 10,
                  background: 'rgba(255, 75, 75, 0.1)',
                  border: '1px solid rgba(255, 75, 75, 0.3)',
                  color: '#ff6b6b',
                  fontSize: 12,
                }}
              >
                {error}
              </div>
            ) : null}

            {/* QR Code and Quick Scan Section */}
            <div style={{ display: 'flex', gap: 18, alignItems: 'center' }}>
              <div
                style={{
                  width: 154,
                  height: 154,
                  flexShrink: 0,
                  background: '#ffffff',
                  borderRadius: 12,
                  padding: 8,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  boxShadow: '0 4px 20px rgba(0, 0, 0, 0.3)',
                  border: '2px solid var(--accent, #00f0ff)',
                }}
              >
                <img
                  src={`${API_BASE_URL}/api/system/pairing-qr.svg?t=${Date.now()}`}
                  alt="Meridian-X Mobile Pairing QR"
                  style={{ width: '100%', height: '100%', objectFit: 'contain' }}
                />
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: 8, flex: 1 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                  <Wifi size={14} color="var(--success, #00ff88)" />
                  <span style={{ fontSize: 12, fontWeight: 600, color: 'var(--success, #00ff88)' }}>
                    Same Wi-Fi Network
                  </span>
                </div>
                <p style={{ margin: 0, fontSize: 11, color: 'var(--text-dim, #8892b0)', lineHeight: 1.5 }}>
                  Open camera app on your phone or tap <b>Scan QR</b> in Meridian-X Mobile to pair instantly without typing IP addresses.
                </p>
                <button
                  onClick={fetchPairingInfo}
                  disabled={loading}
                  style={{
                    display: 'inline-flex',
                    alignItems: 'center',
                    gap: 6,
                    padding: '6px 12px',
                    borderRadius: 8,
                    background: 'rgba(255, 255, 255, 0.05)',
                    border: '1px solid rgba(255, 255, 255, 0.1)',
                    color: 'var(--text-main, #ffffff)',
                    fontSize: 11,
                    cursor: 'pointer',
                    width: 'fit-content',
                    marginTop: 4,
                  }}
                >
                  <RefreshCw size={12} className={loading ? 'animate-spin' : ''} />
                  Refresh LAN IPs
                </button>
              </div>
            </div>

            {/* Manual Endpoints */}
            <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
              <span style={{ fontSize: 11, fontWeight: 700, color: 'var(--text-dim, #8892b0)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Manual Configuration
              </span>

              {/* WebSocket URL */}
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '8px 12px',
                  background: 'rgba(0, 0, 0, 0.35)',
                  borderRadius: 8,
                  border: '1px solid rgba(255, 255, 255, 0.06)',
                }}
              >
                <div style={{ display: 'flex', flexDirection: 'column', gap: 2, overflow: 'hidden' }}>
                  <span style={{ fontSize: 10, color: 'var(--text-dim, #8892b0)' }}>WebSocket Bridge</span>
                  <span style={{ fontSize: 12, fontFamily: 'monospace', color: 'var(--accent, #00f0ff)', textOverflow: 'ellipsis', overflow: 'hidden' }}>
                    {pairingInfo?.ws_url || 'Detecting...'}
                  </span>
                </div>
                <button
                  onClick={() => pairingInfo && handleCopy('ws', pairingInfo.ws_url)}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: copiedKey === 'ws' ? 'var(--success, #00ff88)' : 'var(--text-dim, #8892b0)',
                    cursor: 'pointer',
                    padding: 4,
                  }}
                  title="Copy WebSocket URL"
                >
                  {copiedKey === 'ws' ? <Check size={14} /> : <Copy size={14} />}
                </button>
              </div>

              {/* Pairing Token */}
              <div
                style={{
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  padding: '8px 12px',
                  background: 'rgba(0, 0, 0, 0.35)',
                  borderRadius: 8,
                  border: '1px solid rgba(255, 255, 255, 0.06)',
                }}
              >
                <div style={{ display: 'flex', flexDirection: 'column', gap: 2, overflow: 'hidden' }}>
                  <span style={{ fontSize: 10, color: 'var(--text-dim, #8892b0)' }}>Auth Pairing Password</span>
                  <span style={{ fontSize: 12, fontFamily: 'monospace', color: '#ffb300' }}>
                    {pairingInfo?.auth_token || '••••••••'}
                  </span>
                </div>
                <button
                  onClick={() => pairingInfo && handleCopy('token', pairingInfo.auth_token)}
                  style={{
                    background: 'transparent',
                    border: 'none',
                    color: copiedKey === 'token' ? 'var(--success, #00ff88)' : 'var(--text-dim, #8892b0)',
                    cursor: 'pointer',
                    padding: 4,
                  }}
                  title="Copy Pairing Password"
                >
                  {copiedKey === 'token' ? <Check size={14} /> : <Copy size={14} />}
                </button>
              </div>

              {/* Tailscale / Multi-NIC info if present */}
              {pairingInfo?.tailscale_ip && (
                <div
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: 6,
                    padding: '6px 10px',
                    borderRadius: 6,
                    background: 'rgba(0, 240, 255, 0.05)',
                    border: '1px solid rgba(0, 240, 255, 0.15)',
                    fontSize: 10,
                    color: 'var(--text-dim, #8892b0)',
                  }}
                >
                  <ShieldCheck size={12} color="var(--accent, #00f0ff)" />
                  <span>Tailscale VPN Mesh Node Detected: <b>{pairingInfo.tailscale_ip}</b></span>
                </div>
              )}
            </div>
          </div>
        </motion.div>
      </div>
    </AnimatePresence>
  );
}

