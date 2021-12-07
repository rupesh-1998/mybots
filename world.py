import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.worldId = p.loadSDF("min_wrld.sdf")
