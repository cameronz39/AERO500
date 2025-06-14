import numpy as np
from pytransform3d import plot_utils
from scipy.spatial.transform import Rotation as R
from utils import projectSphere
import random

class Boid():
    def __init__(self,cube_size,col,maxSpeed = 1.1,isHawk = False):
        self.pos = np.asarray([random.uniform(-cube_size,cube_size),
                               random.uniform(-cube_size,cube_size),
                               random.uniform(-cube_size,cube_size)])
        
        self.vel = np.asarray([random.uniform(-maxSpeed,maxSpeed),
                               random.uniform(-maxSpeed,maxSpeed),
                               random.uniform(-maxSpeed,maxSpeed)])
        self.cube_size = cube_size
        self.maxSpeed = maxSpeed

        self.boid_col = col
        self.isHawk = isHawk
        if isHawk: 
            self.maxSpeed = 0.6
        
        self.num_neighbors = []

    def step(self,ax, steering=np.zeros(3), prey = None):
        detected, x_out, y_out, z_out, pts_detected = self.detectBounds(ax,detectRange=6,plotFlag=False)
        acc = np.zeros(3)
        if not self.isHawk:
            steering = np.asarray(steering).reshape(3,)
            acc = steering.copy()

        if detected:
            boundary_push = pts_detected * (np.asarray([-x_out,-y_out,-z_out]))*0.0005
            acc += boundary_push
        elif np.linalg.norm(self.vel) > self.maxSpeed:
            self.vel *= self.maxSpeed / np.linalg.norm(self.vel)

        if self.isHawk and prey is not None:
            chase_vec = prey.pos - self.pos
            future_prey_pos = prey.pos + prey.vel * 2.5

            desired = future_prey_pos - self.pos
            desired = desired / np.linalg.norm(desired) * self.maxSpeed
            pursue = desired - self.vel

            miss_factor = 0.6
            acc += miss_factor*pursue

        self.vel += acc
        self.pos += self.vel


    def draw(self,ax):
        world_dir = self.vel / np.linalg.norm(self.vel)
        body_dir = [0, 0, 1]
        axis = np.cross(body_dir,world_dir) 
        angle = np.clip(np.arccos(np.dot(world_dir,body_dir)), -np.pi, np.pi)

        # if the cross product norm is very small, go into edge case to avoid divide by 0
        if np.linalg.norm(axis) < 1e-9: 
            if self.vel[2] > 0: # velocity is approximately [0, 0, 1] in world frame
                C = np.eye(3) 
            else: # velocity is apporximately [0, 0, -1]
                C = np.asarray([[-1, 0, 0],[0,1,0],[0,0,-1]])
        else:
            axis /= np.linalg.norm(np.cross(body_dir,world_dir))
            C = R.from_rotvec(angle*axis).as_matrix()

        transform = np.eye(4)
        transform[:3,:3] = C
        transform[:3,3] = self.pos - self.vel

        plot_utils.plot_cone(ax,height=2,radius=1,A2B=transform,wireframe=False,alpha=0.70,color=self.boid_col)

        h = 2
        r = 1
        if self.isHawk:
            h = 3
            r = 1.5

        plot_utils.plot_cone(ax,height=h,radius=r,A2B=transform,wireframe=False,alpha=0.70,color=self.boid_col)

    def detectBounds(self,ax,plotFlag=False,detectRange=1):
        num_pts = 40
        x, y, z = projectSphere(num_pts)
        x = x*detectRange + self.pos[0]
        y = y*detectRange + self.pos[1]
        z = z*detectRange + self.pos[2]

        mean_x = []
        mean_y = []
        mean_z = []

        pts_detected = 0
        for i in range(len(x)):
            if abs(x[i]) > self.cube_size or abs(y[i]) > self.cube_size or abs(z[i]) > self.cube_size:
                if plotFlag: ax.scatter(x[i],y[i],z[i],color='red')
                mean_x.append(x[i])
                mean_y.append(y[i])
                mean_z.append(z[i])
                pts_detected += 1
            else:
                if plotFlag: ax.scatter(x[i],y[i],z[i],color='blue')
                continue

        if mean_x:
            return True, np.mean(mean_x), np.mean(mean_y), np.mean(mean_z), pts_detected
        else:
            return False, None, None, None, None
