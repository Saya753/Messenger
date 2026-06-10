# جستوجوی پیامها

class BSTNode:
    def __init__(self, message):
        self.message = message
        self.left = None
        self.right = None
class MessageBST:
    def __init__(self):
        self.root = None
        
    def insert(self, message):
        def _insert(node, message): # تابع بازگشتی برای پیدا کردن مکان مناسب در درخت BST
            if node is None: # از ریشه شروع به بررسی میکند اگر به جای خالی رسیدیم یک گره جدید میسازیم
                return BSTNode(message)
            if message.id < node.message.id:
                node.left = _insert(node.left, message) 
            else:
                node.right = _insert(node.right, message)
            return node
        self.root = _insert(self.root, message) # درج از گره شروع میشه
        
    def search(self, message_id):
        def _search(node):
            if node is None:
                return None
            if message_id == node.message.id:
                return node.message
            elif message_id < node.message.id:
                return _search(node.left)
            else:
                return _search(node.right)
        return _search(self.root)
            
    def delete(self, message_id):
        def _main_value_node(node): # تابع کمکی برای پیدا کردن کوچکترین مقدار زیردرخت راست 
            current = node          # وقتی گره دو فرزند داره و باید حذف بشه جاشو با کوچکترین گره سمت راست باید عوض کرد
            while current.left:
                current = current.left
            return current
        
        def _delete(node, message_id):
            if node is None:
                return node, False
            if message_id < node.message.id:                  # شبیه جستوجوی BST
                node.left, deleted = _delete(node.left, message_id)
            elif message_id > node.message.id:
                node.right, deleted = _delete(node.right, message_id)
            else:                                     # برای وقتی که گره پیدا شد بررسی فرزند چپ و راستش
                if node.left is None:
                    return node.right, True
                elif node.right is None:
                    return node.left, True
                temp = _main_value_node(node.right)                # برای وقتی که دو فرزند داره و temp کوچکترین گره سمت راست است
                node.message = temp.message                        # پیام این گره جایگزین گره فعلی میشه
                node.right = _delete(node.right, temp.message.id)  # temp از زیر درخت راست حذف میشه
                return node, True
            return node, deleted
        self.root, deleted = _delete(self.root, message_id)
        return deleted
        
    def traverse_inorder(self): # مرتب کردن پیامها به صورت صعودی براساس id (چپ->ریشه->راست)
        result = []             # نمایش مرتب پیامها به کاربر
        
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.message)
                _inorder(node.right)
        _inorder(self.root)
        return result