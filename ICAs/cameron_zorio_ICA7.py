import numpy as np
import scipy
from numpy import linalg
import scipy.linalg

import matplotlib.pyplot as plt
from scipy.integrate import odeint
# Task 1 --------------------------------
A = np.array([[1,3,5],[2, 5, 1],[2, 3, 8]])

rank = linalg.matrix_rank(A)
print(f"The matrix A has a full rank of {rank}")

inv = linalg.inv(A)
print(f"Inverse: \n{inv}")

det = linalg.det(A)
print(f"Determinant: {det:.3f}")

tr = linalg.trace(A)
print(f"Trace: {tr}")

eigval, eigvec = linalg.eig(A)
print(f"Eigenvalues: {eigval}")
print(f"Eigenvectors: \n{eigvec}")

norm = linalg.matrix_norm(A)
print(f"Norm: {norm}")

L,U = scipy.linalg.lu(A,permute_l=True)
print(f"Lower Upper Decomposition: \nL:\n{L}\nU\n{U}")

sing_vals = linalg.svdvals(A)
print(f"Singular Values: {sing_vals}")

b = np.array([[10],[8],[3]])
x = linalg.solve(A,b)

print(f"Solution to Ax = b: \nx = {x}")


# Task 2 --------------------------------

mu = 1

# returns the time-derivative of the system state (x, x_dot) -> (x_dot x_ddot)
def state_dot(t,state):
    x, x_dot = state
    return [x_dot, mu*(1-x**2)*x_dot - x]

t_span = np.linspace(0,10,5000)

plt.figure()

for i in range(-4,5):
    for j in range(-4,5):
        initial_state = [i,j]
        sol = odeint(state_dot,initial_state,t = t_span,tfirst=True)
        plt.plot(sol[:,0],sol[:,1])

plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Van der Pol Oscillator Trajectories")
plt.show()