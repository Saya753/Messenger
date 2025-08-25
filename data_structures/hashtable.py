#کاربران

class User:
    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id
        
    def __str__(self):
        return f"{self.username} (ID:{self.user_id})"
        
class UserNode:
    def __init__(self, user):
        self.user = user
        self.next = None
    
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size
    
    def insert(self, key, user):
        index = self.hash_function(key)
        new_node = UserNode(user)
        if self.table[index] is None: # اگر ذاکت خالی باشه
            self.table[index] = new_node
        else:                                    # برخورد یعنی باکت پره پس باید بریم جلو
            new_node.next = self.table[index]
            self.table[index] = new_node
            
            # current = self.table[index]
            # while current.next:     # میریم تا آخر زنجیره
            #     if current.key == key:  # اگر کاربر از قبل وجود داشت → بروزرسانی
            #         current.user = user
            #         return
            #     current = current.next
            # current.next = new_node  # در نهایت اضافه‌کردن به انتهای لیست پیوندی
            
    def get(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.user.username == key:
                return current.user
            current = current.next 
        return None
                
    def delete(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None
        while current:
            if current.user.username == key: # کاربر پیدا شد
                if prev:                     # وسط لیست یعنی یه کاربر قبلی داره
                    prev.next = current.next
                else:                        # اول گره هست
                    self.table[index] = current.next
                return True
            prev = current
            current = current.next
        return False
    
    def display(self):    
        for i in range(self.size):
            print(f"[{i}] -> ", end="")
            current = self.table[i]
            while current:
                print(f"{current.user}", end=" -> ")
                current = current.next
            print("None")
            
    def to_list(self): # برای اینکه بیاد کاربر ها رو به صورت یک لیست مرتب کنه برای ذخیره توی فایل
        all_users = []
        for bucket in self.table: # پیماییش کل خونه های هش
            current = bucket
            while current:
                all_users.append(current.user)
                current = current.next
        return all_users