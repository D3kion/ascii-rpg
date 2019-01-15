import sys

import pygame
from pygame.locals import *

from scenes import IntroScene, Scene


def get_xy(colrow: tuple):
    return (colrow[0] * 10, colrow[1] * 15)


class Engine:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('ascii-rpg')

        self.screen = pygame.display.set_mode((1024, 768), RESIZABLE)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont('consolas', 15)

        self.screen_size = pygame.display.get_surface().get_size()
        self.cols, self.rows = 80, 35

        fontsize = self.font.size('a')
        self.size = self.width, self.height = (
            self.cols * fontsize[0],
            self.rows * fontsize[1]
        )

        self.display = pygame.Surface(self.size)

        # self.renderer = Renderer(self)
        # self.scene = IntroScene()

    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((10, 10, 10))

            self.screen.blit(
                self.display,
                ((self.screen_size[0] - self.display.get_height) // 2,
                 (self.screen_size[1] - self.display.get_width) // 2)
            )

            # self.renderer.render_scene(
            #     self.scene,
            #     ((self.cols - 34) // 2, (self.rows - 7) // 2))

            pygame.display.flip()
            self.clock.tick(10)


class Renderer:
    def __init__(self, engine: Engine):
        self.screen = engine.screen
        self.font = engine.font

    def render_row(self, text: str, cursor: tuple,
                   color: tuple = (255, 255, 255)):
        for i in range(len(text)):
            label = self.font.render(text[i], 1, color)
            self.screen.blit(label, get_xy(cursor))
            cursor = (cursor[0] + 1, cursor[1])

    def render_scene(self, scene: Scene, cursor: tuple = (0, 0)):
        content = scene.content
        for row in range(len(content)):
            self.render_row(content[row], cursor)
            cursor = (cursor[0], cursor[1] + 1)
