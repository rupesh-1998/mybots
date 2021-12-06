import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c

from sensor import SENSOR

class ROBOT:
    def __init__(self):
        self.motors={}
        self.bodyId = p.loadURDF("body.urdf")
        self.robot = self.bodyId

    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) #each time this returns an instance of Sensor
            self.values = np.zeros(c.iterations)
          
    def Sense(self, t):
        for i in self.sensors:#each i is torso, bleg, fleg (link name)
           self.values[t] = SENSOR(i).Get_Value()
        