
#! /usr/bin/python

import pygame
from pygame import *

#WIN_WIDTH = 800
#WIN_HEIGHT = 640
WIN_WIDTH = 507*2
WIN_HEIGHT = 247*2

HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
#CAMERA_SLACK = 30

spritesheet= pygame.image.load("media/graphics/Redmage.png")

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

 
pygame.mixer.init()
sound_jump=pygame.mixer.Sound('media/sounds/jump.wav')
pygame.mixer.music.load('media/sounds/soft.flac')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)



def main():
    
    
    #global screen
    #global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("Use arrows to move!")
    timer = pygame.time.Clock()
    A_count=0

    up = down = left = right   = casting = False
    #bg= Surface((32,32))
    #bg.convert()
    #bg.fill(Color("#000000"))
    bg= pygame.image.load("media/graphics/bg.png").convert_alpha()
    bg= pygame.transform.scale(bg,DISPLAY )
    entities = pygame.sprite.Group()
    player = Player(16*2, 16*2)
    platforms = []

    x = y = 0
    level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                    FFFFFFFFFFFF                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N    FFFFFFFFFFFF                                                                                   N",
        "N                                                                                                   N",
        "N                          FFFFFF                                                                   N",
        "N                 FFFFFF                                                                            N",
        "N                                                                                                   N",
        "N         FFFFFFFF                                                                                  N",
        "N                                                                                                   N",
        "N                     FFFFFF                                                                        N",
        "N                                                                                                   N",
        "N   FFFFFFFFFFFF                                                                                    N",
        "N        A                                                   A                                       N",
        "N                 FFFFFFFFFFFF                                                                      N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                 FFFFFFFFFFFF FFFFFFFFFFFF                                                         N",
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]
    # build thE lEvEl",]  
    for row in level:
        for col in row:
            if col == "A":
                A_count+=1
                p = avisos(x, y,A_count)

                platforms.append(p)
                entities.add(p)
            if col == "P":
                p = Platform(x, y)
                platforms.append(p)
                entities.add(p)
            if col == "E":
                e = ExitBlock(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "N":
                e = nones(x, y)
                platforms.append(e)
                entities.add(e)
            if col == "F":
                e = PlatformFloor(x, y)
                platforms.append(e)
                entities.add(e)
            x += 16*2
        y += 16*2
        x = 0

    total_level_width  = len(level[0])*16*2
    total_level_height = len(level)*16*2
    camera = Camera(complex_camera, total_level_width, total_level_height)
    entities.add(player)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_z:
                casting = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYUP and e.key == K_z:
                casting = False

            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.rewind()
                pygame.mixer.music.play()

        # draw background
        #for y in range(32):
        #    for x in range(32):
        #        screen.blit(bg, (x * 32, y * 32))

        screen.blit(bg,(0,0))
        #soft_theme.play()
        camera.update(player)

        # update player, draw everything else
        player.update(up, down, left, right, casting, platforms)
        for e in entities:
            screen.blit(e.image, camera.apply(e))

        pygame.display.update()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

    l = min(0, l)                           # stop scrolling at the left edge
    l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
    t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
    t = min(0, t)                           # stop scrolling at the top
    return Rect(l, t, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.faceR=True
        self.counter=0
        self.onAir= True

        #self.image = Surface((32,32))
        #self.image.fill(Color("#0000FF"))
        #self.image.convert()
        self.image = standR
        #self.image =  pygame.image.load("media/graphics/move.png").convert_alpha()        
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )
        self.rect = Rect(x, y, 32*2, 32*2)

    def update(self, up, down, left, right, casting, platforms):
        if up:
            # only jump if on the ground

            if self.onGround: 
                self.yvel -= 10
                sound_jump.play()
        if down:
            pass
        if casting:
            
            if self.onGround: self.power()
            
        if left:
            self.faceR=False
            self.xvel = -8
        if right:
            self.faceR=True
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        if self.yvel < 0 or  self.yvel > 1.2 :
            self.onAir = True
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

        self.animate()

    def power(self):
        bg= pygame.image.load("media/graphics/bg2.png").convert_alpha()
        bg= pygame.transform.scale(bg,DISPLAY )
        

        print("hola")

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.onAir= False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom

    def animate(self):

        if self.xvel > 0 or self.xvel < 0:
            #self.updatecharacter(walkR1)
            walk=(walkR1, walkR2, walkR4)
            self.animateloop(walk)
            #if not self.onGround : self.updatecharacter(jumping)
            if  self.onAir : self.updatecharacter(jumping)

        else :
            self.updatecharacter(standR)
            if  self.onAir : self.updatecharacter(jumping)

    def animateloop(self,vect):
        if self.counter == 10:
            self.updatecharacter(vect[0])
        elif self.counter == 18:
            self.updatecharacter(vect[1])
        elif self.counter == 24:
            self.updatecharacter(vect[2])
       
            
            self.counter = 0
        self.counter = self.counter + 1


    def updatecharacter(self,surf):
        if not self.faceR : surf = pygame.transform.flip(surf,True,False)
        self.image= surf
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )


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
        self.image = Surface((70, 50))
        self.image =  pygame.image.load("media/graphics/aviso"+str(A_count)+".png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(110 ,90) )
        self.rect = Rect(x, y, 16*2, 16*2)

    def update(self):
        pass


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))

if __name__ == "__main__":
    main()