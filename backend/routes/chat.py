# chat.py
from fastapi import APIRouter, HTTPException
from bson import ObjectId
import datetime
import uuid

from config.db import chat_collection, message_collection
from models.ChatModel import CreateChatModel, InsertMessage, GetMessages, GetMessage, DeleteMessage, DeleteChat

router = APIRouter()

# Helper function to convert BSON ObjectId to str
def object_id_str(o):
    return str(o) if isinstance(o, ObjectId) else o

@router.post("/create")
def create_chat(chat: CreateChatModel):
    chat_id = str(uuid.uuid4())
    existing_chat = chat_collection.find_one({"user_id": chat.user_id, "chat_name": chat.chat_name})
    if existing_chat:
        raise HTTPException(status_code=400, detail="Chat already exists for this user")

    new_chat = {
        "user_id": chat.user_id,
        "chat_id": chat_id,
        "chat_name": chat.chat_name,
        "created_at": datetime.datetime.utcnow()
    }
    result = chat_collection.insert_one(new_chat)
    return {"chat_id": chat_id}

@router.post("/insert-message")
def insert_message(message: InsertMessage):
    chat = chat_collection.find_one({"user_id": message.user_id, "chat_id": message.chat_id})
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")

    message_id = str(uuid.uuid4())
    current_datetime = datetime.datetime.now()
    new_message = {
        "user_id": message.user_id,
        "message_id": message_id,
        "chat_id": message.chat_id,
        "input_text": message.input_text,
        "output_text": message.output_text,
        "timestamp": current_datetime.timestamp()
    }
    result = message_collection.insert_one(new_message)
    return {"message_id": message_id}

@router.get("/get-messages")
def get_messages(messages: GetMessages):
    messages = list(message_collection.find({"user_id": messages.user_id, "chat_id": messages.chat_id}))
    if not messages:
        raise HTTPException(status_code=404, detail="Messages not found")

    return {"messages": [{**message, "_id": object_id_str(message["_id"])} for message in messages]}

@router.get("/get-message")
def get_message(message: GetMessage):
    message = message_collection.find_one({"user_id": message.user_id, "message_id": message.message_id})
    if not message:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"message": {**message, "_id": object_id_str(message["_id"])}}

@router.delete("/delete-message")
def delete_message(message: DeleteMessage):
    result = message_collection.delete_one({"user_id": message.user_id, "message_id": message.message_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Message not found")

    return {"status": "Message deleted"}

@router.delete("/delete-chat")
def delete_chat(chat: DeleteChat):
    chat_result = chat_collection.delete_one({"user_id": chat.user_id, "chat_id": chat.chat_id})
    if chat_result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Chat not found")

    message_collection.delete_many({"user_id": chat.user_id, "message_id": chat.chat_id})
    return {"status": "Chat and associated messages deleted"}
