"""1. Develop a simple login system with a username and password field. Implement user
authentication, and show a success message if the login is successful, or an error
message if the login fails."""

import tkinter as tk
from tkinter import messagebox
 
def login():
    user = username_entry.get()
    pwd = password_entry.get()
 
    if user == "admin" and pwd == "123":
        messagebox.showinfo("Login Status", "Login Successful ✅")
    else:
        messagebox.showerror("Login Status", "Login Failed ❌")


root = tk.Tk()
root.title("Login System")
root.geometry("300x180")
 
tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)
 
tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)
 
tk.Button(root, text="Login", command=login).pack(pady=10)

root.mainloop()
