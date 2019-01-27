import sys

import pygame

from engine import Display
from . import Drawer


class Scene:
    def __init__(self, display: Display):
        self.display = display
        self.clock = display.clock
        self.drawer = Drawer(display)

    def loop(self):
        self.running = True
        while self.running:
            self._handle_events()
            self._draw()
            self.display.render()
            self.clock.tick(10)

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _draw(self):
        raise NotImplementedError
