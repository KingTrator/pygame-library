import os
from sys import exit
import pygame
from pygame.locals import *

pygame.init()
LARGURA, ALTURA = 600, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('dinoRun')
DIRETORIO = os.path.dirname(__file__) # diretório principal
CAMINHO_IMAGENS = os.path.join(DIRETORIO, 'imagens')
SPRITE_SHEET_PATH = os.path.join(CAMINHO_IMAGENS, 'dino.png')
SPRITE_SHEET = pygame.image.load(SPRITE_SHEET_PATH).convert_alpha()
BRANCO = (255, 255, 255)


class Dino(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.lista_dino_imagens = []
        for i in range(6):
            img = SPRITE_SHEET.subsurface((i * 32, 0), (32, 32))
            self.lista_dino_imagens.append(img)

        self.position = 0
        self.contador = 0
        self.image = self.lista_dino_imagens[self.contador]
        self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.rect = self.image.get_rect()
        
    
    def update(self):
        if self.contador <= 5:
            self.image = self.lista_dino_imagens[int(self.contador)]
            self.image = pygame.transform.scale(self.image, (32 * 3, 32 * 3))
        self.contador += 0.1
        if self.contador > 5:
            self.contador = 0

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)
FPS = 30
clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    TELA.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        else:
            dino.update()

    todas_as_sprites.draw(TELA)
    todas_as_sprites.update()
    pygame.display.flip()
