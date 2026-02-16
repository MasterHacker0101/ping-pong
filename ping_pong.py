import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ping Pong Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles and ball
paddle_width, paddle_height = 10, 100
paddle_speed = 10
ball_size = 20

player1_pos = [50, HEIGHT//2 - paddle_height//2]
player2_pos = [WIDTH - 50 - paddle_width, HEIGHT//2 - paddle_height//2]
ball_pos = [WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2]
ball_vec = [5, 5]  # Ball velocity

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_pos[1] > 0:
        player1_pos[1] -= paddle_speed
    if keys[pygame.K_s] and player1_pos[1] < HEIGHT - paddle_height:
        player1_pos[1] += paddle_speed

    # Player 2 controls
    if keys[pygame.K_UP] and player2_pos[1] > 0:
        player2_pos[1] -= paddle_speed
    if keys[pygame.K_DOWN] and player2_pos[1] < HEIGHT - paddle_height:
        player2_pos[1] += paddle_speed

    # Move the ball
    ball_pos[0] += ball_vec[0]
    ball_pos[1] += ball_vec[1]

    # Collision with top and bottom
    if ball_pos[1] <= 0 or ball_pos[1] >= HEIGHT - ball_size:
        ball_vec[1] = -ball_vec[1]

    # Collision with paddles
    if (player1_pos[0] < ball_pos[0] < player1_pos[0] + paddle_width and
        player1_pos[1] < ball_pos[1] < player1_pos[1] + paddle_height) or (
        player2_pos[0] < ball_pos[0] < player2_pos[0] + paddle_width and
        player2_pos[1] < ball_pos[1] < player2_pos[1] + paddle_height):
        ball_vec[0] = -ball_vec[0]

    # Reset the ball if it goes off screen
    if ball_pos[0] < 0 or ball_pos[0] > WIDTH:
        ball_pos = [WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2]
        ball_vec = [5, 5]

    # Drawing
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player1_pos[0], player1_pos[1], paddle_width, paddle_height))
    pygame.draw.rect(screen, WHITE, (player2_pos[0], player2_pos[1], paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_pos[0], ball_pos[1], ball_size, ball_size))
    pygame.display.flip()
    pygame.time.delay(30)