import sys
from random import randrange
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
        self.display.set_scene(MenuScene)

    def _draw(self):
        with open('./scenes/IntroScene') as f:
            text = [i.strip('\n') for i in f.readlines()]

        for i in range(len(text)):
            self.display.draw((9, 5+i), text[i], (223, 223, 255))


class MenuScene(Scene):
    def __init__(self, display: Display):
        super().__init__(display)

        self.current_choice = 1

    def _handle_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._handle_keys(event)

    def _handle_keys(self, event):
        if event.key in (pygame.K_DOWN, pygame.K_s):
            if self.current_choice < 4:
                self.current_choice += 1
        elif event.key in (pygame.K_UP, pygame.K_w):
            if self.current_choice > 0:
                self.current_choice -= 1
        elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
            if self.current_choice == 1:
                pass  # play
            elif self.current_choice == 2:
                pass  # open game wiki in browser
            elif self.current_choice == 3:
                pass  # settings
            elif self.current_choice == 4:
                sys.exit()

    def _draw(self):
        self.drawer.box((0, 0), (80, 35))
        self.drawer.box((29, 12), (21, 3))
        self.drawer.box((29, 14), (21, 8))

        self.display.draw((35, 13), 'ASCII-RPG')
        self.display.draw((34, 16), 'Играть')
        self.display.draw((34, 17), 'Вики')
        self.display.draw((34, 18), 'Настройки')
        self.display.draw((34, 19), 'Выйти')

        self._draw_pointer()

    def _draw_pointer(self):
        pos = (
            (32, 16),
            (32, 17),
            (32, 18),
            (32, 19),
        )

        if not self.current_choice:
            color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
            self.display.draw((35, 13), 'ASCII-RPG', color)
        else:
            self.display.draw(pos[self.current_choice-1], '>', (0, 63, 0))
