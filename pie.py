import matplotlib.pyplot as plt
import numpy as np
x=["25%","40%","55%","70%","85%","100%"]
y=np.array([100,75,50,25,0])
plt.xlabel("Watering Percentage")
plt.ylabel("Soil Moisture Percentage")
z=np.array([25,27,29,31,33,35])



plt.plot(x,y)
plt.show()