import pygame
import Walls, Heroes, pickups

pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False
FPS = 60
clock = pygame.time.Clock()

player_list = pygame.sprite.Group()

player1 = Heroes.Taylor()
player1.rect.x = 100
player1.rect.y = 100
player_list.add(player1)

player2 = Heroes.Kosbie()
player2.rect.x = 400
player2.rect.y = 400
player_list.add(player2)
startImg= pygame.image.load('images/splashScreen.jpg')
startImg = pygame.transform.scale(startImg, (1010, 510))

def startScreen(screen, intro):
    while intro==True:
        screen.blit(startImg, (0,0))
        pygame.draw.rect(screen,(100,100,100),[1000/2,500/2,10,10])
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                intro = False

startScreen(screen, True)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.rect.y > 0: player1.direction[1] = 1
    elif keys[pygame.K_s] and player1.rect.y + 28 < 505: player1.direction[1] = -1
    else: player1.direction[1] = 0
    if keys[pygame.K_d] and player1.rect.x + 28 < 1005: player1.direction[0] = 1
    elif keys[pygame.K_a] and player1.rect.x > 0: player1.direction[0] = -1
    else: player1.direction[0] = 0

    if keys[pygame.K_UP] and player2.rect.y > 0: player2.direction[1] = 1
    elif keys[pygame.K_DOWN] and player2.rect.y + 28 < 505: player2.direction[1] = -1
    else: player2.direction[1] = 0
    if keys[pygame.K_RIGHT] and player2.rect.x + 28 < 1005: player2.direction[0] = 1
    elif keys[pygame.K_LEFT] and player2.rect.x > 0: player2.direction[0] = -1
    else: player2.direction[0] = 0

    if player1.direction != [0, 0]: player1.move()
    if player2.direction != [0, 0]: player2.move()

    screen.fill((0, 0, 0))
    Walls.redrawAll(screen)
    pickups.redrawAll (screen)
    player1.update()
    player_list.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
