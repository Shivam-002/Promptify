from pymongo import MongoClient

client = MongoClient("")
db = client["promptify"]
chat_collection = db["chatbase"]
message_collection = db["messagebase"]
