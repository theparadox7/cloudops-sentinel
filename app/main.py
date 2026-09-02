from fastapi import FastAPI

from app.api.v1.health import router as health_router
from app.core.config import settings
from app.router.organization import router as organization_router

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
)

app.include_router(
    organization_router,
)