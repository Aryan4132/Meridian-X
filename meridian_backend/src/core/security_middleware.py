import logging
from typing import Callable, List, Optional
from fastapi import Request, Response, status
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

logger = logging.getLogger("meridian_security")

# Default CORS allowed origins
DEFAULT_ALLOWED_ORIGINS = {
    "tauri://localhost",
    "https://tauri.localhost",
    "http://tauri.localhost",
    "http://localhost:5173",
    "http://localhost:4132",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:4132",
}

class HTTPSecurityHeadersMiddleware(BaseHTTPMiddleware):
    """Injects standard HTTP security headers on all responses (SEC-21)."""
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "default-src 'self'"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response

class MaxBodySizeMiddleware(BaseHTTPMiddleware):
    """
    Rejects requests with Content-Length larger than max_bytes (default 10MB).
    Mitigates DoS and memory exhaustion attacks (SEC-03).
    """
    def __init__(self, app, max_bytes: int = 10_485_760):  # 10 MB
        super().__init__(app)
        self.max_bytes = max_bytes

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        content_length = request.headers.get("content-length")
        if content_length:
            try:
                length_int = int(content_length)
                if length_int > self.max_bytes:
                    logger.warning(
                        f"[SECURITY] Request body size {length_int} bytes exceeds limit of {self.max_bytes} bytes. "
                        f"Path: {request.url.path}, IP: {request.client.host if request.client else 'unknown'}"
                    )
                    return JSONResponse(
                        status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                        content={
                            "detail": f"Payload too large. Maximum request body size is {self.max_bytes // (1024 * 1024)}MB."
                        }
                    )
            except ValueError:
                pass

        return await call_next(request)


class TrustedOriginMiddleware(BaseHTTPMiddleware):
    """
    Validates Origin/Referer headers on state-mutating requests (POST/PUT/DELETE/PATCH).
    Mitigates CSRF and unauthorized cross-origin requests from non-browser clients (SEC-06).
    """
    def __init__(self, app, allowed_origins: Optional[set] = None):
        super().__init__(app)
        self.allowed_origins = allowed_origins or DEFAULT_ALLOWED_ORIGINS

    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        # Only validate state-mutating methods
        if request.method in ("POST", "PUT", "DELETE", "PATCH"):
            origin = request.headers.get("origin")
            referer = request.headers.get("referer")

            # Check Origin if present
            if origin and origin.lower() not in self.allowed_origins:
                logger.warning(
                    f"[SECURITY] Rejected untrusted Origin '{origin}'. "
                    f"Path: {request.url.path}, IP: {request.client.host if request.client else 'unknown'}"
                )
                return JSONResponse(
                    status_code=status.HTTP_403_FORBIDDEN,
                    content={"detail": f"Access forbidden. Untrusted origin header: {origin}"}
                )

            # Fallback to Referer check if no Origin header
            if not origin and referer:
                matched = any(referer.lower().startswith(allowed.lower()) for allowed in self.allowed_origins)
                if not matched:
                    logger.warning(
                        f"[SECURITY] Rejected untrusted Referer '{referer}'. "
                        f"Path: {request.url.path}, IP: {request.client.host if request.client else 'unknown'}"
                    )
                    return JSONResponse(
                        status_code=status.HTTP_403_FORBIDDEN,
                        content={"detail": f"Access forbidden. Untrusted referer header."}
                    )

        return await call_next(request)


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    """
    Injects standard security response headers:
    nosniff, DENY frame options, referrer-policy, XSS protection (SEC-21).
    """
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        response: Response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-XSS-Protection"] = "1; mode=block"
        return response
