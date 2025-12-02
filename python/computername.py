# Get and show computer name as a popup

# Show a button to get computer name
import os
import tkinter as tk
from tkinter import messagebox

def show_computer_name():
	computer_name = os.environ.get('COMPUTERNAME') or os.uname().nodename
	messagebox.showinfo("Computer Name", f"This computer's name is: {computer_name}")

root = tk.Tk()
root.title("Get Computer Name")
root.geometry("300x100")

btn = tk.Button(root, text="Get Computer Name", command=show_computer_name)
btn.pack(pady=30)

root.mainloop()
