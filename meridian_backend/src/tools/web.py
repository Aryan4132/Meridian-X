import httpx
import os
from typing import Dict, Any

def search_web(query: str) -> str:
    # 1. Primary: Use the standard DDGS wrapper
    try:
        from ddgs import DDGS
        with DDGS() as ddgs:
            results = ddgs.text(query, max_results=5)
            if results:
                lines = []
                for r in results:
                    title = r.get("title", "")
                    link = r.get("href", "")
                    body = r.get("body", "")
                    lines.append(f"Title: {title}\nURL: {link}\nSnippet: {body}\n")
                return "\n".join(lines)
    except Exception as e:
        print("DuckDuckGo wrapper search failed, attempting Tavily fallback:", e)

    # 2. Tavily Fallback if DDG returns empty or fails
    tavily_key = os.environ.get("TAVILY_API_KEY")
    if tavily_key:
        try:
            print("[Search] DuckDuckGo returned no output. Falling back to Tavily...")
            headers = {"Content-Type": "application/json"}
            payload = {"api_key": tavily_key, "query": query}
            res = httpx.post("https://api.tavily.com/search", json=payload, headers=headers, timeout=10.0)
            if res.status_code == 200:
                results = res.json().get("results", [])
                lines = []
                for r in results:
                    lines.append(f"Title: {r.get('title')}\nURL: {r.get('url')}\nContent: {r.get('content')}\n")
                if lines:
                    return "\n".join(lines)
        except Exception as e:
            return f"Web search failed (DuckDuckGo empty/failed, Tavily fallback failed): {e}"
            
    return "Web search returned no results (DuckDuckGo yielded nothing and Tavily is unconfigured or failed)."


def fetch_page(url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    with httpx.Client(follow_redirects=True) as client:
        res = client.get(url, headers=headers, timeout=15.0)
        return res.text

def parse_page(html: str) -> str:
    try:
        from selectolax.parser import HTMLParser
        parser = HTMLParser(html)
        # Strip script and style elements
        for element in parser.css('script, style, head, nav, footer'):
            element.decompose()
        text = parser.body.text(separator='\n')
        # Cleanup double newlines
        return "\n".join([line.strip() for line in text.split('\n') if line.strip()])
    except ImportError:
        # Simple regex parser fallback if selectolax failed to install
        import re
        text = re.sub(r'<script.*?</script>', '', html, flags=re.DOTALL)
        text = re.sub(r'<style.*?</style>', '', text, flags=re.DOTALL)
        text = re.sub(r'<.*?>', ' ', text)
        return "\n".join([line.strip() for line in text.split('\n') if line.strip()])

def download_file(url: str, dest: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(dest)), exist_ok=True)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }
    with httpx.stream("GET", url, headers=headers, follow_redirects=True, timeout=30.0) as r:
        r.raise_for_status()
        with open(dest, "wb") as f:
            for chunk in r.iter_bytes(chunk_size=8192):
                f.write(chunk)
    return f"Successfully downloaded file from {url} to {dest}"

def autonomous_research(topic: str, max_depth: int = 3) -> str:
    """Perform a fully autonomous search and reading crawl using DuckDuckGo to compile a research report."""
    import re
    import concurrent.futures
    from database import ingest_into_knowledge_base, get_ollama_client
    
    print(f"[Research Agent] Searching web for topic: '{topic}'...")
    search_results = search_web(topic)
    if search_results.startswith("Web search failed"):
        return search_results
        
    # Extract URLs using regex
    urls = re.findall(r"URL:\s*(https?://[^\s]+)", search_results)
    if not urls:
        return "Could not find any research URLs from search results."
        
    # Deduplicate and limit
    unique_urls = []
    for u in urls:
        if u not in unique_urls:
            unique_urls.append(u)
    unique_urls = unique_urls[:max_depth]
    
    client = get_ollama_client()
    model = os.environ.get("MERIDIAN_MODEL", "qwen2.5-coder:7b-instruct-q4_K_M")
    
    report_lines = [
        f"# Consolidated Research Report: {topic}",
        f"Sources crawled: {len(unique_urls)}\n"
    ]
    
    def crawl_and_summarize(idx: int, url: str):
        print(f"[Research Agent] Crawling source {idx}/{len(unique_urls)}: {url}")
        try:
            html = fetch_page(url)
            text = parse_page(html)
            
            # Ask Ollama to summarize the page for the topic
            prompt = (
                f"You are a research analyst. Extract and summarize the key facts, numbers, and info "
                f"specifically relevant to the topic '{topic}' from this webpage text. "
                "List them as 3-5 clear bullet points.\n\n"
                f"Source URL: {url}\n"
                f"Content:\n{text[:4000]}"
            )
            res = client.generate(model=model, prompt=prompt)
            summary = (res.response if hasattr(res, "response") else res.get("response", "")).strip()
            
            # Ingest summary into LanceDB RAG cache for subsequent agent lookups
            ingest_into_knowledge_base(url, summary, {"topic": topic, "type": "research_cache"})
            
            return idx, url, summary
        except Exception as e:
            return idx, url, f"*Crawl failed: {e}*"

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(unique_urls)) as executor:
        futures = [executor.submit(crawl_and_summarize, i, url) for i, url in enumerate(unique_urls, 1)]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
            
    # Sort results back to original crawled order
    results.sort(key=lambda x: x[0])
    
    for idx, url, summary in results:
        report_lines.append(f"### Source {idx}: {url}")
        report_lines.append(summary + "\n")
            
    return "\n".join(report_lines)

