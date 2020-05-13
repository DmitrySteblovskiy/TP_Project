import pyglet


class resourses:
    def __init__(self):
        self.Zombie_usual_right = pyglet.image.load('zombie_right.png')
        self.Zombie_usual_left = pyglet.image.load('zombie_left.png')
        self.hero_right = pyglet.image.load('hero_right.png')
        self.hero_left = pyglet.image.load('hero_left.png')
        self.sniper_bullet = pyglet.image.load('bullet.png')
        self.menu_level_1 = pyglet.image.load('icon_level_1.png')
        self.menu_level_2 = pyglet.image.load('icon_level_2.png')
        self.menu_level_3 = pyglet.image.load('icon_level_3.png')
        self.phon_level_1 = pyglet.image.load('level_1_phon.bmp')
        self.menu_map = pyglet.image.load('icon_map.png')