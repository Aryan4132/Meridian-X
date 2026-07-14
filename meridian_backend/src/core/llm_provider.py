import os
import json
import httpx
import logging
import asyncio
from typing import AsyncGenerator, List, Dict, Any, Optional
from database import get_mongo_db

logger = logging.getLogger("meridian_llm_provider")

def get_ollama_host() -> str:
  """
  Retrieves the Ollama host URL.
  Checks:
  1. Environment variable OLLAMA_HOST.
  2. SQLite/MongoDB user_profile database.
  """
  host = os.getenv("OLLAMA_HOST")
  if host:
    return host
    
  try:
    from database import get_user_profile
    db_host = get_user_profile("ollama_host")
    if db_host:
      return db_host
  except Exception as e:
    logger.debug(f"Failed to fetch ollama_host from database: {e}")
    
  return "http://localhost:11434"

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
  timeout_config = httpx.Timeout(30.0, connect=10.0)

  async def stream_with_retries(url: str, method: str = "POST", headers: dict = None, json_payload: dict = None) -> AsyncGenerator[bytes, None]:
    delay = 1.0
    for attempt in range(retries):
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
            
            async for line in response.iter_lines():
              if line:
                yield line.encode('utf-8') if isinstance(line, str) else line
            return
      except (httpx.RequestError, httpx.TimeoutException) as e:
        if attempt < retries - 1:
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
    fallback_model = "qwen2.5-coder:1.5b-instruct-q8_0"
    try:
      async with httpx.AsyncClient(timeout=3.0) as client:
        res = await client.get(f"{ollama_host}/api/tags")
        if res.status_code == 200:
          models_data = res.json()
          available = [m["name"] for m in models_data.get("models", [])]
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
    else:
      yield f"Error: Unsupported provider '{provider}'"
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
