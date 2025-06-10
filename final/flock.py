from boids import Boid
import matplotlib.cm   as cm  
import matplotlib.colors as mcolors   

class Flock():
    def __init__(self,cube_size,num_boids = 50):
        self.boids = []

        color_map = cm.get_cmap('viridis',num_boids)
        cols = [mcolors.to_rgb(color_map(i)) for i in range(num_boids)]
        # color gen here
        for i in range(num_boids):
            self.boids.append(Boid(cube_size,col=cols[i]))

    def step(self,ax):
        for boid in self.boids:
            for neighbor in self.boids:
                # apply the boids rules
                pass
            boid.step(ax)

    def draw(self,ax):
        for boid in self.boids:
            boid.draw(ax)