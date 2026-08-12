import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:4132';

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
    const response = await axios.get(`${API_BASE_URL}/api/auth/oauth/providers`);
    return response.data.providers || {};
  } catch (error) {
    console.error('Failed to fetch OAuth providers:', error);
    return {};
  }
};

export const authorizeOAuthFlow = async (provider: string, redirectUri: string = window.location.origin + '/oauth/callback') => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/auth/oauth/authorize`, {
      provider,
      redirect_uri: redirectUri
    });
    return response.data;
  } catch (error) {
    console.error('OAuth authorization request failed:', error);
    throw error;
  }
};

export const handleOAuthCallback = async (state: string, code: string, provider: string) => {
  try {
    const response = await axios.post(`${API_BASE_URL}/api/auth/oauth/callback`, {
      state,
      code,
      provider,
      redirect_uri: window.location.origin + '/oauth/callback'
    });
    if (response.data.access_token) {
      localStorage.setItem('MERIDIAN_OAUTH_TOKEN', response.data.access_token);
    }
    return response.data;
  } catch (error) {
    console.error('OAuth callback failed:', error);
    throw error;
  }
};

export const getOAuthConnectionsStatus = async (): Promise<Record<string, OAuthConnectionStatus>> => {
  try {
    const response = await axios.get(`${API_BASE_URL}/api/auth/oauth/status`);
    return response.data.connections || {};
  } catch (error) {
    console.error('Failed to fetch OAuth connections status:', error);
    return {};
  }
};
