import Unit.py
import Walls.py
import Bullets.py

class GameObject:
    def __init__(self, x, y, res):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

        self.ax = 0
        self.ay = -9.8

    def update_positions(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.vx += self.ax * dt
        self.vy += self.ay * dt

    def draw(self, x, y):
        self.picture.blit(x, y)