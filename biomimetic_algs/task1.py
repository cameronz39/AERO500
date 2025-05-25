import numpy as np
import random
import matplotlib.pyplot as plt
np.set_printoptions(legacy='1.25')

# distance from node i to node j is dist[i][j]
d_0 = np.array([[0, 10, 12, 11, 14], 
                 [10, 0, 13, 15, 8], 
                 [12, 13, 0, 9, 14], 
                 [11, 15, 9, 0, 16], 
                 [14, 8, 14, 16, 0]]) # inital distance matrix

# initial pheremone matrix
tau = np.ones((5,5))

alpha = 1
beta = 2
rho = 0.5

class Ant():
    def __init__(self):
        self.M = [0, 1, 2, 3, 4] # valid nodes the ant may travel to
        self.path = []
        self.p = [0, 0, 0, 0, 0]
        self.d = d_0
        self.tot_dist = 0

        self.r = random.choice(self.M) # starting node randomly selected
        self.M.remove(self.r)
        self.path.append(self.r)

        self.eta = np.ones((5,5))
        self.update_eta(self.M)

    def update_eta(self, M):
        # takes the reciprocal of each element in M, skipping zeros
        for i in range(self.d.shape[0]):
            for j in range(self.d.shape[1]):
                if self.d[i,j] != 0:
                    self.eta[i][j] = 1 / self.d[i][j]
                else:
                    self.eta[i][j] = 0

        for i in range(self.d.shape[0]):
            if i not in self.M:
                self.eta[:,i] = 0

    def choose_next_node(self,tau):
        self.p = [0, 0, 0, 0, 0]
        denom = sum((tau[self.r,s]**alpha)*(self.eta[self.r,s]**beta) for s in self.M)
        for s in self.M: # for each node s the ant may travel to
            self.p[s] = (tau[self.r,s]**alpha) * (self.eta[self.r,s]**beta) / denom

        # print(f"Probabilites: \n{self.p}")
        # choose next node based off calculated probabilities
        next_node = np.random.choice(len(self.p), p = self.p) 
        # update the path
        self.path.append(next_node)
        # update the distance travelled
        self.tot_dist += self.d[self.r,next_node]
        # remove the chosen node from M and the probabilites
        self.M.remove(next_node)
        self.p[next_node] = 0
        # update the eta matrix (sets the col to zero like in lecture)
        self.update_eta(self.M)
        # print(f"Traveling to node {next_node} and covering a distance of {self.d[self.r,next_node]}")
        self.r = next_node # current node = next node

    def travel(self,tau):
        print(f"Starting at node: {self.r}")
        while self.M:
            self.choose_next_node(tau)
        self.tot_dist += self.d[self.path[-1],self.path[0]]
        # print(f"Completing loop now by travelling: {self.d[self.path[-1],self.path[0]]} back to {self.path[0]}")
        self.path.append(self.path[0])
        
        print("Completed journey!")
        print(self.path)
        print(self.tot_dist)

    def update_pheromone(self,tau):
        new_pheromone = np.zeros((5,5))
        # print(f"laying {1/self.tot_dist}")
        for i in range(len(self.path)-1):
            frm = self.path[i]
            to = self.path[i+1]
            new_pheromone[frm,to] += 1/self.tot_dist

        tau += new_pheromone

num_iterations = 40
distances = np.zeros((num_iterations,3))
for i in range(num_iterations):
    # randomly seed ants
    ant_0 = Ant()
    ant_1 = Ant()
    ant_2 = Ant()

    ant_0.travel(tau)
    ant_1.travel(tau)
    ant_2.travel(tau)

    # pheromone decay
    tau *= (1-rho)

    # pheromone update
    ant_0.update_pheromone(tau)
    ant_1.update_pheromone(tau)
    ant_2.update_pheromone(tau)

    # log data
    distances[i,0] = ant_0.tot_dist
    distances[i,1] = ant_1.tot_dist
    distances[i,2] = ant_2.tot_dist

plt.figure()
plt.plot(distances[:,0],label='Ant 0')
plt.plot(distances[:,1],label='Ant 1')
plt.plot(distances[:,2],label='Ant 2')
plt.title("Ants converging to 1 solution")
plt.grid()
plt.legend()
plt.xlabel("Iteration number")
plt.ylabel("Distance Travelled")
plt.show()



    




