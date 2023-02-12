import rebound
import matplotlib.pyplot as plt
import csv
import json
import utils

sim = rebound.Simulation()
sim.G = 6.67E-11    # in m^3 kg^-1 s^-2
# sim.dt = 31556926000   # timestep of 1 year    10000/1000y

# loading data into simulation
with open("data.csv", "r") as fp:
    data = csv.reader(fp)
    for index, i in enumerate(data):
        if(index == 0):
            # load swarm mass from the first line of .csv
            m = float(i[0])
            continue
        if(index == 1):
            # create central black hole
            sim.add(m=float(i[0])*utils.MS)
            continue
        sim.add(m=m*utils.MS, x=float(i[0])*utils.PC, y=float(i[1])*utils.PC, z=float(i[2])*utils.PC, vx=float(i[3])*1000, vy=float(i[4])*1000, vz=float(i[5])*1000)

# integrate in time, log positions into data
data = [[[i.x],[i.y],[i.z],[i.vx],[i.vy],[i.vz]] for i in sim.particles]
# for i in range(100):
#     sim.steps(100)
#     print(i)
#     print(sim.t/315569260000)
#     for j in range(len(sim.particles)):
#         data[j][0].append(sim.particles[j].x)
#         data[j][1].append(sim.particles[j].y)
#         data[j][2].append(sim.particles[j].z)

# Structure of data variable:
# [ swarms
#  [ coordinates of the swarm
#   [x in time],
#   [y],
#   [z]
#  ]
# ]

# save simulation data
with open("data.json", "w") as fp:
    fp.write(json.dumps(data))
sim.save("snapshot.bin")

# display in matplotlib
fig = plt.figure()
ax = plt.axes(projection="3d")
for i in data:
    ax.plot3D(i[0], i[1], i[2])
    ax.scatter3D([i[0][-1] for i in data], [i[1][-1] for i in data], [i[2][-1] for i in data])
plt.show()