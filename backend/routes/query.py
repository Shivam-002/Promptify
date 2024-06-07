# route/query.py
from fastapi import APIRouter
from models.QueryModel import QueryModel
from main import promptify_prompt

router = APIRouter()


@router.get("/")
def query(input_prompt: str, context: str = None):
    result = promptify_prompt(input_prompt, context)
    print(result)
    return result
