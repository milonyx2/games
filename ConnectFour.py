import numpy as np
import pygame

# Constants
ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARESIZE = 100
RADIUS = int(SQUARESIZE / 2 - 5)
WIDTH = COLUMN_COUNT * SQUARESIZE
HEIGHT = (ROW_COUNT + 1) * SQUARESIZE
SIZE = (WIDTH, HEIGHT)

# Colors
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
WINNING_COLOR = (255, 215, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Connect Four")

def create_board():
    return np.zeros((ROW_COUNT, COLUMN_COUNT))

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[ROW_COUNT - 1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def winning_move(board, piece):
    # Check horizontal locations for win
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece:
                return True

    # Check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece:
                return True

    # Check positively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(ROW_COUNT - 3):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece:
                return True

    # Check negatively sloped diagonals
    for c in range(COLUMN_COUNT - 3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BLUE, (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.circle(screen, BLACK, (int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (int(c * SQUARESIZE + SQUARESIZE / 2), HEIGHT - int(r * SQUARESIZE + SQUARESIZE / 2)), RADIUS)

def display_winner(winner):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 74)
    text = font.render(f"Player {winner} Wins!", True, WINNING_COLOR)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4))
    
    restart_button = pygame.font.Font(None, 36).render("Play Again", True, WHITE)
    quit_button = pygame.font.Font(None, 36).render("Quit", True, WHITE)
    
    screen.blit(restart_button, (WIDTH // 2 - restart_button.get_width() // 2, HEIGHT // 2))
    screen.blit(quit_button, (WIDTH // 2 - quit_button.get_width() // 2, HEIGHT // 2 + 50))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if WIDTH // 2 - restart_button.get_width() // 2 <= x <= WIDTH // 2 + restart_button.get_width() // 2 and HEIGHT // 2 <= y <= HEIGHT // 2 + 36:
                    waiting = False
                    main_game()
                elif WIDTH // 2 - quit_button.get_width() // 2 <= x <= WIDTH // 2 + quit_button.get_width() // 2 and HEIGHT // 2 + 50 <= y <= HEIGHT // 2 + 86:
                    pygame.quit()
                    exit()

def main_game():
    board = create_board()
    draw_board(board)
    pygame.display.update()
    game_over = False
    turn = 0  # Player 1 starts

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, BLACK, (0, 0, WIDTH, SQUARESIZE))
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)

                        if winning_move(board, 1):
                            display_winner(1)
                            game_over = True

                # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(posx // SQUARESIZE)

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)

                        if winning_move(board, 2):
                            display_winner(2)
                            game_over = True

                draw_board(board)

                # Switch turns
                turn += 1
                turn = turn % 2

    pygame.quit()

# Start the game
main_game()
