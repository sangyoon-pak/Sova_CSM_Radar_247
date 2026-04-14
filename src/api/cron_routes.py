"""API routes for cron job management."""
from fastapi import APIRouter
from pydantic import BaseModel

from src.scheduler.cron_manager import add_job, remove_job, toggle_job
from src.db import database

router = APIRouter()


class CronJobCreate(BaseModel):
    name: str
    cron_expression: str
    timezone: str = "Asia/Seoul"


class CronJobToggle(BaseModel):
    enabled: bool


@router.get("/cron")
def list_cron_jobs():
    return database.get_cron_jobs()


@router.post("/cron")
def create_cron_job(body: CronJobCreate):
    add_job(body.name, body.cron_expression, body.timezone)
    return {"ok": True, "name": body.name}


@router.delete("/cron/{name}")
def delete_cron_job(name: str):
    remove_job(name)
    return {"ok": True}


@router.patch("/cron/{name}")
def update_cron_job(name: str, body: CronJobToggle):
    toggle_job(name, body.enabled)
    return {"ok": True, "enabled": body.enabled}


@router.post("/cron/{name}/run")
def run_cron_job_now(name: str):
    from src.scheduler.cron_manager import _run_probe_job
    _run_probe_job(name)
    return {"ok": True, "message": "Probe job executed"}


@router.get("/cron/summary")
def cron_summary(limit: int = 20):
    return database.get_cron_run_summary(limit=limit)
