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
intructionsImg = pygame.image.load('images/splashScreen.jpg')
intructionsImg = pygame.transform.scale(intructionsImg, (1010, 510))

def startScreen(screen, intro):
    while intro==True:
        screen.blit(startImg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                intro = False

startScreen(screen, True)
def instructionsScreen(screen, start):
    while start== True:
        screen.blit(intructionsImg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                start = False
instructionsScreen(screen, True)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.rect.y > 0: player1.direction[1] = 1
    elif keys[pygame.K_s] and player1.rect.y + 28 < 505: player1.direction[1] = -1
    if keys[pygame.K_w]: player1.direction[1] = 1
    elif keys[pygame.K_s]: player1.direction[1] = -1
    else: player1.direction[1] = 0
    if keys[pygame.K_d] and player1.rect.x + 28 < 1005: player1.direction[0] = 1
    elif keys[pygame.K_a] and player1.rect.x > 0: player1.direction[0] = -1
    else: player1.direction[0] = 0

    if keys[pygame.K_UP] and player2.rect.y > 0: player2.direction[1] = 1
    elif keys[pygame.K_DOWN] and player2.rect.y + 28 < 505: player2.direction[1] = -1
    else: player2.direction[1] = 0
    if keys[pygame.K_RIGHT] and player2.rect.x + 28 < 1005: player2.direction[0] = 1
    elif keys[pygame.K_LEFT] and player2.rect.x > 0: player2.direction[0] = -1
    if keys[pygame.K_UP]: player2.direction[1] = 1
    elif keys[pygame.K_DOWN]: player2.direction[1] = -1
    else: player2.direction[1] = 0
    if keys[pygame.K_RIGHT]: player2.direction[0] = 1
    elif keys[pygame.K_LEFT]: player2.direction[0] = -1

    else: player2.direction[0] = 0

    if player1.direction != [0, 0]: player1.move()
    if player2.direction != [0, 0]: player2.move()

    screen.fill((0, 0, 0))
    Walls.redrawAll(screen)
    pickups.redrawAll (screen)
    player1.update()
    player_list.draw(screen)
    pygame.draw.rect(screen, (150,150,150), (player1.rect.x,player1.rect.y-5, 28, 5))
    pygame.draw.rect(screen, (255,0,0), (player1.rect.x,player1.rect.y-5,(28*(.01*player1.health)),5))
    pygame.draw.rect(screen, (150,150,150), (player2.rect.x,player2.rect.y-5,28, 5))
    pygame.draw.rect(screen, (255,0,0), (player2.rect.x,player2.rect.y-5, (28*(.01*player2.health)), 5))
    pygame.display.flip()
    clock.tick(FPS)
