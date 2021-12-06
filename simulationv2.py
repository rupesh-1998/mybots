import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random
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
        pyrosim.Prepare_To_Simulate("body.urdf")
        self.robot.Prepare_To_Sense()
        for self.i in range(c.iterations):
            print('SIMI', self.i)
            p.stepSimulation()
            self.robot.Sense(self.i)
            ##backLegSensorValues[self.i] = pyrosim.Get_Touch_Sensor_Value_For_Link("bLeg")
            #frontLegSensorValues[self.i] = pyrosim.Get_Touch_Sensor_Value_For_Link("fLeg")

            #backLegMotorValues[self.i] = c.backLegamplitude * np.sin(c.backLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + c.backLegphaseOffset)
            #frontLegMotorValues[self.i] = c.frontLegamplitude * np.sin(c.frontLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + c.frontLegphaseOffset)

            #pyrosim.Set_Motor_For_Joint(

            #bodyIndex = robot,

            #jointName = "Torso_bLeg",

            #controlMode = p.POSITION_CONTROL,

            #targetPosition = backLegMotorValues[self.i],

            #maxForce = c.maxForce)

            #pyrosim.Set_Motor_For_Joint(

            #bodyIndex = robot,

            #jointName = "Torso_fLeg",

            #controlMode = p.POSITION_CONTROL,

            #targetPosition = frontLegMotorValues[self.i],

            #maxForce = c.maxForce)
            #time.sleep(1/600)

    def __del__(self):
        p.disconnect()

        