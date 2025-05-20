# Task 1 ---------------------

import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque
from scipy import stats

def monteCarloPi(maxIterations,tol):
    inside_pts = 0 # points inside the unit quarter circle
    last_estimate = 0
    current_estimate = 0
    past_diffs = deque(maxlen=5) # queue of the 5 previous differences
    for i in range(1,maxIterations+1):
        rand_x = random.uniform(0, 1)
        rand_y = random.uniform(0, 1)
        
        if rand_x**2 + rand_y**2 <= 1:
            inside_pts += 1
        
        # the ratio of points inside the unit quarter circle to total points should
        # roughly equal the area of the unit quarter circle
        current_estimate = 4*(inside_pts / i) 
        if i != 0:
            past_diffs.append(abs(current_estimate - last_estimate))   

            # only break if we are certain the differences are settling
            if len(past_diffs) == 5 and all(d < tol for d in past_diffs):
                break
        last_estimate = current_estimate

    return current_estimate, i

# Number of iterations for convergence depends on how you 
# define the tolerance, but the method used here needs about 50 
# iterations

estimate, iterations = monteCarloPi(1000,0.02)
print(f"Esimated Pi as {estimate} using {iterations} points")

# now run trials until we are within 1% of pi
err = 1
trials = 0
while err > 0.01:
    estimate, iterations = monteCarloPi(1000,0.02)
    err = abs((estimate - np.pi) / np.pi)
    trials += 1

print(f"Estimated a value of pi of {estimate} after {trials} trials")

# Task 2 -----------------------------------------------------
'''
plt.figure
inside_pts = 0 
last_estimate = 0
current_estimate = 0
tol = 0.005
maxIterations = 5000
past_diffs = deque(maxlen=5) # queue of the 5 previous differences
for i in range(1,maxIterations+1):
    rand_x = random.uniform(-2, 3) # domain of integration
    rand_y = random.uniform(0, 10) # enough to safely capture the range of the function on this domain
    
    col = 'blue'
    if rand_y <= (rand_x**3)*np.sin(rand_x): # if point is inside function
        inside_pts += 1
        col = 'red' 
    plt.scatter(rand_x,rand_y,color=col)
    
    # the ratio of points inside the function to total points should equal 
    # the ratio of area under the curve to total area
    current_estimate = (5*10)*(inside_pts / i) 
    if i != 0:
        past_diffs.append(abs(current_estimate - last_estimate))   

        # only break if we are certain the differences are settling
        if len(past_diffs) == 5 and all(d < tol for d in past_diffs):
            break
    last_estimate = current_estimate

x = np.linspace(-2,3,100)
y = (x**3)*np.sin(x)
plt.plot(x,y,color='black',linewidth=3)
plt.show()
print(f"Estimate using Monte Carlo Integration method: {last_estimate} with {i} points")
'''
# Task 3 -----------------------------------------

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

plt.grid()
plt.scatter(sigma_P,sigma_rho)
# plt.show() <---- uncomment for SUBMISSION

# Task 4 ----------------------------------------------------------------

unit_price = {
    "yearly": [50, 52, 55, 57, 65],
    "min": 50,
    "max": 70,
    "mode": 55
}

unit_sales = {
    "yearly": [2000, 2200, 2700, 2500, 2800],
    "min": 2000,
    "max": 3000,
    "mode": 2400
}

variable_costs = {
    "yearly": [50000, 55000, 56000, 57000, 58000],
    "min": 50000,
    "max": 65000,
    "mode": 55200
}

fixed_costs = {
    "yearly": [10000, 12000, 15000, 16000, 17000],    
    "min": 10000,
    "max": 20000,
    "mode": 14000
}

def draw_triangle_dis(data): # uniformly samples a grid until the result falls into the triangular PDF
    a = data["min"]
    b = data["max"]
    c = data["mode"]

    while True:
        x = random.uniform(a,b)
        y = random.uniform(0, 2/(b-a))

        if a <= x and x <= c:
            pdf_out = (2*(x-a)) / ((b-a)*(c-a))

        elif c <= x and x <= b:
            pdf_out = (2*(b-x))/((b-a)*(b-c))
        else:
            pdf_out = 0
        
        if y <= pdf_out:
            return x
        
n = 10000
earnings_samples = []
var_cost_samples = []
fixed_cost_samples  = []
sales_samples = []
for i in range(1,n):
    price  = draw_triangle_dis(unit_price)
    sales  = draw_triangle_dis(unit_sales)
    var_c  = draw_triangle_dis(variable_costs)
    fix_c  = draw_triangle_dis(fixed_costs)

    earnings = price * sales - (var_c + fix_c)
    earnings_samples.append(earnings)
    var_cost_samples.append(var_c)
    fixed_cost_samples.append(fix_c)
    sales_samples.append(price * sales)


plt.figure()
plt.hist(earnings_samples, bins=70)   
plt.xlabel("Earnings")
plt.ylabel("Frequency")
plt.title("Next‑Year Earnings Predictions using Monte Carlo Simulation")
plt.grid(True)
# plt.show()

theta_hat_n = np.mean(earnings_samples) # samples mean
sigma_hat_n = 0
for sample in earnings_samples:
    sigma_hat_n += (sample - theta_hat_n)**2
sigma_hat_n = np.sqrt((sigma_hat_n)/(n-1))

z = 1.96 # from text, for alpha = 0.05 

L = theta_hat_n - z*(sigma_hat_n/np.sqrt(n))
U = theta_hat_n + z*(sigma_hat_n/np.sqrt(n))

print(f"95% confidence interval for next year's earnings: [{L:.0f}, {U:.0f}]")


plt.figure()
plt.scatter(var_cost_samples,earnings_samples)
plt.show()
