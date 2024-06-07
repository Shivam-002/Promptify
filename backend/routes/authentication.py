# route/authentication.py
from fastapi import APIRouter

router = APIRouter()

@router.get("/auth")
def authenticate():
    return {"message": "Authentication route"}