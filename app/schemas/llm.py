from pydantic import BaseModel, Field, HttpUrl


class LLMInput(BaseModel):
    user_prompt: str = Field(min_length=1, max_length=1000)


class SiteInput(BaseModel):
    url: HttpUrl