import pybullet as p

class WORLD:
    def __init__(self):
        #physicsClient = p.connect(p.GUI)
        #self.path=p.setAdditionalSearchPath(pybullet_data.getDataPath())
        #adding a floor
        self.planeId = p.loadURDF("plane.urdf")
        #self.bodyId = p.loadURDF("body.urdf")
        #self.robot = self.bodyId


        #loading the mininal world from generate.py
        p.loadSDF("min_wrld.sdf")

        #self.close=p.disconnect()
