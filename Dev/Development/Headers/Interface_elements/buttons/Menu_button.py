import pyglet
import Interface_buttons.py


class Menu_button(Interface_buttons):
    def __init__(self, x, y, res):
        super().__init__(x, y)

        self.picture = res.menu_map

    def action_if_clicked(self, window_current):
        window_current.clear()
        window_current.on_close()
        window = Map(800, 600)
        pyglet.clock.schedule_interval(window.update, 1 / 60.0)
        pyglet.app.run()
