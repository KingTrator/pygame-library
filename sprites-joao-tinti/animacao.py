import os
import pygame
from pygame.locals import * # "*" manda importar tudo
from sys import exit
# Por que importar submódulos?
# Porque, por motivo de economia, às vezes grandes bibliotecas não tem todos
# os seus submódulos prontos para uso, por isso importá-los diretamente garante isso.

pygame.init()

os.chdir(r'C:\Users\Win10\OneDrive\Documentos\Estudos\python-libraries\pygame-library'
         r'\sprites-joao-tinti\animation-master')
caminho_imagens = os.getcwd()
TELA_LARGURA, TELA_ALTURA = 640, 480
TELA = pygame.display.set_mode((TELA_LARGURA, TELA_ALTURA))
pygame.display.set_caption('Sprites')

BRANCO = (255, 255, 255)

class Sapo(pygame.sprite.Sprite): # Sapo herda dados deste último.
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        # Embora seja válido usar esse método de inicialização,
        # o uso de "super()" é mais recomendado atualmente.
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load(os.path.join('attack_1.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_2.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_3.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_4.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_5.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_6.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_7.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_8.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_9.png')))
        self.sprites.append(pygame.image.load(os.path.join('attack_10.png')))

        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (128*3, 64*3))
        # Outra forma de aumentar as imagens em relação ao seu tamanho original.

        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        # Função que usa o métod "update()" herdado da classe parental.
        def update(self):
            self.atual += 1
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[self.atual]

todas_as_sprites = pygame.sprite.Group() # Embora aqui haja apenas uma sprite
# É uma boa prática inserir todas as sprites dentrou de um grupo
SAPO = Sapo()
todas_as_sprites.add(SAPO)

while True:
    TELA.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_as_sprites.draw(TELA)
    todas_as_sprites.update()
    pygame.display.flip()
    # O "pygame.display.flip" é melhor que o update em termos de processamento para o caso
    # de estarmos atualizando a tela inteira. update pode ser usado para atualizar pequenos trechos.