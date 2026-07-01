import os
import json
import httpx
import logging
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
  2. MongoDB user_profile collection (saved via first-run onboarding / settings UI).
  """
  env_name = f"{provider.upper()}_API_KEY"
  key = os.getenv(env_name)
  if key:
    return key
    
  # Fallback to MongoDB profiles
  try:
    db = get_mongo_db()
    col = db["user_profile"] if db is not None else None
    profile_key = f"{provider.lower()}_key"
    record = col.find_one({"key": profile_key}) if col is not None else None
    if record and "value" in record:
      return record["value"]
  except Exception as e:
    logger.debug(f"Failed to fetch {provider} key from MongoDB: {e}")
    
  return None

async def generate_completion_stream(
  messages: List[Dict[str, str]],
  provider: str,
  model: str,
  temperature: float = 0.7
) -> AsyncGenerator[str, None]:
  """
  Asynchronously streams completions from the chosen provider (Ollama, OpenAI, Anthropic, Gemini, DeepSeek).
  """
  provider = provider.lower()
  
  if provider == "ollama":
    ollama_host = get_ollama_host()
    url = f"{ollama_host}/api/chat"
    payload = {
      "model": model,
      "messages": messages,
      "options": {"temperature": temperature},
      "stream": True
    }
    
    async with httpx.AsyncClient(timeout=30.0) as client:
      async with client.stream("POST", url, json=payload) as response:
        if response.status_code != 200:
          yield f"Error: Ollama returned status code {response.status_code}"
          return
          
        async for line in response.iter_lines():
          if not line:
            continue
          try:
            data = json.loads(line)
            chunk = data.get("message", {}).get("content", "")
            if chunk:
              yield chunk
          except Exception:
            pass

  elif provider == "openai":
    api_key = get_api_key("openai")
    if not api_key:
      yield "Error: OpenAI API Key (OPENAI_API_KEY) is missing. Set it in settings."
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
    
    async with httpx.AsyncClient(timeout=30.0) as client:
      async with client.stream("POST", url, headers=headers, json=payload) as response:
        if response.status_code != 200:
          err_text = await response.aread()
          yield f"Error: OpenAI returned {response.status_code} - {err_text.decode('utf-8')}"
          return
          
        async for line in response.iter_lines():
          if not line or not line.startswith("data: "):
            continue
          line_content = line[6:].strip()
          if line_content == "[DONE]":
            break
          try:
            data = json.loads(line_content)
            chunk = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
            if chunk:
              yield chunk
          except Exception:
            pass

  elif provider in ["anthropic", "claude"]:
    api_key = get_api_key("anthropic") or get_api_key("claude")
    if not api_key:
      yield "Error: Anthropic API Key (ANTHROPIC_API_KEY) is missing. Set it in settings."
      return
      
    url = "https://api.anthropic.com/v1/messages"
    headers = {
      "x-api-key": api_key,
      "anthropic-version": "2023-06-01",
      "content-type": "application/json"
    }
    # Anthropic message model expects role to be assistant / user
    # System instructions must be supplied separately
    system_prompt = ""
    refined_messages = []
    for msg in messages:
      if msg.get("role") == "system":
        system_prompt = msg.get("content", "")
      else:
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
      
    async with httpx.AsyncClient(timeout=30.0) as client:
      async with client.stream("POST", url, headers=headers, json=payload) as response:
        if response.status_code != 200:
          err_text = await response.aread()
          yield f"Error: Anthropic returned {response.status_code} - {err_text.decode('utf-8')}"
          return
          
        async for line in response.iter_lines():
          if not line or not line.startswith("data: "):
            continue
          line_content = line[6:].strip()
          try:
            data = json.loads(line_content)
            event_type = data.get("type")
            if event_type == "content_block_delta":
              chunk = data.get("delta", {}).get("text", "")
              if chunk:
                yield chunk
          except Exception:
            pass

  elif provider == "gemini":
    api_key = get_api_key("gemini")
    if not api_key:
      yield "Error: Gemini API Key (GEMINI_API_KEY) is missing. Set it in settings."
      return
      
    # Use Gemini's OpenAI-compatible Endpoint
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
    
    async with httpx.AsyncClient(timeout=30.0) as client:
      async with client.stream("POST", url, headers=headers, json=payload) as response:
        if response.status_code != 200:
          err_text = await response.aread()
          yield f"Error: Gemini returned {response.status_code} - {err_text.decode('utf-8')}"
          return
          
        async for line in response.iter_lines():
          if not line or not line.startswith("data: "):
            continue
          line_content = line[6:].strip()
          if line_content == "[DONE]":
            break
          try:
            data = json.loads(line_content)
            chunk = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
            if chunk:
              yield chunk
          except Exception:
            pass

  elif provider == "deepseek":
    api_key = get_api_key("deepseek")
    if not api_key:
      yield "Error: DeepSeek API Key (DEEPSEEK_API_KEY) is missing. Set it in settings."
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
    
    async with httpx.AsyncClient(timeout=30.0) as client:
      async with client.stream("POST", url, headers=headers, json=payload) as response:
        if response.status_code != 200:
          err_text = await response.aread()
          yield f"Error: DeepSeek returned {response.status_code} - {err_text.decode('utf-8')}"
          return
          
        async for line in response.iter_lines():
          if not line or not line.startswith("data: "):
            continue
          line_content = line[6:].strip()
          if line_content == "[DONE]":
            break
          try:
            data = json.loads(line_content)
            chunk = data.get("choices", [{}])[0].get("delta", {}).get("content", "")
            if chunk:
              yield chunk
          except Exception:
            pass
  else:
    yield f"Error: Unsupported provider '{provider}'"
