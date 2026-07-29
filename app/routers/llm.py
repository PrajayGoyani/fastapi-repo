from fastapi import APIRouter, status
from app.schemas.llm import LLMInput, SiteInput
from app.services import llm as llm_service

router = APIRouter(
    prefix="/llm",
    tags=["llm"]
)


@router.post("/generate-gemini", status_code=status.HTTP_200_OK)
def generate_gemini(data: LLMInput):
    return llm_service.create_stream_response(
        model="gemini-3.6-flash",
        contents=data.user_prompt
    )

@router.post("/summarise-website", status_code=status.HTTP_200_OK)
def summarise_website(data: SiteInput):
    return llm_service.create_stream_response(
        model="gemini-3.6-flash",
        contents=llm_service.user_prompt_prefix + str(data.url)
    )

