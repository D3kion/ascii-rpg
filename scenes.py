import pygame
from pygame.locals import *


class Scene:
    path = './scenes/scene'

    def __init__(self):
        with open(self.path, encoding='utf8') as f:
            self.content = [line.strip() for line in f.readlines()]


class IntroScene(Scene):
    path = './scenes/test'
