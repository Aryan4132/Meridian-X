import os
import json
import httpx
import logging
import asyncio
from typing import AsyncGenerator, List, Dict, Any, Optional
from database import get_mongo_db

import re
import math

logger = logging.getLogger("meridian_llm_provider")

SECRET_REGEX_PATTERNS = [
    re.compile(r"sk-[a-zA-Z0-9]{32,}"),
    re.compile(r"ghp_[a-zA-Z0-9]{36}"),
    re.compile(r"eyJ[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}\.[a-zA-Z0-9_-]{10,}"),
]

def scan_and_redact_secrets(text: str) -> str:
    """Scans and redacts high-entropy API keys and tokens before sending to LLM APIs (SEC-11)."""
    if not text:
        return text
        
    redacted_text = text
    for pattern in SECRET_REGEX_PATTERNS:
        matches = pattern.findall(redacted_text)
        for match in matches:
            redacted_text = redacted_text.replace(match, "[REDACTED_SECRET]")
            from src.core.audit_logger import log_sensitive_action
            log_sensitive_action("SECURITY_AUDIT", "secret_redacted", {"secret_type": "high_entropy_token"}, "SUCCESS")
            
    return redacted_text

def get_ollama_host() -> str:
  """
  Retrieves the normalized Ollama host URL.
  """
  try:
    from database import get_ollama_client_host
    return get_ollama_client_host()
  except Exception:
    host = os.getenv("OLLAMA_HOST")
    if not host:
      host = "http://localhost:11434"
    if host == "0.0.0.0":
      return "http://127.0.0.1:11434"
    if host.startswith("0.0.0.0:"):
      return f"http://127.0.0.1:{host.split(':')[1]}"
    if "0.0.0.0" in host:
      return host.replace("0.0.0.0", "127.0.0.1")
    if not host.startswith("http://") and not host.startswith("https://"):
      return f"http://{host}"
    return host

def get_api_key(provider: str) -> Optional[str]:
  """
  Retrieves the API key for a provider.
  Checks:
  1. Environment variables (e.g., OPENAI_API_KEY, ANTHROPIC_API_KEY, GEMINI_API_KEY, DEEPSEEK_API_KEY).
  2. SQLite/MongoDB user_profile database (saved via first-run onboarding / settings UI).
  """
  env_name = f"{provider.upper()}_API_KEY"
  key = os.getenv(env_name)
  if key:
    return key
    
  # Fallback to database profiles (SQLite first, then MongoDB via get_user_profile)
  try:
    from database import get_user_profile
    profile_key = f"{provider.lower()}_key"
    val = get_user_profile(profile_key)
    if val is not None and val != "":
      return val
  except Exception as e:
    logger.debug(f"Failed to fetch {provider} key from database profile: {e}")
    
  return None


async def generate_completion_stream(
  messages: List[Dict[str, str]],
  provider: str,
  model: str,
  temperature: float = 0.7
) -> AsyncGenerator[str, None]:
  """
  Asynchronously streams completions from the chosen provider (Ollama, OpenAI, Anthropic, Gemini, DeepSeek).
  Includes retry logic, timeouts, and fallback behavior.
  """
  provider = provider.lower()
  retries = 3
  timeout_config = httpx.Timeout(30.0, connect=5.0, read=30.0)

  async def stream_with_retries(url: str, method: str = "POST", headers: Optional[dict] = None, json_payload: Optional[dict] = None) -> AsyncGenerator[bytes, None]:

    delay = 1.0
    for attempt in range(retries):
      # SEC-FIX: only retry requests that failed BEFORE any token was
      # delivered — retrying mid-stream re-yields already-delivered tokens,
      # duplicating output.
      delivered_any = False
      try:
        async with httpx.AsyncClient(timeout=timeout_config) as client:
          async with client.stream(method, url, headers=headers, json=json_payload) as response:
            if response.status_code != 200:
              if response.status_code in [429] or response.status_code >= 500:
                if attempt < retries - 1:
                  logger.warning(f"[{provider}] Server returned status {response.status_code}. Retrying in {delay}s...")
                  await asyncio.sleep(delay)
                  delay *= 2
                  continue
              err_content = await response.aread()
              # We yield the error message so the outer loop knows it failed
              yield f"Error: status code {response.status_code} - {err_content.decode('utf-8', errors='ignore')}".encode('utf-8')
              return
            
            async for line in response.aiter_lines():
              if line:
                delivered_any = True
                yield line.encode('utf-8') if isinstance(line, str) else line
            return
      except (httpx.RequestError, httpx.TimeoutException) as e:
        if not delivered_any and attempt < retries - 1:
          logger.warning(f"[{provider}] Network error: {e}. Retrying in {delay}s...")
          await asyncio.sleep(delay)
          delay *= 2
        else:
          yield f"Error: connection failed - {e}".encode('utf-8')
          return

  async def run_ollama_fallback() -> AsyncGenerator[str, None]:
    ollama_host = get_ollama_host()
    url = f"{ollama_host}/api/chat"
    
    # Resolve fallback model
    fallback_model = "llama3.2:3b"
    try:
      async with httpx.AsyncClient(timeout=3.0) as client:
        res = await client.get(f"{ollama_host}/api/tags")
        if res.status_code == 200:
          models_data = res.json()
          available = [
            m["name"] for m in models_data.get("models", []) 
            if m.get("size", 0) > 1000 and ":cloud" not in m.get("name", "").lower() and "cloud" not in m.get("name", "").lower()
          ]
          if available:
            for am in available:
              if "qwen" in am or "llama" in am:
                fallback_model = am
                break
            else:
              fallback_model = available[0]
    except Exception:
      pass

    yield f"\n[System Warning: Remote provider '{provider}' failed. Falling back to local Ollama '{fallback_model}'...]\n"
    
    payload = {
      "model": fallback_model,
      "messages": messages,
      "options": {"temperature": temperature},
      "stream": True
    }
    
    async for line_bytes in stream_with_retries(url, json_payload=payload):
      line = line_bytes.decode('utf-8', errors='ignore').strip()
      if line.startswith("Error:"):
        yield f"\n[System Error: Ollama fallback also failed: {line}]\n"
        return
      try:
        data = json.loads(line)
        chunk = data.get("message", {}).get("content", "")
        if chunk:
          yield chunk
      except Exception:
        pass

  # --- Provider Specific Implementations ---

  if provider == "ollama":
    ollama_host = get_ollama_host()
    url = f"{ollama_host}/api/chat"
    payload = {
      "model": model,
      "messages": messages,
      "options": {"temperature": temperature},
      "stream": True
    }
    
    generator = stream_with_retries(url, json_payload=payload)
    try:
      async for line_bytes in generator:
        line = line_bytes.decode('utf-8', errors='ignore').strip()
        if line.startswith("Error:"):
          yield f"Error: Ollama stream failed. {line}"
          return
        try:
          data = json.loads(line)
          chunk = data.get("message", {}).get("content", "")
          if chunk:
            yield chunk
        except Exception:
          pass
    finally:
      await generator.aclose()

  else:
    # Remote Providers (OpenAI, Anthropic, Gemini, DeepSeek)
    url = ""
    headers = {}
    payload = {}
    
    if provider == "openai":
      api_key = get_api_key("openai")
      if not api_key:
        err_msg = "Error: OpenAI API Key is missing."
        logger.error(err_msg)
        yield err_msg
        return
      url = "https://api.openai.com/v1/chat/completions"
      headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
      }
      payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": True
      }

    elif provider in ["anthropic", "claude"]:
      api_key = get_api_key("anthropic") or get_api_key("claude")
      if not api_key:
        err_msg = "Error: Anthropic API Key is missing."
        logger.error(err_msg)
        yield err_msg
        return
      url = "https://api.anthropic.com/v1/messages"
      headers = {
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
      }
      system_prompt = ""
      refined_messages = []
      for msg in messages:
        if msg.get("role") == "system":
          system_prompt = msg.get("content", "")
        elif msg.get("role") in ("user", "assistant"):
          refined_messages.append({
            "role": msg.get("role"),
            "content": msg.get("content")
          })
      payload = {
        "model": model,
        "messages": refined_messages,
        "max_tokens": 4096,
        "temperature": temperature,
        "stream": True
      }
      if system_prompt:
        payload["system"] = system_prompt

    elif provider == "gemini":
      api_key = get_api_key("gemini")
      if not api_key:
        err_msg = "Error: Gemini API Key is missing."
        logger.error(err_msg)
        yield err_msg
        return
      url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"
      headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
      }
      payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": True
      }

    elif provider == "deepseek":
      api_key = get_api_key("deepseek")
      if not api_key:
        err_msg = "Error: DeepSeek API Key is missing."
        logger.error(err_msg)
        yield err_msg
        return
      url = "https://api.deepseek.com/chat/completions"
      headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
      }
      payload = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
        "stream": True
      }
    elif provider in ["custom", "custom_openai", "local_openai", "llama_cpp", "vllm", "lmstudio"]:
      # Universal Custom Provider (llama.cpp, vLLM, LM Studio, LocalAI, OpenRouter, HuggingFace, custom proxies)
      from database import get_user_profile
      custom_base = (
          os.getenv("CUSTOM_LLM_BASE_URL") 
          or os.getenv(f"{provider.upper()}_BASE_URL")
          or get_user_profile("custom_llm_base_url") 
          or "http://localhost:8000/v1"
      )
      url = custom_base if custom_base.endswith("/chat/completions") else f"{custom_base.rstrip('/')}/chat/completions"
      api_key = get_api_key(provider) or os.getenv("CUSTOM_LLM_API_KEY") or get_user_profile("custom_llm_api_key") or "bearer-token-placeholder"

      headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
      }
      payload = {
        "model": model or get_user_profile("custom_llm_model") or "default",
        "messages": messages,
        "temperature": temperature,
        "stream": True
      }

    else:
      # Universal Dynamic Vault Provider (Groq, OpenRouter, Mistral, Together, Perplexity, etc.)
      api_key = get_api_key(provider)
      if api_key:
        custom_base = os.getenv(f"{provider.upper()}_API_KEY_BASE_URL") or os.getenv(f"{provider.upper()}_BASE_URL")
        if custom_base:
          url = custom_base if custom_base.endswith("/chat/completions") else f"{custom_base.rstrip('/')}/chat/completions"
        elif provider == "groq":
          url = "https://api.groq.com/openai/v1/chat/completions"
        elif provider == "openrouter":
          url = "https://openrouter.ai/api/v1/chat/completions"
        elif provider == "mistral":
          url = "https://api.mistral.ai/v1/chat/completions"
        elif provider == "together":
          url = "https://api.together.xyz/v1/chat/completions"
        elif provider == "perplexity":
          url = "https://api.perplexity.ai/chat/completions"
        else:
          url = f"https://api.{provider}.com/v1/chat/completions"

        headers = {
          "Authorization": f"Bearer {api_key}",
          "Content-Type": "application/json"
        }
        payload = {
          "model": model,
          "messages": messages,
          "temperature": temperature,
          "stream": True
        }
      else:
        yield f"Error: Unsupported provider '{provider}'. Please add API key or set Custom Base URL in Settings."
        return

    # Execute remote call
    success = False
    err_msg = ""
    
    generator = stream_with_retries(url, headers=headers, json_payload=payload)
    try:
      async for line_bytes in generator:
        line = line_bytes.decode('utf-8', errors='ignore').strip()
        if line.startswith("Error:"):
          err_msg = line
          break
        
        # Process chunks based on provider format
        if provider == "anthropic":
          if line.startswith("data: "):
            line = line[6:].strip()
          try:
            data = json.loads(line)
            if data.get("type") == "content_block_delta":
              chunk = data.get("delta", {}).get("text", "")
              if chunk:
                success = True
                yield chunk
          except Exception:
            pass
        else: # OpenAI, Gemini, DeepSeek compatible formats
          if line.startswith("data: "):
            line = line[6:].strip()
          if line == "[DONE]":
            break
          try:
            data = json.loads(line)
            chunk = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
            if chunk:
              success = True
              yield chunk
          except Exception:
            pass
            
    except Exception as exc:
      err_msg = f"Error: Exception during stream: {exc}"
    finally:
      await generator.aclose()

    if not success:
      # If we yielded nothing and encountered an error, raise the error
      logger.error(f"Remote provider {provider} stream call failed: {err_msg}")
      yield f"Error: Remote provider {provider} call failed: {err_msg}"


async def call_llm(
  messages: List[Dict[str, str]],
  provider: Optional[str] = None,
  model: Optional[str] = None,
  temperature: float = 0.7
) -> str:
  """
  Unified non-streaming completion call for any provider.
  Automatically redacts sensitive secrets in messages.
  Resolves provider/model defaults from database if not supplied.
  """
  sanitized_messages = []
  for msg in messages:
    content = msg.get("content", "")
    sanitized_messages.append({
      **msg,
      "content": scan_and_redact_secrets(content)
    })
  
  if not provider or not model:
    try:
      from database import get_brain_model, get_model_source
      if not model:
        model = get_brain_model()
      if not provider:
        source = get_model_source()
        provider = "ollama" if source == "local" else "openrouter"
    except Exception:
      provider = provider or "ollama"
      model = model or "llama3.2:3b"
      
  chunks = []
  async for chunk in generate_completion_stream(sanitized_messages, provider=provider, model=model, temperature=temperature):
    chunks.append(chunk)
  return "".join(chunks)

def call_llm_sync(
  messages: List[Dict[str, str]],
  provider: Optional[str] = None,
  model: Optional[str] = None,
  temperature: float = 0.7
) -> str:
  """
  Synchronous wrapper for call_llm.
  """
  try:
    loop = asyncio.get_running_loop()
  except RuntimeError:
    loop = None

  if loop and loop.is_running():
    import concurrent.futures
    with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
      return pool.submit(lambda: asyncio.run(call_llm(messages, provider, model, temperature))).result()
  else:
    return asyncio.run(call_llm(messages, provider, model, temperature))

