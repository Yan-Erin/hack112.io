import pygame
import random
from sys import exit

margin=5
rightPiece = [
    [  True,  True,  True,  True],
    [  False,  False,  False,  True],
    [  False,  False,  False,  True],
    [  False,  False,  False,  True]
]

cubePiece = [
    [   True,   True],
    [   True,   True]
]

fortPiece = [
    [   True,   True,   True,   True,   True],
    [   False,   False,   False,   False,   True],
    [   False,   False,   False,   False,   False],
    [   True,   False,   False,   False,   False],
    [   True,   True,   True,   True,   True]
]

longPiece = [ [True], [True], [True], [True] ]

wallPieces = [fortPiece, longPiece, cubePiece, rightPiece]


cabinetImg= pygame.image.load('images/cabinet.png')
cabinetImg = pygame.transform.scale(cabinetImg, (18, 20))

chairImg = pygame.image.load('images/chair.png')
chairImg = pygame.transform.scale(chairImg, (18, 20))

def getCellBounds(row,col):
    y1= row*20 + margin
    x1= col*20 + margin
    return (x1,y1)
    

def Wall(row,col, image, screen):
    (x, y) = getCellBounds(row,col)
    screen.blit(image, (x,y))

def isValidWall(x,y,walls,chosenPiece):
    if (x,y) in walls:
        return False
    if x in range(4) and y in range(4):
        return False
    if  x in range(35,47) and y in range(10,25):
        return False
    for i in range(len(chosenPiece)):
        for j in range(len(chosenPiece[i])):
            if chosenPiece[i][j] and (((x+i+1, y+j+1) in walls) or ((x+i, y+j-3) in walls) or ((x+i-3, y+j) in walls) or ((x+i-3, y+j-3) in walls) or ((x+i, y+j+3) in walls) or ((x+i+3, y+j) in walls) or ((x+i+2, y+j+2) in walls) or ((x+i-1, y+j)in walls) or ((x+i, y+j-1)in walls) or ((x+i-1, y+j-1)in walls) or((x+i-2, y+j-2)in walls) or ((x+i, y+j-2)in walls) or ((x+i-2, y+j)in walls) or ((x+i+1, y+j)in walls) or ((x+i, y+j+1)in walls)):
                return False
    return True
walls={}

def makeWalls(numOfPieces):
    l=[cabinetImg, chairImg]
    for i in range( numOfPieces):
        chosenPiece=random.choice(wallPieces)
        x=random.randint(0,20)
        y=random.randint(0,47)
        while not (isValidWall(x,y,walls,chosenPiece)):
            x=random.randint(0,20)
            y=random.randint(0,47)
        for w in range(len(chosenPiece)):
            for j in range(len(chosenPiece[0])):
                if chosenPiece[w][j]:
                    walls[(x+w,y+j)]= random.choice(l)
makeWalls(20)


def redrawAll(screen):
    for row in range(500//20):
        for col in range (1000//20):
            (x1,y1)= getCellBounds(row,col)
            pygame.draw.rect(screen, (100,100,100), pygame.Rect(x1,y1,20,20),1)
    for i in walls:
        Wall(i[0],i[1],walls[i], screen)
