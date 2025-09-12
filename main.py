from fastapi import FastAPI
from api.v1.routes import router
from common.error_handlers import moderation_failed_handler, CorrelationMiddleware
from domain.exceptions import ModerationFailedError

app = FastAPI(title="AI Moderation Portal")

# Middleware & error handlers
app.add_middleware(CorrelationMiddleware)
app.add_exception_handler(ModerationFailedError, moderation_failed_handler)

# Routers
app.include_router(router, prefix="/api/v1")