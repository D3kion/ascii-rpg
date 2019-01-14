import sys

import pygame
from pygame.locals import *

pygame.init()

COLS, ROWS = 80, 35
SIZE = WIDTH, HEIGHT = COLS * 10, ROWS * 15

WHITE = 255, 255, 255
BLACK = 0, 0, 0

SCREEN = pygame.display.set_mode(SIZE, RESIZABLE)
clock = pygame.time.Clock()

myFont = pygame.font.SysFont('consolas', 15)

def rows_cols_test():
    for i in range(100):
        label = myFont.render(str(i%10), 1, WHITE)
        SCREEN.blit(label, (0 + 10*i, 0))

        label = myFont.render(str(i%10), 1, WHITE)
        SCREEN.blit(label, (0, 0 + 15*i))

with open('./scenes/scene') as f:
    scene = [line.strip() for line in f.readlines()]

while True:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    SCREEN.fill(BLACK)

    rows_cols_test()

    pygame.display.flip()
