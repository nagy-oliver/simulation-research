#visualize initial conditions

import rebound
import matplotlib.pyplot as plt
import csv
import numpy as np


fig = plt.figure(figsize=(9, 6))
#create data for 3d line
xline = np.linspace(0, 15, 1000)
yline = np.sin(xline)
zline = np.cos(xline)
#3d container
ax = plt.axes(projection = '3d')
#3d scatter plot
ax.plot3D(xline, yline, zline)
ax.plot3D(yline, zline, xline)
#give labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()