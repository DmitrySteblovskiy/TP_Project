class Boss(Unit):
    def __init__(self, x, y, res, hero):
        super().__init__(self, x, y, res)
        self.hero = hero
        self.picture = res.Zombie_boss
        self.hp = 1000

    def behave(self):
        if (self.hero.x <= self.x) and (self.ax > -30):
            self.ax -= 2

        elif (self.hero.x >= self.x) and (self.ax > 30):
            self.ax += 2

        elif (self.hero.y <= self.y) and (self.ay > -30):
            self.ay -= 2

        elif (self.hero.y >= self.x) and (self.ay < 30):
            self.ay += 2