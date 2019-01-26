import pygame

from . import Singleton
from .engine import Engine


class Display(metaclass=Singleton):
    def _draw_display(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        display_position = (
            (screen_width - self._display.get_width()) // 2,
            (screen_height - self._display.get_height()) // 2)
        self._screen.blit(self._display, display_position)

    def _get_xy(self, colrow: tuple):
        col, row = colrow
        return (col * self.font_width, row * self.font_height)

    def set_engine(self, engine: Engine):
        self._engine = engine
        self._config = engine.config
        self._screen = engine.screen
        self._font = engine.font

        self.font_width, self.font_height = self._font.size('a')
        size = (self._config.DISPLAY_COLS * self.font_width,
                self._config.DISPLAY_ROWS * self.font_height)
        self._display = pygame.Surface(size)

        self.render()

    def draw(self, xy: tuple, text: str, color: tuple = (255, 255, 255)):
        label = self._font.render(text, 1, color)
        self._display.blit(label, self._get_xy(xy))

    def render(self):
        self._draw_display()
        pygame.display.flip()
