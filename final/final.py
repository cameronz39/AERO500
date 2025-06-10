from utils import plotBounds
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from boids import Boid


CUBE_SIZE = 15
NUM_FRAMES = 100  # Number of animation frames

def update(frame, boid, ax):
    ax.clear()
    plotBounds(ax, CUBE_SIZE, col='midnightblue', thickness=1)

     # Update boid position and draw
    boid.step(ax)
    boid.draw(ax)

    # Set consistent viewing angles and limits
    ax.set_xlim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_ylim(-CUBE_SIZE, CUBE_SIZE)
    ax.set_zlim(-CUBE_SIZE, CUBE_SIZE)
    ax.view_init(elev=30, azim=frame)  # Rotate view for better visualization
    
    return ax

# Initialize the boid
test_boid = Boid(CUBE_SIZE)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Create the animation
anim = FuncAnimation(
    fig, 
    update, 
    frames=NUM_FRAMES,
    fargs=(test_boid, ax),
    interval=50,  # Time between frames in milliseconds
    blit=False
)

gif_path = 'boid_animation.gif'
anim.save(gif_path, writer=PillowWriter(fps=18))
print(f"Saved animation to {gif_path}")