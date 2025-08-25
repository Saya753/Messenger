from data_structures.hashtable import HashTable
from data_structures.stack import MessageStack
from data_structures.bst import MessageBST
from models.user import User
from models.message import Message
from models.chat import PrivateChat
from storage.storage_handler import save_chats, load_chats
from storage.storage_handler import load_users, save_users
from datetime import datetime
import hashlib

class AppController:
    def __init__(self):
        self.users = HashTable()
        self.messages_stack = MessageStack()
        self.messages_bst = MessageBST()
        self.next_message_id = 1  # برای ID خودکار
        self.next_user_id = 1 
        self.private_chat = {}
        self.private_chats = load_chats()

        self.load_data()

    def load_data(self):
        # users
        for user in load_users():
            self.users.insert(user.username, user)
            self.next_user_id = max(self.next_user_id, user.user_id + 1)

        # messages
        # messages = load_messages()
        # for msg in messages:
        #     self.messages_stack.push(msg)
        #     self.messages_bst.insert(msg)
        #     self.next_message_id = max(self.next_message_id, msg.id + 1)
        self.private_chats = load_chats()
        
    def save_data(self):
        # all_users = self.users.to_list() 
        # all_messages = self.messages_bst.traverse_inorder()
        # save_users(all_users)
        # save_messages(all_messages)
        save_users(self.users.to_list())
        save_chats(self.private_chats)  

    
    # def add_user(self, username): 
    #     if self.users.get(username):
    #         return False
    #     new_user = User(username, user_id=len(self.users.to_list()) + 1)
    #     self.users.insert(username, new_user)
    #     self.save_data()
    #     return True
    
    def add_user(self, username):
        if self.users.get(username):
            return False  # کاربر تکراری
        new_user = User(username, self.next_user_id)
        self.users.insert(username, new_user)
        self.next_user_id += 1
        self.save_data()
        return True
    
    def delete_user(self, username):
        username = username
        user = self.users.get(username)
        if not user:
            print(f"[ERROR] User '{username}' not found!")
            return False
        self.users.delete(username)
        self.save_data()
        print(f"[INFO] User '{username}' deleted.")
        return True


    def get_all_users(self):
        return self.users.to_list()

    # def send_message(self, text, sender):
    #     user = self.users.get(sender)
    #     if not user:
    #         return False
        
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     msg = Message(self.next_message_id, text, sender, timestamp)
    #     self.messages_stack.push(msg)
    #     self.messages_bst.insert(msg)
    #     user.add_message(msg.id)
    #     self.next_message_id += 1
    #     self.save_data()
    #     return True

    # def reply_to_message(self, message_id, reply_text):
    #     msg = self.messages_bst.search(message_id)
    #     if msg:
    #         msg.add_reply(reply_text)
    #         self.save_data()
    #         return True
    #     return False

    # def get_all_messages_sorted(self):
    #     return self.messages_bst.traverse_inorder()

    # def get_latest_messages(self, count=5):
    #     return self.messages_stack.display()[:count]
    
    # def search_message(self, message_id):
    #     return self.messages_bst.search(message_id)
    
    def get_chat_key(self, user1, user2):
        return tuple(sorted([user1, user2])) 
    
    def get_or_create_private_chat(self, user1, user2):
        key = self.get_chat_key(user1, user2)
        if key not in self.private_chats:
            self.private_chats[key] = PrivateChat(user1, user2)
        return self.private_chats[key]
    
    def get_chat_messages(self, username1, username2):
        # chat = self.get_or_create_chat(username1, username2)
        # return chat.get_all_messages()
        return self.get_private_chat_messages(username1, username2)

    def send_private_message(self, sender, receiver, text):
        if not self.users.get(sender) or not self.users.get(receiver):
            return None
        chat = self.get_or_create_private_chat(sender, receiver)
        msg = chat.send_message(sender, text)
        self.save_data()
        return msg.id
    
    def get_private_chat_messages(self, user1, user2):
        chat = self.get_or_create_private_chat(user1, user2)
        return chat.get_all_messages()

    def reply_to_private_message(self, user1, user2, message_id, reply_text):
        chat = self.get_or_create_private_chat(user1, user2)
        result = chat.reply_to_message(message_id, reply_text)
        self.save_data()  # این خط ............................................................................
        return result

    def delete_private_message(self, user1, user2, message_id):
        user1 = user1
        user2 = user2
        key = self.get_chat_key(user1, user2)

        if key not in self.private_chats:
            print(f"[ERROR] Chat between '{user1}' & '{user2}' not found!")
            return False

        chat = self.private_chats[key]
        result = chat.messages.delete(message_id) 
        self.save_data()
        if result:
            print(f"[INFO] Message with id {message_id} deleted successfuly")
            self.save_data()
            return True
        else:
            print(f"[ERROR] Message with id {message_id} not found")
            return False

    def search_in_chat(self, user1, user2, message_id):
        user1 = user1
        user2 = user2
        chat = self.get_or_create_private_chat(user1, user2)
        return chat.search_message(message_id)

    def search_messages_smart(self, query, current_user):
        current_user = current_user.lower()
        results = []
        try:
            query_id = int(query)
        except ValueError:
            query_id = None

        for key, chat in self.private_chats.items():
            if current_user not in key:
                continue

            for msg in chat.get_all_messages():
                if query_id is not None and msg.id == query_id:
                    return [{
                        "chat_with": chat.user2 if chat.user1 == current_user else chat.user1,
                        "message_id": msg.id,
                        "text": msg.text,
                        "sender": msg.sender,
                        "timestamp": msg.timestamp
                    }]
                elif query.lower() in msg.text.lower():
                    results.append({
                        "chat_with": chat.user2 if chat.user1 == current_user else chat.user1,
                        "message_id": msg.id,
                        "text": msg.text,
                        "sender": msg.sender,
                        "timestamp": msg.timestamp
                    })
        return results
    
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, username, password):
        if self.users.get(username):
            return False
        hashed_pw = self.hash_password(password)
        new_user = User(username, self.next_user_id, hashed_pw)
        self.users.insert(username, new_user)
        self.next_user_id += 1
        self.save_data()
        return True
    
    def login_user(self, username, password):
        user = self.users.get(username)
        if not user:
            return False
        hashed_input = self.hash_password(password)
        return user.password == hashed_input