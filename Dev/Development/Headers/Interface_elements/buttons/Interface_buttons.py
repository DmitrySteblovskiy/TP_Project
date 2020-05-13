import pyglet
import Interface_elements.py


class Interface_buttons(Interface_elements):
    def is_inside(self, mouse_x, mouse_y):
        if mouse_x >= self.x and mouse_x <= self.x + self.picture.width:
            if mouse_y >= self.y and mouse_y <= self.y + self.picture.height:
                return True
        return False

    def draw(self):
        self.picture.blit(self.x, self.y)
