import pygame
import Walls, Heroes

pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False
FPS = 60
clock = pygame.time.Clock()

player1 = Heroes.Kosbie()
player1.rect.x = 100
player1.rect.y = 100
player_list = pygame.sprite.Group()
player_list.add(player1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player1.direction[1] = 1
    elif keys[pygame.K_s]: player1.direction[1] = -1
    else: player1.direction[1] = 0
    if keys[pygame.K_d]: player1.direction[0] = 1
    elif keys[pygame.K_a]: player1.direction[0] = -1
    else: player1.direction[0] = 0

    if player1.direction != [0, 0]: player1.move()

    screen.fill((0, 0, 0))
    Walls.redrawAll(screen)
    player1.update()
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
