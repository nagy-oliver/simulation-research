import rebound
import matplotlib.pyplot as plt
import json

import utils

# load the simulation from data
sim = rebound.Simulation("snapshot.bin")
print(sim.t/31556926)
with open("data.json", "r") as fp:
    data = json.load(fp)

# pick up and integrate forward
# for i in range(2000):
#     print(f"Iteration number {i}")
#     print(f"Simulation time: {sim.t/utils.YR}")
#     print(f"Simulation timestep: {sim.dt/utils.YR}")
#     # sim.steps(100)  #100/1000
#     sim.integrate(sim.t + 1000*utils.YR)
    
#     for j in range(len(sim.particles)):
#         data[j][0].append(sim.particles[j].x)
#         data[j][1].append(sim.particles[j].y)
#         data[j][2].append(sim.particles[j].z)
#         data[j][3].append(sim.particles[j].vx)
#         data[j][4].append(sim.particles[j].vy)
#         data[j][5].append(sim.particles[j].vz)

# save simulation data
# with open("data.json", "w") as fp:
#     fp.write(json.dumps(data))
# sim.save("snapshot.bin")

data_dil = [[j[::100] for j in data[index]] for (index, i) in enumerate(data)]
print("diluted")
# display in matplotlib
fig = plt.figure()
print("works")
ax = plt.axes(projection="3d")
for i in data_dil:
    ax.plot3D(i[0], i[1], i[2])
    ax.scatter3D(i[0][0], i[1][0], i[2][0])
plt.show()