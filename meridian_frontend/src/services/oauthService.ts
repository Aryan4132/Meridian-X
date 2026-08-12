import { API_BASE_URL } from '../config';

export interface OAuthProvider {
  name: string;
  auth_url: string;
  token_url: string;
  scopes: string[];
}

export interface OAuthConnectionStatus {
  connected: boolean;
  updated_at: number | null;
}

export const getOAuthProviders = async (): Promise<Record<string, OAuthProvider>> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/oauth/providers`);
    const data = await response.json();
    return data.providers || {};
  } catch (error) {
    console.error('Failed to fetch OAuth providers:', error);
    return {};
  }
};

export const authorizeOAuthFlow = async (provider: string, redirectUri: string = window.location.origin + '/oauth/callback') => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/oauth/authorize`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ provider, redirect_uri: redirectUri })
    });
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('OAuth authorization request failed:', error);
    throw error;
  }
};

export const handleOAuthCallback = async (state: string, code: string, provider: string) => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/oauth/callback`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        state,
        code,
        provider,
        redirect_uri: window.location.origin + '/oauth/callback'
      })
    });
    const data = await response.json();
    if (data.access_token) {
      localStorage.setItem('MERIDIAN_OAUTH_TOKEN', data.access_token);
    }
    return data;
  } catch (error) {
    console.error('OAuth callback failed:', error);
    throw error;
  }
};

export const getOAuthConnectionsStatus = async (): Promise<Record<string, OAuthConnectionStatus>> => {
  try {
    const response = await fetch(`${API_BASE_URL}/api/auth/oauth/status`);
    const data = await response.json();
    return data.connections || {};
  } catch (error) {
    console.error('Failed to fetch OAuth connections status:', error);
    return {};
  }
};
