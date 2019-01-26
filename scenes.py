from engine import Display
from engine.ui import Scene


class TestScene(Scene):
    def loop(self):
        self._running = True
        while self._running:
            self._handle_events()
            self._draw()
            self.display.render()
            self.clock.tick(10)

    def _draw(self):
        self.drawer.box((0, 0), (80, 35))
        self.display.draw((2, 2), 'Hello World!', (127, 0, 0))

    # def _draw(self):
    #     self.display.draw((28, 12), '+-------------------+')
    #     self.display.draw((28, 13), '|     ASCII-RPG     |')
    #     self.display.draw((28, 14), '+-------------------+')
    #     self.display.draw((28, 15), '|                   |')
    #     self.display.draw((28, 16), '|     > Играть <    |')
    #     self.display.draw((28, 17), '|       Выйти       |')
    #     self.display.draw((28, 18), '|                   |')
    #     self.display.draw((28, 19), '+-------------------+')
