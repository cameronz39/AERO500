from utils import plotBounds
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from flock import Flock
from boids import Boid
import numpy as np


CUBE_SIZE = 25
NUM_FRAMES = 600 # Number of animation frames
FLOCK_SIZE = 100
NEIGHBOR_DIST = 15
CROWD_DIST = 1.0

SEP_WEIGHT = 0.5
ALIGN_WEIGHT = 0.012
COH_WEIGHT = 0.003
HAWK_WEIGHT = 10.0
# Initialize the hawk
hawk = Boid(CUBE_SIZE,col='red',isHawk=True)

# Initialize the flock
flck = Flock(CUBE_SIZE,num_boids=FLOCK_SIZE,hawk=hawk,crowd_dist=CROWD_DIST,neigh_dist=NEIGHBOR_DIST,
             sep_weight=SEP_WEIGHT,align_weight=ALIGN_WEIGHT,coh_weight=COH_WEIGHT,hawk_weight=HAWK_WEIGHT)



def update(frame, flck, ax):
    ax.clear()
    plotBounds(ax, CUBE_SIZE, col='midnightblue', thickness=1)

     # Update boid position and draw
    flck.step(ax)
    flck.draw(ax)
    hawk.step(ax,prey=flck.boids[0])
    hawk.draw(ax)

    # Set consistent viewing angles and limits
    ax.set_xlim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_ylim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_zlim(-CUBE_SIZE, CUBE_SIZE)
    return ax



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