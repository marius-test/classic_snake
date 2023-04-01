import pygame


pygame.init()
game_screen = pygame.display.set_mode((640, 480))
pygame.display.update()
pygame.display.set_caption("Python Snake by Marius, enjoy!")


green = (0, 255, 0)
red = (255, 0 ,0)
white = (255, 255, 255)
black = (0, 0 ,0)


game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)

        if event.type==pygame.QUIT:
            game_over = True
        
    pygame.draw.rect(game_screen, green, [320, 240, 10, 10])
    # [] first two numbers is the position on the screen
    # [] second two numbers is the size of the rectangle
    pygame.display.update()


pygame.quit()
quit()
