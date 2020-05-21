import pyglet
from random import randint
from pyglet.window import key
from pyglet.gl import GL_LINES, glEnable, GL_BLEND, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA


class resources:
    file = open('Globals.txt')
    globals = file.read()
    info = globals.split(' ')
    success = bool(info[2])
    level_passed = int(info[5])
    file.close()

    def __init__(self):
        self.Zombie_usual_right = pyglet.image.load('res/zombie_right.png')
        self.Zombie_usual_left = pyglet.image.load('res/zombie_left.png')
        self.hero_right = pyglet.image.load('res/hero_right.png')
        self.hero_left = pyglet.image.load('res/hero_left.png')
        self.sniper_bullet = pyglet.image.load('res/bullet.png')
        self.menu_level_1 = pyglet.image.load('res/icon_level_1.png')
        self.menu_level_2 = pyglet.image.load('res/icon_level_2.png')
        self.menu_level_3 = pyglet.image.load('res/icon_level_3.png')
        self.menu_level_4 = pyglet.image.load('res/icon_level_4.png')
        self.menu_level_5 = pyglet.image.load('res/icon_level_5.png')
        self.phon_level_1 = pyglet.image.load('res/level_1_phon.bmp')
        self.menu_map = pyglet.image.load('res/icon_map.png')
        self.phon_success = pyglet.image.load('res/phon_success.png')
        self.phon_fail = pyglet.image.load('res/fail.png')
        self.phon_menu = pyglet.image.load('res/phon_menu.png')

        self.ZombieFast_left = pyglet.image.load('res/zombie_fast_left.png')
        self.ZombieFast_right = pyglet.image.load('res/zombie_fast_right.png')

        self.boss_left = pyglet.image.load('res/boss_left.png')
        self.boss_right = pyglet.image.load('res/boss_right.png')

        self.cloning = pyglet.image.load('res/cloning.png')


