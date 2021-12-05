import pybullet as p
import time

#This creates an object, physicsClient, which handles the physics, and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)

#This statement increases the physics inside the world for a small amount. 
#For example, if an object is suspended above the ground, 
#it will move a small distance toward the ground, because simulated gravity is pulling it down.
for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
p.disconnect()
