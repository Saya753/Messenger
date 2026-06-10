class User:
<<<<<<< HEAD
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
=======
    def __init__(self, username, user_id, password=None):
        self.username = username
        self.user_id = user_id
        self.password = password
>>>>>>> 9d89458f4f382f9116d2062a1d84b6fabd3f9449
        self.messages = []
        
    def add_message(self, message_id):
        self.messages.append(message_id)
        
    def get_messages(self):
        return self.messages
    
    def __str__(self):
        return f"{self.username} (ID: {self.user_id})"    