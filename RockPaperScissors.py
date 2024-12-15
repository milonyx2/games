import tkinter as tk
import random

# Function to play the game and determine the result
def play_game(user_choice):
    choices = ["Rock", "Paper", "Scissors"]
    cpu_choice = random.choice(choices)

    result_label.config(text=f"User: {user_choice} | CPU: {cpu_choice}")

    if user_choice == cpu_choice:
        result_label.config(text="It's a tie!", fg="gray")
    elif (user_choice == "Rock" and cpu_choice == "Scissors") or \
         (user_choice == "Paper" and cpu_choice == "Rock") or \
         (user_choice == "Scissors" and cpu_choice == "Paper"):
        result_label.config(text="You win!", fg="green")
    else:
        result_label.config(text="CPU wins!", fg="red")

    play_again_button.config(state=tk.NORMAL)

# Function to reset the game
def reset_game():
    result_label.config(text="Choose Rock, Paper, or Scissors", fg="black")
    play_again_button.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Set the window background color
root.configure(bg="lightgray")

# Create buttons for user choices with larger fonts
font = ("Arial", 20)
rock_button = tk.Button(root, text="Rock", command=lambda: play_game("Rock"), bg="lightblue", font=font, height=2, width=8)
paper_button = tk.Button(root, text="Paper", command=lambda: play_game("Paper"), bg="lightgreen", font=font, height=2, width=8)
scissors_button = tk.Button(root, text="Scissors", command=lambda: play_game("Scissors"), bg="lightcoral", font=font, height=2, width=8)

rock_button.pack(side=tk.LEFT, padx=20)
paper_button.pack(side=tk.LEFT, padx=20)
scissors_button.pack(side=tk.LEFT, padx=20)

# Create a label with a larger font to display the result
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 24), fg="black", bg="lightgray")
result_label.pack(pady=20)

# Create a "Play Again" button with a larger font
play_again_button = tk.Button(root, text="Play Again", command=reset_game, state=tk.DISABLED, bg="lightyellow", font=font)
play_again_button.pack()

root.mainloop()
