# 代码生成时间: 2025-09-20 08:43:48
import tkinter as tk
from tkinter import messagebox
import random
# TODO: 优化性能

"""随机数生成器程序。"""
# 增强安全性

class RandomNumberGenerator:
    """随机数生成器类。"""
    def __init__(self, master):
        self.master = master
        self.master.title("随机数生成器")

        # 设置标签
# 添加错误处理
        self.label = tk.Label(master, text="请输入两个整数：")
        self.label.pack(pady=10)

        # 设置输入框
        self.lower_bound = tk.Entry(master)
        self.lower_bound.pack(pady=10)
# 增强安全性
        self.upper_bound = tk.Entry(master)
        self.upper_bound.pack(pady=10)

        # 设置生成按钮
        self.generate_button = tk.Button(master, text="生成随机数", command=self.generate_random)
        self.generate_button.pack(pady=10)

        # 设置结果显示框
        self.result_label = tk.Label(master, text="")
# 改进用户体验
        self.result_label.pack(pady=10)

    def generate_random(self):
        """生成随机数并显示结果。"""
        try:
            lower = int(self.lower_bound.get())
# NOTE: 重要实现细节
            upper = int(self.upper_bound.get())
            if lower >= upper:
                messagebox.showerror("错误", "下界必须小于上界")
                return
            random_number = random.randint(lower, upper)
            self.result_label.config(text=f"生成的随机数是：{random_number}")
        except ValueError:
            messagebox.showerror("错误", "请输入有效的整数")

def main():
    """程序的主入口。"""
# 增强安全性
    root = tk.Tk()
    app = RandomNumberGenerator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
