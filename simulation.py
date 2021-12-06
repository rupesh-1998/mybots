import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import math
import random
import matplotlib.pyplot as plt

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
backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

backLegMotorValues = np.zeros(1000)
frontLegMotorValues = np.zeros(1000)

angs = np.linspace(-np.pi, np.pi, 1000)
targetAngs = (np.pi/4)*np.sin(angs)
#plt.plot(targetAngs)
#plt.show();

backLegamplitude = np.pi/4
backLegfrequency = 10
backLegphaseOffset = np.pi/4

frontLegamplitude = np.pi/4
frontLegfrequency = 10
frontLegphaseOffset = 0


pyrosim.Prepare_To_Simulate("body.urdf")
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("bLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("fLeg")

    backLegMotorValues[i] = backLegamplitude * np.sin(backLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + backLegphaseOffset)
    frontLegMotorValues[i] = frontLegamplitude * np.sin(frontLegfrequency * (((i/1000)*(2*np.pi))-(np.pi)) + frontLegphaseOffset)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robot,

    jointName = "Torso_bLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = backLegMotorValues[i],

    maxForce = 25)

    pyrosim.Set_Motor_For_Joint(

    bodyIndex = robot,

    jointName = "Torso_fLeg",

    controlMode = p.POSITION_CONTROL,

    targetPosition = frontLegMotorValues[i],

    maxForce = 25)

    
    if i < 19:
        print(random.random()-math.pi/2)
    time.sleep(1/60)
p.disconnect()

#print(backLegSensorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegSensorValues", backLegSensorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegSensorValues", frontLegSensorValues)

np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegMotorValues", backLegMotorValues)
np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegMotorValues", frontLegMotorValues)

