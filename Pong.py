import tkinter as tk
import random

# Initialize the game window
window = tk.Tk()
window.title("Pong Game")

# Set up the canvas
canvas = tk.Canvas(window, width=600, height=400, bg="black")
canvas.pack()

# Paddle A
paddle_a = canvas.create_rectangle(10, 150, 30, 250, fill="white")

# Paddle B
paddle_b = canvas.create_rectangle(570, 150, 590, 250, fill="white")

# Ball
ball = canvas.create_oval(295, 195, 305, 205, fill="white")

# Initialize ball movement
ball_speed_x = 2
ball_speed_y = 2

# Initialize scores
score_a = 0
score_b = 0

# Create score labels
score_label_a = canvas.create_text(200, 50, text=score_a, fill="white", font=("Arial", 24))
score_label_b = canvas.create_text(400, 50, text=score_b, fill="white", font=("Arial", 24))

# Function to update the scores
def update_scores():
    canvas.itemconfig(score_label_a, text=score_a)
    canvas.itemconfig(score_label_b, text=score_b)

# Function to reset the ball
def reset_ball():
    canvas.coords(ball, 295, 195, 305, 205)

# Function to start a new game
def try_again():
    global score_a, score_b
    score_a = 0
    score_b = 0
    update_scores()
    reset_ball()
    game_loop()

# Create "Try Again" button
try_again_button = tk.Button(window, text="Try Again", command=try_again, font=("Arial", 16))
try_again_button.pack()

# Main game loop
def game_loop():
    global ball_speed_x, ball_speed_y, score_a, score_b

    # Move the ball
    canvas.move(ball, ball_speed_x, ball_speed_y)

    # Get the current ball coordinates
    ball_pos = canvas.coords(ball)

    # Check if the ball hits the top or bottom walls
    if ball_pos[3] >= 400 or ball_pos[1] <= 0:
        ball_speed_y = -ball_speed_y

    # Check if the ball hits the paddles
    if ball_pos[2] >= 600:
        if canvas.coords(paddle_b)[1] <= ball_pos[3] <= canvas.coords(paddle_b)[3]:
            ball_speed_x = -ball_speed_x
        else:
            # Player A scores a point
            score_a += 1
            reset_ball()
            update_scores()
            # Visual bounce off paddle A
            ball_speed_x = -ball_speed_x
    elif ball_pos[0] <= 0:
        if canvas.coords(paddle_a)[1] <= ball_pos[3] <= canvas.coords(paddle_a)[3]:
            ball_speed_x = -ball_speed_x
        else:
            # Player B scores a point
            score_b += 1
            reset_ball()
            update_scores()
            # Visual bounce off paddle B
            ball_speed_x = -ball_speed_x

    # Check if the game is won
    if score_a >= 5 or score_b >= 5:
        if score_a > score_b:
            winner = "Player A"
        else:
            winner = "Player B"
        canvas.create_text(300, 200, text=f"{winner} wins!", fill="white", font=("Arial", 30))
    else:
        window.after(10, game_loop)

# Start the game loop
game_loop()

# Bind keys to control paddles
def move_paddle_a(event):
    if event.keysym == "w":
        canvas.move(paddle_a, 0, -10)
    elif event.keysym == "s":
        canvas.move(paddle_a, 0, 10)

def move_paddle_b(event):
    if event.keysym == "Up":
        canvas.move(paddle_b, 0, -10)
    elif event.keysym == "Down":
        canvas.move(paddle_b, 0, 10)

# Bind keys to paddle movement
window.bind_all("w", move_paddle_a)
window.bind_all("s", move_paddle_a)
window.bind_all("<Up>", move_paddle_b)
window.bind_all("<Down>", move_paddle_b)

# Run the game
window.mainloop()
