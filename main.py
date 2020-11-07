import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
done = False
<<<<<<< Updated upstream
while not done:
=======
FPS = 60
clock = pygame.time.Clock()

sprites_list = pygame.sprite.Group()

player1 = Heroes.Taylor()
player1.rect.x = 50
player1.rect.y = 40
sprites_list.add(player1)

player2 = Heroes.Kosbie()
player2.rect.x = 900
player2.rect.y = 440
sprites_list.add(player2)
startImg= pygame.image.load('images/splashScreen.jpg')
startImg = pygame.transform.scale(startImg, (1010, 510))
intructionsImg = pygame.image.load('images/instructionsScreen.jpg')
intructionsImg = pygame.transform.scale(intructionsImg, (1010, 510))

def startScreen(screen, intro):
    while intro==True:
        screen.blit(startImg, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type==pygame.MOUSEBUTTONDOWN:
                intro = False
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

startScreen(screen, True)
def instructionsScreen(screen, start):
    while start== True:
        screen.blit(intructionsImg, (0,0))
        pygame.display.update()
>>>>>>> Stashed changes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
<<<<<<< Updated upstream
        pygame.display.flip()
=======
                pygame.quit()
instructionsScreen(screen, True)

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
    if keys[pygame.K_SPACE]: sprites_list.add(player1.attack())

    if keys[pygame.K_UP] and player2.rect.y > 0: player2.direction[1] = 1
    elif keys[pygame.K_DOWN] and player2.rect.y + 28 < 505: player2.direction[1] = -1
    else: player2.direction[1] = 0
    if keys[pygame.K_RIGHT] and player2.rect.x + 28 < 1005: player2.direction[0] = 1
    elif keys[pygame.K_LEFT] and player2.rect.x > 0: player2.direction[0] = -1
    else: player2.direction[0] = 0
    if keys[pygame.K_RETURN]: sprites_list.add(player2.attack())

    if player1.direction != [0, 0]: player1.move()
    if player2.direction != [0, 0]: player2.move()

    screen.fill((0, 0, 0))
    Walls.redrawAll(screen)
    Pickups.redrawAll (screen)
    sprites_list.draw(screen)
    pygame.draw.rect(screen, (150,150,150), (player1.rect.x,player1.rect.y-5, 28, 5))
    pygame.draw.rect(screen, (255,0,0), (player1.rect.x,player1.rect.y-5,(28*(.01*player1.health)),5))
    pygame.draw.rect(screen, (150,150,150), (player2.rect.x,player2.rect.y-5,28, 5))
    pygame.draw.rect(screen, (255,0,0), (player2.rect.x,player2.rect.y-5, (28*(.01*player2.health)), 5))
    pygame.display.flip()
    clock.tick(FPS)
>>>>>>> Stashed changes
