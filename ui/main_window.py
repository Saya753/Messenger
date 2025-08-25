import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Listbox, Scrollbar, END
#مسیج باکس برای نمایش چنجره
#  پیام مثللا خطا در ورود یا ثبت نام موقثیت داشت
#سیمپل برای ورودی
# تاپ برای بازکردن یک پنجره جدید رو برنامه اصلی
# لیست برای لیست انتخابی
# اسکرول همون نوار#
from controller import AppController
#در اپ کنترلر عمل ثبت نام و ارسال پیام
# ریپلای و... صورت میگیره پس باید بمونه #

import json
import os
#این دو برای قایل ها هستن #
from datetime import datetime

NOTIF_FILE = 'notifications.json'

#
#توابعی که در زیر هستند مربوط به خبر دادن به 
#کاربر هستند که چه کسی بهشون پیام داده و در چه زمانی 
# که در فایل ذخیره میشه #


#برای نمایش کسانی که پیام جدید دادن
def load_notifications():
    #زمانی که هیچ نوتیفکیشنی نیست
    if not os.path.exists(NOTIF_FILE):
        return {}
    
    # فایل را در حالت خواندن باز کردم به نام اف 
    with open(NOTIF_FILE, 'r', encoding='utf-8') as f:
        #تابع لود برای اینکه هربار که کاربر 
        # برنامه رو ران میکنه مقدار هر کلید که همون زمان
        # ایدی و اسم طرفی هست که پیام جدید گذاشته رو بالا
        # میاره#
        return json.load(f)
    
    #دقیقا برعکس لود .
    # سیو میاد کاربر جدیدی که پیام داده
    #  رو سیو میکنه برای نمایش#
    #دیتا دیکشنری از اطلاعات مورد نیاز مثل زمان ارسال و ... هست
def save_notifications(data):
    with open(NOTIF_FILE, 'w', encoding='utf-8') as f:
        #  تابع دامپ برای ذخیره ی دیتا در فایل اف
        # فالز گزاشتم تا کد گزاری نشه و هرچی هست نوشته بشه
        # ایندنت برای خوانایی کد#
        #از دامپ به جای دامپز استفاده کردم
        #  چون میخواستیم ذخیره کنیم
        json.dump(data, f, ensure_ascii=False, indent=2)


#افزودن نوت جدید
# که کاربر گیرنده و ارسال ککنده و زمان و ایدی پیام رو
# در خود داره#
def add_notification(to_user, from_user, msg_time, msg_id):
    #باصدازدن لود نوتی پیام های قبلی پاک نمیشه 
    # و یا صدا زدنش یه بار پیام های قبلی رو در فایل مجدد به علاوه
    # پیام جدید رو درفایل اضافه میکنه و ذخیره میکنه#
    notifs = load_notifications()
    #نوتیفس یک دیکشنری با کلید اسم هرکاربره و مقدارش لیستی از پیام
    #هاست
    #یوز نوتیفس برای همون کاربری هست میخوایم براش الان پیام جدید بزاریم#
    user_notifs = notifs.get(to_user, [])
    #اینجا پیام جدید به لیست کاربر اضافه میشه#
    user_notifs.append({"sender": from_user, "time": msg_time, "message_id": msg_id})
    #تا 5 پیام قبلی خواستم که اهمیت بیشتری دارن نوت بزاره#
    user_notifs = user_notifs[-5:]
    #اینجا در دیکشنری کلی نوتیفس لیست نوتیفس کاربر مورد نظر 
    # به روز رسانی میشه#
    notifs[to_user] = user_notifs
    #بعد به روز رسانی ذخیره میکنیم 
    save_notifications(notifs)

#این تابع بعد ورود هر کاربر شروع به کار میکنه
# برای اون کاربر میره چک میکنه همه ی کاربرارو که کیا بهش پیام
# دادن بعد اگه کرسی پیام داد خب بالا میاره اگه نه که
# لیست خالی برمیگردونه #
def get_user_notifications(username):
    notifs = load_notifications()
    return notifs.get(username, [])


def clear_notifications_for_user(username):
    notifs = load_notifications()
    if username in notifs:
        notifs[username] = []
        save_notifications(notifs)

class ChatAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📨Messenger")
        self.root.geometry("750x650")
        self.app = AppController()
        self.current_user = None
        self.chat_partner = None
        self.users_data = {user.username: user for user in self.app.get_all_users()}
        self.last_chats = []
        self.build_main_ui()

    def build_main_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Register", font=("Helvetica", 16, "bold")).pack(pady=20)
        tk.Button(self.root, text="Sign UP", command=self.register_user).pack(pady=10)
        tk.Button(self.root, text="Login", command=self.login_user).pack(pady=10)

    def register_user(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Sign Up", font=("Helvetica", 16, "bold")).pack(pady=20)
        tk.Label(self.root, text="Enter Your Username.", font=("Helvetica", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 14), fg='grey')
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Enter Your Username.")
        self.username_entry.bind("<FocusIn>", self.clear_username_placeholder)
        tk.Label(self.root, text="Creat A Password.", font=("Helvetica", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=10)
        self.toggle_password_button = tk.Button(self.root, text="👁️‍🗨️", command=self.toggle_password_visibility)
        self.toggle_password_button.pack(pady=5)
        tk.Button(self.root, text="Sign Up", command=self.save_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_ui).pack(pady=10)

    def clear_username_placeholder(self, event):   # بعد از این کاربر اینو کلیک کرد متن اماده پاک میشه
        if self.username_entry.get() == "Enter Your Username.":
            self.username_entry.delete(0, tk.END)
            self.username_entry.config(fg='black')

    def toggle_password_visibility(self):
        if self.password_entry.cget('show') == '*':
            self.password_entry.config(show='')
            self.toggle_password_button.config(text="🙈")
        else:
            self.password_entry.config(show='*')
            self.toggle_password_button.config(text="👁️‍🗨️")

    def save_user(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        if not username or username == "Enter Your Username.":
            messagebox.showerror("Error!", "Invalid Username!")
            return
        if not password or password == "Creat A Password.":
            messagebox.showerror("Error!", "Enter Your Password.")
            return
        if self.app.register_user(username, password):
            messagebox.showinfo("Signed up Successfully", "User Signed up Succussfully.")
            self.users_data = {user.username: user for user in self.app.get_all_users()}
            self.build_main_ui()
        else:
            messagebox.showerror("Error!", "Username Is Already Used.")

    def login_user(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text="Log In", font=("Helvetica", 16, "bold")).pack(pady=20)
        tk.Label(self.root, text="Enter Your Username.", font=("Helvetica", 12)).pack(pady=5)
        self.username_entry = tk.Entry(self.root, font=("Helvetica", 14), fg='grey')
        self.username_entry.pack(pady=10)
        self.username_entry.insert(0, "Enter Your Username.")
        self.username_entry.bind("<FocusIn>", self.clear_username_placeholder)
        tk.Label(self.root, text="Enter Your Password.", font=("Helvetica", 12)).pack(pady=5)
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 14), show="*")
        self.password_entry.pack(pady=10)
        self.toggle_password_button = tk.Button(self.root, text="👁️‍🗨️", command=self.toggle_password_visibility)
        self.toggle_password_button.pack(pady=5)
        tk.Button(self.root, text="Log In", command=self.verify_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.build_main_ui).pack(pady=10)

    def verify_user(self):
        username = self.username_entry.get().strip().lower()
        password = self.password_entry.get().strip()
        if not username or username == "Enter Your Username.":
            messagebox.showerror("Error", "Invalid Username!")
            return
        if not password or password == "Enter Your Password.":
            messagebox.showerror("Error!", "Enter Your Password.")
            return
        if self.app.login_user(username, password):
            self.current_user = username
            self.users_data = {user.username: user for user in self.app.get_all_users()}
            self.build_user_dashboard()
        else:
            messagebox.showerror("Error!", "Invalid Username or Password!")

    def build_user_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Welcome {self.current_user}", font=("Helvetica", 14, "bold")).pack(pady=10)
        self.last_chats = self.get_user_chats(self.current_user)
        tk.Button(self.root, text="✉Start New Chat", command=self.open_new_chat_window, fg="#fff", bg="#2896f7", font=("Helvetica", 12, "bold")).pack(pady=(10, 20))
        tk.Label(self.root, text="Previous Chats: ", font=("Helvetica", 13, "bold"), anchor="e").pack(fill="x")
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=False, padx=60)
        for partner in self.last_chats:
            btn = tk.Button(frame, text=partner, width=35, anchor="e", font=("Helvetica", 12), relief="ridge",
                            command=lambda p=partner: self.open_chat_with_partner(p), bg="#F0F7FF", fg="#045")
            btn.pack(pady=3, anchor="e", fill="x")
        tk.Button(self.root, text="🔍Search in Messages", command=self.search_messages).pack(pady=5)
        tk.Button(self.root, text="🚪Exit", command=self.build_main_ui).pack(pady=20)
        self.show_new_messages_notification()  # نمایش پیام‌های جدید پایین صفحه

    def show_new_messages_notification(self):
        notifications = get_user_notifications(self.current_user)
        if notifications:
            notif_text = ""
            for n in notifications:
                notif_text += f"You have a message from {n['sender']} at {n['time']}.\n"
            tk.Label(self.root, text=notif_text, fg="#1976d2", font=("Helvetica", 12, "bold")).pack(side=tk.BOTTOM, pady=5)

    def get_user_chats(self, username):
        chat_keys = list(self.app.private_chats.keys())
        partners = set()
        for key in chat_keys:
            if username in key:
                partner = key[0] if key[1] == username else key[1]
                partners.add(partner)
        return sorted(list(partners))

    def open_chat_with_partner(self, partner):
        self.chat_partner = partner
        clear_notifications_for_user(self.current_user)
        self.build_chat_ui()

    def open_new_chat_window(self):
        win = Toplevel(self.root)
        win.title("New Chat")
        win.geometry("400x350")
        tk.Label(win, text="Chose a contact from list", font=("Helvetica", 13, "bold")).pack(pady=10)
        tk.Label(win, text="Contacts List:", font=("Helvetica", 12)).pack()
        list_frame = tk.Frame(win)
        list_frame.pack(pady=5)
        scrollbar = Scrollbar(list_frame)
        scrollbar.pack(side="left", fill="y")
        all_users = [u for u in self.users_data.keys() if u != self.current_user]
        listbox = Listbox(list_frame, width=30, height=8, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
        for partner in all_users:
            listbox.insert(END, partner)
        listbox.pack(side="left")
        scrollbar.config(command=listbox.yview)
        def on_select(event=None):
            selection = listbox.curselection()
            if selection:
                partner = listbox.get(selection[0])
                win.destroy()
                self.open_chat_with_partner(partner)
        listbox.bind("<Double-Button-1>", on_select)
        tk.Label(win, text="Enter the contact username", font=("Helvetica", 12)).pack(pady=10)
        entry = tk.Entry(win, font=("Helvetica", 14), justify="right")
        entry.pack(pady=5)
        def send_to_new():
            new_partner = entry.get().strip().lower()
            if not new_partner or new_partner == self.current_user:
                messagebox.showerror("Error!", "Invalid Contact!")
                return
            win.destroy()
            self.open_chat_with_partner(new_partner)
        tk.Button(win, text="Start Chat", command=send_to_new, bg="#2196f3", fg="#fff", font=("Helvetica", 12)).pack(pady=15)
        tk.Button(win, text="Close", command=win.destroy).pack(pady=5)

    def build_chat_ui(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        tk.Label(self.root, text=f"Chat with {self.chat_partner}", font=("Helvetica", 14)).pack(pady=10)
        self.messages_box = tk.Text(self.root, width=90, height=24, state="disabled", font=("Helvetica", 12), wrap="word")
        self.messages_box.pack(pady=5)
        self.entry_msg = tk.Entry(self.root, width=65, font=("Helvetica", 13))
        self.entry_msg.pack(side=tk.LEFT, padx=5, pady=5)
        tk.Button(self.root, text="Send", command=self.send_message).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="↩Reply", command=self.reply_to_message).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="✏Edit", command=self.edit_reply_of_message).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="🗑Delete", command=self.delete_message).pack(side=tk.LEFT, padx=5)
        tk.Button(self.root, text="⬅Back", command=self.build_user_dashboard).pack(pady=10, anchor=tk.W)
        self.load_chat_messages()

    def load_chat_messages(self):
        # گرفتن لیست پیام‌ها
        messages = self.app.get_private_chat_messages(self.current_user, self.chat_partner)
        last_msg_id_from_partner = None
        for msg in reversed(messages):
            if msg.sender == self.chat_partner and msg.text != "Seen":
                last_msg_id_from_partner = msg.id
                break

        # پاک‌کردن همه پیام‌های قبلی "پیام شما دیده شد." که خود کاربر فرستاده
        for msg in messages:
            if msg.sender == self.current_user and msg.text.strip() == "Seen":
                self.app.delete_private_message(self.current_user, self.chat_partner, msg.id)
        # ارسال پیام جدید "دیده شد" فقط اگر پیام جدیدی هست
        if last_msg_id_from_partner is not None:
            self.app.send_private_message(self.current_user, self.chat_partner, "Seen")

        # نمایش پیام‌ها با رنگ خاص
        self.messages_box.config(state="normal")
        self.messages_box.delete(1.0, tk.END)
        messages = self.app.get_private_chat_messages(self.current_user, self.chat_partner)
        for msg in messages:
            if msg.text.strip() == "Seen":
                self.messages_box.insert(tk.END, f"*** {msg.text} ***\n", "seen_msg")
            else:
                self.messages_box.insert(tk.END, f"[{msg.id}] {msg.sender}: {msg.text}\n")
            replies = msg.get_replies()
            if replies:
                for r in replies:
                    self.messages_box.insert(tk.END, f"↪ Reply: {r}\n")
        self.messages_box.tag_configure("seen_msg", foreground="#1CB486", font=("Helvetica", 13, "bold", "italic"))
        self.messages_box.config(state="disabled")

    def send_message(self):
        text = self.entry_msg.get().strip()
        if text:
            msg_id = self.app.send_private_message(self.current_user, self.chat_partner, text)
            self.entry_msg.delete(0, tk.END)
            # ثبت نوتیف جدید در فایل
            msg_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            add_notification(self.chat_partner, self.current_user, msg_time, msg_id if msg_id else "-")
            self.load_chat_messages()

    def reply_to_message(self):
        win = tk.Toplevel(self.root)
        win.title("Reply")
        win.geometry("350x200")
        win.transient(self.root)
        win.grab_set()
        win.focus_set()

        tk.Label(win, text="Message Id", font=("Helvetica", 12)).pack(pady=5)
        id_entry = tk.Entry(win, font=("Helvetica", 12))
        id_entry.pack(pady=5)
        id_entry.focus_set()

        tk.Label(win, text="Reply Text: ", font=("Helvetica", 12)).pack(pady=5)
        reply_entry = tk.Entry(win, font=("Helvetica", 12))
        reply_entry.pack(pady=5)

        def send_reply(event=None):
            try:
                msg_id = int(id_entry.get())
            except:
                messagebox.showerror("Error!", "Message id must be bumber.", parent=win)
                return
            reply = reply_entry.get().strip()
            if not reply:
                messagebox.showerror("Error!", "Messege can't be empty!", parent=win)
                return
            result = self.app.reply_to_private_message(self.current_user, self.chat_partner, msg_id, reply)
            if result:
                messagebox.showinfo("Reply", "Reply Sent Successfully.", parent=win)
            else:
                messagebox.showerror("Error!", "Message Not Found!", parent=win)
            win.destroy()
            self.load_chat_messages()

        def focus_to_reply(event):
            reply_entry.focus_set()
        id_entry.bind('<Return>', focus_to_reply)
        reply_entry.bind('<Return>', send_reply)

        tk.Button(win, text="Send Reply", command=send_reply, bg="#2196f3", fg="#fff", font=("Helvetica", 12)).pack(pady=15)
        tk.Button(win, text="Cancel", command=win.destroy).pack()

    def edit_reply_of_message(self):
        msg_id = simpledialog.askinteger("Edit Reply", "Enter Message Id: ")
        if not msg_id:
            return

        messages = self.app.get_private_chat_messages(self.current_user, self.chat_partner)
        target_msg = None
        for msg in messages:
            if msg.id == msg_id:
                target_msg = msg
                break

        if not target_msg:
            messagebox.showerror("Error!", "Message Not Found!")
            return

        replies = target_msg.get_replies()
        if not replies:
            messagebox.showerror("Error!", "NO Reply Was Found!")
            return

        reply_index = 0
        if len(replies) > 1:
            reply_index = simpledialog.askinteger(
                "Reply Id", f"Reply Id for Edit/Delete {len(replies)}):"
            )
            if not reply_index or reply_index < 1 or reply_index > len(replies):
                messagebox.showerror("Error!", "Reply Id Is Invalid!")
                return
            reply_index -= 1

        if hasattr(target_msg.replies, 'edit_reply'):
            target_msg.replies.edit_reply(reply_index, " ")
        else:
            messagebox.showerror("Error!", "Can't Edit Reply!")
            return

        self.app.save_data()

        new_reply = simpledialog.askstring("New Reply: ", "Enter New Reply.")
        if new_reply:
            target_msg.replies.edit_reply(reply_index, new_reply.strip())
            self.app.save_data()
            messagebox.showinfo("Edit Reply: ", "New Reply Edited Successfully.")
        else:
            messagebox.showinfo("Delete Reply: ", "Reply Deleted Successfully.")

        self.load_chat_messages()

    def delete_message(self):
        msg_id = simpledialog.askinteger("Delete Message: ", "Enter Message Id.")
        if msg_id:
            result = self.app.delete_private_message(self.current_user, self.chat_partner, msg_id)
            if result:
                messagebox.showinfo("Delete Message: ", "Message Deleted Successfully.")
            else:
                messagebox.showerror("Error!", "Message Not Found!")
            self.load_chat_messages()

    def search_messages(self):
        query = simpledialog.askstring("Search: ", "Enter Text or Message Id: ")
        if query:
            results = self.app.search_messages_smart(query, self.current_user)
            if not results:
                messagebox.showinfo("Search Result: ", "Message Not Found!")
            else:
                output = ""
                for msg in results:
                    output += f"[{msg['message_id']}] از {msg['sender']} به {msg['chat_with']}: {msg['text']} ({msg['timestamp']})\n"
                messagebox.showinfo("Search Result: ", output)