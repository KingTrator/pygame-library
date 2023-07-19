import pygame
from pygame.locals import *
from sys import exit
from random import randint
# Aprendendo a dar movimento ao personagem, por som, etc.
pygame.init()
altura = 480
largura = 680
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('JOGO3')
relogio = pygame.time.Clock()
x = int(altura/2)
y = int(largura/2)
z = h = 50
fonte = pygame.font.SysFont('arial', 50, True, False)
pontos = 0
musica_de_fundo = pygame.mixer.music.load('BoxCat.mp3') # define a variável da música e diz o caminho dela.
pygame.mixer.music.set_volume(0.5) # ajusta o som reproduzido (pode fazer = para "faz_ponto"
pygame.mixer.music.play(-1) # põe a música de fundo para tocar, e, quando terminar (-1), recomeça.
faz_ponto = pygame.mixer.Sound('CoinSong.wav') # música de "pegou o círculo".
while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, False, (0, 250, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[K_w]:
            x -= 20
        if pygame.key.get_pressed()[K_s]:
            x += 20
        if pygame.key.get_pressed()[K_d]:
            y += 20
        if pygame.key.get_pressed()[K_a]:
            y -= 20
    ret = pygame.draw.rect(tela, (255, 0, 0), (y, x, 40, 40))
    cir = pygame.draw.circle(tela, (0, 100, 200), (z, h), 20)
    ret_circ = pygame.Rect(z-40, h-40, 50, 50) # Cria um retângulo ao redor do círculo
    if ret.colliderect(ret_circ):  # Só funciona entre retângulos, por isso a "gambiarra".
        z = randint(50, 620)
        h = randint(50, 400)
        pontos += 1
        faz_ponto.play()

    tela.blit(texto_formatado, (420, 20))
    pygame.display.update()
