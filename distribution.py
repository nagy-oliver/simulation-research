import math
import random
import csv

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

print("Generating data successful")