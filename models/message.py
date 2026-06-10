from data_structures.linked_list import ReplyList

class Message:
    def __init__(self, id, text, sender, receiver, timestamp):
        self.id = id
        self.text = text
        self.sender = sender
        self.receiver = receiver 
        self.timestamp = timestamp # زمان ارسال پیام
        self.replies = ReplyList()
        
    def __str__(self):
        return f"[{self.id}] {self.sender} → {self.receiver}: {self.text} @ {self.timestamp}"
        
    def add_reply(self, reply_text):
        self.replies.add_reply(reply_text)
        
    def get_replies(self):
        return self.replies.get_all_replies()