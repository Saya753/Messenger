import tkinter as tk
from ui.main_window import ChatAppGUI

if __name__ == "__main__":
    root = tk.Tk()  #متغیر برای ساخت پنجره  
    app = ChatAppGUI(root)   
    root.mainloop()
