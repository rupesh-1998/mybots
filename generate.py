import pyrosim.pyrosim as pyrosim

def Create_World():
    pyrosim.Start_SDF("min_wrld.sdf")

    length, width, height = 1, 1, 1
    x, y, z = 5, 5, 0.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

    pyrosim.End()

def Generate_Body():
    pyrosim.Start_URDF("body.urdf")

    length, width, height = 1, 1, 1
    x, y, z = 1.5, 0, 1.5
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Torso_bLeg" , parent= "Torso" , child = "bLeg" , type = "revolute", position = "1 0 1")

    length, width, height = 1, 1, 1
    x, y, z = -0.5, 0, -0.5
    pyrosim.Send_Cube(name="bLeg", pos=[x,y,z] , size=[length, width, height])

    pyrosim.Send_Joint(name = "Torso_fLeg" , parent= "Torso" , child = "fLeg" , type = "revolute", position = "2 0 1")

    length, width, height = 1, 1, 1
    x, y, z = 0.5, 0, -0.5
    pyrosim.Send_Cube(name="fLeg", pos=[x,y,z] , size=[length, width, height])

    pyrosim.End()

def Generate_Brain():
    pyrosim.Start_NeuralNetwork("brain.nndf")

    pyrosim.Send_Sensor_Neuron(name = 0, linkName = "Torso")

    pyrosim.Send_Sensor_Neuron(name = 1, linkName = "bLeg")

    pyrosim.Send_Sensor_Neuron(name = 2, linkName = "fLeg")

    pyrosim.Send_Motor_Neuron(name = 3, jointName = "Torso_bLeg")

    pyrosim.Send_Motor_Neuron(name = 4, jointName = "Torso_fLeg")

    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()
