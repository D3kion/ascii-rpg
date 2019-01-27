import pygame

from engine import Display
from engine.ui import Scene


class TestScene(Scene):
    def _draw(self):
        self.drawer.box((0, 0), (80, 35))
        self.display.draw((2, 2), 'Hello World!', (127, 0, 0))


class IntroScene(Scene):
    def loop(self):
        self._draw()
        self.display.render()

        pygame.time.delay(2500)
        self.display.set_scene(TestScene)

    def _draw(self):
        with open('./scenes/IntroScene') as f:
            text = [i.strip('\n') for i in f.readlines()]

        for i in range(len(text)):
            self.display.draw((9, 5+i), text[i], (223, 223, 255))
