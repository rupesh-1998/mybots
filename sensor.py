import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim

class SENSOR():
    def __init__(self, linkname):
        self.linkname = linkname
        #print('linkname', self.linkname)


    def Get_Value(self):
        #self.values = np.zeros(c.iterations)
        ##self.values[self.t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        #print(self.values)
        print('NEW')
        self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkname)
        print('getval', self.linkname, self.values)