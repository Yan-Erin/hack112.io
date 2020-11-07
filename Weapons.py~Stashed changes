import pygame
import os

class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.direction = direction
        self.dx = None
        self.dy = None
        self.damage = 10
        self.speed = 5
        self.images = []
        for i in range(4):
            img = pygame.image.load(os.path.join("images", f"{self.name}{str(i)}.png"))
            self.images.append(img)
        if self.direction == [0, 1]: self.image = self.images[0]
        if self.direction == [0, -1]: self.image = self.images[3]
        if self.direction == [1, 0]: self.image = self.images[1]
        if self.direction == [-1, 0]: self.image = self.images[2]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        pass


class Plane(Projectile):

    def __init__(self, x, y, direction):
        self.name = "plane"
        Projectile.__init__(self, x, y, direction)


class Pencil(Projectile):

    def __init__(self, x, y, direction):
        self.name = "pencil"
        Projectile.__init__(self, x, y, direction)
