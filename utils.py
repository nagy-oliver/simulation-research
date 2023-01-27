# unit conversion
PC = 3.08567758E16  # PC to m
MS = 1.989E30       # Ms to kg
YR = 31556926       # Yr to s
G  = 6.67E-11       # G in SI units

def radial(x, y, z, vx, vy, vz):
    #radial velocity
    return (x*vx+y*vy+z*vz)/(x**2+y**2+z**2)**0.5

def tangential(x, y, z, vx, vy, vz):
    return ((vx**2+vy**2+vz**2)**2-radial(x, y, z, vx, vy, vz)**2)**0.5