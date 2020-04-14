import Unit.py
import Walls.py
import Bullets.py

class GameObject:
    def __init__(self, x, y, res):
        self.res = res
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = -500
        self.concerns = False

    def update_positions(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx += self.ax * dt
        self.vy += self.ay * dt

        self.concerns = False

    def draw(self):
        self.picture.blit(self.x, self.y)