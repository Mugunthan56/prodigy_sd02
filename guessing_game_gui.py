import tkinter as tk
import random

# Function to start/restart the game
def start_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry.config(state="normal")
    check_button.config(state="normal")
    result_label.config(text="", fg="black")
    entry.delete(0, tk.END)
    replay_button.pack_forget()

# Function to check user's guess
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="Please enter a valid number!", fg="orange")
        return

    guess = int(guess)
    attempts += 1

    if guess < number_to_guess:
        result_label.config(text="Too low! Try again.", fg="blue")
    elif guess > number_to_guess:
        result_label.config(text="Too high! Try again.", fg="blue")
    else:
        result_label.config(
            text=f"🎉 Guessed number {guess} is correct!\nAttempts: {attempts}",
            fg="green",
        )
        entry.config(state="disabled")
        check_button.config(state="disabled")
        replay_button.pack(pady=10)  # Show replay button

# GUI Window setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x270")
root.resizable(False, False)

tk.Label(root, text="Guess a number between 1 and 100", font=("Arial", 12)).pack(pady=15)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Hidden OK / Replay Button
replay_button = tk.Button(root, text="OK - Play Again", font=("Arial", 12), command=start_game)

# Start the game initially
start_game()

root.mainloop()
