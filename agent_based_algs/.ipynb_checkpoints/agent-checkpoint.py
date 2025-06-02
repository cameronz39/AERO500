import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
# jupyter notebook --no-browser --ip=0.0.0.0 --port=8888
class Bird():
    id = 0
    def __init__(self,a,lim_x,lim_y):
        self.id = Bird.id
        Bird.id += 1
        self.a = a # half of a birds wingspan
        self.x = np.array([random.uniform(-lim_x,lim_x),random.uniform(-lim_y,lim_y)])

        self.leader = None
        self.flock_side = None
        
class Flock():
    def __init__(self,size,a,lim_x,lim_y,gamma,FLOCK_Y_SPACING):
        self.birds = []
        self.a = a
        self.gamma = gamma
        self.x_correction = 0.1
        self.y_correction = 0.1
        self.FLOCK_Y_SPACING = FLOCK_Y_SPACING
        
        for i in range(size):
            self.birds.append(Bird(a,lim_x,lim_y))

    def d_nom(self):
        return np.sqrt(1.12**2 + 4 * self.a**2)      
    
    def com(self):
        return np.mean([bird.x[0] for bird in self.birds])

    def plot(self, with_leaders=False):
        plt.figure(figsize=(6, 6))
        for bird in self.birds:
            plt.scatter(*bird.x, color='tab:blue')
            plt.text(*bird.x, f"{bird.id}", fontsize=9,
                     ha='center', va='center', color='white')
            if with_leaders and bird.leader is not None:
                tail = bird.x
                head = bird.leader.x
                plt.plot([tail[0], head[0]], [tail[1], head[1]],
                         'k--', linewidth=0.8)

        plt.gca().set_aspect('equal')
        plt.title("Initial flock with leader-follower links" if with_leaders else "Initial flock")
        plt.grid(True)
        plt.show()
    
    def assign_leaders(self):
        positions = np.array([bird.x for bird in self.birds])  
        y_coords   = positions[:, 1]

        # which birds are on the left/right of the flock
        x_sign    = np.sign(positions[:, 0] - self.com())  
        
        for i, bird in enumerate(self.birds):
            mask_front = y_coords > bird.x[1] 
            mask_side  = x_sign == x_sign[i]

            # only birds in front and on the same side of the flock are valid leaders
            valid_birds = np.where(mask_front & mask_side)[0]


            if valid_birds.size == 0:
                # if none are found, allow birds on same side
                valid_birds = np.where(mask_front)[0]


            if valid_birds.size == 0:        
                # if still none are found, then this bird is the principle leader       
                bird.leader = None                   
                continue

            deltas     = positions[valid_birds] - bird.x
            distances  = np.linalg.norm(deltas, axis=1)

            # pick nearest valid leader
            j = valid_birds[np.argmin(distances)]
            bird.leader = self.birds[j]

    def far_field_correction(self,bird):
        # applies the B and F matricies to each bird
        if bird.leader is None:
            return np.zeros(2)
    
        dx, dy = bird.leader.x - bird.x

        # don't overshoot the leader
        if dy <= 0:
            return np.array([0,-self.y_correction])
        
        # stay to the correct left/right side of the flock
        if abs(dx) < bird.a:    
            direction = 1.0 if bird.x[0] > self.com() else -1.0
            return np.array([direction * self.x_correction,0])
        
        return np.zeros(2)
        
    def step(self):
        self.assign_leaders()

        for bird in self.birds:
            if bird.leader is None:
                continue
            r = bird.leader.x - bird.x
            
            if np.linalg.norm(r) > self.d_nom(): # far-field update
                bird.x += self.gamma * r 
                bird.x += self.far_field_correction(bird)
                continue
            else: # near-field update
                if bird.flock_side is None:
                    # bird.flock_side = np.sign(bird.x[0] - bird.leader.x[0]) or 1.0
                    bird.flock_side = np.sign(bird.x[0] - self.com()) or 1.0
                r_des = np.array([bird.flock_side*2*self.a,-self.FLOCK_Y_SPACING])
                S = r_des - r
                bird.x += self.gamma * S

                
a = 0.5
numBirds = 20
gamma = 0.03
lim_x = 10
lim_y = 10
steps  = 500
FLOCK_Y_SPACING = 1.12
flock = Flock(numBirds,a,lim_x,lim_y,gamma,FLOCK_Y_SPACING)

fig, ax = plt.subplots(figsize=(6,6))
ax.set_xlim(-lim_x-5, lim_x+5)
ax.set_ylim(-lim_y, lim_y)
ax.set_aspect('equal')
ax.grid(True)

scatter = ax.scatter([b.x[0] for b in flock.birds],
                     [b.x[1] for b in flock.birds])

def init():
    scatter.set_offsets([[b.x[0], b.x[1]] for b in flock.birds])
    return scatter,

def update(frame):
    flock.step()
    scatter.set_offsets([[b.x[0], b.x[1]] for b in flock.birds])
    ax.set_title(f"t = {frame}")
    return scatter,

ani = FuncAnimation(fig, update, frames=steps, init_func=init,
                    interval=80, blit=True)

gif_path = "flock_sim.gif"
ani.save(gif_path, writer=PillowWriter(fps=18))
print(f"Saved animation to {gif_path}")