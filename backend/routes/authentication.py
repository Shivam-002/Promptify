# route/authentication.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/authenticate")
def authenticate():
    return {"message": "Authentication route"}
