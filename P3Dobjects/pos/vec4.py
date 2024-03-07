import P3Dobjects.data

class Vec4(P3Dobjects.data.Data):
    def __init__(self, x=0, y=0, z=0, w=0):
        super().__init__()
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other):
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z + self.w * other.w
