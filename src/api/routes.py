"""API routes for agent and dashboard."""
from pathlib import Path

from fastapi import HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

from src.agent.email_agent import run_agent
from src.agent.prompts import PROBE_TRIGGER_MESSAGE
from src.db import database

from fastapi import APIRouter
router = APIRouter()


class RunAgentRequest(BaseModel):
    input: str | None = None
    probe: bool = False


class RunAgentResponse(BaseModel):
    output: str
    status: str


@router.post("/agent/run", response_model=RunAgentResponse)
def run_agent_endpoint(req: RunAgentRequest):
    try:
        input_text = PROBE_TRIGGER_MESSAGE if req.probe else (req.input or "Hello, what can you do?")
        output = run_agent(input_text)
        database.log_interaction(
            "manual" if not req.probe else "manual_probe",
            input_text[:500],
            output,
            "completed",
        )
        return RunAgentResponse(output=output, status="completed")
    except Exception as e:
        database.log_interaction("manual", req.input or "", "", "error", error_message=str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/interactions")
def list_interactions(limit: int = 50, offset: int = 0):
    return database.get_interactions(limit=limit, offset=offset)


@router.get("/")
def serve_dashboard():
    p = Path(__file__).parent.parent / "web" / "index.html"
    if p.exists():
        return FileResponse(p)
    from fastapi.responses import HTMLResponse
    return HTMLResponse("<h1>Email Draft Agent</h1><p>Dashboard UI not found.</p>")
