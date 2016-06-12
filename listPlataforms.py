import pygame
from pygame import *

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass

class PlatformFloor(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/grass.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass

class nones(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image =  pygame.image.load("media/graphics/trans.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass

class avisos(Entity):
    def __init__(self, x, y, A_count):
        Entity.__init__(self)
        self.image = Surface((0,0))
        self.image =  pygame.image.load("media/graphics/aviso"+str(A_count)+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(110 ,90) )
        self.rect = Rect(x, y, 1, 1)

    def update(self):
        pass


class PlatformB(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/grassB.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass
class PlatformC(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/grassC.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image =  pygame.image.load("media/graphics/Portal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(24*2 ,32*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

class ExitBlock2(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image =  pygame.image.load("media/graphics/Portal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(24*2 ,32*2) )
        self.rect = Rect(x, y, 16*2, 16*2)