from Resources import *
#from Levels import *


class Interface_elements:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Interface_buttons(Interface_elements):
    def is_inside(self, mouse_x, mouse_y):
        if mouse_x >= self.x and mouse_x <= self.x + self.picture.width:
            if mouse_y >= self.y and mouse_y <= self.y + self.picture.height:
                return True
        return False

    def draw(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.picture.blit(self.x, self.y)


class Level_button(Interface_buttons):
    def __init__(self, x, y, res, level):
        super().__init__(x, y)
        self.level = level
        if self.level == 1:
            self.picture = res.menu_level_1
        if level == 2:
            self.picture = res.menu_level_2
        if level == 3:
            self.picture = res.menu_level_3
        if level == 4:
            self.picture = res.menu_level_4
        if level == 5:
            self.picture = res.menu_level_5

    def action_if_clicked(self, window_current):
        window_current.clear()
        window_current.on_close()

        if (self.level == 1):
            window = Level1(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 2):
            window = Level2(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 3):
            window = Level3(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 4):
            window = Level4(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 5):
            window = Level5(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Menu_button(Interface_buttons):
    def __init__(self, x, y, res):
        super().__init__(x, y)

        self.picture = res.menu_map

    def action_if_clicked(self, window_current):
        window_current.clear()
        window_current.on_close()
        window = Map(800, 600)
        glEnable(GL_BLEND)
        pyglet.clock.schedule_interval(window.update, 1 / 60.0)
        pyglet.app.run()


class Text_button(Interface_elements):
    def __init__(self, text, x, y):
        super().__init__(x,y)
        self.label = pyglet.text.Label(text, 'Times New Roman', 36, x, y)

    def draw(self):
        self.label.draw()
