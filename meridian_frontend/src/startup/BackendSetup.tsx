import React, { useState, useEffect } from 'react';
import { motion } from 'motion/react';
import { invoke } from '@tauri-apps/api/core';
import { Download, Cpu, CheckCircle2, AlertTriangle, RefreshCw } from 'lucide-react';
import { GITHUB_REPO } from '../config';

interface BackendSetupProps {
  onComplete: () => void;
}

type DownloadStatus = 'detecting' | 'downloading' | 'extracting' | 'complete' | 'error';

export function BackendSetup({ onComplete }: BackendSetupProps) {
  const [status, setStatus] = useState<DownloadStatus>('detecting');
  const [progress, setProgress] = useState<number>(0);
  const [downloadedMb, setDownloadedMb] = useState<number>(0);
  const [totalMb, setTotalMb] = useState<number>(0);
  const [speed, setSpeed] = useState<string>('0 MB/s');
  const [errorMessage, setErrorMessage] = useState<string>('');
  const [platformName, setPlatformName] = useState<string>('Detecting system...');

  const getPlatformAsset = (): { filename: string; label: string } => {
    const userAgent = navigator.userAgent.toLowerCase();
    if (userAgent.includes('win')) {
      return { filename: 'api-windows.zip', label: 'Windows (x64)' };
    } else if (userAgent.includes('mac')) {
      return { filename: 'api-macos.zip', label: 'macOS (Universal)' };
    } else {
      return { filename: 'api-linux.zip', label: 'Linux (x86_64)' };
    }
  };

  const startDownloadAndExtract = async () => {
    setStatus('downloading');
    setProgress(0);
    setErrorMessage('');

    try {
      const targetAsset = getPlatformAsset();
      setPlatformName(targetAsset.label);

      let version = '0.1.0';
      if ((window as any).__TAURI_INTERNALS__) {
        try {
          version = await invoke<string>('get_app_version');
        } catch (e) {
          console.warn('Could not get Tauri version, fallback to v0.1.0:', e);
        }
      }

      const downloadUrl = `https://github.com/${GITHUB_REPO}/releases/download/v${version}/${targetAsset.filename}`;

      const response = await fetch(downloadUrl);
      if (!response.ok) {
        throw new Error(`Failed to download sidecar package (HTTP ${response.status}). Release asset may still be building.`);
      }

      const contentLength = response.headers.get('content-length');
      const totalBytes = contentLength ? parseInt(contentLength, 10) : 0;
      setTotalMb(parseFloat((totalBytes / (1024 * 1024)).toFixed(1)));

      if (!response.body) {
        throw new Error('Response body is not readable');
      }

      const reader = response.body.getReader();
      const chunks: Uint8Array[] = [];
      let receivedBytes = 0;
      let startTime = Date.now();
      let lastTime = startTime;
      let lastBytes = 0;

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        chunks.push(value);
        receivedBytes += value.length;

        const now = Date.now();
        if (now - lastTime >= 400) {
          const timeDiffSec = (now - lastTime) / 1000;
          const bytesDiff = receivedBytes - lastBytes;
          const currentSpeedMBs = (bytesDiff / (1024 * 1024)) / timeDiffSec;
          setSpeed(`${currentSpeedMBs.toFixed(1)} MB/s`);

          lastTime = now;
          lastBytes = receivedBytes;
        }

        setDownloadedMb(parseFloat((receivedBytes / (1024 * 1024)).toFixed(1)));
        if (totalBytes > 0) {
          const pct = Math.min(100, Math.round((receivedBytes / totalBytes) * 100));
          setProgress(pct);
        }
      }

      setStatus('extracting');
      setProgress(100);

      // Concatenate downloaded chunks into a single Uint8Array
      const fullBuffer = new Uint8Array(receivedBytes);
      let offset = 0;
      for (const chunk of chunks) {
        fullBuffer.set(chunk, offset);
        offset += chunk.length;
      }

      if ((window as any).__TAURI_INTERNALS__) {
        await invoke('extract_backend_zip', { zipBytes: Array.from(fullBuffer) });
      }

      setStatus('complete');
      setTimeout(() => {
        onComplete();
      }, 1200);

    } catch (err: any) {
      console.error('Backend setup failed:', err);
      setStatus('error');
      setErrorMessage(err?.message || 'Download failed. Check your internet connection.');
    }
  };

  useEffect(() => {
    startDownloadAndExtract();
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center overflow-hidden" style={{ background: 'var(--bg-void)', color: 'var(--text-bright)' }}>
      {/* Background glowing particles effect */}
      <div className="absolute inset-0 pointer-events-none" style={{ background: 'radial-gradient(circle at center, var(--accent-muted) 0, transparent 70%)' }} />

      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="relative w-full max-w-lg p-8 rounded-2xl backdrop-blur-xl shadow-2xl text-center"
        style={{ background: 'var(--bg-float)', border: '1px solid var(--border-active)' }}
      >
        <div
          className="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-2xl"
          style={{ background: 'var(--accent-muted)', border: '1px solid var(--border-active)', color: 'var(--accent)' }}
        >
          {status === 'complete' ? (
            <CheckCircle2 className="h-8 w-8 animate-bounce" style={{ color: 'var(--success)' }} />
          ) : status === 'error' ? (
            <AlertTriangle className="h-8 w-8" style={{ color: 'var(--danger)' }} />
          ) : (
            <Cpu className="h-8 w-8 animate-pulse" style={{ color: 'var(--accent)' }} />
          )}
        </div>

        <h2 className="text-2xl font-bold tracking-tight mb-2" style={{ color: 'var(--text-bright)', fontFamily: 'var(--font-heading)' }}>
          {status === 'complete' ? 'Backend Engine Ready' : 'Setting Up Meridian Engine'}
        </h2>
        <p className="text-sm mb-6" style={{ color: 'var(--text-dim)' }}>
          {status === 'complete'
            ? 'Sidecar intelligence core initialized.'
            : `Downloading Python AI engine sidecar for ${platformName}...`}
        </p>

        {status === 'error' ? (
          <div className="mb-6 rounded-xl p-4 text-left" style={{ background: 'color-mix(in srgb, var(--danger) 10%, transparent)', border: '1px solid var(--danger)' }}>
            <p className="text-xs font-semibold mb-1" style={{ color: 'var(--danger)' }}>Installation Failed</p>
            <p className="text-xs" style={{ color: 'var(--text-main)' }}>{errorMessage}</p>
            <button
              onClick={startDownloadAndExtract}
              className="mt-4 flex w-full items-center justify-center gap-2 rounded-lg px-4 py-2 text-xs font-medium transition-all shadow-lg"
              style={{ background: 'var(--danger)', color: '#fff' }}
            >
              <RefreshCw className="h-4 w-4" /> Retry Download
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            {/* Progress bar container */}
            <div className="relative h-3 w-full overflow-hidden rounded-full" style={{ background: 'var(--bg-surface)', border: '1px solid var(--border-subtle)' }}>
              <motion.div
                className="h-full transition-all duration-300"
                style={{ width: `${progress}%`, background: 'var(--accent)' }}
              />
            </div>

            <div className="flex items-center justify-between text-xs" style={{ color: 'var(--text-dim)' }}>
              <span>
                {status === 'extracting'
                  ? 'Extracting binaries...'
                  : status === 'complete'
                  ? 'Ready'
                  : `${downloadedMb} MB / ${totalMb > 0 ? totalMb + ' MB' : '...'}`}
              </span>
              <span className="font-semibold" style={{ fontFamily: 'var(--font-main)', color: 'var(--accent)' }}>{progress}%</span>
              <span>{status === 'downloading' ? speed : ''}</span>
            </div>
          </div>
        )}
      </motion.div>
    </div>
  );
}
