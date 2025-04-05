import pygame
import time
import random

pygame.init()

# Colors
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)
black = (0, 0, 0)

# Display size
width = 600
height = 400

# Set up display
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game by Alok')

# Snake block size and speed
block = 20
speed = 15

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

def message(msg, color, y_offset=0):
    text = font.render(msg, True, color)
    win.blit(text, [width // 6, height // 3 + y_offset])

def game():
    game_over = False
    game_close = False

    x = width // 2
    y = height // 2
    dx = 0
    dy = 0

    snake = []
    length = 1

    foodx = round(random.randrange(0, width - block) / 20.0) * 20.0
    foody = round(random.randrange(0, height - block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = block
                    dx = 0

        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            game_close = True

        win.fill(black)
        pygame.draw.rect(win, red, [foodx, foody, block, block])

        snake.append([x, y])
        if len(snake) > length:
            del snake[0]

        # Check for collision with self
        for block_piece in snake[:-1]:
            if block_piece == [x, y]:
                game_close = True

        for seg in snake:
            pygame.draw.rect(win, green, [seg[0], seg[1], block, block])

        pygame.display.update()

        # Eat food
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - block) / 20.0) * 20.0
            foody = round(random.randrange(0, height - block) / 20.0) * 20.0
            length += 1

        clock.tick(speed)

    pygame.quit()
    quit()

game()