from fastapi import APIRouter, Form, UploadFile, Depends
from app.services import auth

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
def login(username: str = Form(), password: str = Form()):
    return auth.register(username, password)

@router.post("/login")
def login(username: str = Form(), password: str = Form()):
    return auth.login(username, password)

def authenticated():
    return {}

# Secure Endpoint
@router.post("/upload")
def upload(file: UploadFile, user = Depends(authenticated)):
    contents = file.read()
    return {"filename": file.filename, "size": len(contents)}