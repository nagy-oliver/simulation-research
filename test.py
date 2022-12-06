#recalculate G for the situation
#change v units
#figure out time flow

import rebound
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

sim = rebound.Simulation()

# unit conversion
PC = 3.08567758E16  # PC to m
MS = 1.989E30       # Ms to kg
sim.G = 6.67E-11    # in m^3 kg^-1 s^-2
sim.dt = 31556926   # timestep of 1 year


# loading data into simulation
with open("data.csv", "r") as fp:
    data = csv.reader(fp)
    m = 0
    # counter = 0
    for i in data:
        # counter += 1
        # if(counter == 10):
        #     break
        if(m==0):
            m = float(i[0])
            continue
        sim.add(m=m*MS, x=float(i[0])*PC, y=float(i[1])*PC, z=float(i[2])*PC, vx=float(i[3])*1000, vy=float(i[4])*1000, vz=float(i[5])*1000)

# integrate in time
data = [[[i.x],[i.y],[i.z]] for i in sim.particles]

# print(sim.calculate_com())
for i in range(100):
    sim.steps(100)
    for j in range(len(sim.particles)):
        data[j][0].append(sim.particles[j].x)
        data[j][1].append(sim.particles[j].y)
        data[j][2].append(sim.particles[j].z)
# print(sim.status())
# print(len(data))
# print(sim.calculate_com())

# show data afterwards
fig = plt.figure()
ax = plt.axes(projection="3d")
for i in data:
    ax.plot3D(i[0], i[1], i[2])
# ax.plot3D(data[500][0], data[500][1], data[500][2])
# ax.plot3D(data[2][0], data[2][1], data[2][2])
plt.show()

# def vel(x, y):
#     return (center[1]-y, x-center[0])
# center = (0, 0)

# center = (0.5, math.sin(math.pi/3)/2)
# coords1 = (0, 0)
# coords2 = (1, 0)
# coords3 = (0.5, math.sin(math.pi/3))

# vel1 = vel(coords1[0], coords1[1])
# vel2 = vel(coords2[0], coords2[1])
# vel3 = vel(coords3[0], coords3[1])

# sim.add(m=2, vx=vel1[0], vy=vel1[1])              
# sim.add(m=1, x=1, vx=vel2[0], vy=vel2[1]) 
# sim.add(m=1, x=math.cos(math.pi/3), y=math.sin(math.pi/3), vx=vel3[0], vy=vel3[1])

# xpos1 = []
# ypos1 = []
# xpos2 = []
# ypos2 = []
# xpos3 = []
# ypos3 = []

# points = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
# vels = [vel(i/2, j/2) for i,j in points]
# pos = [[[], []] for i in range(len(points))]
# for i in range(len(points)):
#     sim.add(m=1, x=points[i][0], y=points[i][1], vx=vels[i][0], vy=vels[i][1])

# print(sim.status())


# for i in range(1, 1000):
#     sim.integrate(i/100)
#     for j in range(len(sim.particles)):
#         pos[j][0].append(sim.particles[j].x*100)
#         pos[j][1].append(sim.particles[j].y*100)
    # for p in sim.particles:
    #     print(p.x, p.y, p.z)
    # xpos1.append(sim.particles[0].x*100)
    # ypos1.append(sim.particles[0].y*100)
    # xpos2.append(sim.particles[1].x*100)
    # ypos2.append(sim.particles[1].y*100)
    # xpos3.append(sim.particles[2].x*100)
    # ypos3.append(sim.particles[2].y*100)



# for o in sim.calculate_orbits():
#     print(o)

# fig, ax = plt.subplots()
# ax.plot(xpos1, ypos1, label="first one")
# ax.plot(xpos2, ypos2)
# ax.plot(xpos3, ypos3)
# for i in pos:
#     ax.plot(i[0], i[1], label="x")
# ax.legend()
# plt.show()

# for p in sim.particles:
#     print(p.x, p.y, p.z)
# for o in sim.calculate_orbits(): 
#     print(o)