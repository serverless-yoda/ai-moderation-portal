from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from common.logging import CorrelationIdContext, get_logger
from domain.exceptions import ModerationFailedError
from starlette.middleware.base import BaseHTTPMiddleware

logger = get_logger(__name__)

async def moderation_failed_handler(request: Request, exc:ModerationFailedError):
    return JSONResponse(
        status_code=500,
        content={
            "error": "Moderation system fauled", "details": str(exc)
        }
    )

class CorrelationMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        cid = CorrelationIdContext.new_id()
        request.state.correlation_id = cid
        response = await call_next(request)
        response.headers["X-Correlation-ID"]  = cid
        return response
        