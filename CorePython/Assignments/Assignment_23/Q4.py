# Quiz Game: Create an interactive quiz game with multiple-choice questions. Display
# questions one at a time and allow the user to select an answer. Provide feedback on
# whether the selected answer is correct or incorrect.

import tkinter as tk
from tkinter import messagebox

# ------------------ QUIZ DATA ------------------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Madrid", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Venus", "Mars", "Jupiter"],
        "answer": "Mars"
    },
    {
        "question": "Who wrote 'Harry Potter'?",
        "options": ["J.K. Rowling", "Mark Twain", "Leo Tolstoy", "Charles Dickens"],
        "answer": "J.K. Rowling"
    }
]

# ------------------ FUNCTIONS ------------------
current_question = 0
score = 0

def load_question():
    """Load the current question and options"""
    question_label.config(text=questions[current_question]["question"])
    selected_option.set(-1)  # reset selection (no option selected)
    opts = questions[current_question]["options"]
    for i, rb in enumerate(option_buttons):
        rb.config(text=opts[i], value=i)  # ensure each button has a unique value

def next_question():
    """Check answer and move to next question"""
    global current_question, score

    sel = selected_option.get()
    if sel == -1:
        messagebox.showwarning("No Selection", "Please select an answer before proceeding.")
        return

    chosen_text = questions[current_question]["options"][sel]
    correct_answer = questions[current_question]["answer"]

    if chosen_text == correct_answer:
        score += 1
        messagebox.showinfo("Correct!", "🎉 That's the right answer!")
    else:
        messagebox.showerror("Incorrect!", f"❌ The correct answer was: {correct_answer}")

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_result()

def show_result():
    """Display the final score"""
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(questions)}")
    root.destroy()  # Close the window

# ------------------ UI SETUP ------------------
root = tk.Tk()
root.title("Quiz Game")
root.geometry("480x320")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🎯 Quiz Game", font=("Arial", 18, "bold"), fg="blue")
title_label.pack(pady=10)

# Question label
question_label = tk.Label(root, text="", font=("Arial", 14), wraplength=440, justify="left")
question_label.pack(pady=10)

# Option variable and buttons
selected_option = tk.IntVar(value=-1)  # IntVar to track index of selected option
option_buttons = []
for i in range(4):
    rb = tk.Radiobutton(root, text="", variable=selected_option, value=i, font=("Arial", 12))
    rb.pack(anchor="w", padx=40, pady=4)
    option_buttons.append(rb)

# Next button
next_button = tk.Button(root, text="Next", command=next_question, bg="green", fg="white", font=("Arial", 12, "bold"))
next_button.pack(pady=12)

# Load first question
load_question()

root.mainloop()
