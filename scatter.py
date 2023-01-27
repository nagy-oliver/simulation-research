import json
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open("archive/two_mil/data.json", "r") as fp:
    data = json.load(fp)

fig = plt.figure()
ax = plt.axes(projection="3d")

def update_plot(j):
    ax.clear()
    ax.scatter3D([i[0][j-1] for i in data], [i[1][j-1] for i in data], [i[2][j-1] for i in data])
    print(j)

# Set up the animation
# ani = animation.FuncAnimation(fig, update_plot, frames=2000, interval=10)
# ani.save('animation.mp4')
plt.show()