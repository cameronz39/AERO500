# Task 1 ---------------------

import random
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

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
print(f"Esimated Pi as {estimate} using {iterations} iterations")

# now run trials until we are within 1% of pi
err = 1
trials = 0
while err > 0.01:
    estimate, iterations = monteCarloPi(1000,0.02)
    err = abs((estimate - np.pi) / np.pi)
    trials += 1

print(f"Estimated a value of pi of {estimate} after {trials} trials")

# Task 2