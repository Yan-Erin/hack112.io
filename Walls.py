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

obstacle={}

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
    walls=set()
    for i in range( numOfPieces):
        chosenPiece=random.choice(wallPieces)
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



while not done:
        for event in pygame.event.get():
            for row in range(500//20):
                for col in range (1000//20):
                    (x1,y1)= getCellBounds(row,col)
                    pygame.draw.rect(screen, (255,255,255), pygame.Rect(x1,y1,20,20),1)
        for i in obstacle:
            for j in obstacle[i]:
                if i == "Walls":
                    Wall(j[0],j[1])
                elif i=="SizeBoosters":
                    SizeBooster(j[0],j[1])
                elif i== "Hearts":
                    Heart(j[0],j[1])
        if event.type == pygame.QUIT:
            done = True
        pygame.display.flip()

pygame.quit()