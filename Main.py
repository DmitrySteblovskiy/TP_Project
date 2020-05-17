from Windows import *


if __name__ == "__main__":
    window = Map(800, 600)
    window.config.alpha_size = 8
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    pyglet.app.run()