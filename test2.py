import rebound
import matplotlib.pyplot as plt
sim = rebound.Simulation()

sim.add(m=1)
sim.add(m=1, x=1, y=0)
sim.add(m=1, x=0.6, y=1.3)
# sim.add(m=1, x=0, y=1)
print(sim.status())

x1 = []
x2 = []
x3 = []
x4 = []
y1 = []
y2 = []
y3 = []
y4 = []


for i in range(1000):
    sim.integrate(i/100)
    x1.append(sim.particles[0].x)
    x2.append(sim.particles[1].x)
    x3.append(sim.particles[2].x)
    # x4.append(sim.particles[3].x)
    y1.append(sim.particles[0].y)
    y2.append(sim.particles[1].y)
    y3.append(sim.particles[2].y)
    # y4.append(sim.particles[3].y)
    print(sim.status())

fig, ax = plt.subplots()
ax.plot(x1, y1, label="1")
ax.plot(x2, y2, label="2")
ax.plot(x3, y3, label="3")
# ax.plot(x4, y4, label="4")
ax.legend()
plt.show()