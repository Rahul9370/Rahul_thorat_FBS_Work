"""4. Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
questions one at a time and allow the user to select an answer. Provide feedback on
whether the selected answer is correct or incorrect."""
import tkinter as tk
from tkinter import messagebox

quiz = [
    {
        "question": "What is the capital of India?",
        "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
        "answer": "Delhi"
    },
    {
        "question": "Which language is used for web development?",
        "options": ["Python", "HTML", "C++", "Java"],
        "answer": "HTML"
    },
    {
        "question": "2 + 2 * 2 = ?",
        "options": ["6", "8", "4", "2"],
        "answer": "6"
    }
]

current_q = 0
score = 0

def check_answer():
    global current_q, score
    selected = var.get()
    if selected == "":
        messagebox.showwarning("Warning", "Please select an option")
        return
    if selected == quiz[current_q]["answer"]:
        messagebox.showinfo("Result", "Correct ✅")
        score += 1
    else:
        messagebox.showinfo("Result", f"Incorrect ❌. Correct answer: {quiz[current_q]['answer']}")
    
    current_q += 1
    if current_q < len(quiz):
        display_question()
    else:
        messagebox.showinfo("Quiz Completed", f"You scored {score} out of {len(quiz)}")
        root.destroy()

def display_question():
    question_label.config(text=quiz[current_q]["question"])
    for i, option in enumerate(quiz[current_q]["options"]):
        radio_buttons[i].config(text=option, value=option)
    var.set("")

root = tk.Tk()
root.title("Quiz Game")
root.geometry("400x300")

question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 12, "bold"))
question_label.pack(pady=20)

var = tk.StringVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=var, value="", font=("Arial", 11))
    rb.pack(anchor='w', padx=50)
    radio_buttons.append(rb)

tk.Button(root, text="Submit", command=check_answer, width=15, bg="lightblue").pack(pady=20)

display_question()
root.mainloop()
