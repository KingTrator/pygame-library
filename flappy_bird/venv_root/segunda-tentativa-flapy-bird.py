import os
import pygame
import random
os.chdir(r'C:\Users\Win10\OneDrive\Documentos\Estudos\python-libraries\pygame-library\flappy_bird\imgs')
LARGURA = 1200
ALTURA = 600
BASE = pygame.image.load(os.path.join('imgs', 'base.png'))
clock = pygame.time.Clock   # variável que armazena o tempo de frame exbido na tela.
def run():
    clock.tick(60)  # define o display de frames em 60fps
    
    pygame.display

