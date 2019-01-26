from engine.engine import Engine
from engine.display import Display
from scenes import TestScene

if __name__ == '__main__':
    engine = Engine()
    display = Display()

    display.set_engine(engine)
    engine.set_scene(TestScene)
