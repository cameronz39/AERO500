from boids import Boid
import matplotlib.cm   as cm  
import matplotlib.colors as mcolors   
import numpy as np

class Flock():
    def __init__(self,cube_size,num_boids = 50,hawk=None,neigh_dist=5,crowd_dist=2,
                 sep_weight=1.5,coh_weight=1.0,align_weight=0.8,hawk_weight=0.5):
        
        self.boids = []

        color_map = cm.get_cmap('viridis',num_boids)
        cols = [mcolors.to_rgb(color_map(i)) for i in range(num_boids)]
        # color gen here
        for i in range(num_boids):
            self.boids.append(Boid(cube_size,col=cols[i]))

        self.neigh_dist = neigh_dist
        self.crowd_dist = crowd_dist
        self.sep_weight = sep_weight
        self.coh_weight = coh_weight
        self.align_weight = align_weight
        self.hawk_weight = hawk_weight
        self.hawk = hawk

    def step(self,ax):
        # save pos and vel of each boid in the flock
        pos = np.array([boid.pos for boid in self.boids])
        vel = np.array([boid.vel for boid in self.boids])

        for i, boid in enumerate(self.boids):
            diff = pos - boid.pos    
            dist = np.linalg.norm(diff, axis=1) # distance of this boid to every other boid
            mask = (dist > 0) & (dist < self.neigh_dist)
            if not np.any(mask):  # no neighbors, no steering vector needed
                boid.step(ax)
                continue

            # filter out boids that are far away
            neigh_pos = pos[mask]
            neigh_vel = vel[mask]
            neigh_diff = diff[mask]
            neigh_dist = dist[mask]

            boid.num_neighbors.append(np.size(neigh_pos))

            # evade the hawk
            evade_corr = np.zeros(3)
            if self.hawk is not None and not boid.isHawk:
                delta = boid.pos - self.hawk.pos
                dist     = np.linalg.norm(delta)

                # inverse-square push
                push = (1.0 / max(dist**2, 1e-6))
                evade_corr = delta / max(dist, 1e-6) * push 
    
            # finally apply the three rules of boids

            # Seperation: avoid crowding -----------------------------------------------
            crowd_mask = neigh_dist < self.crowd_dist
            sep_correction = np.zeros(3)
            if np.any(crowd_mask):
                crowd_diff = neigh_diff[crowd_mask] # now only considering very close boids
                inv_sqr_term = 1.0 / (neigh_dist[crowd_mask]**2)[:,None]
                sep_correction = np.sum(crowd_diff * inv_sqr_term,axis=0)

            # Alignment: steer to align velocites with neighboring boid's velocities ----
            unit_headings = neigh_vel / np.linalg.norm(neigh_vel, axis=1, keepdims=True)

            if unit_headings.size:
                mean_heading = unit_headings.mean(axis=0)
                mean_heading /= np.linalg.norm(mean_heading)           # normalize
                desired_vel  = mean_heading * boid.maxSpeed            
                align_correction   = desired_vel - boid.vel
            else:
                align_correction = np.zeros(3)

            # Cohesion: stter toward center of mass -----------------------------------------
            center = np.mean(neigh_pos,axis=0)
            coh_correction = center - boid.pos

            steer = (self.sep_weight * sep_correction +
                     self.align_weight * align_correction +
                     self.coh_weight * coh_correction +
                     self.hawk_weight * evade_corr)
            
            boid.step(ax,steer)


    def draw(self,ax):
        for boid in self.boids:
            boid.draw(ax)