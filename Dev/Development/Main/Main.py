import pyglet
from random import randint
from pyglet.window import key
from pyglet.gl import GL_LINES, glEnable, GL_BLEND, glBlendFunc, GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA
from pynput.mouse import Controller


progress = 1
success = False
level_passed = 0

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
        self.phon_success = pyglet.image.load('phon_success.png')
        self.phon_fail = pyglet.image.load('fail.png')
        self.phon_menu = pyglet.image.load('phon_menu.png')

        self.zombie_fast_left = pyglet.image.load('zombie_fast_left.png')
        self.zombie_fast_right = pyglet.image.load('zombie_fast_right.png')


class Interface_elements:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Interface_buttons(Interface_elements):
    def is_inside(self, mouse_x, mouse_y):
        if mouse_x >= self.x and mouse_x <= self.x + self.picture.width:
            if mouse_y >= self.y and mouse_y <= self.y + self.picture.height:
                return True
        return False

    def draw(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        self.picture.blit(self.x, self.y)


class Level_button(Interface_buttons):
    def __init__(self, x, y, res, level):
        super().__init__(x, y)
        self.level = level
        if self.level == 1:
            self.picture = res.menu_level_1
        if level == 2:
            self.picture = res.menu_level_2
        if level == 3:
            self.picture = res.menu_level_3

    def action_if_clicked(self, window_current):
        window_current.clear()
        window_current.on_close()

        if (self.level == 1):
            window = Level1(800, 500)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 2):
            window = Level2(1200, 1080)
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()

        elif (self.level == 3):
            window = Level3(900, 600)
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Menu_button(Interface_buttons):
    def __init__(self, x, y, res):
        super().__init__(x, y)

        self.picture = res.menu_map

    def action_if_clicked(self, window_current):
        window_current.clear()
        window_current.on_close()
        window = Map(800, 600)
        glEnable(GL_BLEND)
        pyglet.clock.schedule_interval(window.update, 1 / 60.0)
        pyglet.app.run()


class Text_button(Interface_elements):
    def __init__(self, text, x, y):
        super().__init__(x,y)
        print ("b")
        self.label = pyglet.text.Label(text, 'Times New Roman', 36, x, y)

    def draw(self):
        self.label.draw()
        print ("a")


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


class Zombie_usual(Zombie):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res, hero)
        self.hp = 1
        self.velocity = 40
        self.cost = 1

        self.left_pict = self.res.Zombie_usual_left
        self.right_pict = self.res.Zombie_usual_right

class Zombie_fast(Zombie):
    def __init__(self, x, y, res, hero):
        super().__init__(x, y, res, hero)
        self.hp = 1
        self.velocity = 60
        self.cost = 5

        self.left_pict = self.res.zombie_fast_left
        self.right_pict = self.res.zombie_fast_right





class Zombie_Boss(Unit):
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
        if ((self.y == 0) or (self.concerns == True)):
            self.vy = self.jump_speed


class wall(GameObject):
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


class Interface(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.res = resourses()
        self.buttons = []
        self.set_interface()

    def on_draw(self):
        glEnable(GL_BLEND)

        self.phon.blit(0, 0)

        for button in self.buttons:
            button.draw()

    def update(self, dt):
        pass

    def on_mouse_press(self, x, y, button, modifier):
        if (button == pyglet.window.mouse.LEFT):
            for button_interface in self.buttons:
                if button_interface.is_inside(x, y):
                    button_interface.action_if_clicked(self)


class Map(Interface):
    def set_interface(self):
        global levels_available
        self.phon = self.res.phon_menu
        self.buttons.append(Level_button(100, 0, self.res, 1))


class Ending(Interface):
    def set_interface(self):  # do not delete
        self.buttons.append(Menu_button(400, 100, self.res))
        global success
        if (success):
            self.phon = self.res.phon_success
        else:
            self.phon = self.res.phon_fail


class Levels(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_objects_on_map()

    def on_draw(self):
        glEnable(GL_BLEND)

        self.phon.blit(0, 0)
        self.hero.draw()

        self.draw_interface()

        for z in self.zombies:
            z.draw()

        for bul in self.bullets:
            bul.draw()

    def collision_walls(self, dt, object1):
        for wall in self.walls:
            if (wall.orientation == "horiz"):
                if ((abs(object1.y - wall.y) <= abs(object1.vy) * dt) and (
                        (wall.x <= abs(object1.x - abs(object1.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(
                    object1.x + object1.picture.width - abs(object1.vx) * dt) <= wall.x + wall.length))):
                    object1.concerns = True
                    object1.y = wall.y
                    object1.set_collision(-1, -1, 0, 0)
                if ((abs(object1.y + object1.picture.height - wall.y) <= abs(object1.vy) * dt) and (
                        (wall.x <= abs(object1.x - abs(object1.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(
                    object1.x + object1.picture.width - abs(
                        object1.vx) * dt) <= wall.x + wall.length))):  # удар башкой
                    object1.set_collision(-1, -1, 0, -1)
            else:
                if ((abs(object1.x - wall.x) <= abs(object1.vx) * dt) and (
                        (wall.y <= abs(object1.y) <= wall.y + wall.length) or (
                        wall.y <= abs(object1.y + object1.picture.height) <= wall.y + wall.length))):  # стена слева
                    object1.concerns = True
                    object1.x = wall.x + 1
                    object1.set_collision(-1, 0, -1, -1)
                elif ((abs(wall.x - object1.x - object1.picture.width) <= abs(object1.vx) * dt) and (
                        (wall.y <= abs(object1.y) <= wall.y + wall.length) or (
                        wall.y <= abs(object1.y + object1.picture.height) <= wall.y + wall.length))):  # стена справа
                    object1.concerns = True
                    object1.x = wall.x - object1.picture.width - 1
                    object1.set_collision(0, -1, -1, -1)

    def collide_wall(self, dt, object1):
        for wall in self.walls:
            if (wall.orientation == "horiz"):
                if ((abs(object1.y - wall.y) <= abs(object1.vy) * dt) and (
                        (wall.x <= abs(object1.x - abs(object1.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(
                    object1.x + object1.picture.width - abs(object1.vx) * dt) <= wall.x + wall.length))):
                    object1.concerns = True
                    object1.y = wall.y
                    object1.dead = True
                if ((abs(object1.y + object1.picture.height - wall.y) <= abs(object1.vy) * dt) and (
                        (wall.x <= abs(object1.x - abs(object1.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(
                    object1.x + object1.picture.width - abs(
                        object1.vx) * dt) <= wall.x + wall.length))):  # удар башкой
                    object1.dead = True
            else:
                if ((abs(object1.x - wall.x) <= abs(object1.vx) * dt) and (
                        (wall.y <= abs(object1.y) <= wall.y + wall.length) or (
                        wall.y <= abs(object1.y + object1.picture.height) <= wall.y + wall.length))):  # стена слева
                    object1.concerns = True
                    object1.x = wall.x + 1
                    object1.dead = True
                elif ((abs(wall.x - object1.x - object1.picture.width) <= abs(object1.vx) * dt) and (
                        (wall.y <= abs(object1.y) <= wall.y + wall.length) or (
                        wall.y <= abs(object1.y + object1.picture.height) <= wall.y + wall.length))):  # стена справа
                    object1.concerns = True
                    object1.x = wall.x - object1.picture.width - 1
                    object1.dead = True
    def collision_objects(self, dt, object1, object2):
        if ((object2.x <= object1.x + object1.picture.width <= object2.x + object2.picture.width) and (
                (object2.y <= object1.y <= object2.y + object2.picture.height) or (
                object2.y <= object1.y + object1.picture.height <= object2.y + object2.picture.height))):
            return True

        if ((object2.x <= object1.x <= object2.x + object2.picture.width) and (
                (object2.y <= object1.y <= object2.y + object2.picture.height) or (
                object2.y <= object1.y + object1.picture.height <= object2.y + object2.picture.height))):
            return True

        if (object1.y <= object2.y <= object2.y + object2.picture.height <= object1.y + object1.picture.height) and (
                (object2.x <= object1.x <= object2.x + object2.picture.width) or (
                object2.x <= object1.x + object1.picture.width <= object2.x + object2.picture.width)):
            return True

        if (object1.x <= object2.x <= object2.x + object2.picture.width <= object1.x + object1.picture.width) and (
                (object2.y <= object1.y <= object2.y + object2.picture.height) or (
                object2.y <= object1.y + object1.picture.height <= object2.y + object2.picture.height)):
            return True

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.hero.control(-1, 0)
        if symbol == key.RIGHT:
            self.hero.control(1, 0)
        if symbol == key.UP:
            self.hero.jump()

        if symbol == key.DOWN:
            self.shoot = 1

    def update(self, dt):
        self.hero.update_positions(dt)

        i = len(self.bullets) - 1
        while i >= 0:
            if (self.collide_wall(dt, self.bullets[i])):
                self.bullets[i].dead = True
            if (self.bullets[i].dead == True):
                self.bullets[i].y -= 1000
                del self.bullets[i]
            i -= 1

        print (len(self.bullets))

        self.shooting()

        for bul in self.bullets:
            bul.update_positions(dt)

        for z in self.zombies:
            z.behave()
            for bul in self.bullets:
                if self.collision_objects(dt, bul, z) == True:
                    bul.dead = True
                    z.hp -= 1
                    self.hero.points += z.cost

            if self.collision_objects(dt, self.hero, z) == True:
                self.hero.hp -= 1
            z.update_positions(dt)

        self.clean_dead_zombies()
        self.death_condition()

        self.collision_walls(dt, self.hero)

        for zombie in self.zombies:
            self.collision_walls(dt, zombie)
        self.level_completion()

    def draw_interface(self):
        label = pyglet.text.Label('hp ' + str(self.hero.hp),
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=10, y=10)

        label2 = pyglet.text.Label('points ' + str(self.hero.points),
                                   font_name='Times New Roman',
                                   font_size=36,
                                   x=600, y=10)

        label3 = pyglet.text.Label("kill 4 zombies",
                                   font_name='Times New Roman',
                                   font_size=26,
                                   x=200, y=10)

        label.draw()
        label2.draw()
        label3.draw()

    def clean_dead_zombies(self):
        i = len(self.zombies) - 1
        while i >= 0:
            if (self.zombies[i].hp <= 0):
                del self.zombies[i]
            i -= 1

    def death_condition(self):
        global success
        if (self.hero.hp <= 0):
            success = False
            self.clear()
            self.on_close()
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()
    def shooting(self):
        if self.shoot == 1:
            if self.hero.orientation == 1:
                self.bullets.append(sniper_bullet(self.hero.x + 20, self.hero.y + 30, resourses(), 500, 0))
                self.shoot = 0
            else:
                self.bullets.append(sniper_bullet(self.hero.x, self.hero.y + 30, resourses(), -500, 0))
                self.shoot = 0

class Level1(Levels):
    def create_objects_on_map(self):
        self.shoot = 0

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = [Zombie_usual(randint(100, 200),
                                     randint(400, 600),
                                     res,
                                     self.hero) for i in range(5)]
        for i in range (2):
            self.zombies.append(Zombie_fast(randint(100, 200),
                                     randint(400, 600),
                                     res,
                                     self.hero))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(self.hero.points >= 15):
            global success
            success = True
            self.clear()
            self.on_close()
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level2(Levels):
    def create_objects_on_map(self):
        self.shoot = 0

        self.hero = Hero(10, 100, resourses())
        self.zombies = [Zombie_usual(randint(100, 200),
                                     randint(400, 600),
                                     resourses(),
                                     self.hero) for i in range(3)]
        self.walls = []
        self.walls.append(wall(10,
                               50,
                               resourses(),
                               "horiz",
                               780))

        self.walls.append(wall(100,
                               150,
                               resourses(),
                               "horiz",
                               400))

        self.walls.append(wall(10,
                               50,
                               resourses(),
                               "vert",
                               600))
        self.walls.append(wall(790, 50, resourses(), "vert", 600))

        self.bullets = []

    def level_completion(self):
        if(self.hero.points > 50):
            self.clear()
            self.on_close()
            window = Ending(800, 600)
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level3(Levels):
    def create_objects_on_map(self):
        self.shoot = 0

        self.hero = Hero(10, 100, resourses())
        self.zombies = [Zombie_usual(randint(100, 200),
                                     randint(400, 600),
                                     resourses(),
                                     self.hero) for i in range(3)]
        self.walls = []
        self.walls.append(wall(10,
                               50,
                               resourses(),
                               "horiz",
                               780))

        self.walls.append(wall(100,
                               150,
                               resourses(),
                               "horiz",
                               400))

        self.walls.append(wall(10,
                               50,
                               resourses(),
                               "vert",
                               600))
        self.walls.append(wall(790, 50, resourses(), "vert", 600))

        self.bullets = []

    def level_completion(self):
        if(self.hero.points > 250):
            self.clear()
            self.on_close()
            window = Ending(800, 600)
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


if __name__ == "__main__":
    window = Map(800, 600)
    window.config.alpha_size = 8
    pyglet.clock.schedule_interval(window.update, 1 / 60.0)
    pyglet.app.run()