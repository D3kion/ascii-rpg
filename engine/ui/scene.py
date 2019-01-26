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
        raise NotImplementedError

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
