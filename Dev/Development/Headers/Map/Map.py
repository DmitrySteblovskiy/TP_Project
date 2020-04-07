import pyglet
import math
from random import randint
from OpenGL.GL import *
from pynput.mouse import Button, Controller
from pyglet.window import mouse

import level1.py

height = int(input())  # in pixels, please
width = int(input())  # in pixels, please


def createpolygons():  # we can actually make whatever and wherever we wish, but that's actually a pentagon
    angle = 2 * math.pi / 5
    vertex = [0, 0, 0]
    for i in range(4):
        x = vertex[i * 3] * math.cos(angle) - vertex[i * 3 + 1] * math.sin(angle)
        vertex.append(x)
        y = vertex[i * 3 + 1] * math.cos(angle) + vertex[i * 3] * math.sin(angle)
        vertex.append(y)
        vertex.append(0)
    return vertex


def colorpolygon():  # required to change the figure's color
    color = []
    for i in range(15):
        color.append(0)


"""class myWindow(pyglet.window.Window):   #some class
    def __init__(self, width, height, name):
        super().__init__(width, heigth, name, resizable=True)
        self.width = width
        self.height = height
        glClearColor(1, 1, 1, 1)
    def on_draw(self):
        self.clear()
"""

Map = pyglet.window.Window(height, width, "map", resizable=True)  # standard
glClearColor(1, 1, 1, 1)  # white background


class Mapwindow(pyglet.window.Window):  # Map Class

    def __init__(self, width, heigth, name):
        super().__init__(width, heigth, name, resizable=True)
        self.width = width
        self.height = heigth
        self.x = 0
        self.y = 0

        #
        self.pictures = SetResourses()
        (self.window_x, self.window_y) = self.get_size()
        self.compress_scale = self.window_y / self.pictures.background.height
        #

        glClearColor(1, 1, 1, 1)
        self.points = pyglet.graphics.vertex_list(4,
                                                  ('v3f/stream', createpolygons(4, -self.width / 2, -self.height / 2)),
                                                  ('c3B', colordata(4)))

    # time to detect all your actions

    def on_draw(self):  # creating my perfect pentagon
        self.clear()
        level_polygon = pyglet.graphics.vertex_list(('v3f/stream', createpolygons()), ('c3B', colorpolygon()))
        level_polygon.draw(GL_LINE_LOOP)

    def on_mouse_motion(self, x, y, dx, dy):  # the mouse's motion
        self.x = x
        self.y = y
        self.clear()
        level_polygon = pyglet.graphics.vertex_list(('v3f/stream', createpolygons()), ('c3B', colorpolygon()))
        level_polygon.draw(GL_LINE_LOOP)

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        zoom = 1.00
        if scroll_y > 0:
            zoom = 1.03
        elif scroll_y < 0:
            zoom = 0.97
        glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)

    def mouse_click(x, y, button, modifier):  # changing to the 1st level
        mouse = Controller()
        if (button == mouse.LEFT) & (mouse):  # trying to solve it
            self.clear()
            Gl.Load(Level1)




if __name__ == "__main__":  # running the game
    window = GameWindow(fullscreen=True)
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    pyglet.app.run()