import time
import httpx
import logging
from typing import Dict, List, Any, Optional

class ExperimentRunner:
    """
    One-Click Experiment Runner (🧪)
    Spins up temporary test calls against API endpoints with isolated auth headers,
    validates response status codes and schema definitions, and produces pass/fail matrix reports.
    """
    def __init__(self, default_base_url: str = "http://127.0.0.1:4132"):
        self.default_base_url = default_base_url

    async def run_experiment(
        self,
        endpoint: str,
        method: str = "GET",
        headers: Optional[Dict[str, str]] = None,
        payload: Optional[Dict[str, Any]] = None,
        expected_status: int = 200,
        expected_schema_keys: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Runs isolated API experiment without mutating git workspace state."""
        url = f"{self.default_base_url}{endpoint}" if endpoint.startswith("/") else endpoint
        req_headers = headers or {}
        req_headers.setdefault("User-Agent", "Meridian-Experiment-Runner/1.0")

        start_time = time.time()
        result = {
            "endpoint": endpoint,
            "method": method.upper(),
            "expected_status": expected_status,
            "timestamp": start_time,
            "passed": False,
            "errors": []
        }

        async with httpx.AsyncClient(timeout=5.0) as client:
            try:
                if method.upper() == "GET":
                    resp = await client.get(url, headers=req_headers)
                elif method.upper() == "POST":
                    resp = await client.post(url, headers=req_headers, json=payload or {})
                elif method.upper() == "DELETE":
                    resp = await client.delete(url, headers=req_headers)
                else:
                    resp = await client.request(method, url, headers=req_headers, json=payload)

                elapsed_ms = round((time.time() - start_time) * 1000, 2)
                result["actual_status"] = resp.status_code
                result["response_time_ms"] = elapsed_ms

                if resp.status_code != expected_status:
                    result["errors"].append(f"Expected status {expected_status}, got {resp.status_code}.")

                try:
                    json_data = resp.json()
                    result["response_body"] = json_data
                    if expected_schema_keys:
                        missing = [k for k in expected_schema_keys if k not in json_data]
                        if missing:
                            result["errors"].append(f"Missing schema keys in response: {missing}")
                except Exception:
                    result["response_text"] = resp.text[:500]

                result["passed"] = len(result["errors"]) == 0

            except Exception as err:
                result["errors"].append(f"Network / Execution error: {err}")
                result["passed"] = False

        return result
