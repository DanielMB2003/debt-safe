from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.api.routes.pages import router as pages_router
from app.api.routes.debt_api import router as debt_api_router

app = FastAPI(title=settings.app_name)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(pages_router)
app.include_router(debt_api_router)