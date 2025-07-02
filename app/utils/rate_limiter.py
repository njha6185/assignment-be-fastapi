import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse

# Configuration
RATE_LIMIT = 15        # Max requests
TIME_WINDOW = 60      # Time window in seconds

request_store = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        now = time.time()

        if client_ip not in request_store:
            request_store[client_ip] = []

        request_store[client_ip] = [ts for ts in request_store[client_ip] if now - ts < TIME_WINDOW]

        if len(request_store[client_ip]) >= RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"detail": f"Too Many Requests: limit is {RATE_LIMIT} per {TIME_WINDOW} seconds."}
            )

        request_store[client_ip].append(now)
        return await call_next(request)
