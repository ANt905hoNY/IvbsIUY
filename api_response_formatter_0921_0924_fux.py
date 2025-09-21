# 代码生成时间: 2025-09-21 09:24:07
import json
import tkinter as tk
from tkinter import messagebox

"""
API响应格式化工具

该工具用于将API响应的原始数据格式化为更易读的JSON格式。
"""

class ApiResponseFormatter:
    def __init__(self, master):
        """
        初始化界面
        :param master: tkinter的主窗口
        """
        self.master = master
        self.master.title("API响应格式化工具")

        # 创建输入框
        self.input_label = tk.Label(master, text="输入API响应数据：")
        self.input_label.pack()
        self.input_text = tk.Text(master, height=10, width=50)
        self.input_text.pack()

        # 创建输出框
        self.output_label = tk.Label(master, text="格式化后的JSON数据：")
        self.output_label.pack()
        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.pack()

        # 创建格式化按钮
        self.format_button = tk.Button(master, text="格式化", command=self.format_response)
        self.format_button.pack()

    def format_response(self):
        """
        格式化API响应数据
        """
        try:
            # 获取输入框中的数据
            raw_data = self.input_text.get("1.0", tk.END)

            # 尝试将数据转换为JSON格式
            json_data = json.loads(raw_data)

            # 将JSON数据格式化为字符串并显示在输出框中
            formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, formatted_json)
        except json.JSONDecodeError as e:
            # 处理JSON解析错误
            messagebox.showerror("错误", f"JSON解析错误：{e}")

# 创建主窗口
root = tk.Tk()

# 创建ApiResponseFormatter实例
formatter = ApiResponseFormatter(root)

# 运行主循环
root.mainloop()