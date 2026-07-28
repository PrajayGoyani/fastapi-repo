from fastapi import APIRouter, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from google import genai

router = APIRouter(
    prefix="/llm",
    tags=["llm"]
)

client = genai.Client()

class Input(BaseModel):
    user_prompt: str

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

class SiteInput(BaseModel):
    url: str

# stream response as they arrive
@router.post("/generate-gemini", status_code=status.HTTP_200_OK)
def generate(data: Input):
    def stream_text():
        for chunk in client.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=data.user_prompt,
        ):
            if chunk.text:
                yield f"data: {chunk.text}\n\n"

    return StreamingResponse(stream_text(), media_type="text/event-stream")


@router.post("/summarise-website", status_code=status.HTTP_200_OK)
def generate(data: SiteInput):
    
    def stream_text():
        for chunk in client.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=user_prompt_prefix + data.url
        ):
            if chunk.text:
                yield f"data: {chunk.text}\n\n"

    return StreamingResponse(stream_text(), media_type="text/event-stream")
