import pyglet
from pyglet.gl import GL_BLEND
from Levels import *
from GameObject import *
from Interface_elements import *
from .Res.Resources import *


class Interface(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.res = resourses()
        self.buttons = []
        self.set_interface()

    def on_draw(self):
        glEnable(GL_BLEND)

        self.phon.blit(0, 0)

        for button in self.buttons:
            button.draw()

    def update(self, dt):
        pass

    def on_mouse_press(self, x, y, button, modifier):
        if (button == pyglet.window.mouse.LEFT):
            for button_interface in self.buttons:
                if button_interface.is_inside(x, y):
                    button_interface.action_if_clicked(self)


class Map(Interface):
    def set_interface(self):
        global level_passed

        self.phon = self.res.phon_menu
        self.buttons.append(Level_button(100, 200, self.res, 1))

        if level_passed >= 2:
            self.buttons.append(Level_button(200, 200, self.res, 2))

        if level_passed >= 3:
            self.buttons.append(Level_button(500, 200, self.res, 3))

        if level_passed >= 4:
            self.buttons.append(Level_button(600, 200, self.res, 4))

        if level_passed >= 5:
            self.buttons.append(Level_button(700, 200, self.res, 5))


class Ending(Interface):
    def set_interface(self):  # do not delete
        self.buttons.append(Menu_button(400, 100, self.res))
        global success
        if (success):
            self.phon = self.res.phon_success
        else:
            self.phon = self.res.phon_fail


if __name__ == "__main__":
    window = Map(800, 600)
    window.config.alpha_size = 8
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    pyglet.app.run()