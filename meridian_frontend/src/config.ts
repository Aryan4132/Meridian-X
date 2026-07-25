// Meridian-X Central Frontend Configuration

export const API_HOST = typeof window !== 'undefined' && (window as any).__MERIDIAN_API_HOST__
  ? (window as any).__MERIDIAN_API_HOST__
  : '127.0.0.1';

export const API_PORT = typeof window !== 'undefined' && (window as any).__MERIDIAN_API_PORT__
  ? (window as any).__MERIDIAN_API_PORT__
  : '4132';

const metaEnv = (import.meta as any).env;

export const API_BASE_URL = metaEnv?.VITE_API_BASE_URL
  ? metaEnv.VITE_API_BASE_URL
  : `http://${API_HOST}:${API_PORT}`;

export const GITHUB_REPO = 'Aryan4132/Meridian-X';
export const GITHUB_RELEASES_URL = `https://github.com/${GITHUB_REPO}/releases`;
