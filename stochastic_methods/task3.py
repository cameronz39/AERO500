import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

R = 287.053
T_0 = 288.15 
rho_0 = 1.225

P_0 = rho_0*R*T_0

P_1_ideal = 104847
T_1_ideal = 298.15

rho_ideal = P_1_ideal / (R*T_1_ideal)

P_1_dev = 52
sigma_T = .2


rho_meas = []

# first analytically calculate the error
rho_dev = np.sqrt( ((1/(R*T_1_ideal)**2) * P_1_dev**2)   +  (((P_1_ideal*sigma_T)/(R*T_1_ideal**2))**2)  )
print(f"Analytically calculated error: +/- {rho_dev:.6f}")

# now estimate the error with a Monte Carlo simulation
iterations = 1000
for i in range(1,iterations):
    P = np.random.normal(loc = P_1_ideal, scale = P_1_dev)
    T = np.random.normal(loc = T_1_ideal,scale = sigma_T)
    rho = P / (R*T)
    rho_meas.append(rho)

print(f"Monte Carlo results with {iterations} iterations: 1 Std Dev error: +/- {np.std(rho_meas):.6f}")
    
# repeat with varying error in the pressure meausurement
sigma_P = []
sigma_rho = []
for i in range(1,17):
    iterations = 1000
    sigma_P.append(i*50)
    rho_meas = []
    for j in range(1,iterations):
        P = np.random.normal(loc = P_1_ideal, scale = sigma_P[-1])
        T = np.random.normal(loc = T_1_ideal,scale = sigma_T)
        rho = P / (R*T)
        rho_meas.append(rho)
    sigma_rho.append(np.std(rho_meas))

plt.title("Error in Density with Varying Error in Pressure")
plt.xlabel("Error in Pressure [Pa]")
plt.ylabel("Error in Density [kg/m^3]")
plt.grid()
plt.scatter(sigma_P,sigma_rho)
plt.show()