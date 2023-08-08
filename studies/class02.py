import pygame
import sys

pygame.init()

width, height = 1200, 600
window = pygame.display.set_mode((width, height))

font = pygame.font.Font(None, 72)
text = font.render("Hello, World!", True, (255, 255, 255))

# Não entendi como funciona
text_rect = text.get_rect(center=(width/2, height/2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Você clicou no texto")


    # Por que dentro de uma tupla?
    window.fill((0, 0, 0))

    window.blit(text, text_rect.topleft)
    # Por que "flip()" e não "update()"?
    pygame.display.flip()

# Problema: a área de texto clicável não está correspondendo exatamente ao texto em si nem
# está sendo razoável, ou seja, correspondendo a um retângulo que está bem próximo do texto. Na verdade,
# está correspondendo a toda a tela de jogo.



