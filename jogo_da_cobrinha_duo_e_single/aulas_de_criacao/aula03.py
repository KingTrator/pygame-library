import pygame
from pygame.locals import *
from sys import exit
# Aprendendo a dar movimento ao personagem, pressionando repetidas vezes a tecla.
pygame.init()
altura = 480
largura = 680
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO3')
relogio = pygame.time.Clock()
x = altura/2
y = largura/2
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                y -= 100
            if event.key == K_w:
                x -= 100
            if event.key == K_s:
                x += 100
            if event.key == K_d:
                y += 100
                if y >= largura :
                    y = 0
    pygame.draw.rect(tela, (150, 0, 0), (y, x, 40, 40))



    pygame.display.update()

