import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random
import constants as c



#This creates an object, physicsClient, which handles the physics, 
#and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#setting gravity
p.setGravity(0,0,-9.8)

#adding a floor
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")
robot = bodyId


#loading the mininal world from generate.py
p.loadSDF("min_wrld.sdf")


#This statement increases the physics inside the world for a small amount. 
#For example, if an object is suspended above the ground, 
#it will move a small distance toward the ground, 
#because simulated gravity is pulling it down.
backLegSensorValues = np.zeros(c.iterations)
frontLegSensorValues = np.zeros(c.iterations)

backLegMotorValues = np.zeros(c.iterations)
frontLegMotorValues = np.zeros(c.iterations)

pyrosim.Prepare_To_Simulate("body.urdf")
for i in range(c.iterations):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("bLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("fLeg")

    backLegMotorValues[i] = c.backLegamplitude * np.sin(c.backLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + c.backLegphaseOffset)
    frontLegMotorValues[i] = c.frontLegamplitude * np.sin(c.frontLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + c.frontLegphaseOffset)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robot,

    jointName = "Torso_bLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = backLegMotorValues[i],

    maxForce = c.maxForce)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robot,

    jointName = "Torso_fLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = frontLegMotorValues[i],

    maxForce = c.maxForce)
    time.sleep(1/60)

p.disconnect()

#print(backLegSensorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegSensorValues", backLegSensorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegSensorValues", frontLegSensorValues)

np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegMotorValues", backLegMotorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegMotorValues", frontLegMotorValues)

