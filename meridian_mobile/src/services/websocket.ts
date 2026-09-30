/**
 * MOB-01: Mobile Full-Duplex WebSocket Service with Tailscale & LAN Auto-Fallback.
 * Outbound connection dials directly from Rust via @tauri-apps/plugin-websocket
 * bypassing Android incoming connection blocks & WebView CSP restrictions.
 */

let WebSocketPlugin: any = null;
try {
  // @ts-ignore
  WebSocketPlugin = (window as any).__TAURI__?.websocket;
} catch (e) {
  // Fallback for browser preview
}


export interface ServerEndpoint {
  type: 'tailscale' | 'lan' | 'localhost' | 'custom';
  ip: string;
  ws_url: string;
  http_url: string;
}

export type MessageCallback = (msg: any) => void;

class MeridianMobileWebSocket {
  private socket: any = null;
  private listeners: Set<MessageCallback> = new Set();
  private reconnectTimer: any = null;
  private isConnected: boolean = false;
  private currentEndpointIndex: number = 0;
  private configuredEndpoints: string[] = [];

  constructor() {
    this.initEndpoints();
  }

  private initEndpoints() {
    // Load cached or environment endpoints
    const savedCustom = localStorage.getItem('meridian_ws_target');
    const defaultPort = '4132';

    const candidates: string[] = [];
    if (savedCustom) {
      candidates.push(savedCustom);
    }

    // Common Tailscale & Local LAN IP defaults
    const tailscaleIp = localStorage.getItem('meridian_tailscale_ip');
    if (tailscaleIp) {
      candidates.push(`ws://${tailscaleIp}:${defaultPort}/ws`);
    }

    const lanIp = localStorage.getItem('meridian_lan_ip');
    if (lanIp) {
      candidates.push(`ws://${lanIp}:${defaultPort}/ws`);
    }

    // Default fallback IPs
    candidates.push(`ws://100.100.100.100:${defaultPort}/ws`); // Example Tailscale IP placeholder
    candidates.push(`ws://192.168.1.100:${defaultPort}/ws`);   // Example LAN IP placeholder
    candidates.push(`ws://127.0.0.1:${defaultPort}/ws`);      // Localhost fallback

    this.configuredEndpoints = Array.from(new Set(candidates));
  }

  public setEndpoints(endpoints: string[]) {
    this.configuredEndpoints = endpoints;
    this.currentEndpointIndex = 0;
  }

  public async connect(): Promise<boolean> {
    if (this.socket && this.isConnected) {
      return true;
    }

    const targetUrl = this.configuredEndpoints[this.currentEndpointIndex] || 'ws://127.0.0.1:4132/ws';
    console.log(`🔌 [MOB-01] Connecting to Meridian WebSocket target: ${targetUrl}`);

    try {
      // Use Tauri native WebSocket plugin dialer from Rust if available
      if (typeof window !== 'undefined' && (window as any).__TAURI__) {
        this.socket = await WebSocketPlugin.connect(targetUrl);
        this.socket.addListener((msg: any) => {
          this.handleIncoming(msg);
        });
      } else {
        // Fallback to browser WebSocket in standard dev web preview
        const rawSocket = new WebSocket(targetUrl);
        rawSocket.onmessage = (evt) => {
          this.handleIncoming(evt.data);
        };
        rawSocket.onopen = () => {
          this.isConnected = true;
          console.log(`✅ [MOB-01] Connected via Web WebSocket to ${targetUrl}`);
        };
        rawSocket.onclose = () => {
          this.handleDisconnect();
        };
        rawSocket.onerror = (err) => {
          console.warn(`⚠️ [MOB-01] Web socket error:`, err);
          this.handleDisconnect();
        };
        this.socket = rawSocket;
      }

      this.isConnected = true;
      localStorage.setItem('meridian_ws_target', targetUrl);
      return true;

    } catch (error) {
      console.warn(`❌ [MOB-01] Failed to connect to ${targetUrl}:`, error);
      this.isConnected = false;
      this.rotateEndpointAndRetry();
      return false;
    }
  }

  private handleIncoming(raw: any) {
    try {
      let data = raw;
      if (typeof raw === 'string') {
        data = JSON.parse(raw);
      } else if (raw && raw.data) {
        data = typeof raw.data === 'string' ? JSON.parse(raw.data) : raw.data;
      }


      // Automatically handle server network discovery payloads
      if (data && data.type === 'handshake_ack' && data.network) {
        if (data.network.endpoints) {
          const discoveredWsUrls = data.network.endpoints.map((e: ServerEndpoint) => e.ws_url);
          if (discoveredWsUrls.length > 0) {
            this.setEndpoints(discoveredWsUrls);
          }
        }
      }

      this.listeners.forEach((callback) => {
        try {
          callback(data);
        } catch (e) {
          console.error('Error in mobile WS listener callback:', e);
        }
      });
    } catch (e) {
      console.log('Received raw message:', raw);
    }
  }

  private rotateEndpointAndRetry() {
    this.currentEndpointIndex = (this.currentEndpointIndex + 1) % this.configuredEndpoints.length;
    console.log(`🔄 [MOB-01] Rotating to endpoint index ${this.currentEndpointIndex}: ${this.configuredEndpoints[this.currentEndpointIndex]}`);

    if (this.reconnectTimer) {
      clearTimeout(this.reconnectTimer);
    }

    // Auto reconnect delay
    this.reconnectTimer = setTimeout(() => {
      this.connect();
    }, 3000);
  }

  private handleDisconnect() {
    this.isConnected = false;
    console.log('🔌 [MOB-01] Mobile WebSocket disconnected. Attempting auto-reconnect...');
    this.rotateEndpointAndRetry();
  }

  public async send(message: any): Promise<boolean> {
    if (!this.socket || !this.isConnected) {
      console.warn('⚠️ [MOB-01] Cannot send message, socket not connected.');
      return false;
    }

    const payload = typeof message === 'string' ? message : JSON.stringify(message);

    try {
      if (this.socket.send) {
        await this.socket.send(payload);
        return true;
      }
      return false;
    } catch (e) {
      console.error('Failed to send payload over mobile socket:', e);
      return false;
    }
  }

  public addListener(callback: MessageCallback) {
    this.listeners.add(callback);
    return () => this.listeners.delete(callback);
  }

  public disconnect() {
    if (this.reconnectTimer) {
      clearTimeout(this.reconnectTimer);
    }
    if (this.socket && this.socket.close) {
      try {
        this.socket.close();
      } catch (e) {}
    }
    this.isConnected = false;
  }
}

export const mobileWebSocketService = new MeridianMobileWebSocket();
