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

        timestamps = request_store.get(client_ip, [])
        valid_timestamps = [ts for ts in timestamps if now - ts < TIME_WINDOW]

        if len(valid_timestamps) >= RATE_LIMIT:
            return JSONResponse(
                status_code=429,
                content={"detail": f"Too Many Requests: limit is {RATE_LIMIT} per {TIME_WINDOW} seconds."}
            )

        # Save updated timestamps
        valid_timestamps.append(now)
        request_store[client_ip] = valid_timestamps

        # Optional: cleanup if no timestamps
        if not valid_timestamps:
            request_store.pop(client_ip, None)

        return await call_next(request)

