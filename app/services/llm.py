import logging
from google import genai
from google.genai.errors import APIError
from fastapi import status
from fastapi.responses import StreamingResponse
from app.core.exceptions import AppException

logger = logging.getLogger(__name__)
client = genai.Client()

system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
"""

user_prompt_prefix = """
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.

"""

def stream_text(model: str, contents: str):
    try:
        for chunk in client.models.generate_content_stream(
            model=model,
            contents=contents,
        ):
            if chunk.text:
                yield f"data: {chunk.text}\n\n"
    except APIError as e:
        logger.error(f"Gemini API error during streaming: {e}")
        yield f"event: error\ndata: Gemini API error: {e.message if hasattr(e, 'message') else str(e)}\n\n"
    except Exception as e:
        logger.error(f"Unexpected error during stream generation: {e}")
        yield f"event: error\ndata: An error occurred while generating the summary.\n\n"

def create_stream_response(model: str, contents: str):
    try:
        generator = stream_text(
            model=model,
            contents=contents
        )
        return StreamingResponse(generator, media_type="text/event-stream")
    except Exception as e:
        logger.error(f"Error preparing response stream: {e}")
        raise AppException.error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "Failed to initiate response stream."
        )
