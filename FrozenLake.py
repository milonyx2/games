import sys

import pygame

# Initialize Pygame
pygame.init()

# Constants
GRID_SIZE = 100
GRID_WIDTH = 4
GRID_HEIGHT = 4
WINDOW_WIDTH = GRID_SIZE * GRID_WIDTH
WINDOW_HEIGHT = GRID_SIZE * GRID_HEIGHT + 50  # Increased window height for the bar
CIRCLE_RADIUS = 20
GRID_COLOR = (200, 200, 200)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BAR_COLOR = (150, 150, 150)
BUTTON_COLOR = (50, 150, 200)
BUTTON_TEXT_COLOR = WHITE
FPS = 30

# Initialize game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Grid Game")

# Player position
player_x = GRID_SIZE // 2
player_y = GRID_SIZE // 2

# Goal position
goal_x = (GRID_WIDTH - 1) * GRID_SIZE + GRID_SIZE // 2
goal_y = (GRID_HEIGHT - 1) * GRID_SIZE + GRID_SIZE // 2

# Obstacle positions
obstacles = [(150, 50), (250, 150), (350, 250)]

# Function to reset game
def reset_game():
    global player_x, player_y
    player_x = GRID_SIZE // 2
    player_y = GRID_SIZE // 2

# Main game loop
clock = pygame.time.Clock()
game_over = False
while not game_over:
    window.fill(WHITE)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and player_y > 0:
                player_y -= GRID_SIZE
            elif event.key == pygame.K_DOWN and player_y < WINDOW_HEIGHT - GRID_SIZE - 50:  # Adjusted for the bar
                player_y += GRID_SIZE
            elif event.key == pygame.K_LEFT and player_x > 0:
                player_x -= GRID_SIZE
            elif event.key == pygame.K_RIGHT and player_x < WINDOW_WIDTH - GRID_SIZE:
                player_x += GRID_SIZE
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if "Play Again" button is clicked
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if WINDOW_WIDTH / 2 - 50 <= mouse_x <= WINDOW_WIDTH / 2 + 50 and WINDOW_HEIGHT - 50 <= mouse_y <= WINDOW_HEIGHT - 25:
                reset_game()

    # Draw grid
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(window, GRID_COLOR, (x, 0), (x, WINDOW_HEIGHT - 50))  # Adjusted for the bar
    for y in range(0, WINDOW_HEIGHT - 50, GRID_SIZE):  # Adjusted for the bar
        pygame.draw.line(window, GRID_COLOR, (0, y), (WINDOW_WIDTH, y))

    # Draw player
    pygame.draw.circle(window, BLACK, (player_x, player_y), CIRCLE_RADIUS)

    # Draw goal
    pygame.draw.circle(window, GREEN, (goal_x, goal_y), CIRCLE_RADIUS)

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(window, RED, (obstacle[0] - CIRCLE_RADIUS, obstacle[1] - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2))

    # Check for collision with obstacles
    for obstacle in obstacles:
        if abs(player_x - obstacle[0]) < CIRCLE_RADIUS + GRID_SIZE / 2 and \
                abs(player_y - obstacle[1]) < CIRCLE_RADIUS + GRID_SIZE / 2:
            # Player collided with obstacle, reset player position and show "Game Over" message
            reset_game()
            font = pygame.font.Font(None, 36)
            text = font.render("Game Over", True, BLACK)
            window.blit(text, (150, 50))
            pygame.display.update()
            pygame.time.wait(1000)  # Wait for 1 second before resetting

    # Check for goal reached
    if abs(player_x - goal_x) < CIRCLE_RADIUS + GRID_SIZE / 2 and \
            abs(player_y - goal_y) < CIRCLE_RADIUS + GRID_SIZE / 2:
        # Player reached the goal
        font = pygame.font.Font(None, 36)
        text = font.render("Goal Reached!", True, BLACK)
        window.blit(text, (50, 50))

    # Draw the bar at the bottom for the "Play Again" button
    pygame.draw.rect(window, BAR_COLOR, (0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50))

    # Draw "Play Again" button
    pygame.draw.rect(window, BUTTON_COLOR, (WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT - 50, 100, 25))
    font = pygame.font.Font(None, 24)
    text = font.render("Play Again", True, BUTTON_TEXT_COLOR)
    text_rect = text.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 37.5))
    window.blit(text, text_rect)

    # Update display
    pygame.display.update()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()
