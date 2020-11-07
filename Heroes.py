import pygame
import os
import math

class Hero(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.speed = 2.2
        self.health = 100
        self.armor = 0
        self.direction = [0, 0] # dx, dy
        self.name = "taylor"
        self.images = []
        for i in range(4):
            img = pygame.image.load(os.path.join("images", f"{self.name}{str(i)}.png"))
            img = pygame.transform.scale(img,(28,28))
            self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0

    def move(self):
        angles = [
            [None,  270,    90],
            [0,     315,    45],
            [180,   225,    135]
        ]
        i, j = self.direction
        if i == 0 and j == 1: self.image = self.images[3]
        if i == 0 and j == -1: self.image = self.images[0]
        if i == 1 and j == 0: self.image = self.images[1]
        if i == -1 and j == 0: self.image = self.images[2]
        angle = angles[i][j] * math.pi / 180
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)
        self.rect.x += self.dx
        self.rect.y += self.dy


class Kosbie(Hero):

    def specialAbility(self):
        pass

class Taylor(Hero):
    def specialAbility(self):
        pass