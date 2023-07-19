import pygame
from pygame.locals import *
from sys import exit
# obs: O interpretador que estou usando auqi é diferente do de outros arquivos.py
# Vou usar algumas das funções básicas do pygame para aprender melhor a como usá-las.
pygame.init()   # imprescindível
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))   # define o tamanho da tela
pygame.display.set_caption('JOGO')                  # dá um título
while True:  # todo jogo está dentro de um looping infinito
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 40))
    pygame.draw.circle(tela, (0, 0, 120), (500, 280), 40)
    pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 10)
    pygame.display.update()