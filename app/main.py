from fastapi import FastAPI

from app.api.post_router import router
from app.core.config import settings

app=FastAPI(
    title=settings.APP_NAME
)

@app.get("/health")
def health():
    return {
        "status":"Running"
    }

app.include_router(
    router,
    prefix="/api/posts"
)