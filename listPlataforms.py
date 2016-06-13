import pygame
from pygame import *

'''
lista de todos los objetos que utilizamos, clases ajenas al jugador
canciones y posiciones en las hojas de sprites, todo lo relacionado 
a esto se encuentra en esta hoja, su funcionamiento no es mas que una lista
de objetos.







'''

bombsheet= pygame.image.load("media/graphics/bombsheet.png")
spritesheet= pygame.image.load("media/graphics/Redmage.png")
firesheet=pygame.image.load("media/graphics/fire.png")
thundersheet=pygame.image.load("media/graphics/thunder.png")
icesheet=pygame.image.load("media/graphics/ice.png")
trans=pygame.image.load("media/graphics/trans.png")
wallpaper=pygame.image.load("media/graphics/wallpaper.jpg")

character = Surface((18,26),pygame.SRCALPHA)
character.blit(spritesheet,(-835,-9))
character = pygame.transform.scale(character, (18*3,26*2))
standR = character

character = Surface((18,26),pygame.SRCALPHA)
character.blit(spritesheet,(-812,-9))
character = pygame.transform.scale(character, (18*2,26*2))
walkR1 = character

character = Surface((18,26),pygame.SRCALPHA)
character.blit(spritesheet,(-790,-9))
character = pygame.transform.scale(character, (18*2,26*2))
walkR2 = character

character = Surface((17,25),pygame.SRCALPHA)
character.blit(spritesheet,(-768,-9))
character = pygame.transform.scale(character, (17*2,25*2))
walkR3 = character

character = Surface((17,25),pygame.SRCALPHA)
character.blit(spritesheet,(-746,-9))
character = pygame.transform.scale(character, (17*2,25*2))
walkR4 = character

character = Surface((18,27),pygame.SRCALPHA)
character.blit(spritesheet,(-666,-8))
character = pygame.transform.scale(character, (18*2,27*2))
jumping = character

character = Surface((18,24),pygame.SRCALPHA)
character.blit(spritesheet,(-190,-12))
character = pygame.transform.scale(character, (18*2,24*2))
getdown = character

character = Surface((20,25),pygame.SRCALPHA)
character.blit(spritesheet,(-162,-83))
character = pygame.transform.scale(character, (20*2,25*2))
hands = character

character = Surface((16,18),pygame.SRCALPHA)
character.blit(spritesheet,(-296,-331))
character = pygame.transform.scale(character, (16*2,18*2))
sword = character

character = Surface((18,26),pygame.SRCALPHA)
character.blit(spritesheet,(-767,-9))
character = pygame.transform.scale(character, (18*2,26*2))
swordmove1 = character

character = Surface((19,26),pygame.SRCALPHA)
character.blit(spritesheet,(-743,-9))
character = pygame.transform.scale(character, (19*2,26*2))
swordmove2 = character

character = Surface((5,9),pygame.SRCALPHA)
character.blit(spritesheet,(-530,-339))
character = pygame.transform.scale(character, (5*2,9*2))
sword1 = character

character = Surface((5,22),pygame.SRCALPHA)
character.blit(spritesheet,(-541,-326))
character = pygame.transform.scale(character, (5*2,22*2))
sword2 = character

character = Surface((9,22),pygame.SRCALPHA)
character.blit(spritesheet,(-553,-326))
character = pygame.transform.scale(character, (9*2,22*2))
sword3 = character

character = Surface((18,22),pygame.SRCALPHA)
character.blit(spritesheet,(-564,-326))
character = pygame.transform.scale(character, (18*2,22*2))
sword4 = character

character = Surface((29,29),pygame.SRCALPHA)
character.blit(firesheet,(-93,-6))
character = pygame.transform.scale(character, (29*2,29*2))
fire1  = character

character = Surface((29,29),pygame.SRCALPHA)
character.blit(firesheet,(-126,-6))
character = pygame.transform.scale(character, (29*2,29*2))
fire2 = character

character = Surface((29,29),pygame.SRCALPHA)
character.blit(firesheet,(-162,-6))
character = pygame.transform.scale(character, (29*2,29*2))
fire3 = character

character = Surface((14,15),pygame.SRCALPHA)
character.blit(thundersheet,(-31,-14))
character = pygame.transform.scale(character, (14*2,15*2))
thunder1 = character

character = Surface((21,21),pygame.SRCALPHA)
character.blit(thundersheet,(-53,-11))
character = pygame.transform.scale(character, (21*2,21*2))
thunder2 = character

character = Surface((42,34),pygame.SRCALPHA)
character.blit(thundersheet,(-76,-3))
character = pygame.transform.scale(character, (42*2,34*2))
thunder3 = character

character = Surface((37,40),pygame.SRCALPHA)
character.blit(icesheet,(-136,0))
character = pygame.transform.scale(character, (37*2,40*2))
ice1 = character

character = Surface((34,36),pygame.SRCALPHA)
character.blit(icesheet,(-96,-3))
character = pygame.transform.scale(character, (34*2,36*2))
ice2 = character

character = Surface((34,36),pygame.SRCALPHA)
character.blit(icesheet,(-53,-3))
character = pygame.transform.scale(character, (34*2,36*2))
ice3 = character

character = Surface((26,38),pygame.SRCALPHA)
character.blit(bombsheet,(-11,0))
character = pygame.transform.scale(character, (26*2,38*2))
bombf1 = character

character = Surface((26,38),pygame.SRCALPHA)
character.blit(bombsheet,(-58,0))
character = pygame.transform.scale(character, (26*2,38*2))
bombf2 = character

character = Surface((26,38),pygame.SRCALPHA)
character.blit(bombsheet,(-105,-1))
character = pygame.transform.scale(character, (26*2,38*2))
bombf3 = character

character = Surface((26,29),pygame.SRCALPHA)
character.blit(bombsheet,(-9,-266))
character = pygame.transform.scale(character, (26*2,29*2))
bombd1 = character

character = Surface((26,29),pygame.SRCALPHA)
character.blit(bombsheet,(-57,-266))
character = pygame.transform.scale(character, (26*2,29*2))
bombd2 = character

character = Surface((26,29),pygame.SRCALPHA)
character.blit(bombsheet,(-107,-266))
character = pygame.transform.scale(character, (26*2,29*2))
bombd3 = character

character = Surface((27,28),pygame.SRCALPHA)
character.blit(bombsheet,(-279,-263))
character = pygame.transform.scale(character, (27*2,28*2))
bombg1 = character

character = Surface((27,28),pygame.SRCALPHA)
character.blit(bombsheet,(-279,-263))
character = pygame.transform.scale(character, (27*2,28*2))
bombg1 = character

character = Surface((27,30),pygame.SRCALPHA)
character.blit(bombsheet,(-327,-262))
character = pygame.transform.scale(character, (27*2,30*2))
bombg2 = character

character = Surface((30,31),pygame.SRCALPHA)
character.blit(bombsheet,(-373,-262))
character = pygame.transform.scale(character, (30*2,31*2))
bombg3 = character

character = Surface((26,29),pygame.SRCALPHA)
character.blit(bombsheet,(-280,-6))
character = pygame.transform.scale(character, (26*2,29*2))
bombb1 = character

character = Surface((28,29),pygame.SRCALPHA)
character.blit(bombsheet,(-327,-6))
character = pygame.transform.scale(character, (28*2,29*2))
bombb2 = character

character = Surface((30,30),pygame.SRCALPHA)
character.blit(bombsheet,(-376,-6))
character = pygame.transform.scale(character, (30*2,30*2))
bombb3 = character



 
pygame.mixer.init()
sound_jump=pygame.mixer.Sound('media/sounds/jump.wav')
sound_portal=pygame.mixer.Sound('media/sounds/portal.wav')
sound_option=pygame.mixer.Sound('media/sounds/option.wav')



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

class PlatformW(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/wood.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass
class PlatformS(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        #self.image = Surface((32, 32))
        #self.image.convert()
        #self.image.fill(Color("#DDDDDD"))
        self.image =  pygame.image.load("media/graphics/stone.png").convert_alpha()
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


class Element(Entity):
    def __init__(self, x, y,prect,face):
        Entity.__init__(self)
        self.faceR = True
        self.image = fire1
        self.counter= 0
        self.rect = prect
        self.xvel=10
        self.rect = Rect(x, y, 16*2, 16*2)
        self.rect.left=prect.left+32
        self.rect.top =prect.top+16
        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )
        self.faceR= face

    def update(self,platforms):
        #x=prect
        #self.rect.left+=prect.left
        if self.faceR ==True:
            self.rect.left += self.xvel
        else : self.rect.left -= self.xvel
        self.collide(self.xvel,platforms)
        

    def updatecharacter(self,surf):
        if not self.faceR : surf = pygame.transform.flip(surf,True,False)
        self.image= surf
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )
    
    def collide(self, xvel, platforms):
            for p in platforms:
                if pygame.sprite.collide_rect(self, p):
                   
                    if xvel > 0:
                        self.rect.right = p.rect.left
                        #self.xve=self.xvel
                        self.xvel=0
                        self.image = trans
                        self.image = pygame.transform.scale(self.image,(16*2 ,16*2) )

                        print "collide right"
                    if xvel < 0:
                        #self.x-=self.xvel
                        
                        self.rect.left = p.rect.right
                        
                        print "collide left"
                        self.xvel=0
                    
class Enemy(Entity):
    def __init__(self, x, y,rand):
        Entity.__init__(self)
        self.xvel = 3
        self.yvel = 0
        self.faceR=True
        if rand == 1:
            self.image = bombf1
        if rand == 2:
            self.image = bombg1
        if rand == 3:
            self.image = bombb1
        self.color=rand
        self.image = pygame.transform.scale(self.image,(32*2 ,32*2) )
        self.rect = Rect(x, y, 32*2, 32*2)
        self.counter=0
        self.now=x
        self.die=False
        self.done=False

    def update(self,platforms,course,shoots):
        # increment in x direction
        if self.rect.left <  course[1] and self.faceR  : 
            self.rect.left += self.xvel
        elif self.rect.left >  course[0]:
            self.faceR=False
            self.rect.left -= self.xvel
        else : self.faceR=True
        
        # do x-axis collisions
        #self.collide(self.xvel, 0, platforms)
        # increment in y direction
        #self.rect.top += sin(self.xvel)
        # assuming we're in the air
        
        # do y-axis collisions
        #self.collide(0, self.yvel, platforms)
        
        self.collide(shoots)
        if not self.die:
            self.animate()
         
    def collide(self, shoots):
        for p in shoots:
            if pygame.sprite.collide_rect(self, p):
                self.image=fire3
                self.die=True


                
               

    def animate(self):

        if self.color == 1:
            walk=(bombf1,bombf2,bombf3) 
        if self.color == 2:
            walk=(bombg1,bombg2,bombg3)
        if self.color == 3:
            walk=(bombb1,bombb2,bombb3)
        self.animateloop(walk)
        


    def animateloop(self,vect):
        if self.counter == 15:
            self.updatecharacter(vect[0])
        elif self.counter == 25:
            self.updatecharacter(vect[1])
        elif self.counter == 40:
            self.updatecharacter(vect[2])
            
                
            
            self.counter = 0
        self.counter = self.counter + 1


    def updatecharacter(self,surf):
        if not self.faceR : surf = pygame.transform.flip(surf,True,False)
        self.image= surf
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )



class Boss(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 3
        self.yvel = 0
        self.faceR=True
        self.image = bombf1
        self.image = pygame.transform.scale(self.image,(32*8 ,32*8) )
        self.rect = Rect(x, y, 32*8, 32*8)
        self.counter=0
        self.now=x
        self.die=False
        self.done=False
        self.vida=1000

    def update(self,platforms,course,shoots):
        # increment in x direction
        if self.rect.left <  course[1]+1000 and self.faceR  : 
            self.rect.left += self.xvel
        elif self.rect.left >  course[0]:
            self.faceR=False
            self.rect.left -= self.xvel
        else : self.faceR=True
        
        # do x-axis collisions
        #self.collide(self.xvel, 0, platforms)
        # increment in y direction
        #self.rect.top += sin(self.xvel)
        # assuming we're in the air
        
        # do y-axis collisions
        #self.collide(0, self.yvel, platforms)
        
        self.collide(shoots)
        if not self.die:
            self.animate()
         
    def collide(self, shoots):
        for p in shoots:
            if pygame.sprite.collide_rect(self, p):
                self.updatecharacter(fire3)
                if self.vida==0:
                    self.die=True
                self.vida-=1

                
               

    def animate(self):

        walk=(bombf1,bombf2,bombf3)
        self.animateloop(walk)
        


    def animateloop(self,vect):
        if self.counter == 15:
            self.updatecharacter(vect[0])
        elif self.counter == 25:
            self.updatecharacter(vect[1])
        elif self.counter == 40:
            self.updatecharacter(vect[2])
            
                
            
            self.counter = 0
        self.counter = self.counter + 1


    def updatecharacter(self,surf):
        if not self.faceR : surf = pygame.transform.flip(surf,True,False)
        self.image= surf
        self.image = pygame.transform.scale(self.image,(32*8 ,32*8) )
