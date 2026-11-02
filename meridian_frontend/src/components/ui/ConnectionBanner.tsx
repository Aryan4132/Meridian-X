import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'motion/react';
import { WifiOff, RefreshCw, CheckCircle2 } from 'lucide-react';
import { useApp } from '../../AppContext';
import { API_BASE_URL } from '../../config';

export default function ConnectionBanner() {
  const { backendAlive } = useApp();
  const [retryAttempt, setRetryAttempt] = useState(1);
  const [countdown, setCountdown] = useState(3);
  const [justReconnected, setJustReconnected] = useState(false);

  useEffect(() => {
    if (backendAlive) {
      if (retryAttempt > 1) {
        setJustReconnected(true);
        const t = setTimeout(() => setJustReconnected(false), 3000);
        return () => clearTimeout(t);
      }
      setRetryAttempt(1);
      setCountdown(3);
      return;
    }

    // When offline, calculate exponential backoff: min(30, 2 ^ attempt)
    const nextInterval = Math.min(30, Math.max(3, Math.pow(1.6, retryAttempt)));
    setCountdown(Math.round(nextInterval));

    const timer = setInterval(() => {
      setCountdown((prev) => {
        if (prev <= 1) {
          setRetryAttempt((a) => a + 1);
          fetch(`${API_BASE_URL}/api/health`).catch(() => {});
          return Math.round(Math.min(30, Math.pow(1.6, retryAttempt + 1)));
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [backendAlive, retryAttempt]);

  const handleManualRetry = async () => {
    try {
      await fetch(`${API_BASE_URL}/api/health`);
    } catch {
      // Ignored - AppContext health check will catch state
    }
  };

  return (
    <AnimatePresence>
      {!backendAlive && (
        <motion.div
          initial={{ y: -40, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -40, opacity: 0 }}
          transition={{ duration: 0.25, ease: 'easeOut' }}
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            zIndex: 9999,
            background: 'linear-gradient(90deg, rgba(239, 68, 68, 0.95), rgba(185, 28, 28, 0.95))',
            color: '#fff',
            padding: '6px 16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
            fontSize: '12px',
            fontWeight: 500,
            boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
            backdropFilter: 'blur(8px)',
          }}
        >
          <div style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
            <WifiOff size={15} className="animate-pulse" />
            <span>
              <strong>Backend Disconnected:</strong> Reconnecting in {countdown}s (Attempt #{retryAttempt})
            </span>
          </div>
          <button
            onClick={handleManualRetry}
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '4px',
              padding: '3px 8px',
              borderRadius: '4px',
              background: 'rgba(255, 255, 255, 0.2)',
              border: '1px solid rgba(255, 255, 255, 0.3)',
              color: '#fff',
              fontSize: '11px',
              cursor: 'pointer',
              fontWeight: 600,
            }}
          >
            <RefreshCw size={12} />
            Retry Now
          </button>
        </motion.div>
      )}

      {justReconnected && (
        <motion.div
          initial={{ y: -40, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          exit={{ y: -40, opacity: 0 }}
          transition={{ duration: 0.25 }}
          style={{
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            zIndex: 9999,
            background: 'linear-gradient(90deg, rgba(16, 185, 129, 0.95), rgba(5, 150, 105, 0.95))',
            color: '#fff',
            padding: '6px 16px',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '8px',
            fontSize: '12px',
            fontWeight: 600,
            boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
          }}
        >
          <CheckCircle2 size={15} />
          <span>Backend Reconnected Successfully</span>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
