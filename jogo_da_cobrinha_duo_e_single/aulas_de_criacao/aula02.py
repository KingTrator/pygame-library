from time import sleep
import pygame
from pygame.locals import *
from sys import exit
# Vamos adicionar movimenot às estruturas do JOGO.
pygame.init() # inicia o jogo.
largura = 680
altura = 540
tela = pygame.display.set_mode((largura, altura))   # define altura e largura da tela de jogo.
pygame.display.set_caption('JOGO2')                 # Dá título ao jogo.
x = y = 0                                           # define como 0 a posição inicial do quadrado
relogio = pygame.time.Clock()
while True: # Todo jogo roda em um looping infinito
    relogio.tick(60)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (0, 0, 255), (x, y, 40, 50))
    y += 1
    x += 2
    if y > altura:
        y = 0
    if x >= largura/2:
        x = 0


    pygame.display.update()
