import rebound
import matplotlib.pyplot as plt
import csv
import json

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
    for i in data:
        if(m==0):
            # load mass from the first line of .csv
            m = float(i[0])
            continue
        sim.add(m=m*MS, x=float(i[0])*PC, y=float(i[1])*PC, z=float(i[2])*PC, vx=float(i[3])*1000, vy=float(i[4])*1000, vz=float(i[5])*1000)

# integrate in time, log positions into data
data = [[[i.x],[i.y],[i.z]] for i in sim.particles]
for i in range(100):
    sim.steps(100)
    for j in range(len(sim.particles)):
        data[j][0].append(sim.particles[j].x)
        data[j][1].append(sim.particles[j].y)
        data[j][2].append(sim.particles[j].z)

# save simulation data
with open("data.json", "w") as fp:
    fp.write(json.dumps(data))
sim.save("snapshot.bin")

# display in matplotlib
fig = plt.figure()
ax = plt.axes(projection="3d")
for i in data:
    ax.plot3D(i[0], i[1], i[2])
plt.show()