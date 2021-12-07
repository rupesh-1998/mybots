import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

from robot import ROBOT
from world import WORLD 

class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.world = WORLD()
        self.robot = ROBOT()
    
    def Run(self):
        #pyrosim.Prepare_To_Simulate("body.urdf")
        #self.robot.Prepare_To_Sense()

        for i in range(c.iterations):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Act(i)
            time.sleep(c.sleepTime)
        self.__del__()

    def __del__(self):
        #self.physicsClient.disconnect()
        pass

        