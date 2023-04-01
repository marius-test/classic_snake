import pygame


pygame.init()
game_screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Python Snake by Marius, enjoy!")

green = (0, 255, 0)
red = (255, 0 ,0)
white = (255, 255, 255)
black = (0, 0 ,0)

x1 = 400
y1 = 300

x1_move = 0
y1_move = 0

time = pygame.time.Clock()

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)

        if event.type == pygame.QUIT:
            game_over = True
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
    game_screen.fill(black)
    pygame.draw.rect(game_screen, green, [x1, y1, 10, 10])
    # [] first two numbers is the position on the screen
    # [] second two numbers is the size of the rectangle
    pygame.display.update()

    time.tick(30)

pygame.quit()
quit()
