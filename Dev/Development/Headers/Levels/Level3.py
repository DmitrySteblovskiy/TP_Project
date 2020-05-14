<<<<<<< HEAD
import pyglet
import Levels.py


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
=======
class Level1(pyglet.window.Window):

    def __init__(self, width, heigth, name):
        self.width = width
        self.height = heigth
        self.x = 0
        self.y = 0
        glClearColor(1, 1, 1, 1)
        self.points = pyglet.graphics.vertex_list(4,
                                                  ('v3f/stream', createpolygons(4, -self.width / 2, -self.height / 2)),
                                                  ('c3B', colordata(4)))

    def on_draw(self):
        self.clear()
        self.points.draw(gl.GL_LINE_LOOP)

    def on_mouse_motion(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.points = pyglet.graphics.vertex_list(4, (
            'v3f/stream', createpolygons(4, x - self.width / 2, y - self.height / 2)), ('c3B', colordata(4)))

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        zoom = 1.00
        if scroll_y > 0:
            zoom = 1.03
        elif scroll_y < 0:
            zoom = 0.97
        glOrtho(-zoom, zoom, -zoom, zoom, -1, 1)
>>>>>>> Laga
