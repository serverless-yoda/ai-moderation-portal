from fastapi import FastAPI
from api.v1.routes import router

app = FastAPI(title="AI Moderation Portal")
app.include_router(router, prefix="/api/v1")