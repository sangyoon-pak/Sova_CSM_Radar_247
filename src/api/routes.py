"""API routes for agent and dashboard."""
from pathlib import Path
from threading import Thread

from fastapi import HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_core.callbacks import BaseCallbackHandler

from datetime import datetime

from src.agent.email_agent import run_agent
from src.agent.memory import compact_memory
from src.agent.prompts import PROBE_TRIGGER_MESSAGE
from src.agent.tools.doc_upload import ingest_upload
from src.config import settings
from src.db import database
from src.api import run_state

from fastapi import APIRouter
router = APIRouter()


class RunAgentRequest(BaseModel):
    input: str | None = None
    probe: bool = False


class RunAgentResponse(BaseModel):
    output: str
    status: str


class RunAgentAsyncResponse(BaseModel):
    run_id: str
    status: str


class _UITraceCallback(BaseCallbackHandler):
    def __init__(self, run_id: str):
        self.run_id = run_id

    def on_chat_model_start(self, serialized, messages, **kwargs):
        run_state.add_event(self.run_id, "model_start", "LLM call started")

    def on_chat_model_end(self, response, **kwargs):
        text = ""
        try:
            if response.generations and response.generations[0]:
                text = str(response.generations[0][0].message.content)[:1000]
        except Exception:
            text = ""
        run_state.add_event(self.run_id, "model_end", "LLM call finished", text)

    def on_tool_start(self, serialized, input_str, **kwargs):
        name = serialized.get("name", "tool") if isinstance(serialized, dict) else "tool"
        run_state.add_event(self.run_id, "tool_start", f"Tool start: {name}", str(input_str)[:1000])

    def on_tool_end(self, output, **kwargs):
        run_state.add_event(self.run_id, "tool_end", "Tool output", str(output)[:1500])

    def on_chain_start(self, serialized, inputs, **kwargs):
        name = serialized.get("name", "chain") if isinstance(serialized, dict) else "chain"
        run_state.add_event(self.run_id, "chain_start", f"Chain start: {name}")

    def on_chain_end(self, outputs, **kwargs):
        run_state.add_event(self.run_id, "chain_end", "Chain end", str(outputs)[:1000])


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


@router.post("/agent/run_async", response_model=RunAgentAsyncResponse)
def run_agent_async_endpoint(req: RunAgentRequest):
    input_text = PROBE_TRIGGER_MESSAGE if req.probe else (req.input or "Hello, what can you do?")
    trigger_type = "manual_probe" if req.probe else "manual"
    run_id = run_state.create_run(trigger_type=trigger_type, input_text=input_text[:500])

    def _worker():
        cb = _UITraceCallback(run_id)
        try:
            output = run_agent(input_text, callbacks=[cb])
            database.log_interaction(trigger_type, input_text[:500], output, "completed")
            run_state.complete_run(run_id, output)
        except Exception as e:
            database.log_interaction(trigger_type, input_text[:500], "", "error", error_message=str(e))
            run_state.fail_run(run_id, str(e))

    Thread(target=_worker, daemon=True).start()
    return RunAgentAsyncResponse(run_id=run_id, status="running")


@router.get("/agent/runs/{run_id}")
def get_agent_run(run_id: str):
    run = run_state.get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail="Run not found")
    return run


@router.post("/docs/upload")
async def docs_upload(file: UploadFile = File(...)):
    """
    Upload a document and ingest it into the grep-based knowledge base.

    Current support:
    - .md / .txt (and other extensions are wrapped as markdown as a best-effort fallback)
    """
    try:
        result = await ingest_upload(file=file, kb_path=settings.kb_path_resolved)  # type: ignore[name-defined]
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    return result


@router.get("/interactions")
def list_interactions(limit: int = 50, offset: int = 0):
    return database.get_interactions(limit=limit, offset=offset)


@router.delete("/interactions")
def delete_interactions(before: str | None = None):
    """
    Delete interaction history.
    - If `before` is provided (ISO datetime string), delete rows with created_at < before.
    - If not provided, delete all interactions.
    """
    dt = None
    if before:
        try:
            dt = datetime.fromisoformat(before)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid 'before' datetime format. Use ISO 8601.")
    deleted = database.delete_interactions(before=dt)
    return {"deleted": deleted}


class CompactMemoryRequest(BaseModel):
    before: str | None = None
    max_interactions: int = 200


@router.post("/memory/compact")
def memory_compact(req: CompactMemoryRequest):
    """
    Summarize and delete older interactions into a compact memory note.
    - `before`: ISO datetime string; if omitted, uses now().
    - `max_interactions`: how many interactions to summarize in one call.
    """
    dt = None
    if req.before:
        try:
            dt = datetime.fromisoformat(req.before)
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid 'before' datetime format. Use ISO 8601.")
    result = compact_memory(before=dt, max_interactions=req.max_interactions)
    return result


@router.get("/")
def serve_dashboard():
    p = Path(__file__).parent.parent / "web" / "index.html"
    if p.exists():
        return FileResponse(p)
    from fastapi.responses import HTMLResponse
    return HTMLResponse("<h1>Email Draft Agent</h1><p>Dashboard UI not found.</p>")
