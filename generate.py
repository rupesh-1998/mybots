import pyrosim.pyrosim as pyrosim

# tell pyrosim where to store information about the world you'd like to create. 
# This world will currently be called box, 
# because it will only contain a box 
# (links can be spheres, cylinders, or boxes).
#pyrosim.Start_SDF("boxes.sdf")


#stores a box with initial position x=0, y=0, z=0.5, 
#and length, width and height all equal to 1 meter, in box.sdf



#x2, y2, z2 = 0, 1, 1.5
#pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length, width, height])

#for 6x6x10 tower of reducing sized blocks
#top=0
#for i in range(10):
#    for j in range(6):
#        for k in range(6):
#            length, width, height = 1*(0.9**i), 1*(0.9**i), 1*(0.9**i)
#            x, y, z = 0+j, 0+k, top + (0.5*height)
#            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])
#    top += height

def Create_World():
    pyrosim.Start_SDF("min_wrld.sdf")

    length, width, height = 1, 1, 1
    x, y, z = 5, 5, 0.5
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length, width, height])

    pyrosim.End()

def Create_Robot():
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


Create_World()
Create_Robot()
