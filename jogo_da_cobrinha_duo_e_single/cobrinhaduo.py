import pygame
from pygame.locals import *
from sys import exit
from random import randint
pygame.init()
length = 900
height = 680
snake_length = points = x_temp = y_temp = snake2_length = points2 = x2_temp = y2_temp = 0
h = [randint(30, 830) for _ in range(5)]
z = [randint(30, 630) for _ in range(5)]
speed = 4
speed2 = 4
y = int(height/2)
x = int(length/2)
y2 = randint(30, 630)
x2 = randint(30, 830)
body_list = []
body2_list = []
screen = pygame.display.set_mode((length, height))
pygame.display.set_caption("SNAKE'S GAME")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 60, True, True)
pygame.mixer.music.load('BoxCat.mp3')
pygame.mixer.music.play(-1)
point_play_song = pygame.mixer.Sound('CoinSong.wav')
lose_game = pygame.mixer.Sound('chaves-ta-bom-mas-nao-se-irrite.mp3')


def grow_snake(pos, color):
    for i in pos:
        pygame.draw.rect(screen, color, (i[0], i[1], 20, 20))


def reload_game():
    global snake_length, points, x_temp, y_temp, z, h, x, y, body_list, death, head_list, snake2_length, points2, x2_temp, y2_temp, x2, y2, body2_list
    snake_length = points = x_temp = y_temp = snake2_length = points2 = x2_temp = y2_temp = 0
    y = int(height / 2)
    x = int(length / 2)
    y2 = randint(30, 630)
    x2 = randint(30, 830)
    body_list = []
    body2_list = []
    head_list = []
    h = [randint(30, 830) for _ in range(5)]
    z = [randint(30, 630) for _ in range(5)]
    death = False


while True:
    clock.tick(60)
    screen.fill((255, 255, 255))
    message = f'PONTOS: {points}'
    message2 = f'PONTOS: {points2}'
    formated_message = font.render(message, False, (0, 0, 0))
    formated_message2 = font.render(message2, False, (0, 0, 0))
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
            # Control for second snake
            if event.key == K_LEFT:
                if x2_temp == speed2:
                    pass
                else:
                    x2_temp = -speed2
                    y2_temp = 0
            if event.key == K_RIGHT:
                if x2_temp == -speed2:
                    pass
                else:
                    x2_temp = speed2
                    y2_temp = 0
            if event.key == K_UP:
                if y2_temp == speed2:
                    pass
                else:
                    y2_temp = -speed2
                    x2_temp = 0
            if event.key == K_DOWN:
                if y2_temp == -speed2:
                    pass
                else:
                    y2_temp = speed2
                    x2_temp = 0
    x += x_temp
    y += y_temp
    x2 += x2_temp
    y2 += y2_temp
    snake = pygame.draw.rect(screen, (0, 255, 0), (x, y, 20, 20))
    snake2 = pygame.draw.rect(screen, (255, 105, 180), (x2, y2, 20, 20))  # Pink snake
    apples = [pygame.draw.circle(screen, (255, 0, 0), (h[i]+5, z[i]+5), 5) for i in range(5)]
    apple_rects = [pygame.Rect(h[i] - 5, z[i] - 5, 20, 20) for i in range(5)]
    for i in range(5):
        if snake.colliderect(apple_rects[i]):
            h[i] = randint(30, 830)
            z[i] = randint(30, 630)
            points += 1
            snake_length += 1
            point_play_song.play()
        if snake2.colliderect(apple_rects[i]):
            h[i] = randint(30, 830)
            z[i] = randint(30, 630)
            points2 += 1
            snake2_length += 1
            point_play_song.play()
    head_list = [x, y]
    head2_list = [x2, y2]
    body_list.append(head_list)
    body2_list.append(head2_list)
    if body_list.count(head_list) > 1 or body2_list.count(head2_list) > 1:
        pygame.mixer.music.stop()
        screen.fill((255, 255, 255))
        end_message = 'GAME OVER! R para reiniciar.'
        formated_end_message = font.render(end_message, False, (0, 0, 255))
        rect_end_message = formated_end_message.get_rect()
        rect_end_message.center = (height//2, length//2)
        screen.blit(formated_end_message, rect_end_message)
        pygame.display.update()
        death = True
        lose_game.play(-1)
        while death:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        lose_game.stop()
                        pygame.mixer.music.play(-1)
                        reload_game()
    if x > length:
        x = 0
    if x < 0:
        x = length
    if y > height:
        y = 0
    if y < 0:
        y = height
    if x2 > length:
        x2 = 0
    if x2 < 0:
        x2 = length
    if y2 > height:
        y2 = 0
    if y2 < 0:
        y2 = height

    if len(body_list) > snake_length:
        body_list.pop(0)
    if len(body2_list) > snake2_length:
        body2_list.pop(0)
    grow_snake(body_list, (0, 255, 0))  # Green snake
    grow_snake(body2_list, (255, 105, 180))  # Pink snake
    screen.blit(formated_message, (500, 20))
    screen.blit(formated_message2, (500, 50))
    pygame.display.update()
