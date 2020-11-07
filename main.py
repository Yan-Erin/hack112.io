import pygame
import Walls
import pickups
pygame.init()
done = False
screen = pygame.display.set_mode((1010, 510))
Walls.redrawAll(screen)
while not done:
    for event in pygame.event.get():
        pickups.redrawAll(screen)
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()
pygame.quit()
