import rebound
import json
import math
import random
import csv
import matplotlib.pyplot as plt
import utils

### Create distribution of matter, save as CSV

N = 1000      #number of swarms
M = 10**6     #Sun masses
R = 10        #PC
a = 0.6*R     #unit of R
m = M/N       #units of M, swarm mass
spheres = 20  #number of spheres to iterate through, experimental, dimensionless

swarms = []
class Swarm:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
    def __str__(self):
        return f"{round(self.x, 3)} {round(self.y, 3)} {round(self.z, 3)}    {round(self.vx, 3)} {round(self.vy, 3)} {round(self.vz, 3)}    {math.sqrt(self.x**2+self.y**2+self.z**2)} {math.sqrt(self.vx**2+self.vy**2+self.vz**2)}"

def density(r):     #unit of mass/R^3
    return 3*M/(4*math.pi*a**3*(1+r**2/a**2)**(5/2))

def velocity(r):
    v = (1-r/(R+0.5))*15    #in km/s; r,R in PC
    vx = random.uniform(0, v)
    vy = random.uniform(0, math.sqrt(v**2-vx**2))
    vz = math.sqrt(v**2-vx**2-vy**2)
    return vx, vy, vz

for i in range(spheres):
    #find the distance of the sphere from the center
    radius = (R/spheres)*(i+1) #unit of R
    #calculate point density of the sphere
    den = density(radius)
    #find the number of swarms to add
    num = round(den*4*math.pi*radius**2*R/spheres/m)
    #add the swarms
    for j in range(num):
        x = random.uniform(0, radius)
        y = random.uniform(0, math.sqrt(radius**2-x**2))
        z = math.sqrt(radius**2-x**2-y**2)
        x *= [-1,1][random.randrange(2)]
        y *= [-1,1][random.randrange(2)]
        z *= [-1,1][random.randrange(2)]
        vx, vy, vz = velocity(radius)
        swarms.append(Swarm(x, y, z, vx, vy, vz))

# for i in swarms:
#     print(i)
# print(f"Mass should be {M}, it is {len(swarms)*m}, meaning {M/len(swarms)/m} ratio")

# add data to data.csv
with open("data.csv", "w") as fp:
    writer = csv.writer(fp)
    writer.writerow([m])
    for i in swarms:
        writer.writerow([i.x, i.y, i.z, i.vx, i.vy, i.vz])


### Load simulation from CSV

sim = rebound.Simulation()
sim.G = utils.G
sim.dt = 1000*utils.YR

with open("data.csv", "r") as fp:
    data = csv.reader(fp)
    m = 0
    for i in data:
        if(m==0):
            # load mass from the first line of .csv
            m = float(i[0])
            continue
        sim.add(m=m*utils.MS, x=float(i[0])*utils.PC, y=float(i[1])*utils.PC, z=float(i[2])*utils.PC, vx=float(i[3])*1000, vy=float(i[4])*1000, vz=float(i[5])*1000)

data = [[[i.x],[i.y],[i.z],[i.vx],[i.vy],[i.vz]] for i in sim.particles]


### Infinite loop to integrate the simulation

while(1):
    for i in range(100):
        # integrate by 1000 years
        sim.integrate(sim.t+1000*utils.YR)
        print(i)
        # log particle positions and velocities
        for j in range(len(sim.particles)):
            data[j][0].append(sim.particles[j].x)
            data[j][1].append(sim.particles[j].y)
            data[j][2].append(sim.particles[j].z)
            data[j][3].append(sim.particles[j].vx)
            data[j][4].append(sim.particles[j].vy)
            data[j][5].append(sim.particles[j].vz)
    # save simulation data
    with open("data.json", "w") as fp:
        fp.write(json.dumps(data))
    sim.save("snapshot.bin")