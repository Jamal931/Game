import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font for the score
font = pygame.font.SysFont("comicsans", 35)

# Function to display the score
def draw_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Function to draw the snake
def draw_snake(snake_blocks):
    for block in snake_blocks:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Main function
def main():
    clock = pygame.time.Clock()

    # Snake's initial position and direction
    snake = [[100, 100], [80, 100], [60, 100]]  # Starting with 3 blocks
    direction = "RIGHT"

    # Food position
    food = [
        random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
        random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
    ]

    # Game variables
    score = 0
    running = True

    while running:
        clock.tick(FPS)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Snake controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        if keys[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        if keys[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        if keys[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

        # Move the snake
        head_x, head_y = snake[0]
        if direction == "UP":
            head_y -= BLOCK_SIZE
        elif direction == "DOWN":
            head_y += BLOCK_SIZE
        elif direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif direction == "RIGHT":
            head_x += BLOCK_SIZE

        # Add new head to the snake
        new_head = [head_x, head_y]
        snake.insert(0, new_head)

        # Check if the snake eats the food
        if new_head == food:
            score += 1
            food = [
                random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
                random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
            ]
        else:
            # Remove the last block of the snake to maintain size
            snake.pop()

        # Check for collisions
        if (
            head_x < 0 or head_x >= WIDTH or
            head_y < 0 or head_y >= HEIGHT or
            new_head in snake[1:]
        ):
            print("Game Over!")
            running = False

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, (food[0], food[1], BLOCK_SIZE, BLOCK_SIZE))  # Draw food
        draw_snake(snake)
        draw_score(score)
        pygame.display.update()

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()
