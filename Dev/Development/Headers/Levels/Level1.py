import pyglet
import Levels.py


class Level1(Levels):
    def create_objects_on_map(self):
        self.shoot = 0

        res = resourses()

        self.phon = res.phon_level_1
        self.hero = Hero(10, 100, res)
        self.zombies = [Zombie_usual(randint(100, 200),
                                     randint(400, 600),
                                     res,
                                     self.hero) for i in range(3)]
        self.walls = []
        self.walls.append(wall(0, 100, res, "horiz", 800))
        self.walls.append(wall(0, 250, res, "horiz", 200))
        self.walls.append(wall(600, 250, res, "horiz", 200))

        self.walls.append(wall(200, 400, res, "horiz", 400))

        self.walls.append(wall(0, 100, res, "vert", 1000))
        self.walls.append(wall(800, 100, res, "vert", 1000))

        self.bullets = []

    def level_completion(self):
        if(self.hero.points > 3):
            global success
            success = True
            self.clear()
            self.on_close()
            window = Ending(800, 600)
            pyglet.clock.schedule_interval(window.update, 1 / 60.0)
            pyglet.app.run()
