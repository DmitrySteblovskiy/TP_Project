import bomb_bullet.py
import sniper_bullet.py


class bullets(GameObject):
    def __init__(self, x, y, res, vx, vy):
        super().__init__(x, y, res)
        self.dead = False
        self.vx = vx
        self.vy = vy