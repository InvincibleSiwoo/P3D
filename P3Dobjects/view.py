from P3Dobjects.object import P3DObject
from OpenGL.GL import *
from pywavefront import Wavefront


class View(P3DObject):
    def __init__(self, position=(0, 0, 0), obj_file_path="cube.obj"):
        super().__init__(view=True)
        self.position = position
        self.obj_file_path = obj_file_path

        if self.obj_file_path == "cube.obj":
            self.vertices = [
                [-0.5, -0.5, 0.5], [0.5, -0.5, 0.5], [0.5, 0.5, 0.5], [-0.5, 0.5, 0.5],
                [-0.5, -0.5, -0.5], [0.5, -0.5, -0.5], [0.5, 0.5, -0.5], [-0.5, 0.5, -0.5],
            ]
            self.faces = [
                (0, 1, 2, 3),
                (4, 5, 6, 7),
                (0, 1, 5, 4),
                (3, 2, 6, 7),
                (0, 3, 7, 4),
                (1, 2, 6, 5)
            ]
        else:
            mesh = Wavefront(self.obj_file_path)
            self.vertices = mesh.vertices
            self.faces = mesh.mesh_list[0].faces

    def draw(self):
        glBegin(GL_QUADS)
        for face in self.faces:
            for vertex_index in face:
                vertex = self.vertices[vertex_index]
                glVertex3f(vertex[0] + self.position[0],
                           vertex[1] + self.position[1],
                           vertex[2] + self.position[2])
        glEnd()
