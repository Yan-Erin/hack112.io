import pygame
import Walls, Heroes

pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False

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
        if event.type == pygame.KEYDOWN:
            if event.key == ord("w"):
                player1.movement[1] = 1
            if event.key == ord("a"):
                player1.movement[0] = -1
            if event.key == ord("s"):
                player1.movement[1] = -1
            if event.key == ord("d"):
                player1.movement[0] = 1
        if event.type == pygame.KEYUP:
            if event.key == ord("w"):
                player1.movement[1] = 0
            if event.key == ord("a"):
                player1.movement[0] = 0
            if event.key == ord("s"):
                player1.movement[1] = 0
            if event.key == ord("d"):
                player1.movement[0] = 0
        if player1.movement != [0, 0]:
            player1.move(dw)

    screen.fill((0, 0, 0))
    Walls.redrawAll(screen)
    player1.update()
    player_list.draw(screen)
    pygame.display.flip()