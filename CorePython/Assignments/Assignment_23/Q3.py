# Design a basic calculator to perform +,-,/,*
import tkinter as tk
from tkinter import messagebox

# Function to update expression
def press(num):
    entry_field.insert(tk.END, num)

# Function to clear entry field
def clear():
    entry_field.delete(0, tk.END)

# Function to evaluate expression
def calculate():
    try:
        expression = entry_field.get()
        result = eval(expression)
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero.")
        clear()
    except Exception:
        messagebox.showerror("Error", "Invalid Input.")
        clear()

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field for input and result
entry_field = tk.Entry(root, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
entry_field.pack(fill="x", padx=10, pady=10, ipady=10)

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack()

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        tk.Button(button_frame, text=text, width=5, height=2, bg="green", fg="white",
                  font=("Arial", 14, "bold"), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(button_frame, text=text, width=5, height=2, font=("Arial", 14),
                  command=lambda t=text: press(t)).grid(row=row, column=col, padx=5, pady=5)

# Clear button
tk.Button(root, text="Clear", width=20, height=2, bg="red", fg="white",
          font=("Arial", 12, "bold"), command=clear).pack(pady=10)

root.mainloop()
