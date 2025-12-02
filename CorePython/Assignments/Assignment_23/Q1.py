# Develop a simple login system with a username and password field. Implement user
# authentication, and show a success message if the login is successful, or an error
# message if the login fails.


import tkinter as tk
from tkinter import messagebox

USERNAME = "admin"
PASSWORD = "12345"

def login():
    user = username_entry.get()
    pwd = password_entry.get()

    if user == USERNAME and pwd == PASSWORD:
        messagebox.showinfo("Login Successful", f"Welcome, {user}!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


root = tk.Tk()
root.title("Login System")
root.geometry("300x200")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="User Login", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Username label and entry
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Password label and entry
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Login button
login_button = tk.Button(root, text="Login", command=login, bg="blue", fg="white")
login_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
