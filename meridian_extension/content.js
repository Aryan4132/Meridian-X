// Meridian-X Chrome Extension Content Script
(() => {
  // Guard against double-injection on navigations
  if (window.__meridianBridgeLoaded) return;
  window.__meridianBridgeLoaded = true;

  console.log("[Meridian Bridge] Content script initialized on:", window.location.href);

  chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    const { action, params } = request;

    switch (action) {
      case "extract_text":
        sendResponse({
          success: true,
          data: {
            title: document.title,
            url: window.location.href,
            text: getVisibleText(params?.maxLength || 8000),
            metaDescription: document.querySelector('meta[name="description"]')?.content || ""
          }
        });
        break;

      case "get_interactive_elements":
        sendResponse({
          success: true,
          data: extractInteractiveElements()
        });
        break;

      case "click":
        sendResponse(handleClick(params?.selector, params?.text));
        break;

      case "fill":
        sendResponse(handleFill(params?.selector, params?.value, params?.submit));
        break;

      case "edit_element":
        sendResponse(handleEditElement(params?.selector, params?.html, params?.text));
        break;

      case "scroll":
        const direction = params?.direction || "down";
        const amount = params?.amount || 500;
        window.scrollBy({
          top: direction === "down" ? amount : -amount,
          behavior: "smooth"
        });
        sendResponse({ success: true, message: `Scrolled ${direction} by ${amount}px` });
        break;

      case "navigate":
        // Navigate the current tab (used when background sends it through content script path)
        window.location.href = params?.url || "";
        sendResponse({ success: true, message: `Navigating to ${params?.url}` });
        break;

      default:
        sendResponse({ success: false, error: `Unknown action: ${action}` });
    }

    return true; // Keep channel open for async
  });

  function getVisibleText(limit) {
    const clone = document.body.cloneNode(true);
    // Remove scripts, styles, noscript, svg
    const removables = clone.querySelectorAll("script, style, noscript, svg, iframe");
    removables.forEach(el => el.remove());

    const text = clone.innerText || clone.textContent || "";
    const cleanText = text.replace(/\s+/g, " ").trim();
    return cleanText.substring(0, limit);
  }

  function extractInteractiveElements() {
    const nodes = document.querySelectorAll("a, button, input, select, textarea, [role='button'], [tabindex='0']");
    const elements = [];
    let count = 0;

    nodes.forEach((el, index) => {
      if (count >= 50) return; // Cap at top 50 interactive items
      const rect = el.getBoundingClientRect();
      const isVisible = rect.width > 0 && rect.height > 0 && rect.bottom >= 0 && rect.top <= (window.innerHeight || document.documentElement.clientHeight);
      
      if (!isVisible) return;

      const tag = el.tagName.toLowerCase();
      const text = (el.innerText || el.getAttribute("aria-label") || el.getAttribute("placeholder") || el.value || "").trim().substring(0, 40);

      elements.push({
        id: index + 1,
        tag: tag,
        type: el.getAttribute("type") || "",
        text: text,
        selector: generateUniqueSelector(el)
      });
      count++;
    });

    return elements;
  }

  function handleClick(selector, text) {
    let target = null;
    if (selector) {
      target = document.querySelector(selector);
    }
    if (!target && text) {
      const candidates = Array.from(document.querySelectorAll("button, a, [role='button']"));
      target = candidates.find(el => (el.innerText || "").toLowerCase().includes(text.toLowerCase()));
    }

    if (!target) {
      return { success: false, error: `Could not find click target for selector: ${selector || text}` };
    }

    target.scrollIntoView({ behavior: "smooth", block: "center" });
    target.focus();
    target.click();

    return {
      success: true,
      message: `Clicked element <${target.tagName.toLowerCase()}> "${(target.innerText || "").substring(0, 30)}"`
    };
  }

  function handleFill(selector, value, submit) {
    if (!selector) {
      return { success: false, error: "Selector required to fill input" };
    }

    const input = document.querySelector(selector);
    if (!input) {
      return { success: false, error: `Input element not found: ${selector}` };
    }

    input.scrollIntoView({ behavior: "smooth", block: "center" });
    input.focus();
    input.value = value || "";

    // Dispatch input & change events for reactive frameworks (React, Vue, etc.)
    input.dispatchEvent(new Event("input", { bubbles: true }));
    input.dispatchEvent(new Event("change", { bubbles: true }));

    if (submit) {
      const form = input.closest("form");
      if (form) {
        form.dispatchEvent(new Event("submit", { bubbles: true, cancelable: true }));
        if (typeof form.submit === "function") {
          form.submit();
        }
      } else {
        input.dispatchEvent(new KeyboardEvent("keydown", { key: "Enter", bubbles: true }));
      }
    }

    return {
      success: true,
      message: `Filled "${selector}" with value length ${value ? value.length : 0}`
    };
  }

  function handleEditElement(selector, html, text) {
    if (!selector) {
      return { success: false, error: "Selector required to edit element" };
    }
    const target = document.querySelector(selector);
    if (!target) {
      return { success: false, error: `Element not found: ${selector}` };
    }
    if (html !== undefined && html !== null) {
      target.innerHTML = html;
    } else if (text !== undefined && text !== null) {
      target.innerText = text;
    }
    // Also support contentEditable elements (e.g. Notion, Google Docs web canvas, rich editors)
    if (target.isContentEditable || target.getAttribute("contenteditable") === "true") {
      target.dispatchEvent(new Event("input", { bubbles: true }));
    }
    return {
      success: true,
      message: `Updated content of element <${target.tagName.toLowerCase()}> "${selector}"`
    };
  }

  function generateUniqueSelector(el) {
    if (el.id) return `#${CSS.escape(el.id)}`;
    if (el.name) return `${el.tagName.toLowerCase()}[name="${CSS.escape(el.name)}"]`;
    if (el.getAttribute("aria-label")) return `${el.tagName.toLowerCase()}[aria-label="${CSS.escape(el.getAttribute("aria-label"))}"]`;
    // Fallback: tag + nth-of-type index for disambiguation
    const siblings = Array.from(el.parentElement?.children || []).filter(c => c.tagName === el.tagName);
    const index = siblings.indexOf(el) + 1;
    const parentSelector = el.parentElement?.id ? `#${CSS.escape(el.parentElement.id)} ` : "";
    return `${parentSelector}${el.tagName.toLowerCase()}:nth-of-type(${index})`;
  }
})();

