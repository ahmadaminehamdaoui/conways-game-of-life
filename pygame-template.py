import pygame, sys

# setup
pygame.init()
pygame.display.init()
pygame.display.set_caption('Level Editor')
screen = pygame.display.set_mode((500, 500))

while True:

    # clear screen
    screen.fill((0,0,0))

    # events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # update
    pygame.display.update()
