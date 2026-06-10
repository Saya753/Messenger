# پاسخ ها ریپلای

class ReplyNode:
    def __init__(self, text):
        self.text = text
        self.next = None
        
class ReplyList:
    def __init__(self):
        self.top = None
        
    def add_reply(self, text):
        new_node = ReplyNode(text)
        if self.top is None:
            self.top = new_node
        else:
            current = self.top
            while current.next:
                current = current.next
            current.next = new_node
            
    def get_all_replies(self):
        replies = []
        current = self.top
        while current:
            replies.append(current.text)
            current = current.next
        return replies
    
    def is_empty(self):
        return self.top is None
    
    def print_replies(self):
        current = self.top
        print("Replies: ")
        while current:
            print(f"- {current.text}")
            current = current.next