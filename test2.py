#visualize initial conditions

import rebound
import matplotlib.pyplot as plt
import csv
sim = rebound.Simulation()

with open("data.csv", "r") as fp:
    data = csv.reader(fp)
    m = 0
    for i in data:
        if(m==0):
            m = float(i[0])
            print(m)
            print(type(m))
            continue
        #change velocity units?
        sim.add(m=m, x=float(i[0]), y=float(i[1]), z=float(i[2]))

xdata = [i.x for i in sim.particles]
ydata = [i.y for i in sim.particles]
zdata = [i.z for i in sim.particles]

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.scatter3D(xdata, ydata, zdata)
plt.show()