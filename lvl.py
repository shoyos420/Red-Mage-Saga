import pygame
from plataform import *
from listPlataforms import *



'''
programa encargado de el disenioo de los niveles

por caracteres se encarga de diseniar e interpretar 
los disenios del juego, muy util a la hora de hacer pequenios
cambios en el nivel

foncion constructor lee y genera los tipos de objetos utilizados en el 
juego






'''

def level(num):
	if num == 1:
		level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                             E     N",
        "N                                                                                          BC       N",
        "N                                                                                     BFC     FC    N",
        "N                                                                                BFC                N",
        "N                                                                                                   N",
        "N                                                                         BFFC                      N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                              BFFFC                N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                      BFFFC                        N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                              BFFFFFFC             N",
        "N          A                  A                                A                                    N",
        "N                                                                      BFFFFFC                      N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                              H                                                    N",
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

		return level
	elif num == 2:
		level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                              SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS                     N",
        "N                                                                                        H          N",
        "N                                                                     H                             N",
        "N                                                    BC           BC         H  BFFFFFFFFFFFFFC   H N",
        "N                                                 H BFFC   H     BFFC                               N",
        "N                                                  BFFFFFC    BFFFFFFFFC                  W         N",
        "N                                             BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC                W     N",
        "N                   BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC                      N",
        "N                  BFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSSFSFFFFFFFC              W       N",
        "N     FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFSSSSSFFFFFFC         W            N",
        "N                                                                  SSS                           W  N",
        "N                                               H                  SSS                              N",
        "NFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB                     SSS                      W       N",
        "NFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFC                 SSS                              N",
        "NFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFB           H         SSS                              N",
        "N                                                 BFC        SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS      N",
        "N                                                      BFC   SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS   W  N",
        "N     FFFFFFFFFFFFFFC              BF                        SS H           H     H         SS      N",
        "N    H     H        FC            BFC               BFC      SS       H     H       H  H    SS      N",
        "N                   FFC          BFFF                        SS             H H             SS W    N",
        "N FFFFFFFFFFFFFFF   FFFC   H    BFFFF            BFC      H  SS     H   H      H    H  H    SS      N",
        "N                   FFFFC      BFFFFF                        SSH                 HH    H    SS     EN",
        "N                   FFFFFFC   BFFFFFF          BFC           SS                             SS      N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

		return level
        elif num == 3:
                level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNSSSSSSSSSSSSSSSSSSSSSSSSSSSNNNNNNNNNNNNNNNNNNN",
        "N W E                                                        H            H                         N",
        "N W                                                                 H                               N",
        "N W  WWWW     H                                        SSSSSSSSSSSSSSSSSSSSSSSSSSS                  N",
        "N W                                             SSSSSSSSSSSSSSSSSSS                                 N",
        "N W        WWWW                                 SSSSSSSSSSSSSSSSS                     BFC           N",
        "N W  H                   H     BFFFFC           SSSSSSSSSSSSSSS                H                    N",
        "N W                                             SSSSSSSSSSSSSS                                SS    N",
        "N WWWW                 BFFFC                    SSSSSSSSSSSS             BFFFFFFFFFC         SSSS   N",
        "N W                                             SSSSSSSSSS                                  SSSSSSS N",
        "N W            BFFFFC                           SSSSSSSS             BC                    SSSSSSSSSN",
        "N W    H                            H           SSSSSSS             W                    SSSSSSSSSSSS",
        "N W       WWW                                   SSSSSS          H                             SSSSSSS",
        "N W                                             SSSSS             BC             H                  S",
        "N W    WWWW            H                       SS                                        SS         S",
        "N W                                           SSS            BC        H          BFC    SS         S",
        "N WWW                      FF                SSSS        BC      H            BFC        SSSS       S",
        "N W                       BWWC               SSSS                                        SS       SSS",
        "N W          BFFC        WWWWWWWW            SSSS            BFFFFFFFFFFFFFFC            SS      SSSS",
        "N WW     H                 WW       WW       SSSS          BC                            SS   SSSSSSS",
        "N WWW               WWW    WW                SSSS       BC                               SS     SSSSS",
        "N WWWW                     WW    WW          SS                   H         H            SSS        N",
        "N WWWWW       H            WW        H       S  H        H             H                 SS        UN",
        "N WWWWWW                   WW                S                                           SS         N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

                return level
        elif num == 4:
                level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                       V                                              V                            N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

                return level




def constructor(level,aux):
        count=aux
        entities = pygame.sprite.Group()
        enemies = pygame.sprite.Group()
        platforms = []
        colorcount=1
        
        x = y = 0
        for row in level:
                for col in row:
                    if col == "A":
                        count+=1
                        p = avisos(x, y,count)

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
                    if col == "B":
                        e = PlatformB(x, y)
                        platforms.append(e)
                        entities.add(e)
                    if col == "C":
                        e = PlatformC(x, y)
                        platforms.append(e)
                        entities.add(e)
                    if col == "U":
                        e = ExitBlock2(x, y)
                        platforms.append(e)
                        entities.add(e)
                    if col == "H":
                        e = Enemy(x, y,colorcount)
                        enemies.add(e)
                        colorcount+=1
                        if colorcount ==4:
                            colorcount=1
                    if col == "W":
                        e = PlatformW(x, y)
                        platforms.append(e)
                        entities.add(e)
                    if col == "S":
                        e = PlatformS(x, y)
                        platforms.append(e)
                        entities.add(e)  
                    if col == "V":
                        e = Boss(x, y)
                        
                        enemies.add(e)  
                    x += 16*2
                y += 16*2
                x = 0

        return (platforms,entities,count,enemies)