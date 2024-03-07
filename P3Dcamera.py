from OpenGL.GLU import gluLookAt
from math import sin, cos, radians

from P3Dobjects.pos.position import Position

class Camera:
    def __init__(self, position=(0, 0, 0), pitch=0, yaw=0, roll=0):
        self.position = Position(*position)
        self.pitch = pitch
        self.yaw = yaw
        self.roll = roll

    def look(self):
        x = cos(radians(self.pitch)) * cos(radians(self.yaw))
        y = sin(radians(self.pitch))
        z = sin(radians(self.yaw)) * cos(radians(self.pitch))
        target = [self.position.x + x, self.position.y + y, self.position.z + z]
        gluLookAt(self.position.x, self.position.y, self.position.z, *target, 0, 1, 0)
