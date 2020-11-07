import pygame
import random
from sys import exit

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


kozImg = pygame.image.load('koz.png')
kozImg = pygame.transform.scale(kozImg, (40,40))

taylorImg = pygame.image.load('taylor.png')
taylorImg = pygame.transform.scale(taylorImg, (40, 40))

chairImg = pygame.image.load('chair.png')
chairImg = pygame.transform.scale(chairImg, (20, 20))

def character1(row, col):
    (x, y) = getCellBounds(row, col)
    screen.blit(kozImg, (x,y))

def character2(row, col):
    (x, y) = getCellBounds(row, col)
    screen.blit(taylorImg, (x,y))

def getCellBounds(row,col):
    y1= row*20 + margin
    x1= col*20 + margin
    return (x1,y1)
    

def Wall(row,col):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y,20,20))

def isValidWall(x,y,walls,chosenPiece):
    if (x,y) in walls:
        return False
    for i in range(len(chosenPiece)):
        for j in range(len(chosenPiece[i])):
            if chosenPiece[i][j] and (((x+i+1, y+j+1) in walls) or ((x+i, y+j-3) in walls) or ((x+i-3, y+j) in walls) or ((x+i-3, y+j-3) in walls) or ((x+i, y+j+3) in walls) or ((x+i+3, y+j) in walls) or ((x+i+2, y+j+2) in walls) or ((x+i-1, y+j)in walls) or ((x+i, y+j-1)in walls) or ((x+i-1, y+j-1)in walls) or((x+i-2, y+j-2)in walls) or ((x+i, y+j-2)in walls) or ((x+i-2, y+j)in walls) or ((x+i+1, y+j)in walls) or ((x+i, y+j+1)in walls)):
                return False
    return True
walls=set()

def makeWalls(numOfPieces):
    for i in range( numOfPieces):
        chosenPiece=random.choice(wallPieces)
        x=random.randint(0,22)
        y=random.randint(0,47)
        for w in range(len(chosenPiece)):
            for j in range(len(chosenPiece[0])):
                if chosenPiece[w][j]:
                    walls.add((x+w,y+j))
makeWalls(35)


def redrawAll(screen):
    for row in range(500//20):
        for col in range (1000//20):
            (x1,y1)= getCellBounds(row,col)
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(x1,y1,20,20),1)
    for i in walls:
        Wall(i[0],i[1], screen)
