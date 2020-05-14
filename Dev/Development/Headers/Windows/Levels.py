import pyglet
from pyglet.gl import GL_BLEND
from Resources import *
from GameObject import *
from Interface_elements import *


class Levels(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.create_objects_on_map()

        self.right_press = False
        self.left_press = False

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

    def on_key_release(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.left_press = False

        if symbol == key.RIGHT:
            self.right_press = False

    def on_key_press(self, symbol, modifiers):
        if symbol == key.LEFT:
            self.left_press = True
            self.hero.control(-1, 0)
        if symbol == key.RIGHT:
            self.right_press = True
            self.hero.control(1, 0)
        if symbol == key.UP:
            self.hero.jump()

        if symbol == key.DOWN:
            self.shoot = 1

    def update(self, dt):
        self.hero.update_positions(dt)
        self.clean_dead_bullets(dt)

        if self.right_press == False and self.left_press == False:
            self.hero.vx = 0

        self.shooting()

        for bul in self.bullets:
            bul.update_positions(dt)

        self.interaction_with_zombies(dt)

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

        label3 = pyglet.text.Label(self.mission,
                                   font_name='Times New Roman',
                                   font_size=26,
                                   x=200, y=10)

        label.draw()
        label2.draw()
        label3.draw()

    def interaction_with_zombies(self, dt):
        for z in self.zombies:
            z.behave()
            for bul in self.bullets:
                if self.collision_objects(dt, bul, z) == True and bul.dead == False:
                    bul.dead = True
                    z.hp -= 1


            if self.collision_objects(dt, self.hero, z) == True:
                self.hero.hp -= 1
            z.update_positions(dt)

    def clean_dead_zombies(self):
        i = len(self.zombies) - 1
        while i >= 0:
            if (self.zombies[i].hp <= 0):
                self.hero.points += self.zombies[i].cost
                del self.zombies[i]
            i -= 1

    def clean_dead_bullets(self, dt):
        i = len(self.bullets) - 1
        while i >= 0:
            if (self.collide_wall(dt, self.bullets[i])):
                self.bullets[i].dead = True
            if (self.bullets[i].dead == True):
                del self.bullets[i]
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
        self.mission = "kill all zombies"

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = []

        for i in range(10):
            self.zombies.append(Zombie_usual(randint(100, 200),
                                     randint(400, 600), res, self.hero))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(len(self.zombies) == 0):
            global success
            global level_passed

            success = True
            self.clear()
            self.on_close()

            if level_passed < 2:
                level_passed = 2
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level2(Levels):
    def create_objects_on_map(self):
        self.shoot = 0
        self.mission = "kill all zombies"

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = []
        for i in range(3):
            self.zombies.append(Zombie_usual(randint(100, 200),
                                             randint(400, 600), res, self.hero))
        for i in range(3):
            self.zombies.append(Zombie_fast(randint(100, 200),
                                             randint(400, 600), res, self.hero))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(len(self.zombies) == 0):
            global success
            global level_passed

            success = True
            self.clear()
            self.on_close()

            if level_passed < 3:
                level_passed = 3
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level3(Levels):
    def create_objects_on_map(self):
        self.shoot = 0
        self.mission = "kill all zombies"

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = []
        for i in range(3):
            self.zombies.append(Zombie_cloning(randint(100, 200),
                                             randint(400, 600), res, self.hero, self.zombies))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(len(self.zombies) == 0):
            global success
            global level_passed

            success = True
            self.clear()
            self.on_close()

            if level_passed < 4:
                level_passed = 4
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level4(Levels):
    def create_objects_on_map(self):
        self.shoot = 0
        self.mission = "kill all zombies"

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = []
        self.zombies.append(Zombie_Boss(randint(100, 200),
                                     randint(400, 600), res, self.hero, self.zombies))
        self.zombies.append(Zombie_Boss(randint(100, 200),
                                        randint(400, 600), res, self.hero, self.zombies))
        for i in range(3):
            self.zombies.append(Zombie_usual(randint(100, 200),
                                             randint(400, 600), res, self.hero))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(len(self.zombies) == 0):
            global success
            global level_passed

            success = True
            self.clear()
            self.on_close()

            if level_passed < 5:
                level_passed = 5
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()


class Level5(Levels):
    def create_objects_on_map(self):
        self.shoot = 0
        self.mission = "kill all zombies"

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = []
        for i in range(20):
            self.zombies.append(Zombie_Boss(randint(100, 200),
                                        randint(400, 600), res, self.hero, self.zombies))
        for i in range(30):
            self.zombies.append(Zombie_usual(randint(100, 200),
                                             randint(400, 600), res, self.hero))
        for i in range (20):
            self.zombies.append(Zombie_cloning(randint(100, 200),
                                            randint(400, 600), res, self.hero, self.zombies))
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(len(self.zombies) == 0):
            global success
            global level_passed

            success = True
            self.clear()
            self.on_close()

            if level_passed < 6:
                level_passed = 6
            window = Ending(800, 600)
            window.config.alpha_size = 8
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()
