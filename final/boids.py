import numpy as np
from pytransform3d import plot_utils
from scipy.spatial.transform import Rotation as R
from utils import projectSphere

class Boid():
    def __init__(self,cube_size):
        self.pos = np.asarray([0.0,1,0.0])
        self.vel = np.asarray([0.8, 0.2, 0.3])
        self.cube_size = cube_size

    def step(self,ax):
        detected, x_out, y_out, z_out = self.detectBounds(ax,detectRange=5,plotFlag=True)
        acc = np.asarray([0.0, 0.0, 0.0])
        if detected:
            push = (np.asarray([-x_out,-y_out,-z_out]))*0.05
            acc += push


        # ax.quiver(self.pos[0],self.pos[1],self.pos[2],-x_out,-y_out,-z_out)


        self.pos += self.vel
        self.vel += acc

    def draw(self,ax):
        # ax.quiver(self.pos[0],self.pos[1],self.pos[2],self.vel[0],self.vel[1],self.vel[2])
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

        plot_utils.plot_cone(ax,height=2,radius=1,A2B=transform,wireframe=False,alpha=0.70,color='orange')

    def detectBounds(self,ax,plotFlag=False,detectRange=1):
        x, y, z = projectSphere(10)
        x = x*detectRange + self.pos[0]
        y = y*detectRange + self.pos[1]
        z = z*detectRange + self.pos[2]

        mean_x = []
        mean_y = []
        mean_z = []

        for i in range(len(x)):
            if abs(x[i]) > self.cube_size or abs(y[i]) > self.cube_size or abs(z[i]) > self.cube_size:
                if plotFlag: ax.scatter(x[i],y[i],z[i],color='red')
                mean_x.append(x[i])
                mean_y.append(y[i])
                mean_z.append(z[i])
            else:
                if plotFlag: ax.scatter(x[i],y[i],z[i],color='blue')
                continue

        if mean_x:
            return True, np.mean(mean_x), np.mean(mean_y), np.mean(mean_z)
        else:
            return False, None, None, None
