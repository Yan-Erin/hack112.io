import pygame
import Walls
pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False
while not done:
    for event in pygame.event.get():
        Walls.redrawAll(screen)
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
pygame.quit()