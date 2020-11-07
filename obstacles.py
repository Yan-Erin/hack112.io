import Walls
import random
def SizeBooster(row,col,screen):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(x,y,20,20))
def Heart(row,col,screen):
    (x, y) = getCellBounds(row,col)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(x,y,20,20))