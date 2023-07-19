import pygame
from pygame.locals import *
# É possível importar direto na função, mas isso, em outras linguagens menos inteligentes,
# poderia causar um delay no jogo, pois toda vez que a função move fosse convocada
# (toda vez que uma teclada é pressionada), aconteceria uma importação.


def move(x=0, y=0):
    if pygame.key.get_pressed()[K_w]:
        x -= 20
    if pygame.key.get_pressed()[K_s]:
        x += 20
    if pygame.key.get_pressed()[K_a]:
        y -= 20
    if pygame.key.get_pressed()[K_d]:
        y += 20
    return x, y


