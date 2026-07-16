from fastapi import APIRouter
from app.routers.ingest import JOB_STATUS, JOB_RESULTS
from app.schemas.main import ResultResponse
from app.core.exceptions import AppException

router = APIRouter(prefix="/results", tags=["results"])

@router.get("/{job_id}", response_model=ResultResponse)
async def get_result(job_id: str):
    if job_id not in JOB_STATUS:
        raise AppException.not_found("Job not found")

    return {
        "job_id": job_id,
        "status": JOB_STATUS[job_id],
        "result": JOB_RESULTS.get(job_id),
    }