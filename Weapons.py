class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y, direction):
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direction = direction
        self.dx = None
        self.dy = None


class Plane(Projectile):

    def __init__(self, x, y, direction):
        self.damage = 5
        self.speed = 5
        self.image = pygame.image.load(os.path.join("images", ".png"))
        Projectile.__init__(self, x, y direction)


class Book(Projectile):

    def __init__(self, x, y, direction):
        self.damage = 10
        self.speed = 5
        self.image = pygame.image.load(os.path.join("images", ".png"))
        Projectile.__init__(self, x, y, direction)