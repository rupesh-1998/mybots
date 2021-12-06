import numpy as np
import matplotlib.pyplot as plt

backLegSensordata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegSensorValues.npy")
frontLegSensordata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegSensorValues.npy")

backLegMotordata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegMotorValues.npy")
frontLegMotordata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegMotorValues.npy")


plt.plot(backLegMotordata, label='back', alpha=0.5)#, linewidth=4)
plt.plot(frontLegMotordata, label='front', alpha=0.5)#, linewidth=2)
plt.legend()
plt.show()