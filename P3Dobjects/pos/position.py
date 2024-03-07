import P3Dobjects.data


class Position(P3Dobjects.data.Data):
    def __init__(self, x=0, y=0, z=0, w=0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.w = w