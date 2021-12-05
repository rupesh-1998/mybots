import pybullet as p
import time
import pybullet_data

#This creates an object, physicsClient, which handles the physics, 
#and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

#setting gravity
p.setGravity(0,0,-9.8)

#adding a floor
planeId = p.loadURDF("plane.urdf")
bodyId = p.loadURDF("body.urdf")

#loading the mininal world from generate.py
p.loadSDF("min_wrld.sdf")


#This statement increases the physics inside the world for a small amount. 
#For example, if an object is suspended above the ground, 
#it will move a small distance toward the ground, 
#because simulated gravity is pulling it down.
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()
