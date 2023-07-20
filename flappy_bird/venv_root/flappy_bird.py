import pygame
import os
import random


# GLOSSÁRIO:
# 0. Por padrão, CONSTANTES são escritas em uppercase.
# 1. "pygame.transform.sclae2x()" permite duplicar a escala de algo
# 2. "pygame.image.load()" permite carregar alguma imagem a partir de seu caminho.

TELA_LARGURA = 500
TELA_ALTURA = 800
# Definindo as variáveis que armazenam as imagens
IMG_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMG_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMG_BG = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMGS_BIRD = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
    ]
pygame.font.init()  # Chama os métodos para usar fontes da biblioteca Pygame.
FONTE_PONTOS = pygame.font.SysFont('arial', 50)  # ('família', tamanho)


class Passaro:
    IMGS = IMGS_BIRD    # recebe a variável global
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5


    def __init__(self, x, y):
        self.x = x
        self.y = y  # posição, altera-se a cada quadro do jogo
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y    # altura, recebe o valor da posição apenas quando o pássaro pula
        self.tempo = 0  # Tempo para a parábola que o bird escreve ao saltar
        self.contagem_imagem = 0    # identifica qual a imagem que está sendo usada
        self.imagem = self.IMGS[0]


    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
        # Todas as variáveis "self.variável" são compartilhadas pelas funções da classe.


    def mover(self):
        # Cálculo do deslocamento:
        self.tempo += 1
        deslocamento = 1.5 * (self.tempo**2) + (self.velocidade * self.tempo)

        # Delimitando o deslocamento:
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
            # Roubando um pouco a Física, isso faz o movimento de subida ser mais forte.
        self.y += deslocamento

        # Alterando o ângulo do pássaro enquanto se desloca:
        if deslocamento < 0 or self.y < (self.altura + 50):
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        else:
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO


    def desenhar(self, tela):
        # Especificando a imagem a ser usada no frame/tempo:
        self.contagem_imagem += 1

        if self.contagem_imagem < self.TEMPO_ANIMACAO:
            self.imagem = self.IMGS[0]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
            self.imagem = self.IMGS[2]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
            self.imagem = self.IMGS[1]
        elif self.contagem_imagem < self.TEMPO_ANIMACAO*4 + 1:
            self.imagem = self.IMGS[0]
            self.contagem_imagem = 0


        if self.angulo <= -80:
            self.imagem = self.IMGS[1]
            self.contagem_imagem = self.TEMPO_ANIMACAO*2

        imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
        pos_centro_imagem = self.imagem.get_rect(topleft=(self.x, self.y)).center
        retangulo = imagem_rotacionada.get_rect(center=pos_centro_imagem)
        tela.blit(imagem_rotacionada, retangulo.topleft)


    def get_mask(self):
        '''

        :return: None
        Explicação: Esta é uma função simples, mas poderosa.
        O Pygame não observa a imagem que criamos, mas sim um retângulo.
        Isso pode levar a bugs nas colisões.
        Para corrigir isso, criamos uma máscara, a qual divide o retângulo que
        contém a imagem do passáro em dezenas de pequenos retângulos no tamanho de um pixel.
        Isso também é feito com a imagem do cano. Se um pixel do cano e um pixel do pássaro (imagens e não
        os retângulos que os contém) forem coincidentes, detecta-se a colisão.
        Isso torna, em escala visual, a colisão muito mais efetiva.
        Criar máscaras torna o código mais gastoso computacionalmente, mas neste caso é essencial.
        '''
        pygame.mask.from_surface(self.imagem)


class Cano:
    DISTANCIA = 200     # eu não comentei, mas a unidade aqui é "px" pixels.
    VELOCIDADE = 5

    def __init__(self, x):
        self.x = x
        self.altura = 0
        self.pos_topo = 0
        self.pos_base = 0
        self.CANO_TOPO = pygame.transform.flip(IMG_CANO, False, True)   # (source_img, Rotacionar Eixo X?, rot. Eixo Y?)
        self.CANO_BASE = IMG_CANO
        self.passou = False  # define se o cano passou o pelo pássaro
        self.definir_altura()


    def definir_altura(self):
        self.altura = random.randrange(50, 450)
        self.pos_topo = self.altura - self.CANO_TOPO.get_height()
        self.pos_base = self.altura + self.DISTANCIA


    def mover_cano(self):
        self.x -= self.VELOCIDADE


    def desenhar_cano(self, tela):
        tela.blit(self.CANO_TOPO, (self.x, self.pos_topo))
        tela.blit(self.CANO_BASE, (self.x, self.pos_base))

    def colidir(self, passaro):
        

class Chao:
    pass


