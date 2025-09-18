# 代码生成时间: 2025-09-18 14:06:28
import tkinter as tk
from tkinter import ttk
from psutil import virtual_memory
import platform

"""
Memory Analysis Application using Python and Tkinter
This application provides a simple GUI to display the current memory usage of the system.
"""

class MemoryAnalysisApp:
    def __init__(self, root):
        """Initialize the application"""
        self.root = root
        self.root.title("Memory Usage Analysis")
        self.root.geometry("400x200")

        self.create_widgets()

    def create_widgets(self):
        """Create the GUI widgets"""
        self.status_label = ttk.Label(self.root, text="Fetching memory usage...")
        self.status_label.pack(pady=10)

        # Fetch memory usage and update the label
        self.update_memory_usage()

    def update_memory_usage(self):
        """Update the memory usage label"""
        try:
            # Get the memory usage statistics
            mem = virtual_memory()
            used_mem = mem.used / (1024 * 1024 * 1024)  # Convert to GB
            total_mem = mem.total / (1024 * 1024 * 1024)  # Convert to GB
            used_percentage = mem.percent

            # Update the label with the memory usage
            self.status_label.config(text=f"Used Memory: {used_mem:.2f} GB ({used_percentage}%)
Total Memory: {total_mem:.2f} GB")
        except Exception as e:
            # Handle any exceptions that occur
            self.status_label.config(text=f"Error: {e}")

def main():
    """Main function to run the application"""
    if platform.system() == "Windows":
        import ctypes
        ctypes.windll.shcore.SetProcessDpiAwareness(1)  # Enable DPI awareness on Windows

    root = tk.Tk()
    app = MemoryAnalysisApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()