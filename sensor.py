import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR():
    def __init__(self, linkname):
        self.linkname = linkname
        self.values = np.zeros(c.iterations)


    def Get_Value(self, t):
        self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        if(t==c.iterations-1):
            print(self.values)

    def Save_Values(self):
        np.save(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\sensorValues"+self.linkName+".npy",self.values)
