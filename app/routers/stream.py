from pathlib import Path
from fastapi import APIRouter, WebSocket
from fastapi.responses import StreamingResponse, FileResponse

router = APIRouter(prefix="/stream", tags=["Stream", "WebSocket"])


BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_PATH = BASE_DIR / "report.pdf"

# StreamingResponse — send data in chunks
@router.get("")
async def stream():
    async def generate():
        for i in range(10):
            yield f"data: chunk {i}\n\n"
    return StreamingResponse(generate(), media_type="text/event-stream")

@router.get("/download")
async def download():
    return FileResponse(
        path=REPORT_PATH,
        filename="report.pdf",
        media_type="application/pdf",
    )

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Echo: {data}")
