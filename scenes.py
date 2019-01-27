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
        if event.key == pygame.K_DOWN:
            if self.current_choice < 4:
                self.current_choice += 1
        elif event.key == pygame.K_UP:
            if self.current_choice > 0:
                self.current_choice -= 1

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
            (0, 0),
            (32, 16),
            (32, 17),
            (32, 18),
            (32, 19),
        )

        if self.current_choice:
            self.display.draw(pos[self.current_choice], '>', (0, 63, 0))
