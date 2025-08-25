# from data_structures.stack import MessageStack

# stack = MessageStack()

# stack.push("Hello!")
# stack.push("How u doin?")
# stack.push("What's up?")

# print("Last message: ", stack.peek())
# print("All mesages: ")
# for message in stack.display():
#     print(">>", message)
# print("Deleted message: ", stack.pop())

# from data_structures.hashtable import HashTable, User

# ht = HashTable()

# ht.insert("negin", User("negin", 100))
# ht.insert("hossein", User("hossein", 101))
# ht.insert("mahta", User("mahta", 102))
# ht.insert("zeinab", User("zeinab", 103))

# print("Show table: ")
# ht.display()

# print("\nSearch negin: ", ht.get("negin"))
# print("Delete hossein: ", ht.delete("hossein"))
# print("Search mahta: ", ht.get("mahta"))
# print("Delete zeinab: ", ht.delete("zeinab"))

# from data_structures.linked_list import ReplyList

# replies = ReplyList()
# replies.add_reply("Hello")
# replies.add_reply("I'm doing well")
# replies.add_reply("where r u")

# replies.print_replies()

# print("\nAll Replies: ")
# print(replies.get_all_replies())

# from data_structures.bst import MessageBST
# from models.message import Message

# bst = MessageBST()
# bst.insert(Message(5, "negin", " Hello", "2025-06-01 17:50"))
# bst.insert(Message(3, "hossein", "Good morning", "2025-06-01 17:53"))
# bst.insert(Message(7, "negin", "What r u doing right now", "2025-06-01 17:53"))
# bst.insert(Message(6,"hossein", "I'm working on my project", "2025-06-01 17:54"))

# print(" (inorder):")
# for msg in bst.traverse_inorder():
#     print(msg)

# print("\nSearch message by ID = 6:")
# found = bst.search(6)
# if found:
#     print(found.text)

# print("\nDelete message by ID = 3")
# bst.delete(3)
# for msg in bst.traverse_inorder():
#     print(msg)

# msg = Message(1, "Hello world!", "hossein", "2025-06-01 14:00")
# msg.add_reply("Hi hossein")
# msg.add_reply("How r u doing")

# print(msg)
# print("All replies: ")
# for reply in msg.get_replies():
#     print("-", reply)

# from models.user import User

# u = User("sara", 102)
# u.add_message(1)
# u.add_message(5)

# print(u)
# print("Sent Message: ", u.get_messages())

# from storage.storage_handler import save_users, load_users, save_messages, load_messages

# users = load_users()
# messages = load_messages()

# users.append({"username": "sara", "user_id": 102, "messages": [1, 5]})
# messages.append({
#     "id": 1,
#     "text": "سلام!",
#     "sender": "sara",
#     "timestamp": "2025-06-01 14:00",
#     "replies": ["سلام علی!", "چه جالب!"]
#   })

# save_users(users)
# save_messages(messages)

from controller import AppController

def main():

    app = AppController()
   # app.private_chats = {} 

    # print("Add User📥")
    # app.add_user("Negin")
    # app.add_user("Hossein")

    # print("\nSend Message💬")
    # app.send_message("Helloooo", "Negin")
    # app.send_message("What's up", "Hossein")

    # print("\nReply to Messages📥")
    # app.reply_to_message(1, "Hi Hossein")

    # print("\n🕵️‍♂️ Messages by ID = 1: ")
    # msg = app.search_message(1)
    # if msg:
    #     print("Replyes: ", msg.get_replies())
    # else:
    #     print("Message Not Found!")

    # print("\nUsers🧑‍🤝‍🧑")
    # for u in app.get_all_users():
    #     print(u)

    # print("\nAll Messages Sorted🗂: ")
    # for m in app.get_all_messages_sorted():
    #     print(m)

    # print("\nRecent Massages🕒: ")
    # for m in app.get_latest_messages():
    #     print(m)
    
    app.add_user("negin")
    app.add_user("zeinab")
    
    # print("Registered users:")
    # for u in app.get_all_users():
    #     print("-", u.username)
    
    # msg_id = app.send_private_message("negin", "zeinab", "Test Message")
    # print("Sent msg id:", msg_id)

    # result = app.search_in_chat("negin", "zeinab", msg_id)
    # if result:
    #     print("✅ Found:", result)
    # else:
    #     print("❌ Not found")

    
    app.send_private_message("negin", "zeinab", "Hello")
    app.send_private_message("zeinab", "negin", "Hi..How u doing?")
    app.send_private_message("negin", "zeinab", "Thanks.What's up sis?")
    
    result = app.search_in_chat("negin", "zeinab", 1)
    
    if result:
        print("Message found:", result)
    else:
        print("Message not found.")
    
    # msg_id = app.send_private_message("negin", "zeinab", "Hello")
    # print("Sent message ID:", msg_id)
    # chat = app.get_or_create_private_chat("negin", "zeinab")
    # found = chat.search_message(msg_id)
    # if found:
    #     print("✅Message with id:", found)
    # else:
    #     print("❌Message not found")

    # deleted = app.delete_private_message("negin", "zeinab", 1)
    # print("✅Deleted Message: ", deleted)

    
    # chat = app.get_or_create_private_chat("negin", "zeinab")
    # print("In-order Traversal of BST:")
    # for m in chat.messages.traverse_inorder():
    #     print(f"id={m.id}, text={m.text}")

    
    # msg = app.get_private_chat_messages("negin", "zeinab")
    # for m in msg:
    #     print(f"DEBUG → ID: {m.id} | {m.sender} → {m.receiver}: {m.text}")
    
    # chat = app.get_or_create_private_chat("negin", "zeinab")
    # msg = chat.search_message(1)
    # if msg:
    #     print(f"✅ FOUND MESSAGE: {msg}")
    # else:
    #     print("❌ Message with ID 1 not found")

    
    # app.reply_to_private_message("zeinab", "negin", 1, "Halooo")
    # app.reply_to_private_message("negin", "zeinab", 3, "I have an exam tommorrow")

    # messages = app.get_private_chat_messages("negin", "zeinab")
    # print("Private Chat: ")
    # # print("Messages: ", len(messages))
    # for msg in messages:
    #     print(msg)
    #     # print("ID:", msg.id, "→", msg.text)
    #     for reply in msg.get_replies():
    #         print("↪", reply)

if __name__ == "__main__":
    main()