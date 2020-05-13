import pyglet
import Interface.py


class Ending(Interface):
    def set_interface(self):  # do not delete
        self.buttons.append(Menu_button(100, 0, self.res))
        global success
        if (success):
            self.labels.append(Text_button('WINNER WINNER - CHICKEN DINNER!',
                                      'Times New Roman',
                                      36, 400, 300))
            for button in self.buttons:
                button.draw()
        else:
            self.labels.append(Text_button('You have lost:(  Try again!',
                                      'Times New Roman',
                                      36, 400, 300))
            for button in self.buttons:
                button.draw()
