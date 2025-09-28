"""3. Design a basic calculator to perform +,-,/,*"""
import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operator.get()
        
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Invalid operator")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Number 1:").pack(pady=5)
entry1 = tk.Entry(root, width=20)
entry1.pack()

tk.Label(root, text="Number 2:").pack(pady=5)
entry2 = tk.Entry(root, width=20)
entry2.pack()

tk.Label(root, text="Operator (+, -, *, /):").pack(pady=5)
operator = tk.Entry(root, width=5)
operator.pack()

tk.Button(root, text="Calculate", command=calculate, width=15, bg="lightgreen").pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

root.mainloop()
