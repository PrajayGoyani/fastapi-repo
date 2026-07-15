import uuid
import asyncio
from typing import Any
from fastapi import APIRouter, BackgroundTasks
from app.schemas.main import Event, IngestResponse

router = APIRouter(prefix="/ingest", tags=["ingest"])

# demo in-memory stores
JOB_STATUS: dict[str, str] = {}
JOB_RESULTS: dict[str, Any] = {}


async def process_event(job_id: str, event: Event):
    JOB_STATUS[job_id] = "processing"

    # replace with real ETL / queue / load logic
    # validate, transform, write to DB logic
    await asyncio.sleep(10)

    result = {
        "user_id": event.user_id,
        "value": event.value,
        "processed": True,
    }

    JOB_RESULTS[job_id] = result
    JOB_STATUS[job_id] = "done"

@router.post("", response_model=IngestResponse)
async def ingest(event: Event, background_tasks: BackgroundTasks):
    job_id = str(uuid.uuid4())
    JOB_STATUS[job_id] = "queued"
    background_tasks.add_task(process_event, job_id, event)
    return {"job_id": job_id, "status": "queued"}

