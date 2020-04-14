class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.shoot = 0

        self.hero = Hero(10, 100, resourses())
        self.zombies = [Zombie_usual(randint(200, 300), randint(600, 800), resourses(), self.hero) for i in range(100)]

        self.walls = []

        self.walls.append(wall(10, 50, resourses(), "horiz", 780))
        self.walls.append(wall(300, 250, resourses(), "horiz", 200))

        self.walls.append(wall(10, 150, resourses(), "horiz", 100))
        self.walls.append(wall(690, 150, resourses(), "horiz", 100))

        self.walls.append(wall(10, 50, resourses(), "vert", 600))
        self.walls.append(wall(790, 50, resourses(), "vert", 600))

        self.bullets = []

    def on_draw(self):
        self.clear()
        self.hero.draw()

        text = "LOL NICE!"



        if(self.hero.hp < 0):
            if abs(self.hero.hp) < self.hero.points:
                text = "LOL U'RE NOT NOOB"

            elif abs(self.hero.hp) >= self.hero.points:
                text = "LOL U'RE NOOB"

            elif abs(self.hero.hp) > self.hero.points * 10:
                text = "LOL U'RE pro."

        print(len(self.bullets))

        label = pyglet.text.Label('hp ' + str(self.hero.hp),
                                  font_name='Times New Roman',
                                  font_size=36,
                                  x=10, y=10)

        label2 = pyglet.text.Label('points ' + str(self.hero.points),
                                   font_name='Times New Roman',
                                   font_size=36,
                                   x=600, y=10)

        label3 = pyglet.text.Label(text,
                                   font_name='Times New Roman',
                                   font_size=26,
                                   x=200, y=10)

        label.draw()
        label2.draw()
        label3.draw()

        for z in self.zombies:
            z.draw()
        for h in self.walls:
            h.draw()

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
                # if ((self.hero.y + self.hero.vy * dt < wall.y) and (self.hero.y + self.hero.picture.height + self.hero.vy * dt > wall.y) and (self.hero.x + self.hero.picture.width == wall.x)):
                # Hero.set_collision(self.hero, 0, -1, -1, -1)
                # if ((self.hero.y < wall.y) and (self.hero.y + self.hero.picture.height > wall.y) and
                # (self.hero.x == wall.x + wall.length)):
                # Hero.set_collision(self.hero, -1, 0, -1, -1)
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

            # wall.y <= abs(self.hero.y + abs(self.hero.vy) * dt) <= wall.y + 100

            # for zombie in self.zombies:
            # if (wall.orientation == "horiz"):
            # if ((abs(zombie.y - wall.y) <= abs(zombie.vy) * dt) and ((wall.x <= abs(zombie.x - abs(zombie.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(zombie.x + zombie.picture.width - abs(zombie.vx) * dt) <= wall.x + wall.length))):
            # self.zombie.concerns = True
            # Zombie_usual.set_collision(zombie, -1, -1, 0, 0)
            # if  ((abs(zombie.y + zombie.picture.height - wall.y) <= abs(zombie.vy) * dt) and ((wall.x <= abs(zombie.x - abs(zombie.vx) * dt) <= wall.x + wall.length) or (wall.x <= abs(zombie.x + zombie.picture.width - abs(zombie.vx) * dt) <= wall.x + wall.length))):  #удар башкой
            # Zombie_usual.set_collision(zombie, -1, -1, 0, -1)
            # if ((zombie.y < wall.y) and (zombie.y + zombie.picture.height > wall.y) and (zombie.x + zombie.picture.width == wall.x)):
            # Zombie_usual.set_collision(zombie, 0, -1, -1, -1)
            # if ((zombie.y < wall.y) and (zombie.y + zombie.picture.height > wall.y) and
            # (zombie.x == wall.x)):
            # Zombie_usual.set_collision(zombie, -1, 0, -1, -1)
            # else:
            # if ((abs(zombie.x - wall.x) <= abs(zombie.vx) * dt) and ((wall.y <= abs(zombie.y) <= wall.y + wall.length) or (wall.y <= abs(zombie.y + zombie.picture.height) <= wall.y + wall.length))): # стена слева
            # self.hero.concerns = True
            # Zombie_usual.set_collision(zombie, -1, 0, -1, -1)
            # elif ((abs(wall.x - zombie.x - zombie.picture.width - 1) <= abs(zombie.vx) * dt) and ((wall.y <= abs(zombie.y) <= wall.y + wall.length) or (wall.y <= abs(zombie.y + zombie.picture.height) <= wall.y + wall.length))): # стена справа
            # self.hero.concerns = True
            # Zombie_usual.set_collision(zombie, 0, -1, -1, -1)

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

        for i in range(len(self.bullets)):
            if (self.bullets[i].x >= 780) or (self.bullets[i].x <= 10):
                del self.bullets[i]
                break

        if self.shoot == 1:
            if self.hero.orientation == 1:
                self.bullets.append(sniper_bullet(self.hero.x + 20, self.hero.y + 30, resourses(), 500, 0))
                self.shoot = 0
            else:
                self.bullets.append(sniper_bullet(self.hero.x, self.hero.y + 30, resourses(), -500, 0))
                self.shoot = 0

        for bul in self.bullets:
            bul.update_positions(dt)

        for z in self.zombies:
            z.behave()

            for bul in self.bullets:
                if self.collision_objects(dt, bul, z) == True:
                    z.y += 1000
                    z.x = 500
                    self.hero.points += 1
                    bul.dead = True

            if self.collision_objects(dt, self.hero, z) == True:
                self.hero.hp -= 1

        for z in self.zombies:
            z.update_positions(dt)

        self.collision_walls(dt, self.hero)

        for zombie in self.zombies:
            self.collision_walls(dt, zombie)