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
        img = pygame.image.load(os.path.join("sprites", "test.png"))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.y = 0

    def move(self):
        angles = [
            [None,  270,    90],
            [0,     315,    45],
            [180,   225,    135]
        ]
        i, j = self.direction
        angle = angles[i][j] * math.pi / 180
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)
        print(f"dx = {self.dx}, dy = {self.dy}")
        self.rect.x += self.dx
        self.rect.y += self.dy

class Kosbie(Hero):

    def specialAbility(self):
        pass

class Taylor(Hero):
    def specialAbility(self):
        pass