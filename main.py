import pygame
import time
import random


pygame.init()

# window size
screen_width = 800
screen_height = 600

# rgb colors
green = (0, 255, 0)
red = (255, 0 ,0)
black = (0, 0 ,0)

x1 = screen_width / 2
y1 = screen_height / 2

snake_block = 10
snake_speed = 30

x1_moved = 0
y1_moved = 0

game_state = True
font = pygame.font.SysFont('Courier', 50, True, False)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Snake by MariusB5")
clock = pygame.time.Clock()

def message(message_arg, color):
    message_var = font.render(message_arg, True, color)
    screen.blit(message_var, [280, 270])

while game_state:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_state = False
        if event.type == pygame.KEYDOWN:
            # KEYDOWN referring to any key from the keyboard
            if event.key == pygame.K_LEFT:
                x1_moved = -snake_block
                y1_moved = 0
            elif event.key == pygame.K_RIGHT:
                x1_moved = snake_block
                y1_moved = 0
            elif event.key == pygame.K_UP:
                y1_moved = -snake_block
                x1_moved = 0
            elif event.key == pygame.K_DOWN:
                y1_moved = snake_block
                x1_moved = 0

    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_state = False

    x1 += x1_moved
    y1 += y1_moved
    screen.fill(black)
    pygame.draw.rect(screen, green, [x1, y1, snake_block, snake_block])
    # [] first two numbers is the position on the screen
    # [] second two numbers is the size of the rectangle
    pygame.display.update()

    clock.tick(snake_speed)

message("GAME OVER", red)
pygame.display.update()
time.sleep(5)

pygame.quit()
quit()
