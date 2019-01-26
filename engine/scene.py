import sys

import pygame

from .display import Display


class Scene:
    def __init__(self):
        self.display = Display()

    def loop(self):
        raise NotImplementedError

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
