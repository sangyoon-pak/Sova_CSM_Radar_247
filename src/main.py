"""FastAPI application - Email Draft Agent dashboard and API."""
from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.api.routes import router
from src.api.cron_routes import router as cron_router
from src.db.database import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    title="Email Draft Agent",
    description="Local Appier email assistant with grep-based doc search",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, tags=["agent"])
app.include_router(cron_router, tags=["cron"])

web_dir = Path(__file__).parent / "web"
if web_dir.exists():
    app.mount("/static", StaticFiles(directory=str(web_dir)), name="static")


@app.get("/health")
def health():
    return {"status": "ok"}
