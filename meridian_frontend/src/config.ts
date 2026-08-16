// Meridian-X Central Frontend Configuration

export const API_HOST = typeof window !== 'undefined' && (window as any).__MERIDIAN_API_HOST__
  ? (window as any).__MERIDIAN_API_HOST__
  : '127.0.0.1';

export const API_PORT = typeof window !== 'undefined' && (window as any).__MERIDIAN_API_PORT__
  ? (window as any).__MERIDIAN_API_PORT__
  : '4132';

const metaEnv = (import.meta as any).env;

export const getApiBaseUrl = (): string => {
  if (typeof window !== 'undefined') {
    const customUrl = window.localStorage.getItem('MERIDIAN_REMOTE_BACKEND_URL');
    if (customUrl && customUrl.trim()) {
      return customUrl.trim().replace(/\/+$/, '');
    }
  }
  return metaEnv?.VITE_API_BASE_URL
    ? metaEnv.VITE_API_BASE_URL
    : `http://${API_HOST}:${API_PORT}`;
};

export const API_BASE_URL = getApiBaseUrl();

export const getApiKey = (): string => {
  if (typeof window === 'undefined') return '';

  const customKey = window.localStorage.getItem('MERIDIAN_REMOTE_API_KEY');
  if (customKey && customKey.trim()) return customKey.trim();

  const fromWindow = (window as any).__MERIDIAN_API_KEY__;
  if (fromWindow) return String(fromWindow);

  const fromEnv = metaEnv?.VITE_API_KEY;
  if (fromEnv) return String(fromEnv);

  return window.localStorage.getItem('VITE_API_KEY') || '';
};

export const attachApiKeyToFetch = () => {
  if (typeof window === 'undefined') return;

  const apiKey = getApiKey();
  const oauthToken = window.localStorage.getItem('MERIDIAN_OAUTH_TOKEN');
  if (!apiKey && !oauthToken) return;

  const originalFetch = window.fetch.bind(window);
  (window as any).fetch = (input: RequestInfo | URL, init?: RequestInit) => {
    const target = typeof input === 'string'
      ? input
      : input instanceof URL
        ? input.toString()
        : input.url;

    if (target.includes(`:${API_PORT}`)) {
      const nextInit: RequestInit = init ? { ...init } : {};
      const headers = new Headers(nextInit.headers || {});
      if (apiKey && !headers.has('X-API-Key')) {
        headers.set('X-API-Key', apiKey);
      }
      if (oauthToken && !headers.has('Authorization')) {
        headers.set('Authorization', `Bearer ${oauthToken}`);
      }
      nextInit.headers = headers;
      return originalFetch(input, nextInit);
    }
    return originalFetch(input, init);
  };
};

attachApiKeyToFetch();

export const GITHUB_REPO = 'Aryan4132/Meridian-X';
export const GITHUB_RELEASES_URL = `https://github.com/${GITHUB_REPO}/releases`;
