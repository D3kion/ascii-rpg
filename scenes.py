from engine.scene import Scene

from engine.display import Display


class TestScene(Scene):
    def loop(self):
        self._handle_events()
        self._draw()
        self.display.render()

        return True

    def _draw(self):
        self.display.draw((28, 12), '+-------------------+')
        self.display.draw((28, 13), '|     ASCII-RPG     |')
        self.display.draw((28, 14), '+-------------------+')
        self.display.draw((28, 15), '|                   |')
        self.display.draw((28, 16), '|     > Играть <    |')
        self.display.draw((28, 17), '|       Выйти       |')
        self.display.draw((28, 18), '|                   |')
        self.display.draw((28, 19), '+-------------------+')
