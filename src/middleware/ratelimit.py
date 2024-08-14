# src/middleware/ratelimit.py
import asyncio
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 100, window_size: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests = {}

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        
        request_times = self.requests[client_ip]
        current_time = asyncio.get_event_loop().time()
        request_times = [t for t in request_times if current_time - t < self.window_size]
        
        if len(request_times) >= self.max_requests:
            return Response("Too Many Requests", status_code=429)
        
        request_times.append(current_time)
        self.requests[client_ip] = request_times
        
        response = await call_next(request)
        return response