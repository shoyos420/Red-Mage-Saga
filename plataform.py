
#! /usr/bin/python

import pygame
from pygame import *
import lvl , listPlataforms
from listPlataforms import *
from lvl import *
import menu

from math import *
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









def main(aux):
    pygame.mixer.music.load('media/sounds/soft.flac')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    #global screen
    #global cameraX, cameraY
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
    pygame.display.set_caption("RED MAGE!!")
    timer = pygame.time.Clock()
    A_count=0
    atack_counter=0
    nivel=aux
    shoots=[]
    

    up = down = left = right  =atack = casting = False
    #bg= Surface((32,32))
    #bg.convert()
    #bg.fill(Color("#000000"))
    bg= pygame.image.load("media/graphics/bg.png").convert_alpha()
    bg= pygame.transform.scale(bg,DISPLAY )
    
    player = Player(16*2, 16*2+690)
    
    sw= Element(16,16*2+690,player.rect,player.faceR)
    shoots.append(sw)

    #test=Enemy(16*2+200, 16*2+650)
    
    level=lvl.level(nivel)

    dataLevel=constructor(level,A_count)
    platforms=dataLevel[0]
    entities=dataLevel[1]
    salida=dataLevel[2]
    enemies=dataLevel[3]
    # build thE lEvEl",]  
    

    total_level_width  = len(level[0])*16*2
    total_level_height = len(level)*16*2
    camera = Camera(complex_camera, total_level_width, total_level_height)
    #entities.add(player)
    #entities.add(sw)

    while 1:
        timer.tick(60)

        for e in pygame.event.get():
            if e.type == QUIT: raise SystemExit, "QUIT"
            if e.type == KEYDOWN and e.key == K_ESCAPE:
                raise SystemExit, "ESCAPE"
            if e.type == KEYDOWN and e.key == K_SPACE:
                menu.pausa(screen)
            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYDOWN and e.key == K_z:
                new=Element(16,16*2+690,player.rect,player.faceR)
                shoots.append(new)
            if e.type == KEYDOWN and e.key == K_x:
                atack = True
            if e.type == KEYDOWN and e.key == K_m:
                while(aux):
                    pygame.time.wait(.001)
                    if e.type == KEYDOWN and e.key == K_m:
                        aux=0

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
            if atack_counter>10:
                atack = False
                atack_counter=0

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
        player.update(up, down, left, right, casting,atack, platforms,enemies)
        
        #test.update(platforms,(16*2+180,16*2+270))
        for e in enemies:

            e.update(platforms,(e.now,e.now+100),shoots)
            if e.die:
                screen.blit(e.image, camera.apply(e))

                enemies.remove(e)

        for e in shoots:
            e.update(platforms)

        
        if player.salida == True :
            pygame.time.wait(1)
            sound_portal.play()
            if nivel==1:
                menu.main()
                print("menuuuu")
            nivel+=1
            level=lvl.level(nivel)
            dataLevel=constructor(level,A_count)
            platforms=dataLevel[0]
            entities=dataLevel[1]
            salida=dataLevel[2]
            enemies=dataLevel[3]
            player.salida=False
            # build thE lEvEl",]  
            

            total_level_width  = len(level[0])*16*2
            total_level_height = len(level)*16*2
            camera = Camera(complex_camera, total_level_width, total_level_height)
            #entities.add(player)
            #entities.add(sw)  
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for e in shoots:
            screen.blit(e.image, camera.apply(e))
        for e in enemies:
            screen.blit(e.image, camera.apply(e))
        
        screen.blit(player.image, camera.apply(player))

        pygame.display.update()
        atack_counter+=1

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
'''
class spell(Entity,tipo):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.faceR = True
        self.image = sword1
        self.counter= 0
        self.rect = Rect(x, y, 32*2, 32*2)

    def update(self,atack,rigth,left):
        

        if rigth:
            self.faceR=True

        if left: 
            self.faceR=True

        if atack:
            if self.counter == 10:
                self.updatecharacter(sword1)
            elif self.counter == 18:
                self.updatecharacter(sword2)
            elif self.counter == 24:
                self.updatecharacter(sword3)
       
            
            self.counter = 0
        self.counter = self.counter + 1

    def updatecharacter(self,surf):
        if not self.faceR : surf = pygame.transform.flip(surf,True,False)
        self.image= surf
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )
'''


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.faceR=True
        self.counter=0
        self.onAir= True
        self.down=False
        self.atack=False
        self.x=x
        self.y=y
        self.salida=False
        self.vidas=3
        self.lock=False
        self.counter=0
        

        #self.image = Surface((32,32))
        #self.image.fill(Color("#0000FF"))
        #self.image.convert()
        self.image = standR
        #self.image =  pygame.image.load("media/graphics/move.png").convert_alpha()        
        self.image = pygame.transform.scale(self.image,(26*2 ,32*2) )
        self.rect = Rect(x, y, 32*2, 32*2)

    def update(self, up, down, left, right, casting, atack,platforms,enemies):
        #if not self.lock:    
        if up:
                # only jump if on the ground

            if self.onGround: 
                self.yvel -= 10
                    #self.pos[1]-=10
                sound_jump.play()
        if down:
            self.down=True
        if casting:
                
            if self.onGround: self.power()
        if atack:
            self.atack=True   
        if left:
            self.faceR=False
            self.xvel = -8
            self.x-=8
        if right:
            self.faceR=True
            self.xvel = 8
            self.x+=8
        if not self.onGround:
                # only accelerate with gravity if in the air
            self.yvel += 0.3
                # max falling speed
            if self.yvel > 100: self.yvel = 100
        if not(left or right):
            self.xvel = 0
        if self.yvel < 0 or  self.yvel > 1.2 :
            self.onAir = True
        if not down :
            self.down=False
        if not atack:
            self.atack=False
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms,enemies)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms,enemies)

        self.animate()
        
        #else:
         #3#   self.counter+=1
            #if self.counter == 2:
             #   self.lock=False
        

    def power(self):
        bg= pygame.image.load("media/graphics/bg2.png").convert_alpha()
        bg= pygame.transform.scale(bg,DISPLAY )
        

        print("hola")

    def collide(self, xvel, yvel, platforms,enemies):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    self.salida=True
                if xvel > 0:
                    self.rect.right = p.rect.left
                    self.x-=self.xvel
                    self.xvel=0
                    print "collide right"
                if xvel < 0:
                    self.x-=self.xvel
                    self.rect.left = p.rect.right
                    print "collide left"
                    self.xvel=0
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.onAir= False
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
        for p in enemies:
            if pygame.sprite.collide_rect(self, p):
                
                    
                if self.vidas==0:
                    print "muerto"
                    menu.main() 
                else : 
                    self.vidas-=1 
                    self.updatecharacter(getdown)
                    if self.faceR:
                        self.rect.left+=10
                    else: self.rect.left-=10

    def animate(self):

        if self.atack and not self.onAir:
            swordAtack=(swordmove1,swordmove2,swordmove2)
            self.animateloop(swordAtack)

        elif self.xvel > 0 or self.xvel < 0:
            #self.updatecharacter(walkR1)
            walk=(walkR1, walkR2, walkR4)
            self.animateloop(walk)
            #if not self.onGround : self.updatecharacter(jumping)
            if  self.onAir : self.updatecharacter(jumping)

        

           
        elif self.down==True :
            self.updatecharacter(getdown)
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




if __name__ == "__main__":
    main()