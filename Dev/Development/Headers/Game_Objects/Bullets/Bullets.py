import bomb_bullet.py
import sniper_bullet.py

class bullets(GameObject):
    def __init__(self, x, y, res, vx, vy):
        super().__init__(self, x, y, res)
        super.vx = vx
        super.vy = vy

