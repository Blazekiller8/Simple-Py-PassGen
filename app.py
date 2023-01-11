import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

def generate_password():
    length = password_length.get()
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    password_result.set(password)
    pyperclip.copy(password)
    messagebox.showinfo("Password Copied", f"Password of length {length} copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("350x200")
root.configure(bg='#2C3E50')

password_length = tk.IntVar()
password_result = tk.StringVar()

# Title Label
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 14), bg='#2C3E50', fg='#FFFFFF')
title_label.place(relx=0.5, rely=0.1, anchor='center')

# Length Label
length_label = tk.Label(root, text="Enter Length of Password :", font=("Helvetica", 12), bg='#2C3E50', fg='#FFFFFF')
length_label.place(relx=0.5, rely=0.3, anchor='center')

# Length Entry
password_length_entry = tk.Entry(root, textvariable=password_length, font=("Helvetica", 12), bg='#F5F5F5', fg='#000000')
password_length_entry.place(relx=0.5, rely=0.4, anchor='center', width=150)

# Generate Button
generate_button = tk.Button(root, text="Generate", font=("Helvetica", 12), bg='#1ABC9C', fg='#000000', activebackground='#F5F5F5', activeforeground='#000000', command=generate_password)
generate_button.place(relx=0.5, rely=0.6, anchor='center', width=150)

root.mainloop()