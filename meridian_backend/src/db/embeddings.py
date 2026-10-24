import os
import re
import numpy as np
from typing import Optional, List, Any

# Global cache for Ollama client
_cached_ollama_client = None

def get_ollama_client_host() -> str:
    """Resolves Ollama host from environment or user profile settings."""
    host = os.environ.get("OLLAMA_HOST")
    if not host:
        try:
            from src.db.profile import get_user_profile
            db_host = get_user_profile("ollama_host")
            if db_host:
                host = str(db_host)
        except Exception:
            pass
    if not host:
        host = "http://127.0.0.1:11434"

    if host == "0.0.0.0":
        return "http://127.0.0.1:11434"
    if host.startswith("0.0.0.0:"):
        return f"http://127.0.0.1:{host.split(':')[1]}"
    if "0.0.0.0" in host:
        return host.replace("0.0.0.0", "127.0.0.1")
    if not host.startswith("http://") and not host.startswith("https://"):
        return f"http://{host}"
    return host

def get_ollama_client() -> Any:
    """Returns cached Ollama client instance."""
    global _cached_ollama_client
    if _cached_ollama_client is None:
        import ollama
        _cached_ollama_client = ollama.Client(host=get_ollama_client_host())
    return _cached_ollama_client

def _get_fallback_embedding(text: str, dim: int = 768) -> List[float]:
    """Generates a deterministic in-memory feature-hash vector when remote providers are offline."""
    if not text:
        return [0.0] * dim
    import hashlib
    words = re.findall(r"\w+", text.lower())
    vec = np.zeros(dim, dtype=np.float32)
    for word in words:
        h = int(hashlib.md5(word.encode("utf-8")).hexdigest(), 16)
        idx = h % dim
        val = 1.0 if (h % 2 == 0) else -1.0
        vec[idx] += val
    norm = np.linalg.norm(vec)
    if norm > 1e-9:
        vec = vec / norm
    return vec.tolist()

def _get_openai_embedding(text: str, api_key: str, dim: int = 768) -> Optional[List[float]]:
    """Fetches OpenAI text-embedding-3-small embedding."""
    try:
        import httpx
        url = "https://api.openai.com/v1/embeddings"
        headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
        payload = {"model": "text-embedding-3-small", "input": text, "dimensions": dim}
        res = httpx.post(url, headers=headers, json=payload, timeout=10.0)
        if res.status_code == 200:
            data = res.json()
            return data["data"][0]["embedding"]
    except Exception as e:
        print(f"[Embedding] OpenAI embedding failed: {e}")
    return None

_cached_fastembed_model = None

def get_embedding(text: str) -> Optional[List[float]]:
    """Multi-provider embedding generator (OpenAI -> Ollama -> FastEmbed -> In-Memory Fallback)."""
    if not text or not text.strip():
        return None

    if len(text) > 2000:
        text = text[:2000]

    # 1. Try OpenAI if key is present
    openai_key = os.environ.get("OPENAI_API_KEY")
    if not openai_key:
        try:
            from src.db.profile import get_user_profile
            openai_key = get_user_profile("openai_key")
        except Exception:
            pass
    if openai_key:
        vec = _get_openai_embedding(text, openai_key)
        if vec is not None:
            return vec

    # 2. Try Ollama
    embed_model = os.environ.get("EMBEDDING_MODEL")
    if not embed_model:
        try:
            from src.db.profile import get_user_profile
            embed_model = get_user_profile("embedding_model")
        except Exception:
            pass
    if not embed_model or str(embed_model).startswith("for ex"):
        embed_model = "nomic-embed-text"

    try:
        client = get_ollama_client()
        res = client.embeddings(model=embed_model, prompt=text)
        embedding = res.embedding if hasattr(res, "embedding") else (res.get("embedding") if isinstance(res, dict) else None)
        if embedding:
            return list(embedding)
    except Exception as e:
        print(f"[Embedding] Warning: Ollama embedding failed ({embed_model}): {e}")

    # 3. Fallback to FastEmbed / In-Memory Deterministic Hashing Vectorizer
    global _cached_fastembed_model
    try:
        from fastembed import TextEmbedding  # type: ignore # pyright: ignore[reportMissingImports]
        if _cached_fastembed_model is None:
            _cached_fastembed_model = TextEmbedding()
        embeddings = list(_cached_fastembed_model.embed([text]))
        if len(embeddings) > 0:
            return list(embeddings[0])
    except Exception:
        pass

    return _get_fallback_embedding(text)

def normalize_vector(v: List[float]) -> np.ndarray:
    """Normalizes vector to unit length for cosine inner product comparisons."""
    arr = np.array(v, dtype=np.float32)
    norm = np.linalg.norm(arr)
    if norm > 1e-9:
        return arr / norm
    return arr
