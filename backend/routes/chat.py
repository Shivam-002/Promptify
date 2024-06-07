# route/authentication.py
from fastapi import APIRouter

router = APIRouter()


@router.post("/create")
def create_chat():
    # TODO : Create an API to create a chat in the mongoDB
    # the chat should be one per user
    pass


@router.post("/insert-message")
def insert_message():
    # TODO : Create an API to insert a message in the chat
    # take care of AI message or user message
    # you can also create a model as required
    pass


@router.get("/get-messages")
def get_messages():
    # TODO : Create an API to get all the messages in the chat
    pass


@router.get("/get-message")
def get_message():
    # TODO : Create an API to get a specific message in the chat
    pass


@router.delete("/delete-message")
def delete_message():
    # TODO : Create an API to delete a specific message in the chat
    pass


@router.delete("/delete-chat")
def delete_chat():
    # TODO : Create an API to delete the chat
    pass
