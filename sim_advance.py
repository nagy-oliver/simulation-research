import rebound
import matplotlib.pyplot as plt
import json

# load the simulation from data
sim = rebound.Simulation("snapshot.bin")
print(sim.t/31556926)
with open("archive/two_mil/data.json", "r") as fp:
    data = json.load(fp)

# pick up and integrate forward
# for i in range(200):
#     print(f"Iteration number {i}")
#     sim.steps(100)  #100/1000
#     for j in range(len(sim.particles)):
#         data[j][0].append(sim.particles[j].x)
#         data[j][1].append(sim.particles[j].y)
#         data[j][2].append(sim.particles[j].z)

# save simulation data
# with open("data.json", "w") as fp:
#     fp.write(json.dumps(data))
# sim.save("snapshot.bin")

# display in matplotlib
fig = plt.figure()
ax = plt.axes(projection="3d")
for i in data:
    ax.plot3D(i[0], i[1], i[2])
    # ax.scatter3D(i[0][0], i[1][0], i[2][0])
plt.show()