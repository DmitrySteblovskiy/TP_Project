class Zombie_usual(Unit):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res)
        self.orientation = 1;
        self.hero = hero
        self.picture = res.Zombie_usual_right
        self.dead = False

    def behave(self):
        if (self.hero.x <= self.x):
            self.orientation = 0
            self.picture = self.res.Zombie_usual_left
            if self.vx > -40 * randint(1, 10):
                self.ax -= 20 * randint(1, 10)

            else:
                self.ax = 0
                self.vx = -40 * randint(1, 10)
        else:
            if (self.hero.x >= self.x):
                self.orientation = 1
                self.picture = self.res.Zombie_usual_right
                if self.vx < 40 * randint(1, 10):
                    self.ax += 20 * randint(1, 10)
                else:
                    self.vx = 40 * randint(1, 10)
                    self.ax = 0