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

export const getApiKey = (): string => {
  if (typeof window === 'undefined') return '';

  const fromWindow = (window as any).__MERIDIAN_API_KEY__;
  if (fromWindow) return String(fromWindow);

  const fromEnv = metaEnv?.VITE_API_KEY;
  if (fromEnv) return String(fromEnv);

  return window.localStorage.getItem('VITE_API_KEY') || '';
};

export const attachApiKeyToFetch = () => {
  if (typeof window === 'undefined') return;

  const apiKey = getApiKey();
  if (!apiKey) return;

  const originalFetch = window.fetch.bind(window);
  (window as any).fetch = (input: RequestInfo | URL, init?: RequestInit) => {
    const target = typeof input === 'string'
      ? input
      : input instanceof URL
        ? input.toString()
        : input.url;

    const isApiRequest = target.includes('/api/') || target.includes('api/');
    const isLocalRequest = target.startsWith('/') || target.startsWith('http://localhost') || target.startsWith('http://127.0.0.1') || target.startsWith('http://[::1]') || target.includes(':4132');

    if (isApiRequest && isLocalRequest) {
      const headers = new Headers(init?.headers || {});
      if (!headers.has('X-API-Key')) {
        headers.set('X-API-Key', apiKey);
      }
      return originalFetch(input, { ...init, headers });
    }

    return originalFetch(input, init);
  };
};

attachApiKeyToFetch();

export const GITHUB_REPO = 'Aryan4132/Meridian-X';
export const GITHUB_RELEASES_URL = `https://github.com/${GITHUB_REPO}/releases`;
