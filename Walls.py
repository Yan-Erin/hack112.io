import pygame
import random

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

obstacle={}

def getCellBounds(row,col):
    y1= row*(20) +margin
    x1= col*20 + margin
    return (x1,y1)
    

def Wall(row,col,screen):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x,y,20,20))
def SizeBooster(row,col,screen):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(x,y,20,20))
def Heart(row,col,screen):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,20,20))

def isValidWall(x,y,walls,chosenPiece):
    if (x,y) in walls:
        return False
    for i in range(len(chosenPiece)):
        for j in range(len(chosenPiece[i])):
            if chosenPiece[i][j] and (((x+i+1, y+j+1) in walls) or ((x+i, y+j-3) in walls) or ((x+i-3, y+j) in walls) or ((x+i-3, y+j-3) in walls) or ((x+i, y+j+3) in walls) or ((x+i+3, y+j) in walls) or ((x+i+2, y+j+2) in walls) or ((x+i-1, y+j)in walls) or ((x+i, y+j-1)in walls) or ((x+i-1, y+j-1)in walls) or((x+i-2, y+j-2)in walls) or ((x+i, y+j-2)in walls) or ((x+i-2, y+j)in walls) or ((x+i+1, y+j)in walls) or ((x+i, y+j+1)in walls)):
                return False
    return True
def makeWalls(numOfPieces):
    walls=set()
    for i in range( numOfPieces):
        chosenPiece=random.choice(wallPieces)
        x=random.randint(0,20)
        y=random.randint(0,47)
        while (not isValidWall(x,y, walls, chosenPiece)):
            x=random.randint(0,22)
            y=random.randint(0,47)
        for w in range(len(chosenPiece)):
            for j in range(len(chosenPiece[0])):
                if chosenPiece[w][j]:
                    walls.add((x+w,y+j))
    obstacle["Walls"]= walls
makeWalls(35)


def makeSizeBoosters(numOfPieces):
    sizeBoosters=set()
    for i in range( numOfPieces):
        x=random.randint(0,24)
        y=random.randint(0,49)
        while ((x,y) in sizeBoosters) or ((x,y) in obstacle.values()):
            x=random.randint(0,24)
            y=random.randint(0,49)
        sizeBoosters.add((x,y))
    obstacle["SizeBoosters"]= sizeBoosters
makeSizeBoosters(10)

def makeHearts(numOfPieces):
    hearts=set()
    for i in range( numOfPieces):
        x=random.randint(0,24)
        y=random.randint(0,49)
        while ((x,y) in hearts) or  ((x,y) in obstacle.values()):
            x=random.randint(0,24)
            y=random.randint(0,49)
        hearts.add((x,y))
    obstacle["Hearts"] = hearts
makeHearts(15)


def redrawAll(screen):
    for row in range(500//20):
        for col in range (1000//20):
            (x1,y1)= getCellBounds(row,col)
            pygame.draw.rect(screen, (255,255,255), pygame.Rect(x1,y1,20,20),1)
    for i in obstacle:
        for j in obstacle[i]:
            if i == "Walls":
                Wall(j[0],j[1], screen)
            elif i=="SizeBoosters":
                SizeBooster(j[0],j[1],screen)
            elif i== "Hearts":
                Heart(j[0],j[1],screen)
