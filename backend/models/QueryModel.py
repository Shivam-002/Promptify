from pydantic import BaseModel


class QueryModel(BaseModel):
    input_prompt: str
    context: str = None
