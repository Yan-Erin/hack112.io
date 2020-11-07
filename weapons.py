  import math
  import pygame
  
  
  class Weapon(pygame.weapon.Weapon):

    def init(self):
        pygame.Weapon.Weapon_init_(self)
        self.bx = 0
        self.by = 0
        self.bdx = 0
        self.bdy = 0
        self.bspeed = 20
        self.bdmg = 30
        self.px = 0
        self.py = 0
        self.pdx = 0
        self.pdy = 0
        self.pspeed = 40
        self.pdmg = 15
    def control(self, angle):
        self.bdx = self.speed * math.cos(angle)
        self.bdy = self.speed * math.sin(angle)
        self.pdx = self.speed * math.cos(angle)
        self.pdy = self.speed * math.sin(angle)

    def move(self):
        self.bx += self.bdx
        self.by += self.bdy
        self.px += self.pdx
        self.py += self.pdy
        