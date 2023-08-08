import pygame
import sys


# Para inicializar o pygame, usamos:
pygame.init()

# definindo a área da tela de jogo:
largura, altura = 1200, 600
window = pygame.display.set_mode((largura, altura))

# Para definir a fonte do texto que será escrito na tela:
font = pygame.font.Font(None, 36)
text = font.render("Hello, World!", True, (255, 255, 255))

# Looping do jogo:
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()  # interrompe o looping
            # Alternativamente, você poderia ter feito o while True ser "while running", e criar as linhas:
            # running = False (quando sair do looping "for" irá interromper todo o looping de jogo)
            # break (sairá do looping for).
    # cor de fundo:
    window.fill((255, 0, 0))
    # IMPORTANTE: Em Pygame, como já vi antes, qualquer objeto é focalizado a partir
    # do left top (relembrar aulas de CSS), por isso precisamos, eventualmente, fazer alguns
    # ajustões como abaixo: eu pego o tamanho do texto para depois usar metade do seu length
    # e ajustar a posição de exibição do texto na tela.
    width_text = text.get_width()
    # Exibir o texto:
    window.blit(text, ((largura/2) - (width_text/2), altura/2))

    # Atualizar a janela:
    pygame.display.flip()


# Este aqui é o arcabouço básico de qualquer jogo feito por Pygame.
# Há alguns adereços, claro, mas estes métodos, basicamente, sempre são usados:
# pygame.init() - é a função principal do pygame - a função da classe principal -, sem ela, basicamente,
# os métodos do pygame não alterarão os respectivos atributos.
# pygame.display.set_mode - é a função que cria a área de jogo, ou a área da tela de jogo, a partir de
# uma referência em pixels (px).
# for event in pygame.event.get(): - o método .get de event de pygame é fundamental para que o script
# possa capturar ações do jogador, como fechar a tela, cliques com o mouse ou inputs do teclado.
# if event.type == pygame.QUIT: - talvez existam outras formas de fechar o jogo, mas essa é a mais convencional:
# clicando no "botão x" top right. É interessante notar que não invocamos um método "QUIT()", mas sim a CONSTANTE
# QUIT.
# pygame.display.flip() - outro método fundamental, sem ele não apareceriam as alterações feitas pelo usuário.
