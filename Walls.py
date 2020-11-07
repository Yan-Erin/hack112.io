import pygame
import random
pygame.init()
screen = pygame.display.set_mode((1010, 510))
done = False
margin=5
iPiece = [
    [  True,  True,  True,  True ]
    ]

jPiece = [
    [  True, False, False ],
    [  True,  True,  True ]
    ]

lPiece = [
    [ False, False,  True ],
    [  True,  True,  True ]
    ]

sPiece = [
    [ False,  True,  True ],
    [  True,  True, False ]
    ]

tPiece = [
    [ False,  True, False ],
    [  True,  True,  True ]
    ]

zPiece = [
    [  True,  True, False ],
    [ False,  True,  True ]
    ]
wallPieces= [iPiece,jPiece, lPiece,sPiece,tPiece, zPiece]
walls=[]
sizeBoosters=set()
hearts=set()

def getCellBounds(row,col):
    y1= row*(20) +margin
    x1= col*20 + margin
    return (x1,y1)
    

def Wall(row,col):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y,20,20))
def SizeBooster(row,col):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(x,y,20,20))
def Heart(row,col):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,20,20))


def makeWalls(numOfPieces):
    for i in range( numOfPieces):
        chosenPiece=random.choice(wallPieces)
        x=random.randint(0,22)
        y=random.randint(0,47)
        for w in range(len(chosenPiece)):
            for j in range(len(chosenPiece[0])):
                if chosenPiece[w][j]:
                    walls.append((x+w,y+j))
makeWalls(35)
walls=set(walls)


def makeSizeBoosters(numOfPieces):
    for i in range( numOfPieces):
        x=random.randint(0,25)
        y=random.randint(0,50)
        while ((x,y) in sizeBoosters) or ((x,y) in walls):
            x=random.randint(0,25)
            y=random.randint(0,50)
        sizeBoosters.add((x,y))
makeSizeBoosters(10)

def makeHearts(numOfPieces):
    for i in range( numOfPieces):
        x=random.randint(0,25)
        y=random.randint(0,50)
        while ((x,y) in hearts) or ((x,y) in walls) or ((x,y)in sizeBoosters):
            x=random.randint(0,25)
            y=random.randint(0,50)
        hearts.add((x,y))
makeHearts(15)


while not done:
        for event in pygame.event.get():
            for row in range(500//20):
                for col in range (1000//20):
                    (x1,y1)= getCellBounds(row,col)
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x1,y1,20,20),1)
        for wall in walls:
            Wall(wall[0],wall[1])
        for booster in sizeBoosters:
            SizeBooster(booster[0],booster[1])
        for heart in hearts:
            Heart(heart[0],heart[1])
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()

pygame.quit()