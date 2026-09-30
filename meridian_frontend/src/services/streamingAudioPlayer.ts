/**
 * streamingAudioPlayer.ts — Unified Streaming TTS Audio Engine
 * Single source of truth for chunked, ultra-low latency voice synthesis and playback.
 * Shared across Desktop Mascot, Timeline Dashboard, and Floating Assistant.
 */

import { API_BASE_URL } from '../config';

export type AudioPlayerState = 'idle' | 'loading' | 'speaking';

class StreamingAudioPlayer {
  private static instance: StreamingAudioPlayer;
  private audioQueue: Map<number, string> = new Map();
  private nextSeqToEnqueue = 0;
  private nextSeqToPlay = 0;
  private isPlaying = false;
  private currentAudio: HTMLAudioElement | null = null;
  private textBuffer = '';
  private firstChunkDispatched = false;
  private generationId = 0;
  private stateListeners: Set<(state: AudioPlayerState) => void> = new Set();
  private currentState: AudioPlayerState = 'idle';

  private constructor() {}

  public static getInstance(): StreamingAudioPlayer {
    if (!StreamingAudioPlayer.instance) {
      StreamingAudioPlayer.instance = new StreamingAudioPlayer();
    }
    return StreamingAudioPlayer.instance;
  }

  public subscribeState(listener: (state: AudioPlayerState) => void): () => void {
    this.stateListeners.add(listener);
    listener(this.currentState);
    return () => this.stateListeners.delete(listener);
  }

  private setState(state: AudioPlayerState) {
    if (this.currentState !== state) {
      this.currentState = state;
      this.stateListeners.forEach(listener => listener(state));
    }
  }

  public resetSession(): number {
    this.stop();
    this.generationId++;
    this.textBuffer = '';
    this.firstChunkDispatched = false;
    this.nextSeqToEnqueue = 0;
    this.nextSeqToPlay = 0;
    return this.generationId;
  }

  public stop() {
    if (this.currentAudio) {
      this.currentAudio.pause();
      this.currentAudio.src = '';
      this.currentAudio = null;
    }
    this.audioQueue.forEach(url => URL.revokeObjectURL(url));
    this.audioQueue.clear();
    this.isPlaying = false;
    this.setState('idle');
  }

  public stopAllAudio() {
    this.stop();
  }

  public feedText(delta: string, genId?: number) {
    if (genId !== undefined && genId !== this.generationId) return;
    this.textBuffer += delta;

    // Early clause trigger: 3-5 words or punctuation mark for sub-200ms TTFA
    if (!this.firstChunkDispatched) {
      const words = this.textBuffer.trim().split(/\s+/);
      const clauseMatch = this.textBuffer.match(/^([^.,!?;:\n]+[.,!?;:\n])\s*(.*)$/s);
      if (clauseMatch && clauseMatch[1].trim()) {
        const firstChunk = clauseMatch[1].trim();
        this.textBuffer = clauseMatch[2];
        this.firstChunkDispatched = true;
        this.dispatchChunk(firstChunk);
      } else if (words.length >= 4) {
        const firstChunk = words.slice(0, 4).join(' ');
        const idx = this.textBuffer.indexOf(words[3]);
        this.textBuffer = (idx !== -1 ? this.textBuffer.slice(idx + words[3].length) : '').trim();
        this.firstChunkDispatched = true;
        this.dispatchChunk(firstChunk);
      }
      return;
    }

    while (true) {
      const match = this.textBuffer.match(/^([\s\S]*?[.!?,;:\n])\s*([\s\S]*)$/);
      if (match && match[1].trim().length > 0) {
        const chunk = match[1].trim();
        this.textBuffer = match[2] || '';
        this.dispatchChunk(chunk);
      } else {
        const words = this.textBuffer.trim().split(/\s+/);
        if (words.length >= 12) {
          const chunk = words.slice(0, 10).join(' ');
          const idx = this.textBuffer.indexOf(words[9]);
          this.textBuffer = (idx !== -1 ? this.textBuffer.slice(idx + words[9].length) : '').trim();
          this.dispatchChunk(chunk);
        } else {
          break;
        }
      }
    }
  }

  public dispatchImmediateText(fullText: string, genId?: number) {
    if (genId !== undefined && genId !== this.generationId) return;
    const clean = fullText.replace(/<[^>]*>/g, '').trim();
    if (!clean) return;

    const sentences = clean.match(/[^.!?\n]+[.!?\n]?/g) || [clean];
    for (const s of sentences) {
      const trimmed = s.trim();
      if (trimmed) this.dispatchChunk(trimmed);
    }
  }

  public flush(genId?: number) {
    if (genId !== undefined && genId !== this.generationId) return;
    if (this.textBuffer.trim()) {
      this.dispatchChunk(this.textBuffer.trim());
      this.textBuffer = '';
    }
    this.checkAndPlayNext();
  }

  private dispatchChunk(chunkText: string) {
    const clean = chunkText.replace(/<[^>]*>/g, '').trim();
    if (!clean) return;
    const seq = this.nextSeqToEnqueue++;
    this.fetchTTSForChunk(clean, seq, this.generationId);
  }

  private async fetchTTSForChunk(chunkText: string, seq: number, genId: number) {
    try {
      const voice = localStorage.getItem('meridian_tts_voice') || 'M1';
      const res = await fetch(`${API_BASE_URL}/api/tts`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: chunkText, voice, lang: 'na' }),
      });

      if (res.ok && genId === this.generationId) {
        const blob = await res.blob();
        if (genId === this.generationId) {
          const url = URL.createObjectURL(blob);
          this.audioQueue.set(seq, url);
          this.checkAndPlayNext();
        }
      }
    } catch (e) {
      console.warn('[StreamingAudioPlayer] Chunk synthesis error:', e);
    }
  }

  private checkAndPlayNext() {
    if (this.isPlaying) return;

    if (this.audioQueue.has(this.nextSeqToPlay)) {
      this.isPlaying = true;
      this.setState('speaking');

      const url = this.audioQueue.get(this.nextSeqToPlay)!;
      this.audioQueue.delete(this.nextSeqToPlay);
      this.nextSeqToPlay++;

      const audio = new Audio(url);
      const volume = parseFloat(localStorage.getItem('meridian_ui_volume') || '0.5');
      audio.volume = Math.max(0, Math.min(1, volume));
      this.currentAudio = audio;

      const cleanup = () => {
        URL.revokeObjectURL(url);
        if (this.currentAudio === audio) {
          this.currentAudio = null;
        }
        this.isPlaying = false;
        this.checkAndPlayNext();
      };

      audio.onended = cleanup;
      audio.onerror = cleanup;
      audio.play().catch(cleanup);
    } else if (this.audioQueue.size === 0 && !this.isPlaying) {
      this.setState('idle');
    }
  }
}

export const streamingAudio = StreamingAudioPlayer.getInstance();
