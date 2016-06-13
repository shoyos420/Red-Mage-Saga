import pygame
from listPlataforms import *
import sys
import plataform

# Constantes

# Colores
NEGRO   = (   0,   0,   0)
BLANCO    = ( 255, 255, 255)
AZUL     = (   0,   0, 255)
ROJO      = ( 255,   0,   0)
VERDE    = (   0, 255,   0)

# Dimensiones pantalla
ANCHO  = 507*2
ALTO = 247*2


class Menu():

    color=NEGRO
    fondo=BLANCO
    espacio=30
    titulo_x, titulo_y=200,300
    pos_titulo=(titulo_x, titulo_y)
    opciones=[]
    pos_op=1


    def __init__(self):
        self.fuente = pygame.font.Font(None, 36)
        self.nop=1
        self.seleccion=0

    def abajo(self):
        self.nop+=1
        if self.nop > len(self.opciones):
            self.nop=1

    def arriba(self):
        self.nop-=1
        if self.nop <= 0:
            self.nop=len(self.opciones)


    def draw(self, pantalla):
        self.texto=self.fuente.render('Menu',True,self.color)
        pantalla.blit(self.texto, self.pos_titulo)
        i=1
        for op in self.opciones:
            self.texto=self.fuente.render(op,True,self.color)
            pantalla.blit(self.texto, [self.titulo_x, self.titulo_y+(self.espacio*i)])
            if self.nop==i:
                pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
                pygame.draw.circle(pantalla, self.color, pos, 5, 0)
            else:
                pos=[self.titulo_x-30, self.titulo_y+12+(self.espacio*i)]
                pygame.draw.circle(pantalla, self.fondo, pos, 5, 0)
            i+=1


def main():
    """ Programa principal """
    pygame.mixer.music.load('media/sounds/prologue.mp3')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)
    pygame.init()
    tam = [ANCHO, ALTO]
    pantalla = pygame.display.set_mode(tam)
    pygame.display.set_caption("menu")
    pantalla.blit(wallpaper,(0,0))
    menu=Menu()
    opciones=['Nuevo', 'Tutorial', 'Salir']
    menu.opciones=opciones
    fin=False
    reloj = pygame.time.Clock()

    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
                sys.exit(1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    print 'abajo'
                    sound_option.play()
                    menu.abajo()
                if event.key == pygame.K_UP:
                    print "arriba"
                    sound_option.play()
                    menu.arriba()
                if event.key == pygame.K_RETURN:
                    menu.seleccion=menu.nop
                    sound_option.play()
                    print 'seleccion'

        print 'opcion: ', menu.nop

        
        if menu.seleccion==3:
            menu.seleccion=0
            fin=True
            sys.exit(1)
        elif menu.seleccion==1:
            plataform.main(2)
        elif menu.seleccion==2:
            plataform.main(1)


        reloj.tick(60)
        menu.draw(pantalla)
        pygame.display.flip()

if __name__ == '__main__' :
    main()