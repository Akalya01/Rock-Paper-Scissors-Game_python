import tkinter as tk
from tkinter import messagebox
import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def play_game(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    winner = determine_winner(user_choice, computer_choice)
    result = f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n"

    if winner == "tie":
        result += "It's a tie!"
    elif winner == "user":
        result += "You win!"
    else:
        result += "Computer wins!"

    messagebox.showinfo("Result", result)

def main():
    def on_button_click(choice):
        play_game(choice)

    root = tk.Tk()
    root.title("Rock-Paper-Scissors Game")

    label = tk.Label(root, text="Choose your move:")
    label.pack()

    buttons_frame = tk.Frame(root)
    buttons_frame.pack()

    choices = ["rock", "paper", "scissors"]
    for choice in choices:
        button = tk.Button(buttons_frame, text=choice, command=lambda c=choice: on_button_click(c))
        button.pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    main()
