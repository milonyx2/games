import tkinter as tk
import random

# Initialize the game window
window = tk.Tk()
window.title("Snake Game")

# Set up the canvas
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack()

# Snake initial position and direction
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = "Right"

# Food initial position
food = (200, 200)

# Initialize game variables
score = 0

# Function to reset the game
def reset_game():
    global snake, snake_direction, food, score
    snake = [(100, 100), (90, 100), (80, 100)]
    snake_direction = "Right"
    food = (200, 200)
    score = 0
    try_again_button.pack_forget()
    update_score()
    canvas.delete("all")
    draw_food()
    draw_snake()
    move()

# Create "Try Again" button
try_again_button = tk.Button(window, text="Try Again", command=reset_game, font=("Arial", 16))

# Function to update the score
def update_score():
    canvas.create_text(50, 10, text=f"Score: {score}", fill="white", font=("Arial", 12))

# Function to draw the snake
def draw_snake():
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="green")

# Function to move the snake
def move():
    global snake_direction
    new_head = get_new_head()

    if check_collision(new_head):
        game_over()
        return

    snake.insert(0, new_head)
    if new_head == food:
        eat_food()
        draw_food()
    else:
        snake.pop()

    canvas.delete("all")
    draw_snake()
    draw_food()
    update_score()
    window.after(100, move)

# Function to get the new head position based on the current direction
def get_new_head():
    x, y = snake[0]
    if snake_direction == "Up":
        return x, y - 10
    elif snake_direction == "Down":
        return x, y + 10
    elif snake_direction == "Left":
        return x - 10, y
    elif snake_direction == "Right":
        return x + 10, y

# Function to check collision with walls or itself
def check_collision(new_head):
    x, y = new_head
    if x < 0 or x >= 400 or y < 0 or y >= 400 or new_head in snake[1:]:
        return True
    return False

# Function to handle the game over
def game_over():
    canvas.create_text(200, 200, text="Game Over", fill="red", font=("Arial", 24))
    try_again_button.pack()

# Function to generate and draw food
def draw_food():
    x, y = food
    canvas.create_oval(x, y, x + 10, y + 10, fill="red")

# Function to handle food consumption
def eat_food():
    global food, score
    score += 10
    x = random.randint(0, 39) * 10
    y = random.randint(0, 39) * 10
    food = (x, y)

# Function to change snake direction
def change_direction(event):
    global snake_direction
    if event.keysym == "Up" and snake_direction != "Down":
        snake_direction = "Up"
    elif event.keysym == "Down" and snake_direction != "Up":
        snake_direction = "Down"
    elif event.keysym == "Left" and snake_direction != "Right":
        snake_direction = "Left"
    elif event.keysym == "Right" and snake_direction != "Left":
        snake_direction = "Right"

# Bind arrow keys to change direction
window.bind_all("<Up>", change_direction)
window.bind_all("<Down>", change_direction)
window.bind_all("<Left>", change_direction)
window.bind_all("<Right>", change_direction)

# Initial draw of snake and food
draw_snake()
draw_food()
update_score()

# Start the game
move()

# Run the game
window.mainloop()
