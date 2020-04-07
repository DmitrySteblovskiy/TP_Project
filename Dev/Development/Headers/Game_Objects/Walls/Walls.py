class wall(GameObject):
    def __init__(self, x, y, res):
        super().__init__(self, x, y, res)
        self.picture = res.wall

