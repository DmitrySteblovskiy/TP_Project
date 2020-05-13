import pyglet
import Levels.py


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

