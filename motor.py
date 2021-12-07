import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.Prepare_To_Act()
        print(self.jointName)

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.phaseOffset = c.phaseOffset
        self.maxForce = c.maxForce

        self.motorValues = self.amplitude * np.sin(self.frequency * np.linspace(-np.pi, np.pi, 1000) + self.phaseOffset)

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(bodyIndex = robot,
                                jointName = self.jointName, 
                                controlMode = p.POSITION_CONTROL,
                                targetPosition = self.motorValues[t],
                                maxForce = self.maxForce)
    def Save_Values(self):
        np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\sensorValues"+self.jointName+".npy",self.motorValues)

        
