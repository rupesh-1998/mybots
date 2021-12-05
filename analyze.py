import numpy as np
import matplotlib.pyplot as plt

backLegdata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\backLegSensorValues.npy")
frontLegdata = np.load(r"C:\Users\rupes\Data Science Masters\Nature Inspired Computation\CW2\data\frontLegSensorValues.npy")


plt.plot(backLegdata, label='back', alpha=0.5)
plt.plot(frontLegdata, label='front', alpha=0.5)
plt.legend()
plt.show()