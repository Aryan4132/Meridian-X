// Meridian-X Chrome Extension Service Worker (Manifest V3)
const DEFAULT_PORTS = [4132, 8000];
let ws = null;
let currentPortIndex = 0;
let reconnectTimer = null;
let isConnected = false;
let reconnectAttempts = 0;

function getWsUrl() {
  const port = DEFAULT_PORTS[currentPortIndex];
  return `ws://127.0.0.1:${port}/api/browser/extension`;
}

function connect() {
  // Guard: already connecting or open on a live socket
  if (ws && (ws.readyState === WebSocket.CONNECTING || ws.readyState === WebSocket.OPEN)) {
    return;
  }

  // Clean up stale dead socket references before creating a new one
  if (ws) {
    try { ws.close(); } catch (_) {}
    ws = null;
  }

  const url = getWsUrl();
  console.log(`[Meridian Bridge] Attempting connection to ${url} (attempt ${reconnectAttempts + 1})`);

  try {
    ws = new WebSocket(url);
  } catch (err) {
    console.warn(`[Meridian Bridge] WebSocket construction failed: ${err}`);
    scheduleReconnect();
    return;
  }

  ws.onopen = () => {
    console.log(`[Meridian Bridge] Connected to ${url}`);
    isConnected = true;
    reconnectAttempts = 0;
    if (reconnectTimer) { clearTimeout(reconnectTimer); reconnectTimer = null; }
    chrome.storage.local.set({ meridian_connected: true, meridian_port: DEFAULT_PORTS[currentPortIndex] });
    chrome.action.setBadgeText({ text: "ON" });
    chrome.action.setBadgeBackgroundColor({ color: "#10b981" }); // Emerald green

    // Handshake
    ws.send(JSON.stringify({
      type: "handshake",
      payload: {
        agent: "chrome-extension",
        version: "1.0.1",
        timestamp: Date.now()
      }
    }));
  };

  ws.onmessage = async (event) => {
    try {
      const msg = JSON.parse(event.data);
      // Ignore pongs — they are just keepalives
      if (msg.type === "pong" || msg.type === "handshake_ack") return;
      console.log("[Meridian Bridge] Received command:", msg);
      handleIncomingMessage(msg);
    } catch (err) {
      console.error("[Meridian Bridge] Failed to parse message:", err);
    }
  };

  ws.onclose = (event) => {
    console.warn(`[Meridian Bridge] Disconnected from ${url} (code=${event.code})`);
    isConnected = false;
    ws = null;
    chrome.storage.local.set({ meridian_connected: false });
    chrome.action.setBadgeText({ text: "OFF" });
    chrome.action.setBadgeBackgroundColor({ color: "#64748b" }); // Slate
    scheduleReconnect();
  };

  ws.onerror = () => {
    console.warn("[Meridian Bridge] WebSocket error on", url);
    // onclose will fire after onerror — no need to schedule reconnect here
    try { ws.close(); } catch (_) {}
  };
}

function scheduleReconnect() {
  if (reconnectTimer) clearTimeout(reconnectTimer);
  reconnectAttempts++;
  // Rotate ports on every other attempt so both ports are tried equally
  if (reconnectAttempts % 2 === 0) {
    currentPortIndex = (currentPortIndex + 1) % DEFAULT_PORTS.length;
  }
  // Exponential backoff capped at 15s: 3s, 6s, 12s, 15s, 15s...
  const delay = Math.min(3000 * Math.pow(1.5, Math.min(reconnectAttempts - 1, 4)), 15000);
  console.log(`[Meridian Bridge] Reconnecting in ${Math.round(delay / 1000)}s to port ${DEFAULT_PORTS[currentPortIndex]}`);
  reconnectTimer = setTimeout(connect, delay);
}

// Keep Service Worker alive with lightweight alarm (requires "alarms" permission in manifest)
chrome.alarms.create("meridian_heartbeat", { periodInMinutes: 0.4 });
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === "meridian_heartbeat") {
    if (!ws || ws.readyState === WebSocket.CLOSED || ws.readyState === WebSocket.CLOSING) {
      connect();
    } else if (ws.readyState === WebSocket.OPEN) {
      try {
        ws.send(JSON.stringify({ type: "ping", timestamp: Date.now() }));
      } catch (e) {
        console.warn("[Meridian Bridge] Ping failed:", e);
        connect();
      }
    }
  }
});

// Initial boot
connect();

async function handleIncomingMessage(msg) {
  const { id, action, params } = msg;
  if (!action || !id) return;

  try {
    // Find active tab
    const [activeTab] = await chrome.tabs.query({ active: true, lastFocusedWindow: true });
    if (!activeTab || !activeTab.id) {
      sendResponse(id, { success: false, error: "No active browser tab found" });
      return;
    }

    if (action === "get_tab_info") {
      sendResponse(id, {
        success: true,
        data: {
          id: activeTab.id,
          title: activeTab.title,
          url: activeTab.url,
          favIconUrl: activeTab.favIconUrl
        }
      });
      return;
    }

    if (action === "open_tab") {
      const newTab = await chrome.tabs.create({ url: params.url || "about:blank", active: params.active ?? true });
      sendResponse(id, { success: true, message: `Opened tab ${newTab.id} at ${newTab.url}`, data: { id: newTab.id, url: newTab.url } });
      return;
    }

    if (action === "navigate") {
      await chrome.tabs.update(activeTab.id, { url: params.url });
      sendResponse(id, { success: true, message: `Navigated to ${params.url}` });
      return;
    }

    // Forward DOM actions to Content Script via scripting.executeScript (more reliable than sendMessage for cross-origin)
    chrome.tabs.sendMessage(activeTab.id, { id, action, params }, (res) => {
      if (chrome.runtime.lastError) {
        // Content script not loaded on this page — try injecting it first
        chrome.scripting.executeScript(
          { target: { tabId: activeTab.id }, files: ["content.js"] },
          () => {
            if (chrome.runtime.lastError) {
              sendResponse(id, { success: false, error: `Content script injection failed: ${chrome.runtime.lastError.message}` });
              return;
            }
            // Retry message after injection
            chrome.tabs.sendMessage(activeTab.id, { id, action, params }, (res2) => {
              if (chrome.runtime.lastError) {
                sendResponse(id, { success: false, error: chrome.runtime.lastError.message });
              } else {
                sendResponse(id, res2 || { success: true });
              }
            });
          }
        );
      } else {
        sendResponse(id, res || { success: true });
      }
    });

  } catch (err) {
    sendResponse(id, { success: false, error: String(err) });
  }
}

function sendResponse(id, result) {
  if (ws && ws.readyState === WebSocket.OPEN) {
    try {
      ws.send(JSON.stringify({
        type: "rpc_response",
        id: id,
        result: result,
        timestamp: Date.now()
      }));
    } catch (e) {
      console.warn("[Meridian Bridge] Failed to send response:", e);
    }
  }
}

// Listener for messages from popup
chrome.runtime.onMessage.addListener((req, sender, sendResponseToSender) => {
  if (req.action === "get_status") {
    sendResponseToSender({ connected: isConnected, port: DEFAULT_PORTS[currentPortIndex] });
  } else if (req.action === "reconnect") {
    // Force full reconnect
    if (ws) { try { ws.close(); } catch (_) {} ws = null; }
    isConnected = false;
    reconnectAttempts = 0;
    connect();
    sendResponseToSender({ status: "reconnecting" });
  }
  return true;
});
