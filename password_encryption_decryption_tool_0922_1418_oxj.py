# 代码生成时间: 2025-09-22 14:18:07
import tkinter as tk
from tkinter import messagebox
from getpass import getpass
import hashlib
import base64
import os

"""
密码加密解密工具
"""

# 使用AES算法进行加密和解密
class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        """
        加密算法
        :param plaintext: 明文
        :return: 加密后的数据
        """
        # 这里使用base64编码作为演示，实际可以替换为AES等其他加密算法
        return base64.b64encode(plaintext.encode('utf-8'))

    def decrypt(self, ciphertext):
        """
        解密算法
        :param ciphertext: 密文
        :return: 解密后的明文
        """
        # 这里使用base64解码作为演示，实际可以替换为AES等其他加密算法
        return base64.b64decode(ciphertext).decode('utf-8')

# 密码加密解密工具界面
class PasswordToolApp:
    def __init__(self, root):
        self.root = root
        self.root.title('密码加密解密工具')
        self.root.geometry('400x200')

        self.label1 = tk.Label(root, text='原始密码：')
        self.label1.pack()

        self.entry1 = tk.Entry(root, show='*')
        self.entry1.pack()

        self.label2 = tk.Label(root, text='加密结果：')
        self.label2.pack()

        self.entry2 = tk.Entry(root, show='*')
        self.entry2.pack()

        self.label3 = tk.Label(root, text='解密结果：')
        self.label3.pack()

        self.entry3 = tk.Entry(root, show='*')
        self.entry3.pack()

        self.encrypt_button = tk.Button(root, text='加密', command=self.encrypt_action)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(root, text='解密', command=self.decrypt_action)
        self.decrypt_button.pack()

    def encrypt_action(self):
        """
        加密操作
        """
        password = self.entry1.get()
        if not password:
            messagebox.showerror('错误', '请输入原始密码')
            return

        try:
            cipher = AESCipher('my_secret_key')
            encrypted_password = cipher.encrypt(password)
            self.entry2.delete(0, tk.END)
            self.entry2.insert(0, encrypted_password)
        except Exception as e:
            messagebox.showerror('错误', str(e))

    def decrypt_action(self):
        """
        解密操作
        """
        encrypted_password = self.entry2.get()
        if not encrypted_password:
            messagebox.showerror('错误', '请输入加密结果')
            return

        try:
            cipher = AESCipher('my_secret_key')
            decrypted_password = cipher.decrypt(encrypted_password)
            self.entry3.delete(0, tk.END)
            self.entry3.insert(0, decrypted_password)
        except Exception as e:
            messagebox.showerror('错误', str(e))

# 主程序入口
if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordToolApp(root)
    root.mainloop()