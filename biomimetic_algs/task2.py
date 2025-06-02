import numpy as np
import matplotlib.pyplot as plt
import random
# create uniform particle distribution to start


def ackley(x,y):
    d = 2
    a = 20
    b = 0.2
    c = 2*np.pi

    sqrt_block = -b*np.sqrt((1/d)*(x**2 + y**2)) 
    cos_block = ((1/d)*(np.cos(c*x) + np.cos(c*y)))

    return -a*np.exp(sqrt_block) - np.exp(cos_block) + a + np.exp(1)

phi_p = 1 # cognitive coefficient
phi_g = 1 # social coefficient
w = .8 # particle "inertia"

class Particle():
    def __init__(self,x,y,vel_bound):
        self.x = x
        self.y = y

        self.v_x = random.uniform(-vel_bound,vel_bound)
        self.v_y = random.uniform(-vel_bound,vel_bound)

        # best known position of the particle
        self.p_x = x 
        self.p_y = y
        
    def update_vel(self,g_x,g_y):
        r_p = random.uniform(0,1)
        r_g = random.uniform(0,1)
        self.v_x = w*self.v_x + phi_p*r_p*(self.p_x - self.x) + phi_g*r_g*(g_x - self.x)

        r_p = random.uniform(0,1)
        r_g = random.uniform(0,1)
        self.v_y = w*self.v_y + phi_p*r_p*(self.p_y - self.y) + phi_g*r_g*(g_y - self.y)

    def update_pos(self):
        self.x += self.v_x
        self.y += self.v_y

        if ackley(self.x,self.y) < ackley(self.p_x,self.p_y):
            self.p_x = self.x
            self.p_y = self.y

def plot_particles(particles):
    particle: Particle
    for particle in particles:
        plt.scatter(particle.x,particle.y,color='blue')


S = 20
particles = []
for s in range(S):
    x = random.uniform(-5,5)
    y = random.uniform(-5,5)
    particles.append(Particle(x,y,2))

g_x = particles[0].p_x
g_y = particles[0].p_y

max_iterations = 50

pos_x_history = np.zeros((max_iterations, S))
pos_y_history = np.zeros((max_iterations, S))

for i in range(max_iterations):
    for j in range(len(particles)):
        if ackley(particles[j].p_x,particles[j].p_y) < ackley(g_x,g_y):
            g_x = particles[j].p_x
            g_y = particles[j].p_y

    for j, particle in enumerate(particles):
        particle.update_vel(g_x,g_y)
        particle.update_pos()

        pos_x_history[i,j] = particle.x
        pos_y_history[i,j] = particle.y
        




x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)

fig, axs = plt.subplots(2,2, figsize = (8,6))

fig.suptitle('Swarm positions over time')

axs[0,0].contourf(X,Y,Z, levels=20, cmap = 'viridis')
axs[0,0].scatter(pos_x_history[0,:],pos_y_history[0,:],color='darkorange',edgecolors='black')
axs[0,0].set_xlim(-4,4)
axs[0,0].set_ylim(-4,4)
axs[0,0].set_title('1 iterations')
axs[0,0].grid(True)

axs[0,1].contourf(X,Y,Z, levels=20, cmap = 'viridis')
axs[0,1].scatter(pos_x_history[10,:],pos_y_history[10,:],color='darkorange',edgecolors='black')
axs[0,1].set_xlim(-4,4)
axs[0,1].set_ylim(-4,4)
axs[0,1].set_title('10 iterations')
axs[0,1].grid(True)

axs[1,0].contourf(X,Y,Z, levels=20, cmap = 'viridis')
axs[1,0].scatter(pos_x_history[30,:],pos_y_history[30,:],color='darkorange',edgecolors='black')
axs[1,0].set_xlim(-4,4)
axs[1,0].set_ylim(-4,4)
axs[1,0].set_title('30 iterations')
axs[1,0].grid(True)

axs[1,1].contourf(X,Y,Z, levels=20, cmap = 'viridis')
axs[1,1].scatter(pos_x_history[-1,:],pos_y_history[-1,:],color='darkorange',edgecolors='black')
axs[1,1].set_xlim(-4,4)
axs[1,1].set_ylim(-4,4)
axs[1,1].set_title('50 iterations')
axs[1,1].grid(True)

plt.show()

