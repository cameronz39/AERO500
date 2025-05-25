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

max_iterations = 100
plt.figure()
for i in range(max_iterations):
    for j in range(len(particles)):
        if ackley(particles[j].p_x,particles[j].p_y) < ackley(g_x,g_y):
            g_x = particles[j].p_x
            g_y = particles[j].p_y

    for particle in particles:
        particle.update_vel(g_x,g_y)
        particle.update_pos()

    if i % 20 == 0:
        plt.clf()
        plot_particles(particles)
        plt.show()
        
















x = np.linspace(-5, 5, 400)
y = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x, y)
Z = ackley(X, Y)

# Plot the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('Ackley Function')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
# plt.show()