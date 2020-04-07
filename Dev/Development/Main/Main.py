import pyglet
from random import randint

import Resources.py
import GameObjects.py
import Map.py

if __name__ == "__main__":
    window = GameWindow(fullscreen=True)
    pyglet.clock.schedule_interval(window.update, 1/60.0)
    pyglet.app.run()