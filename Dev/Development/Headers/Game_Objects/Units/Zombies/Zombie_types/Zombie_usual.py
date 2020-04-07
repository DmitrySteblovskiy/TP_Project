class Zombie_usual(Unit):
    def __init__(self, x, y, res, hero):
        super().__init__(self, x, y, res)
        self.hero = hero
        self.picture = res.Zombie_usual
        self.hp = 100

    def behave(self):
        if (self.hero.x <= self.x) and (self.ax > -3):
            self.ax -= 1

        elif (self.hero.x >= self.x) and (self.ax > 3):
            self.ax += 1

        elif (self.hero.y <= self.y) and (self.ay > -3):
            self.ay -= 1

        elif (self.hero.y >= self.x) and (self.ay < 3):
            self.ay += 1