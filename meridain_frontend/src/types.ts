/**
 * @license
 * SPDX-License-Identifier: Apache-2.0
 */

export interface Message {
  id: string;
  sender: 'user' | 'assistant';
  text: string;
  timestamp: string;
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
}

