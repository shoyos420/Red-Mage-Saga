import pygame
from plataform import *
from listPlataforms import *


def level(num):
	if num == 1:
		level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                             E     N",
        "N                    BFFFFFFFFFFC                                                          BC       N",
        "N                                                                                     BFC     F     N",
        "N                                                                                BFC                N",
        "N                                                                                                   N",
        "N    BFFFFFFFFFFFC                                                        BFFC                      N",
        "N                                                                                                   N",
        "N                          BFFFFFFC                                                                 N",
        "N                 BFFFFFFC                                                     BFFFC                N",
        "N                                                                                                   N",
        "N         BFFFFFFFC                                                                                 N",
        "N                                                                      BFFFC                        N",
        "N                     BFFFFFFC                                                                      N",
        "N                                                                                                   N",
        "N   BFFFFFFFFFFC                                                               BFFFFFFC             N",
        "N        A                                                   A                                      N",
        "N                 BFFFFFFFFFFC                                        BFFFFFFC                      N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                 BFFFFFFFFFFC BFFFFFFFFFFC                                                         N",
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

		return level
	elif num == 2:
		level = [
        "NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN",
        "N                                                                                                   N",
        "N                                                                                             U     N",
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
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                                   N",
        "N                                                                                              E    N",
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

		return level
        elif num == 3:
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
        "N                                                                                               U   N",
        "N                                                                                                   N",
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
        "N                                                                                                   N",
        "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF",]

                return level




def constructor(level,aux):
        A_count=aux
        entities = pygame.sprite.Group()
        platforms = []
        x = y = 0
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
                    x += 16*2
                y += 16*2
                x = 0

        return (platforms,entities,A_count)