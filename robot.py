import pybullet as p
import pyrosim.pyrosim as pyrosim
import numpy as np
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
    def __init__(self):
        self.robot = p.loadURDF("body.urdf")
        self.nn = NEURAL_NETWORK("brain.nndf")
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) #each time this returns an instance of Sensor
          
    def Sense(self, t):
        for i in self.sensors:#each i is torso, bleg, fleg (link name)
           self.sensors[i].Get_Value(t)

    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            self.motors[jointName] = MOTOR(jointName)

    def Act(self, t):
         for i in self.motors:
            self.motors[i].Set_Value(self.robot, t)

    def Think(self):
        self.nn.Update()
        self.nn.Print()
       

    def Save(self):
        for i in self.sensors:
            self.sensors[i].Save_Values()