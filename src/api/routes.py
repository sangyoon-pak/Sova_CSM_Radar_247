"""API routes for agent and dashboard."""
from pathlib import Path
from threading import Thread

from fastapi import HTTPException, File, UploadFile
from fastapi.responses import FileResponse
from pydantic import BaseModel
from langchain_core.callbacks import BaseCallbackHandler

from datetime import datetime

from src.agent.email_agent import run_agent
from src.agent.memory import compact_memory, refresh_learning_instructions
from src.agent.prompts import PROBE_TRIGGER_MESSAGE
from src.agent.tools.doc_upload import ingest_upload
from src.agent.tools import doc_search
from src.agent.tools.openrouter_web import run_web_search
from src.config import settings
from src.db import database
from src.api import run_state

from fastapi import APIRouter
router = APIRouter()


class RunAgentRequest(BaseModel):
    input: str | None = None
    probe: bool = False
    web: bool = False
    web_url: str | None = None


class RunAgentResponse(BaseModel):
    output: str
    status: str


class RunAgentAsyncResponse(BaseModel):
    run_id: str
    status: str


class AgentProfileRequest(BaseModel):
    vendor_name: str
    product_context: str
    role_title: str


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


def _tools_used_from_events(events: list[dict] | None) -> list[str]:
    names: list[str] = []
    seen: set[str] = set()
    for e in events or []:
        if str(e.get("type", "")) != "tool_start":
            continue
        title = str(e.get("title", ""))
        if title.startswith("Tool start:"):
            name = title.split("Tool start:", 1)[1].strip()
            if name and name not in seen:
                seen.add(name)
                names.append(name)
    return names


@router.post("/agent/run", response_model=RunAgentResponse)
def run_agent_endpoint(req: RunAgentRequest):
    try:
        input_text = PROBE_TRIGGER_MESSAGE if req.probe else (req.input or "Hello, what can you do?")
        if req.web:
            res = run_web_search(query=input_text, model=settings.llm_model_for_main, url=req.web_url)
            output = res.text or "No web search output."
        else:
            output = run_agent(input_text)
        database.log_interaction(
            "manual" if not req.probe else "manual_probe",
            input_text[:500],
            output,
            "completed",
            metadata={"tools_used": [], "events": []},
        )
        return RunAgentResponse(output=output, status="completed")
    except Exception as e:
        database.log_interaction("manual", req.input or "", "", "error", error_message=str(e))
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/agent/run_async", response_model=RunAgentAsyncResponse)
def run_agent_async_endpoint(req: RunAgentRequest):
    input_text = PROBE_TRIGGER_MESSAGE if req.probe else (req.input or "Hello, what can you do?")
    trigger_type = "manual_probe" if req.probe else "manual"
    if req.web:
        trigger_type = trigger_type + "_web"
    run_id = run_state.create_run(trigger_type=trigger_type, input_text=input_text[:500])

    def _worker():
        cb = _UITraceCallback(run_id)
        try:
            if req.web:
                run_state.add_event(run_id, "model_start", "Web search started")
                res = run_web_search(query=input_text, model=settings.llm_model_for_main, url=req.web_url)
                output = res.text or "No web search output."
                run_state.add_event(run_id, "model_end", "Web search finished", (output or "")[:1000])
            else:
                output = run_agent(input_text, callbacks=[cb])
            run_state.complete_run(run_id, output)
            run = run_state.get_run(run_id) or {}
            events = run.get("events") or []
            metadata = {
                "run_id": run_id,
                "tools_used": _tools_used_from_events(events),
                "events": events,
            }
            database.log_interaction(trigger_type, input_text[:500], output, "completed", metadata=metadata)
        except Exception as e:
            run_state.fail_run(run_id, str(e))
            run = run_state.get_run(run_id) or {}
            events = run.get("events") or []
            metadata = {
                "run_id": run_id,
                "tools_used": _tools_used_from_events(events),
                "events": events,
            }
            database.log_interaction(
                trigger_type,
                input_text[:500],
                "",
                "error",
                error_message=str(e),
                metadata=metadata,
            )

    Thread(target=_worker, daemon=True).start()
    return RunAgentAsyncResponse(run_id=run_id, status="running")


@router.get("/agent/runs/{run_id}")
def get_agent_run(run_id: str):
    run = run_state.get_run(run_id)
    if not run:
        raise HTTPException(status_code=404, detail="Run not found")
    return run


@router.get("/agent/profile")
def get_agent_profile():
    return database.get_agent_profile_settings()


@router.put("/agent/profile")
def set_agent_profile(req: AgentProfileRequest):
    try:
        return database.set_agent_profile_settings(
            vendor_name=req.vendor_name,
            product_context=req.product_context,
            role_title=req.role_title,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


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

@router.get("/kb/documents")
def list_docs(limit: int = 200, offset: int = 0):
    return database.list_kb_documents(limit=limit, offset=offset)


@router.delete("/kb/documents/{doc_id}")
def delete_kb_doc(doc_id: int):
    try:
        return database.delete_kb_document(doc_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/kb/reindex")
def reindex_kb_documents():
    """
    Rebuild search indexes from currently registered KB documents.
    Useful when uploads previously failed indexing or retrieval looks incomplete.
    """
    try:
        import json as _json

        docs = database.list_kb_documents(limit=5000, offset=0)
        paths: list[Path] = []
        updated_doc_ids: list[int] = []
        for d in docs:
            p = (d.get("path") or "").strip()
            if p and Path(p).exists():
                paths.append(Path(p))
                updated_doc_ids.append(int(d.get("id")))

        result = doc_search.index_files(paths)

        # Mark included docs as indexed (clear prior error marker).
        for d in docs:
            doc_id = int(d.get("id"))
            if doc_id not in updated_doc_ids:
                continue
            md = d.get("metadata") or {}
            if isinstance(md, str):
                try:
                    md = _json.loads(md)
                except Exception:
                    md = {}
            md["index_status"] = "indexed"
            md.pop("index_error", None)
            database.update_kb_document_metadata(doc_id, md)

        return {
            "ok": True,
            "indexed_docs": len(updated_doc_ids),
            "indexed_files": result.get("indexed_files", []),
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class RCUrlUpsertRequest(BaseModel):
    url: str
    title: str | None = None
    tags: list[str] | None = None
    scope: str | None = None
    enabled: bool = True


@router.get("/rc/urls")
def list_rc_urls(limit: int = 200, offset: int = 0, enabled_only: bool = False):
    return database.list_rc_urls(limit=limit, offset=offset, enabled_only=enabled_only)


@router.post("/rc/urls")
def upsert_rc_url(req: RCUrlUpsertRequest):
    try:
        return database.upsert_rc_url(
            url=req.url,
            title=req.title,
            tags=req.tags,
            scope=req.scope,
            enabled=req.enabled,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class RCUrlToggleRequest(BaseModel):
    enabled: bool


@router.patch("/rc/urls")
def toggle_rc_url(req: RCUrlUpsertRequest):
    """
    Update an existing RC URL's enabled flag (and optional metadata).
    """
    try:
        return database.upsert_rc_url(
            url=req.url,
            title=req.title,
            tags=req.tags,
            scope=req.scope,
            enabled=req.enabled,
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.delete("/rc/urls")
def delete_rc_url(url: str):
    try:
        return {"deleted": database.delete_rc_url(url)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


class RCDiscoverRequest(BaseModel):
    base_url: str
    max_urls: int = 10


@router.post("/rc/discover")
def discover_rc_urls(req: RCDiscoverRequest):
    """
    Discover up to N sub-URLs under the same domain using OpenRouter web search.
    This is a best-effort approximation (not a full crawler).
    """
    try:
        base = (req.base_url or "").strip()
        if not base.startswith(("http://", "https://")):
            raise ValueError("base_url must start with http:// or https://")
        n = max(1, min(int(req.max_urls or 10), 10))
        prompt = (
            "Find up to {n} important child documentation pages under this base URL. "
            "Return ONLY a JSON object: {{\"urls\": [\"https://...\", ...]}}. "
            "Prefer URLs on the same domain and within the same docs section/path.\n"
            "Base URL: {base}"
        ).format(n=n, base=base)
        res = run_web_search(query=prompt, model=settings.llm_model_for_main, url=base, max_output_tokens=1200)
        import json as _json
        import re as _re
        raw = (res.text or "").strip()
        if "```" in raw:
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        urls: list[str] = []
        try:
            data = _json.loads(raw)
            cand = data.get("urls") or []
            if isinstance(cand, list):
                urls = [str(u).strip() for u in cand if str(u).strip().startswith(("http://", "https://"))]
        except Exception:
            # fallback: extract urls from text/citations
            urls = _re.findall(r"https?://\\S+", raw)
        # Include citations as additional candidates
        urls.extend(res.citations or [])
        # Dedup + keep under same host
        from urllib.parse import urlparse
        host = urlparse(base).netloc
        seen = set()
        out: list[str] = []
        for u in urls:
            pu = urlparse(u)
            if host and pu.netloc != host:
                continue
            if u in seen:
                continue
            seen.add(u)
            out.append(u)
            if len(out) >= n:
                break
        # Upsert discovered urls as disabled by default (user can toggle on)
        for u in out:
            database.upsert_rc_url(url=u, enabled=False)
        return {"base_url": base, "discovered": out}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


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


class FeedbackRequest(BaseModel):
    interaction_id: int | None = None
    verdict: str
    note: str | None = None
    correction: str | None = None


class OptimizeRequest(BaseModel):
    interactions_keep_days: int = 30
    memory_keep_days: int = 60
    feedback_keep_days: int = 120
    purge_memory_table: bool = False
    delete_report_outputs: bool = False
    vacuum: bool = True


class ThreadCreateRequest(BaseModel):
    title: str | None = None
    pinned: bool = False


class ThreadSendRequest(BaseModel):
    thread_id: int
    text: str
    probe: bool = False


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


@router.post("/memory/feedback")
def memory_feedback(req: FeedbackRequest):
    row = database.insert_feedback(
        interaction_id=req.interaction_id,
        verdict=req.verdict,
        note=req.note,
        correction=req.correction,
    )
    try:
        refresh = refresh_learning_instructions()
    except Exception as e:
        refresh = {"updated": False, "error": str(e)}
    return {"feedback": row, "learning_refresh": refresh}


@router.post("/memory/refresh")
def memory_refresh():
    return refresh_learning_instructions()


@router.get("/maintenance/stats")
def maintenance_stats():
    return database.db_stats()


@router.post("/maintenance/optimize")
def maintenance_optimize(req: OptimizeRequest):
    return database.optimize_data_store(
        interactions_keep_days=req.interactions_keep_days,
        memory_keep_days=req.memory_keep_days,
        feedback_keep_days=req.feedback_keep_days,
        purge_memory_table=req.purge_memory_table,
        delete_report_outputs=req.delete_report_outputs,
        vacuum=req.vacuum,
    )


@router.get("/threads")
def list_threads(limit: int = 50, offset: int = 0, q: str | None = None):
    return database.list_threads(limit=limit, offset=offset, query=q)


@router.post("/threads")
def create_thread(req: ThreadCreateRequest):
    return database.create_thread(title=req.title, pinned=req.pinned)


@router.get("/threads/{thread_id}/messages")
def get_thread_messages(thread_id: int, limit: int = 200, offset: int = 0):
    return database.list_messages(thread_id=thread_id, limit=limit, offset=offset)


@router.delete("/threads/{thread_id}")
def delete_thread(thread_id: int):
    try:
        return database.delete_thread(thread_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/threads/send", response_model=RunAgentAsyncResponse)
def send_thread_message(req: ThreadSendRequest):
    text = (req.text or "").strip()
    if not text and not req.probe:
        raise HTTPException(status_code=400, detail="text is required")

    # Persist the user message immediately.
    user_msg = database.add_message(
        thread_id=req.thread_id,
        role="user",
        content=text if text else "(probe inbox)",
        metadata={"kind": "probe" if req.probe else "message"},
    )

    input_text = PROBE_TRIGGER_MESSAGE if req.probe else text
    trigger_type = "thread_probe" if req.probe else "thread_message"
    run_id = run_state.create_run(trigger_type=trigger_type, input_text=input_text[:500])

    def _worker():
        cb = _UITraceCallback(run_id)
        try:
            output = run_agent(input_text, callbacks=[cb])
            run_state.complete_run(run_id, output)
            run = run_state.get_run(run_id) or {}
            events = run.get("events") or []
            metadata = {
                "run_id": run_id,
                "tools_used": _tools_used_from_events(events),
                "events": events,
                "thread_id": req.thread_id,
                "user_message_id": user_msg.get("id"),
            }
            database.add_message(
                thread_id=req.thread_id,
                role="assistant",
                content=output,
                metadata=metadata,
            )
            database.log_interaction(
                trigger_type,
                input_text[:500],
                output,
                "completed",
                metadata=metadata,
            )
        except Exception as e:
            run_state.fail_run(run_id, str(e))
            run = run_state.get_run(run_id) or {}
            events = run.get("events") or []
            metadata = {
                "run_id": run_id,
                "tools_used": _tools_used_from_events(events),
                "events": events,
                "thread_id": req.thread_id,
                "user_message_id": user_msg.get("id"),
            }
            database.add_message(
                thread_id=req.thread_id,
                role="assistant",
                content=f"Error: {e}",
                metadata=metadata,
            )
            database.log_interaction(
                trigger_type,
                input_text[:500],
                "",
                "error",
                error_message=str(e),
                metadata=metadata,
            )

    Thread(target=_worker, daemon=True).start()
    return RunAgentAsyncResponse(run_id=run_id, status="running")


@router.get("/")
def serve_dashboard():
    p = Path(__file__).parent.parent / "web" / "index.html"
    if p.exists():
        # Prevent stale UI caching (important when iterating on a single-file dashboard).
        return FileResponse(
            p,
            headers={
                "Cache-Control": "no-store, max-age=0",
                "Pragma": "no-cache",
            },
        )
    from fastapi.responses import HTMLResponse
    return HTMLResponse("<h1>Sova — CSM Radar Agent 24/7</h1><p>Dashboard UI not found.</p>")
