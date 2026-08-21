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

      let version = '0.5.2';
      if ((window as any).__TAURI_INTERNALS__) {
        try {
          version = await invoke<string>('get_app_version');
        } catch (e) {
          console.warn('Could not get Tauri version, fallback to v0.5.2:', e);
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
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-950 text-white font-sans overflow-hidden">
      {/* Background glowing particles effect */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_center,rgba(232,160,32,0.12)_0,transparent_70%)] pointer-events-none" />

      <motion.div
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        className="relative w-full max-w-lg p-8 rounded-2xl bg-slate-900/90 border border-amber-500/20 backdrop-blur-xl shadow-2xl shadow-amber-500/10 text-center"
      >
        <div className="mx-auto mb-6 flex h-16 w-16 items-center justify-center rounded-2xl bg-amber-500/10 border border-amber-500/30 text-amber-400">
          {status === 'complete' ? (
            <CheckCircle2 className="h-8 w-8 text-emerald-400 animate-bounce" />
          ) : status === 'error' ? (
            <AlertTriangle className="h-8 w-8 text-rose-400" />
          ) : (
            <Cpu className="h-8 w-8 animate-pulse text-amber-400" />
          )}
        </div>

        <h2 className="text-2xl font-bold tracking-tight text-slate-100 mb-2">
          {status === 'complete' ? 'Backend Engine Ready' : 'Setting Up Meridian Engine'}
        </h2>
        <p className="text-sm text-slate-400 mb-6">
          {status === 'complete'
            ? 'Sidecar intelligence core initialized.'
            : `Downloading Python AI engine sidecar for ${platformName}...`}
        </p>

        {status === 'error' ? (
          <div className="mb-6 rounded-xl bg-rose-500/10 border border-rose-500/30 p-4 text-left">
            <p className="text-xs font-semibold text-rose-400 mb-1">Installation Failed</p>
            <p className="text-xs text-rose-200">{errorMessage}</p>
            <button
              onClick={startDownloadAndExtract}
              className="mt-4 flex w-full items-center justify-center gap-2 rounded-lg bg-rose-600 hover:bg-rose-500 px-4 py-2 text-xs font-medium text-white transition-all shadow-lg"
            >
              <RefreshCw className="h-4 w-4" /> Retry Download
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            {/* Progress bar container */}
            <div className="relative h-3 w-full overflow-hidden rounded-full bg-slate-800 border border-slate-700">
              <motion.div
                className="h-full bg-gradient-to-r from-amber-500 to-amber-300 transition-all duration-300"
                style={{ width: `${progress}%` }}
              />
            </div>

            <div className="flex items-center justify-between text-xs text-slate-400">
              <span>
                {status === 'extracting'
                  ? 'Extracting binaries...'
                  : status === 'complete'
                  ? 'Ready'
                  : `${downloadedMb} MB / ${totalMb > 0 ? totalMb + ' MB' : '...'}`}
              </span>
              <span className="font-mono text-amber-400 font-semibold">{progress}%</span>
              <span>{status === 'downloading' ? speed : ''}</span>
            </div>
          </div>
        )}
      </motion.div>
    </div>
  );
}
