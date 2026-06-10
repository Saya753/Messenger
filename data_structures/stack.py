#پیامهای اخیر

class StackNode:
    def __init__(self, message):
        self.message = message
        self.next = None
        
class MessageStack:
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None
    
    def push(self, message):
        new_node = StackNode(message)
        new_node.next = self.top
        self.top = new_node
        
    def pop(self): 
        if self.is_empty():
            return None
        removed = self.top
        self.top = self.top.next
        return removed.message
    
    def peek(self):
        if self.is_empty():
            return None
        return self.top.message
    
    def display(self):
        current = self.top
        result = []
        while current:
            result.append(current.message)
            current = current.next
        return result