import pygame
def startScreen(screen, intro):
    while intro==True:
        startImg= pygame.image.load('images/splashScreen.jpg')
        startImg = pygame.transform.scale(startImg, (1010, 510))
        screen.blit(startImg, (0,0))
        pygame.draw.rect(screen,(100,100,100),[1000/2,500/2,10,10])
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()
            if event.type==MOUSEBUTTONDOWN:
                intro = False

