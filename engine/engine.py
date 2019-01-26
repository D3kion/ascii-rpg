import sys

import pygame
from pygame.locals import *

from . import Singleton
from .config import Config


class Engine(metaclass=Singleton):
    def __init__(self):
        self.config = Config()

        pygame.init()
        pygame.display.set_caption(self.config.WINDOW_CAPTION)

        self.screen = pygame.display.set_mode(self.config.WINDOW_RESOLUTION,
                                              RESIZABLE)
        self.font = pygame.font.SysFont('consolas', 18)
        self.clock = pygame.time.Clock()

        self.screen.fill((10, 10, 10))

    def loop(self):
        self._running = True
        while self._running:
            running = self._loop()
            self.clock.tick(10)

    def set_scene(self, scene):
        self._loop = scene().loop
        self.loop()
