from fastapi import APIRouter, Form, UploadFile, Depends
from app.services import auth
from app.dependencies import get_current_user


router = APIRouter(prefix="/auth", tags=["auth"]) #dependencies=[Depends(get_current_user)] for all API in route

@router.post("/register")
def login(username: str = Form(), password: str = Form()):
    return auth.register(username, password)

@router.post("/login")
def login(username: str = Form(), password: str = Form()):
    return auth.login(username, password)

# Secure Endpoint
@router.post("/upload")
async def upload(file: UploadFile, current_user=Depends(get_current_user)):
    contents = await file.read()
    return {"filename": file.filename, "size": len(contents)}