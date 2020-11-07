import Walls
import random
import pygame
pickups={}
def SizeBooster(row,col,screen):
    (x, y) = Walls.getCellBounds(row,col)
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(x,y,20,20))
def Heart(row,col,screen):
    (x, y) = Walls.getCellBounds(row,col)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,20,20))

def makeSizeBoosters(numOfPieces):
    sizeBoosters=set()
    for i in range(numOfPieces):
        x=random.randint(0,24)
        y=random.randint(0,49)
        while ((x,y) in sizeBoosters) or ((x,y) in pickups.values() or (x,y) in Walls.walls):
            x=random.randint(0,24)
            y=random.randint(0,49)
        sizeBoosters.add((x,y))
    pickups["SizeBoosters"]= sizeBoosters
makeSizeBoosters(10)
def makeHearts(numOfPieces):
    hearts=set()
    for i in range( numOfPieces):
        x=random.randint(0,24)
        y=random.randint(0,49)
        while ((x,y) in hearts) or  ((x,y) in pickups.values() or (x,y) in Walls.walls):
            x=random.randint(0,24)
            y=random.randint(0,49)
        hearts.add((x,y))
    pickups["Hearts"] = hearts
makeHearts(15)

def addNewHeart():
    x=random.randint(0,24)
    y=random.randint(0,49)
    while ((x,y) in sizeBoosters) or ((x,y) in pickups.values() or (x,y) in Walls.walls):
        x=random.randint(0,24)
        y=random.randint(0,49)
    pickups["Hearts"].add(xy)
def addNewSizeBooster():
    x=random.randint(0,24)
    y=random.randint(0,49)
    while ((x,y) in sizeBoosters) or ((x,y) in pickups.values() or (x,y) in Walls.walls):
        x=random.randint(0,24)
        y=random.randint(0,49)
    pickups["SizeBoosters"].add(x,y)

def redrawAll (screen):
    for i in pickups:
        for j in pickups[i]:
            if i=="Hearts":
                Heart(j[0], j[1],screen)
            if  i== "SizeBoosters":
                SizeBooster(j[0], j[1],screen)