import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()
height = 480
length = 640
screen = pygame.display.set_mode((length, height))
pygame.display.set_caption('JOGO DA COBRINHA')
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 50, False, True)
points = 0
pygame.mixer.music.load('BoxCat.mp3')  # Background music
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
do_point = pygame.mixer.Sound('CoinSong.wav')
y = int(height / 2)
x = int(length / 2)
speed = 10
x_temp = 0
y_temp = 0
z = h = 0
body_list = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]  # Defines the initial body lenght
start_length = 5  # Allows the body_list to start with 5 elements


def grow_snake(pos):
    for i in pos:
        pygame.draw.rect(screen, (0, 255, 0), (i[0] - 0, i[1] - 0, 40, 40))  # Defines how snake's body grows


while True:
    clock.tick(60)
    screen.fill((255, 255, 255))  # Game screen returns to white after a whole iteration, which avoids painting the screen
    message = f'Pontos: {points}'
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
                    x_temp = - speed
                    y_temp = 0
            elif event.key == K_d:
                if x_temp == -speed:
                    pass
                else:
                    x_temp = speed
                    y_temp = 0
            elif event.key == K_w:
                if y_temp == speed:
                    pass
                else:
                    y_temp = -speed
                    x_temp = 0
            elif event.key == K_s:
                if y_temp == -speed:
                    pass
                else:
                    y_temp = speed
                    x_temp = 0
    x += x_temp
    y += y_temp
    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, 40, 40))
    apple = pygame.draw.circle(screen, (255, 0, 0), (z, h), 20)
    ret_apple = pygame.Rect(z - 20, h - 20, 40, 40)  # Creates a rectangle around the circle
    if snake.colliderect(ret_apple):  # Only works with rectangle, that's why I did not enter the "apple"
        z = randint(50, 620)
        h = randint(50, 400)
        points += 1
        start_length += 1
        do_point.play()
    head_list = [x, y]
    body_list.append(head_list)
    if len(body_list) > start_length:
        body_list.pop(0)  # limited the length of the snake to current position
    grow_snake(body_list)
    screen.blit(formated_message, (420, 20))
    pygame.display.update()
