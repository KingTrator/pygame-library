import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Primeiro joguinho, créditos a um cara aí do YT pelo passo a passo.

# Definindo as variáveis iniciais do jogo, display, tamanho da cobra, efeitos ingame.
pygame.init()
length = 900
height = 680
snake_length = points = x_temp = y_temp = 0
h = randint(30, 830)
z = randint(30, 630)
speed = 10
y = int(height/2)
x = int(length/2)
body_list = []
screen = pygame.display.set_mode((length, height))
pygame.display.set_caption("SNAKE'S GAME")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 60, True, True)
pygame.mixer.music.load('BoxCat.mp3')
pygame.mixer.music.play(-1)
point_play_song = pygame.mixer.Sound('CoinSong.wav')

# Funções que definem o crescimento da cobra e o restart.
def grow_snake(pos):
    for i in pos:
        pygame.draw.rect(screen, (0, 255, 0), (i[0], i[1], 20, 20))


def reload_game():
    global snake_length, points, x_temp, y_temp, z, h, x, y, body_list, death, head_list
    snake_length = points = x_temp = y_temp = 0
    y = int(height / 2)
    x = int(length / 2)
    body_list = []
    head_list = []
    h = randint(30, 830)
    z = randint(30, 630)
    death = False


while True:
    clock.tick(60)
    screen.fill((255, 255, 255))
    message = f'PONTOS: {points}'
    formated_message = font.render(message, False, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_temp == speed:
                    pass
                else:
                    x_temp = -speed
                    y_temp = 0
            if event.key == K_d:
                if x_temp == -speed:
                    pass
                else:
                    x_temp = speed
                    y_temp = 0
            if event.key == K_w:
                if y_temp == speed:
                    pass
                else:
                    y_temp = -speed
                    x_temp = 0
            if event.key == K_s:
                if y_temp == -speed:
                    pass
                else:
                    y_temp = speed
                    x_temp = 0
    x += x_temp
    y += y_temp
    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
    apple = pygame.draw.circle(screen, (255, 0, 0), (h+5, z+5), 5)
    apple_rect = pygame.Rect(h - 5, z - 5, 20, 20)
    if snake.colliderect(apple_rect):
        h = randint(30, 830)
        z = randint(30, 630)
        points += 1
        snake_length += 1
        point_play_song.play()
    head_list = [x, y]
    body_list.append(head_list)
    if body_list.count(head_list) > 1:
        screen.fill((255, 255, 255))
        end_message = 'GAME OVER! R para reiniciar.'
        formated_end_message = font.render(end_message, False, (0, 0, 255))
        rect_end_message = formated_end_message.get_rect()
        rect_end_message.center = (height//2, length//2)
        screen.blit(formated_end_message, rect_end_message)
        pygame.display.update()
        death = True
        while death:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reload_game()
    if x > length:
        x = 0
    if x < 0:
        x = length
    if y > height:
        y = 0
    if y < 0:
        y = height

    if len(body_list) > snake_length:
        body_list.pop(0)
    grow_snake(body_list)
    screen.blit(formated_message, (500, 20))
    pygame.display.update()
