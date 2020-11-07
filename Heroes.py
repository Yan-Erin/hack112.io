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
        self.speed = 5
        self.health = 100
        self.armor = 0
        self.movement = [0, 0] # dx, dy
        img = pygame.image.load(os.path.join("sprites", "test.png"))
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.x = 0

    def move(self):
        if self.movement[0] == 0 and self.movement[1] != 0:
            if self.movement[1] == 1: angle = 270
            else: angle = 90
            angle *= math.pi / 180
        else:
            angle = math.atan(self.movement[1] / self.movement[0])
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