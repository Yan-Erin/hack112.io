import math

class Hero(pygame.hero.Hero):

    def init(self):
        pygame.hero.Hero_init_(self)
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.speed = 50
        self.health = 100
        self.armor = 0

    def control(self, angle):
        self.dx = self.speed * math.cos(angle)
        self.dy = self.speed * math.sin(angle)

    def move(self):
        self.x += self.dx
        self.y += self.dy

class Kosbie(Hero):
    def specialAbility(self):
        pass

class Taylor(Hero):
    def specialAbility(self):
        pass