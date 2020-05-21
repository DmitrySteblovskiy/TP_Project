from Resources import *
from abc import ABC


class GameObject(ABC):
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
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.picture.blit(self.x, self.y)


class Unit(GameObject):
    def set_collision(self, x_right_velocity=-1, x_left_velocity=-1,
                      y_up_velocity=-1, y_down_velocity=-1):
        if (x_right_velocity >= 0) and (self.vx >= 0):
            self.vx = x_right_velocity
        if (x_left_velocity >= 0) and (self.vx <= 0):
            self.vx = -x_left_velocity
        if (y_up_velocity >= 0) and (self.vy >= 0):
            self.vy = y_up_velocity
        if (y_down_velocity >= 0) and (self.vy <= 0):
            self.vy = -y_down_velocity

    def friction(self):
        if (self.vx < -10):
            self.ax = 100;
        if (self.vx > 10):
            self.ax = -100


class Zombie(Unit):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res)
        self.orientation = 1;
        self.hero = hero
        self.dead = False

    def behave(self):
        self.extra_ection()
        if (self.hero.x <= self.x):
            self.orientation = 0
            self.picture = self.left_pict
            if self.vx > -self.velocity * randint(1, 10):
                self.ax -= self.velocity/2 * randint(1, 10)

            else:
                self.ax = 0
                self.vx = -self.velocity * randint(1, 10)
        else:
            if (self.hero.x >= self.x):
                self.orientation = 1
                self.picture = self.right_pict
                if self.vx < self.velocity * randint(1, 10):
                    self.ax += self.velocity/2 * randint(1, 10)
                else:
                    self.vx = self.velocity * randint(1, 10)
                    self.ax = 0

    def extra_ection(self):
        pass


class ZombieUsual(Zombie):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res, hero)
        self.hp = 1
        self.velocity = 40
        self.cost = 1

        self.left_pict = self.res.Zombie_usual_left
        self.right_pict = self.res.Zombie_usual_right

        self.picture = self.left_pict


class ZombieFast(Zombie):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res, hero)
        self.hp = 1
        self.velocity = 60
        self.cost = 5

        self.left_pict = self.res.ZombieFast_left
        self.right_pict = self.res.ZombieFast_right
        self.picture = self.left_pict


class ZombieBoss(Zombie):
    def __init__(self, x, y, res, hero, zombies):
        super().__init__(x, y, res, hero)
        self.hp = 10
        self.velocity = 20
        self.cost = 100
        self.time = 0

        self.zombies = zombies

        self.left_pict = self.res.boss_left
        self.right_pict = self.res.boss_right
        self.picture = self.left_pict

    def extra_ection(self):
        self.time += 1
        if self.time >= 100:
            if (len (self.zombies) < 300):
                self.zombies.append(ZombieFast(self.x, self.y, self.res, self.hero))
            self.time = 1


class ZombieСloning(Zombie):
    def __init__(self, x, y, res, hero, zombies):
        super().__init__(x, y, res, hero)
        self.hp = 1
        self.velocity = 40
        self.cost = 1
        self.time = 0

        self.jump_speed = randint(100, 200)

        self.zombies = zombies

        self.left_pict = self.res.cloning
        self.right_pict = self.res.cloning
        self.picture = self.left_pict

    def extra_ection(self):
        self.time += 1
        if self.time >= 100:
            if len(self.zombies) < 100:
                self.zombies.append(ZombieСloning(self.x, self.y, self.res, self.hero, self.zombies))
            self.time = 1


        if ((self.y == 0) or (self.concerns == True)):
            self.vy = self.jump_speed

class Hero(Unit):
    def __init__(self, x, y, res):
        super().__init__(x, y, res)
        self.orientation = 1
        self.picture = res.hero_right
        self.hp = 100
        self.jump_speed = 400  # default
        self.points = 0

    def control(self, a_x, a_y):
        if a_x == -1:
            self.picture = self.res.hero_left
            self.orientation = -1

            self.vx = -300
        elif a_x == 1:
            self.picture = self.res.hero_right
            self.orientation = 1

            self.vx = 300

    def jump(self):
        if (self.concerns == True):
            self.vy = self.jump_speed


class Wall(GameObject):
    def __init__(self, x, y, res, orientation, length):
        super().__init__(x, y, res)
        self.ay = 0
        self.orientation = orientation
        self.length = length

    def draw(self):
        if (self.orientation == "horiz"):
            line = pyglet.graphics.vertex_list(2, ('v3f/stream', [self.x, self.y, 0, self.x + self.length, self.y, 0]),
                                               ('c3B', [255, 0, 100, 255, 0, 100]))
            line.draw(GL_LINES)

        else:
            line = pyglet.graphics.vertex_list(2, ('v3f/stream', [self.x, self.y, 0, self.x, self.y + self.length, 0]),
                                               ('c3B', [255, 0, 100, 255, 0, 100]))
            line.draw(GL_LINES)


class bullets(GameObject):
    def __init__(self, x, y, res, vx, vy):
        super().__init__(x, y, res)
        self.dead = False
        self.vx = vx
        self.vy = vy


class bomb_bullet(bullets):
    def __init__(self, x, y, res, vx, vy):
        super().__init__(x, y, res, vx, vy)
        self.picture = res.bomb_bullet


class sniper_bullet(bullets):
    def __init__(self, x, y, res, vx, vy):
        super().__init__(x, y, res, vx, vy)
        self.picture = res.sniper_bullet
        self.ay = 0
