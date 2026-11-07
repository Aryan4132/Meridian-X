// Meridian-X Popup Script
document.addEventListener("DOMContentLoaded", async () => {
  const statusBadge = document.getElementById("statusBadge");
  const statusDot = document.getElementById("statusDot");
  const statusText = document.getElementById("statusText");
  const tabTitle = document.getElementById("tabTitle");
  const portVal = document.getElementById("portVal");
  const sendBtn = document.getElementById("sendBtn");
  const reconnectBtn = document.getElementById("reconnectBtn");

  // Query active tab
  const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
  if (tab) {
    tabTitle.textContent = tab.title || tab.url || "Blank tab";
  } else {
    tabTitle.textContent = "No active tab";
  }

  // Query service worker connection state
  chrome.runtime.sendMessage({ action: "get_status" }, (res) => {
    if (chrome.runtime.lastError) {
      // Service worker may be sleeping — show disconnected
      updateUIDisconnected();
      return;
    }
    if (res && res.connected) {
      updateUIConnected(res.port);
    } else {
      updateUIDisconnected(res && res.port);
    }
  });

  function updateUIConnected(port) {
    statusBadge.className = "badge badge-on";
    statusDot.className = "dot dot-on";
    statusText.textContent = "CONNECTED";
    portVal.textContent = `ws://127.0.0.1:${port || 4132}/api/browser/extension`;
    sendBtn.disabled = false;
  }

  function updateUIDisconnected(port) {
    statusBadge.className = "badge badge-off";
    statusDot.className = "dot dot-off";
    statusText.textContent = "DISCONNECTED";
    portVal.textContent = `ws://127.0.0.1:${port || 4132}/api/browser/extension`;
    sendBtn.disabled = true;
    sendBtn.title = "Reconnect to Meridian backend first";
  }

  reconnectBtn.addEventListener("click", () => {
    statusText.textContent = "CONNECTING...";
    chrome.runtime.sendMessage({ action: "reconnect" }, () => {
      if (chrome.runtime.lastError) return;
      setTimeout(() => {
        chrome.runtime.sendMessage({ action: "get_status" }, (res) => {
          if (chrome.runtime.lastError) { updateUIDisconnected(); return; }
          if (res && res.connected) {
            updateUIConnected(res.port);
          } else {
            updateUIDisconnected(res && res.port);
          }
        });
      }, 1500);
    });
  });

  sendBtn.addEventListener("click", async () => {
    if (!tab || !tab.id) return;

    // Step 1: Extract page text from content script
    sendBtn.textContent = "Extracting...";
    sendBtn.disabled = true;

    chrome.tabs.sendMessage(tab.id, { action: "extract_text", params: { maxLength: 4000 } }, async (extractRes) => {
      if (chrome.runtime.lastError || !extractRes || !extractRes.success) {
        sendBtn.textContent = "Extraction Failed";
        sendBtn.disabled = false;
        setTimeout(() => { sendBtn.textContent = "Send Tab to Meridian Agent"; sendBtn.disabled = false; }, 2000);
        return;
      }

      // Step 2: Forward extracted content to Meridian backend via HTTP
      sendBtn.textContent = "Sending to Meridian...";
      const pageData = extractRes.data || {};

      try {
        // Detect the connected port from storage
        const stored = await chrome.storage.local.get(["meridian_port"]);
        const port = stored.meridian_port || 4132;

        const payload = {
          text: `[Chrome Extension] Page received from browser tab.\n\nTitle: ${pageData.title || "?"}\nURL: ${pageData.url || "?"}\n\nContent:\n${pageData.text || ""}`,
          source: "chrome_extension"
        };

        const response = await fetch(`http://127.0.0.1:${port}/api/agent/message`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(payload),
          signal: AbortSignal.timeout(8000)
        });

        if (response.ok) {
          sendBtn.textContent = "✓ Sent to Meridian!";
          setTimeout(() => { sendBtn.textContent = "Send Tab to Meridian Agent"; sendBtn.disabled = false; }, 2500);
        } else {
          sendBtn.textContent = `Backend Error ${response.status}`;
          setTimeout(() => { sendBtn.textContent = "Send Tab to Meridian Agent"; sendBtn.disabled = false; }, 3000);
        }
      } catch (fetchErr) {
        // Backend might not have /api/agent/message — show tab data was captured anyway
        sendBtn.textContent = "✓ Tab Data Captured";
        console.warn("[Meridian Popup] Backend push failed (tab data captured by extension):", fetchErr);
        setTimeout(() => { sendBtn.textContent = "Send Tab to Meridian Agent"; sendBtn.disabled = false; }, 2500);
      }
    });
  });
});
