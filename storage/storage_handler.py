import json
import os
from models.user import User
from models.message import Message
from data_structures.linked_list import ReplyList

USER_FILE = "users.json"
MESSAGE_FILE = "massage.json"

#----------Users----------

def save_users(users_list):
    data = []
    for user in users_list:
<<<<<<< HEAD
        data.append({"username": user.username, "user_id": user.user_id, "messages": user.messages})
=======
        data.append({"username": user.username, "user_id": user.user_id, "messages": user.messages, "password": user.password})
>>>>>>> 9d89458f4f382f9116d2062a1d84b6fabd3f9449
    
    with open(USER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        
def load_users():
    if not os.path.exists(USER_FILE):
        return []
    
    with open(USER_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    users = []
    for u in data:
<<<<<<< HEAD
        user = User(u["username"], u["user_id"])
=======
        user = User(u["username"], u["user_id"], u.get("password"))
>>>>>>> 9d89458f4f382f9116d2062a1d84b6fabd3f9449
        user.messages = u.get("massages", [])
        users.append(user)
    return users

#----------Messages----------

# def save_messages(message_list):
#     data = []
#     for msg in message_list:
#         data.append({
#             "id": msg.id,
#             "text": msg.text,
#             "sender": msg.sender,
#             "receiver": msg.receiver,
#             "timestamp": msg.timestamp,
#             "replies": msg.get_replies()
#         })
    
#     with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)
        
# def load_messages():
#     if not os.path.exists(MESSAGE_FILE):
#         return []
    
#     with open(MESSAGE_FILE, "r", encoding="utf-8") as f:
#         data = json.load(f)
        
#     messages = []
#     for m in data:
#         msg = Message(
#             id = m["id"],
#             text = m["text"],
#             sender = m["sender"],
#             receiver=m["receiver"],
#             timestamp = m["timestamp"]
#         )
#         for reply in m.get("replies", []):
#             msg.add_reply(reply)
#         messages.append(msg)
#     return messages

# storage_private_chats.py

import pickle
import os

CHAT_FILE = "private_chats.pkl"

def save_chats(chat_dict):
    with open(CHAT_FILE, "wb") as f:
        pickle.dump(chat_dict, f)

def load_chats():
    if not os.path.exists(CHAT_FILE):
        return {}
    with open(CHAT_FILE, "rb") as f:
        return pickle.load(f)
