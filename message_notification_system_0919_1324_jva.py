# 代码生成时间: 2025-09-19 13:24:02
import tkinter as tk
from tkinter import messagebox
import threading

"""
消息通知系统，使用TKINTER框架创建一个简单的GUI应用，
用户可以在文本框中输入消息，点击按钮后显示消息通知框。
"""

class MessageNotificationSystem:
    def __init__(self, root):
        # 设置主窗口标题和大小
        root.title("Message Notification System")
        root.geometry("400x200")

        # 创建文本框，用于输入消息
        self.message_entry = tk.Entry(root, width=50)
        self.message_entry.pack(pady=20)

        # 创建按钮，点击后显示消息通知框
        self.notify_button = tk.Button(root, text="Notify", command=self.show_notification)
        self.notify_button.pack(pady=10)

    def show_notification(self):
        # 获取文本框中的消息
        message = self.message_entry.get()

        # 检查消息是否为空
        if not message.strip():
            messagebox.showwarning("Warning", "Please enter a message.")
            return

        # 使用线程显示消息通知框，避免阻塞主线程
        threading.Thread(target=self.display_message, args=(message,)).start()

    def display_message(self, message):
        # 显示消息通知框
        messagebox.showinfo("Notification", message)

# 创建主窗口
root = tk.Tk()

# 创建消息通知系统实例
notification_system = MessageNotificationSystem(root)

# 运行主循环
root.mainloop()