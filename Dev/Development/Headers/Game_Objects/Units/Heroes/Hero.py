import Skin.py

class Hero(Unit):
    def __init__(self, x, y, res):
        super().__init__(self, x, y, res)
        self.picture = res.hero
        self.hp = 100

    def control(self, a_x, a_y):
        self.ax = a_x
        self.ay = a_y

    def shoot(self, bullet_type):
        #создание пули

