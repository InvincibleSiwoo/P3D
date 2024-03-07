from P3Dobjects.object import P3DObject

class Data(P3DObject):
    def __init__(self):
        super().__init__(view=False)

    def __str__(self):
        return "P3D Data"

    def __repr__(self):
        return "P3D Data"
