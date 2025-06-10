from utils import plotBounds
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from boids import Boid
from flock import Flock
import numpy as np


CUBE_SIZE = 15
NUM_FRAMES = 200  # Number of animation frames
FLOCK_SIZE = 1

def update(frame, flck, ax):
    ax.clear()
    plotBounds(ax, CUBE_SIZE, col='midnightblue', thickness=1)

     # Update boid position and draw
    flck.step(ax)
    flck.draw(ax)

    # Set consistent viewing angles and limits
    ax.set_xlim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_ylim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_zlim(-CUBE_SIZE, CUBE_SIZE)
    return ax

# Initialize the boid
flck = Flock(CUBE_SIZE,num_boids=FLOCK_SIZE)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the animation
anim = FuncAnimation(
    fig, 
    update, 
    frames=NUM_FRAMES,
    fargs=(flck, ax),
    interval=50,  # Time between frames in milliseconds
    blit=False
)

gif_path = 'boid_animation.gif'
anim.save(gif_path, writer=PillowWriter(fps=18))
print(f"Saved animation to {gif_path}")