import pyglet
import Interface.py


class Map(Interface):
    def set_interface(self):
        global levels_available
        self.buttons.append(Level_button(100, 0, self.res, 1))

        for button in self.buttons:
            button.draw()
