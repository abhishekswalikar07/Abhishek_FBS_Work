# Build a currency converter application that converts between different currencies. The
# user should be able to enter an amount, select the input currency, select the output
# currency, and see the converted amount.

import tkinter as tk
from tkinter import ttk, messagebox

# Predefined exchange rates (base: USD)
exchange_rates = {
    "USD": 1.0,
    "EUR": 0.93,
    "GBP": 0.79,
    "INR": 83.15,
    "JPY": 151.52,
    "AUD": 1.52,
}

def convert_currency():
    try:
        amount = float(Currency_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            converted_amount = amount
        else:
            # Convert input amount to USD first, then to target currency
            usd_amount = amount / exchange_rates[from_currency]
            converted_amount = usd_amount * exchange_rates[to_currency]

        result_label.config(
            text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}",
            fg="green"
        )
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the amount.")

# ---------------- GUI SETUP ----------------

window = tk.Tk()
window.title("Currency Converter")
window.geometry("500x300")
window.resizable(False, False)

# Title
title_label = tk.Label(window, text="💱 Currency Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Amount Entry
Currency_label = tk.Label(window, text="Enter Amount:")
Currency_label.pack()
Currency_entry = tk.Entry(window)
Currency_entry.pack(pady=5)

# Dropdowns for From and To Currency
currency_list = list(exchange_rates.keys())

from_currency_var = tk.StringVar(value="USD")
to_currency_var = tk.StringVar(value="INR")

from_label = tk.Label(window, text="From Currency:")
from_label.pack()
from_menu = ttk.Combobox(window, textvariable=from_currency_var, values=currency_list, state="readonly")
from_menu.pack(pady=5)

to_label = tk.Label(window, text="To Currency:")
to_label.pack()
to_menu = ttk.Combobox(window, textvariable=to_currency_var, values=currency_list, state="readonly")
to_menu.pack(pady=5)

# Convert Button
convert_button = tk.Button(window, text="Convert", command=convert_currency, bg="blue", fg="white")
convert_button.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

window.mainloop()
