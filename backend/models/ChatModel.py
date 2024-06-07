from pydantic import BaseModel

class CreateChatModel(BaseModel):
    user_id: str
    chat_name: str

class InsertMessage(BaseModel):
    user_id: str
    chat_id: str
    input_text: str
    output_text: str

class GetMessages(BaseModel):
    user_id: str
    chat_id: str

class GetMessage(BaseModel):
    user_id: str
    message_id: str

class DeleteMessage(BaseModel):
    user_id: str
    message_id: str

class DeleteChat(BaseModel):
    user_id: str
    chat_id: str