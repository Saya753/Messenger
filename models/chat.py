from data_structures.bst import MessageBST
from data_structures.linked_list import ReplyList
from models.message import Message
from datetime import datetime

class PrivateChat:
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2
        self.messages = MessageBST()
        self.next_massage_id = 1
        
    def send_message(self, sender, text):
        receiver = self.user2 if sender == self.user1 else self.user1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = Message(self.next_massage_id, text, sender, receiver, timestamp)
        self.messages.insert(msg)  # داخل درخت bst
        self.next_massage_id += 1  # ای دی برای پیام بعدی
        return msg
        
    def get_all_messages(self):
        return self.messages.traverse_inorder()
    
    def search_message(self, msg_id):
        return self.messages.search(msg_id)
    
    def reply_to_message(self, msg_id, reply_text):
        msg = self.messages.search(msg_id)
        if msg:
            print(f"[DEBUG] Reply to {msg.id}: {reply_text}")
            msg.add_reply(reply_text)
            return True
        else:
            print(f"[ERROR] Message with id:  {msg_id} not found")
        return False