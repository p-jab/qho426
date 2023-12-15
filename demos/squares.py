import matplotlib.pyplot as plt
import matplotlib.animation as a

fig, ax = plt.subplots()

def small():
    x = [3,3,4,4,3]
    y = [3,4,4,3,3]
    ax.plot(x, y, "r:o")

def medium():
    x = [2,2,5,5,2]
    y = [2,5,5,2,2]
    ax.plot(x, y, "g--s")

def large():
    x = [1,1,6,6,1]
    y = [1,6,6,1,1]
    ax.plot(x, y, "b-p")

def animate(frame):
    ax.cla()
    ax.set_xlim(0,7)
    ax.set_ylim(0,7)
    if frame % 3 == 0:
        small()
    elif frame % 3 == 1:
        medium()
    else:
        large()

x = a.FuncAnimation(fig, animate, frames = 3, interval=1000)
plt.show()