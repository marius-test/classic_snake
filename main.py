import pygame
import time


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

snake = 10
speed = 20

x1_move = 0
y1_move = 0

game_state = True
font = pygame.font.SysFont(None, 50)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Python Snake by MariusB5, enjoy!")
clock = pygame.time.Clock()

def message(message_arg, color):
    message_var = font.render(message_arg, True, color)
    screen.blit(message_var, [x1, y1])

while game_state:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_state = False
        if event.type == pygame.KEYDOWN:
            # KEYDOWN referring to any key from the keyboard
            if event.key == pygame.K_LEFT:
                x1_move = -10
                y1_move = 0
            elif event.key == pygame.K_RIGHT:
                x1_move = 10
                y1_move = 0
            elif event.key == pygame.K_UP:
                y1_move = -10
                x1_move = 0
            elif event.key == pygame.K_DOWN:
                y1_move = 10
                x1_move = 0

    x1 += x1_move
    y1 += y1_move
    screen.fill(black)
    pygame.draw.rect(screen, green, [x1, y1, 10, 10])
    # [] first two numbers is the position on the screen
    # [] second two numbers is the size of the rectangle
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
