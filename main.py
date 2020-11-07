import pygame
import Walls
import pickups
pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False
Walls.redrawAll(screen)
while not done:
    for event in pygame.event.get():
        pickups.redrawAll(screen)
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
pygame.quit()
