import Walls
import random
import pygame

heartIcon= pygame.image.load('images/heart.png')
heartIcon = pygame.transform.scale(heartIcon, (20, 20))
blueIcon = pygame.image.load('images/bluething.png')
blueIcon = pygame.transform.scale(blueIcon, (20, 20))
pickups={}
def SizeBooster(row,col,screen):
    (x, y) = Walls.getCellBounds(row,col)
    screen.blit(blueIcon, (x,y))
def Heart(row,col,screen):
    (x, y) = Walls.getCellBounds(row,col)
    screen.blit(heartIcon, (x,y))

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