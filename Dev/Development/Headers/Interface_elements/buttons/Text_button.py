import pyglet
import Interface_elements.py


class Text_button(Interface_elements):
    def __init__(self, text, font_name, font_size, x, y):
        super().__init__(x,y)
        self.label = pyglet.text.Label(self.text, self.font_name,self.font_size, self.x, self.y)

    def draw(self):
        self.label.draw()
