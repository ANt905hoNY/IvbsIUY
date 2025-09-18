# 代码生成时间: 2025-09-19 01:17:35
import tkinter as tk
from tkinter import messagebox
import psutil
import os

"""
Process Manager GUI Application using Python and Tkinter.
This application allows users to view and manage system processes.
"""

class ProcessManager:
    def __init__(self, root):
        """Initialize the ProcessManager GUI."""
        self.root = root
        self.root.title('Process Manager')
        self.root.geometry('400x300')

        # Create a frame for the listbox
        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        # Create a listbox to display processes
        self.listbox = tk.Listbox(frame, width=50, height=15)
        self.listbox.pack(side='left', fill='both', expand=True)

        # Create a scrollbar for the listbox
        scrollbar = tk.Scrollbar(frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        scrollbar.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=scrollbar.set)

        # Update the listbox with the current processes
        self.update_processes()

    def update_processes(self):
        """Update the listbox with the current system processes."""
        try:
            self.listbox.delete(0, tk.END)  # Clear the listbox
            for process in psutil.process_iter(['pid', 'name']):
                self.listbox.insert(tk.END, f'{process.info[