import sys

import pygame

from engine.display import Display


class Scene:
    def __init__(self, display: Display):
        self.display = display
        self.clock = display.clock

    def loop(self):
        raise NotImplementedError

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
