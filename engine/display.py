import sys

import pygame
from pygame.locals import *

from engine import Config


class Display():
    def __init__(self):
        self.config = Config()

        pygame.init()
        pygame.display.set_caption(self.config.WINDOW_CAPTION)

        self.screen = pygame.display.set_mode(self.config.WINDOW_RESOLUTION,
                                              FULLSCREEN)
        self.font = pygame.font.SysFont('consolas', 18)
        self.clock = pygame.time.Clock()

    def _draw_display(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        display_position = (
            (screen_width - self._display.get_width()) // 2,
            (screen_height - self._display.get_height()) // 2)
        self.screen.blit(self._display, display_position)

    def _get_xy(self, colrow: tuple):
        col, row = colrow
        return (col * self.font_width, row * self.font_height)

    def draw(self, xy: tuple, text: str, color: tuple = (255, 255, 255)):
        label = self.font.render(text, 1, color)
        self._display.blit(label, self._get_xy(xy))

    def render(self):
        self.screen.fill((15, 15, 15))
        self._draw_display()
        pygame.display.flip()

    def set_scene(self, scene):
        self.font_width, self.font_height = self.font.size('a')
        size = (self.config.DISPLAY_COLS * self.font_width,
                self.config.DISPLAY_ROWS * self.font_height)
        self._display = pygame.Surface(size)

        scene(self).loop()
