/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export interface Message {
  id?: string;
  role: 'user' | 'assistant';
  content: string;
  timestamp: number | string;
}


export type ThoughtType = 'planning' | 'ocr' | 'exec' | 'status' | 'info' | 'warning';

export interface ThoughtStep {
  id: string;
  type: ThoughtType;
  text: string;
  timestamp: string;
  tool?: string;
  command?: string;
  status: 'pending' | 'running' | 'completed' | 'failed';
}

export interface ModelSettings {
  modelSource: 'local' | 'api';
  apiProvider?: string;
  selectedModel: string;
  brainModel: string;
  ocrModel: string;
  openaiKey?: string;
  anthropicKey?: string;
  geminiKey?: string;
  deepseekKey?: string;
}

export interface SystemResource {
  cpuUsage: number;
  ramUsage: number;
  cpuHistory: number[];
  ramHistory: number[];
}

export interface ProactiveNudge {
  id: string;
  type: string;
  title: string;
  message: string;
  action_hint?: string;
  icon: string;
  timestamp: string;
  mascot_state?: string;
  action?: string;
  patch?: {
    file_path: string;
    original: string;
    proposed: string;
    error_message: string;
  };
}

export interface JobRun {
  id: number | string;
  status: string;
  goal: string;
  timestamp: number;
  log?: string;
}

export interface ClipboardRecord {
  text: string;
  timestamp: number;
}

export interface DeveloperStats {
  total: number;
  success: number;
  failed: number;
  audits: number;
  heals: number;
  gitCommits: number;
  pomodoros: number;
}

export interface SystemUsage {
  cpu: number;
  ram: number;
}
