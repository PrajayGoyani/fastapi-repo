from fastapi import APIRouter, Request, UploadFile, Depends
from pydantic import BaseModel

from app.services import auth
from app.dependencies import get_current_user
from app.core.limiter import limiter


router = APIRouter(prefix="/auth", tags=["auth"]) # dependencies=[Depends(get_current_user)] to secure all API routes

class Register(BaseModel):
    username: str
    password: str

class Login(Register):
    pass

@router.post("/register")
@limiter.limit("5/minite")
def login(request: Request, data: Register):
    # return request.client
    request_data = data.__dict__
    return auth.register(**request_data)

@router.post("/login")
@limiter.limit("5/minute")
def login(request: Request, data: Login):
    # return request.client
    request_data = data.__dict__
    return auth.login(**request_data)

# Secure Endpoint
@router.post("/upload")
async def upload(file: UploadFile, current_user=Depends(get_current_user)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}