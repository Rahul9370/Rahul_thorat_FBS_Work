"""2. Build a currency converter application that converts between different currencies. The
user should be able to enter an amount, select the input currency, select the output
currency, and see the converted amount."""
import tkinter as tk
from tkinter import ttk, messagebox

rates = {
    "USD": 1.0,
    "INR": 83.0,
    "EUR": 0.93,
    "GBP": 0.82,
    "JPY": 150.0
}

def convert():
    try:
        amount = float(amount_entry.get())
        from_curr = from_currency.get()
        to_curr = to_currency.get()
        if from_curr not in rates or to_curr not in rates:
            messagebox.showerror("Error", "Invalid currency selected")
            return
        amount_in_usd = amount / rates[from_curr]
        converted_amount = amount_in_usd * rates[to_curr]
        result_label.config(text=f"Converted Amount: {converted_amount:.2f} {to_curr}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x220")
root.resizable(False, False)

tk.Label(root, text="Amount:").pack(pady=5)
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()

tk.Label(root, text="From Currency:").pack(pady=5)
from_currency = ttk.Combobox(root, values=list(rates.keys()), state="readonly", width=18)
from_currency.pack()
from_currency.current(0)

tk.Label(root, text="To Currency:").pack(pady=5)
to_currency = ttk.Combobox(root, values=list(rates.keys()), state="readonly", width=18)
to_currency.pack()
to_currency.current(1)

tk.Button(root, text="Convert", command=convert, width=15, bg="lightblue").pack(pady=10)

result_label = tk.Label(root, text="Converted Amount: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
